# 2607_12931_ExToken-headline-split

## 用途
- 服务于 [[wiki/papers/2607_12931_ExToken.md|ExToken]]，拆分 structured exploration、interaction budget 与训练收益。

## Evidence
- 方法证据命题：ExToken 以 demonstrations 中的 behavioral priors 构造 token-conditioned policies，并用 state-conditioned selector 组织在线探索。来源：[[raw/2607_12931_ExToken.pdf]]，Abstract、Sec. 1。
- 分类证据命题：目标是有限 interaction budget 下的 RL fine-tuning，属于 training/adaptation efficiency。
- 待核证据命题：收敛速度、交互量和最终任务表现需回到同一 training protocol。

## Table / Metric Anchors
- **Method**：behavior token 与 selector。
- **Experiments**：interaction budget、learning curve、wall-clock 与 success 待核。

## Table / Metric Split
- environment steps、rollout count、GPU time 与 success rate 不是同一指标。
- offline demonstration cost 与 online interaction cost 需分开。

## 不可混写项
- 不把更快收敛写成 inference acceleration。
- 不把 behavioral tokens 自动归为 inference-time reasoning。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页只承担 online RL sample-efficiency evidence。
