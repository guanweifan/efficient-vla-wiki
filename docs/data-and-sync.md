# 数据与同步

这份文档说明项目里的数据从哪里来，哪些内容在 Git 里，哪些内容要单独拉取。

## 内容分类

这个项目里的内容大致分成三类：

1. 仓库自写内容
   - 包括 `wiki/`、`docs/`、`.codex/skills/`、`scripts/`，以及本地使用的 `threads/`。
2. `raw/`
   - 第三方论文 PDF。
3. `extracts/`
   - 从 `raw/` 生成的解析结果。

## Git 里直接可用的部分

- `wiki/`
- `docs/`
- `.codex/skills/`
- `scripts/`
- `external/awesome-efficient-vla/`

`raw/` 和 `extracts/` 需要单独拉取到本地。

## `raw/` 怎么获取

- `raw/` 通过 `scripts/release/fetch_raw.py` 拉取到本地。
- 它保存原始 PDF。
- 你在做 query、reflect、lint、ingest 时，事实依据最终都要回到这里。

## `extracts/` 怎么获取

- `extracts/` 通过 Hugging Face dataset 拉取到本地。
- 使用的脚本是：
  - `scripts/release/sync_hf_extracts.py`
- 常规用法是直接拉取最新版本。

## `extracts/` 里有什么

- `pdftotext.txt`
- `pdftotext.bbox.html`
- `docling/*.md`
- `docling/*.json`
- figure / image 导出结果

这些内容用于检索、定位和回读。

## `update.md` 的作用

- 增量来源默认是：
  - `external/awesome-efficient-vla/update.md`
- 当你只想跟进最新论文时，`wiki-ingest` 会基于这份文件更新本地 `wiki`。

## 许可证

- 仓库自写内容采用 `MIT`

第三方论文 PDF、论文图片和从论文内容导出的解析结果，不在这个许可证里。

## Hugging Face 数据集

- `extracts/` 的公开分发走单独的 Hugging Face dataset repo。
- 当前仓库保留了同步脚本、数据集整理脚本、manifest 和数据集卡片模板。

## Manifest 和同步脚本

- `scripts/release/manifests/` 里的文件是操作元数据。
- `scripts/release/` 里的脚本用于抓取、同步和整理分发文件。

## 复用时

1. 先区分仓库自写内容和第三方论文内容。
2. `raw/` 和 `extracts/` 再分发前，先检查上游许可。
3. 不确定时，优先链接回上游来源。
