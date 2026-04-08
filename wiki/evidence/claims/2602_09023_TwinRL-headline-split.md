# 2602_09023_TwinRL-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_09023_TwinRL.md|2602_09023_TwinRL]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`42%`、`100%`、`30%`、`20 minutes` 目前仍是 bundled headline，仍需分别拆到 SFT warm-up、online RL、ID/OOD 区域和具体任务设置。

## Evidence
- 核心证据命题：TwinRL 的核心命题是：真实世界 VLA manipulation 的 online RL 瓶颈不只是 rollout 昂贵，更在于**有效 exploration space 被 SFT 数据分布强烈约束**；因此，若想让 real-world RL 真正高效，关键不只是多做在线交互，而是先用 high-fidelity digital twin 扩展探索空间，再用数字孪生持续引导真实机器人的探索重点。 来源：[[raw/2602_09023_TwinRL.pdf]]，**Abstract / introduction**：最清楚地给出 TwinRL 的总 framing：为什么 effective exploration space 受 SFT 分布约束，以及为什么 digital twin 应被用来扩展和引导探索。
- 补充证据命题：论文据此提出一个 digital twin–real-world collaborative RL 框架：在 SFT warm-up 阶段，利用数字孪生产生额外轨迹扩大 trajectory distribution support；进入 online RL 后，再在 digital twin 中并行跑 RL、构造 twin buffer、识别 failure-prone yet informative configurations，并把这些配置转化为 targeted human-in-the-loop rollouts。 来源：[[raw/2602_09023_TwinRL.pdf]]，**Fig. 1 (p.1)**：TwinRL 总体概览图，也是 `100%`、`20 minutes`、ID/OOD convergence 故事线的第一锚点。
- 主证据锚点 1：来源：[[raw/2602_09023_TwinRL.pdf]]，**Abstract / introduction**：最清楚地给出 TwinRL 的总 framing：为什么 effective exploration space 受 SFT 分布约束，以及为什么 digital twin 应被用来扩展和引导探索。
- 主证据锚点 2：来源：[[raw/2602_09023_TwinRL.pdf]]，**Fig. 1 (p.1)**：TwinRL 总体概览图，也是 `100%`、`20 minutes`、ID/OOD convergence 故事线的第一锚点。
- 主证据锚点 3：来源：[[raw/2602_09023_TwinRL.pdf]]，**Method section on digital twin construction and sim-to-real guided exploration**：若补 `L2`，这里是 smartphone-to-twin、parallel RL、targeted HiL 三段式流程的关键入口。

## Table / Metric Anchors
- **TABLE I (p.7)**：exploration space expansion 的核心消融锚点，用来核对 SFT warm-up 阶段 twin-generated ID/OOD trajectories 对 warm-up success 的影响。
- **TABLE II (p.7)**：twin buffer 消融锚点，用来判断 successful / failed trajectories 与 online RL steps / success 的关系。
- **FIG. 6 (p.7)**：guided HiL training-curve 锚点，用来核对 `100%` 与 `~14 min / ~20 min` 这组 online RL efficiency headline。

## Table / Metric Split
- `TABLE I | exploration-space expansion warm-up`：在 `0 ID / 0 OOD` twin data 时，warm-up `Avg SR = 27%`；加入 `30 ID / 30 OOD` 后升到 `57% (+30)`；`60 ID / 30 OOD` 升到 `67% (+40)`；`30 ID / 60 OOD` 则给出 `OOD 70%`、`Avg 70% (+43)`。因此 `42%` 级别的 headline 本质上是 warm-up augmentation 对 average success 的提升，不是 online RL 最终收敛结果。来源：[[raw/2602_09023_TwinRL.pdf]]，第 7 页，Table I。
- `TABLE II | twin buffer composition`：`20 S / 0 F` 时 online RL 只需 `3.5k` steps 且达到 `100%` success；`20 S / 20 F` 时是 `4.5k / 90%`；`20 S / 40 F` 时退化到 `7.0k / 70%`。因此 twin buffer 的 headline 应写成“成功轨迹主导的 replay 初始化更快更稳”，而不是笼统的 “digital twin improves RL”。来源：[[raw/2602_09023_TwinRL.pdf]]，第 7 页，Table II。
- `FIG. 6 | guided HiL efficiency`：有 twin-guided HiL 时，training curve 在大约 `4k steps (~14 min)` 达到 `100%`；正文同时把四个任务的平均在线训练时间概括为约 `20 minutes`。因此 `100%` 与 `20 minutes` 分别对应单任务训练曲线峰值和跨任务平均用时，不能 bundled 成一个无条件效率 headline。来源：[[raw/2602_09023_TwinRL.pdf]]，第 7 页，Fig. 6 与相邻文字。

## 不可混写项
- `42%`、`100%`、`30%`、`20 minutes` 目前仍是 bundled headline，仍需分别拆到 SFT warm-up、online RL、ID/OOD 区域和具体任务设置。
- 论文把 exploration space expansion 与 sim-to-real guided online RL 一起包装成 TwinRL 主体；后续 evidence 层可能需要区分“初始化分布扩展”的收益与“在线 twin-guided exploration”的收益。
- 论文强调 digital twin 可识别 failure-prone yet informative states，但当前更强的证据是“保留 difficulty landscape / convergence benefit”，仍应明确这类 twin fidelity claim 的边界，而不是直接等同于高保真 success-rate matching。

## 影响页面
- [[wiki/papers/2602_09023_TwinRL.md|2602_09023_TwinRL]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
