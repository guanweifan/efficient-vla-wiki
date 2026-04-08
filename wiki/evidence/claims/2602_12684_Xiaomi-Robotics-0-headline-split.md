# 2602_12684_Xiaomi-Robotics-0-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_12684_Xiaomi-Robotics-0.md|2602_12684_Xiaomi-Robotics-0]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`98.7%`、`85.5% / 74.7% / 79.2%`、`4.75 / 4.80`、真实机器人 throughput 都来自不同 benchmark 与不同指标；仍需拆清各自的比较对象和评价方式。

## Evidence
- 这篇论文提出 **Xiaomi-Robotics-0**，目标是在保持大规模 VLA 泛化能力的同时，实现**fast and smooth real-time execution**。作者的基本判断是：VLA 的主要落地难点并不只是精度，而是高推理延迟会让连续 action chunk 难以平滑衔接，导致真实机器人 rollout 出现 jerkiness 和 OOD motion。来源：[[raw/2602_12684_Xiaomi-Robotics-0.pdf]]，第 1-2 页 Abstract、Introduction。
- 方法上的主张不是单一模块创新，而是一套完整的 **training recipe + deployment strategy**。模型本身由 **Qwen3-VL-4B-Instruct** 作为 VLM 骨干，加上一个基于 **flow-matching** 的 diffusion transformer 动作生成器，整体约 **4.7B 参数**。训练上分为 pre-training 和 post-training 两阶段；post-training 中又专门针对 **asynchronous execution** 设计了 action prefix conditioning、`Λ-shape attention mask` 等机制，以兼顾连续性和反应性。来源：[[raw/2602_12684_Xiaomi-Robotics-0.pdf]]，第 1-4 页 Abstract、Fig. 1、Sec. 2。
- 主证据锚点 1：来源：[[raw/2602_12684_Xiaomi-Robotics-0.pdf]]，**Abstract**：第 1 页。可直接承载 `real-time execution`、`asynchronous rollout`、`consumer-grade GPU` 和 simulation / real-robot headline。
- 主证据锚点 2：来源：[[raw/2602_12684_Xiaomi-Robotics-0.pdf]]，**Figure 1 + Introduction**：第 2 页。用于锚定为什么高延迟会导致 jerky motion，以及 training recipe + deployment strategy 的总体 framing。
- 主证据锚点 3：来源：[[raw/2602_12684_Xiaomi-Robotics-0.pdf]]，**Sec. 2.2 / Figure 3 / Figure 4**：第 3-5 页。用于锚定 `Qwen3-VL-4B + DiT flow-matching`、Choice Policies、pre-training / post-training、Λ-shape attention mask 与 async execution。

## Table / Metric Anchors
- **Table 1 / CALVIN results**：第 5-7 页。用于锚定 LIBERO、SimplerEnv、CALVIN 上的 benchmark 数字与不同指标口径。

## Table / Metric Split
- `**Table 1 / CALVIN results**` 这一层应单独承载 `**Table 1 / CALVIN results**` 相关的 benchmark / metric / operating point。 这一层对应 LIBERO、SimplerEnv、CALVIN 上的 benchmark 数字与不同指标口径。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_12684_Xiaomi-Robotics-0.pdf]]，`**Table 1 / CALVIN results**`。

## 不可混写项
- `98.7%`、`85.5% / 74.7% / 79.2%`、`4.75 / 4.80`、真实机器人 throughput 都来自不同 benchmark 与不同指标；仍需拆清各自的比较对象和评价方式。
- 论文同时使用 `Xiaomi-Robotics-0`、`advanced VLA model`、`open-sourced VLA model with real-time execution` 等 framing；后续 taxonomy 需要统一其主定位。
- 真实机器人部分更强调 throughput 和 smooth rollout，而不是单纯 success rate；仍需决定在单篇主 claim 中把“实时平滑执行”放多高。

## 影响页面
- [[wiki/papers/2602_12684_Xiaomi-Robotics-0.md|2602_12684_Xiaomi-Robotics-0]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
