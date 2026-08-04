# 2607_27205_TurboVLA-headline-split

## 用途
- 服务于 [[wiki/papers/2607_27205_TurboVLA.md|TurboVLA]]，拆分 architecture、memory、latency 与 capability scope。

## Evidence
- 方法证据命题：TurboVLA 以轻量 visual/text encoders 和直接 continuous action chunk decoder 替代 LLM-centric pathway。来源：[[raw/2607_27205_TurboVLA.pdf]]，Abstract、Sec. 1。
- 分类证据命题：效率来自固定 compact architecture，主路线为 `Static Backbone Selection`。
- 待核证据命题：parameters、inference VRAM、latency、Hz 与 success 需绑定 RTX 4090 evaluation。

## Table / Metric Anchors
- **Method**：V+L-to-A pathway 与 compact decoder。
- **Experiments**：parameter count、VRAM、latency、Hz、success 待核。

## Table / Metric Split
- policy latency、action update frequency、VRAM 与 model parameters 不同。
- compact policy benchmark result 与 generalist reasoning capability 不同。

## 不可混写项
- 不把 consumer-GPU result 泛化为 edge-device performance。
- 不把低显存自动写成低训练成本。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页保留 hardware operating point 与 capability scope。
