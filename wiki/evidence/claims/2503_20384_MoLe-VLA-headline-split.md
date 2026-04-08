# 2503_20384_MoLe-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2503_20384_MoLe-VLA.md|2503_20384_MoLe-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`8% mean success rate improvement` 和 `×5.6 computational cost reduction` 目前只保留为 headline；后续 `L2` 需要精确钉到对应 baseline、任务集合与具体表格。

## Evidence
- 这篇论文提出 **MoLe-VLA**（简称 **MoLe**），目标是通过**动态 layer activation** 提升 VLA 在机器人场景中的效率，而不是简单做 early exit 或 token pruning。作者的问题定义是：很多 LLM layers 在 robotics tasks 中存在冗余，但直接砍掉后层会损失对下游任务更关键的语义信息。来源：[[raw/2503_20384_MoLe-VLA.pdf]]，第 1-2 页 Abstract、Introduction。
- 核心主张是：把每个 LLM layer 视作一个 expert，构建 **Mixture-of-Layers** 机制，在输入端通过 router 动态选择当前任务最相关的 layers，以此在保持甚至提升 robotic performance 的同时显著降低计算成本。来源：[[raw/2503_20384_MoLe-VLA.pdf]]，第 1-3 页 Abstract、Introduction；第 4 页 Fig. 2。
- 主证据锚点 1：来源：[[raw/2503_20384_MoLe-VLA.pdf]]，**Abstract + Fig. 1**：第 1 页。用于锚定 MoLe 的问题定义、SBH 动机、`8% / ×5.6` headline claim。
- 主证据锚点 2：来源：[[raw/2503_20384_MoLe-VLA.pdf]]，**Introduction**：第 1-3 页。用于锚定为什么 early exit / shallow truncation 不够，以及为什么要做 layer-wise activation。
- 主证据锚点 3：来源：[[raw/2503_20384_MoLe-VLA.pdf]]，**Fig. 2 + Sec. 3.2**：第 4 页。用于锚定整体框架，包括 MoLe、STAR、CogKD 在 VLA 中的位置关系。

## Table / Metric Anchors
- **Table 1 / Table 2 / Table 4**：第 6-8 页。用于锚定 RLBench 上的性能、推理分析与 scalability。
- **Table 5 / Table 6**：第 8 页。用于锚定 STAR 和 CogKD 的 ablation，以及 real-world FR3 三任务结果。

## Table / Metric Split
- `**Table 1 / Table 2 / Table 4**` 这一层应单独承载 `**Table 1 / Table 2 / Table 4**` 相关的 benchmark / metric / operating point。 这一层对应 RLBench 上的性能、推理分析与 scalability。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2503_20384_MoLe-VLA.pdf]]，`**Table 1 / Table 2 / Table 4**`。
- `**Table 5 / Table 6**` 这一层应单独承载 `**Table 5 / Table 6**` 相关的 benchmark / metric / operating point。 这一层对应 STAR 和 CogKD 的 ablation，以及 real-world FR3 三任务结果。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2503_20384_MoLe-VLA.pdf]]，`**Table 5 / Table 6**`。

## 不可混写项
- `8% mean success rate improvement` 和 `×5.6 computational cost reduction` 目前只保留为 headline；后续 `L2` 需要精确钉到对应 baseline、任务集合与具体表格。
- 文中同时讨论 MoLe-VLA、MoLe-CogAct 等表述；仍需由主编统一单篇页中对“方法名”和“具体实例/实验变体”的命名口径。
- 论文把 STAR 和 CogKD 都写成关键组件，但当前页面尚未判断二者在最终 headline gains 中各自贡献多大；仍需依据 Table 5 ablation 决定是否将其中一个上升为更强的单篇 claim。

## 影响页面
- [[wiki/papers/2503_20384_MoLe-VLA.md|2503_20384_MoLe-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
