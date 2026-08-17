# 2608_06994_PILOT-headline-split

## 用途
- 服务于 [[wiki/papers/2608_06994_PILOT.md|PILOT]]，拆分 Motion-CoT representation、few-shot data setting 与 inference pipeline latency。

## Evidence
- 方法证据命题：Representational Deduction 以 state-transition supervision 训练 Motion-CoT，并让 CDE 的 future latent prediction 与 action trajectory refinement 解耦。来源：[[raw/2608_06994_PILOT.pdf]]，Sec. 1、Sec. 3。
- few-shot 证据命题：Agibot-G1 的 10% data setting 下，PILOT / Fast-WAM average success 为 62.4% / 40.8%；完整数据下为 83.1% / 73.3%。来源：[[raw/2608_06994_PILOT.pdf]]，Table 4。
- latency 证据命题：RoboCasa 上 decoupled understanding path 为 111.60 ms / 8.26 Hz，50-step predict-then-act path 为 1329.95 ms / 0.75 Hz。来源：[[raw/2608_06994_PILOT.pdf]]，Appendix Sec. 7.3、Table 6。

## Table / Metric Anchors
- **Table 4-5**：real-world / few-shot 与 component ablation。
- **Table 6**：understanding-vs-generation pipeline comparison。

## Table / Metric Split
- Motion-CoT task gain、10% data retention 与 rollout-bypass latency 是三条独立证据。
- raw action-step timing、effective control frequency 与 pipeline latency 不可互换。

## 不可混写项
- 不把 10% data result 写成 90% wall-clock training saving。
- 不把相对 50-step predict-then-act 的 11.9x 泛化为相对所有 WAM。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- future-frame generation 在训练时提供 supervision、部署时 bypass；不能写成完全没有 world-model training cost。
