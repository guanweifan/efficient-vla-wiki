# efficient-vla-research-map

## Question
- 如果从第一性原理出发，把 efficient VLA 看成“在 embodied control 中以更低总代价保留足够能力”的研究议程，当前语料可以稳定分成哪些主路线，它们之间如何衔接成一张研究地图？

## Shared Ground
- 当前页是 [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]] 的配套 survey / map 页面；它不重写已有 `inference / training / reasoning / deployment` 子主题页，而是把这些主题和当前语料里高频出现的 `model-and-representation efficiency` 一起收束成一张更适合综述写作的总地图。
- 从第一性原理看，efficient VLA 的核心问题不是“模型能不能更快”这么单一，而是：在真实 embodied loop 里，总代价可以同时卡在 `模型/表示`、`训练/适配`、`单步推理`、`reasoning overhead`、`系统部署` 五层。
- 因此，当前语料里最稳的组织方式不是按 `manipulation / driving / navigation` 划大类，也不是按 `pruning / quantization / Mamba` 这类局部技巧划大类，而是按“作者把哪一层代价当成主战场”来分。
- 当前页据此把 efficient VLA 收束成 `3` 个宏观家族、`5` 条主路线：
  - `供给侧效率`：`model-and-representation efficiency`、`training-and-adaptation efficiency`
  - `运行时效率`：`inference-time compute allocation`、`reasoning efficiency`
  - `落地侧效率`：`deployment-oriented efficiency`
- 当前稳定共识是：一个成熟的 efficient VLA 工作通常不会只落在单一点上，而是至少会把其中两层串起来；但分类时仍应按其**首要瓶颈**与**主 headline 所服务的问题**来定位。

## Theme Structure
- 结构角色：survey / research map companion page。
- 总纲页：[[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]
- 已有子主题页：
  - [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
  - [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
  - [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
  - [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- 当前页新增的稳定 survey 视角：
  - `model-and-representation efficiency`
  - 作用：把 `TinyVLA / SmolVLA / EdgeVLA / RoboMamba / FAST / ActionCodec / QuantVLA` 这类“先改 policy substrate 本身”的工作，从既有四页之间抽出来，作为 efficient VLA 的底层路线来理解。

## Route Split
- `model-and-representation efficiency`
  - 核心问题：如何让 VLA 的 policy substrate 自身更小、更稀、更易量化或更信息高效，而不是先接受一个昂贵底座再事后加速。
  - 代表性小类：
    - `compact backbone / small VLA design`：[[wiki/papers/2409_12514_TinyVLA.md|TinyVLA]]、[[wiki/papers/2506_01844_SmolVLA.md|SmolVLA]]、[[wiki/papers/2507_14049_EdgeVLA.md|EdgeVLA]]
    - `action representation / tokenizer / codec`：[[wiki/papers/2501_09747_FAST.md|FAST]]、[[wiki/papers/2602_15397_ActionCodec.md|ActionCodec]]
    - `efficient architecture replacement`：[[wiki/papers/2406_04339_RoboMamba.md|RoboMamba]]、[[wiki/papers/2603_01700_TacMamba.md|TacMamba]]
    - `low-bit / quantized substrate`：[[wiki/papers/2602_20309_QuantVLA.md|QuantVLA]]、[[wiki/papers/2506_07530_BitVLA.md|BitVLA]]、[[wiki/papers/2602_03782_QVLA.md|QVLA]]
- `training-and-adaptation efficiency`
  - 核心问题：如何更便宜地获得一个可用的 VLA，而不是只在部署时才追求省算力。
  - 代表性小类：
    - `tokenization-driven training efficiency`：[[wiki/papers/2501_09747_FAST.md|FAST]]
    - `teacher / action-expert distillation`：[[wiki/papers/2510_09607_VITA-VLA.md|VITA-VLA]]、[[wiki/papers/2511_18082_ActDistill.md|ActDistill]]
    - `data-centric efficiency`：[[wiki/papers/2511_16233_FT-NCFM.md|FT-NCFM]]
    - `train-to-infer bridge`：[[wiki/papers/2603_25661_Fast-dVLA.md|Fast-dVLA]]
- `inference-time compute allocation`
  - 核心问题：当底座固定后，如何只在真正必要的位置花计算，把单步控制成本降下来。
  - 代表性小类：
    - `cache-and-reuse`：[[wiki/papers/2502_02175_VLA-Cache.md|VLA-Cache]]
    - `pruning-and-selection`：[[wiki/papers/2505_21200_FlashVLA.md|FlashVLA]]、[[wiki/papers/2509_05614_SpecPrune-VLA.md|SpecPrune-VLA]]、[[wiki/papers/2511_16449_VLA-Pruner.md|VLA-Pruner]]、[[wiki/papers/2603_22991_VLA-IAP.md|VLA-IAP]]、[[wiki/papers/2603_25766_ETA-VLA.md|ETA-VLA]]、[[wiki/papers/2604_05323_VLA-InfoEntropy.md|VLA-InfoEntropy]]、[[wiki/papers/2604_09244_Tri-Stage-Token-Pruning-Framework.md|Tri-Stage Token Pruning Framework]]
    - `sampling / decoding compression`：[[wiki/papers/2603_25661_Fast-dVLA.md|Fast-dVLA]]、[[wiki/papers/2604_05656_SnapFlow.md|SnapFlow]]、[[wiki/papers/2604_01567_AnchorVLA.md|AnchorVLA]]、[[wiki/papers/2604_05672_A1.md|A1]]
    - `async / streaming / chunk scheduling`：[[wiki/papers/2511_14148_AsyncVLA.md|AsyncVLA]]、[[wiki/papers/2602_01100_StreamVLA.md|StreamVLA]]、[[wiki/papers/2603_28565_StreamingVLA.md|StreamingVLA]]、[[wiki/papers/2604_04161_AAC.md|AAC]]
- `reasoning efficiency`
  - 核心问题：如何保留 planning、few-shot adaptation、self-correction 这些 reasoning 收益，同时摆脱 always-on explicit CoT 的高延迟。
  - 代表性小类：
    - `explicit reasoning cost compression`：[[wiki/papers/2505_08243_ECoT-Lite.md|ECoT-Lite]]
    - `dual-system reasoning-action split`：[[wiki/papers/2507_16815_ThinkAct.md|ThinkAct]]
    - `latent planning / verbalizable latent reasoning`：[[wiki/papers/2601_09708_Fast-ThinkAct.md|Fast-ThinkAct]]、[[wiki/papers/2602_01166_LaRA-VLA.md|LaRA-VLA]]
    - `gated / routed reasoning`：[[wiki/papers/2602_01100_StreamVLA.md|StreamVLA]]、[[wiki/papers/2603_05147_ActThinkAbstain.md|ActThinkAbstain]]
- `deployment-oriented efficiency`
  - 核心问题：如何让前述效率收益在真实硬件、网络、控制周期与 jitter 约束下仍然成立，而不是只停留在 benchmark latency。
  - 代表性小类：
    - `edge-native VLA design`：[[wiki/papers/2507_14049_EdgeVLA.md|EdgeVLA]]、[[wiki/papers/2603_03380_LiteVLA-Edge.md|LiteVLA-Edge]]、[[wiki/papers/2506_01844_SmolVLA.md|SmolVLA]]
    - `representation-for-throughput`：[[wiki/papers/2507_05116_VOTE.md|VOTE]]
    - `system throughput tuning`：[[wiki/papers/2603_26360_Realtime-VLA-V2.md|Realtime-VLA V2]]
    - `async control / chunk scheduling / real-time serving`：[[wiki/papers/2512_03044_Video2Act.md|Video2Act]]、[[wiki/papers/2603_19199_FASTER.md|FASTER]]
    - `system / placement / network analysis`：[[wiki/papers/2602_18397_VLA-Perf.md|VLA-Perf]]

## Boundary Conditions
- 分类时默认问的是：**这篇论文主要在压哪一层成本**。如果一篇论文同时涉及多层，应按其 headline 与问题设定所服务的首要瓶颈来定位，而不是把所有技术元素都升格成主类。
- `tokenization`、`quantization`、`async` 这类路线天然跨层：
  - `tokenization` 既可能属于 `model-and-representation efficiency`，也可能属于 `training-and-adaptation efficiency`；
  - `quantization` 既可能属于 `model-and-representation efficiency`，也可能服务 `deployment-oriented efficiency`；
  - `async / streaming` 既可能是 `inference-time compute allocation`，也可能是 `deployment-oriented efficiency` 的 system trick。
- `manipulation / driving / navigation` 更适合视为应用场景，而不是 efficient VLA 的顶层 taxonomy；当前多域论文更像是在不同场景里实例化同一批效率路线。
- 若一篇论文只提升 task performance、但没有把效率问题写成主问题，或没有明确的成本口径，则不应强行纳入 efficient VLA 主地图。

## Not Directly Comparable
- `模型更小 / 内存更省`、`训练更便宜`、`推理更快`、`thinking overhead 更低`、`控制频率更高` 分属不同效率层，不能压成统一 superiority claim。
- 低比特 PTQ、token pruning、latent reasoning、edge deployment 都可能让系统“更高效”，但它们回答的是不同层的问题，不宜直接排成单一优劣顺序。
- 以 driving / navigation 为主场景的论文，可以帮助暴露路线边界，但不应自动和 manipulation 主线的 operating point 混写。

## Evidence Links
- [[wiki/evidence/metrics/runtime-vs-task-metrics.md|runtime-vs-task-metrics]]
- [[wiki/evidence/metrics/training-cost-vs-performance.md|training-cost-vs-performance]]
- [[wiki/evidence/metrics/retention-ratio-vs-speed-performance.md|retention-ratio-vs-speed-performance]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/papers/2409_12514_TinyVLA.md|TinyVLA]]
- [[wiki/papers/2501_09747_FAST.md|FAST]]
- [[wiki/papers/2502_02175_VLA-Cache.md|VLA-Cache]]
- [[wiki/papers/2505_08243_ECoT-Lite.md|ECoT-Lite]]
- [[wiki/papers/2505_21200_FlashVLA.md|FlashVLA]]
- [[wiki/papers/2506_01844_SmolVLA.md|SmolVLA]]
- [[wiki/papers/2506_07530_BitVLA.md|BitVLA]]
- [[wiki/papers/2507_14049_EdgeVLA.md|EdgeVLA]]
- [[wiki/papers/2507_05116_VOTE.md|VOTE]]
- [[wiki/papers/2507_16815_ThinkAct.md|ThinkAct]]
- [[wiki/papers/2509_05614_SpecPrune-VLA.md|SpecPrune-VLA]]
- [[wiki/papers/2510_09607_VITA-VLA.md|VITA-VLA]]
- [[wiki/papers/2511_14148_AsyncVLA.md|AsyncVLA]]
- [[wiki/papers/2511_16233_FT-NCFM.md|FT-NCFM]]
- [[wiki/papers/2511_16449_VLA-Pruner.md|VLA-Pruner]]
- [[wiki/papers/2511_18082_ActDistill.md|ActDistill]]
- [[wiki/papers/2512_03044_Video2Act.md|Video2Act]]
- [[wiki/papers/2601_09708_Fast-ThinkAct.md|Fast-ThinkAct]]
- [[wiki/papers/2602_01100_StreamVLA.md|StreamVLA]]
- [[wiki/papers/2602_01166_LaRA-VLA.md|LaRA-VLA]]
- [[wiki/papers/2602_15397_ActionCodec.md|ActionCodec]]
- [[wiki/papers/2602_18397_VLA-Perf.md|VLA-Perf]]
- [[wiki/papers/2602_20309_QuantVLA.md|QuantVLA]]
- [[wiki/papers/2602_03782_QVLA.md|QVLA]]
- [[wiki/papers/2603_01700_TacMamba.md|TacMamba]]
- [[wiki/papers/2603_03380_LiteVLA-Edge.md|LiteVLA-Edge]]
- [[wiki/papers/2603_05147_ActThinkAbstain.md|ActThinkAbstain]]
- [[wiki/papers/2603_19199_FASTER.md|FASTER]]
- [[wiki/papers/2603_22991_VLA-IAP.md|VLA-IAP]]
- [[wiki/papers/2603_25766_ETA-VLA.md|ETA-VLA]]
- [[wiki/papers/2603_26360_Realtime-VLA-V2.md|Realtime-VLA V2]]
- [[wiki/papers/2603_28565_StreamingVLA.md|StreamingVLA]]
- [[wiki/papers/2406_04339_RoboMamba.md|RoboMamba]]
- [[wiki/papers/2603_25661_Fast-dVLA.md|Fast-dVLA]]
- [[wiki/papers/2604_01567_AnchorVLA.md|AnchorVLA]]
- [[wiki/papers/2604_04161_AAC.md|AAC]]
- [[wiki/papers/2604_05323_VLA-InfoEntropy.md|VLA-InfoEntropy]]
- [[wiki/papers/2604_05656_SnapFlow.md|SnapFlow]]
- [[wiki/papers/2604_05672_A1.md|A1]]
- [[wiki/papers/2604_09244_Tri-Stage-Token-Pruning-Framework.md|Tri-Stage Token Pruning Framework]]

## Open Questions
- `model-and-representation efficiency` 当前已经足够稳定到能作为 survey 主路线，但仓库里还缺一页专门承接它的独立子主题页；当前先由本页兼任总地图入口。
- 多数论文仍然分别优化 `model size / training cost / runtime / deployment` 中的一层，真正同时显式建模五层 tradeoff 的工作仍少。
- `energy`、`memory ceiling`、`jitter` 与 `closed-loop failure mode` 还没有被统一纳入一套跨论文通用的 efficiency language。

## Gate Check
- `required_sections_complete: yes`
- `evidence_links_present: yes`
- `unscoped_comparative_claims: 0`
- `boundary_conditions_present: yes`
