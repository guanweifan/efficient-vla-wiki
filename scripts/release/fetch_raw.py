#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import tempfile
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "raw"
DEFAULT_MANIFEST = ROOT / "scripts" / "release" / "manifests" / "papers.jsonl"


def load_manifest(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def download_file(url: str, dest: Path) -> None:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "efficient-vla-wiki-fetch-raw/1.0",
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST, help="Path to papers.jsonl manifest.")
    parser.add_argument("--paper-id", nargs="*", default=[], help="Only fetch the given paper ids.")
    parser.add_argument("--arxiv-id", nargs="*", default=[], help="Only fetch the given arXiv ids.")
    parser.add_argument("--dry-run", action="store_true", help="Only print which PDFs would be fetched.")
    parser.add_argument("--force", action="store_true", help="Re-download PDFs even if they already exist locally.")
    args = parser.parse_args()

    manifest_path = args.manifest if args.manifest.is_absolute() else (ROOT / args.manifest)
    manifest_path = manifest_path.resolve()
    if not manifest_path.exists():
        raise SystemExit(f"Manifest not found: {manifest_path}")

    wanted_paper_ids = set(args.paper_id)
    wanted_arxiv_ids = set(args.arxiv_id)

    records = load_manifest(manifest_path)
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    selected = []
    for record in records:
        paper_id = str(record["paper_id"])
        arxiv_id = str(record["arxiv_id"])
        if wanted_paper_ids and paper_id not in wanted_paper_ids:
            continue
        if wanted_arxiv_ids and arxiv_id not in wanted_arxiv_ids:
            continue
        selected.append(record)

    for record in selected:
        raw_path = ROOT / str(record["raw_path"])
        source_url = str(record["source_url"])
        if raw_path.exists() and not args.force:
            print(f"[SKIP] {record['paper_id']} ({raw_path.relative_to(ROOT)} exists)")
            continue
        if args.dry_run:
            print(f"[DRY-RUN] {record['paper_id']} <- {source_url}")
            continue
        try:
            download_file(source_url, raw_path)
            print(f"[DOWNLOADED] {record['paper_id']} <- {source_url}")
        except urllib.error.URLError as exc:
            print(f"[FAILED] {record['paper_id']} <- {source_url} :: {exc}")
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
