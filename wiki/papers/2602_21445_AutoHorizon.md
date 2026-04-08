# 2602_21445_AutoHorizon

## Source
- Raw: [[raw/2602_21445_AutoHorizon.pdf]]
- Extracts manifest: [[extracts/parses/2602_21445_AutoHorizon/manifest.json]]
- Primary text fallback: [[extracts/parses/2602_21445_AutoHorizon/pdftotext.txt]]

## Claim
- 这篇论文讨论的不是如何训练新的 VLA，而是 **flow-based VLA 在 action chunking 中应该执行多长的 execution horizon**。作者的核心判断是：固定 execution horizon 往往是次优的，因为 policy 在不同 rollout 阶段对“长时平滑性”和“短时反应性”的需求会变化；因此 horizon 应该随 chunk 和感知条件动态调整，而不是靠人工 heuristic 或 brute-force tuning 固定下来。来源：[[raw/2602_21445_AutoHorizon.pdf]]，第 1-2 页 Abstract、Introduction。
- 基于对 cross-attention 和 self-attention 的分析，论文提出 **AutoHorizon**：一种 **test-time** 的动态执行 horizon 估计方法。它把 action self-attention 视为模型预测极限的 proxy，用 **bidirectional soft-pointer** 去找 attention 轨迹开始 plateau 的 turning point，从而为每个预测 chunk 动态决定要执行多少 action。来源：[[raw/2602_21445_AutoHorizon.pdf]]，第 2-6 页 Sec. 1、Sec. 3.4。
- 论文保留了较强的 headline performance claim：AutoHorizon 在 simulated 与 real-world manipulation 上都有效，**computational overhead 可忽略**，并且能跨 **不同 flow-based policy** 泛化。在 LIBERO 上，它相对固定 horizon baselines 和随机 horizon baseline 持续占优；在 RoboTwin 与 real-world tasks 上也给出 comparable or superior 的结果。这里的 caveat 是：这些结论高度依赖 **flow-based + action chunking** 的设定，不应直接泛化到所有 VLA 或所有 policy family。来源：[[raw/2602_21445_AutoHorizon.pdf]]，第 1 页 Abstract；第 6-8 页 Table 1、Table 2、Table 3、Table 4。
- 从当前证据看，AutoHorizon 更像一篇 **test-time control / execution policy paper**，重点不是 backbone 改造，而是基于注意力结构为 flow-based VLA 动态选取 execution horizon，以平衡 long-term consistency 与 short-term reactivity。来源：[[raw/2602_21445_AutoHorizon.pdf]]，第 2-3 页 Introduction、Related Work；第 5-6 页 Sec. 3.4。

## Methodology Index
- execution horizon selection
- action chunking
- flow-based VLA
- test-time adaptation
- attention-guided control
- predictive limit estimation
- bidirectional soft-pointer
- turning-point detection
- radial action sinks
- action self-attention
- long-term consistency vs short-term reactivity
- dynamic horizon estimation
- no retraining / negligible overhead

## Data Pointer
- **Abstract + Introduction**：第 1-2 页。适合后续回收 “固定 horizon 次优” 的问题定义，以及 `dynamic execution horizon` 的总体 framing。
- **Figure 1**：第 1 页。适合后续补 `pi0.5` 在 LIBERO 上随 execution horizon 先升后降的核心经验现象。
- **Figure 2 + Sec. 3.4 AutoHorizon**：第 3-6 页。适合后续补 `bidirectional soft-pointer`、plateau turning point、以及为什么 attention 可作为 predictive limit proxy。
- **Table 1 / Table 2**：第 6-7 页。适合后续补在 `pi0.5` 与 `GR00T N1.5` 上的 LIBERO 结果，区分 `p=10`、`p=50` 和不同 task suite。
- **Table 3 / Table 4**：第 8 页。适合后续补 RoboTwin 与 real-world tasks 上的结果，并区分 “comparable” 和 “strictly better” 的具体场景。

## 待核点
- `AutoHorizon` 的 headline 优势目前主要体现在相对固定 horizon / random baseline 的比较上；后续需要进一步拆清哪些场景是显著更强，哪些只是 comparable。
- 论文强调 `negligible computational overhead`，但当前 `L1` 还没有把 overhead 精确钉到具体表格或 wall-clock 数字；后续需要补强。
- 这篇方法严格建立在 **flow-based VLA + action chunking** 之上；后续 taxonomy 需要明确它是一般性的 `execution policy`，还是更窄的 `flow-based chunk-horizon controller`。
- real-world 部分目前只保留为高层 claim；后续需要进一步钉清三个任务上的固定 horizon 对比和方差情况，避免把 “best on average” 误写成无条件优势。
