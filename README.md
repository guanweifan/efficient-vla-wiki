# efficient-vla-wiki

围绕 efficient VLA 论文搭建的研究知识库。

`raw/` 保存原始论文；`wiki/` 沉淀稳定知识；`threads/` 记录问题、讨论和阶段性结论。

## 项目定位

这个项目用于整理 efficient VLA 方向的论文材料，并把阅读、核对、归纳和维护放进同一套结构里。

仓库当前已经完成冷启动，后续以增量维护为主。

## 搭建流程

整个流程按 `Pass 0-5` 推进，先建立参考层，再补单篇页、证据层和主题层，最后做审计收口。

- `Pass 0 | Parse Baseline`：解析 `raw/*.pdf`，建立 `extracts/` 参考层，方便后续定位和回读。
- `Pass 1 | Semantic Scan`：逐篇建立 `wiki/papers/` 初版，先写清 `Claim`、`Methodology Index`、`Data Pointer`。
- `Pass 2 | Reverse Calibration`：从新到旧回看，校正旧术语、旧问题定义和过宽的 headline。
- `Pass 3 | Evidence Mining`：补关键 claim、图、表和 wording，把高价值信息落到 `wiki/evidence/`。
- `Pass 4 | Historical Reconciliation, Clustering and Modeling`：在 `papers + evidence` 之上做历史整合、主题聚类和 `wiki/synthesis/` 建模。
- `Pass 5 | Audit and Reflect`：审计链接、结构、控制文件和文档一致性，让仓库进入可维护状态。

## 四个 Skill

- `wiki-ingest`：处理新增论文，补单篇页，并更新受影响页面。
- `wiki-query`：围绕具体问题检索 `wiki/`，并把回答沉淀到 `threads/`。
- `wiki-reflect`：把 thread 中已经稳定、且重新核证过的内容回流到 `wiki/`。
- `wiki-lint`：做健康检查和定向修复，处理证据链、结构、链接和索引漂移。
