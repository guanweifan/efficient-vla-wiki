# wiki-ingest example

## 示例 1

先从 `update.md` 吸收新论文，再落到 `wiki/`：

```text
使用 wiki-ingest，读取 external/awesome-efficient-vla/update.md。
先运行：
- .venv/bin/python scripts/ingest_update.py --source external/awesome-efficient-vla/update.md --json

然后对本轮新增论文：
- 建立或补强对应的 wiki/papers/<stem>.md
- 写清 Claim、Methodology Index、Data Pointer
- 默认先读 raw PDF、pdftotext 和 bbox；只有需要章节/表格/图片时再查 extracts 里的 Docling/Marker
- 做 impact analysis，检查哪些 evidence / synthesis 页面需要同步更新
- 更新 wiki/index.md 和 wiki/log.md
如果某篇论文带来新的共享口径或高价值图表，再继续补 L2。
```

## 示例 2

只处理指定 arXiv：

```text
使用 wiki-ingest，只处理 2604.04161 和 2604.05672。
先运行：
- .venv/bin/python scripts/ingest_update.py --source external/awesome-efficient-vla/update.md --only-arxiv 2604.04161 2604.05672 --json

然后逐篇完成 L1，并判断是否需要更新现有 evidence / synthesis 页面。
```

## 示例 3

只看本轮会新增什么，不落盘：

```text
使用 wiki-ingest，先做 dry-run：
- .venv/bin/python scripts/ingest_update.py --source external/awesome-efficient-vla/update.md --dry-run --json

根据 dry-run 结果决定本轮 ingest 范围，再正式执行。
```
