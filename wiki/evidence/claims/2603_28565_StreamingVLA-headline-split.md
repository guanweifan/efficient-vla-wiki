# 2603_28565_StreamingVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_28565_StreamingVLA.md|2603_28565_StreamingVLA]] 的单篇证据落点，用来拆开 streaming 执行、latency speedup 与 halting reduction。

## Evidence
- 核心证据命题：`StreamingVLA` 通过 action flow matching 与 adaptive early observation，把 observation、generation、execution 改写成可重叠的 streaming pipeline。来源：[[raw/2603_28565_StreamingVLA.pdf]]，Abstract；Sec. 3；Sec. 4。
- 补充证据命题：其重点是 stage-wise parallelism，而不是普通 pruning / cache reuse。来源：[[raw/2603_28565_StreamingVLA.pdf]]，Introduction；Fig. 1。

## Table / Metric Anchors
- **Abstract / Fig. 1**：`2.4×` latency speedup 与 `6.5×` halting reduction 的第一锚点。
- **runtime analysis section**：适合后续补 `Thalt` 与有效 latency 定义。
- **主实验表**：适合后续拆 task success、latency 与 halting 的关系。

## 不可混写项
- `2.4× latency speedup`
- `6.5× execution halting reduction`
- 这两类指标都属于 runtime pipeline 口径，不应直接和 task success 压成一条 superiority claim。

## 影响页面
- [[wiki/papers/2603_28565_StreamingVLA.md|2603_28565_StreamingVLA]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]

## 边界
- 本页只承担单篇 streaming claim 的落点，不承担与现有 `StreamVLA` 的 taxonomy 融合。
