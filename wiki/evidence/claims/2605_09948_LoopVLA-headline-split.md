# 2605_09948_LoopVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_09948_LoopVLA.md|2605_09948_LoopVLA]] 的单篇证据落点，用来拆分 recurrent architecture、sufficiency-guided early stopping、parameter reduction 与 throughput headline。

## Evidence
- 核心证据命题：LoopVLA 复用共享 Transformer block 做迭代 multimodal token refinement，并在每轮输出 candidate action 与 sufficiency score。来源：[[raw/2605_09948_LoopVLA.pdf]]，Abstract、Figure 2、Figure 3。
- 训练证据命题：sufficiency head 通过 self-supervised distribution alignment 学习，不依赖外部 sufficiency label。来源：[[raw/2605_09948_LoopVLA.pdf]]，Abstract、method section。
- 结果证据命题：论文在 LIBERO、LIBERO-Plus、VLA-Arena 上报告任务结果，并将参数减少与 throughput 提升分开呈现。来源：[[raw/2605_09948_LoopVLA.pdf]]，Tables 1-6、Figure 6。

## Table / Metric Anchors
- **Figure 1-3**：architecture and sufficiency mechanism。
- **Tables 1-3**：main benchmark results。
- **Tables 4-6 / Figure 6**：ablation and selected loop indices。

## Table / Metric Split
- 参数规模、迭代步数、throughput 与 task success 是不同口径。
- early stopping 是 policy 内部动态计算，不是外部 deployment scheduler。

## 不可混写项
- 不应写成 visual token pruning。
- 不应把 sufficiency score 写成显式人工标签。

## 影响页面
- [[wiki/papers/2605_09948_LoopVLA.md|2605_09948_LoopVLA]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
