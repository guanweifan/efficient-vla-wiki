# 2602_00780_EcoVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_00780_EcoVLA.md|2602_00780_EcoVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`1.60x`、`2.18x`、`0.4%`、`0.5%` 这些 headline 数字来自不同模型、不同 pruning ratio 以及是否组合 token pruning 的不同设置，仍需逐项拆证据。

## Evidence
- 核心证据命题：EcoVLA 的核心主张是：VLA 的最优模型稀疏模式会随着物理环境演化而动态变化，因此 static pruning 不够自适应，而固定间隔 dynamic pruning 又过于粗糙且往往依赖额外训练。 来源：[[raw/2602_00780_EcoVLA.pdf]]，**Abstract / introduction**：最清楚地说明为什么 static pruning 与 fixed-interval dynamic pruning 都不够，以及 EcoVLA 解决的两个核心问题：adaptive sparsity 与 pruning overhead。
- 补充证据命题：论文据此提出一个 training-free、plug-and-play 的 adaptive model pruning 框架，用于在线更新 VLA backbone 的稀疏模式，并且尽量把 pruning overhead 隐藏在原本的 inference bubbles 里。具体来说，EcoVLA 由两部分组成：Environment-aware Adaptive Pruning (`EAP`)，负责根据当前环境和时间一致性更新 channel sparsity pattern；Interleaved Inference Orchestration (`I2O`)，负责把 pruning 计算与推理过程并行交织，避免直接把 pruning 开销叠加到 wall-clock latency 上。 来源：[[raw/2602_00780_EcoVLA.pdf]]，**Figure 1 (p.1)**：最直接展示环境演化下 channel importance score 会变化，是“为什么要 adaptive pruning”的第一锚点。
- 主证据锚点 1：来源：[[raw/2602_00780_EcoVLA.pdf]]，**Abstract / introduction**：最清楚地说明为什么 static pruning 与 fixed-interval dynamic pruning 都不够，以及 EcoVLA 解决的两个核心问题：adaptive sparsity 与 pruning overhead。
- 主证据锚点 2：来源：[[raw/2602_00780_EcoVLA.pdf]]，**Figure 1 (p.1)**：最直接展示环境演化下 channel importance score 会变化，是“为什么要 adaptive pruning”的第一锚点。
- 主证据锚点 3：来源：[[raw/2602_00780_EcoVLA.pdf]]，**Figure 2 (p.3)**：EcoVLA 整体 pipeline 图，若补 `L2`，这是理解 EAP 与 I2O 如何配合的主方法锚点。

## Table / Metric Anchors
- **Table 1 (p.7)**：OpenVLA-OFT on LIBERO 的主结果锚点，用来核对独立 speedup 和与 FastV / VLA-Cache 组合后的额外收益。
- **Table 2 (p.7)**：π0.5 on LIBERO 的跨模型结果锚点，用来支撑 EcoVLA 在本身已较快的模型上仍能继续提速。
- **Table 3 (p.7)**：CogACT on SIMPLER 的结果锚点，用来支撑跨架构与跨 action decoder 的适用性。
- **Table 4 (p.7)**：real-world robot 结果锚点，用来支撑真实部署有效性。

## Table / Metric Split
- `**Table 1 (p.7)**` 这一层应单独承载 `**Table 1 (p.7)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_00780_EcoVLA.pdf]]，`**Table 1 (p.7)**`。
- `**Table 2 (p.7)**` 这一层应单独承载 `**Table 2 (p.7)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_00780_EcoVLA.pdf]]，`**Table 2 (p.7)**`。
- `**Table 3 (p.7)**` 这一层应单独承载 `**Table 3 (p.7)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_00780_EcoVLA.pdf]]，`**Table 3 (p.7)**`。
- `**Table 4 (p.7)**` 这一层应单独承载 `**Table 4 (p.7)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_00780_EcoVLA.pdf]]，`**Table 4 (p.7)**`。

## 不可混写项
- `1.60x`、`2.18x`、`0.4%`、`0.5%` 这些 headline 数字来自不同模型、不同 pruning ratio 以及是否组合 token pruning 的不同设置，仍需逐项拆证据。
- 论文把 EAP 与 I2O 一起包装成 EcoVLA 的总创新；后续 evidence 层可能需要区分“adaptive pruning quality”的收益与“overhead masking / orchestration”的收益。
- 论文强调可与 token pruning 正交组合，但这种组合优势当前主要通过少数特定方法与设置呈现；仍应明确其组合边界，而不是泛化成对任意 acceleration stack 都同样有效。

## 影响页面
- [[wiki/papers/2602_00780_EcoVLA.md|2602_00780_EcoVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
