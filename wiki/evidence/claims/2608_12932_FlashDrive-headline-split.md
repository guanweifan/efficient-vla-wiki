# 2608_12932_FlashDrive-headline-split

## 用途
- 服务于 [[wiki/papers/2608_12932_FlashDrive.md|FlashDrive]]，拆分四阶段算法收益、系统优化、量化与 closed-loop simulation。

## Evidence
- 方法证据命题：FlashDrive 分别用 streaming reuse、diffusion speculative draft、adaptive flow-step cache 处理 encode/prefill、reasoning decode 与 action stages，并叠加 CUDA Graph/kernel fusion/W4A8。来源：[[raw/2608_12932_FlashDrive.pdf]]，Sec. 3。
- latency 证据命题：RTX PRO 6000 上 Alpamayo 1.5-10B 从 716.9 ms 降至 151.4 ms；最终行同时包含全部算法、系统优化与 W4A8。来源：[[raw/2608_12932_FlashDrive.pdf]]，Table 1。
- closed-loop 证据命题：AlpaSim 中 rollout latency 从 1150 降至 463 ms；collision/off-road 下降，Wrong Lane 上升，且 metric 包含 inference、trajectory optimization 与 simulator rendering。来源：[[raw/2608_12932_FlashDrive.pdf]]，Table 3、Appendix Table A3。

## Table / Metric Anchors
- **Table 1-2**：stage ablation 与 cross-device latency。
- **Table 3 / Table A3**：closed-loop metric definitions 与 rollout scope。

## Table / Metric Split
- encode、prefill、reasoning decode、action、system overhead 与 quantization 的收益分层。
- model inference latency、control Hz 与 simulator rollout latency 不可互换。

## 不可混写项
- 不把 4.7x 归因给 cross-frame cache 或任一单项技术。
- 不因 collision/off-road 改善而省略 Wrong Lane 退化或 simulation setting。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 当前 closed-loop evidence 来自 AlpaSim，未覆盖 real-vehicle sensor/actuator/network path。
