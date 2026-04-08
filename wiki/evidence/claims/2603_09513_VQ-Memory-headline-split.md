# 2603_09513_VQ-Memory-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_09513_VQ-Memory.md|2603_09513_VQ-Memory]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`25.0% -> 56.3%` 与 `48.8% -> 76.5%` 来自 `π0` 在 `RuleSafe` multi-task setting 下的 headline，不应直接外推到所有 base model。

## Evidence
- 核心证据命题：这篇论文要解决的是：现有 articulated manipulation benchmark 多聚焦短时、近 Markov 的简单操作，难以覆盖门锁、密码锁、逻辑锁等需要长期阶段记忆与非当前观测推断的任务；同时，直接把原始历史状态当 memory 又容易带来噪声敏感和过拟合。 来源：[[raw/2603_09513_VQ-Memory.pdf]]，`PDF p.1-2` Abstract + Introduction：
- 补充证据命题：作者提出两部分贡献：一是 `RuleSafe`，用规则化 articulated lock 机制构造 non-Markovian、long-horizon manipulation benchmark；二是 `VQ-Memory`，把历史 joint-state sequence 经 `VQ-VAE` 压缩成离散 memory tokens，以更紧凑、结构化且噪声鲁棒的方式向 VLA / diffusion policy 提供阶段上下文。 来源：[[raw/2603_09513_VQ-Memory.pdf]]，RuleSafe 的问题动机、non-Markovian articulated manipulation 的设定、以及 `VQ-Memory` 的高层主张都在这里。
- 主证据锚点 1：来源：[[raw/2603_09513_VQ-Memory.pdf]]，`PDF p.1-2` Abstract + Introduction：
- 主证据锚点 2：来源：[[raw/2603_09513_VQ-Memory.pdf]]，RuleSafe 的问题动机、non-Markovian articulated manipulation 的设定、以及 `VQ-Memory` 的高层主张都在这里。
- 主证据锚点 3：来源：[[raw/2603_09513_VQ-Memory.pdf]]，`PDF p.3-5` Fig. 1 + benchmark construction section：

## Table / Metric Anchors
- `PDF p.6-7` Table 1 + Table 2：
  - single-task 与 cross-model 泛化结果在这里；`rule 020` 上对 `DP3 / RDT / CogACT` 的提升应回这里核定。
- `PDF p.7` Table 3：
  - multi-task 主结果在这里；`25.0% -> 56.3%` 和 `48.8% -> 76.5%` 的 headline 应回这张表。
- `PDF p.8` Table 4：
  - cluster 数量与 memory length 的 ablation 在这里，用于锚定“为什么离散 memory 能更稳”和“最佳 memory budget 在哪里”。

## Table / Metric Split
- ``PDF p.6-7` Table 1 + Table 2` 这一层支撑 ``PDF p.6-7` Table 1 + Table 2` 对应的 benchmark / metric / operating point。 - single-task 与 cross-model 泛化结果在这里；`rule 020` 上对 `DP3 / RDT / CogACT` 的提升应回这里核定。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2603_09513_VQ-Memory.pdf]]，``PDF p.6-7` Table 1 + Table 2`。
- ``PDF p.7` Table 3` 这一层支撑 ``PDF p.7` Table 3` 对应的 benchmark / metric / operating point。 - multi-task 主结果在这里；`25.0% -> 56.3%` 和 `48.8% -> 76.5%` 的 headline 应回这张表。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2603_09513_VQ-Memory.pdf]]，``PDF p.7` Table 3`。
- ``PDF p.8` Table 4` 这一层支撑 ``PDF p.8` Table 4` 对应的 benchmark / metric / operating point。 - cluster 数量与 memory length 的 ablation 在这里，当前对应“为什么离散 memory 能更稳”和“最佳 memory budget 在哪里”。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2603_09513_VQ-Memory.pdf]]，``PDF p.8` Table 4`。

## 不可混写项
- `25.0% -> 56.3%` 与 `48.8% -> 76.5%` 来自 `π0` 在 `RuleSafe` multi-task setting 下的 headline，不应直接外推到所有 base model。
- `VQ-Memory` 的 architecture-agnostic 主张主要来自 `rule 020` 上对 `DP3 / RDT / CogACT` 的跨模型增益；这更像困难单任务泛化证据，而不是全 benchmark 全 setting 的统一结论。
- 论文当前更像是在证明“高层时序记忆与阶段感知”问题已被显著改善，但作者也明确保留了执行精度仍是瓶颈的 caveat；后续不能把 remaining failures 忽略掉。

## 影响页面
- [[wiki/papers/2603_09513_VQ-Memory.md|2603_09513_VQ-Memory]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
