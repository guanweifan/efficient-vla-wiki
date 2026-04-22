# 使用指南

这份文档补充说明几种常见用法，重点放在“你可以怎样用这个项目”。

## 1. 只做 query

想基于现有 `wiki` 写一份问题报告时，直接用 `wiki-query`。

默认顺序：

1. 先看 `wiki/synthesis/`
2. 再看 `wiki/evidence/`
3. 最后看 `wiki/papers/`
4. 关键处不稳，再回 `raw/`

结果会写到：

- `threads/query/*.md`

全新的问题通常会新建一个 query 文件；如果你是在已有主轴上继续追问，内容一般会继续补到对应 thread 里。

适合的问题：

- 研究路线梳理
- 方法分型
- 某个专题的代表工作
- 某类效率路线的边界和分歧

## 2. 把 query 结果写回 `wiki`

如果某个 thread 里的结论已经站稳，就用 `wiki-reflect`。

它会把内容按最小落点写回：

- `wiki/papers/`
- `wiki/evidence/`
- `wiki/synthesis/`

这一步适合做：

- 术语边界整理
- 共享 evidence 补页
- 主题页局部收紧

## 3. 检查 `wiki`

如果你想看 `wiki` 现在是否合理，就用 `wiki-lint`。

它会重点看：

- 断链
- `raw` 锚点
- 单篇页和证据页之间的链接
- 主题页的 `Evidence Links`
- `wiki/index.md`、`wiki/log.md`、`wiki/status.json`

## 4. 拉取最新版本

### 拉取最新 `wiki`

```bash
git pull --rebase
git submodule update --init --recursive
```

### 拉取最新 `raw/`

```bash
uv run python scripts/release/fetch_raw.py
```

### 拉取最新 `extracts/`

```bash
uv run python scripts/release/sync_hf_extracts.py pull
```

## 5. 在本地维护自己的版本

如果你想长期维护自己的 `wiki`，可以直接在本地继续使用：

- `wiki-query`
- `wiki-reflect`
- `wiki-lint`
- `wiki-ingest`

一条常见路径是：

1. 先基于现有 `wiki` 做 query
2. 把已经站稳的内容 reflect 回 `wiki`
3. 用 lint 做检查和收口
4. 有新论文时再 ingest

`threads/` 默认适合作为你自己的本地工作区来用。

## 6. 只跟进最新论文

如果你只想跟进 `update.md` 里的新论文，主入口就是 `wiki-ingest`。

默认来源固定为：

- `external/awesome-efficient-vla/update.md`

这个流程会依次完成：

1. 读取 `update.md`
2. 下载缺失 PDF
3. 补对应的 `extracts/`
4. 更新受影响的 `wiki`

这个流程会先用 `scripts/ingest_update.py` 准备 `raw/` 和 `extracts/`，再继续更新 `wiki`。

## 7. `extracts/` 的使用方式

大多数使用者只需要拉取最新版本的 `extracts/`：

```bash
uv run python scripts/release/sync_hf_extracts.py pull
```

只有在下面这些情况，才需要自己跑解析：

- 新增论文后本地补建
- 某篇论文的解析结果损坏
- 你想自己重跑某篇论文的解析结果

这时再用：

- `scripts/build_extracts.py`

## 8. 环境

基础使用环境：

- Python `3.11`
- `uv`

如果你要在本地补 `raw/` 和 `extracts/`，还需要：

- `pdfinfo`
- `pdftotext`
- `docling`
- `marker_single`

`uv sync` 会安装项目依赖，其中包括 `docling` 和 `marker-pdf`。
