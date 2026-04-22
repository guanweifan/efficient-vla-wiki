---
name: wiki-ingest
description: 用于把 raw/ 中新增或变更的论文增量吸收到 wiki/。适合在需要补单篇页、做影响分析并更新受影响页面时使用。
---

# Wiki Ingest

## 用途

这个技能用来吸收新增论文，并把它们写进现有 `wiki/`。

适合这些情况：

- `raw/` 里有了新 PDF
- 某篇论文还没有单篇页
- 新论文已经影响到现有证据页或主题页

## 不适合的情况

- 仓库还没有基本骨架
- 需要重做整库整理
- 只是修断链、修计数或做收口检查

## 先读什么

- `AGENTS.md`
- `WIKI_SCHEMA.md`

## 输入

- 一个 `update.md` 风格的候选列表
- 一个或多个 `raw/*.pdf`
- 必要时附带用户当前关心的问题

如果本地有 `external/awesome-efficient-vla/update.md`，可以把它当成候选源之一。

## 核心规则

- `raw/` 是唯一事实来源。
- `extracts/` 用来定位和回读。
- `scripts/ingest_update.py` 负责补 `raw/` 和 `extracts/`。
- `wiki-ingest` 负责在此基础上更新 `wiki/`。
- 单篇页优先，证据页和主题页按需更新。
- 一轮 ingest 只围绕本轮新增论文做定点传播。
- 受影响页面要跟着更新，不能只停在新增单篇页。

## 建议流程

1. 先用 `scripts/ingest_update.py` 看本轮会处理哪些论文。
2. 下载缺失 PDF。
3. 为新增论文补局部 `extracts/`。
4. 建立或补强对应的 `papers/<stem>.md`。
5. 做影响分析，判断会影响哪些：
   - `papers/`
   - `evidence/`
   - `synthesis/`
   - `wiki/index.md`
6. 只更新真正受影响的页面。
7. 同步 `wiki/log.md` 和必要的 `wiki/status.json`。

## 工具入口

先看计划：

```bash
uv run python scripts/ingest_update.py --dry-run --json
```

正式执行：

```bash
uv run python scripts/ingest_update.py --json
```

只处理指定 arXiv：

```bash
uv run python scripts/ingest_update.py --only-arxiv 2604.04161 2604.05672 --json
```

## 输出

- `raw/` 和 `extracts/` 已补齐
- 本轮新增论文对应的 `papers/<stem>.md`
- 必要的 `evidence/` 更新
- 必要的 `synthesis/` 更新
- 同步后的 `wiki/index.md`、`wiki/log.md` 和 `wiki/status.json`

## 转交条件

- 新论文只是下载到了本地，还没办法稳定写进 `wiki/`：继续补原文和证据
- 问题已经变成 thread 里的稳定结论回写：转 `wiki-reflect`
- 问题已经变成断链、漏链、控制文件失配：转 `wiki-lint`
- 某个主题要大改：转周期维护

## 禁止事项

- 不把 parser 输出当事实来源。
- 不把新增论文机械追加到主题页末尾。
- 不在证据还没站稳时直接写大段主题结论。
- 不为 ingest 额外生成一堆长期保留的中间文件。

## 验收

- 本轮目标论文已经具备 `raw/<stem>.pdf`
- 对应的 `extracts/` 已经补齐
- 每篇新增论文都有可用的单篇页
- 受影响页面已经更新，或者已经说明为什么这轮不动
- `wiki/index.md`、`wiki/log.md` 和必要的 `wiki/status.json` 已同步
