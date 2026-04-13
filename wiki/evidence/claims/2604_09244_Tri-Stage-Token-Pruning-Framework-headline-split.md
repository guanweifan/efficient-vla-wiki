# 2604_09244_Tri-Stage-Token-Pruning-Framework-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_09244_Tri-Stage-Token-Pruning-Framework.md|2604_09244_Tri-Stage-Token-Pruning-Framework]] 的单篇证据落点，用来拆开 MVLA、tri-stage salience analysis 和 speedup / overhead headline。

## Evidence
- 核心证据命题：这篇论文把 MVLA 的 pruning 问题写成 2D / 3D modality salience 在三个阶段中的差异与动态。来源：[[raw/2604_09244_Tri-Stage-Token-Pruning-Framework.pdf]]，Abstract；Introduction；Fig. 1。
- 补充证据命题：对应的 tri-stage pruning framework 面向 data preprocessing、semantic synthesis、action iteration 三个阶段分别做 modality-aware token selection。来源：[[raw/2604_09244_Tri-Stage-Token-Pruning-Framework.pdf]]，Sec. 3。

## Table / Metric Anchors
- **Abstract / main result table**：`2.55×` speedup 与 `5.8%` overhead。
- **RLBench 主实验表**：适合后续拆 pruning ratio 与 success rate。
- **overhead / ablation 表**：适合后续补三阶段各自的贡献。

## 不可混写项
- `2.55× inference speedup`
- `5.8% overhead`
- `minimal accuracy loss`
- 这些都需要和具体 pruning ratio、MVLA setting 与 RLBench 任务结果一起读。

## 影响页面
- [[wiki/papers/2604_09244_Tri-Stage-Token-Pruning-Framework.md|2604_09244_Tri-Stage-Token-Pruning-Framework]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]

## 边界
- 本页只承担单篇 MVLA pruning claim 的收口，不替代 2D-only 与 2D+3D 路线的跨论文建模。
