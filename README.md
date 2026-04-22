# Efficient VLA Wiki

<p>
  <a href="README.md">
    <img alt="中文" src="https://img.shields.io/badge/%E4%B8%AD%E6%96%87-1677FF?style=flat-square">
  </a>
  <a href="README.en.md">
    <img alt="English" src="https://img.shields.io/badge/English-69B1FF?style=flat-square">
  </a>
  <a href="https://huggingface.co/datasets/guanweifan/efficient-vla-extracts">
    <img alt="Hugging Face Extracts" src="https://img.shields.io/badge/Extracts-Hugging%20Face-F6C343?style=flat-square">
  </a>
  <a href="external/awesome-efficient-vla/README.md">
    <img alt="Source List" src="https://img.shields.io/badge/Source-awesome--efficient--vla-B31B1B?style=flat-square">
  </a>
</p>

一个面向 efficient VLA 论文的本地知识库。将原始论文、解析结果、稳定知识和问题报告放在同一套目录里，适合直接做 query，也适合从当前版本继续维护自己的本地研究工作区。

论文范围建立在 [awesome-efficient-vla](external/awesome-efficient-vla/README.md) 的收集基础上。

## 快速入口

| 如果你想做什么 | 直接这样开始 |
| --- | --- |
| 跟随官方最新版本使用 | 拉取最新仓库、`raw/` 和 `extracts/`，然后直接使用 `wiki-query` |
| 从当前版本开始维护自己的本地库 | 从当前版本开始，按 `wiki-query -> wiki-reflect -> wiki-lint -> wiki-ingest` 推进 |

> [!TIP]
> 建议直接用 Obsidian 打开仓库，并使用双链笔记、反向链接和页面跳转在 `wiki/`、`threads/` 和原文入口之间来回查看。

## 初始化

### 环境

- Python `3.11`
- `uv`

如果你要在本地更新论文和解析结果，还需要：

- `pdfinfo`
- `pdftotext`
- `docling`
- `marker_single`

`uv sync` 会安装项目依赖，其中包括 `docling` 和 `marker-pdf`。

```bash
uv sync
```

### 获取本地数据

1. 克隆仓库并初始化 submodule

```bash
git clone https://github.com/guanweifan/efficient-vla-wiki.git
cd efficient-vla-wiki
git submodule update --init --recursive
```

2. 拉取 `raw/`

```bash
uv run python scripts/release/fetch_raw.py --dry-run
uv run python scripts/release/fetch_raw.py
```

3. 拉取 `extracts/`

```bash
uv run python scripts/release/sync_hf_extracts.py pull
```

## 仓库结构

```text
.
├── raw/                         # 原始 PDF，按 manifest 拉取到本地
├── extracts/                    # 解析结果，从 Hugging Face 拉取
│   ├── meta/                    # 全局状态文件
│   └── parses/                  # 按论文存放的解析目录
├── wiki/                        # 稳定知识层
│   ├── papers/                  # 单篇论文页
│   ├── evidence/                # 可复用证据页
│   └── synthesis/               # 跨论文主题页
├── threads/                     # 本地 query 报告，可作为你自己的工作区
├── external/                    # 外部输入源
│   └── awesome-efficient-vla/   # 默认论文增量来源，包含 update.md
├── scripts/                     # 数据层和同步脚本
│   ├── build_extracts.py        # 需要时补建解析结果
│   ├── ingest_update.py         # 按 update.md 拉取新论文并补 extracts
│   └── release/                 # 拉取 raw、同步 extracts、整理分发文件
├── docs/                        # 使用说明和模板
│   └── templates/               # 单篇页、证据页、主题页模板
├── AGENTS.md                    # 协作规则
└── WIKI_SCHEMA.md               # wiki 结构和维护规则
```

## 四个 skill

- `wiki-query`：用现有 `wiki` 写 query 报告，输出到 `threads/query/*.md`
- `wiki-reflect`：把 `threads/` 里已经站稳的内容写回 `wiki`
- `wiki-lint`：检查 `wiki` 的结构、证据链和控制文件
- `wiki-ingest`：跟进 `update.md` 里的新论文，并把结果更新到 `wiki`

更详细的使用路径见 [docs/usage.md](docs/usage.md)。

## 跟随官方版本使用

### 更新到最新版本

```bash
git pull --rebase
git submodule update --init --recursive
uv run python scripts/release/fetch_raw.py
uv run python scripts/release/sync_hf_extracts.py pull
```

### 基于现有 `wiki` 做 query

主入口是 `wiki-query`。它会先在 `wiki/` 里找相关内容，关键处再回到 `raw/`，结果写进 `threads/query/*.md`。

以下为使用示例：

1. 研究地图

   `Prompt`
   > 请你系统分析一下当前 Efficient VLA 的主要研究方向，梳理目前大致可以分成哪些核心类别，每一类分别在解决什么问题、为什么重要、彼此之间的边界和联系是什么，并结合代表性工作形成一份带有综述视角的全景式调研，帮助我快速建立对这一领域整体格局的清晰认识。

   `Sample Query`
   [q0001-efficient-vla-research-map](threads/query/q0001-efficient-vla-research-map.md)

2. 基线选择

   `Prompt`
   > 请你系统分析一下当前常用的 Efficient VLA baseline 都有哪些，它们分别属于什么类型、在社区中的使用分布如何、各自的优缺点是什么，以及如果我想选择一个合适的开源 baseline 作为后续修改和实验的 code base，应该重点考虑哪些因素，并给出尽量具体、实用的选择建议。

   `Sample Query`
   [q0002-vla-baselines-recent](threads/query/q0002-vla-baselines-recent.md)

3. 专题追踪

   `Prompt`
   > 请你详细分析一下当前 VLA 中与 token 剪枝相关的工作，梳理这一方向已经有哪些代表性方法，它们各自的核心思路和适用场景是什么，同时比较它们与传统 VLM token 剪枝工作的区别，说明 VLA 场景下问题的特殊性在哪里、现有方法还存在哪些不足，以及未来最值得继续推进的方向是什么。

   `Sample Query`
   [q0003-vla-token-pruning-landscape](threads/query/q0003-vla-token-pruning-landscape.md)


## 维护自己的本地知识库

### 常见顺序

1. 用 `wiki-query` 写问题报告
2. 用 `wiki-reflect` 把稳定结果写回 `wiki`
3. 用 `wiki-lint` 做检查和收口
4. 有新论文时再用 `wiki-ingest`

### 把 query 结果写回 `wiki`

主入口是 `wiki-reflect`。它会把 `threads/` 里已经站稳的内容写回单篇页、证据页或主题页。

### 检查 `wiki`

主入口是 `wiki-lint`。它会重点检查：

- 断链
- 证据链缺口
- `papers / evidence / synthesis` 三层分工
- `wiki/index.md`、`wiki/log.md`、`wiki/status.json`

### 只跟进 `update.md` 里的最新论文

主入口是 `wiki-ingest`。

默认增量来源固定为 `external/awesome-efficient-vla/update.md`。

这一路径会做这些事：

1. 读取 `update.md`
2. 下载缺失 PDF 到 `raw/`
3. 补对应的 `extracts/`
4. 更新受影响的 `wiki/papers/`
5. 按需要更新 `wiki/evidence/`、`wiki/synthesis/`
6. 同步 `wiki/index.md`、`wiki/log.md` 和 `wiki/status.json`

## 数据和许可

- 数据获取和同步方式见 [docs/data-and-sync.md](docs/data-and-sync.md)
- 仓库自写内容采用 `MIT`
- `raw/` 和 `extracts/` 不在仓库 `MIT` 许可证内，复用前先检查上游许可

## 引用

论文范围建立在 [awesome-efficient-vla](external/awesome-efficient-vla/README.md) 之上。引用论文列表或 survey 时，优先引用上游工作：

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

仓库本身的引用信息见 [CITATION.cff](CITATION.cff)。
