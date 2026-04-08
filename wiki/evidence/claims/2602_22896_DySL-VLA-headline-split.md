# 2602_22896_DySL-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_22896_DySL-VLA.md|2602_22896_DySL-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`2.1%`、`85.7×`、`13.7×`、`3.75×` 等 headline 数字来自不同比较维度；仍需拆清哪些是 Calvin 上的 training-efficiency claim，哪些是 inference-latency claim。

## Evidence
- 这篇论文的核心问题是：VLA 推理加速不应对每个 action prediction 一视同仁，因为机器人操作中的 action importance 明显不均匀，关键动作比预备动作更需要高精度。作者据此提出 **DySL-VLA**，通过 **dynamic-static layer skipping** 在重要动作上保留更多计算、在不重要动作上跳过更多层，从而兼顾实时性与准确率。来源：[[raw/2602_22896_DySL-VLA.pdf]]，第 1-2 页 Abstract、Introduction。
- 方法上的主张不是简单 early exit，而是三件事的组合：把层分成 **informative layers** 与 **incremental layers**；用 **prior-post skipping guidance** 决定何时允许跳层；再用 **skip-aware two-stage knowledge distillation** 训练 lightweight skipping controllers 与 adapters，而不是重训整个 LLM backbone。来源：[[raw/2602_22896_DySL-VLA.pdf]]，第 2-5 页 Sec. 3.1-3.3。
- 主证据锚点 1：来源：[[raw/2602_22896_DySL-VLA.pdf]]，**Abstract + Introduction + Figure 1**：第 1-2 页。用于锚定 “不同动作重要性不同” 的问题 framing，以及为何 uniform acceleration 次优。
- 主证据锚点 2：来源：[[raw/2602_22896_DySL-VLA.pdf]]，**Table 1 + Sec. 3.1 Observation and Overview**：第 2-3 页。用于锚定它和 pruning / quantization / MoLe / DeeR 的方法差异，以及 `informative vs incremental layers` 的总体结构。
- 主证据锚点 3：来源：[[raw/2602_22896_DySL-VLA.pdf]]，**Figure 5 / Figure 7 / Sec. 3.2-3.3**：第 4-5 页。用于锚定 `dynamic-static skipping`、`pre-skip prediction`、`post-skip verification` 和两阶段蒸馏的具体机制。

## Table / Metric Anchors
- **Table 1 + Sec. 3.1 Observation and Overview**：第 2-3 页。用于锚定它和 pruning / quantization / MoLe / DeeR 的方法差异，以及 `informative vs incremental layers` 的总体结构。
- **Table 2 / Table 3 / Table 4**：第 5-6 页。用于锚定 Calvin、LIBERO、latency breakdown 与 ablation，拆清 `2.1% / 85.7× / 13.7× / 3.75×` 各自对应的对象。

## Table / Metric Split
- `**Table 1 + Sec. 3.1 Observation and Overview**` 这一层应单独承载 `**Table 1 + Sec. 3.1 Observation and Overview**` 相关的 benchmark / metric / operating point。 这里收口为：**Table 1 + Sec. 3.1 Observation and Overview**：第 2-3 页。当前对应它和 pruning / quantization / MoLe / DeeR 的方法差异，以及 `informative vs incremental layers` 的总体结构。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_22896_DySL-VLA.pdf]]，`**Table 1 + Sec. 3.1 Observation and Overview**`。
- `**Table 2 / Table 3 / Table 4**` 这一层应单独承载 `**Table 2 / Table 3 / Table 4**` 相关的 benchmark / metric / operating point。 这里收口为：**Table 2 / Table 3 / Table 4**：第 5-6 页。当前对应 Calvin、LIBERO、latency breakdown 与 ablation，拆清 `2.1% / 85.7× / 13.7× / 3.75×` 各自对应的对象。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_22896_DySL-VLA.pdf]]，`**Table 2 / Table 3 / Table 4**`。

## 不可混写项
- `2.1%`、`85.7×`、`13.7×`、`3.75×` 等 headline 数字来自不同比较维度；仍需拆清哪些是 Calvin 上的 training-efficiency claim，哪些是 inference-latency claim。
- 论文同时覆盖 RoboFlamingo-3B/9B 和 OpenVLA-OFT-7B，且在 Calvin 与 LIBERO 上的 headline 不完全相同；仍需统一单篇页里的主 benchmark 叙述策略。
- `prior-post skipping guidance` 当前被概括为一套 gating 机制；仍需更精确地区分 `pre-skip prediction` 与 `post-skip verification` 的角色。

## 影响页面
- [[wiki/papers/2602_22896_DySL-VLA.md|2602_22896_DySL-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
