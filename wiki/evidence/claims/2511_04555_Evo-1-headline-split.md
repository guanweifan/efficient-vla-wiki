# 2511_04555_Evo-1-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2511_04555_Evo-1.md|2511_04555_Evo-1]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`without robot-data pretraining` 是这篇论文的重要 headline，但 real-world 训练部分又明确为四个任务各收集 `100` 条 teleoperation demonstrations；引用时要区分“无大规模机器人预训练”与“完全零机器人数据 / 零机器人微调”。

## Evidence
- 核心证据命题：这篇论文要解决的是：现有 VLA 往往参数规模大、训练和推理成本高、控制频率低，而且端到端训练容易破坏 vision-language backbone 的语义表示，导致泛化变差；同时很多方法还依赖大规模机器人预训练数据。 来源：[[raw/2511_04555_Evo-1.pdf]]，`PDF p.1-2` Abstract + Introduction：
- 补充证据命题：作者提出 `Evo-1`，这是一个轻量化 VLA：以 `InternVL3-1B` 为原生 multimodal backbone，配合 `cross-modulated diffusion transformer` 和一个优化后的 integration module 生成连续动作，并通过 `two-stage training` 在适配下游动作生成的同时尽量保留 VLM 的语义空间。 来源：[[raw/2511_04555_Evo-1.pdf]]，Evo-1 的问题设定、`0.77B` 参数、无需 robot-data pretraining、以及 simulation / real-world headline 在这里。
- 主证据锚点 1：来源：[[raw/2511_04555_Evo-1.pdf]]，`PDF p.1-2` Abstract + Introduction：
- 主证据锚点 2：来源：[[raw/2511_04555_Evo-1.pdf]]，Evo-1 的问题设定、`0.77B` 参数、无需 robot-data pretraining、以及 simulation / real-world headline 在这里。
- 主证据锚点 3：来源：[[raw/2511_04555_Evo-1.pdf]]，`PDF p.3-5` Sec. 3 + Fig. 1 / Fig. 2：

## Table / Metric Anchors
- `PDF p.5-7` Table 1 + benchmark subsections：
  - Meta-World `80.6%`、LIBERO `94.8%`、RoboTwin `37.8%` 以及与 SmolVLA、π0 等基线的比较都在这里；`+12.4%` 与 `+6.9%` 需要分别回到 Meta-World / RoboTwin 去读，后续不要压成统一平均。
- `PDF p.8` Table 2：
  - 推理效率分析在这里；`2.3 GB` GPU memory、`16.4 Hz` inference frequency、`78%` real-world success 都来自这张表，且绑定在 `RTX 4090d` 的统一测量设置。
- `PDF p.8-9` Table 3 + generalization section：
  - 未见干扰物、背景变化、位置变化、高度变化下的真实世界泛化结果在这里，用于锚定 generalization evidence。

## Table / Metric Split
- ``PDF p.5-7` Table 1 + benchmark subsections` 这一层支撑 ``PDF p.5-7` Table 1 + benchmark subsections` 对应的 benchmark / metric / operating point。 - Meta-World `80.6%`、LIBERO `94.8%`、RoboTwin `37.8%` 以及与 SmolVLA、π0 等基线的比较都在这里；`+12.4%` 与 `+6.9%` 需要分别回到 Meta-World / RoboTwin 去读，后续不要压成统一平均。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2511_04555_Evo-1.pdf]]，``PDF p.5-7` Table 1 + benchmark subsections`。
- ``PDF p.8` Table 2` 这一层支撑 ``PDF p.8` Table 2` 对应的 benchmark / metric / operating point。 - 推理效率分析在这里；`2.3 GB` GPU memory、`16.4 Hz` inference frequency、`78%` real-world success 都来自这张表，且绑定在 `RTX 4090d` 的统一测量设置。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2511_04555_Evo-1.pdf]]，``PDF p.8` Table 2`。
- ``PDF p.8-9` Table 3 + generalization section` 这一层支撑 ``PDF p.8-9` Table 3 + generalization section` 对应的 benchmark / metric / operating point。 - 未见干扰物、背景变化、位置变化、高度变化下的真实世界泛化结果在这里，当前对应 generalization evidence。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2511_04555_Evo-1.pdf]]，``PDF p.8-9` Table 3 + generalization section`。

## 不可混写项
- `without robot-data pretraining` 是这篇论文的重要 headline，但 real-world 训练部分又明确为四个任务各收集 `100` 条 teleoperation demonstrations；引用时要区分“无大规模机器人预训练”与“完全零机器人数据 / 零机器人微调”。
- `16.4 Hz` / `2.3 GB` / `78%` 都来自特定 RTX 4090d 配置与四个 real-world 任务，不应直接外推成普遍部署结论。
- `state-of-the-art` 主要落在 Meta-World 与 RoboTwin；LIBERO 上是强结果 `94.8%`，但若写统一 SOTA 结论，需要按 benchmark 分开表述。

## 影响页面
- [[wiki/papers/2511_04555_Evo-1.md|2511_04555_Evo-1]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
