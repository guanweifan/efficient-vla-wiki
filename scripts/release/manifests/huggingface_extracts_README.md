---
pretty_name: efficient-vla-extracts
size_categories:
  - 1K<n<10K
task_categories:
  - text-retrieval
  - question-answering
language:
  - en
tags:
  - robotics
  - vision-language-action
  - arxiv
  - pdf-parsing
---

# efficient-vla-extracts

Parser-derived artifacts for the `efficient-vla-wiki` project.

This dataset is the data layer companion to the main repository:

- GitHub: `efficient-vla-wiki`
- Dataset repo: `efficient-vla-extracts`

## What is inside

The staged upload keeps the local directory structure:

```text
extracts/
├── meta/
│   ├── extract_build_index.jsonl
│   └── extract_build_status.json
└── parses/
    └── <paper_id>/
```

Each paper directory may contain:

- `pdftotext.txt`
- `pdftotext.bbox.html`
- `docling/*.md`
- `docling/*.json`
- parser-generated images and figures
- `manifest.json`

## What this dataset is for

This dataset is used as the local parse layer for:

- paper lookup
- section and figure localization
- evidence backtracking
- query-time report generation
- wiki maintenance in `efficient-vla-wiki`

## Source and generation

- Source papers are collected from arXiv into the local `raw/` directory of the main repository.
- Parser artifacts are generated from local PDFs with:
  - `pdftotext`
  - `pdfinfo`
  - `Docling`
  - `Marker`

## License note

This dataset contains parser-derived artifacts from third-party papers.

- Reuse conditions depend on the license of each source paper.
- Do not assume a single uniform redistribution license for all files.
- Check the source paper license before re-hosting or republishing extracted content.

## Related files

- Main repository policy: `docs/data-and-sync.md`
- Local manifest: `scripts/release/manifests/papers.jsonl`
- Local HF config: `scripts/release/manifests/huggingface_extracts.json`
