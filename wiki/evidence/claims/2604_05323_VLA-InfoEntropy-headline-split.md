# 2604_05323_VLA-InfoEntropy-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_05323_VLA-InfoEntropy.md|2604_05323_VLA-InfoEntropy]] 的单篇证据落点，用来拆开 entropy-based token selection 的多组效率 headline。

## Evidence
- 核心证据命题：`VLA-InfoEntropy` 用 visual entropy、attention entropy 和 timestep 信息做 training-free token selection。来源：[[raw/2604_05323_VLA-InfoEntropy.pdf]]，Abstract；Introduction。
- 补充证据命题：它把 `VLA-Cache` reuse 作为基础机制之一，但论文新的主增量是 entropy-guided selection policy。来源：[[raw/2604_05323_VLA-InfoEntropy.pdf]]，Fig. 1；方法部分。

## Table / Metric Anchors
- **主实验表**：`76.4%` average success、`34.9%` FLOPs reduction、`39.8%` CUDA latency reduction。
- **benchmark-specific rows**：`86.4%` LIBERO-Spatial success 与其他子 benchmark。
- **hyperparameter sensitivity / ablation**：适合后续补 token 数量与 success / latency tradeoff。

## 不可混写项
- `1.53× speedup`
- `34.9% FLOPs reduction`
- `39.8% CUDA latency reduction`
- `76.4% average success`
- `86.4% LIBERO-Spatial success`
- 这些数字涉及不同 benchmark 与指标，不应压成统一 headline。

## 影响页面
- [[wiki/papers/2604_05323_VLA-InfoEntropy.md|2604_05323_VLA-InfoEntropy]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]

## 边界
- 本页只承担单篇 entropy-based selection 的 claim 落点，不提前上升成通用共享 metric 页。
