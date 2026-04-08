# 2602_21445_AutoHorizon-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_21445_AutoHorizon.md|2602_21445_AutoHorizon]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`AutoHorizon` 的 headline 优势目前主要体现在相对固定 horizon / random baseline 的比较上；仍需进一步拆清哪些场景是显著更强，哪些只是 comparable。

## Evidence
- 这篇论文讨论的不是如何训练新的 VLA，而是 **flow-based VLA 在 action chunking 中应该执行多长的 execution horizon**。作者的核心判断是：固定 execution horizon 往往是次优的，因为 policy 在不同 rollout 阶段对“长时平滑性”和“短时反应性”的需求会变化；因此 horizon 应该随 chunk 和感知条件动态调整，而不是靠人工 heuristic 或 brute-force tuning 固定下来。来源：[[raw/2602_21445_AutoHorizon.pdf]]，第 1-2 页 Abstract、Introduction。
- 基于对 cross-attention 和 self-attention 的分析，论文提出 **AutoHorizon**：一种 **test-time** 的动态执行 horizon 估计方法。它把 action self-attention 视为模型预测极限的 proxy，用 **bidirectional soft-pointer** 去找 attention 轨迹开始 plateau 的 turning point，从而为每个预测 chunk 动态决定要执行多少 action。来源：[[raw/2602_21445_AutoHorizon.pdf]]，第 2-6 页 Sec. 1、Sec. 3.4。
- 主证据锚点 1：来源：[[raw/2602_21445_AutoHorizon.pdf]]，**Abstract + Introduction**：第 1-2 页。可直接承载 “固定 horizon 次优” 的问题定义，以及 `dynamic execution horizon` 的总体 framing。
- 主证据锚点 2：来源：[[raw/2602_21445_AutoHorizon.pdf]]，**Figure 1**：第 1 页。用于锚定 `pi0.5` 在 LIBERO 上随 execution horizon 先升后降的核心经验现象。
- 主证据锚点 3：来源：[[raw/2602_21445_AutoHorizon.pdf]]，**Figure 2 + Sec. 3.4 AutoHorizon**：第 3-6 页。用于锚定 `bidirectional soft-pointer`、plateau turning point、以及为什么 attention 可作为 predictive limit proxy。

## Table / Metric Anchors
- **Table 1 / Table 2**：第 6-7 页。用于锚定在 `pi0.5` 与 `GR00T N1.5` 上的 LIBERO 结果，区分 `p=10`、`p=50` 和不同 task suite。
- **Table 3 / Table 4**：第 8 页。用于锚定 RoboTwin 与 real-world tasks 上的结果，并区分 “comparable” 和 “strictly better” 的具体场景。

## Table / Metric Split
- `**Table 1 / Table 2**` 这一层应单独承载 `**Table 1 / Table 2**` 相关的 benchmark / metric / operating point。 这里收口为：**Figure 1**：第 1 页。当前对应 `pi0.5` 在 LIBERO 上随 execution horizon 先升后降的核心经验现象。；**Table 1 / Table 2**：第 6-7 页。当前对应在 `pi0.5` 与 `GR00T N1.5` 上的 LIBERO 结果，区分 `p=10`、`p=50` 和不同 task suite。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_21445_AutoHorizon.pdf]]，`**Table 1 / Table 2**`。
- `**Table 3 / Table 4**` 这一层应单独承载 `**Table 3 / Table 4**` 相关的 benchmark / metric / operating point。 这一层对应 RoboTwin 与 real-world tasks 上的结果，并区分 “comparable” 和 “strictly better” 的具体场景。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_21445_AutoHorizon.pdf]]，`**Table 3 / Table 4**`。

## 不可混写项
- `AutoHorizon` 的 headline 优势目前主要体现在相对固定 horizon / random baseline 的比较上；仍需进一步拆清哪些场景是显著更强，哪些只是 comparable。
- 论文强调 `negligible computational overhead`，但当前 `L1` 还没有把 overhead 精确钉到具体表格或 wall-clock 数字；仍需补强。
- 这篇方法严格建立在 **flow-based VLA + action chunking** 之上；后续 taxonomy 需要明确它是一般性的 `execution policy`，还是更窄的 `flow-based chunk-horizon controller`。

## 影响页面
- [[wiki/papers/2602_21445_AutoHorizon.md|2602_21445_AutoHorizon]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
