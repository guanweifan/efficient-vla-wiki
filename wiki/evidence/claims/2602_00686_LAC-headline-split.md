# 2602_00686_LAC-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_00686_LAC.md|2602_00686_LAC]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`1.76x`、`+1.9`、`+5.0` 目前仍是 bundled headline，仍需分别拆到 LIBERO、SIMPLER、real-world 的具体实验设置和 base model 上。

## Evidence
- 核心证据命题：LAC 的核心命题是：VLA 推理加速不应继续依赖与任务目标脱节的 heuristic caching / pruning 规则，而应该被重写成一个直接对任务成功负责的 learnable computation policy。论文认为，现有 rule-based token caching 方法通常用 attention、saliency 等 proxy 决定 token 是否复用，但 “模型看哪里” 并不等于 “任务真正需要哪里”，这会让加速策略在动态场景下与任务目标错位。 来源：[[raw/2602_00686_LAC.pdf]]，**Abstract / introduction**：最清楚地说明论文为何反对 rule-based caching，以及为什么把推理加速重写成 learnable policy optimization 问题。
- 补充证据命题：为此，LAC 提出一个轻量的学习式 adaptive caching 框架，用两个协作模块共同决定缓存策略：Cached Token Selector 学习 token 级动态显著性，Cache Ratio Predictor 决定整体 token reuse budget。 来源：[[raw/2602_00686_LAC.pdf]]，**Figure 1 (p.1)**：最关键的 framing 图，直接对比 rule-based selector 与 LAC 的 learnable selector，并给出 `20%` vs `40%` cache ratio 的直观故事线。
- 主证据锚点 1：来源：[[raw/2602_00686_LAC.pdf]]，**Abstract / introduction**：最清楚地说明论文为何反对 rule-based caching，以及为什么把推理加速重写成 learnable policy optimization 问题。
- 主证据锚点 2：来源：[[raw/2602_00686_LAC.pdf]]，**Figure 1 (p.1)**：最关键的 framing 图，直接对比 rule-based selector 与 LAC 的 learnable selector，并给出 `20%` vs `40%` cache ratio 的直观故事线。
- 主证据锚点 3：来源：[[raw/2602_00686_LAC.pdf]]，**Figure 2 (p.3)**：LAC 两阶段训练框架的核心锚点，说明 selector 初始化与 joint optimization 如何衔接。

## Table / Metric Anchors
- **Table 1 (p.6)**：LIBERO 主结果锚点，用来核对 `1.76x` wall-clock speedup、`+1.9` 平均成功率和 FLOPs 下降。
- **Table 3 (p.8)**：SIMPLER / CogAct 结果锚点，用来支撑其跨架构可迁移性和 diffusion-style decoder 上的有效性。
- **Table 4 (p.8)**：real-world manipulation 结果锚点，用来支撑 `+5.0` 成功率提升与实际部署收益。
- **Table 2 / additional ablations**：若补 `L2`，这里是判断 selector、ratio predictor、stochastic recovery 各自贡献的关键位置。

## Table / Metric Split
- `**Table 1 (p.6)**` 这一层应单独承载 `**Table 1 (p.6)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_00686_LAC.pdf]]，`**Table 1 (p.6)**`。
- `**Table 3 (p.8)**` 这一层应单独承载 `**Table 3 (p.8)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_00686_LAC.pdf]]，`**Table 3 (p.8)**`。
- `**Table 4 (p.8)**` 这一层应单独承载 `**Table 4 (p.8)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_00686_LAC.pdf]]，`**Table 4 (p.8)**`。
- `**Table 2 / additional ablations**` 这一层应单独承载 `**Table 2 / additional ablations**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_00686_LAC.pdf]]，`**Table 2 / additional ablations**`。

## 不可混写项
- `1.76x`、`+1.9`、`+5.0` 目前仍是 bundled headline，仍需分别拆到 LIBERO、SIMPLER、real-world 的具体实验设置和 base model 上。
- 论文把 Cached Token Selector 与 Cache Ratio Predictor 共同包装成 LAC 主体；后续 evidence 层可能需要区分“token-level saliency 学习”的贡献与“global reuse budget 预测”的贡献。
- 论文强调 learned policy 比 heuristic 更 task-aware，但其 motion prior 仍依赖 optical flow；仍应明确这种设计在极端动态视觉条件下的适用边界，而不是直接泛化为所有场景都同样有效。

## 影响页面
- [[wiki/papers/2602_00686_LAC.md|2602_00686_LAC]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
