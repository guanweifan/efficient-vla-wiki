# 2502_02175_VLA-Cache-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2502_02175_VLA-Cache.md|2502_02175_VLA-Cache]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`1.7x` 与 `15%` 是 abstract 里的 headline 数字，但正文中不同模型/场景下对应的具体度量并不完全相同；后续 `L2` 需要拆成按模型与 setting 的证据。

## Evidence
- 论文把自己的主要收益表述为：在 `LIBERO`、`SIMPLER` 和真实机器人设置中，**最高可达约 1.7x CUDA latency speedup 与约 15% control frequency 增益，同时任务成功率基本保持**。更稳的写法是：这些 headline 来自不同模型和 setting，不应压成统一 operating point。 来源：[[raw/2502_02175_VLA-Cache.pdf]]，第 1 页，Abstract。
- 在更具体的模拟结果里，作者声称相对标准 `OpenVLA`，`VLA-Cache` 在 `LIBERO` 上可实现 **27.31% FLOPs reduction** 与 **1.63x latency improvement**，同时平均 success rate 仅下降 **0.3%**；并且对 `OpenVLA-OFT` 这类更高频 VLA 仍然有增益。 来源：[[raw/2502_02175_VLA-Cache.pdf]]，第 8 页，Sec. 5.3 与 Table 2。
- 主证据锚点 1：来源：[[raw/2502_02175_VLA-Cache.pdf]]，**Abstract + Intro**：作者对问题设定、方法定位与 headline 数字主张的最紧凑版本。 来源：[[raw/2502_02175_VLA-Cache.pdf]]，第 1-2 页。
- 主证据锚点 2：来源：[[raw/2502_02175_VLA-Cache.pdf]]，**Method core**：`Sec. 3 Methodology` + `Figure 2`，这里最用于锚定“静态 token 选择 / task-relevance 过滤 / layer-adaptive reuse”三件事的局部证据。 来源：[[raw/2502_02175_VLA-Cache.pdf]]，第 3-4 页。
- 主证据锚点 3：来源：[[raw/2502_02175_VLA-Cache.pdf]]，**Failure mode of naive reuse**：`Table 1` 直接给出“只按静态性复用”会显著掉点，而 attention-based 过滤能恢复性能。 来源：[[raw/2502_02175_VLA-Cache.pdf]]，第 4 页，Table 1。

## Table / Metric Anchors
- **Failure mode of naive reuse**：`Table 1` 直接给出“只按静态性复用”会显著掉点，而 attention-based 过滤能恢复性能。  
  来源：[[raw/2502_02175_VLA-Cache.pdf]]，第 4 页，Table 1。
- **Main simulation result**：`Table 2`，若要补“相对 FastV / SparseVLM / baseline 的收益结构”，这里是主锚点。  
  来源：[[raw/2502_02175_VLA-Cache.pdf]]，第 8 页，Table 2。
- **Real-robot result**：`Table 5` 给总体真实机器人结果；`Table 7` 给动态背景鲁棒性。  
  来源：[[raw/2502_02175_VLA-Cache.pdf]]，第 9 页，Table 5；第 15 页，Table 7。

## Table / Metric Split
- `**Failure mode of naive reuse**` 这一层支撑 `**Failure mode of naive reuse**` 对应的 benchmark / metric / operating point。 `Table 1` 直接给出“只按静态性复用”会显著掉点，而 attention-based 过滤能恢复性能。 来源：[[raw/2502_02175_VLA-Cache.pdf]]，第 4 页，Table 1。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2502_02175_VLA-Cache.pdf]]，`**Failure mode of naive reuse**`。
- `**Main simulation result**` 这一层支撑 `**Main simulation result**` 对应的 benchmark / metric / operating point。 `Table 2`，当前用于拆开“相对 FastV / SparseVLM / baseline 的收益结构”，这里是主证据入口。 来源：[[raw/2502_02175_VLA-Cache.pdf]]，第 8 页，Table 2。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2502_02175_VLA-Cache.pdf]]，`**Main simulation result**`。
- `**Real-robot result**` 这一层支撑 `**Real-robot result**` 对应的 benchmark / metric / operating point。 `Table 5` 给总体真实机器人结果；`Table 7` 给动态背景鲁棒性。 来源：[[raw/2502_02175_VLA-Cache.pdf]]，第 9 页，Table 5；第 15 页，Table 7。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2502_02175_VLA-Cache.pdf]]，`**Real-robot result**`。

## 不可混写项
- `1.7x` 与 `15%` 是 abstract 里的 headline 数字，但正文中不同模型/场景下对应的具体度量并不完全相同；后续 `L2` 需要拆成按模型与 setting 的证据。
- 当前页面把 `OpenVLA`、`OpenVLA-OFT`、`CogAct` 上的效果合并在同一层概述里；如果要做更细的 `claims/tables` 页面，需要分模型整理。
- 真实机器人部分使用的是 fine-tuned `OpenVLA` policy 作为被加速对象；若要强调“training-free”的边界，需要明确区分“加速方法不训练”与“底座 policy 本身可能已被 fine-tune”，也不要把 temporal caching 和单帧 pruning 混成一类方法。

## 影响页面
- [[wiki/papers/2502_02175_VLA-Cache.md|2502_02175_VLA-Cache]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
