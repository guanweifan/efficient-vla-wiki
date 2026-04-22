[中文](../data-and-sync.md) | English

# Data and Sync

This document explains where the repository data comes from, what is stored in Git, and what should be pulled separately.

## Content groups

The repository content can be grouped into three parts:

1. repository-authored content
   - including `wiki/`, `docs/`, `.codex/skills/`, `scripts/`, and local `threads/`
2. `raw/`
   - third-party paper PDFs
3. `extracts/`
   - parser outputs generated from `raw/`

## What is directly available in Git

- `wiki/`
- `docs/`
- `.codex/skills/`
- `scripts/`
- `external/awesome-efficient-vla/`

`raw/` and `extracts/` should be pulled separately to your local machine.

## How to get `raw/`

- `raw/` is pulled locally with `scripts/release/fetch_raw.py`
- it stores the original PDFs
- query, reflect, lint, and ingest all fall back to this layer when a fact needs to be checked directly

## How to get `extracts/`

- `extracts/` is pulled from the Hugging Face dataset
- the sync script is:
  - `scripts/release/sync_hf_extracts.py`
- the normal use case is to pull the latest version directly

## What is inside `extracts/`

- `pdftotext.txt`
- `pdftotext.bbox.html`
- `docling/*.md`
- `docling/*.json`
- figure and image exports

These files are used for retrieval, locating evidence, and reading back source content.

## What `update.md` does

- the default update source is:
  - `external/awesome-efficient-vla/update.md`
- when you only want to follow the latest papers, `wiki-ingest` uses this file to update your local `wiki`

## License

- repository-authored content uses `MIT`

Third-party paper PDFs, paper images, and parser outputs derived from paper content are not covered by this license.

## Hugging Face dataset

- `extracts/` is distributed through a separate Hugging Face dataset repo
- this repository keeps the sync script, dataset assembly script, manifest, and dataset card template

## Manifest and sync scripts

- files under `scripts/release/manifests/` are operation metadata
- scripts under `scripts/release/` are used for fetching, syncing, and preparing distribution files

## Reuse

1. separate repository-authored content from third-party paper content first
2. check upstream licenses before redistributing `raw/` or `extracts/`
3. when unsure, link back to the upstream source
