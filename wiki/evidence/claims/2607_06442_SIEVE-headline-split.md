# 2607_06442_SIEVE-headline-split

## 用途
- 服务于 [[wiki/papers/2607_06442_SIEVE.md|SIEVE]]，拆分数据比例、训练步骤与任务表现。

## Evidence
- 方法证据命题：SIEVE 基于 primitive-transition composition 评估 demonstration structure，并选择各模式中的代表性 medoid trajectories。来源：[[raw/2607_06442_SIEVE.pdf]]，Abstract、Sec. 1。
- 分类证据命题：收益作用于 imitation-learning data usage 与 training steps，主路线为 training efficiency。
- 待核证据命题：50% demonstrations / 50% steps 等 headline 需要绑定对应 benchmark 和 baseline。

## Table / Metric Anchors
- **Method**：primitive discovery、structural exposure、trajectory selection。
- **Experiments**：data ratio、steps、selection cost 与 performance 待核。

## Table / Metric Split
- 少数据、少训练步数与更高任务表现是三类证据。
- selection preprocessing cost 不能默认忽略。

## 不可混写项
- 不把单个 setting 的 full-data comparison 泛化为普遍结论。
- 不把 data efficiency 写成 inference acceleration。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页只承担 SIEVE 的 data-centric evidence。
