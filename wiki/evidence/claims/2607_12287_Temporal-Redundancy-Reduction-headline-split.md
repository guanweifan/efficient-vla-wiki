# 2607_12287_Temporal-Redundancy-Reduction-headline-split

## 用途
- 服务于 [[wiki/papers/2607_12287_Temporal-Redundancy-Reduction.md|Temporal Redundancy Reduction]]，拆分视觉复用与 action-step compression。

## Evidence
- 方法证据命题：论文联合 selective visual-token refresh 与 learned two-step flow-matching policy。来源：[[raw/2607_12287_Temporal-Redundancy-Reduction.pdf]]，Abstract、Sec. 1。
- 分类证据命题：主要 headline 同时覆盖 action sampling 与 temporal perception；按主瓶颈归入 action generation，保留 temporal reuse 次级入口。
- 待核证据命题：over-2x system speedup 与 task result 需要绑定平台、baseline 和联合配置。

## Table / Metric Anchors
- **Method**：token update 与 two-step schedule。
- **Experiments / Ablation**：component latency、end-to-end latency 与 success 待核。

## Table / Metric Split
- perception latency、action-head latency 与 end-to-end latency 是三层指标。
- visual reuse 与 sampling compression 的贡献不能互相替代。

## 不可混写项
- 不把 two-step action generation 写成视觉 cache 收益。
- 不把摘要中的 system-level headline 脱离硬件条件泛化。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页明确保留双机制拆分。
