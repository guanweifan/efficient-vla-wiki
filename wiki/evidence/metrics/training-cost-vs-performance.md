# training-cost-vs-performance

## 用途
- 当前页收敛 `training steps / GPU hours / preprocessing cost / data ratio / downstream performance` 这组最容易被混写的口径。
- 当前页只记录 source-grounded evidence 与不可混写项，不承担主题级 synthesis。

## Evidence
- [[wiki/papers/2501_09747_FAST.md|2501_09747_FAST]]：`training time by up to 5x` 不是单一指标；它在文中分别落到 `training steps`、`GPU hours` 与 compute-matched checkpoint 三种比较口径上，而且这些 headline 服务于 `π0-FAST vs diffusion π0` 的 training-efficiency 讨论，不应被误写成 inference latency。来源：[[raw/2501_09747_FAST.pdf]]，第 1 页 Abstract；第 9-10 页 Fig. 9、Fig. 11。
- [[wiki/papers/2511_16233_FT-NCFM.md|2511_16233_FT-NCFM]]：`5% synthetic data`、`85-90%` performance 与 `80%+ training-time reduction` 分别来自 `CALVIN Avg. Len`、`Meta-World / LIBERO success rate`、`Table 4 / Table 5` 成本分析；它们共同支持的是 data-centric efficiency，不是单一训练速度指标。来源：[[raw/2511_16233_FT-NCFM.pdf]]，第 6-7 页，Table 1-5。

## 不可混写项
- `training steps`、`GPU hours`、`one-time preprocessing cost`、`policy training time` 不是同一种训练成本指标。
- `更少数据达到接近性能` 与 `更少训练时间` 不是同一命题；必须明确 benchmark、metric 与 cost table。
- training-efficiency headline 不能被写成 inference speedup。

## 影响页面
- [[wiki/papers/2501_09747_FAST.md|2501_09747_FAST]]
- [[wiki/papers/2511_16233_FT-NCFM.md|2511_16233_FT-NCFM]]

## 边界
- 当前页只收敛训练成本与性能口径，不讨论哪一路线“更优”。
- 若如需讨论 data-centric efficiency 如何改变 VLA 训练范式，应留到主题建模阶段。
