# 2603_07949_RAPID-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_07949_RAPID.md|2603_07949_RAPID]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`1.73×`、`15.8%`、`5%∼7%` 分别对应 speedup、accuracy improvement 和 system overhead；仍需把 baseline、任务与硬件语境拆清。

## Evidence
- 这篇论文的核心问题是：**现有面向 VLA 的 edge-cloud collaborative inference 往往依赖视觉环境特征做 partitioning，但这种环境导向策略容易受到 visual noise 干扰，而且忽略了 embodied task 中不同动作阶段的 step-wise redundancy**。作者据此提出 **RAPID**，希望用与环境更解耦的运动学信号来驱动 edge-cloud partitioning。来源：[[raw/2603_07949_RAPID.pdf]]，第 1-2 页 Abstract、Introduction、Fig. 1。
- 方法上的主张是一个 **kinematic-oriented edge-cloud co-inference framework**。RAPID 包含两套核心机制：一是 **Compatibility-Optimal Partitioning**，用运动学异常分数检测应否触发云端 offload；二是 **Redundancy-Aware Partitioning**，利用不同动作阶段的冗余差异和 torque / acceleration 等运动学特征，构造实时的 **Action Importance Score**，指导更优的 edge-cloud 分工。来源：[[raw/2603_07949_RAPID.pdf]]，第 1-4 页 Abstract、Introduction、Observation and Motivation、Sec. IV。
- 主证据锚点 1：来源：[[raw/2603_07949_RAPID.pdf]]，**Abstract + Introduction + Fig. 1**：第 1-2 页。用于锚定 vision-based partitioning 的局限、visual noise 问题，以及 RAPID 的整体 framing。
- 主证据锚点 2：来源：[[raw/2603_07949_RAPID.pdf]]，**Observation and Motivation / Fig. 2 / Fig. 3**：第 3-4 页。用于锚定为什么运动学指标更稳健，以及 redundancy 与 kinematics 的相关性。
- 主证据锚点 3：来源：[[raw/2603_07949_RAPID.pdf]]，**Sec. IV / Algorithm 1 / Fig. 4**：第 4-6 页。用于锚定 `Compatibility-Optimal`、`Redundancy-Aware`、`Action Importance Score` 和 dual-threshold dispatcher 的具体实现。

## Table / Metric Anchors
- **Simulation benchmark / Table III**：第 6 页。用于锚定 edge-side / cloud-side / total latency、load 分配，以及与 `Edge-Only VLA`、`ISAR` 的比较。
- **Real-world + Table IV / overhead discussion + Fig. 5**：第 6-7 页。用于锚定 `1.73×`、`15.8%`、`5%∼7%` 的具体语境，以及 overhead 来源和限制。

## Table / Metric Split
- `**Simulation benchmark / Table III**` 这一层应单独承载 `**Simulation benchmark / Table III**` 相关的 benchmark / metric / operating point。 这里收口为：**Simulation benchmark / Table III**：第 6 页。当前对应 edge-side / cloud-side / total latency、load 分配，以及与 `Edge-Only VLA`、`ISAR` 的比较。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_07949_RAPID.pdf]]，`**Simulation benchmark / Table III**`。
- `**Real-world + Table IV / overhead discussion + Fig. 5**` 这一层应单独承载 `**Real-world + Table IV / overhead discussion + Fig. 5**` 相关的 benchmark / metric / operating point。 这里收口为：**Real-world + Table IV / overhead discussion + Fig. 5**：第 6-7 页。当前对应 `1.73×`、`15.8%`、`5%∼7%` 的具体语境，以及 overhead 来源和限制。；`1.73×`、`15.8%`、`5%∼7%` 分别对应 speedup、accuracy improvement 和 system overhead；这里需要把 baseline、任务与硬件语境拆清。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_07949_RAPID.pdf]]，`**Real-world + Table IV / overhead discussion + Fig. 5**`。

## 不可混写项
- `1.73×`、`15.8%`、`5%∼7%` 分别对应 speedup、accuracy improvement 和 system overhead；仍需把 baseline、任务与硬件语境拆清。
- RAPID 当前同时被描述为 `kinematic-oriented ECC partitioning`、`compatibility-optimal + redundancy-aware framework`、`edge-cloud co-inference framework`；后续 taxonomy 需要统一主定位。
- 论文的主要收益是系统级协同推理收益，而不是 backbone-level model quality improvement；后续单篇主 claim 需要继续保持这个边界，避免被误读成“通用 VLA 提升”。

## 影响页面
- [[wiki/papers/2603_07949_RAPID.md|2603_07949_RAPID]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
