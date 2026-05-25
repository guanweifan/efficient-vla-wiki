# inference-efficiency-routes

## Question
- 推理期高效 VLA 如何从局部 token/cache 复用，演化到 pruning、caching、speculative / parallel decoding、async / streaming control 这些更广的 compute-allocation 路线？

## Shared Ground
- 本页是 [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]] 之下的子主题页；它承接总纲页已经固定好的效率定义，不单独重写“效率”总概念。
- 当前主题的固定比较轴是：
  - 冗余来源：`token / cache / action chunk / language layer / diffusion timestep / block schedule`
  - 控制面：`semantic saliency / action-aware / interaction-aware / gated execution / streaming trigger`
  - 代价口径：`latency / speedup / FLOPs / frequency / skip ratio`
  - 适用边界：`training-free` vs `requires adaptation`，以及 `single-family validation` vs `broader validated scope`
- `VLA-Cache`、`FlashVLA`、`EfficientVLA`、`SpecPrune-VLA`、`VLA-Pruner`、`VLA-IAP`、`ETA-VLA`、`VLA-InfoEntropy`、`GridS`、`AsyncVLA`、`StreamVLA`、`StreamingVLA`、`Fast-dVLA`、`SnapFlow`、`AnchorVLA`、`A1`、`SpanVLA`、`CF-VLA`、`DP-Cache / V-AEFusion`、`BlockVLA`、`Realtime-VLA FLASH`、`DEFLECT`、`Fast-dDrive`、`AsyncShield` 共同表明，推理效率的核心是 inference-time compute allocation，而不是训练阶段成本。
- 这些工作都不是单纯追求“更高 speedup”，而是在不同冗余来源和不同控制面上重新分配计算预算。
- 共享 evidence 页已经稳定支持两个共识：
  - runtime headline 必须和 task 或 operating point 口径一起阅读；
  - retention / pruning ratio 只有在与性能保持条件绑定时才有解释力。
- 在 `pruning-and-selection` 子线上，更稳的内部演化不是继续追单一 keep ratio，而是从 `semantic-only / perception-first saliency` 逐步转向 `action-aware / phase-aware / interaction-aware / view-sensitive` 的 compute allocation。

## Theme Structure
- 结构角色：inference 路线子主题页。
- 总纲页：[[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]
- 相邻但不等价的子主题：
  - [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
  - [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
- 本页只处理 inference-time compute allocation 路线，不承担训练成本、总定义或部署总纲。

## Route Split
- `cache-and-reuse`
  - 代表：[[wiki/papers/2502_02175_VLA-Cache.md|VLA-Cache]]
  - 依据：通过 temporal 或 latent reuse 回收已有计算，而不是直接丢弃 token。
- `pruning-and-selection`
  - 代表：[[wiki/papers/2509_05614_SpecPrune-VLA.md|SpecPrune-VLA]]、[[wiki/papers/2511_16449_VLA-Pruner.md|VLA-Pruner]]、[[wiki/papers/2603_22991_VLA-IAP.md|VLA-IAP]]、[[wiki/papers/2603_25766_ETA-VLA.md|ETA-VLA]]、[[wiki/papers/2604_05323_VLA-InfoEntropy.md|VLA-InfoEntropy]]、[[wiki/papers/2604_09244_Tri-Stage-Token-Pruning-Framework.md|Tri-Stage Token Pruning Framework]]、[[wiki/papers/2605_07931_OneWM-VLA.md|OneWM-VLA]]、[[wiki/papers/2605_11817_GridS.md|GridS]]
  - 依据：通过 semantic / action / interaction-aware 规则选择性保留 token、模态或路径；其中新近工作已经开始显式处理 temporal compression、2D/3D modality salience、world-module per-frame visual bandwidth，以及 differentiable coordinate-based visual resampling。
- `sampling-or-decoding compression`
  - 代表：[[wiki/papers/2603_25661_Fast-dVLA.md|Fast-dVLA]]、[[wiki/papers/2604_05656_SnapFlow.md|SnapFlow]]、[[wiki/papers/2604_01567_AnchorVLA.md|AnchorVLA]]、[[wiki/papers/2604_05672_A1.md|A1]]、[[wiki/papers/2604_19710_SpanVLA.md|SpanVLA]]、[[wiki/papers/2604_19730_FASTER.md|FASTER (value-guided sampling)]]、[[wiki/papers/2604_24622_CF-VLA.md|CF-VLA]]、[[wiki/papers/2604_24447_DP-Cache-V-AEFusion.md|DP-Cache / V-AEFusion]]、[[wiki/papers/2605_13382_BlockVLA.md|BlockVLA]]、[[wiki/papers/2605_13778_Realtime-VLA-FLASH.md|Realtime-VLA FLASH]]、[[wiki/papers/2605_23163_Fast-dDrive.md|Fast-dDrive]]
  - 依据：通过 block-wise diffusion、single-step generation、anchored truncated diffusion、warm-start denoising、action bridge + flow-matching expert、coarse-to-fine low-NFE generation、diffusion-step caching、speculative draft-verify-fallback，或 structured-output block diffusion 压缩 action decoding / sampling 开销；其中 [[wiki/papers/2604_19730_FASTER.md|FASTER (value-guided sampling)]] 目前只作为 VLA-adjacent reference。
- `async-or-streaming-control`
  - 代表：[[wiki/papers/2511_14148_AsyncVLA.md|AsyncVLA]]、[[wiki/papers/2602_01100_StreamVLA.md|StreamVLA]]、[[wiki/papers/2603_28565_StreamingVLA.md|StreamingVLA]]、[[wiki/papers/2604_04161_AAC.md|AAC]]、[[wiki/papers/2604_24086_AsyncShield.md|AsyncShield]]、[[wiki/papers/2605_08168_Async-VLA-Inference.md|Async-VLA-Inference]]、[[wiki/papers/2605_19294_DEFLECT.md|DEFLECT]]
  - 依据：通过 asynchronous regeneration、completion-state gating、streaming overlap、adaptive chunk scheduling、cloud-edge latency realignment、delay-robust method evaluation 或 offline stale-action preference tuning 让 compute allocation 服从控制节奏。

## Boundary Conditions
- `training-free` 只能在 evidence 页列出的具体方法与验证范围内成立；需要 adaptation 的方法不能被混入同一 headline。
- `speedup / latency reduction` 只有在明确对应冗余来源与控制面时才可比较；单纯列 speedup 数值不足以建立路线关系。
- `retention ratio` 或 `skip ratio` 必须和性能保持条件一起阅读；否则 pruning/selection 路线之间不可直接比较。
- `frequency` 或 `real-time` 结果只有在明确系统 placement、执行循环与 control setting 时才可与 async/streaming 路线比较。
- action chunk scheduling、single-step flow generation、truncated diffusion 都在压推理期成本，但它们作用的对象分别是 control cadence、sampling steps 与 denoising horizon，不能直接混成同一路径 superiority claim。
- action bridge + flow matching 与 value-guided candidate filtering 都属于 action-generation cost compression，但前者是 driving VLA action head 设计，后者是 general diffusion-policy / RL sampling acceleration；比较时必须保留 VLA-specific 与 VLA-adjacent 边界。
- coarse-to-fine low-NFE generation、diffusion-step caching 与 pipeline overlap 都压 action-expert 相关成本，但分别作用于 starting point、denoising redundancy 与 VLM/action-expert serialization。
- world-module visual bandwidth compression 只在 auxiliary rollout / latent world token 设定中成立；不能直接并入 policy perception token pruning 的 keep-ratio 比较。
- `semantic-only pruning`、`action-aware dynamic pruning`、`interaction-first pruning` 与 `multi-view hierarchical pruning` 虽同属 pruning-and-selection，但依赖的控制信号与适用 setting 不同，不能只按 keep ratio 或 speedup 压成单一优劣序列。
- differentiable coordinate resampling、hard token pruning 与 world-module latent compression 同属 visual bandwidth 问题，但采样对象、控制信号和可解释的 retention 口径不同。
- block diffusion、speculative inference、offline delay-robust tuning 与 structured driving output serving 都可降低 action-side 推理成本，但分别作用于 diffusion block、draft verification、stale action preference 和 JSON-like trajectory output。
- async 方法评测框架与新的 runtime 加速机制不等价；[[wiki/papers/2605_08168_Async-VLA-Inference.md|Async-VLA-Inference]] 更适合作为 delay robustness 对照锚点。
- [[wiki/papers/2605_09948_LoopVLA.md|LoopVLA]] 的 throughput 收益来自 policy substrate 内部的 recurrent / sufficiency-guided dynamic computation；它可作为 inference compute allocation 的边界例子，但不应和外部 scheduler 或 pruning route 混写。

## Not Directly Comparable
- 训练侧效率工作如 [[wiki/papers/2501_09747_FAST.md|FAST]]、[[wiki/papers/2511_16233_FT-NCFM.md|FT-NCFM]] 不能进入本主题主比较。
- 纯部署分析如 [[wiki/papers/2602_18397_VLA-Perf.md|VLA-Perf]] 只能提供边界说明，不能直接与 inference-time compute-allocation 路线比较。
- 只给单一 speedup、未说明 redundancy source 或控制面的 headline，只能算边缘例子，不能参与 route-level 比较。

## Evidence Links
- [[wiki/evidence/metrics/runtime-vs-task-metrics.md|runtime-vs-task-metrics]]
- [[wiki/evidence/metrics/retention-ratio-vs-speed-performance.md|retention-ratio-vs-speed-performance]]
- [[wiki/evidence/wording/semantic-only-vs-embodiment-aware-pruning.md|semantic-only-vs-embodiment-aware-pruning]]
- [[wiki/evidence/wording/training-free-vs-no-retraining.md|training-free-vs-no-retraining]]
- [[wiki/papers/2501_09747_FAST.md|FAST]]
- [[wiki/papers/2502_02175_VLA-Cache.md|VLA-Cache]]
- [[wiki/papers/2505_21200_FlashVLA.md|FlashVLA]]
- [[wiki/papers/2506_10100_EfficientVLA.md|EfficientVLA]]
- [[wiki/papers/2509_05614_SpecPrune-VLA.md|SpecPrune-VLA]]
- [[wiki/papers/2511_16233_FT-NCFM.md|FT-NCFM]]
- [[wiki/papers/2511_16449_VLA-Pruner.md|VLA-Pruner]]
- [[wiki/papers/2511_14148_AsyncVLA.md|AsyncVLA]]
- [[wiki/papers/2602_01100_StreamVLA.md|StreamVLA]]
- [[wiki/papers/2602_18397_VLA-Perf.md|VLA-Perf]]
- [[wiki/papers/2603_25766_ETA-VLA.md|ETA-VLA]]
- [[wiki/papers/2603_28565_StreamingVLA.md|StreamingVLA]]
- [[wiki/papers/2603_25661_Fast-dVLA.md|Fast-dVLA]]
- [[wiki/papers/2603_22991_VLA-IAP.md|VLA-IAP]]
- [[wiki/papers/2604_01567_AnchorVLA.md|AnchorVLA]]
- [[wiki/papers/2604_04161_AAC.md|AAC]]
- [[wiki/papers/2604_05323_VLA-InfoEntropy.md|VLA-InfoEntropy]]
- [[wiki/papers/2604_05656_SnapFlow.md|SnapFlow]]
- [[wiki/papers/2604_05672_A1.md|A1]]
- [[wiki/papers/2604_09244_Tri-Stage-Token-Pruning-Framework.md|Tri-Stage Token Pruning Framework]]
- [[wiki/papers/2604_19710_SpanVLA.md|SpanVLA]]
- [[wiki/papers/2604_19730_FASTER.md|FASTER (value-guided sampling)]]
- [[wiki/papers/2604_24086_AsyncShield.md|AsyncShield]]
- [[wiki/papers/2604_24447_DP-Cache-V-AEFusion.md|DP-Cache / V-AEFusion]]
- [[wiki/papers/2604_24622_CF-VLA.md|CF-VLA]]
- [[wiki/papers/2605_01194_VLA-ATTC.md|VLA-ATTC]]
- [[wiki/papers/2605_07931_OneWM-VLA.md|OneWM-VLA]]
- [[wiki/papers/2605_08168_Async-VLA-Inference.md|Async-VLA-Inference]]
- [[wiki/papers/2605_09948_LoopVLA.md|LoopVLA]]
- [[wiki/papers/2605_11817_GridS.md|GridS]]
- [[wiki/papers/2605_13382_BlockVLA.md|BlockVLA]]
- [[wiki/papers/2605_13778_Realtime-VLA-FLASH.md|Realtime-VLA FLASH]]
- [[wiki/papers/2605_19294_DEFLECT.md|DEFLECT]]
- [[wiki/papers/2605_23163_Fast-dDrive.md|Fast-dDrive]]

## Open Questions
- 目前 `cache-and-reuse` 与 `sampling-or-decoding compression` 在共享 benchmark 上的直接并比仍然不足，后续建模时需要更谨慎处理“更优路线”这种表述。
- 一些 routing/gating 路线仍把系统频率收益与任务成功率混写，后续 closeout 时还需要持续防止回退。
- 新近一批工作把 action-head sampling 压缩、action bridge、chunk scheduling 与 streaming overlap 推到了相邻问题空间；后续需要继续判断它们是否应在更高层被拆成独立 inference 子路线。

## Gate Check
- `required_sections_complete: yes`
- `evidence_links_present: yes`
- `unscoped_comparative_claims: 0`
- `boundary_conditions_present: yes`
