# 2510_25122_NANOVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2510_25122_NANOVLA.md|2510_25122_NANOVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`52x faster inference`、`98% less parameters`、`+13.8% SR`、`62% inference time reduction`、`3.7% precision gain` 来自不同实验与不同变体；仍需把比较对象、硬件、benchmark 和 NanoVLA-S/L/R 区分清楚，不能压成单一 edge superiority claim。

## Evidence
- 这篇论文提出 **NanoVLA**，目标不是简单把 VLA 缩小，而是围绕边缘设备部署重构整条推理链，使 generalist policy 能在 **Jetson Orin Nano** 一类资源受限硬件上真正运行。作者认为现有 VLA 在 edge deployment 上主要有三个问题：计算太重、长时动作容易变得 jerky / brittle、以及固定 backbone 无法匹配任务难度。来源：[[raw/2510_25122_NANOVLA.pdf]]，第 1-2 页 Abstract、Introduction。
- NanoVLA 的核心主张由三部分共同组成：**vision-language decoupling with caching**、**long-short action chunking (LSAC)**、以及 **dynamic routing**。论文把这三者视为互补设计，而不是三个独立 trick：decoupling 负责减少重复跨模态计算，LSAC 负责在长时规划与短时响应之间折中，routing 负责按任务复杂度分配轻重 backbone。来源：[[raw/2510_25122_NANOVLA.pdf]]，第 1-5 页 Abstract、Fig. 1、Sec. 3。
- 主证据锚点 1：来源：[[raw/2510_25122_NANOVLA.pdf]]，**Abstract**：第 1 页。可直接承载 `52x`、`98% less parameters`、decoupling / chunking / routing 三个 headline。
- 主证据锚点 2：来源：[[raw/2510_25122_NANOVLA.pdf]]，**Figure 1 + Introduction**：第 2 页。用于锚定 decoupled late fusion 的总体 framing，以及 NanoVLA-S/L/R 的 edge-oriented positioning。
- 主证据锚点 3：来源：[[raw/2510_25122_NANOVLA.pdf]]，**Sec. 3.1-3.3**：第 3-5 页。用于锚定 decoupling with caching、LSAC、dynamic routing 的方法细节。

## Table / Metric Anchors
- **Table 1 / Table 2**：第 6-7 页。用于锚定 LIBERO 四个 task suite 与 LIBERO-90 上的 benchmark 结果，以及 `NanoVLA-R` 相对 `NanoVLA-L` 的 trade-off。
- **Figure 3 / Table 3**：第 7-8 页。用于锚定 LeRobot 真实世界任务、不同 Nano 变体与 baseline 的比较；`+13.8% SR` 这类 headline 也需要回到这里和 Jetson 设置一起理解。

## Table / Metric Split
- `**Table 1 / Table 2**` 这一层应单独承载 `**Table 1 / Table 2**` 相关的 benchmark / metric / operating point。 这里收口为：论文保留了非常强的 headline numeric claims，但这些数字需要拆开：`52x higher FPS` 与 `+13.8% SR` 绑定在 `Jetson Orin Nano` 上相对 `OpenVLA` 的 edge-side comparison；`98% less parameters` 指向相对多种 multi-billion-parameter baseline 的模型规模对比；`62% inference time reduction` 则来自 LLM decoupling / caching 的单独分析；`3.7% precision gain` 对应 `NanoVLA-R` 相比 `NanoVLA-L` 的 routing trade-off，而不是整个系统在所有 setting 下的统一增益。来源：[[raw/2510_25122_NANOVLA.pdf]]，第 1 页 Abstract；第 6-9 页 Table 1-3、Fig. 4-6。；**Table 1 / Table 2**：第 6-7 页。当前对应 LIBERO 四个 task suite 与 LIBERO-90 上的 benchmark 结果，以及 `NanoVLA-R` 相对 `NanoVLA-L` 的 trade-off。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2510_25122_NANOVLA.pdf]]，`**Table 1 / Table 2**`。
- `**Figure 3 / Table 3**` 这一层应单独承载 `**Figure 3 / Table 3**` 相关的 benchmark / metric / operating point。 这里收口为：论文保留了非常强的 headline numeric claims，但这些数字需要拆开：`52x higher FPS` 与 `+13.8% SR` 绑定在 `Jetson Orin Nano` 上相对 `OpenVLA` 的 edge-side comparison；`98% less parameters` 指向相对多种 multi-billion-parameter baseline 的模型规模对比；`62% inference time reduction` 则来自 LLM decoupling / caching 的单独分析；`3.7% precision gain` 对应 `NanoVLA-R` 相比 `NanoVLA-L` 的 routing trade-off，而不是整个系统在所有 setting 下的统一增益。来源：[[raw/2510_25122_NANOVLA.pdf]]，第 1 页 Abstract；第 6-9 页 Table 1-3、Fig. 4-6。；**Figure 3 / Table 3**：第 7-8 页。当前对应 LeRobot 真实世界任务、不同 Nano 变体与 baseline 的比较；`+13.8% SR` 这类 headline 也需要回到这里和 Jetson 设置一起理解。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2510_25122_NANOVLA.pdf]]，`**Figure 3 / Table 3**`。

## 不可混写项
- `52x faster inference`、`98% less parameters`、`+13.8% SR`、`62% inference time reduction`、`3.7% precision gain` 来自不同实验与不同变体；仍需把比较对象、硬件、benchmark 和 NanoVLA-S/L/R 区分清楚，不能压成单一 edge superiority claim。
- NanoVLA-S、NanoVLA-L、NanoVLA-R 的角色不同：S/L 是 backbone 规模差异，R 是 routing 版本；仍需统一单篇页和主题页的命名及叙述层级。
- 论文同时覆盖 benchmark、real-world、Jetson inference、routing ablation；仍需决定哪些保留为主 claim，哪些降为 supporting evidence。

## 影响页面
- [[wiki/papers/2510_25122_NANOVLA.md|2510_25122_NANOVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
