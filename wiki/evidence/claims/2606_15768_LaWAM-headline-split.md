# 2606_15768_LaWAM-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2606_15768_LaWAM.md|2606_15768_LaWAM]] 的单篇证据落点，用来拆分新增论文的 headline、主效率瓶颈、secondary relevance 与后续待核 metric。
- 本页是 L1 scan-layer evidence；只承接 title / abstract / method-level 信息，不承担跨论文 synthesis。

## Evidence
- 方法证据命题：Replace pixel-space future video generation with compact latent visual subgoals, exposing predictive dynamics to the action policy while avoiding expensive reconstructed future rollouts. 来源：[[raw/2606_15768_LaWAM.pdf]]，Title、Abstract、method section。
- 分类证据命题：当前维护分类为 `2.1 Selective Feature Processing`；次级相关为 `3.1 Raw Action Generation`；该判断用于 wiki 路线入口，后续需要用 method details 与实验 setting 继续复核。
- 待核证据命题：如果论文报告 speedup、latency、memory、training cost、control frequency 或 success rate，需要分别回读对应 table / figure，不能只摘 headline。

## Table / Metric Anchors
- **Abstract / Introduction**：problem framing and claimed efficiency bottleneck。
- **Method section**：mechanism boundary and component placement。
- **Experiments / Results**：runtime, task, training, memory, deployment or ablation evidence 待核。

## Table / Metric Split
- 方法机制、成本口径和任务表现需要分开记录。
- primary category 与 secondary relevance 不应被写成同等强度的主贡献。
- 如果该论文属于 WAM / autonomous driving / runtime infrastructure 边界，应保留边界，不直接并入 manipulation VLA 主线比较。

## 不可混写项
- 不应把尚未细读的 speedup / memory / success headline 写成跨论文 superiority claim。
- 不应把维护分类当成论文原文结论。
- 不应把外部代码仓库或 README 作为事实来源替代 raw PDF。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
