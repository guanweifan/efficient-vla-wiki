# 2411_02359_DeeR-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2411_02359_DeeR-VLA.md|2411_02359_DeeR-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：论文多次写“without sacrificing performance”，但主实验仍集中在 CALVIN benchmark；后续 L2 需要把这个表述收紧到具体 setting，不宜过早泛化成真实机器人结论。

## Evidence
- 作者提出 `DeeR-VLA / DeeR`，并声称它能在 `CALVIN + RoboFlamingo/OpenFlamingo` 这组主设置下把 **LLM-side** 计算量降到原来的 `1/5.2` 到 `1/6.5`，把 **LLM-side** 显存降到原来的 `1/2` 到 `1/6`，且不牺牲整体表现；在相同性能下，实际 **LLM inference time** 从 `55ms` 降到 `17.5ms`。更稳的写法是：这些 headline 主要说明语言模型分支的推理效率，而不是视觉编码器或整套机器人系统的端到端成本。来源：[[raw/2411_02359_DeeR-VLA.pdf]]，第 1 页摘要；第 9 页 Table 5。
- 补充证据命题：核心主张是：机器人控制过程中存在大量“较容易”的时刻，不需要始终激活完整大模型；因此可以为机器人 MLLM 构建多出口、按情境动态提前退出的推理机制，在维持任务表现的同时显著降低 LLM 侧推理成本。 来源：[[raw/2411_02359_DeeR-VLA.pdf]]，动机证据：[[raw/2411_02359_DeeR-VLA.pdf]] 第 2 页 Table 1。这里展示用更浅层 LLM 时成功率下降很小，但 FLOPs 成倍下降，是“easy situations dominate”论点的直接支撑。
- 主证据锚点 1：来源：[[raw/2411_02359_DeeR-VLA.pdf]]，摘要与问题设定：[[raw/2411_02359_DeeR-VLA.pdf]] 第 1 页摘要。这里给出任务动机、DeeR 的一句话定义，以及 `5.2-6.5x` 计算下降、`2-6x` 显存下降的 headline claim。
- 主证据锚点 2：来源：[[raw/2411_02359_DeeR-VLA.pdf]]，动机证据：[[raw/2411_02359_DeeR-VLA.pdf]] 第 2 页 Table 1。这里展示用更浅层 LLM 时成功率下降很小，但 FLOPs 成倍下降，是“easy situations dominate”论点的直接支撑。
- 主证据锚点 3：来源：[[raw/2411_02359_DeeR-VLA.pdf]]，核心机制：[[raw/2411_02359_DeeR-VLA.pdf]] 第 5-6 页 Section 3.2。这里定义 action-consistency 提前退出准则、预算化任务执行问题以及 dataset / online 两种 threshold 求解方式。

## Table / Metric Anchors
- 动机证据：[[raw/2411_02359_DeeR-VLA.pdf]] 第 2 页 Table 1。这里展示用更浅层 LLM 时成功率下降很小，但 FLOPs 成倍下降，是“easy situations dominate”论点的直接支撑。
- 主结果与效率曲线：[[raw/2411_02359_DeeR-VLA.pdf]] 第 7 页 Table 2；第 8 页 Figure 3；第 9 页 Figure 4。这里分别对应与 baselines 的比较、3B 模型上的效率-性能曲线，以及 9B 上的可扩展性结果。
- 实际推理效率：[[raw/2411_02359_DeeR-VLA.pdf]] 第 9 页 Table 5。这里给出与 RoboFlamingo++ 的真实推理时延比较。

## Table / Metric Split
- `Table 1` 对应 **easy-situation motivation** 这一层：它支撑的是“更浅层出口已经能覆盖大量简单时刻，因此 early exit 有潜在收益”，不是 `DeeR` 相对 baselines 的主结果表。来源：[[raw/2411_02359_DeeR-VLA.pdf]]，第 2 页，Table 1。
- `Table 2 / Fig. 3 / Fig. 4` 对应 **CALVIN performance-efficiency frontier**：这里需要区分 `DeeR` 与 `DeeR w. online` 两种 threshold 求解方式，也要区分 3B / 9B 的效率-性能曲线；因此 `5.2-6.5x` compute reduction 与“without sacrificing performance”不能脱离具体设置独立引用。来源：[[raw/2411_02359_DeeR-VLA.pdf]]，第 7-9 页，Table 2、Figure 3、Figure 4。
- `Table 5` 对应 **real LLM-side inference efficiency**：在相近表现 (`Len 4.07` vs `4.08`) 下，`Robo++` 的 LLM 侧 `31.2 GFLOPs / 55ms` 对比 `DeeR` 的 `6 GFLOPs / 17.5ms`；这里支撑的是 `LLM-side` latency / compute 优势，而不是整套 VLA 端到端成本。来源：[[raw/2411_02359_DeeR-VLA.pdf]]，第 9 页，Table 5。

## 不可混写项
- 论文多次写“without sacrificing performance”，但主实验仍集中在 CALVIN benchmark；后续 L2 需要把这个表述收紧到具体 setting，不宜过早泛化成真实机器人结论。
- 该文的大部分 headline efficiency 指标都明确是 `LLM` 侧 FLOPs / memory / latency，而不是整套 VLA 端到端系统成本；后续证据页需要避免把它误写成全系统加速或 general robot control frequency 提升。
- Table 2 同时包含 `DeeR` 与 `DeeR w. online` 两种 threshold 求解方式；chief-editor 需决定 paper-level 默认主结果应优先指向哪一行。

## 影响页面
- [[wiki/papers/2411_02359_DeeR-VLA.md|2411_02359_DeeR-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
