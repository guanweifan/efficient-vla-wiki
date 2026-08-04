# 2606_27807_SpikeVLA-headline-split

## 用途
- 服务于 [[wiki/papers/2606_27807_SpikeVLA.md|SpikeVLA]]，拆分 spiking architecture、估算能耗与任务表现。

## Evidence
- 方法证据命题：SpikeVLA 由 spiking vision encoder、multimodal spiking language model 与 spiking action policy 组成。来源：[[raw/2606_27807_SpikeVLA.pdf]]，Abstract、Sec. 1。
- 分类证据命题：效率机制是固定模型组织替换，主维护路线为 `Static Backbone Selection`。
- 待核证据命题：memory、ACE 与 energy 数值需要回到效率表格及计算假设。

## Table / Metric Anchors
- **Method sections**：Spike-V / Spike-L / Spike-A。
- **Efficiency evaluation**：GPU memory、operation counts、energy model 与 task metrics 待核。

## Table / Metric Split
- 理论能耗估计、GPU latency、GPU memory 与真实设备功耗不是同一指标。
- VLN 成功指标与 manipulation success 不可直接比较。

## 不可混写项
- 不把估算 energy reduction 写成已实现的端侧板级功耗收益。
- 不把静态 SNN architecture 写成 runtime dynamic routing。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页保留 energy-estimation 与 hardware measurement 的边界。
