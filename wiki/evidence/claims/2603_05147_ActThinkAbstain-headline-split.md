# 2603_05147_ActThinkAbstain-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_05147_ActThinkAbstain.md|2603_05147_ActThinkAbstain]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`80%` F1、`5%` 训练数据、模拟中的 success / prevented failures，以及 real-robot 的执行结果目前仍是 bundled headline，仍需拆到 detector quality、routing outcome 和 downstream task result 三个层面。

## Evidence
- 核心证据命题：这篇论文的核心命题是：VLA 的泛化与安全问题不应只靠“统一加重 reasoning”来解决，更合理的方向是先判断当前状态的复杂度，再决定是直接执行、额外思考，还是干脆拒绝执行。 来源：[[raw/2603_05147_ActThinkAbstain.pdf]]，**Abstract / introduction**：最清楚地说明论文为何反对对所有状态 indiscriminately 地施加 reasoning，以及为什么要把复杂度检测提前到执行前。
- 补充证据命题：论文因此提出一个 complexity-aware adaptive inference 框架，把 VLA backbone 提取的 latent embedding 从“被动特征”改造成任务复杂度检测器，再据此在三条执行路径之间路由：**Act** 对已知且高置信任务直接执行，**Think** 对部分 OOD 或模糊场景触发额外 reasoning，**Abstain** 对严重 physical / semantic anomaly 直接停机。 来源：[[raw/2603_05147_ActThinkAbstain.pdf]]，**Fig. 1 (p.2)**：Act / Think / Abstain 路由总览图，也是 complexity detector 与执行分流如何衔接的第一锚点。
- 主证据锚点 1：来源：[[raw/2603_05147_ActThinkAbstain.pdf]]，**Abstract / introduction**：最清楚地说明论文为何反对对所有状态 indiscriminately 地施加 reasoning，以及为什么要把复杂度检测提前到执行前。
- 主证据锚点 2：来源：[[raw/2603_05147_ActThinkAbstain.pdf]]，**Fig. 1 (p.2)**：Act / Think / Abstain 路由总览图，也是 complexity detector 与执行分流如何衔接的第一锚点。
- 主证据锚点 3：来源：[[raw/2603_05147_ActThinkAbstain.pdf]]，**Fig. 3 / Fig. 4 (data scaling + confusion matrix)**：若补 `L2`，这里是 vision-only GMM 为何优于 text/fused，以及 `5%` 数据仍可达到 near-peak 表现的关键证据入口。

## Table / Metric Anchors
- **TABLE I (p.7)**：LIBERO / LIBERO-PRO 主结果锚点，用来核对 ID、partially OOD、fully OOD 下的 SR、PF、A/T/Ab 分布与推理时间。
- **TABLE II (p.7)**：SO-ARM 101 实机结果锚点，用来核对 ID、partially OOD、fully OOD 三类任务下的真实执行/拒绝表现。

## Table / Metric Split
- `TABLE I | simulation routing outcome`：`Spatial base` 从 baseline `73.33 SR / 51.83s` 提升到 `80.00 SR / 44.31s`，`PF = 5`，路由为 `23 / 2 / 5`；`Object object` 从 `63.33 / 91.12s` 到 `66.67 / 69.44s`，`PF = 8`，路由为 `19 / 3 / 8`；`Long base` 从 `53.33 / 132.24s` 到 `60.00 / 80.91s`，`PF = 10`。这里支撑的是 partially OOD 场景中 Think/Abstain 带来的 task-level gain，不是 detector F1 本身。来源：[[raw/2603_05147_ActThinkAbstain.pdf]]，第 7 页，Table I。
- `TABLE I | fully OOD abstention`：在 `Goal swap`、`Object task`、`Spatial swap/task`、`Long swap/task` 这些 fully OOD 变体上，baseline 往往 `0 SR` 且单集耗时 `150s+`，而本文路由结果多为 `0 / 2 / 28`、`0 / 1 / 29`、`0 / 0 / 30`，把推理时间压到约 `3-9s`。因此“prevented failures”与“95% time reduction”是 fully OOD abstention 故事线，不应与 in-distribution success improvement 混写。来源：[[raw/2603_05147_ActThinkAbstain.pdf]]，第 7 页，Table I。
- `TABLE II | real-robot routing`：实机上 `ID` 任务为 `4 / 4`，路由 `4 / 0 / 0`；`Partially OOD` 为 `2 / 3`，路由 `1 / 2 / 0`；`Fully OOD` 为 `0 / 3`，路由 `0 / 0 / 3`。这张表支撑的是实机 routing 行为与 safety outcome，不是 vision-only detector 的 `80% F1 with 5% data`。后者属于 detector-quality 证据，应留到 figure/wording 轮次补。来源：[[raw/2603_05147_ActThinkAbstain.pdf]]，第 7 页，Table II。

## 不可混写项
- `80%` F1、`5%` 训练数据、模拟中的 success / prevented failures，以及 real-robot 的执行结果目前仍是 bundled headline，仍需拆到 detector quality、routing outcome 和 downstream task result 三个层面。
- 论文把复杂度检测器与 Act/Think/Abstain 执行策略一起包装成整体框架；后续 evidence 层可能需要区分“detector 本身是否可靠”与“Think / Abstain 路由是否真的带来任务级收益”。
- 当前实验主要基于 SmolVLA，作者也在 limitations 中承认尚未扩展到 `π0`、OpenVLA；仍应明确它的 architecture-agnostic claim 到底有多少直接证据支持。

## 影响页面
- [[wiki/papers/2603_05147_ActThinkAbstain.md|2603_05147_ActThinkAbstain]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
