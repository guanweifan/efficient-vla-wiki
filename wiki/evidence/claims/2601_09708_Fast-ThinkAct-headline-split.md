# 2601_09708_Fast-ThinkAct-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2601_09708_Fast-ThinkAct.md|2601_09708_Fast-ThinkAct]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`89.3% latency reduction` 与 `9.3× faster` 主要是相对具体 reasoning VLA baseline 的效率 headline，引用时要明确比较对象，而不是泛化成对所有 VLA 的统一提升。

## Evidence
- 核心证据命题：这篇论文要解决的是：reasoning VLA 虽然能通过显式 chain-of-thought 提升长时程规划、few-shot adaptation 和 failure recovery，但长文本 reasoning trace 带来的推理延迟过高，难以满足 embodied 场景的实时要求。 来源：[[raw/2601_09708_Fast-ThinkAct.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 补充证据命题：作者提出 `Fast-ThinkAct`，核心思路是把显式 textual CoT 压缩成 `verbalizable latent reasoning`。它通过一个 textual teacher 生成高质量 reasoning，再用 preference-guided distillation 和 visual trajectory alignment，把语言与视觉规划能力蒸馏到紧凑的连续 latent 与 spatial tokens 中，最后再由 reasoning-enhanced policy learning 把这些 latent planning 转成低层动作。 来源：[[raw/2601_09708_Fast-ThinkAct.pdf]]，Fast-ThinkAct 的问题设定、从长 textual CoT 到 compact latent reasoning 的核心动机、以及 `89.3% reduced inference latency` / `9.3× faster than ThinkAct-7B` 的 headline 都在这里。
- 主证据锚点 1：来源：[[raw/2601_09708_Fast-ThinkAct.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 主证据锚点 2：来源：[[raw/2601_09708_Fast-ThinkAct.pdf]]，Fast-ThinkAct 的问题设定、从长 textual CoT 到 compact latent reasoning 的核心动机、以及 `89.3% reduced inference latency` / `9.3× faster than ThinkAct-7B` 的 headline 都在这里。
- 主证据锚点 3：来源：[[raw/2601_09708_Fast-ThinkAct.pdf]]，`PDF p.3-5` Sec. 3 + Fig. 2：

## Table / Metric Anchors
- `PDF p.7-8` Table 1：
  - RoboTwin2.0 的量化结果在这里，用于锚定双臂 manipulation 的具体证据。
- `PDF p.8-9` Table 2：
  - EgoPlan-Bench2、RoboVQA、OpenEQA 等 embodied reasoning benchmark 的结果在这里，用于锚定“reasoning quality 没丢”的证据。

## Table / Metric Split
- ``PDF p.7-8` Table 1` 这一层支撑 ``PDF p.7-8` Table 1` 对应的 benchmark / metric / operating point。 - RoboTwin2.0 的量化结果在这里，当前对应双臂 manipulation 的具体证据。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2601_09708_Fast-ThinkAct.pdf]]，``PDF p.7-8` Table 1`。
- ``PDF p.8-9` Table 2` 这一层支撑 ``PDF p.8-9` Table 2` 对应的 benchmark / metric / operating point。 - EgoPlan-Bench2、RoboVQA、OpenEQA 等 embodied reasoning benchmark 的结果在这里，当前对应“reasoning quality 没丢”的证据。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2601_09708_Fast-ThinkAct.pdf]]，``PDF p.8-9` Table 2`。

## 不可混写项
- `89.3% latency reduction` 与 `9.3× faster` 主要是相对具体 reasoning VLA baseline 的效率 headline，引用时要明确比较对象，而不是泛化成对所有 VLA 的统一提升。
- 主文当前最容易直接抓到的是 Fig. 3 的 benchmark 结果；若仍需每个 LIBERO 子套件或 SimplerEnv 的精确数值，应回图表或附录进一步核定。
- 论文同时包含 teacher-student distillation、trajectory alignment 和 reasoning-enhanced policy learning 三层机制；若把增益全部归因于 latent reasoning 本身，需要谨慎拆分证据。

## 影响页面
- [[wiki/papers/2601_09708_Fast-ThinkAct.md|2601_09708_Fast-ThinkAct]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
