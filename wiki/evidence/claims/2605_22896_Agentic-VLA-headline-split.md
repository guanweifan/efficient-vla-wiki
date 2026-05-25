# 2605_22896_Agentic-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_22896_Agentic-VLA.md|2605_22896_Agentic-VLA]] 的单篇证据落点，用来拆分 online adaptation、language-guided exploration、experience memory 与 convergence / transfer claims。

## Evidence
- 核心证据命题：Agentic-VLA 由 Adaptive Reward Synthesis、Language-Guided Exploration 与 Experience Memory 构成，用于在线训练和适配。来源：[[raw/2605_22896_Agentic-VLA.pdf]]，Abstract、Figure 1、Algorithm 1。
- 结果证据命题：论文在 LIBERO 上报告 long-horizon、one-shot、cross-task transfer 与 training efficiency，并在 RoboTwin 2.0 hard setting 中评估。来源：[[raw/2605_22896_Agentic-VLA.pdf]]，Tables 1-4、Table 8。
- 消融证据命题：论文分析 reward adjustment、experience memory、decomposition quality 与 learning curves。来源：[[raw/2605_22896_Agentic-VLA.pdf]]，Tables 5-7、Figures 2-5。

## Table / Metric Anchors
- **Figure 1 / Algorithm 1**：framework and training。
- **Tables 1-4 / Table 8**：main results, transfer, convergence, RoboTwin。
- **Tables 5-7 / Figures 2-5**：ablation and mechanism analysis。

## Table / Metric Split
- success gain、one-shot result、cross-task transfer 与 convergence speed 是不同口径。
- language guidance 服务训练探索，不等于测试时 reasoning overhead。

## 不可混写项
- 不应写成 inference-time reasoning compression。
- 不应把 experience memory 写成 deployment cache。

## 影响页面
- [[wiki/papers/2605_22896_Agentic-VLA.md|2605_22896_Agentic-VLA]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
