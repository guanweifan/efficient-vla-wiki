# 2603_05147_ActThinkAbstain

## Source

- Raw: [[raw/2603_05147_ActThinkAbstain.pdf]]
- Primary text fallback: [[extracts/parses/2603_05147_ActThinkAbstain/pdftotext.txt]]
- Fine-grained locator: [[extracts/parses/2603_05147_ActThinkAbstain/pdftotext.bbox.html]]

## Claim

这篇论文的核心命题是：VLA 的泛化与安全问题不应只靠“统一加重 reasoning”来解决，更合理的方向是先判断当前状态的复杂度，再决定是直接执行、额外思考，还是干脆拒绝执行。论文因此提出一个 complexity-aware adaptive inference 框架，把 VLA backbone 提取的 latent embedding 从“被动特征”改造成任务复杂度检测器，再据此在三条执行路径之间路由：**Act** 对已知且高置信任务直接执行，**Think** 对部分 OOD 或模糊场景触发额外 reasoning，**Abstain** 对严重 physical / semantic anomaly 直接停机。作者 headline claim 是：在 vision-only 配置下，复杂度检测器只用 `5%` 训练数据即可达到约 `80%` F1；完整 pipeline 在 LIBERO / LIBERO-PRO 与真实机器人上都能在保持 ID 任务成功率的同时，通过 Think/Abstain 提升部分 OOD 恢复能力与安全性。

显式 caveat：`80%` F1、模拟 benchmark 上的 success / prevented failures，以及 real-robot 的恢复与拒绝结果不是同一个层面的指标，不能被读成一个统一设置下的总性能数字。论文更稳的主张是：**复杂度检测 + 条件式 Act/Think/Abstain 路由** 能把 generalization、latency 和 safety 放进同一个 inference policy 里，而不是强制所有状态都走重 reasoning。

## Methodology Index

- **Complexity-aware adaptive inference**：先评估状态复杂度，再决定执行策略，而不是所有状态都统一走同样的推理路径。
- **Act / Think / Abstain routing**：把执行策略显式分成直接执行、额外 reasoning、主动拒绝三类。
- **VLM-backbone-as-detector**：把 SmolVLA 的 VLM backbone 从被动特征提取器改造成 complexity detector。
- **Vision / text / fused feature extraction**：分别抽取 visual、text、fused embedding，并评估哪种模态最适合复杂度判断。
- **GMM + kNN ensemble scoring**：用 parametric 与 non-parametric density estimators 对 latent novelty / OOD 程度打分。
- **MLP score aggregation**：将多路 novelty score 映射成离散的 Act / Think / Abstain 决策。

## Data Pointer

- **Abstract / introduction**：最清楚地说明论文为何反对对所有状态 indiscriminately 地施加 reasoning，以及为什么要把复杂度检测提前到执行前。
- **Fig. 1 (p.2)**：Act / Think / Abstain 路由总览图，也是 complexity detector 与执行分流如何衔接的第一锚点。
- **Fig. 3 / Fig. 4 (data scaling + confusion matrix)**：后续若补 `L2`，这里是 vision-only GMM 为何优于 text/fused，以及 `5%` 数据仍可达到 near-peak 表现的关键证据入口。
- **TABLE I (p.7)**：LIBERO / LIBERO-PRO 主结果锚点，用来核对 ID、partially OOD、fully OOD 下的 SR、PF、A/T/Ab 分布与推理时间。
- **TABLE II (p.7)**：SO-ARM 101 实机结果锚点，用来核对 ID、partially OOD、fully OOD 三类任务下的真实执行/拒绝表现。
- **Conclusion / limitations**：后续若补 `L2`，这里是 “almost perfect rejection rate” 和 rigid classification boundary 局限性的最好入口。

## 待核点

- `80%` F1、`5%` 训练数据、模拟中的 success / prevented failures，以及 real-robot 的执行结果目前仍是 bundled headline，后续需要拆到 detector quality、routing outcome 和 downstream task result 三个层面。
- 论文把复杂度检测器与 Act/Think/Abstain 执行策略一起包装成整体框架；后续 evidence 层可能需要区分“detector 本身是否可靠”与“Think / Abstain 路由是否真的带来任务级收益”。
- 当前实验主要基于 SmolVLA，作者也在 limitations 中承认尚未扩展到 `π0`、OpenVLA；后续需要明确它的 architecture-agnostic claim 到底有多少直接证据支持。
