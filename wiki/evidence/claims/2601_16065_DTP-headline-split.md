# 2601_16065_DTP-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2601_16065_DTP.md|2601_16065_DTP]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：当前 headline 里的提升值主要来自特定模型与特定 benchmark，不能写成统一“所有 VLA 都能获得某个固定收益”。

## Evidence
- 核心证据命题：这篇论文要解决的是：VLA 在 manipulation 中可能把大量注意力放到 task-irrelevant 图像区域上，即作者所说的 `distracting tokens`。这些 token 会在 action generation 时干扰模型，把动作朝错误区域引导，降低任务成功率。 来源：[[raw/2601_16065_DTP.pdf]]，`PDF p.1` Abstract + Fig. 1：
- 补充证据命题：作者提出 `Distracting Token Pruning (DTP)`，这是一个 training-free、plug-and-play 的推理期框架。它先通过 prompt-to-visual relevance 构造重要区域，再分析 action generation 时的视觉注意力热图，最后用一个 intersection-based pruning 规则，只在“不重要区域里却获得过高注意力”的 token 上做 pruning。 来源：[[raw/2601_16065_DTP.pdf]]，distracting tokens 的问题定义、DTP 的总体动机，以及不同 VLA 在 pruned attention 下成功率提升的直观示意都在这里。
- 主证据锚点 1：来源：[[raw/2601_16065_DTP.pdf]]，`PDF p.1` Abstract + Fig. 1：
- 主证据锚点 2：来源：[[raw/2601_16065_DTP.pdf]]，distracting tokens 的问题定义、DTP 的总体动机，以及不同 VLA 在 pruned attention 下成功率提升的直观示意都在这里。
- 主证据锚点 3：来源：[[raw/2601_16065_DTP.pdf]]，`PDF p.2-4` Method + Fig. 2 / Fig. 3：

## Table / Metric Anchors
- `PDF p.4-5` Table 1：
  - SIMPLER WidowX Robot 上 SpatialVLA / Nora / UniVLA 的主结果在这里；`29.2% -> 37.5%`、`6.2% -> 11.5%`、`68.7% -> 74.0%` 都来自该表。
- `PDF p.5` Table 2：
  - SIMPLER Google Robot 上 SpatialVLA 与 Nora 的结果在这里，用于锚定“跨机器人泛化”的证据。
- `PDF p.5-6` Table 3：
  - LIBERO 上 `Nora + DTP` 的结果在这里；`LIBERO-10` 的 `69.6% -> 76.2%` 以及其余 suite 的提升都在这里。
- `PDF p.7-9` Table 4 / Table 5 + Fig. 5：
  - random pruning / no Gaussian 等 ablation，以及 unimportant attention 与 success/failure 的负相关分析都在这里。

## Table / Metric Split
- ``PDF p.4-5` Table 1` 这一层支撑 ``PDF p.4-5` Table 1` 对应的 benchmark / metric / operating point。 - SIMPLER WidowX Robot 上 SpatialVLA / Nora / UniVLA 的主结果在这里；`29.2% -> 37.5%`、`6.2% -> 11.5%`、`68.7% -> 74.0%` 都来自该表。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2601_16065_DTP.pdf]]，``PDF p.4-5` Table 1`。
- ``PDF p.5` Table 2` 这一层支撑 ``PDF p.5` Table 2` 对应的 benchmark / metric / operating point。 - SIMPLER Google Robot 上 SpatialVLA 与 Nora 的结果在这里，当前对应“跨机器人泛化”的证据。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2601_16065_DTP.pdf]]，``PDF p.5` Table 2`。
- ``PDF p.5-6` Table 3` 这一层支撑 ``PDF p.5-6` Table 3` 对应的 benchmark / metric / operating point。 - LIBERO 上 `Nora + DTP` 的结果在这里；`LIBERO-10` 的 `69.6% -> 76.2%` 以及其余 suite 的提升都在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2601_16065_DTP.pdf]]，``PDF p.5-6` Table 3`。
- ``PDF p.7-9` Table 4 / Table 5 + Fig. 5` 这一层支撑 ``PDF p.7-9` Table 4 / Table 5 + Fig. 5` 对应的 benchmark / metric / operating point。 - random pruning / no Gaussian 等 ablation，以及 unimportant attention 与 success/failure 的负相关分析都在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2601_16065_DTP.pdf]]，``PDF p.7-9` Table 4 / Table 5 + Fig. 5`。

## 不可混写项
- 当前 headline 里的提升值主要来自特定模型与特定 benchmark，不能写成统一“所有 VLA 都能获得某个固定收益”。
- `LIBERO` 结果只在 `Nora` 上额外验证；若写“DTP 在 LIBERO 上普遍有效”，需要保留模型范围 caveat。
- DTP 的目标更接近“改善 visual attention / 探索当前架构 performance upper bound”，不等于通用 token pruning recipe；后续主题归类要注意与一般 efficiency pruning 区分。

## 影响页面
- [[wiki/papers/2601_16065_DTP.md|2601_16065_DTP]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
