# 2605_16241_VLA-AD-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_16241_VLA-AD.md|2605_16241_VLA-AD]] 的单篇证据落点，用来拆分 offline semantic guidance、teacher-student distillation、size / speed / success gap。

## Evidence
- 核心证据命题：VLA-AD 使用 VLM 生成 phase anchors 和 operating-direction descriptions，作为训练期语义监督来蒸馏大 VLA teacher 到轻量 student。来源：[[raw/2605_16241_VLA-AD.pdf]]，Abstract、Figure 1、Figure 2。
- 结果证据命题：论文报告 OpenVLA-7B teacher 到 158M student 的 size reduction、success gap、RTX4090 frequency / speedup，并扩展到 π0.5 teacher。来源：[[raw/2605_16241_VLA-AD.pdf]]，Abstract、Tables 1-3。
- 稳健性证据命题：论文分析 phase / direction guidance 对 noisy teacher actions 和 gripper oscillation 的作用。来源：[[raw/2605_16241_VLA-AD.pdf]]，Figure 4、Tables 4-6。

## Table / Metric Anchors
- **Figure 1-3**：pipeline, phase descriptions, vocabulary。
- **Tables 1-3**：closed-loop success and inference time。
- **Figure 4 / Tables 4-6**：noise / validation / per-task results。

## Table / Metric Split
- model size、Hz / speedup、success gap 和 semantic guidance ablation 分属不同口径。
- VLM 只作为 offline supervisor，不是 test-time reasoning agent。

## 不可混写项
- 不应写成 always-on VLM planner。
- 不应写成纯 architecture downsizing。

## 影响页面
- [[wiki/papers/2605_16241_VLA-AD.md|2605_16241_VLA-AD]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
