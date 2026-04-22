#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "raw"
EXTRACTS_DIR = ROOT / "extracts" / "parses"
MANIFESTS_DIR = ROOT / "scripts" / "release" / "manifests"
PAPERS_MANIFEST = MANIFESTS_DIR / "papers.jsonl"
ARXIV_PREFIX_RE = re.compile(r"^(?P<prefix>\d{4}_\d{4,5})(?:_(?P<alias>.+))?$")


def record_for_pdf(pdf: Path) -> dict[str, object]:
    match = ARXIV_PREFIX_RE.match(pdf.stem)
    if match is None:
        raise ValueError(f"unexpected raw filename: {pdf.name}")

    prefix = match.group("prefix")
    alias = match.group("alias")
    arxiv_id = prefix.replace("_", ".", 1)
    parse_dir = EXTRACTS_DIR / pdf.stem
    parse_manifest = parse_dir / "manifest.json"

    return {
        "paper_id": pdf.stem,
        "arxiv_id": arxiv_id,
        "alias": alias,
        "source_url": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
        "raw_path": f"raw/{pdf.name}",
        "extracts_dir": f"extracts/parses/{pdf.stem}",
        "extracts_manifest_path": str(parse_manifest.relative_to(ROOT)) if parse_manifest.exists() else None,
        "has_extracts_manifest": parse_manifest.exists(),
        "redistribution_review": "not_reviewed",
    }


def main() -> int:
    MANIFESTS_DIR.mkdir(parents=True, exist_ok=True)

    records = [record_for_pdf(pdf) for pdf in sorted(RAW_DIR.glob("*.pdf"))]
    with PAPERS_MANIFEST.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"wrote {len(records)} records to {PAPERS_MANIFEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
