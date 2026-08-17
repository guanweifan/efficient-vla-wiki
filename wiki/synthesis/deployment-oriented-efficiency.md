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
- `EdgeVLA`、`VOTE`、`Video2Act`、`VLA-Perf`、`LiteVLA-Edge`、`Realtime-VLA V2`、`QuantVLA`、`DA-PTQ`、`ActQuant`、`Omega-QVLA`、`AsyncShield`、`DP-Cache / V-AEFusion`、`EdgeFM`、`Async-VLA-Inference`、`Realtime-VLA FLASH`、`ElegantVLA`、`Flash-WAM`、`DEFLECT`、`Fast-dDrive`、`OmniDreams`、`vla.cpp`、`Mix-QVLA`、`MemoryWAM`、`Embodied.cpp`、`VLM2VLA Parameter Redundancy`、`DTR`、`Kairos`、`SpikeVLA`、`Jetson-PI`、`GWP-0.5`、`Reflex`、`FutureRTC`、`TurboVLA`、`QuantWAMs`、`Actuation-Slack Refresh`、`CloudEdgeVLA`、`Faster-WAM` 共同表明：部署可行性已经不再是“附录里的系统注”，而是决定方法是否成立的一等设计对象。
- 当前稳定共识是：如果不说明 hardware、placement、pipeline layer 或 jitter，单个“实时 / 频率更高” headline 没有足够比较意义。
- 新增语料把部署证据继续推进到统一 runtime、decoder-only pruning、quality-guided exit、fast-slow switching、WAM call scheduling、confidence-gated cache 与 full-pipeline CUDA optimization；但这些证据覆盖的 pipeline layer 并不相同。
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
  - 代表：[[wiki/papers/2507_14049_EdgeVLA.md|EdgeVLA]]、[[wiki/papers/2603_03380_LiteVLA-Edge.md|LiteVLA-Edge]]、[[wiki/papers/2606_27807_SpikeVLA.md|SpikeVLA]]、[[wiki/papers/2607_27205_TurboVLA.md|TurboVLA]]
  - 依据：通过小模型、事件驱动稀疏计算、direct vision-language-to-action design 或 ROS/system integration 把部署目标直接嵌入模型设计。
- `low-bit deployment substrate`
  - 代表：[[wiki/papers/2602_20309_QuantVLA.md|QuantVLA]]、[[wiki/papers/2604_11572_DA-PTQ.md|DA-PTQ]]、[[wiki/papers/2605_24011_ActQuant.md|ActQuant]]、[[wiki/papers/2605_28803_QVLA-Omega-QVLA.md|Omega-QVLA]]、[[wiki/papers/2606_19565_Mix-QVLA.md|Mix-QVLA]]、[[wiki/papers/2607_28405_QuantWAMs.md|QuantWAMs]]
  - 依据：通过 VLA-specific PTQ、校准、drift-aware mixed precision、action-guided sub-4-bit PTQ、task-evidence-aware mixed precision 或 full-stack W4A4 quantization 降低 memory / inference cost；但若没有 hardware placement / jitter 证据，仍不能直接等同于完整 edge deployment。
- `structural compression for deployment`
  - 代表：[[wiki/papers/2606_27755_DTR-GateProbe.md|DTR / GateProbe]]、[[wiki/papers/2606_31382_VLM2VLA-Parameter-Redundancy.md|VLM2VLA Parameter Redundancy]]、[[wiki/papers/2608_07361_Planning-Token-Pruning.md|Planning-Token Pruning]]
  - 依据：通过 block-level redundancy probing、adaptation-divergence-guided parameter pruning，或 planning-token trajectory probe 引导 decoder-layer removal 降低模型结构成本；这类工作可以服务部署，但还需要和真实 hardware placement、latency、memory ceiling 分开记录。
- `representation-for-throughput`
  - 代表：[[wiki/papers/2507_05116_VOTE.md|VOTE]]
  - 依据：通过动作表示或输出接口设计去服务 edge throughput。
- `deployment-landscape analysis`
  - 代表：[[wiki/papers/2602_18397_VLA-Perf.md|VLA-Perf]]、[[wiki/papers/2604_24447_DP-Cache-V-AEFusion.md|DP-Cache / V-AEFusion]]
  - 依据：把 model/system/network/placement 或 model-hardware-CET 统一成可分析设计空间。
- `edge-runtime framework`
  - 代表：[[wiki/papers/2604_27476_EdgeFM.md|EdgeFM]]、[[wiki/papers/2605_24011_ActQuant.md|ActQuant]]、[[wiki/papers/2606_08094_vla.cpp.md|vla.cpp]]、[[wiki/papers/2607_02501_Embodied.cpp.md|Embodied.cpp]]、[[wiki/papers/2607_12659_Jetson-PI.md|Jetson-PI]]、[[wiki/papers/2607_13960_GigaWorld-Policy-0.5-GWP-0.5.md|GWP-0.5]]、[[wiki/papers/2608_03682_PhyAI.md|PhyAI]]
  - 依据：通过 thin runtime、operator table、agent-tuned kernels、native C/C++ low-bit runtime、ggml / llama.cpp-style VLA runtime、Jetson onboard engine、modular embodied C++ runtime，或跨 VLA / WAM adapter 的共享 graph / kernel / memory stack 处理 edge inference latency、hardware lock-in、multi-rate execution 和 cross-platform portability。
- `system throughput tuning`
  - 代表：[[wiki/papers/2603_26360_Realtime-VLA-V2.md|Realtime-VLA V2]]、[[wiki/papers/2605_13778_Realtime-VLA-FLASH.md|Realtime-VLA FLASH]]、[[wiki/papers/2605_29438_ElegantVLA.md|ElegantVLA]]、[[wiki/papers/2606_05254_Flash-WAM.md|Flash-WAM]]、[[wiki/papers/2606_07895_TBD-VLA.md|TBD-VLA]]、[[wiki/papers/2606_10040_Efficient-WAM-Efficient-WAM-RT.md|Efficient-WAM]]、[[wiki/papers/2606_20562_MemoryWAM.md|MemoryWAM]]、[[wiki/papers/2607_12287_Temporal-Redundancy-Reduction.md|Temporal Redundancy Reduction]]、[[wiki/papers/2607_13960_GigaWorld-Policy-0.5-GWP-0.5.md|GWP-0.5]]、[[wiki/papers/2607_14695_Reflex.md|Reflex]]、[[wiki/papers/2607_29596_FibVLA.md|FibVLA]]、[[wiki/papers/2608_00391_Actuation-Slack-Refresh.md|Actuation-Slack Refresh]]、[[wiki/papers/2608_02365_Faster-WAM-DoT.md|Faster-WAM]]
  - 依据：通过 calibration、trajectory shaping、speed adaptation、speculative inference、phase-adaptive reuse、selective refresh、streaming overlap、action-only deployment、shallow action module 或 persistent memory，把 control frequency、critical-path latency、long-history context 和 per-chunk inference 写成系统级吞吐问题。
  - 新增代表：[[wiki/papers/2608_06008_Adaptive-WAM.md|Adaptive-WAM]]、[[wiki/papers/2608_06434_EMS.md|EMS]]、[[wiki/papers/2608_06994_PILOT.md|PILOT]]、[[wiki/papers/2608_08725_WA-SpecDec.md|WA-SpecDec]]、[[wiki/papers/2608_09492_TempoWAM.md|TempoWAM]]、[[wiki/papers/2608_10824_Gated-VLA-Cache.md|Gated VLA-Cache]]、[[wiki/papers/2608_11521_RIFT.md|RIFT]]、[[wiki/papers/2608_12932_FlashDrive.md|FlashDrive]]、[[wiki/papers/2608_14379_ReflexVLA.md|ReflexVLA]]；它们分别改变执行深度、模型选择、部署期模块、验证接受率、调用次数、算力、future-cache 构造或完整流水线。
- `cloud-edge latency and jitter adaptation`
  - 代表：[[wiki/papers/2604_24086_AsyncShield.md|AsyncShield]]、[[wiki/papers/2605_08168_Async-VLA-Inference.md|Async-VLA-Inference]]、[[wiki/papers/2605_19294_DEFLECT.md|DEFLECT]]、[[wiki/papers/2607_24008_FutureRTC.md|FutureRTC]]、[[wiki/papers/2608_00569_CloudEdgeVLA.md|CloudEdgeVLA]]
  - 依据：把 delayed intent、observation staleness、prediction-execution misalignment 或 stale cloud features 通过 temporal alignment、delay-robust training/evaluation 或 offline correction 接回控制闭环。
- `fleet-aware serving`
  - 代表：[[wiki/papers/2605_11381_Kairos.md|Kairos]]
  - 依据：把多机器人 generate-execute loop、动态 execution horizon 与跨机器人调度作为 serving 一等对象。
- `structured-output serving`
  - 代表：[[wiki/papers/2605_23163_Fast-dDrive.md|Fast-dDrive]]、[[wiki/papers/2606_31160_Reasoning-aware-Speculative-Decoding-FlatRoPE-AARL.md|Reasoning-aware Speculative Decoding]]
  - 依据：在 driving VLA 中把 JSON-like trajectory output、scaffold tokens、shared-prefix rollout 或 chain-of-causation reasoning speculative decoding 与 serving throughput 绑定为部署侧效率问题。
- `world-model serving / closed-loop simulation`
  - 代表：[[wiki/papers/2606_03159_OmniDreams.md|OmniDreams]]
  - 依据：通过 action-conditioned video generation、streaming KV cache、multi-GPU inference 和 simulator integration，把实时闭环仿真的 sensor generation / serving path 纳入效率边界。
- `real-time rhetoric boundary`
  - 代表：[[wiki/papers/2512_03044_Video2Act.md|Video2Act]]
  - 依据：提醒“实时”必须回到 cold-start、pipeline layer 和具体 deployment setting 才成立。

## Boundary Conditions
- 如果一篇论文只给 benchmark latency、没有 placement、hardware、jitter 或 memory 层说明，则不能直接与 edge-deployment 主链比较。
- 低比特量化可以支撑 deployment feasibility，但 memory reduction / speedup 与真实控制频率、jitter、network placement 仍是不同层。
- `mean latency`、`control frequency`、`cold-start latency`、`jitter` 不在同一层，必须分开阅读。
- `on-device` 与 `server/cloud placement` 的结果不能直接并表，除非 system knob 和 network knob 被明确控制。
- framework benchmark speedup、model-hardware leaderboard 与 closed-loop navigation success 是不同层的部署证据；只能在明确 hardware / placement / jitter / task setting 后比较。
- 一篇论文若主要优化 inference method、本身不以 deployability 为主问题，只能作为边缘例子。
- delay-robust evaluation、offline stale-action tuning 与 cloud-edge safety adapter 都处理 latency，但分别是对照框架、post-training correction 和 edge runtime adapter。
- structured driving output 的 serving throughput 不能直接和 manipulation control frequency 合并。
- low-bit PTQ 的 memory reduction、native runtime latency、full-stack action-head quantization 与 real-world robot success 需要分开；[[wiki/papers/2605_24011_ActQuant.md|ActQuant]] 和 [[wiki/papers/2605_28803_QVLA-Omega-QVLA.md|Omega-QVLA]] 不能互相替代。
- portable runtime、low-bit quantization 和 persistent memory 都可能服务 deployment，但作用层不同：runtime 解决执行栈和硬件可移植性，quantization 解决 model memory / BitOps，persistent memory 解决 long-history context 成本。
- structural pruning 可以服务 deployment，但结构冗余、post-pruning recovery、真实运行延迟和硬件 memory ceiling 不是同一层证据。
- WAM real-time inference 与 AV simulator serving 需要保留 pipeline layer：[[wiki/papers/2606_05254_Flash-WAM.md|Flash-WAM]] 作用于 joint video-action denoising，[[wiki/papers/2606_03159_OmniDreams.md|OmniDreams]] 作用于 closed-loop world-model sensor generation。
- [[wiki/papers/2606_27807_SpikeVLA.md|SpikeVLA]] 的能耗是基于 operation counting 的估算，不是 neuromorphic board 实测；[[wiki/papers/2607_28405_QuantWAMs.md|QuantWAMs]] 的 Blackwell 数值是 block-level kernel 结果，不是完整 WAM 端到端提速。
- [[wiki/papers/2607_12659_Jetson-PI.md|Jetson-PI]] 的 inference latency、reaction latency 与 control frequency 是不同指标；[[wiki/papers/2608_00391_Actuation-Slack-Refresh.md|Actuation-Slack Refresh]] 的关键路径下降也不等于总 FLOPs 或能耗下降。
- [[wiki/papers/2608_00569_CloudEdgeVLA.md|CloudEdgeVLA]] 与 [[wiki/papers/2607_24008_FutureRTC.md|FutureRTC]] 主要证明延迟条件下的闭环鲁棒性；不能据此声称 cloud/network latency 被降低。
- [[wiki/papers/2608_03682_PhyAI.md|PhyAI]] 的 GPU / static-batch timing 未覆盖 capture、transport、queue、handoff 与 tail latency；[[wiki/papers/2608_12932_FlashDrive.md|FlashDrive]] 的 `4.7x` 来自多项算法和系统优化叠加，均不能改写成单一 kernel 或完整真实闭环的普遍收益。
- [[wiki/papers/2608_06434_EMS.md|EMS]] 的 effective switched frequency 不等于 slow VLA 本身频率；[[wiki/papers/2608_14379_ReflexVLA.md|ReflexVLA]] 的 `30 Hz` 是 benchmark 的注入相机设置，不能当作模型实测控制频率。
- [[wiki/papers/2608_07361_Planning-Token-Pruning.md|Planning-Token Pruning]] 的 decoder 实测与端到端投影、[[wiki/papers/2608_09492_TempoWAM.md|TempoWAM]] 的调用次数与 per-call runtime、[[wiki/papers/2608_10824_Gated-VLA-Cache.md|Gated VLA-Cache]] 的 TFLOPs 与 wall-clock latency 必须分栏阅读。

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
- [[wiki/papers/2604_24086_AsyncShield.md|AsyncShield]]
- [[wiki/papers/2604_24447_DP-Cache-V-AEFusion.md|DP-Cache / V-AEFusion]]
- [[wiki/papers/2604_27476_EdgeFM.md|EdgeFM]]
- [[wiki/papers/2605_08168_Async-VLA-Inference.md|Async-VLA-Inference]]
- [[wiki/papers/2605_13778_Realtime-VLA-FLASH.md|Realtime-VLA FLASH]]
- [[wiki/papers/2605_19294_DEFLECT.md|DEFLECT]]
- [[wiki/papers/2605_23163_Fast-dDrive.md|Fast-dDrive]]
- [[wiki/papers/2605_24011_ActQuant.md|ActQuant]]
- [[wiki/papers/2605_28803_QVLA-Omega-QVLA.md|Omega-QVLA]]
- [[wiki/papers/2605_29438_ElegantVLA.md|ElegantVLA]]
- [[wiki/papers/2606_03159_OmniDreams.md|OmniDreams]]
- [[wiki/papers/2606_05254_Flash-WAM.md|Flash-WAM]]
- [[wiki/papers/2606_07895_TBD-VLA.md|TBD-VLA]]
- [[wiki/papers/2606_08094_vla.cpp.md|vla.cpp]]
- [[wiki/papers/2606_10040_Efficient-WAM-Efficient-WAM-RT.md|Efficient-WAM]]
- [[wiki/papers/2606_14010_RT-VLA.md|RT-VLA]]
- [[wiki/papers/2606_19565_Mix-QVLA.md|Mix-QVLA]]
- [[wiki/papers/2606_20562_MemoryWAM.md|MemoryWAM]]

- [[wiki/papers/2606_27755_DTR-GateProbe.md|DTR / GateProbe]]
- [[wiki/papers/2606_31160_Reasoning-aware-Speculative-Decoding-FlatRoPE-AARL.md|Reasoning-aware Speculative Decoding]]
- [[wiki/papers/2606_31382_VLM2VLA-Parameter-Redundancy.md|VLM2VLA Parameter Redundancy]]
- [[wiki/papers/2607_02501_Embodied.cpp.md|Embodied.cpp]]
- [[wiki/papers/2605_11381_Kairos.md|Kairos]]
- [[wiki/papers/2606_27807_SpikeVLA.md|SpikeVLA]]
- [[wiki/papers/2607_12287_Temporal-Redundancy-Reduction.md|Temporal Redundancy Reduction]]
- [[wiki/papers/2607_12659_Jetson-PI.md|Jetson-PI]]
- [[wiki/papers/2607_13960_GigaWorld-Policy-0.5-GWP-0.5.md|GWP-0.5]]
- [[wiki/papers/2607_14695_Reflex.md|Reflex]]
- [[wiki/papers/2607_24008_FutureRTC.md|FutureRTC]]
- [[wiki/papers/2607_27205_TurboVLA.md|TurboVLA]]
- [[wiki/papers/2607_28405_QuantWAMs.md|QuantWAMs]]
- [[wiki/papers/2607_29596_FibVLA.md|FibVLA]]
- [[wiki/papers/2608_00391_Actuation-Slack-Refresh.md|Actuation-Slack Refresh]]
- [[wiki/papers/2608_00569_CloudEdgeVLA.md|CloudEdgeVLA]]
- [[wiki/papers/2608_02365_Faster-WAM-DoT.md|Faster-WAM]]
- [[wiki/papers/2608_03682_PhyAI.md|PhyAI]]
- [[wiki/papers/2608_06008_Adaptive-WAM.md|Adaptive-WAM]]
- [[wiki/papers/2608_06434_EMS.md|EMS]]
- [[wiki/papers/2608_06994_PILOT.md|PILOT]]
- [[wiki/papers/2608_07361_Planning-Token-Pruning.md|Planning-Token Pruning]]
- [[wiki/papers/2608_08725_WA-SpecDec.md|WA-SpecDec]]
- [[wiki/papers/2608_09492_TempoWAM.md|TempoWAM]]
- [[wiki/papers/2608_10824_Gated-VLA-Cache.md|Gated VLA-Cache]]
- [[wiki/papers/2608_11521_RIFT.md|RIFT]]
- [[wiki/papers/2608_12932_FlashDrive.md|FlashDrive]]
- [[wiki/papers/2608_14379_ReflexVLA.md|ReflexVLA]]
## Open Questions
- 当前 deployment 主题仍缺少统一把 `memory ceiling`、`network variability` 与 `closed-loop failure mode` 放在同一表述框架里的 evidence 页。
- `real-time` 在不同论文中对应的 pipeline layer 仍不一致，后续 closeout 需要继续防止混写。

## Gate Check
- `required_sections_complete: yes`
- `evidence_links_present: yes`
- `unscoped_comparative_claims: 0`
- `boundary_conditions_present: yes`
