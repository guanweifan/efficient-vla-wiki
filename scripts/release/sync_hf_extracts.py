#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from huggingface_hub import HfApi, snapshot_download


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = ROOT / "scripts" / "release" / "manifests" / "huggingface_extracts.json"


def load_config(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def repo_id_from_args(config: dict[str, object], override: str | None) -> str:
    repo_id = override or str(config.get("repo_id", "")).strip()
    if not repo_id:
        raise SystemExit(
            "No Hugging Face dataset repo is configured. Set scripts/release/manifests/huggingface_extracts.json "
            "or pass --repo-id."
        )
    return repo_id


def summarize_local_dir(path: Path) -> dict[str, object]:
    if not path.exists():
        return {"exists": False, "file_count": 0, "size_bytes": 0}
    file_count = 0
    size_bytes = 0
    for item in path.rglob("*"):
        if item.is_file():
            file_count += 1
            size_bytes += item.stat().st_size
    return {"exists": True, "file_count": file_count, "size_bytes": size_bytes}


def main() -> int:
    parser = argparse.ArgumentParser(description="Pull or push extracts against the configured Hugging Face dataset repo.")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG, help="Path to huggingface_extracts.json.")
    parser.add_argument("--repo-id", default=None, help="Override the configured Hugging Face dataset repo id.")
    parser.add_argument("--revision", default=None, help="Override the configured target revision.")
    parser.add_argument("--local-dir", type=Path, default=None, help="Override the configured local extracts dir.")
    parser.add_argument("--allow-pattern", nargs="*", default=None, help="Optional allow patterns for pull/push.")
    parser.add_argument("--ignore-pattern", nargs="*", default=None, help="Optional ignore patterns for pull/push.")
    parser.add_argument("command", choices=["status", "pull", "push"], help="Sync command to run.")
    args = parser.parse_args()

    config_path = args.config if args.config.is_absolute() else (ROOT / args.config)
    config_path = config_path.resolve()
    if not config_path.exists():
        raise SystemExit(f"Config not found: {config_path}")

    config = load_config(config_path)
    revision = args.revision or str(config.get("default_revision", "main"))
    local_dir_value = args.local_dir or Path(str(config.get("local_extracts_dir", "extracts")))
    local_dir = local_dir_value if local_dir_value.is_absolute() else (ROOT / local_dir_value)

    if args.command == "status":
        payload = {
            "config_path": str(config_path.relative_to(ROOT)),
            "repo_id": config.get("repo_id", ""),
            "repo_type": config.get("repo_type", "dataset"),
            "revision": revision,
            "local_dir": str(local_dir.relative_to(ROOT)),
            "local_summary": summarize_local_dir(local_dir),
            "hf_token_present": bool(os.environ.get("HF_TOKEN")),
            "status": config.get("status", ""),
            "review_status": config.get("local_review_status", ""),
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    repo_id = repo_id_from_args(config, args.repo_id)
    repo_type = str(config.get("repo_type", "dataset"))

    if args.command == "pull":
        snapshot_download(
            repo_id=repo_id,
            repo_type=repo_type,
            revision=revision,
            local_dir=local_dir,
            allow_patterns=args.allow_pattern,
            ignore_patterns=args.ignore_pattern,
        )
        print(f"pulled {repo_type} {repo_id}@{revision} into {local_dir}")
        return 0

    api = HfApi()
    api.upload_large_folder(
        repo_id=repo_id,
        repo_type=repo_type,
        folder_path=local_dir,
        revision=revision,
        allow_patterns=args.allow_pattern,
        ignore_patterns=args.ignore_pattern,
    )
    print(f"uploaded {local_dir} to {repo_type} {repo_id}@{revision}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
