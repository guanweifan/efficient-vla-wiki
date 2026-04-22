[中文](../usage.md) | English

# Usage Guide

This document explains the main ways to use the repository.

## 1. Query only

If you want to answer a question based on the current `wiki`, use `wiki-query`.

The usual search order is:

1. `wiki/synthesis/`
2. `wiki/evidence/`
3. `wiki/papers/`
4. `raw/` when the answer still needs a direct check

The result is written to:

- `threads/query/*.md`

A new question usually creates a new query file. If you are still following the same main question, the result is usually added to the existing thread.

Good fits include:

- mapping the main research directions
- organizing method families
- finding representative papers for one topic
- clarifying the boundary and disagreements around one efficiency line

## 2. Write query results back to `wiki`

If the conclusion in a thread is already stable, use `wiki-reflect`.

It writes the result back to:

- `wiki/papers/`
- `wiki/evidence/`
- `wiki/synthesis/`

Typical use cases:

- tightening term boundaries
- creating or extending shared evidence pages
- refining a topic page

## 3. Check `wiki`

If you want to check whether `wiki` is still in good shape, use `wiki-lint`.

It focuses on:

- broken links
- `raw` anchors
- links between paper pages and evidence pages
- `Evidence Links` in synthesis pages
- `wiki/index.md`, `wiki/log.md`, and `wiki/status.json`

## 4. Pull the latest version

### Pull the latest `wiki`

```bash
git pull --rebase
git submodule update --init --recursive
```

### Pull the latest `raw/`

```bash
uv run python scripts/release/fetch_raw.py
```

### Pull the latest `extracts/`

```bash
uv run python scripts/release/sync_hf_extracts.py pull
```

## 5. Maintain your own version

If you want to maintain your own local `wiki`, the main tools are:

- `wiki-query`
- `wiki-reflect`
- `wiki-lint`
- `wiki-ingest`

A common order is:

1. query on the current `wiki`
2. reflect stable results back into `wiki`
3. lint the affected pages
4. ingest new papers when needed

`threads/` works well as your own local workspace.

## 6. Follow only the latest papers

If you only want to track the latest papers from `update.md`, use `wiki-ingest`.

The default source is:

- `external/awesome-efficient-vla/update.md`

That flow does the following:

1. read `update.md`
2. download missing PDFs
3. fill the matching `extracts/`
4. update the affected `wiki`

Under the hood, it first uses `scripts/ingest_update.py` to prepare `raw/` and `extracts/`, then continues with the `wiki` update.

## 7. How to use `extracts/`

Most readers only need to pull the latest `extracts/`:

```bash
uv run python scripts/release/sync_hf_extracts.py pull
```

You only need to rebuild parser outputs in a few cases:

- you added papers locally
- one paper has broken parser output
- you want to rerun the parse for one paper

Then use:

- `scripts/build_extracts.py`

## 8. Environment

Base environment:

- Python `3.11`
- `uv`

If you want to maintain `raw/` and `extracts/` locally, you also need:

- `pdfinfo`
- `pdftotext`
- `docling`
- `marker_single`

`uv sync` installs the project dependencies, including `docling` and `marker-pdf`.
