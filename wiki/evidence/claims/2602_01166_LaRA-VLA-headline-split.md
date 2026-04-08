# 2602_01166_LaRA-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_01166_LaRA-VLA.md|2602_01166_LaRA-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`up to 90% latency reduction`、`135 ms`、以及 simulation / real-robot 上的性能提升来自不同评测层面；仍需拆清具体 baseline 和指标口径。

## Evidence
- 这篇论文提出 **LaRA-VLA**，目标是在 VLA 中把显式 textual / visual CoT 内化成**连续 latent reasoning**，从而兼顾 reasoning 结构与实时控制效率。作者的核心判断是：现有 CoT-based VLA 虽然有效，但一方面推理时会生成冗长的显式中间结果，带来很高的 latency；另一方面，无论文字 CoT 还是离散视觉 token CoT，都与机器人连续感知和连续控制存在表征错配。来源：[[raw/2602_01166_LaRA-VLA.pdf]]，第 1-2 页 Abstract、Introduction、Fig. 1。
- 方法上的主张是一个 **unified latent-reasoning VLA**：同时把 textual CoT 和 visual reasoning internalize 到 **continuous latent representations** 中，在 latent space 里完成 reasoning 与 prediction，并在推理阶段完全消除显式 CoT generation。为实现这一点，论文引入了一个 **curriculum-based training paradigm**，逐步从显式 textual/visual CoT 监督过渡到 latent reasoning，再把 latent reasoning dynamics 适配到 action generation。来源：[[raw/2602_01166_LaRA-VLA.pdf]]，第 1 页 Abstract；第 2-5 页 Introduction、Fig. 2、方法章节。
- 主证据锚点 1：来源：[[raw/2602_01166_LaRA-VLA.pdf]]，**Abstract**：第 1 页。可直接承载 `up to 90% latency reduction`、latent reasoning 和 curriculum training 的 headline。
- 主证据锚点 2：来源：[[raw/2602_01166_LaRA-VLA.pdf]]，**Figure 1 + Introduction**：第 1-3 页。用于锚定 textual/visual CoT 与 LaRA-VLA 的差异，以及“离散 CoT 与连续控制错配”的方法动机。
- 主证据锚点 3：来源：[[raw/2602_01166_LaRA-VLA.pdf]]，**Figure 2 + training overview**：第 4-6 页。用于锚定三阶段 curriculum、explicit CoT -> latent reasoning -> action adaptation 的训练路径。

## Table / Metric Anchors
- **Table 2 及实验章节**：第 8-10 页。用于锚定在 LIBERO / SimplerEnv / long-horizon real-robot 上的对比结果，以及具体 latency 数字如 `135 ms`。

## Table / Metric Split
- `**Table 2 及实验章节**` 这一层应单独承载 `**Table 2 及实验章节**` 相关的 benchmark / metric / operating point。 这里收口为：**Table 2 及实验章节**：第 8-10 页。当前对应在 LIBERO / SimplerEnv / long-horizon real-robot 上的对比结果，以及具体 latency 数字如 `135 ms`。；`up to 90% latency reduction`、`135 ms`、以及 simulation / real-robot 上的性能提升来自不同评测层面；这里需要拆清具体 baseline 和指标口径。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_01166_LaRA-VLA.pdf]]，`**Table 2 及实验章节**`。

## 不可混写项
- `up to 90% latency reduction`、`135 ms`、以及 simulation / real-robot 上的性能提升来自不同评测层面；仍需拆清具体 baseline 和指标口径。
- 论文标题是 `Latent Reasoning VLA`，但仓库里文件名采用 `LaRA-VLA`；仍需统一命名口径，避免 `LaRA-VLA` 与 `Latent Reasoning VLA` 并存引发混淆。
- LaRA-VLA 同时强调 `latent reasoning paradigm`、`curriculum-based training`、`continuous latent CoT` 和 `action adaptation`；后续 taxonomy 需要统一其主定位。

## 影响页面
- [[wiki/papers/2602_01166_LaRA-VLA.md|2602_01166_LaRA-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
