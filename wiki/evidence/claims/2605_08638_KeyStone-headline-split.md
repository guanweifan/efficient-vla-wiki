# 2605_08638_KeyStone-headline-split

## 用途
- 服务于 [[wiki/papers/2605_08638_KeyStone.md|KeyStone]] 的单篇证据落点，拆分 action selection、额外采样成本与任务表现。
- 本页是 L1 scan-layer evidence，不承担跨论文路线排序。

## Evidence
- 方法证据命题：KeyStone 从共享模型上下文并行生成多个 action chunks，在连续动作空间聚类，并选择最大簇 medoid。来源：[[raw/2605_08638_KeyStone.pdf]]，Abstract、Sec. 1。
- 分类证据命题：作用对象是生成后的动作候选，主维护路线为 `Raw Action Generation`；其 training-free 并行推理属于次级 inference relevance。
- 待核证据命题：成功率收益、candidate count 与 latency overhead 需要回到对应实验设置逐项记录。

## Table / Metric Anchors
- **Abstract / Method**：candidate generation、clustering、medoid selection。
- **Experiments / Results**：task success、K、latency 与模型/硬件设置待核。

## Table / Metric Split
- wall-clock latency、总 test-time compute 与任务成功率不能合成一个“无成本提升”命题。
- training-free 不等于 zero-compute-overhead。

## 不可混写项
- 不把并行候选在特定 GPU 上的开销结论泛化到任意硬件。
- 不把 action-space self-consistency 写成 action decoder 本身被压缩。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页只承担 KeyStone 的单篇 headline 证据拆分。
