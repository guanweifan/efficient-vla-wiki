# 2608_02365_Faster-WAM-DoT-headline-split

## 用途
- 服务于 [[wiki/papers/2608_02365_Faster-WAM-DoT.md|Faster-WAM / DoT]]，拆分 action-module depth、video backbone 与 end-to-end latency。

## Evidence
- 方法证据命题：Faster-WAM 在 30-layer video backbone 上 docking single-layer action head，并聚合多层 KV 后做 RoPE alignment。来源：[[raw/2608_02365_Faster-WAM-DoT.pdf]]，Abstract、Sec. 1。
- 分类证据命题：核心减少固定 action-module depth，属于 static architecture route。
- 待核证据命题：66.5 ms 与 3.2x headline 需要回到 controlled comparison 的 hardware/model setting。

## Table / Metric Anchors
- **Method**：DoT、KV-Fusion、RoPE realignment。
- **Controlled comparison**：latency、action-head depth、task result 待核。

## Table / Metric Split
- action-module compute、video-backbone compute、NFE 与 end-to-end latency 不同。
- task performance 与 latency comparison 需要保留 benchmark setting。

## 不可混写项
- 不把浅 action head 写成减少 denoising steps。
- 不把 controlled hardware result 泛化到任意 WAM stack。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页保留 architecture depth、sampling steps 与 runtime 三层。
