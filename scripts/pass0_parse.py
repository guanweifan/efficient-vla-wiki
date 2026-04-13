#!/home/guanweifan/efficient-vla-wiki/.venv/bin/python
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw"
EXTRACTS_DIR = ROOT / "extracts"
PARSES_DIR = EXTRACTS_DIR / "parses"
STATUS_PATH = EXTRACTS_DIR / "pass0_status.json"
INDEX_PATH = EXTRACTS_DIR / "pass0_index.jsonl"

VENV_BIN = ROOT / ".venv" / "bin"
TOOLS = {
    "python": VENV_BIN / "python",
    "pdfinfo": shutil.which("pdfinfo") or "pdfinfo",
    "pdftotext": shutil.which("pdftotext") or "pdftotext",
}

STATUS_LOCK = threading.Lock()
INDEX_LOCK = threading.Lock()


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def ensure_dirs() -> None:
    PARSES_DIR.mkdir(parents=True, exist_ok=True)


def iter_pdfs() -> list[Path]:
    return sorted(RAW_DIR.glob("*.pdf"), key=lambda p: p.stem)


def verify_tools() -> None:
    missing = [name for name, tool in TOOLS.items() if not tool or not Path(str(tool)).exists() and shutil.which(str(tool)) is None]
    if missing:
        raise SystemExit(f"Missing tools: {', '.join(missing)}")


def run_command(
    cmd: list[str],
    stdout_path: Path | None = None,
    stderr_path: Path | None = None,
    cwd: Path | None = None,
) -> tuple[int, str]:
    cwd = cwd or ROOT
    if stdout_path is None and stderr_path is None:
        proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
        out = (proc.stdout or "") + (proc.stderr or "")
        return proc.returncode, out

    stdout_handle = stdout_path.open("w", encoding="utf-8") if stdout_path else subprocess.DEVNULL
    stderr_handle = stderr_path.open("w", encoding="utf-8") if stderr_path else subprocess.DEVNULL
    try:
        proc = subprocess.run(cmd, cwd=cwd, stdout=stdout_handle, stderr=stderr_handle, text=True)
        return proc.returncode, ""
    finally:
        if stdout_path:
            stdout_handle.close()
        if stderr_path:
            stderr_handle.close()


def read_pages(pdfinfo_text: str) -> int:
    for line in pdfinfo_text.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    return 0


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_status(all_stems: list[str]) -> dict[str, Any]:
    if STATUS_PATH.exists():
        status = json.loads(STATUS_PATH.read_text(encoding="utf-8"))
    else:
        status = {
            "mode": "running",
            "started_at": now_iso(),
            "updated_at": None,
            "finished_at": None,
            "total_papers": len(all_stems),
            "completed_papers": 0,
            "failed_papers": 0,
            "papers": {},
        }

    status["total_papers"] = len(all_stems)
    papers = status.setdefault("papers", {})
    for stem in all_stems:
        papers.setdefault(
            stem,
            {
                "raw_path": f"raw/{stem}.pdf",
                "status": "pending",
                "started_at": None,
                "completed_at": None,
                "manifest_path": None,
                "error": None,
            },
        )
    return status


def save_status(status: dict[str, Any]) -> None:
    status["updated_at"] = now_iso()
    write_json(STATUS_PATH, status)


def append_index(record: dict[str, Any]) -> None:
    with INDEX_LOCK:
        with INDEX_PATH.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def stage_info() -> dict[str, Any]:
    return {
        "pdfinfo": {},
        "pdftotext": {},
        "pdftotext_bbox": {},
        "docling": {},
        "marker_markdown": {},
    }


def compact_stage(stage: dict[str, Any] | None) -> dict[str, Any]:
    stage = stage or {}
    normalized = stage_info()
    allowed_fields = {
        "pdfinfo": {"status", "command"},
        "pdftotext": {"status", "command", "output"},
        "pdftotext_bbox": {"status", "command", "output"},
        "docling": {"status", "command"},
        "marker_markdown": {"status", "command"},
    }
    for key, fields in allowed_fields.items():
        if key in stage:
            normalized[key] = {field: value for field, value in stage[key].items() if field in fields}
    return normalized


def docling_command(pdf: Path, out_dir: Path, use_ocr: bool) -> list[str]:
    cmd = [
        str(TOOLS["python"]),
        "-m",
        "docling.cli.main",
        str(pdf),
        "--to",
        "md",
        "--to",
        "json",
        "--show-layout",
        "--image-export-mode",
        "placeholder",
        "--tables",
        "--table-mode",
        "accurate",
        "--output",
        str(out_dir),
    ]
    if not use_ocr:
        cmd.insert(-2, "--no-ocr")
    return cmd


def marker_command(pdf: Path, out_dir: Path, output_format: str, disable_image_extraction: bool, use_ocr: bool) -> list[str]:
    cmd = [
        str(TOOLS["python"]),
        "-m",
        "marker.scripts.convert_single",
        str(pdf),
        "--output_dir",
        str(out_dir),
        "--output_format",
        output_format,
        "--disable_multiprocessing",
        "--disable_tqdm",
    ]
    if disable_image_extraction:
        cmd.append("--disable_image_extraction")
    if not use_ocr:
        cmd.append("--disable_ocr")
    return cmd


def list_files(base: Path) -> list[dict[str, Any]]:
    return [
        {"path": rel(path), "size_bytes": path.stat().st_size}
        for path in sorted(base.rglob("*"))
        if path.is_file()
    ]


def paper_manifest(stem: str, pages: int, paper_dir: Path, stage: dict[str, Any]) -> dict[str, Any]:
    return {
        "paper_id": stem,
        "raw_path": f"raw/{stem}.pdf",
        "generated_at": now_iso(),
        "page_count": pages,
        "kind": "pass0_parse_artifacts",
        "notes": [
            "These files are reference parse artifacts, not raw sources and not wiki facts.",
            "They exist to maximize later retrieval, anchoring, figure/table lookup, and cross-checking during wiki construction.",
        ],
        "stages": stage,
        "files": list_files(paper_dir),
    }


def compact_paper_dir(stem: str) -> None:
    paper_dir = PARSES_DIR / stem
    manifest_path = paper_dir / "manifest.json"
    if not paper_dir.exists() or not manifest_path.exists():
        return

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    redundant_files = [
        paper_dir / "pdfinfo.txt",
        paper_dir / "pdfimages.list.txt",
        paper_dir / "commands.stderr.log",
        paper_dir / "docling.run.log",
        paper_dir / "docling.run.err.log",
        paper_dir / "marker.markdown.run.log",
        paper_dir / "marker.markdown.run.err.log",
        paper_dir / "marker.json.run.log",
        paper_dir / "marker.json.run.err.log",
    ]
    for path in redundant_files:
        if path.exists():
            path.unlink()

    for path in (paper_dir / "docling").glob("*.html"):
        path.unlink()
    for path in (paper_dir / "docling").glob("*.txt"):
        path.unlink()

    marker_json_dir = paper_dir / "marker" / "json"
    if marker_json_dir.exists():
        shutil.rmtree(marker_json_dir)

    manifest = paper_manifest(
        stem=stem,
        pages=manifest.get("page_count", 0),
        paper_dir=paper_dir,
        stage=compact_stage(manifest.get("stages")),
    )
    write_json(manifest_path, manifest)


@dataclass
class ParseResult:
    stem: str
    status: str
    manifest_path: str | None
    error: str | None


def parse_one(pdf: Path, force: bool) -> ParseResult:
    stem = pdf.stem
    paper_dir = PARSES_DIR / stem
    manifest_path = paper_dir / "manifest.json"

    if force and paper_dir.exists():
        shutil.rmtree(paper_dir)
    paper_dir.mkdir(parents=True, exist_ok=True)

    if manifest_path.exists() and not force:
        return ParseResult(stem=stem, status="skipped", manifest_path=rel(manifest_path), error=None)
    stage = stage_info()

    try:
        rc, pdfinfo_text = run_command([str(TOOLS["pdfinfo"]), str(pdf)])
        stage["pdfinfo"] = {
            "status": "ok" if rc == 0 else "failed",
            "command": [str(TOOLS["pdfinfo"]), str(pdf)],
        }
        if rc != 0:
            raise RuntimeError("pdfinfo failed")
        pages = read_pages(pdfinfo_text)

        pdftotext_path = paper_dir / "pdftotext.txt"
        rc, _ = run_command([str(TOOLS["pdftotext"]), str(pdf), str(pdftotext_path)])
        stage["pdftotext"] = {
            "status": "ok" if rc == 0 else "failed",
            "command": [str(TOOLS["pdftotext"]), str(pdf), str(pdftotext_path)],
            "output": rel(pdftotext_path),
        }
        if rc != 0:
            raise RuntimeError("pdftotext failed")

        bbox_path = paper_dir / "pdftotext.bbox.html"
        rc, _ = run_command([str(TOOLS["pdftotext"]), "-bbox-layout", str(pdf), str(bbox_path)])
        stage["pdftotext_bbox"] = {
            "status": "ok" if rc == 0 else "failed",
            "command": [str(TOOLS["pdftotext"]), "-bbox-layout", str(pdf), str(bbox_path)],
            "output": rel(bbox_path),
        }
        if rc != 0:
            raise RuntimeError("pdftotext -bbox-layout failed")

        docling_dir = paper_dir / "docling"
        docling_dir.mkdir(exist_ok=True)
        docling_cmd = docling_command(pdf, docling_dir, use_ocr=False)
        rc, out = run_command(docling_cmd)
        if rc != 0:
            docling_cmd = docling_command(pdf, docling_dir, use_ocr=True)
            rc, out = run_command(docling_cmd)
        stage["docling"] = {
            "status": "ok" if rc == 0 else "failed",
            "command": docling_cmd,
        }
        if rc != 0:
            (paper_dir / "docling.failure.log").write_text(out, encoding="utf-8")
            raise RuntimeError("docling failed")

        marker_dir = paper_dir / "marker"
        marker_dir.mkdir(exist_ok=True)
        md_dir = marker_dir / "markdown"
        md_dir.mkdir(exist_ok=True)
        marker_md_cmd = marker_command(pdf, md_dir, output_format="markdown", disable_image_extraction=False, use_ocr=False)
        rc, out = run_command(marker_md_cmd)
        if rc != 0:
            marker_md_cmd = marker_command(pdf, md_dir, output_format="markdown", disable_image_extraction=False, use_ocr=True)
            rc, out = run_command(marker_md_cmd)
        stage["marker_markdown"] = {
            "status": "ok" if rc == 0 else "failed",
            "command": marker_md_cmd,
        }
        if rc != 0:
            (paper_dir / "marker.failure.log").write_text(out, encoding="utf-8")
            raise RuntimeError("marker markdown failed")
        manifest = paper_manifest(stem, pages, paper_dir, stage)
        write_json(manifest_path, manifest)
        return ParseResult(stem=stem, status="completed", manifest_path=rel(manifest_path), error=None)
    except Exception as exc:
        error_path = paper_dir / "error.txt"
        error_path.write_text(str(exc) + "\n", encoding="utf-8")
        return ParseResult(stem=stem, status="failed", manifest_path=rel(manifest_path) if manifest_path.exists() else None, error=str(exc))


def update_status(status: dict[str, Any], result: ParseResult) -> None:
    paper = status["papers"][result.stem]
    if paper["status"] == "pending":
        paper["started_at"] = now_iso()
    paper["status"] = result.status
    if result.status in {"completed", "skipped"}:
        paper["completed_at"] = now_iso()
        paper["manifest_path"] = result.manifest_path
        paper["error"] = None
    elif result.status == "failed":
        paper["completed_at"] = now_iso()
        paper["error"] = result.error
    status["completed_papers"] = sum(1 for item in status["papers"].values() if item["status"] in {"completed", "skipped"})
    status["failed_papers"] = sum(1 for item in status["papers"].values() if item["status"] == "failed")
    save_status(status)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Parse every PDF in raw/.")
    parser.add_argument("--only", nargs="*", default=[], help="Only parse the given stems.")
    parser.add_argument("--jobs", type=int, default=2, help="Parallel paper workers.")
    parser.add_argument("--force", action="store_true", help="Re-run even if manifest exists.")
    parser.add_argument("--compact-extracts", action="store_true", help="Delete redundant parse artifacts and refresh manifests.")
    args = parser.parse_args()

    ensure_dirs()
    verify_tools()

    all_pdfs = iter_pdfs()
    all_stems = [pdf.stem for pdf in all_pdfs]
    pdfs = all_pdfs
    if args.only:
        wanted = set(args.only)
        pdfs = [pdf for pdf in pdfs if pdf.stem in wanted]
    elif not args.all:
        parser.error("Pass --all or --only.")

    if args.compact_extracts:
        for pdf in pdfs:
            compact_paper_dir(pdf.stem)
            print(f"[COMPACTED] {pdf.stem}", flush=True)
        return 0

    status = load_status(all_stems)
    status["mode"] = "running"
    status["finished_at"] = None
    save_status(status)

    selected = []
    for pdf in pdfs:
        current = status["papers"][pdf.stem]["status"]
        if not args.force and current in {"completed", "skipped"} and (PARSES_DIR / pdf.stem / "manifest.json").exists():
            continue
        selected.append(pdf)

    with ThreadPoolExecutor(max_workers=max(args.jobs, 1)) as executor:
        futures = {executor.submit(parse_one, pdf, args.force): pdf.stem for pdf in selected}
        for future in as_completed(futures):
            result = future.result()
            with STATUS_LOCK:
                update_status(status, result)
            append_index(
                {
                    "timestamp": now_iso(),
                    "paper_id": result.stem,
                    "status": result.status,
                    "manifest_path": result.manifest_path,
                    "error": result.error,
                }
            )
            print(f"[{result.status.upper()}] {result.stem}", flush=True)

    status["mode"] = "completed" if status["failed_papers"] == 0 else "completed_with_errors"
    status["finished_at"] = now_iso()
    save_status(status)
    return 0 if status["failed_papers"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
