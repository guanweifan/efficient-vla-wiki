# 2507_16815_ThinkAct-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2507_16815_ThinkAct.md|2507_16815_ThinkAct]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`84.4%`、`+2.5%`、`+4.1 BLEU`、`+7.3% / +9.5%` 这些数字分别来自不同 benchmark；仍需决定哪些保留为主 claim，哪些降为 supporting evidence。

## Evidence
- 这篇论文提出 **ThinkAct**，试图解决 VLA 在复杂 embodied tasks 上“会执行但不会深思”的问题。其基本判断是：把高层视觉-语言推理与低层动作执行分离，并用一个共享的视觉计划潜变量把两者连接起来，可以让 VLA 获得 few-shot adaptation、long-horizon planning 和 self-correction 等能力。来源：[[raw/2507_16815_ThinkAct.pdf]]，第 1 页 Abstract；第 2 页 Fig. 1。
- 核心方法主张是：先让一个 reasoning MLLM 通过 **reinforced visual latent planning** 生成 embodied reasoning plan，再把 reasoning 压缩成 **visual plan latent** 去条件化下游 action model。论文强调这不是单纯加长 CoT，而是让 reasoning 直接对视觉轨迹和动作可行性负责。来源：[[raw/2507_16815_ThinkAct.pdf]]，第 1 页 Abstract；第 4-5 页 Sec. 3、Fig. 2。
- 主证据锚点 1：来源：[[raw/2507_16815_ThinkAct.pdf]]，**Abstract**：第 1 页。可直接承载 dual-system、visual plan latent、reward design 和 few-shot / self-correction headline。
- 主证据锚点 2：来源：[[raw/2507_16815_ThinkAct.pdf]]，**Fig. 1 + Introduction**：第 2 页。用于锚定 “think before act” 的总体 framing，以及 few-shot / long-horizon / self-correction 的任务图示。
- 主证据锚点 3：来源：[[raw/2507_16815_ThinkAct.pdf]]，**Fig. 2 + Sec. 3**：第 4-5 页。用于锚定 reasoning model、action model、latent interface、reward equations 与 GRPO。

## Table / Metric Anchors
- **Table 1**：第 7 页。用于锚定 SimplerEnv / LIBERO manipulation 结果，尤其是 `84.4%` 总体 success 及其比较对象。
- **Table 2**：第 8 页。用于锚定 EgoPlan-Bench2 / RoboVQA / OpenEQA 的 reasoning benchmark 结果。
- **Table 3 + Fig. 5 + Fig. 6**：第 9-11 页。用于锚定 few-shot adaptation、ablation、以及 self-correction 的具体案例与边界。

## Table / Metric Split
- `**Table 1**` 这一层应单独承载 `**Table 1**` 相关的 benchmark / metric / operating point。 这里收口为：**Table 1**：第 7 页。当前对应 SimplerEnv / LIBERO manipulation 结果，尤其是 `84.4%` 总体 success 及其比较对象。；`84.4%`、`+2.5%`、`+4.1 BLEU`、`+7.3% / +9.5%` 这些数字分别来自不同 benchmark；这里需要决定哪些保留为主 claim，哪些降为 supporting evidence。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2507_16815_ThinkAct.pdf]]，`**Table 1**`。
- `**Table 2**` 这一层应单独承载 `**Table 2**` 相关的 benchmark / metric / operating point。 这一层对应 EgoPlan-Bench2 / RoboVQA / OpenEQA 的 reasoning benchmark 结果。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2507_16815_ThinkAct.pdf]]，`**Table 2**`。
- `**Table 3 + Fig. 5 + Fig. 6**` 这一层应单独承载 `**Table 3 + Fig. 5 + Fig. 6**` 相关的 benchmark / metric / operating point。 这一层对应 few-shot adaptation、ablation、以及 self-correction 的具体案例与边界。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2507_16815_ThinkAct.pdf]]，`**Table 3 + Fig. 5 + Fig. 6**`。

## 不可混写项
- `84.4%`、`+2.5%`、`+4.1 BLEU`、`+7.3% / +9.5%` 这些数字分别来自不同 benchmark；仍需决定哪些保留为主 claim，哪些降为 supporting evidence。
- 文中还提到相较 OpenVLA 存在约 `17%` 的 execution-time overhead；仍需决定这个 tradeoff 是否应在单篇主 claim 中更显式呈现。
- ThinkAct 同时被描述为 reasoning VLA、dual-system framework、reinforced latent planning method；后续 taxonomy 需要统一它的主定位。

## 影响页面
- [[wiki/papers/2507_16815_ThinkAct.md|2507_16815_ThinkAct]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
