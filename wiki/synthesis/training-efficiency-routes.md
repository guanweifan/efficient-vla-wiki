# training-efficiency-routes

## Question
- 高效 VLA 如何把“训练侧成本”从附属问题变成独立议程，逐步转向 tokenization、teacher distillation、synthetic coreset 与低成本 adaptation？

## Shared Ground
- 本页是 [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]] 之下的子主题页；它专门处理训练侧成本如何成为独立效率议程。
- 当前主题的固定比较轴是：
  - `training steps / GPU hours / data ratio / adaptation cost`
  - 收益类型：`更快收敛 / 少数据逼近 / cheaper adaptation / 更少 teacher calls`
  - 依赖条件：`teacher / pretrained action expert / synthetic data generator / tokenizer redesign`
  - 与推理侧的关系：`是否伴随 inference tradeoff`
- `FAST`、`VITA-VLA`、`FT-NCFM`、`ActDistill`、`RLT`、`VLA-GSE`、`Efficient Video Transfer`、`D-VLA`、`FrameSkip`、`BlockVLA`、`PCM`、`VLA-AD`、`Agentic-VLA`、`EXPO-FT`、`ForesightFlow`、`Next Forcing`、`RT-VLA`、`CLP`、`FOCA`、`ROAD-VLA`、`FORCE`、`VLM2VLA Parameter Redundancy`、`DTR`、`SIEVE`、`LoRA Fine-Tuning for VLA`、`ExToken`、`CoTinyVLA`、`Enfold` 共同表明，训练效率已经不是 inference efficiency 的附属注脚，而是独立问题。
- 这些工作都把“降低训练代价”写成主收益，但降低代价的方式不同：有的压 token，有的压 teacher/adaptation，有的压 data requirement。
- `Fast-dVLA`、`One-Step VLA` 与 `Flash-WAM` 只作为桥接例子存在：它们说明训练侧技巧可以服务推理路线，但不能因此把训练与推理混成同一主题。

## Theme Structure
- 结构角色：training 路线子主题页。
- 总纲页：[[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]
- 相邻但不等价的子主题：
  - [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
  - [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- 本页不承担 inference-time compute allocation 或 deployment feasibility 的总比较。

## Route Split
- `tokenization-and-compression`
  - 代表：[[wiki/papers/2501_09747_FAST.md|FAST]]
  - 依据：通过 action tokenizer 压低训练步骤与训练成本。
- `teacher-distillation`
  - 代表：[[wiki/papers/2510_09607_VITA-VLA.md|VITA-VLA]]、[[wiki/papers/2511_18082_ActDistill.md|ActDistill]]、[[wiki/papers/2605_16241_VLA-AD.md|VLA-AD]]、[[wiki/papers/2606_14010_RT-VLA.md|RT-VLA]]、[[wiki/papers/2607_25487_CoTinyVLA.md|CoTinyVLA]]、[[wiki/papers/2607_26657_Enfold-Enfold-Flash.md|Enfold]]
  - 依据：通过 teacher/student、action expert、hierarchical CoT supervision、future-processing generator states 或 offline semantic guidance 降低 adaptation 与 supervision 成本；teacher / generator 自身成本需要单独保留。
- `online-RL adaptation interface`
  - 代表：[[wiki/papers/2604_23073_RLT.md|RLT]]、[[wiki/papers/2605_22896_Agentic-VLA.md|Agentic-VLA]]、[[wiki/papers/2605_25477_EXPO-FT.md|EXPO-FT]]、[[wiki/papers/2606_25800_ROAD-VLA.md|ROAD-VLA]]、[[wiki/papers/2606_26006_FORCE.md|FORCE]]、[[wiki/papers/2607_12931_ExToken.md|ExToken]]
  - 依据：通过 compact RL token、轻量 actor-critic、language-guided exploration、experience memory、action-space self-distillation、value-calibrated warm-up，或 human-in-the-loop online RL fine-tuning，把任务特化从 full VLA fine-tuning 转成 sample-efficient online adaptation。
- `parameter-efficient adaptation`
  - 代表：[[wiki/papers/2605_06175_VLA-GSE.md|VLA-GSE]]、[[wiki/papers/2607_10172_LoRA-Fine-Tuning-for-VLA.md|LoRA Fine-Tuning for VLA]]
  - 依据：通过 expert allocation 或 LoRA rank / module allocation 在固定 trainable-parameter budget 下增强 VLM-to-VLA adaptation；静态参数与静态显存不包含 activation memory。
- `data-centric-efficiency`
  - 代表：[[wiki/papers/2511_16233_FT-NCFM.md|FT-NCFM]]、[[wiki/papers/2605_02757_Efficient-Video-Transfer.md|Efficient Video Transfer]]、[[wiki/papers/2605_13757_FrameSkip.md|FrameSkip]]、[[wiki/papers/2606_20867_FOCA.md|FOCA]]、[[wiki/papers/2607_06442_SIEVE.md|SIEVE]]
  - 依据：通过 synthetic coreset / data reduction、高效 sim-to-real video augmentation、frame-level supervision allocation、future-oriented latent supervision，或 structure-aware trajectory selection 降低训练数据构建与数据增强成本。
- `RL-training-system-and-gradient-allocation`
  - 代表：[[wiki/papers/2605_13276_D-VLA.md|D-VLA]]、[[wiki/papers/2605_16154_PCM.md|PCM]]
  - 依据：通过分布式训练流水线或 actor-update gradient chunk masking 降低 embodied RL 训练 wall-clock、吞吐和显存成本。
- `critic-free / mixed-quality policy improvement`
  - 代表：[[wiki/papers/2606_04968_ForesightFlow.md|ForesightFlow]]
  - 依据：通过 self-guided action-potential flow 使用 mixed-quality rollouts，避免 separate critic pipeline，并把 GPU hours、critic parameters 与 best-of-K latency 分层报告。
- `dense future-supervision / pre-finetuning compression`
  - 代表：[[wiki/papers/2606_11187_Next-Forcing.md|Next Forcing]]、[[wiki/papers/2606_20246_CLP.md|CLP]]、[[wiki/papers/2606_27755_DTR-GateProbe.md|DTR / GateProbe]]、[[wiki/papers/2606_31382_VLM2VLA-Parameter-Redundancy.md|VLM2VLA Parameter Redundancy]]
  - 依据：通过 multi-chunk future supervision、fine-tuning 前的结构性 layer pruning、drop-then-recovery sensitivity probing，或 adaptation-divergence-guided parameter pruning 降低 world-model training / adaptation cost；这类路线需要继续区分训练收敛、下游 fine-tuning 时间、参数压缩与部署期 latency。
- `train-to-infer bridge`
  - 代表：[[wiki/papers/2603_25661_Fast-dVLA.md|Fast-dVLA]]、[[wiki/papers/2605_13382_BlockVLA.md|BlockVLA]]、[[wiki/papers/2606_05737_One-Step-VLA.md|One-Step VLA]]、[[wiki/papers/2606_05254_Flash-WAM.md|Flash-WAM]]
  - 依据：训练侧 distillation、schedule design 或 AR-to-diffusion adaptation 被回收进推理效率，但仍不能直接替代训练成本主链。

## Boundary Conditions
- 只要收益主要体现在 inference latency，而不是 `training steps / GPU hours / data ratio / adaptation cost`，就不能进入本主题主比较。
- `teacher-distillation` 方法之间只有在 teacher 依赖、teacher 成本和行为保持目标大致一致时，才有直接比较意义。
- `data-centric` 方法的收益必须回到 data ratio、synthetic set 或 training reduction 设定，不能和 tokenizer 压缩法直接并表为统一“更省”。
- 若一篇论文同时宣称训练更便宜和推理更快，两个收益必须分层写；不能用单一 headline 混写。
- online RL task throughput、video diffusion generation time、trainable-parameter ratio 都是训练/适配侧的不同成本口径，不能直接互相替代。
- Post-training quantization / calibration 只有在论文明确报告 `training steps / GPU hours / data ratio / adaptation cost` 时，才进入训练成本主链；否则更适合放在 low-bit substrate 或 deployment-oriented compression。
- [[wiki/papers/2606_19565_Mix-QVLA.md|Mix-QVLA]] 这类 mixed-precision PTQ 虽按仓库 taxonomy 可归入 compression-oriented training efficiency，但在本页主链中仍需要和真正的 training-cost reduction 分开。
- frame retention、gradient chunk masking、distributed rollout throughput 与 offline VLM semantic supervision 都是训练侧成本控制，但分别作用于数据、梯度、系统流水线和 teacher-student supervision。
- language-guided exploration 如果服务在线训练适配，属于 training efficiency；不能因为使用语言就自动并入 inference-time reasoning efficiency。
- one-step action generation 与 WAM step distillation 如果主要服务推理期 denoising-step reduction，只能作为 `train-to-infer bridge`；不能替代真正的 training-cost evidence。
- mixed-quality policy improvement 要区分 training GPU hours、critic parameters 与 best-of-K inference latency，不能把它们压成单一“更省训练”结论。
- [[wiki/papers/2607_06442_SIEVE.md|SIEVE]] 的 `50% demonstrations / 50% training steps` 结论依赖其选择预算与训练设置；[[wiki/papers/2607_12931_ExToken.md|ExToken]] 的 interaction/sample efficiency 也不能改写成 wall-clock training speedup。
- [[wiki/papers/2607_28405_QuantWAMs.md|QuantWAMs]] 属于 post-training quantization；其 calibration 与 block-level kernel 结果不能作为训练成本下降证据。

## Not Directly Comparable
- 主要目标是 inference latency / deployment 的论文，即使包含 distillation 或 cache，也不能直接与训练效率主链比较。
- [[wiki/papers/2604_11572_DA-PTQ.md|DA-PTQ]] 这类 drift-aware PTQ 属于 post-training compression / calibration；它可以影响部署成本，但不能直接作为 training-cost reduction 证据。
- `Fast-dVLA` 这类桥接工作只能作为边缘例子，不能定义训练效率本身。
- 没有直接训练成本指标的论文，不能进入本主题主比较。

## Evidence Links
- [[wiki/evidence/metrics/training-cost-vs-performance.md|training-cost-vs-performance]]
- [[wiki/papers/2501_09747_FAST.md|FAST]]
- [[wiki/papers/2510_09607_VITA-VLA.md|VITA-VLA]]
- [[wiki/papers/2511_16233_FT-NCFM.md|FT-NCFM]]
- [[wiki/papers/2511_18082_ActDistill.md|ActDistill]]
- [[wiki/papers/2603_25661_Fast-dVLA.md|Fast-dVLA]]
- [[wiki/papers/2604_11572_DA-PTQ.md|DA-PTQ]]
- [[wiki/papers/2604_23073_RLT.md|RLT]]
- [[wiki/papers/2605_02757_Efficient-Video-Transfer.md|Efficient Video Transfer]]
- [[wiki/papers/2605_06175_VLA-GSE.md|VLA-GSE]]
- [[wiki/papers/2605_13276_D-VLA.md|D-VLA]]
- [[wiki/papers/2605_13382_BlockVLA.md|BlockVLA]]
- [[wiki/papers/2605_13757_FrameSkip.md|FrameSkip]]
- [[wiki/papers/2605_16154_PCM.md|PCM]]
- [[wiki/papers/2605_16241_VLA-AD.md|VLA-AD]]
- [[wiki/papers/2605_22896_Agentic-VLA.md|Agentic-VLA]]
- [[wiki/papers/2605_25477_EXPO-FT.md|EXPO-FT]]
- [[wiki/papers/2606_04968_ForesightFlow.md|ForesightFlow]]
- [[wiki/papers/2606_05254_Flash-WAM.md|Flash-WAM]]
- [[wiki/papers/2606_05737_One-Step-VLA.md|One-Step VLA]]
- [[wiki/papers/2606_11187_Next-Forcing.md|Next Forcing]]
- [[wiki/papers/2606_14010_RT-VLA.md|RT-VLA]]
- [[wiki/papers/2606_14048_WAM4D.md|WAM4D]]
- [[wiki/papers/2606_19565_Mix-QVLA.md|Mix-QVLA]]
- [[wiki/papers/2606_20246_CLP.md|CLP]]

- [[wiki/papers/2606_20867_FOCA.md|FOCA]]
- [[wiki/papers/2606_22540_PolicyTrim.md|PolicyTrim]]
- [[wiki/papers/2606_25800_ROAD-VLA.md|ROAD-VLA]]
- [[wiki/papers/2606_26006_FORCE.md|FORCE]]
- [[wiki/papers/2606_27755_DTR-GateProbe.md|DTR / GateProbe]]
- [[wiki/papers/2606_31382_VLM2VLA-Parameter-Redundancy.md|VLM2VLA Parameter Redundancy]]
- [[wiki/papers/2607_06442_SIEVE.md|SIEVE]]
- [[wiki/papers/2607_10172_LoRA-Fine-Tuning-for-VLA.md|LoRA Fine-Tuning for VLA]]
- [[wiki/papers/2607_12931_ExToken.md|ExToken]]
- [[wiki/papers/2607_25487_CoTinyVLA.md|CoTinyVLA]]
- [[wiki/papers/2607_26657_Enfold-Enfold-Flash.md|Enfold]]
- [[wiki/papers/2607_28405_QuantWAMs.md|QuantWAMs]]
## Open Questions
- 当前仍缺少把 `teacher cost` 本身单独量化的统一 evidence 页；这会限制 distillation 路线之间的更细比较。
- 训练侧收益和长期下游泛化之间的关系，仍多依赖单篇论文叙述，后续可能需要更细 evidence 补充。

## Gate Check
- `required_sections_complete: yes`
- `evidence_links_present: yes`
- `unscoped_comparative_claims: 0`
- `boundary_conditions_present: yes`
