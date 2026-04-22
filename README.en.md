# Efficient VLA Wiki

[![中文](https://img.shields.io/badge/%E4%B8%AD%E6%96%87-69B1FF.svg)](README.md)
[![English](https://img.shields.io/badge/English-1677FF.svg)](README.en.md)
[![Extracts](https://img.shields.io/badge/Extracts-Hugging%20Face-F6C343.svg)](https://huggingface.co/datasets/guanweifan/efficient-vla-extracts)
[![Source](https://img.shields.io/badge/Source-awesome--efficient--vla-b31b1b.svg)](https://github.com/guanweifan/awesome-efficient-vla)

A local knowledge base for efficient VLA papers. It keeps paper PDFs, parser outputs, stable knowledge, and query reports in one place, so you can either query the current `wiki` directly or keep extending your own local research workspace from the current version.

The paper scope is built on top of [awesome-efficient-vla](https://github.com/guanweifan/awesome-efficient-vla).

This repository is maintained in Chinese. The English documents here cover the repository overview and usage. If you want a full English working copy, use the prompt in [docs/en/translation-prompt.md](docs/en/translation-prompt.md) to translate the remaining Chinese content locally.

## Start here

| If you want to... | Start with... |
| --- | --- |
| follow the official latest version | pull the latest repository, `raw/`, and `extracts`, then use `wiki-query` |
| maintain your own local knowledge base | start from the current version and work through `wiki-query -> wiki-reflect -> wiki-lint -> wiki-ingest` |

> [!TIP]
> Obsidian works well as the front end for this repository. Use wikilinks, backlinks, and page jumps to move through `wiki/`, `threads/`, and source links.

## Setup

### Environment

- Python `3.11`
- `uv`

If you want to update papers and parser outputs locally, you also need:

- `pdfinfo`
- `pdftotext`
- `docling`
- `marker_single`

`uv sync` installs the project dependencies, including `docling` and `marker-pdf`.

```bash
uv sync
```

### Get local data

1. Clone the repository and initialize the submodule

```bash
git clone https://github.com/guanweifan/efficient-vla-wiki.git
cd efficient-vla-wiki
git submodule update --init --recursive
```

2. Pull `raw/`

```bash
uv run python scripts/release/fetch_raw.py --dry-run
uv run python scripts/release/fetch_raw.py
```

3. Pull `extracts/`

```bash
uv run python scripts/release/sync_hf_extracts.py pull
```

## Repository structure

```text
.
├── raw/                         # original PDFs, pulled locally from the manifest
├── extracts/                    # parser outputs, pulled from Hugging Face
│   ├── meta/                    # global status files
│   └── parses/                  # per-paper parse directories
├── wiki/                        # stable knowledge layer
│   ├── papers/                  # per-paper pages
│   ├── evidence/                # reusable evidence pages
│   └── synthesis/               # cross-paper topic pages
├── threads/                     # local query reports and workspace
├── external/                    # external input sources
│   └── awesome-efficient-vla/   # default paper update source with update.md
├── scripts/                     # data and sync scripts
│   ├── build_extracts.py        # rebuild parser outputs when needed
│   ├── ingest_update.py         # pull new papers from update.md and fill extracts
│   └── release/                 # fetch raw, sync extracts, prepare distribution files
├── docs/                        # usage docs and templates
│   └── templates/               # templates for paper, evidence, and synthesis pages
├── AGENTS.md                    # collaboration rules, maintained in Chinese
└── WIKI_SCHEMA.md               # wiki structure rules, maintained in Chinese
```

## Four skills

- `wiki-query`: write query reports from the current `wiki`, output to `threads/query/*.md`
- `wiki-reflect`: write stable conclusions from `threads/` back into `wiki`
- `wiki-lint`: check the structure, evidence chain, and control files in `wiki`
- `wiki-ingest`: follow new papers from `update.md` and update `wiki`

See [docs/en/usage.md](docs/en/usage.md) for the English usage guide.


## Follow the official version

### Update to the latest version

```bash
git pull --rebase
git submodule update --init --recursive
uv run python scripts/release/fetch_raw.py
uv run python scripts/release/sync_hf_extracts.py pull
```

### Run query on the current `wiki`

The main entry point is `wiki-query`. It searches `wiki/` first, goes back to `raw/` when needed, and writes the result to `threads/query/*.md`.

Typical prompts include:

1. research map

   `Prompt`
   > Please give me a systematic map of the main research directions in efficient VLA. I want a clear overall structure first, then a breakdown of what each direction is trying to solve, why it matters, and how the directions relate to each other.

   `Sample Query`
   [q0001-efficient-vla-research-map](threads/query/q0001-efficient-vla-research-map.md)

2. baseline selection

   `Prompt`
   > Please analyze the main efficient VLA baselines that people currently use. I want to understand what types they fall into, how they are used in practice, and what I should consider if I want to pick one as a code base for my own work.

   `Sample Query`
   [q0002-vla-baselines-recent](threads/query/q0002-vla-baselines-recent.md)

3. topic tracking

   `Prompt`
   > Please analyze the current line of work on token pruning in VLA. I want a structured view of the representative methods, their main ideas, where they work well, how they differ from token pruning in standard VLMs, and what still looks unresolved.

   `Sample Query`
   [q0003-vla-token-pruning-landscape](threads/query/q0003-vla-token-pruning-landscape.md)

## Maintain your own local knowledge base

### Common order

1. use `wiki-query` to write query reports
2. use `wiki-reflect` to write stable results back to `wiki`
3. use `wiki-lint` to check and tighten the structure
4. use `wiki-ingest` when new papers arrive

### Write query results back to `wiki`

The main entry point is `wiki-reflect`. It writes stable conclusions from `threads/` back into paper pages, evidence pages, or synthesis pages.

### Check `wiki`

The main entry point is `wiki-lint`. It checks:

- broken links
- evidence gaps
- the division of labor across `papers / evidence / synthesis`
- `wiki/index.md`, `wiki/log.md`, and `wiki/status.json`

### Follow only the latest papers from `update.md`

The main entry point is `wiki-ingest`.

The default update source is fixed to `external/awesome-efficient-vla/update.md`.

That path does the following:

1. read `update.md`
2. download missing PDFs into `raw/`
3. fill the matching `extracts/`
4. update affected `wiki/papers/`
5. update `wiki/evidence/` and `wiki/synthesis/` when needed
6. sync `wiki/index.md`, `wiki/log.md`, and `wiki/status.json`

## Data and license

- data fetching and sync: [docs/en/data-and-sync.md](docs/en/data-and-sync.md)
- repository-authored content: `MIT`
- `raw/` and `extracts/` are outside the repository `MIT` license and should be reused under their upstream terms

## Citation

The paper scope is built on [awesome-efficient-vla](https://github.com/guanweifan/awesome-efficient-vla). If you cite the paper collection or survey layer, cite the upstream work first:

```bibtex
@misc{guan2025efficientvisionlanguageactionmodelsembodied,
  title={Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey},
  author={Weifan Guan and Qinghao Hu and Aosheng Li and Jian Cheng},
  year={2025},
  eprint={2510.17111},
  archivePrefix={arXiv},
  primaryClass={cs.RO},
  url={https://arxiv.org/abs/2510.17111}
}
```

The repository citation is available in [CITATION.cff](CITATION.cff).
