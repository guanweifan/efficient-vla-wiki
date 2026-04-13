# 2604_05672_A1-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_05672_A1.md|2604_05672_A1]] 的单篇证据落点，用来拆开 early exit、truncated flow matching 与多组 benchmark / deployment headline。

## Evidence
- 核心证据命题：`A1` 通过 action-consistency early exit 与 Inter-Layer Truncated Flow Matching 同时加速 backbone 与 action head。来源：[[raw/2604_05672_A1.pdf]]，Abstract；Sec. 3.3。
- 补充证据命题：论文把问题写成 full inference pipeline 的预算分配，而不是只优化单个子模块。来源：[[raw/2604_05672_A1.pdf]]，Introduction。

## Table / Metric Anchors
- **Abstract / Introduction**：`72%` latency reduction、`76.6%` computation reduction、`29.00%` RoboChallenge。
- **Table 1 / Table 2**：simulation 与 real-world success。
- **Table 5 / Table 6**：adaptive early-exit inference 的 accuracy / TFLOPs / latency。

## 不可混写项
- `up to 72% lower per-episode latency`
- `up to 76.6% backbone computation reduction`
- `29.00% RoboChallenge average success`
- `56.7% real-world mean success`
- `96.6% LIBERO success`
- 这些属于 latency、compute、simulation 和 real-world 四个不同层级。

## 影响页面
- [[wiki/papers/2604_05672_A1.md|2604_05672_A1]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]

## 边界
- 本页只服务单篇 full-pipeline acceleration 的 claim，不承担 open-source 生态层面的外延叙事。
