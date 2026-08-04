# 2607_13960_GigaWorld-Policy-0.5-GWP-0.5-headline-split

## 用途
- 服务于 [[wiki/papers/2607_13960_GigaWorld-Policy-0.5-GWP-0.5.md|GWP-0.5]]，拆分 action-only model path、native runtime 与 AutoResearch。

## Evidence
- 方法证据命题：GWP-0.5 在训练时使用 visual dynamics，在部署时只解码动作，并配套 KV caching、graph compilation 与 C++ runtime。来源：[[raw/2607_13960_GigaWorld-Policy-0.5-GWP-0.5.pdf]]，Abstract、method/deployment sections。
- 分类证据命题：action-only inference 是主模型路线，native runtime 是独立次级 deployment 机制。
- 待核证据命题：latency、active compute 与 task performance 需要按 base/runtime 配置拆分。

## Table / Metric Anchors
- **Method / Deployment**：action-only path 与 runtime stack。
- **Experiments / Ablation**：latency、success、runtime gain、AutoResearch comparison 待核。

## Table / Metric Split
- model architecture gain 与 compiler/runtime gain 不同。
- AutoResearch 搜索结果与训练计算成本不是同一命题。

## 不可混写项
- 不把未来视频监督写成部署期未来视频生成。
- 不把 native runtime 的总收益全归因于轻量 action expert。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页明确分开 model path、runtime 与 training search。
