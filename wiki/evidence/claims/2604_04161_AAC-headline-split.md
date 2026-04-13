# 2604_04161_AAC-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_04161_AAC.md|2604_04161_AAC]] 的单篇证据落点，用来固定 AAC 的方法边界和后续主表入口。

## Evidence
- 核心证据命题：`AAC` 用 action entropy 在 inference-time 动态决定 chunk size，以平衡 consistency 与 reactivity。来源：[[raw/2604_04161_AAC.pdf]]，Abstract；方法部分。
- 补充证据命题：它强调自己无需额外训练或架构修改，主要改的是 chunk scheduling policy。来源：[[raw/2604_04161_AAC.pdf]]，Abstract；Introduction。

## Table / Metric Anchors
- **Fig. 1**：固定 chunk size 在不同任务上的敏感性。
- **Table 1**：RoboCasa / LIBERO 主结果。
- **后续真实世界实验**：适合后续补 simulated vs real-world 的结果差异。

## 不可混写项
- 当前论文的主 headline 仍主要是“优于固定 chunk 与若干基线”这一层。
- 后续必须把 benchmark、chunk size、success rate 和 inference scheduling 分开写。

## 影响页面
- [[wiki/papers/2604_04161_AAC.md|2604_04161_AAC]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]

## 边界
- 本页只承载单篇 chunk scheduling claim，不与 single-step action generation 或 streaming execution 直接混写。
