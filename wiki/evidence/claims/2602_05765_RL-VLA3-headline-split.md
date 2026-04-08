# 2602_05765_RL-VLA3-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_05765_RL-VLA3.md|2602_05765_RL-VLA3]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：这篇的核心贡献是训练基础设施与系统吞吐，不是推理延迟或 policy architecture 本身；如果进入效率 taxonomy，需要避免把它误归为 inference acceleration。

## Evidence
- success-rate curves 与 baseline 基本保持一致，说明这首先是一篇“效率-性能保持”的系统论文，而不是任务性能突破论文。来源：[[raw/2602_05765_RL-VLA3.pdf]]，第 1 页摘要；第 6-8 页 Table 1、Fig. 2-3；附录 B.1。
- 补充证据命题：核心主张是：如果把 VLA 强化学习训练流水线从 environment interaction、rollout generation 到 actor update 全部改写成分层异步系统，并进一步引入细粒度异步交互与 streaming micro-batch 更新，就能显著提升训练吞吐，同时基本保持训练成功率曲线和最终性能。 来源：[[raw/2602_05765_RL-VLA3.pdf]]，系统结构与异步机制：[[raw/2602_05765_RL-VLA3.pdf]] 第 3-5 页 Fig. 1 与 Section 3。这里定义 macro-level 与 micro-level asynchronous design、`Dynamic Batching Scheduler`、以及 `Streamer` 如何用 micro-batch 提前启动训练。
- 主证据锚点 1：来源：[[raw/2602_05765_RL-VLA3.pdf]]，摘要与总体命题：[[raw/2602_05765_RL-VLA3.pdf]] 第 1 页摘要与引言。这里给出 `full asynchronism`、`59.25% / 126.67%` throughput headline，以及 environment / rollout / actor 三层异步框架。
- 主证据锚点 2：来源：[[raw/2602_05765_RL-VLA3.pdf]]，系统结构与异步机制：[[raw/2602_05765_RL-VLA3.pdf]] 第 3-5 页 Fig. 1 与 Section 3。这里定义 macro-level 与 micro-level asynchronous design、`Dynamic Batching Scheduler`、以及 `Streamer` 如何用 micro-batch 提前启动训练。
- 主证据锚点 3：来源：[[raw/2602_05765_RL-VLA3.pdf]]，主吞吐结果：[[raw/2602_05765_RL-VLA3.pdf]] 第 6-7 页 Table 1 与 Fig. 2。这里对应 `LIBERO + π0.5`、`LIBERO + GR00T N1.5`、`ManiSkill + π0` 的 throughput 对比，以及 `59.25%` 与 `126.67%` 的主要出处。

## Table / Metric Anchors
- 主吞吐结果：[[raw/2602_05765_RL-VLA3.pdf]] 第 6-7 页 Table 1 与 Fig. 2。这里对应 `LIBERO + π0.5`、`LIBERO + GR00T N1.5`、`ManiSkill + π0` 的 throughput 对比，以及 `59.25%` 与 `126.67%` 的主要出处。

## Table / Metric Split
- `主吞吐结果` 这一层应单独承载 `主吞吐结果` 相关的 benchmark / metric / operating point。 这里收口为：主吞吐结果：[[raw/2602_05765_RL-VLA3.pdf]] 第 6-7 页 Table 1 与 Fig. 2。这里对应 `LIBERO + π0.5`、`LIBERO + GR00T N1.5`、`ManiSkill + π0` 的 throughput 对比，以及 `59.25%` 与 `126.67%` 的主要出处。；`59.25%` 与 `126.67%` 都是 throughput 口径，分别对应不同 baseline/placement ratio/async 组合，不能压成单一无条件提升。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_05765_RL-VLA3.pdf]]，`主吞吐结果`。

## 不可混写项
- 这篇的核心贡献是训练基础设施与系统吞吐，不是推理延迟或 policy architecture 本身；如果进入效率 taxonomy，需要避免把它误归为 inference acceleration。
- `59.25%` 与 `126.67%` 都是 throughput 口径，分别对应不同 baseline/placement ratio/async 组合，不能压成单一无条件提升。
- 论文提到 real robot deployments，但正文主结果仍然以 `LIBERO` 与 `ManiSkill` 的 RL training infrastructure 实验为主；“real-world validated”需要比 benchmark throughput claim 更保守。

## 影响页面
- [[wiki/papers/2602_05765_RL-VLA3.md|2602_05765_RL-VLA3]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
