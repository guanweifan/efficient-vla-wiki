# deployment-oriented-efficiency

## Question
- 边缘部署、显存约束、频率目标、系统 placement 与 jitter 何时成为高效 VLA 的一等设计对象，而不是事后补充指标？

## Shared Ground
- 本页是 [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]] 之下的场景子主题页；它处理 deployability 何时成为效率的一等设计对象。
- 当前主题的固定比较轴是：
  - `task performance` vs `system deployability`
  - `model knob` vs `system knob` vs `network knob`
  - `on-device / edge latency` vs `task-performance benchmark`
  - `mean latency` vs `control frequency` vs `cold-start latency` vs `jitter`
- `EdgeVLA`、`VOTE`、`Video2Act`、`VLA-Perf`、`LiteVLA-Edge`、`Realtime-VLA V2`、`QuantVLA`、`DA-PTQ` 共同表明：部署可行性已经不再是“附录里的系统注”，而是决定方法是否成立的一等设计对象。
- 当前稳定共识是：如果不说明 hardware、placement、pipeline layer 或 jitter，单个“实时 / 频率更高” headline 没有足够比较意义。
- 共享 runtime evidence 已经稳定支撑 deployment 主题：部署问题必须同时读 performance 和 system constraint，不能只摘一个 latency 行。

## Theme Structure
- 结构角色：deployment / system 场景子主题页。
- 总纲页：[[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]
- 相邻但不等价的子主题：
  - [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
  - [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- 本页关注“在什么系统条件下才算可部署”，不是一般意义上的 inference route 比较。

## Route Split
- `edge-native model design`
  - 代表：[[wiki/papers/2507_14049_EdgeVLA.md|EdgeVLA]]、[[wiki/papers/2603_03380_LiteVLA-Edge.md|LiteVLA-Edge]]
  - 依据：通过小模型、on-device design 或 ROS/system integration 把部署目标直接嵌入模型设计。
- `low-bit deployment substrate`
  - 代表：[[wiki/papers/2602_20309_QuantVLA.md|QuantVLA]]、[[wiki/papers/2604_11572_DA-PTQ.md|DA-PTQ]]
  - 依据：通过 VLA-specific PTQ、校准或 drift-aware mixed precision 降低 memory / inference cost；但若没有 hardware placement / jitter 证据，仍不能直接等同于完整 edge deployment。
- `representation-for-throughput`
  - 代表：[[wiki/papers/2507_05116_VOTE.md|VOTE]]
  - 依据：通过动作表示或输出接口设计去服务 edge throughput。
- `deployment-landscape analysis`
  - 代表：[[wiki/papers/2602_18397_VLA-Perf.md|VLA-Perf]]
  - 依据：把 model/system/network/placement 统一成可分析设计空间。
- `system throughput tuning`
  - 代表：[[wiki/papers/2603_26360_Realtime-VLA-V2.md|Realtime-VLA V2]]
  - 依据：通过 calibration、trajectory shaping、speed adaptation 与硬件约束补偿，把 faster-than-demonstration execution 写成系统级吞吐问题。
- `real-time rhetoric boundary`
  - 代表：[[wiki/papers/2512_03044_Video2Act.md|Video2Act]]
  - 依据：提醒“实时”必须回到 cold-start、pipeline layer 和具体 deployment setting 才成立。

## Boundary Conditions
- 如果一篇论文只给 benchmark latency、没有 placement、hardware、jitter 或 memory 层说明，则不能直接与 edge-deployment 主链比较。
- 低比特量化可以支撑 deployment feasibility，但 memory reduction / speedup 与真实控制频率、jitter、network placement 仍是不同层。
- `mean latency`、`control frequency`、`cold-start latency`、`jitter` 不在同一层，必须分开阅读。
- `on-device` 与 `server/cloud placement` 的结果不能直接并表，除非 system knob 和 network knob 被明确控制。
- 一篇论文若主要优化 inference method、本身不以 deployability 为主问题，只能作为边缘例子。

## Not Directly Comparable
- 只报告更高 Hz、没有具体 hardware / placement / jitter 说明的论文，不能直接进入本主题主比较。
- 纯 inference acceleration 方法，如果不以 deployment feasibility 为主问题，只能提供边界说明。
- 只在封闭 benchmark 中报告 latency、没有闭环 deployment 条件的结果，不能直接与 edge / on-device 结果比较。

## Evidence Links
- [[wiki/evidence/metrics/runtime-vs-task-metrics.md|runtime-vs-task-metrics]]
- [[wiki/papers/2507_14049_EdgeVLA.md|EdgeVLA]]
- [[wiki/papers/2507_05116_VOTE.md|VOTE]]
- [[wiki/papers/2512_03044_Video2Act.md|Video2Act]]
- [[wiki/papers/2602_18397_VLA-Perf.md|VLA-Perf]]
- [[wiki/papers/2603_03380_LiteVLA-Edge.md|LiteVLA-Edge]]
- [[wiki/papers/2603_26360_Realtime-VLA-V2.md|Realtime-VLA V2]]
- [[wiki/papers/2602_20309_QuantVLA.md|QuantVLA]]
- [[wiki/papers/2604_11572_DA-PTQ.md|DA-PTQ]]

## Open Questions
- 当前 deployment 主题仍缺少统一把 `memory ceiling`、`network variability` 与 `closed-loop failure mode` 放在同一表述框架里的 evidence 页。
- `real-time` 在不同论文中对应的 pipeline layer 仍不一致，后续 closeout 需要继续防止混写。

## Gate Check
- `required_sections_complete: yes`
- `evidence_links_present: yes`
- `unscoped_comparative_claims: 0`
- `boundary_conditions_present: yes`
