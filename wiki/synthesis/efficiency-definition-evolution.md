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
- `FAST` 与 `FT-NCFM` 共同表明，训练侧效率已经是独立命题；更少 GPU 小时、更少训练步数或更少数据比例，不能被偷换成推理更快。
- `VLA-Perf` 进一步把 placement、network 与 system knob 拉进效率讨论，说明“效率”已经不是纯模型层指标。
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
  - 代表：[[wiki/papers/2409_12514_TinyVLA.md|TinyVLA]]、[[wiki/papers/2410_05273_HiRT.md|HiRT]]、[[wiki/papers/2505_21200_FlashVLA.md|FlashVLA]]、[[wiki/papers/2506_10100_EfficientVLA.md|EfficientVLA]]
  - 作用：把“更快”和“更强”从单一句子中拆开，要求回到 paired operating point。
- `training-cost disentanglement`
  - 代表：[[wiki/papers/2501_09747_FAST.md|FAST]]、[[wiki/papers/2511_16233_FT-NCFM.md|FT-NCFM]]
  - 作用：把训练时长、GPU 小时、数据比例与推理速度分层阅读。
- `deployment-as-first-class-efficiency`
  - 代表：[[wiki/papers/2602_18397_VLA-Perf.md|VLA-Perf]]
  - 作用：把 placement、jitter、memory ceiling 收编为效率定义本身，而不是附属系统注。
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

## Open Questions
- 当前还缺少一页把 `memory footprint`、`energy` 与 `network transport` 进一步并入统一效率定义；这不阻塞当前主题页，但会影响后续 deployment-oriented synthesis 的细化。
- 多数论文仍把 wording boundary 写在局部实验设置里，而不是方法声明中；后续仍需持续收紧。

## Gate Check
- `required_sections_complete: yes`
- `evidence_links_present: yes`
- `unscoped_comparative_claims: 0`
- `boundary_conditions_present: yes`
