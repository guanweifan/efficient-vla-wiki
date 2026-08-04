# 2607_28405_QuantWAMs-headline-split

## 用途
- 服务于 [[wiki/papers/2607_28405_QuantWAMs.md|QuantWAMs]]，拆分 PTQ calibration、block-level system metric 与 closed-loop result。

## Evidence
- 方法证据命题：QuantWAMs 在 coordinate-compatible modules 共享 activation evidence，以 joint video-action gradient 分配 precision，并用 reachable closed-loop states 修订 denoising-step protection。来源：[[raw/2607_28405_QuantWAMs.pdf]]，Abstract、Sec. 1。
- 分类证据命题：这是 PTQ/compression；按外部 taxonomy 位于 4.1，但不直接构成 training-step/GPU-hour reduction。
- 待核证据命题：memory 与 speedup 是 block-level Blackwell measurements，需要与 end-to-end task metrics 分开。

## Table / Metric Anchors
- **Method**：shared-basis calibration、saliency、rollout audit。
- **Evaluation / Backend scope**：W4A4-dominant config、memory、block speed、task result 待核。

## Table / Metric Split
- weight-plus-activation memory、block speed 与 robot-cycle latency 不同。
- PTQ calibration cost 与 model training cost 不同。

## 不可混写项
- 不把 block-level speedup 写成端到端控制链路 speedup。
- 不把 PTQ 归类标签写成训练成本已下降。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页保留 taxonomy 归类与主题证据资格之间的差异。
