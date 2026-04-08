# 2603_19131_EmbodiedEff-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_19131_EmbodiedEff.md|2603_19131_EmbodiedEff]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`13.6%`、`46.2%`、`34.5%`、`13.2%`、`25.8%` 等 headline 数字目前仍是 bundled summary，仍需拆到具体 intervention、模型与 benchmark。

## Evidence
- 核心证据命题：这篇论文的核心命题是：当前 VLA 研究里流行的 “efficiency” 几乎都在看参数量、FLOPs、decoding throughput 等 inference-side 指标，但这些指标并不能真实反映机器人系统在物理世界中的整体执行效率。 来源：[[raw/2603_19131_EmbodiedEff.pdf]]，**Abstract / introduction**：最清楚地给出论文为什么要从 inference efficiency 转向 embodied efficiency，以及两者为何会错位。
- 补充证据命题：论文主张应把评估重心从单纯的 **inference efficiency** 扩展到 **embodied efficiency**，显式纳入 task completion time、end-effector / joint path length、motion smoothness、action rate 等 system-level 指标。 来源：[[raw/2603_19131_EmbodiedEff.pdf]]，**Fig. 1 (p.1)**：最直接的反例图，展示 `5%` vs `20%` 剪枝下 success rate 相同但 completion time 明显不同，说明 “inference-efficient” 不等于 “embodied-efficient”。
- 主证据锚点 1：来源：[[raw/2603_19131_EmbodiedEff.pdf]]，**Abstract / introduction**：最清楚地给出论文为什么要从 inference efficiency 转向 embodied efficiency，以及两者为何会错位。
- 主证据锚点 2：来源：[[raw/2603_19131_EmbodiedEff.pdf]]，**Fig. 1 (p.1)**：最直接的反例图，展示 `5%` vs `20%` 剪枝下 success rate 相同但 completion time 明显不同，说明 “inference-efficient” 不等于 “embodied-efficient”。
- 主证据锚点 3：来源：[[raw/2603_19131_EmbodiedEff.pdf]]，**Fig. 2 (p.2)**：模型推理阶段与机器人执行阶段的分层示意图，是这篇论文评估口径重构的核心 framing 图。

## Table / Metric Anchors
- **TABLE I (p.4)**：weight pruning 的 embodied metrics 主表，用来核对剪枝后 success rate、completion time、path length、jerk、action rate 的变化。
- **TABLE II (p.5)**：weight quantization 的 embodied metrics 主表，用来判断低比特量化对 smoothness / path cost 的影响。
- **TABLE III (p.6)**：FAST tokenizer 的 action compression 主表，用来核对 “更快完成” 与 “jerk 更高” 之间的 trade-off。
- **TABLE IV (p.6) / TABLE V (p.6)**：分别对应 in-context prompting 与 supervised fine-tuning 的 embodied-efficiency 影响，用来核对 jerk、action rate 与 completion time 的联动变化。

## Table / Metric Split
- `**TABLE I (p.4)**` 这一层应单独承载 `**TABLE I (p.4)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_19131_EmbodiedEff.pdf]]，`**TABLE I (p.4)**`。
- `**TABLE II (p.5)**` 这一层应单独承载 `**TABLE II (p.5)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_19131_EmbodiedEff.pdf]]，`**TABLE II (p.5)**`。
- `**TABLE III (p.6)**` 这一层应单独承载 `**TABLE III (p.6)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_19131_EmbodiedEff.pdf]]，`**TABLE III (p.6)**`。
- `**TABLE IV (p.6) / TABLE V (p.6)**` 这一层应单独承载 `**TABLE IV (p.6) / TABLE V (p.6)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_19131_EmbodiedEff.pdf]]，`**TABLE IV (p.6) / TABLE V (p.6)**`。

## 不可混写项
- `13.6%`、`46.2%`、`34.5%`、`13.2%`、`25.8%` 等 headline 数字目前仍是 bundled summary，仍需拆到具体 intervention、模型与 benchmark。
- 论文把 pruning、quantization、token sparsification、action compression、prompting、SFT 全部放进同一篇评估框架；后续 evidence 层可能需要区分“评估论点本身”与“各具体 intervention 的实证结论”。
- 这篇论文的核心贡献更偏 evaluation / metric critique，而不是新 VLA method；后续在 synthesis 层需要明确它是“评估框架重构”类型，避免被误并入普通 efficiency 方法页。

## 影响页面
- [[wiki/papers/2603_19131_EmbodiedEff.md|2603_19131_EmbodiedEff]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
