# 2605_30011_VisualThink-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_30011_VisualThink-VLA.md|2605_30011_VisualThink-VLA]] 的单篇证据落点，用来拆分 visual intermediate reasoning、selective evidence routing、success-latency trade-off 与 dataset/audit contribution。
- 本页聚焦的 headline bundle：`visual evidence interface`、`selective routing`、`sub-second reasoning latency`、`VisualEvidence-Kit / Set` 需要分层阅读。

## Evidence
- 方法证据命题：VisualThink-VLA 用 compact visual-evidence interface 替代 long textual CoT，并通过 selective routing 暴露 task-relevant evidence tokens。来源：[[raw/2605_30011_VisualThink-VLA.pdf]]，Abstract、Figure 1、Figure 2。
- 数据/监督证据命题：VisualEvidence-Kit 和 VisualEvidence-Set 提供 route supervision 与 audit；这支撑 evidence routing，但不应写成推理期必需人工流程。来源：[[raw/2605_30011_VisualThink-VLA.pdf]]，Abstract、Figure 3、Figure 4、Table 7。
- 结果证据命题：Table 2 / Figure 5 把 success 与 latency 作为 paired trade-off 呈现；Table 3 进一步测试 backbone portability。来源：[[raw/2605_30011_VisualThink-VLA.pdf]]，Table 2、Figure 5、Table 3。

## Table / Metric Anchors
- **Figure 1**：method overview and success-latency teaser。
- **Figure 2**：VisualThink-VLA pipeline。
- **Figure 3 / Figure 4**：VisualEvidence-Set / Kit construction。
- **Table 2 / Figure 5**：success-latency comparison across benchmarks。
- **Table 3**：backbone portability。
- **Table 4 / Figure 9**：internal interface and evidence orchestration ablations。
- **Table 5**：real-robot closed-loop evaluation。

## Table / Metric Split
- latency speedup is primarily against reasoning-augmented textual baselines and dense evidence variants.
- success gains and latency reductions should be read as paired operating points.
- Visual evidence tokens are reasoning substrate, not necessarily pruning keep-ratio tokens.

## 不可混写项
- 不应把 VisualThink-VLA 写成 generic visual token pruning method。
- 不应把 training-only supervision paths counted as inference modules。
- 不应 compare ECoT latency, pruning FLOPs and quantization memory as a single scale。

## 影响页面
- [[wiki/papers/2605_30011_VisualThink-VLA.md|2605_30011_VisualThink-VLA]]
- [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
