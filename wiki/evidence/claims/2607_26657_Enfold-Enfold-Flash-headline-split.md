# 2607_26657_Enfold-Enfold-Flash-headline-split

## 用途
- 服务于 [[wiki/papers/2607_26657_Enfold-Enfold-Flash.md|Enfold / Enfold-Flash]]，拆分 distillation、deployment bypass 与 TensorRT。

## Evidence
- 方法证据命题：Enfold 用 future-conditioned generator states 监督 current-only predictive encoder，部署时 action prediction 不运行 generator。来源：[[raw/2607_26657_Enfold-Enfold-Flash.pdf]]，Abstract、Sec. 1。
- 分类证据命题：效率机制通过训练期表示蒸馏获得，属于 training-side compression；部署期 generator bypass 是其推理结果。
- 待核证据命题：Enfold 与 Enfold-Flash latency 需要绑定同一硬件，并分离 TensorRT operator acceleration。

## Table / Metric Anchors
- **Method**：G2R、R2G、task-head gradient boundary。
- **Experiments**：base/Flash latency、success、representation analysis 待核。

## Table / Metric Split
- learned representation gain 与 operator/runtime gain 不同。
- training supervision cost 与 deployment latency 不同。

## 不可混写项
- 不把训练时访问 observed future 写成推理时使用未来输入。
- 不把 Enfold-Flash 全部收益归给 representation distillation。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页明确区分 model path 与 TensorRT path。
