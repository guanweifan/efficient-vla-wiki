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
- `FAST`、`VITA-VLA`、`FT-NCFM`、`ActDistill` 共同表明，训练效率已经不是 inference efficiency 的附属注脚，而是独立问题。
- 这些工作都把“降低训练代价”写成主收益，但降低代价的方式不同：有的压 token，有的压 teacher/adaptation，有的压 data requirement。
- `Fast-dVLA` 只作为桥接例子存在：它说明训练侧技巧可以服务推理路线，但不能因此把训练与推理混成同一主题。

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
  - 代表：[[wiki/papers/2510_09607_VITA-VLA.md|VITA-VLA]]、[[wiki/papers/2511_18082_ActDistill.md|ActDistill]]
  - 依据：通过 teacher/student 或 action expert 降低 adaptation 与 supervision 成本。
- `data-centric-efficiency`
  - 代表：[[wiki/papers/2511_16233_FT-NCFM.md|FT-NCFM]]
  - 依据：通过 synthetic coreset / data reduction 降低训练需求。
- `train-to-infer bridge`
  - 代表：[[wiki/papers/2603_25661_Fast-dVLA.md|Fast-dVLA]]
  - 依据：训练侧 distillation 被回收进推理效率，但仍不能直接替代训练成本主链。

## Boundary Conditions
- 只要收益主要体现在 inference latency，而不是 `training steps / GPU hours / data ratio / adaptation cost`，就不能进入本主题主比较。
- `teacher-distillation` 方法之间只有在 teacher 依赖、teacher 成本和行为保持目标大致一致时，才有直接比较意义。
- `data-centric` 方法的收益必须回到 data ratio、synthetic set 或 training reduction 设定，不能和 tokenizer 压缩法直接并表为统一“更省”。
- 若一篇论文同时宣称训练更便宜和推理更快，两个收益必须分层写；不能用单一 headline 混写。

## Not Directly Comparable
- 主要目标是 inference latency / deployment 的论文，即使包含 distillation 或 cache，也不能直接与训练效率主链比较。
- `Fast-dVLA` 这类桥接工作只能作为边缘例子，不能定义训练效率本身。
- 没有直接训练成本指标的论文，不能进入本主题主比较。

## Evidence Links
- [[wiki/evidence/metrics/training-cost-vs-performance.md|training-cost-vs-performance]]
- [[wiki/papers/2501_09747_FAST.md|FAST]]
- [[wiki/papers/2510_09607_VITA-VLA.md|VITA-VLA]]
- [[wiki/papers/2511_16233_FT-NCFM.md|FT-NCFM]]
- [[wiki/papers/2511_18082_ActDistill.md|ActDistill]]
- [[wiki/papers/2603_25661_Fast-dVLA.md|Fast-dVLA]]

## Open Questions
- 当前仍缺少把 `teacher cost` 本身单独量化的统一 evidence 页；这会限制 distillation 路线之间的更细比较。
- 训练侧收益和长期下游泛化之间的关系，仍多依赖单篇论文叙述，后续可能需要更细 evidence 补充。

## Gate Check
- `required_sections_complete: yes`
- `evidence_links_present: yes`
- `unscoped_comparative_claims: 0`
- `boundary_conditions_present: yes`
