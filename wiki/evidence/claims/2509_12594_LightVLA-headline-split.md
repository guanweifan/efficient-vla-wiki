# 2509_12594_LightVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2509_12594_LightVLA.md|2509_12594_LightVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`59.1% FLOPs reduction`、`38.2% latency reduction`、`2.6% success-rate improvement` 目前都保留为 headline；仍需精确拆清它们对应的比较对象、GPU / runtime setting 和是否全部相对 OpenVLA-OFT。

## Evidence
- 这篇论文提出 **LightVLA**，目标是让 VLA 的 visual token pruning 从固定比例、启发式压缩，转向**performance-driven、differentiable、adaptive** 的动态选择。作者的核心判断是：在 VLA 中，视觉 token 是否保留，应该由任务表现驱动，而不是由预先设定的 pruning ratio 或 “magic numbers” 决定。来源：[[raw/2509_12594_LightVLA.pdf]]，第 1 页 Abstract；第 2-4 页 Introduction、Method。
- 方法上的关键主张是：LightVLA 用 **dynamic query** 评估 visual token importance，并通过 **Gumbel-softmax** 实现 differentiable token selection；主版本强调 **不引入额外可训练参数**、不需要额外 auxiliary loss，也不依赖固定保留 token 数。来源：[[raw/2509_12594_LightVLA.pdf]]，第 1 页 Abstract；第 3-4 页 Fig. 2、Sec. III。
- 主证据锚点 1：来源：[[raw/2509_12594_LightVLA.pdf]]，**Abstract**：第 1 页。可直接承载 “dynamic query + Gumbel-softmax + 59.1% / 38.2% / 2.6%” 的 headline claim。
- 主证据锚点 2：来源：[[raw/2509_12594_LightVLA.pdf]]，**Fig. 1 + Introduction**：第 1-2 页。用于锚定“更少 visual tokens 但更高 performance”的 framing，以及与 common VLA / acceleration baselines 的相对位置。
- 主证据锚点 3：来源：[[raw/2509_12594_LightVLA.pdf]]，**Fig. 2 + Sec. III**：第 3-4 页。用于锚定 `dynamic query -> token scoring -> Gumbel-softmax` 的主方法链条，以及 parameter-free query generation。

## Table / Metric Anchors
- **Table I / Table II**：第 5 页。用于锚定 LIBERO 四个 task suite 上的 success-rate 结果，以及相对 OpenVLA-OFT 的 FLOPs / latency / token-count 对比。
- **Table III / Table IV**：第 5-6 页。用于锚定 noise-factor schedule、retained-token 数量与性能之间的关系。
- **Table V + Fig. 4 / Fig. 5**：第 7 页。用于锚定 `LightVLA*` 变体、learnable query 位置差异，以及复杂 long-horizon 任务上的补充结果。

## Table / Metric Split
- `**Table I / Table II**` 这一层应单独承载 `**Table I / Table II**` 相关的 benchmark / metric / operating point。 这一层对应 LIBERO 四个 task suite 上的 success-rate 结果，以及相对 OpenVLA-OFT 的 FLOPs / latency / token-count 对比。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2509_12594_LightVLA.pdf]]，`**Table I / Table II**`。
- `**Table III / Table IV**` 这一层应单独承载 `**Table III / Table IV**` 相关的 benchmark / metric / operating point。 这一层对应 noise-factor schedule、retained-token 数量与性能之间的关系。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2509_12594_LightVLA.pdf]]，`**Table III / Table IV**`。
- `**Table V + Fig. 4 / Fig. 5**` 这一层应单独承载 `**Table V + Fig. 4 / Fig. 5**` 相关的 benchmark / metric / operating point。 这里收口为：**Table V + Fig. 4 / Fig. 5**：第 7 页。当前对应 `LightVLA*` 变体、learnable query 位置差异，以及复杂 long-horizon 任务上的补充结果。；主版本 `LightVLA` 与带额外参数的 `LightVLA*` 容易混淆；这里需要在主题页和 evidence 页统一“主方法”和“变体”的叙述口径。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2509_12594_LightVLA.pdf]]，`**Table V + Fig. 4 / Fig. 5**`。

## 不可混写项
- `59.1% FLOPs reduction`、`38.2% latency reduction`、`2.6% success-rate improvement` 目前都保留为 headline；仍需精确拆清它们对应的比较对象、GPU / runtime setting 和是否全部相对 OpenVLA-OFT。
- 主版本 `LightVLA` 与带额外参数的 `LightVLA*` 容易混淆；仍需在主题页和 evidence 页统一“主方法”和“变体”的叙述口径。
- 论文多次使用 `state-of-the-art`、`best performance` 一类表述，但实验主要集中在 **LIBERO** 与特定 foundation model；仍需决定在单篇主 claim 中保留多强的 performance 语气。

## 影响页面
- [[wiki/papers/2509_12594_LightVLA.md|2509_12594_LightVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
