#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "raw"
EXTRACTS_DIR = ROOT / "extracts"
DEFAULT_SOURCE_CANDIDATES = [
    ROOT / "external" / "awesome-efficient-vla" / "update.md",
]
BUILD_EXTRACTS_SCRIPT = ROOT / "scripts" / "build_extracts.py"

KEY_RE = re.compile(
    r"^\s*(?:[-*]\s*)?(?:\*\*)?(?P<key>[A-Za-z][A-Za-z0-9 _/-]*)(?:\*\*)?\s*[:：]\s*(?P<value>.+?)\s*$"
)
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(?P<id>\d{4}\.\d{4,5})(?:v\d+)?(?:\.pdf)?")
STEM_PREFIX_RE = re.compile(r"^(?P<prefix>\d{4}_\d{4,5})")
KNOWN_KEYS = {
    "title": "title",
    "shortname": "shorts",
    "shorts": "shorts",
    "link": "link",
    "code": "code",
    "coreidea": "idea",
    "idea": "idea",
    "primarycategory": "category",
    "category": "category",
    "second": "second",
    "tag": "tag",
    "whythiscategory": "reason",
    "reason": "reason",
}


def normalize_key(raw_key: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", raw_key.lower())


def sanitize_alias(value: str) -> str:
    alias = re.sub(r"\s+", "-", value.strip())
    alias = re.sub(r"[^A-Za-z0-9._-]+", "", alias)
    alias = re.sub(r"-{2,}", "-", alias).strip("._-")
    return alias[:80] or "Paper"


def clean_value(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^\*\*\s*", "", value)
    value = re.sub(r"\s*\*\*$", "", value)
    return value.strip()


def stem_prefix_from_arxiv(arxiv_id: str) -> str:
    return arxiv_id.replace(".", "_")


def arxiv_from_link(link: str) -> str | None:
    match = ARXIV_RE.search(link)
    if not match:
        return None
    return match.group("id")


def canonical_pdf_url(arxiv_id: str) -> str:
    return f"https://arxiv.org/pdf/{arxiv_id}.pdf"


def iter_blocks(text: str) -> Iterable[dict[str, object]]:
    current: dict[str, object] = {}
    for line_no, line in enumerate(text.splitlines(), start=1):
        match = KEY_RE.match(line)
        if not match:
            continue
        key = KNOWN_KEYS.get(normalize_key(match.group("key")))
        if key is None:
            continue
        if key == "title" and current:
            yield current
            current = {}
        current.setdefault("source_lines", []).append(line_no)
        current[key] = clean_value(match.group("value"))
    if current:
        yield current


def load_records(path: Path) -> list[dict[str, object]]:
    text = path.read_text(encoding="utf-8")
    return list(iter_blocks(text))


def resolve_source_path(user_source: Path | None) -> Path:
    if user_source is not None:
        path = user_source if user_source.is_absolute() else (ROOT / user_source)
        path = path.resolve()
        if not path.exists():
            raise SystemExit(f"Source file not found: {path}")
        return path

    for candidate in DEFAULT_SOURCE_CANDIDATES:
        if candidate.exists():
            return candidate.resolve()

    raise SystemExit(
        "No default ingest source found. Pass --source <path> or provide a local update.md-style source "
        "(for example external/awesome-efficient-vla)."
    )


def existing_raw_map() -> dict[str, Path]:
    mapping: dict[str, Path] = {}
    for pdf in sorted(RAW_DIR.glob("*.pdf")):
        match = STEM_PREFIX_RE.match(pdf.stem)
        if not match:
            continue
        mapping.setdefault(match.group("prefix"), pdf)
    return mapping


def manifest_exists(stem: str) -> bool:
    return (EXTRACTS_DIR / "parses" / stem / "manifest.json").exists()


def download_pdf(url: str, dest: Path) -> None:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "efficient-vla-wiki-ingest/1.0",
            "Accept": "application/pdf,*/*;q=0.8",
        },
    )
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(request, timeout=120) as response:
        with tempfile.NamedTemporaryFile(dir=dest.parent, delete=False) as tmp:
            tmp_path = Path(tmp.name)
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                tmp.write(chunk)
    tmp_path.replace(dest)


@dataclass
class IngestResult:
    title: str
    arxiv_id: str | None
    pdf_url: str | None
    stem: str | None
    shorts: str | None = None
    source_lines: list[int] = field(default_factory=list)
    duplicate_count: int = 0
    duplicate_titles: list[str] = field(default_factory=list)
    raw_path: str | None = None
    raw_status: str = "unresolved"
    parse_status: str = "unresolved"
    manifest_path: str | None = None
    error: str | None = None


def summarize(
    records: list[dict[str, object]],
    raw_map: dict[str, Path],
    *,
    only_arxiv: set[str] | None,
    limit: int | None,
) -> tuple[list[IngestResult], list[IngestResult]]:
    ordered: list[IngestResult] = []
    duplicates: list[IngestResult] = []
    seen: dict[str, IngestResult] = {}

    for record in records:
        title = str(record.get("title", "")).strip()
        link = str(record.get("link", "")).strip()
        arxiv_id = arxiv_from_link(link) if link else None
        result = IngestResult(
            title=title,
            shorts=str(record.get("shorts", "")).strip() or None,
            arxiv_id=arxiv_id,
            pdf_url=canonical_pdf_url(arxiv_id) if arxiv_id else None,
            stem=None,
            source_lines=list(record.get("source_lines", [])),
        )
        if only_arxiv and arxiv_id not in only_arxiv:
            continue
        if arxiv_id is None:
            result.error = "missing_or_invalid_arxiv_link"
            duplicates.append(result)
            continue

        prefix = stem_prefix_from_arxiv(arxiv_id)
        existing_pdf = raw_map.get(prefix)
        if existing_pdf is not None:
            result.stem = existing_pdf.stem
            result.raw_path = str(existing_pdf.relative_to(ROOT))
            result.raw_status = "existing"
        else:
            alias = sanitize_alias(result.shorts or title)
            result.stem = f"{prefix}_{alias}"
            result.raw_path = str((RAW_DIR / f"{result.stem}.pdf").relative_to(ROOT))
            result.raw_status = "missing"

        prior = seen.get(arxiv_id)
        if prior is not None:
            prior.duplicate_count += 1
            prior.duplicate_titles.append(title)
            result.raw_status = "duplicate_in_update"
            result.parse_status = "duplicate_in_update"
            duplicates.append(result)
            continue

        seen[arxiv_id] = result
        ordered.append(result)

    if limit is not None:
        ordered = ordered[:limit]
    return ordered, duplicates


def run_extract_build(stems: list[str], jobs: int, force: bool) -> None:
    if not stems:
        return
    cmd = [sys.executable, str(BUILD_EXTRACTS_SCRIPT), "--only", *stems, "--jobs", str(jobs)]
    if force:
        cmd.append("--force")
    subprocess.run(cmd, cwd=ROOT, check=True)


def format_human(results: list[IngestResult], duplicates: list[IngestResult]) -> str:
    lines = []
    for item in results:
        detail = f"{item.arxiv_id} -> {item.stem}"
        status = f"raw={item.raw_status}, parse={item.parse_status}"
        lines.append(f"- {detail} ({status})")
        if item.error:
            lines.append(f"  error: {item.error}")
    if duplicates:
        lines.append("duplicates_or_invalid:")
        for item in duplicates:
            ref = item.arxiv_id or "invalid"
            lines.append(f"- {ref} ({item.raw_status})")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=None,
        help="Path to an update.md-style source file. Defaults to the first known local source that exists.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Plan only; do not download or parse.")
    parser.add_argument("--json", action="store_true", help="Emit JSON summary.")
    parser.add_argument("--limit", type=int, default=None, help="Only process the first N unique arXiv papers.")
    parser.add_argument("--only-arxiv", nargs="*", default=[], help="Only process the given arXiv ids.")
    parser.add_argument("--parse-jobs", type=int, default=2, help="Parallel jobs for building extracts.")
    parser.add_argument("--parse-force", action="store_true", help="Force re-build for selected extracts.")
    args = parser.parse_args()

    source_path = resolve_source_path(args.source)

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    raw_map = existing_raw_map()
    records = load_records(source_path)
    only_arxiv = set(args.only_arxiv) or None
    results, duplicates = summarize(records, raw_map, only_arxiv=only_arxiv, limit=args.limit)

    parse_queue: list[str] = []
    for item in results:
        if item.error:
            item.raw_status = "invalid"
            item.parse_status = "invalid"
            continue

        if item.stem is None or item.raw_path is None or item.arxiv_id is None or item.pdf_url is None:
            item.error = "incomplete_record"
            item.raw_status = "invalid"
            item.parse_status = "invalid"
            continue

        raw_path = ROOT / item.raw_path
        if item.raw_status == "missing" and not args.dry_run:
            try:
                download_pdf(item.pdf_url, raw_path)
                item.raw_status = "downloaded"
            except urllib.error.URLError as exc:
                item.raw_status = "download_failed"
                item.parse_status = "skipped"
                item.error = str(exc)
                continue
        elif item.raw_status == "missing":
            item.raw_status = "pending_download"

        needs_parse = args.parse_force or not manifest_exists(item.stem)
        if needs_parse:
            if args.dry_run:
                item.parse_status = "pending_parse"
            else:
                parse_queue.append(item.stem)
                item.parse_status = "queued"
        else:
            item.parse_status = "existing"
            item.manifest_path = str((EXTRACTS_DIR / "parses" / item.stem / "manifest.json").relative_to(ROOT))

    if parse_queue and not args.dry_run:
        run_extract_build(parse_queue, jobs=args.parse_jobs, force=args.parse_force)

    for item in results:
        if item.stem is None:
            continue
        manifest = EXTRACTS_DIR / "parses" / item.stem / "manifest.json"
        if manifest.exists():
            item.manifest_path = str(manifest.relative_to(ROOT))
            if item.parse_status in {"queued", "pending_parse"}:
                item.parse_status = "generated" if not args.dry_run else item.parse_status
        elif item.parse_status == "queued":
            item.parse_status = "parse_failed"

    payload = {
        "source": str(source_path.relative_to(ROOT)),
        "unique_records": len(results),
        "duplicate_or_invalid_records": len(duplicates),
        "results": [asdict(item) for item in results],
        "duplicates": [asdict(item) for item in duplicates],
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(format_human(results, duplicates))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
