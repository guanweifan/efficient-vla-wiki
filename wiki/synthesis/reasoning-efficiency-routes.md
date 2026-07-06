# reasoning-efficiency-routes

## Question
- VLA 如何在保留 reasoning 收益的同时，逐步摆脱显式 CoT 的 latency / control overhead，转向 latent、gated 与 dual-process efficiency 设计？

## Shared Ground
- 本页是 [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]] 之下的子主题页；它只处理 reasoning substrate 与 compute policy 的效率问题。
- 当前主题的固定比较轴是：
  - reasoning substrate：`textual CoT / visual plan / latent thought / completion-state imagination`
  - compute policy：`always-on / compressed / gated / routed`
  - 收益口径：`planning / few-shot adaptation / safety / robustness / latency reduction`
  - 代价口径：`execution overhead / skip ratio / route complexity / teacher or supervision dependence`
- `ECoT-Lite`、`ThinkAct`、`Fast-ThinkAct`、`LaRA-VLA`、`OneVL`、`StreamVLA`、`ActThinkAbstain`、`VLA-ATTC`、`VisualThink-VLA`、`AdaWAM`、`BLUE`、`AVA-VLA`、`Reasoning-aware Speculative Decoding` 共同表明：reasoning 不是“越多越好”，而是必须控制何时推理、以什么 substrate 推理、付出多大执行代价。
- 这个主题的稳定共识是：如果不说明 reasoning substrate 和 compute policy，只说“更会想”或“更聪明”，就不足以形成可比结论。
- 共享 runtime evidence 说明了一个边界：reasoning gain 必须和 execution overhead 一起阅读，不能只摘收益 headline。

## Theme Structure
- 结构角色：reasoning 路线子主题页。
- 总纲页：[[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]
- 相邻但不等价的子主题：
  - [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
  - [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- 本页不把所有“更聪明”或“更稳健”的论文都纳入 reasoning efficiency；只有显式 reasoning substrate / policy 的工作进入主链。

## Route Split
- `explicit-reasoning retention`
  - 代表：[[wiki/papers/2505_08243_ECoT-Lite.md|ECoT-Lite]]
  - 依据：先承认显式 reasoning 有收益，再尝试压缩其代价。
- `dual-system reasoning-action split`
  - 代表：[[wiki/papers/2507_16815_ThinkAct.md|ThinkAct]]
  - 依据：把 reasoning 与 action 系统分开，让 planning 和 execution 在结构上解耦。
- `latent-planning compression`
  - 代表：[[wiki/papers/2601_09708_Fast-ThinkAct.md|Fast-ThinkAct]]、[[wiki/papers/2602_01166_LaRA-VLA.md|LaRA-VLA]]、[[wiki/papers/2604_18486_OneVL.md|OneVL]]、[[wiki/papers/2606_15099_AVA-VLA.md|AVA-VLA]]
  - 依据：把 reasoning 从显式 CoT 压到 latent 或 verbalizable substrate；[[wiki/papers/2604_18486_OneVL.md|OneVL]] 进一步用训练期 visual world-model decoder 约束 driving latents，并在推理期通过 prefill 接近 answer-only latency；[[wiki/papers/2606_15099_AVA-VLA.md|AVA-VLA]] 则把 early exit 加到 latent reasoning depth 上。
- `visual intermediate reasoning`
  - 代表：[[wiki/papers/2605_30011_VisualThink-VLA.md|VisualThink-VLA]]
  - 依据：用 compact visual-evidence interface 与 selective routing 替代 long textual CoT，在保留空间证据的同时降低 autoregressive textual reasoning latency。
- `gated-or-routed reasoning`
  - 代表：[[wiki/papers/2602_01100_StreamVLA.md|StreamVLA]]、[[wiki/papers/2603_05147_ActThinkAbstain.md|ActThinkAbstain]]、[[wiki/papers/2606_07089_AdaWAM.md|AdaWAM]]、[[wiki/papers/2606_08684_BLUE.md|BLUE]]、[[wiki/papers/2606_15099_AVA-VLA.md|AVA-VLA]]
  - 依据：只在需要时触发 reasoning 成本，把“想不想、想多久、用文本还是视觉想”交给 gating、routing 或 early-exit policy。
- `adaptive parallel deliberation`
  - 代表：[[wiki/papers/2605_01194_VLA-ATTC.md|VLA-ATTC]]
  - 依据：用 uncertainty-based cognitive clutch 触发 test-time deliberation，并用 Relative Action Critic 在并行 action candidates 中做 pairwise selection。
- `speculative reasoning acceleration`
  - 代表：[[wiki/papers/2606_31160_Reasoning-aware-Speculative-Decoding-FlatRoPE-AARL.md|Reasoning-aware Speculative Decoding]]
  - 依据：把 autonomous-driving VLA 的 chain-of-causation reasoning 拆成 routine draft reasoner 与 full visual target verification，直接压低 autoregressive reasoning latency；该路线需要和普通 action decoding speculative inference 分开读。

## Boundary Conditions
- 如果一篇论文没有明确的 reasoning substrate 或 compute policy，就不能和本主题主链直接比较。
- `latent-planning` 与 `gated reasoning` 虽都减少开销，但一个改 substrate、一个改触发策略，必须分 route 阅读。
- `safety`、`robustness`、`few-shot adaptation` 这类收益只有在论文明确把它们与 reasoning mechanism 绑定时才可作为本主题证据。
- 只报告更低 latency、没有明确 reasoning control mechanism 的论文，不能用来支持“reasoning efficiency”结论。
- 若 auxiliary decoder / world model 只在训练期提供 latent supervision，推理期是否保留该模块必须单独说明；不能把训练期 supervision 写成推理期 reasoning compute。
- adaptive TTC 必须同时说明触发条件、candidate sampling 数量和 control-frequency 影响；不能把它写成无成本的 reasoning 提升。
- speculative reasoning 必须说明被加速的是 reasoning token 还是 action head；不能把 reasoning draft acceptance 直接写成 action-generation 加速。
- visual evidence routing 不是传统 visual token pruning；它改变的是 reasoning substrate 和 evidence exposure policy。
- WAM 中的 adaptive textual / visual reasoning 需要和 VLA textual CoT compression 分开读，因为其 action-only fallback、video reasoning 和 subtask text update 属于不同执行模式。
- autonomous-driving VLA 中的 language-use gate 需要和 manipulation CoT compression 分开读，因为其收益依赖 frame-level driving route / action setting。

## Not Directly Comparable
- 纯 pruning / cache / deployment 论文不能直接进入本主题主比较。
- 同样使用“thinking”措辞但没有显式 reasoning control mechanism 的论文，只能作为边缘例子。
- 只提升任务表现、没有说明 reasoning overhead 如何变化的论文，不能直接与 reasoning-efficiency 路线比较。

## Evidence Links
- [[wiki/evidence/metrics/runtime-vs-task-metrics.md|runtime-vs-task-metrics]]
- [[wiki/papers/2505_08243_ECoT-Lite.md|ECoT-Lite]]
- [[wiki/papers/2507_16815_ThinkAct.md|ThinkAct]]
- [[wiki/papers/2601_09708_Fast-ThinkAct.md|Fast-ThinkAct]]
- [[wiki/papers/2602_01166_LaRA-VLA.md|LaRA-VLA]]
- [[wiki/papers/2604_18486_OneVL.md|OneVL]]
- [[wiki/papers/2602_01100_StreamVLA.md|StreamVLA]]
- [[wiki/papers/2603_05147_ActThinkAbstain.md|ActThinkAbstain]]
- [[wiki/papers/2605_01194_VLA-ATTC.md|VLA-ATTC]]
- [[wiki/papers/2605_30011_VisualThink-VLA.md|VisualThink-VLA]]
- [[wiki/papers/2606_07089_AdaWAM.md|AdaWAM]]
- [[wiki/papers/2606_08684_BLUE.md|BLUE]]
- [[wiki/papers/2606_15099_AVA-VLA.md|AVA-VLA]]

- [[wiki/papers/2606_31160_Reasoning-aware-Speculative-Decoding-FlatRoPE-AARL.md|Reasoning-aware Speculative Decoding]]
## Open Questions
- 当前关于 latent reasoning 与 gated reasoning 的统一 benchmark 仍然很弱，后续建模时仍需避免过强路线排序。
- 一些论文把 safety / abstention 作为主要收益，一些把 latency / planning 作为主要收益；这两类收益之间的共同比较轴仍有限。

## Gate Check
- `required_sections_complete: yes`
- `evidence_links_present: yes`
- `unscoped_comparative_claims: 0`
- `boundary_conditions_present: yes`
