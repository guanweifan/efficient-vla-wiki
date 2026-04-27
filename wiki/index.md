# Wiki Index

## 当前状态

- 当前模式：`maintenance`
- 当前阶段：`incremental maintenance`
- 默认入口：`wiki-query -> wiki-reflect -> wiki-lint -> wiki-ingest`

## 当前规模

- `papers/`：`113`
- `evidence/claims/`：`113`
- 共享 `metrics/`：`3`
- 共享 `wording/`：`3`
- `synthesis/`：`6`

## 层级入口

- `papers/`：单篇论文页
- `evidence/`：可复用证据页
- `synthesis/`：跨论文主题页

## 主题结构

- 总纲 / 入口：[[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]
- 研究地图：[[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- 主题页：[[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- 主题页：[[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- 主题页：[[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
- 主题页：[[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]

## 使用方式

- 跟随当前版本直接做 query：先同步仓库、`raw/` 和 `extracts/`，再从 `wiki/` 写 `threads/query/*.md`
- 维护自己的本地知识库：按 `wiki-query -> wiki-reflect -> wiki-lint -> wiki-ingest` 推进
- 只跟进最新论文：默认读取 `external/awesome-efficient-vla/update.md`

## 当前维护重点

- 按增量方式吸收新论文
- 把稳定 thread 结论写回 `wiki`
- 保持 `papers / evidence / synthesis` 三层边界清楚
