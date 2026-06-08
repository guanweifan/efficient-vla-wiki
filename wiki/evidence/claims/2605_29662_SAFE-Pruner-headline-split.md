# 2605_29662_SAFE-Pruner-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_29662_SAFE-Pruner.md|2605_29662_SAFE-Pruner]] 的单篇证据落点，用来拆分 future-aware pruning、semantic attention consistency、adaptive subtask division 与 success-latency headline。
- 本页聚焦的 headline bundle：`future-layer attention forecast`、`plug-and-play pruning`、`up to 1.89x speedup`、`<1.7% success degradation` 需要分层阅读。

## Evidence
- 方法证据命题：SAFE-Pruner uses semantic attention consistency to forecast late-stage token saliency from historical frames, reducing short-sighted pruning risk. 来源：[[raw/2605_29662_SAFE-Pruner.pdf]]，Abstract、Figure 1、Introduction。
- 控制机制命题：adaptive subtask division detects attention shifts so reference frames stay within the same subtask-like context. 来源：[[raw/2605_29662_SAFE-Pruner.pdf]]，Abstract、method section、Table 4。
- 结果证据命题：论文在 LIBERO、SIMPLER and real-robot tasks 上报告 FLOPs/latency reduction with task success; benchmark-specific values must be read separately. 来源：[[raw/2605_29662_SAFE-Pruner.pdf]]，Table 1、Table 2、Table 3。

## Table / Metric Anchors
- **Figure 1**：shallow-only pruning vs SAFE-Pruner comparison。
- **Table 1**：LIBERO success, FLOPs and latency across models。
- **Table 2**：SIMPLER Visual Matching / Variant Aggregation results。
- **Table 3**：real robot success, FLOPs and VLM backbone latency。
- **Table 4**：forecast / division ablation。

## Table / Metric Split
- speedup, FLOPs and backbone latency are related but not identical.
- success degradation must be tied to baseline, benchmark and acceleration setting.
- future-aware pruning differs from semantic-only shallow pruning because it predicts deeper-layer saliency.

## 不可混写项
- 不应把 SAFE-Pruner 写成 action generation compression。
- 不应把 real-robot VLM backbone latency written as full-system latency。
- 不应 claim universal training-free compatibility beyond evaluated architectures。

## 影响页面
- [[wiki/papers/2605_29662_SAFE-Pruner.md|2605_29662_SAFE-Pruner]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
