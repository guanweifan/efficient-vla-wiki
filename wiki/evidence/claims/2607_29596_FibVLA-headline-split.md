# 2607_29596_FibVLA-headline-split

## 用途
- 服务于 [[wiki/papers/2607_29596_FibVLA.md|FibVLA]]，拆分 history sampling、action recurrence 与 feature reuse。

## Evidence
- 方法证据命题：FibVLA 用 logarithmic hindsight sampling 压缩历史，并以 Fibonacci recurrent inference 对齐后续 action chunks 与历史 feature tokens。来源：[[raw/2607_29596_FibVLA.pdf]]，Abstract、Sec. 3.4。
- 分类证据命题：主要减少 temporal history 编码与跨步重复，属于 temporal sharing/reuse。
- 待核证据命题：cache reuse、history coverage、latency 与 task result 要回到同配置实验。

## Table / Metric Anchors
- **Sec. 3.4**：Fibonacci recurrence 与 cache alignment。
- **Experiments / Ablation**：sampling、reuse、latency 与 performance 待核。

## Table / Metric Split
- history token count、cache hit/reuse、policy latency 与 task success 不同。
- flow-matching action expert 本身的 NFE 不应由 temporal route 推断。

## 不可混写项
- 不把 sparse sampling 单独写成 KV reuse 的全部来源。
- 不把 cross-step feature reuse 写成 action-step reduction。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页保留 sampling、reuse 与 action generation 三层。
