# 2608_03682_PhyAI-headline-split

## 用途
- 服务于 [[wiki/papers/2608_03682_PhyAI.md|PhyAI]]，拆分统一 runtime、单请求 latency、batch throughput 与 control-time boundary。

## Evidence
- 方法证据命题：PhyAI 以 adapter 保留 model-specific semantics，并在 onboard、edge、cloud 共用 graph、kernel、memory、cache 与 parallel services。来源：[[raw/2608_03682_PhyAI.pdf]]，Abstract、Sec. 1。
- 运行证据命题：对 11 个 official-path matched pairs 报告 1.40x-4.65x speedup，但比较并非完全 precision-matched，且 specialized runtime 在若干配置更快。来源：[[raw/2608_03682_PhyAI.pdf]]，Fig. 1、Sec. 5.5。
- 控制边界命题：control-time Roofline 以 inference time 与 environment execution window 区分 inference-bound / environment-bound；LIBERO 的 pi0.5 测点是后者。来源：[[raw/2608_03682_PhyAI.pdf]]，Sec. 1、Sec. 7.1。

## Table / Metric Anchors
- **Fig. 1**：single-request latency、matched hardware 与 precision notes。
- **Sec. 5.5 / Sec. 7.1**：measurement scope 与 control-time Roofline。

## Table / Metric Split
- single-request latency、batch throughput、RL rollout simulation 与 robot control rate 必须分开。
- official implementation speedup 与 specialized-runtime absolute latency 不是同一比较。

## 不可混写项
- 不把统一 runtime 写成所有 configuration 下最快。
- 不把 environment-bound timing margin 写成任务成功率或安全性的提升。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 当前证据只支持已测模型、设备、precision 与 workload，不支持任意 embodied policy 的通用性能排序。
