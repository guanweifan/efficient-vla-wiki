#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = ROOT / "scripts" / "release" / "manifests" / "huggingface_extracts.json"


def load_config(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_path(root: Path, value: str | Path) -> Path:
    path = value if isinstance(value, Path) else Path(str(value))
    return path if path.is_absolute() else (root / path)


def summarize_dir(path: Path) -> dict[str, object]:
    if not path.exists():
        return {"exists": False, "file_count": 0, "size_bytes": 0}

    file_count = 0
    size_bytes = 0
    for item in path.rglob("*"):
        if item.is_file():
            file_count += 1
            size_bytes += item.stat().st_size
    return {"exists": True, "file_count": file_count, "size_bytes": size_bytes}


def link_or_copy(src: str, dst: str) -> str:
    try:
        os.link(src, dst)
    except OSError:
        shutil.copy2(src, dst)
    return dst


def build_stage_tree(extracts_dir: Path, stage_dir: Path, dataset_card: Path) -> None:
    if stage_dir.exists():
        shutil.rmtree(stage_dir)
    stage_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(dataset_card, stage_dir / "README.md")
    shutil.copytree(extracts_dir, stage_dir / "extracts", copy_function=link_or_copy)


def main() -> int:
    parser = argparse.ArgumentParser(description="Assemble extracts into a dedicated directory for Hugging Face dataset upload.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG, help="Path to huggingface_extracts.json.")
    parser.add_argument("--stage-dir", type=Path, default=None, help="Override the staging directory.")
    parser.add_argument("--dataset-card", type=Path, default=None, help="Override the dataset card template.")
    args = parser.parse_args()

    config_path = args.config if args.config.is_absolute() else (ROOT / args.config)
    config_path = config_path.resolve()
    if not config_path.exists():
        raise SystemExit(f"Config not found: {config_path}")

    config = load_config(config_path)
    extracts_dir = resolve_path(ROOT, str(config.get("local_extracts_dir", "extracts"))).resolve()
    if not extracts_dir.exists():
        raise SystemExit(f"Local extracts directory not found: {extracts_dir}")

    stage_dir = args.stage_dir or resolve_path(ROOT, str(config.get("local_stage_dir", ".hf/staging/efficient-vla-extracts")))
    stage_dir = stage_dir.resolve()

    dataset_card_value = args.dataset_card or resolve_path(
        ROOT, str(config.get("dataset_card_template", "scripts/release/manifests/huggingface_extracts_README.md"))
    )
    dataset_card = dataset_card_value.resolve()
    if not dataset_card.exists():
        raise SystemExit(f"Dataset card template not found: {dataset_card}")

    build_stage_tree(extracts_dir, stage_dir, dataset_card)

    repo_id = str(config.get("repo_id", "")).strip()
    payload = {
        "repo_id": repo_id,
        "stage_dir": str(stage_dir.relative_to(ROOT)),
        "stage_summary": summarize_dir(stage_dir),
        "extracts_summary": summarize_dir(extracts_dir),
        "next_step": f"hf upload-large-folder {repo_id} {stage_dir} --repo-type dataset" if repo_id else "",
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
