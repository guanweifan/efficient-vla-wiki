# 2604_05656_SnapFlow-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_05656_SnapFlow.md|2604_05656_SnapFlow]] 的单篇证据落点，用来拆开单步生成、速度指标和不同 model family 的结果。

## Evidence
- 核心证据命题：`SnapFlow` 通过 self-distillation 把 flow-matching VLA 的 multi-step denoising 压到 `1-NFE` 单步生成。来源：[[raw/2604_05656_SnapFlow.pdf]]，Abstract；Introduction。
- 补充证据命题：它强调自己与 layer distillation、token pruning 路线正交。来源：[[raw/2604_05656_SnapFlow.pdf]]，Abstract；Related Work。

## Table / Metric Anchors
- **Abstract / Introduction**：`98.75%`、`97.75%`、`9.6×`、`274 ms -> 83 ms`。
- **π0.5 main table**：适合后续拆 LIBERO 四个 suite 的 success。
- **SmolVLA table**：适合后续拆 `3.56×` 与 `8.3% MSE reduction`。

## 不可混写项
- `98.75% average success` vs `97.75% teacher`
- `9.6× denoising speedup`
- `274 ms -> 83 ms end-to-end latency`
- `3.56× end-to-end acceleration`
- `8.3% MSE reduction`
- 这些分别属于不同模型、不同指标与不同实验层。

## 影响页面
- [[wiki/papers/2604_05656_SnapFlow.md|2604_05656_SnapFlow]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]

## 边界
- 本页只承载单篇 action decoding compression 的 claim，不扩写成一般 consistency-model survey。
