# 2507_23318_FastDriveVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2507_23318_FastDriveVLA.md|2507_23318_FastDriveVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：“SOTA” 的比较范围是 nuScenes open-loop planning benchmark 上的当前 baselines 与指定 base model，不应外推成 closed-loop driving 或更广泛 driving stack 的无条件优势。

## Evidence
- 核心证据命题：这篇论文要解决的是：自动驾驶 VLA 模型的视觉 token 序列很长，推理成本高；而已有 attention-based 或 similarity-based token pruning 方法并不充分利用驾驶场景中“前景更关键”的结构，因而效果有限。 来源：[[raw/2507_23318_FastDriveVLA.pdf]]，`PDF p.1` Abstract + Fig. 1：
- 补充证据命题：作者提出 `FastDriveVLA`，核心是一个 plug-and-play 的视觉 token pruner `ReconPruner`。它不依赖 VLA 主体重训练，而是通过前景重建与对抗式前景-背景重建 (`AFBR`) 学会给 visual tokens 打分，从而在推理时只保留更关键的前景相关 tokens。 来源：[[raw/2507_23318_FastDriveVLA.pdf]]，问题设定、foreground-aware pruning 的核心动机、`0.07B` / `241K` / SOTA on nuScenes open-loop benchmark 等 headline 都在这里。
- 主证据锚点 1：来源：[[raw/2507_23318_FastDriveVLA.pdf]]，`PDF p.1` Abstract + Fig. 1：
- 主证据锚点 2：来源：[[raw/2507_23318_FastDriveVLA.pdf]]，问题设定、foreground-aware pruning 的核心动机、`0.07B` / `241K` / SOTA on nuScenes open-loop benchmark 等 headline 都在这里。
- 主证据锚点 3：来源：[[raw/2507_23318_FastDriveVLA.pdf]]，`PDF p.2-4` Fig. 2 / Fig. 3 + Method：

## Table / Metric Anchors
- `PDF p.5-6` Table 1：
  - Impromptu-VLA 上不同 pruning methods 的主结果在这里；`25% / 50% / 75%` pruning 下与 FastV、SparseVLM、VisPruner、DivPrune 的比较都在这里。
- `PDF p.6` Table 2：
  - pixel reconstruction 与 `AFBR` 的 ablation 在这里，用于锚定“为什么 foreground mask prediction 不够”的证据。
- `PDF p.7` Table 3 / Table 4 + Fig. 5：
  - 与 ground-truth foreground mask pruning 的对比、效率分析、以及不同方法保留 token 的可视化都在这里。

## Table / Metric Split
- ``PDF p.5-6` Table 1` 这一层支撑 ``PDF p.5-6` Table 1` 对应的 benchmark / metric / operating point。 - Impromptu-VLA 上不同 pruning methods 的主结果在这里；`25% / 50% / 75%` pruning 下与 FastV、SparseVLM、VisPruner、DivPrune 的比较都在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2507_23318_FastDriveVLA.pdf]]，``PDF p.5-6` Table 1`。
- ``PDF p.6` Table 2` 这一层支撑 ``PDF p.6` Table 2` 对应的 benchmark / metric / operating point。 - pixel reconstruction 与 `AFBR` 的 ablation 在这里，当前对应“为什么 foreground mask prediction 不够”的证据。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2507_23318_FastDriveVLA.pdf]]，``PDF p.6` Table 2`。
- ``PDF p.7` Table 3 / Table 4 + Fig. 5` 这一层支撑 ``PDF p.7` Table 3 / Table 4 + Fig. 5` 对应的 benchmark / metric / operating point。 - 与 ground-truth foreground mask pruning 的对比、效率分析、以及不同方法保留 token 的可视化都在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2507_23318_FastDriveVLA.pdf]]，``PDF p.7` Table 3 / Table 4 + Fig. 5`。

## 不可混写项
- “SOTA” 的比较范围是 nuScenes open-loop planning benchmark 上的当前 baselines 与指定 base model，不应外推成 closed-loop driving 或更广泛 driving stack 的无条件优势。
- “plug-and-play” 更准确地说是：对共享 visual encoder 的 VLA 模型可直接接入，而不是对任意视觉前端都零代价迁移。
- 论文明确推荐 `50%` pruning 作为较平衡的部署点，但不同 pruning ratio 在不同 metric 上各有 tradeoff；后续不能把某一 ratio 的结果写成普遍最优。

## 影响页面
- [[wiki/papers/2507_23318_FastDriveVLA.md|2507_23318_FastDriveVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
