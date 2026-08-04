# 2607_12659_Jetson-PI-headline-split

## 用途
- 服务于 [[wiki/papers/2607_12659_Jetson-PI.md|Jetson-PI]]，拆分 model correction、scheduler 与 edge runtime。

## Evidence
- 方法证据命题：Jetson-PI 用 future representation correction 处理 prediction-execution misalignment，以 confidence 调度 VLM/action expert，并提供 onboard inference engine。来源：[[raw/2607_12659_Jetson-PI.pdf]]，Abstract、Sec. 1。
- 分类证据命题：主贡献位于 asynchronous deployment/runtime；跨步 context reuse 是次级机制。
- 待核证据命题：control-frequency improvement 与 success-rate comparison 要分别绑定 hardware 和 execution policy。

## Table / Metric Anchors
- **Method / System**：correction、scheduling、runtime optimizations。
- **Experiments**：latency、Hz、power、success 与 hardware setting 待核。

## Table / Metric Split
- model forward latency、reaction time、chunk update frequency 与 motor command frequency 不同。
- runtime optimization 与 learned correction 的收益需按 ablation 拆分。

## 不可混写项
- 不把异步 overlap 写成模型 FLOPs reduction。
- 不把不同设备上的频率直接用于算法 superiority。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页保留 onboard hardware 与 algorithm/runtime 两层边界。
