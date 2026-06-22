# efficiency-definition-evolution

## Question
- 高效 VLA 的“效率”如何从粗粒度的“更快/更小”宣传，演化成必须分开讨论 runtime、task performance、training cost、deployment constraint 与 wording boundary 的多轴定义？

## Shared Ground
- 本页在主题建模阶段形成的主题层中充当总纲 / 入口页；它负责统一“效率”这个问题的比较轴与 wording boundary，其他 `4` 个主题页分别承接 inference、training、reasoning 与 deployment 子主题。
- 当前主题的固定比较轴是：
  - `runtime / latency / throughput / frequency`
  - `task performance / success / Avg. Len.`
  - `training cost / GPU hours / data ratio / steps`
  - `deployment constraint / placement / jitter / memory ceiling`
  - `training-free / model-agnostic` 的 wording boundary
- `TinyVLA`、`HiRT`、`FlashVLA`、`EfficientVLA` 这一条主链共同表明，速度 headline 只有在和同一 operating point 上的任务表现一起阅读时才有意义。
- `FAST`、`FT-NCFM`、`FrameSkip`、`PCM`、`D-VLA`、`VLA-AD`、`Agentic-VLA`、`EXPO-FT` 与 `ForesightFlow` 共同表明，训练侧效率已经是独立命题；更少 GPU 小时、更少训练步数、更少数据比例、更少梯度计算、更快在线适配、更少真实机器人在线数据或避免 separate critic pipeline，不能被偷换成推理更快。
- `VLA-Perf`、`AsyncShield`、`Async-VLA-Inference`、`DEFLECT`、`Realtime-VLA FLASH`、`Fast-dDrive`、`ActQuant`、`Omega-QVLA`、`ElegantVLA`、`Flash-WAM`、`OmniDreams`、`vla.cpp`、`Mix-QVLA` 与 `MemoryWAM` 进一步把 placement、network、jitter、serving throughput、stale-action robustness、memory footprint、control frequency、per-chunk WAM latency、persistent memory 与 world-model serving 拉进效率讨论，说明“效率”已经不是纯模型层指标。
- `VisualThink-VLA`、`AdaWAM`、`BLUE` 与 `AVA-VLA` 进一步说明 reasoning overhead 也需要进入效率定义：不仅要问是否推理，还要问用 textual / visual / latent / WAM substrate 推理、是否按上下文触发或早停、以及延迟和任务收益如何配对。
- `training-free-vs-no-retraining` 与 `model-agnostic-vs-validated-compatibility` 两个 wording evidence 页共同表明，强措辞必须回到已验证范围，不能再用作松散宣传语。

## Theme Structure
- 总纲 / 入口页：[[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]
- 子主题页：
  - [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
  - [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
  - [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
  - [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- 阅读顺序默认是：先在本页固定“效率”到底比较什么、哪些口径不能混写，再进入各子主题页。

## Route Split
- `runtime-vs-task-performance disentanglement`
  - 代表：[[wiki/papers/2409_12514_TinyVLA.md|TinyVLA]]、[[wiki/papers/2410_05273_HiRT.md|HiRT]]、[[wiki/papers/2505_21200_FlashVLA.md|FlashVLA]]、[[wiki/papers/2506_10100_EfficientVLA.md|EfficientVLA]]、[[wiki/papers/2605_29662_SAFE-Pruner.md|SAFE-Pruner]]、[[wiki/papers/2606_05737_One-Step-VLA.md|One-Step VLA]]
  - 作用：把“更快”和“更强”从单一句子中拆开，要求回到 paired operating point；token pruning speedup 与 one-step action generation 也必须带着 success / horizon / schedule 条件阅读。
- `training-cost disentanglement`
  - 代表：[[wiki/papers/2501_09747_FAST.md|FAST]]、[[wiki/papers/2511_16233_FT-NCFM.md|FT-NCFM]]、[[wiki/papers/2604_23073_RLT.md|RLT]]、[[wiki/papers/2605_02757_Efficient-Video-Transfer.md|Efficient Video Transfer]]、[[wiki/papers/2605_06175_VLA-GSE.md|VLA-GSE]]、[[wiki/papers/2605_13276_D-VLA.md|D-VLA]]、[[wiki/papers/2605_13757_FrameSkip.md|FrameSkip]]、[[wiki/papers/2605_16154_PCM.md|PCM]]、[[wiki/papers/2605_16241_VLA-AD.md|VLA-AD]]、[[wiki/papers/2605_22896_Agentic-VLA.md|Agentic-VLA]]、[[wiki/papers/2605_25477_EXPO-FT.md|EXPO-FT]]、[[wiki/papers/2606_04968_ForesightFlow.md|ForesightFlow]]、[[wiki/papers/2606_11187_Next-Forcing.md|Next Forcing]]、[[wiki/papers/2606_14010_RT-VLA.md|RT-VLA]]、[[wiki/papers/2606_20246_CLP.md|CLP]]
  - 作用：把训练时长、GPU 小时、数据比例、在线适配样本效率、真实机器人在线数据、数据增强成本、可训练参数比例、critic 参数、训练系统吞吐、梯度计算预算与推理速度分层阅读。
- `reasoning-overhead disentanglement`
  - 代表：[[wiki/papers/2605_30011_VisualThink-VLA.md|VisualThink-VLA]]、[[wiki/papers/2606_07089_AdaWAM.md|AdaWAM]]、[[wiki/papers/2606_08684_BLUE.md|BLUE]]、[[wiki/papers/2606_15099_AVA-VLA.md|AVA-VLA]]
  - 作用：把 reasoning substrate、routing / gating / early-exit policy、latency and task benefit 拆开，避免把“会思考”写成无成本收益。
- `deployment-as-first-class-efficiency`
  - 代表：[[wiki/papers/2602_18397_VLA-Perf.md|VLA-Perf]]、[[wiki/papers/2604_24086_AsyncShield.md|AsyncShield]]、[[wiki/papers/2604_24447_DP-Cache-V-AEFusion.md|DP-Cache / V-AEFusion]]、[[wiki/papers/2604_27476_EdgeFM.md|EdgeFM]]、[[wiki/papers/2605_08168_Async-VLA-Inference.md|Async-VLA-Inference]]、[[wiki/papers/2605_13778_Realtime-VLA-FLASH.md|Realtime-VLA FLASH]]、[[wiki/papers/2605_19294_DEFLECT.md|DEFLECT]]、[[wiki/papers/2605_23163_Fast-dDrive.md|Fast-dDrive]]、[[wiki/papers/2605_24011_ActQuant.md|ActQuant]]、[[wiki/papers/2605_28803_QVLA-Omega-QVLA.md|Omega-QVLA]]、[[wiki/papers/2605_29438_ElegantVLA.md|ElegantVLA]]、[[wiki/papers/2606_03159_OmniDreams.md|OmniDreams]]、[[wiki/papers/2606_05254_Flash-WAM.md|Flash-WAM]]、[[wiki/papers/2606_08094_vla.cpp.md|vla.cpp]]、[[wiki/papers/2606_19565_Mix-QVLA.md|Mix-QVLA]]、[[wiki/papers/2606_20562_MemoryWAM.md|MemoryWAM]]
  - 作用：把 placement、jitter、memory ceiling、hardware cost/energy、runtime framework、edge/cloud network constraint、delay robustness、structured-output serving、low-bit runtime、persistent memory、WAM per-chunk latency 与 world-model serving 收编为效率定义本身，而不是附属系统注。
- `wording-boundary policing`
  - 代表：[[wiki/evidence/wording/training-free-vs-no-retraining.md|training-free-vs-no-retraining]]、[[wiki/evidence/wording/model-agnostic-vs-validated-compatibility.md|model-agnostic-vs-validated-compatibility]]
  - 作用：要求强措辞总是带着已验证 scope 出现。

## Boundary Conditions
- [[wiki/papers/2409_12514_TinyVLA.md|TinyVLA]] 中的 `25.7%` 单臂收益、双臂成功率与 `20x` 延迟优势不在同一比较层，必须分别回到各自 benchmark 与 latency setting。
- [[wiki/papers/2410_05273_HiRT.md|HiRT]] 中的 `Hz`、`task completion time` 与 `dynamic success rate` 不能合成一条“更快更强”的统一 headline。
- [[wiki/papers/2511_16233_FT-NCFM.md|FT-NCFM]] 的 `GPU hours / data ratio` 只说明训练成本边界，不能与 inference latency 或 online frequency 直接并表。
- [[wiki/papers/2602_18397_VLA-Perf.md|VLA-Perf]] 讨论的是系统 placement 与 latency landscape；这类分析只能和 deployment/system design 论文同层比较，不能直接替代 task-performance 提升。
- `training-free`、`model-agnostic` 这类表述只有在 evidence 页所列 backbone / benchmark / validation scope 下才成立。

## Not Directly Comparable
- 只给单一 latency headline、没有 paired task-performance setting 的论文，不能直接和 operating-point 受控论文比较。
- 只降低训练成本、没有 inference claim 的论文，不能直接和推理提速论文比较。
- 只讨论 reasoning gain 或 deployment trick、但没有显式重写效率定义的论文，只能提供边界说明，不能进入本主题主比较。

## Evidence Links
- [[wiki/evidence/metrics/runtime-vs-task-metrics.md|runtime-vs-task-metrics]]
- [[wiki/evidence/metrics/training-cost-vs-performance.md|training-cost-vs-performance]]
- [[wiki/evidence/metrics/retention-ratio-vs-speed-performance.md|retention-ratio-vs-speed-performance]]
- [[wiki/evidence/wording/training-free-vs-no-retraining.md|training-free-vs-no-retraining]]
- [[wiki/evidence/wording/model-agnostic-vs-validated-compatibility.md|model-agnostic-vs-validated-compatibility]]
- [[wiki/papers/2409_12514_TinyVLA.md|TinyVLA]]
- [[wiki/papers/2410_05273_HiRT.md|HiRT]]
- [[wiki/papers/2501_09747_FAST.md|FAST]]
- [[wiki/papers/2505_21200_FlashVLA.md|FlashVLA]]
- [[wiki/papers/2506_10100_EfficientVLA.md|EfficientVLA]]
- [[wiki/papers/2511_16233_FT-NCFM.md|FT-NCFM]]
- [[wiki/papers/2602_18397_VLA-Perf.md|VLA-Perf]]
- [[wiki/papers/2604_23073_RLT.md|RLT]]
- [[wiki/papers/2604_24086_AsyncShield.md|AsyncShield]]
- [[wiki/papers/2604_24447_DP-Cache-V-AEFusion.md|DP-Cache / V-AEFusion]]
- [[wiki/papers/2604_27476_EdgeFM.md|EdgeFM]]
- [[wiki/papers/2605_02757_Efficient-Video-Transfer.md|Efficient Video Transfer]]
- [[wiki/papers/2605_06175_VLA-GSE.md|VLA-GSE]]
- [[wiki/papers/2605_08168_Async-VLA-Inference.md|Async-VLA-Inference]]
- [[wiki/papers/2605_13276_D-VLA.md|D-VLA]]
- [[wiki/papers/2605_13757_FrameSkip.md|FrameSkip]]
- [[wiki/papers/2605_13778_Realtime-VLA-FLASH.md|Realtime-VLA FLASH]]
- [[wiki/papers/2605_16154_PCM.md|PCM]]
- [[wiki/papers/2605_16241_VLA-AD.md|VLA-AD]]
- [[wiki/papers/2605_19294_DEFLECT.md|DEFLECT]]
- [[wiki/papers/2605_22896_Agentic-VLA.md|Agentic-VLA]]
- [[wiki/papers/2605_23163_Fast-dDrive.md|Fast-dDrive]]
- [[wiki/papers/2605_24011_ActQuant.md|ActQuant]]
- [[wiki/papers/2605_25477_EXPO-FT.md|EXPO-FT]]
- [[wiki/papers/2605_28803_QVLA-Omega-QVLA.md|Omega-QVLA]]
- [[wiki/papers/2605_29438_ElegantVLA.md|ElegantVLA]]
- [[wiki/papers/2605_29662_SAFE-Pruner.md|SAFE-Pruner]]
- [[wiki/papers/2605_30011_VisualThink-VLA.md|VisualThink-VLA]]
- [[wiki/papers/2606_03159_OmniDreams.md|OmniDreams]]
- [[wiki/papers/2606_04968_ForesightFlow.md|ForesightFlow]]
- [[wiki/papers/2606_05254_Flash-WAM.md|Flash-WAM]]
- [[wiki/papers/2606_05737_One-Step-VLA.md|One-Step VLA]]
- [[wiki/papers/2606_07089_AdaWAM.md|AdaWAM]]
- [[wiki/papers/2606_06491_TempoVLA.md|TempoVLA]]
- [[wiki/papers/2606_07895_TBD-VLA.md|TBD-VLA]]
- [[wiki/papers/2606_08094_vla.cpp.md|vla.cpp]]
- [[wiki/papers/2606_08242_Light-WAM.md|Light-WAM]]
- [[wiki/papers/2606_08684_BLUE.md|BLUE]]
- [[wiki/papers/2606_08962_Cache.md|C³ache]]
- [[wiki/papers/2606_09811_AHA-WAM.md|AHA-WAM]]
- [[wiki/papers/2606_10040_Efficient-WAM-Efficient-WAM-RT.md|Efficient-WAM]]
- [[wiki/papers/2606_11187_Next-Forcing.md|Next Forcing]]
- [[wiki/papers/2606_12105_DAM-VLA.md|DAM-VLA]]
- [[wiki/papers/2606_14010_RT-VLA.md|RT-VLA]]
- [[wiki/papers/2606_14048_WAM4D.md|WAM4D]]
- [[wiki/papers/2606_14255_ReactVLA.md|ReactVLA]]
- [[wiki/papers/2606_15099_AVA-VLA.md|AVA-VLA]]
- [[wiki/papers/2606_15768_LaWAM.md|LaWAM]]
- [[wiki/papers/2606_19531_ImageWAM.md|ImageWAM]]
- [[wiki/papers/2606_19565_Mix-QVLA.md|Mix-QVLA]]
- [[wiki/papers/2606_20246_CLP.md|CLP]]
- [[wiki/papers/2606_20562_MemoryWAM.md|MemoryWAM]]

## Open Questions
- 当前还缺少一页把 `memory footprint`、`energy` 与 `network transport` 进一步并入统一效率定义；这不阻塞当前主题页，但会影响后续 deployment-oriented synthesis 的细化。
- 多数论文仍把 wording boundary 写在局部实验设置里，而不是方法声明中；后续仍需持续收紧。

## Gate Check
- `required_sections_complete: yes`
- `evidence_links_present: yes`
- `unscoped_comparative_claims: 0`
- `boundary_conditions_present: yes`
