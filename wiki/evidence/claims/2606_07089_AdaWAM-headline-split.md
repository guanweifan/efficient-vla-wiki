# 2606_07089_AdaWAM-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2606_07089_AdaWAM.md|2606_07089_AdaWAM]] 的单篇证据落点，用来拆分 adaptive textual/visual reasoning、dynamic routing、action-only fallback 与 inference-time trade-off。
- 本页聚焦的 headline bundle：`textual reasoning at task transitions`、`visual reasoning for fine manipulation`、`action-only default`、`inference time per step vs success` 需要分层阅读。

## Evidence
- 方法证据命题：AdaWAM uses a dynamic router to activate text reasoning or visual reasoning only when execution context requires them, otherwise defaulting to efficient action-only decoding. 来源：[[raw/2606_07089_AdaWAM.pdf]]，Abstract、Figure 1、Figure 3。
- 标注证据命题：trajectory cues and VLM verification produce subtask-transition and fine-manipulation labels for routing supervision. 来源：[[raw/2606_07089_AdaWAM.pdf]]，Figure 2、method section。
- 结果证据命题：Table 1, Table 2 and Table 3 report benchmark and real-world task performance, while Figure 6 explicitly positions success against inference time per step and task duration. 来源：[[raw/2606_07089_AdaWAM.pdf]]，Table 1、Table 2、Table 3、Figure 6。

## Table / Metric Anchors
- **Figure 1**：video-action joint, action-only and adaptive multimodal reasoning paradigm comparison。
- **Figure 2**：annotation pipeline。
- **Figure 3**：AdaWAM architecture。
- **Table 1**：LIBERO performance。
- **Table 2**：RoboTwin 2.0 performance。
- **Table 3**：real-world task results。
- **Figure 6**：inference time per step, success rate and duration。
- **Table 4**：unseen task generalization。

## Table / Metric Split
- textual reasoning, visual reasoning and action-only decoding are modes selected by context, not a fixed pipeline always executed together.
- success rate, inference time per step and task duration are related but distinct.
- annotation pipeline supports training and routing supervision; it is not a test-time human-in-the-loop mechanism.

## 不可混写项
- 不应把 AdaWAM written as always-on multimodal reasoning; the key claim is adaptive triggering.
- 不应 compare it with pure CoT VLA only by success without latency / duration context.
- 不应 merge WAM visual reasoning with VLA textual CoT compression without noting substrate difference.

## 影响页面
- [[wiki/papers/2606_07089_AdaWAM.md|2606_07089_AdaWAM]]
- [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
