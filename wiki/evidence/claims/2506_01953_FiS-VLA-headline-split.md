# 2506_01953_FiS-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2506_01953_FiS-VLA.md|2506_01953_FiS-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`8% in simulation / 11% in real-world / 117.7 Hz` 目前只保留为 headline claim；后续 `L2` 需要精确钉到对应 table、平台、chunk size 和 baseline。

## Evidence
- 这篇论文提出 **Fast-in-Slow (FiS / FiS-VLA)**，目标是同时解决 robotic manipulation 中的两类核心矛盾：**foundation policy 的泛化能力**与**执行频率/实时性**。作者认为现有 dual-system VLA 虽然把慢推理和快执行拆开了，但由于 System 1 通常是外接的轻量 action model，无法充分继承 VLM-based System 2 的互联网规模预训练知识。来源：[[raw/2506_01953_FiS-VLA.pdf]]，第 1-2 页 Abstract、Introduction。
- 核心主张是：把 **System 1 execution module 嵌入到 VLM-based System 2 内部**，通过部分共享参数、异步频率和异构输入模态，形成一个统一 dual-system foundation model，从而在单个基础模型内部实现 reasoning 与 execution 的协调。来源：[[raw/2506_01953_FiS-VLA.pdf]]，第 1 页 Abstract；第 2-4 页 Fig. 1、Fig. 2、Sec. 3。
- 主证据锚点 1：来源：[[raw/2506_01953_FiS-VLA.pdf]]，**Abstract**：第 1 页。用于锚定 “统一 dual-system + 8% / 11% / 117.7 Hz” 的 headline claim。
- 主证据锚点 2：来源：[[raw/2506_01953_FiS-VLA.pdf]]，**Fig. 1 + Introduction**：第 2 页。用于锚定 FiS 与以往 dual-system VLA 的关键差异，尤其是 “System 1 in System 2”。
- 主证据锚点 3：来源：[[raw/2506_01953_FiS-VLA.pdf]]，**Sec. 3 + Fig. 2**：第 3-4 页。用于锚定整体架构、System 1 / System 2 的角色划分和参数共享方式。

## Table / Metric Anchors
- **Table 1 + quantitative results**：第 7 页。用于锚定 RLBench 上与 baselines 的平均成功率和控制频率。
- **Table 2 + real-world results**：第 8-9 页。用于锚定 Agilex / AlphaBot 等 real-world 比较结果。
- **Table 3 + generalization**：第 9 页。用于锚定 unseen object / background / lighting 等 generalization 维度。
- **Figure 5 / Tables 6-10**：Appendix，对应第 8 页与后续附录。用于锚定 action chunk size、System 1 输入组合和异步频率比的 ablation。

## Table / Metric Split
- `**Table 1 + quantitative results**` 这一层应单独承载 `**Table 1 + quantitative results**` 相关的 benchmark / metric / operating point。 这一层对应 RLBench 上与 baselines 的平均成功率和控制频率。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2506_01953_FiS-VLA.pdf]]，`**Table 1 + quantitative results**`。
- `**Table 2 + real-world results**` 这一层应单独承载 `**Table 2 + real-world results**` 相关的 benchmark / metric / operating point。 这一层对应 Agilex / AlphaBot 等 real-world 比较结果。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2506_01953_FiS-VLA.pdf]]，`**Table 2 + real-world results**`。
- `**Table 3 + generalization**` 这一层应单独承载 `**Table 3 + generalization**` 相关的 benchmark / metric / operating point。 这一层对应 unseen object / background / lighting 等 generalization 维度。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2506_01953_FiS-VLA.pdf]]，`**Table 3 + generalization**`。
- `**Figure 5 / Tables 6-10**` 这一层应单独承载 `**Figure 5 / Tables 6-10**` 相关的 benchmark / metric / operating point。 这一层对应 action chunk size、System 1 输入组合和异步频率比的 ablation。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2506_01953_FiS-VLA.pdf]]，`**Figure 5 / Tables 6-10**`。

## 不可混写项
- `8% in simulation / 11% in real-world / 117.7 Hz` 目前只保留为 headline claim；后续 `L2` 需要精确钉到对应 table、平台、chunk size 和 baseline。
- 文中同时使用 `FiS`、`FiS-VLA`、以及与具体 backbone/robot setup 绑定的表述；主编仍需统一命名口径。
- real-world 成功率目前只保留了聚合结论，仍需决定是否把 Agilex 与 AlphaBot 分开写成更清楚的单篇 evidence 入口。

## 影响页面
- [[wiki/papers/2506_01953_FiS-VLA.md|2506_01953_FiS-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
