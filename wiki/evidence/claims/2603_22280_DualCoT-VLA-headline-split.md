# 2603_22280_DualCoT-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_22280_DualCoT-VLA.md|2603_22280_DualCoT-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`98.8%`、`55.1%`、`83.2 ms` 分别对应 LIBERO、RoboCasa GR1 和单卡 H100 latency analysis；仍需避免把这些数字误写成同一层面的综合结论。

## Evidence
- 这篇论文要解决的问题是：现有带 CoT 的 VLA 往往只能在**单一模态**里思考，并且依赖**自回归**方式逐步生成 reasoning token，因此同时面临两类限制：一是很难兼顾高层逻辑规划与低层空间感知，二是推理 latency 高且容易产生 compounding errors。作者据此提出 **DualCoT-VLA**，希望把 visual CoT 与 linguistic CoT 结合起来，并把 reasoning 从 step-by-step autoregressive decoding 改成 single-step parallel reasoning。来源：[[raw/2603_22280_DualCoT-VLA.pdf]]，第 1-2 页 Abstract、Introduction。
- 方法上的主张是一个 **visual-linguistic CoT paradigm**：用一组 visual CoT query tokens 蒸馏来自 **Depth Anything 3** 的几何 / 深度先验，用一组 linguistic CoT query tokens 通过 frozen auxiliary LLM 内化高层任务规划，再把两路 reasoning-enriched hidden states 一次性送入下游 action expert。其关键 framing 不是“显式生成更多思维文本”，而是**把 multimodal CoT 压入连续 latent space，并在单次 forward pass 中完成 reasoning**。来源：[[raw/2603_22280_DualCoT-VLA.pdf]]，第 2-4 页 Fig. 1、Sec. 3.1-3.2。
- 主证据锚点 1：来源：[[raw/2603_22280_DualCoT-VLA.pdf]]，**Abstract + Introduction**：第 1-2 页。用于锚定 “single-modal CoT + autoregressive reasoning” 的双重瓶颈，以及论文的总体 framing。
- 主证据锚点 2：来源：[[raw/2603_22280_DualCoT-VLA.pdf]]，**Figure 1 + Sec. 3.1-3.2**：第 3-4 页。用于锚定 dual query token、single forward reasoning、teacher modules 在训练 / 推理阶段的不同角色。
- 主证据锚点 3：来源：[[raw/2603_22280_DualCoT-VLA.pdf]]，**Table 1 / LIBERO results**：第 8-9 页。用于锚定 `98.8%` average SR、四个 suite 的具体表现，以及它与 LaRA-VLA / OpenVLA-OFT / Fast-ThinkAct 的差异。

## Table / Metric Anchors
- **Table 1 / LIBERO results**：第 8-9 页。用于锚定 `98.8%` average SR、四个 suite 的具体表现，以及它与 LaRA-VLA / OpenVLA-OFT / Fast-ThinkAct 的差异。
- **Table 2 / RoboCasa GR1 results**：第 10 页。用于锚定 `55.1% across 24 tasks` 的具体 benchmark 语境及各类 task 的分布。
- **Table 3 / Table 4 / real-world section**：第 11 页及前后。用于锚定 `83.2 ms` latency、visual-only vs linguistic-only vs dual-stream 的互补性，以及 real-world baselines 对比。

## Table / Metric Split
- `**Table 1 / LIBERO results**` 这一层应单独承载 `**Table 1 / LIBERO results**` 相关的 benchmark / metric / operating point。 这里收口为：**Table 1 / LIBERO results**：第 8-9 页。当前对应 `98.8%` average SR、四个 suite 的具体表现，以及它与 LaRA-VLA / OpenVLA-OFT / Fast-ThinkAct 的差异。；`98.8%`、`55.1%`、`83.2 ms` 分别对应 LIBERO、RoboCasa GR1 和单卡 H100 latency analysis；这里需要避免把这些数字误写成同一层面的综合结论。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_22280_DualCoT-VLA.pdf]]，`**Table 1 / LIBERO results**`。
- `**Table 2 / RoboCasa GR1 results**` 这一层应单独承载 `**Table 2 / RoboCasa GR1 results**` 相关的 benchmark / metric / operating point。 这里收口为：**Table 2 / RoboCasa GR1 results**：第 10 页。当前对应 `55.1% across 24 tasks` 的具体 benchmark 语境及各类 task 的分布。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_22280_DualCoT-VLA.pdf]]，`**Table 2 / RoboCasa GR1 results**`。
- `**Table 3 / Table 4 / real-world section**` 这一层应单独承载 `**Table 3 / Table 4 / real-world section**` 相关的 benchmark / metric / operating point。 这里收口为：**Table 3 / Table 4 / real-world section**：第 11 页及前后。当前对应 `83.2 ms` latency、visual-only vs linguistic-only vs dual-stream 的互补性，以及 real-world baselines 对比。；`98.8%`、`55.1%`、`83.2 ms` 分别对应 LIBERO、RoboCasa GR1 和单卡 H100 latency analysis；这里需要避免把这些数字误写成同一层面的综合结论。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_22280_DualCoT-VLA.pdf]]，`**Table 3 / Table 4 / real-world section**`。

## 不可混写项
- `98.8%`、`55.1%`、`83.2 ms` 分别对应 LIBERO、RoboCasa GR1 和单卡 H100 latency analysis；仍需避免把这些数字误写成同一层面的综合结论。
- 论文同时强调 `parallel CoT`、`visual-linguistic CoT`、`implicit latent reasoning` 三种 framing；后续 taxonomy 需要统一其主定位。
- 真实世界部分目前只保留了“优于 OpenVLA-OFT / GR00T-N1.6”等高层 claim；仍需进一步钉清任务种类、成功率和 platform setting。

## 影响页面
- [[wiki/papers/2603_22280_DualCoT-VLA.md|2603_22280_DualCoT-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
