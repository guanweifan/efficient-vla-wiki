# 2607_24008_FutureRTC-headline-split

## 用途
- 服务于 [[wiki/papers/2607_24008_FutureRTC.md|FutureRTC]]，拆分异步执行、状态预测与单次推理成本。

## Evidence
- 方法证据命题：FutureRTC 预测 execution-time observation/state，并使冻结 policy 在预测条件下的 action 与实际 execution-time condition 对齐。来源：[[raw/2607_24008_FutureRTC.pdf]]，Abstract、Introduction、method section。
- 分类证据命题：主问题是 asynchronous prediction-execution alignment，属于 deployment/runtime efficiency。
- 待核证据命题：delay robustness、completion speed、smoothness 与 success 需回到各自 metric。

## Table / Metric Anchors
- **Method**：state correction、observation prediction、policy consistency。
- **Experiments**：delay sweep、kinematics、completion time 与 success 待核。

## Table / Metric Split
- auxiliary module overhead 与被隐藏的 policy latency 需要分别记录。
- asynchronous throughput 与 single-forward latency 不同。

## 不可混写项
- 不把 delay compensation 写成 action decoder step reduction。
- 不把 smoother trajectory 自动写成更低模型 latency。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页只承担 asynchronous alignment evidence。
