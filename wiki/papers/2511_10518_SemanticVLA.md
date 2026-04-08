# 2511_10518_SemanticVLA

## Source
- Raw: [[raw/2511_10518_SemanticVLA.pdf]]
- Extracts manifest: [[extracts/parses/2511_10518_SemanticVLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2511_10518_SemanticVLA/pdftotext.txt]]

## Claim
- 这篇论文要解决的是：现有 VLA 在机器人操作中常同时受到两类问题约束，一是视觉输入冗余导致计算浪费，二是 instruction 与视觉之间的语义对齐过浅，导致模型难以抓住真正与任务相关的语义锚点和空间关系。
- 核心主张是：如果把“语义对齐的视觉稀疏化”“跨 SigLIP / DINOv2 的层级融合”“语义条件化动作耦合”联合设计，就能在减少视觉与动作表示冗余的同时，提升语义 grounding、动作可解释性和整体效率。
- 作者提出 `SemanticVLA`，由 `SD-Pruner`、`SH-Fuser` 和 `SA-Coupler` 三部分组成，并声称在 `LIBERO` 上相对 `OpenVLA` 将 overall success rate 提升 `21.1%`，同时把 training cost 和 inference latency 分别降低 `3.0×` 与 `2.7×`；在同一套结果中，`SemanticVLA` 的 overall LIBERO success rate 为 `97.7%`，`SemanticVLA-Lite` 为 `95.8%`。来源：[[raw/2511_10518_SemanticVLA.pdf]]，第 1 页摘要；第 4-5 页 Table 1；附录 Table 9。

## Methodology Index
- semantic-aligned sparsification
- efficient robotic manipulation
- SD-Pruner
- ID-Pruner
- SA-Pruner
- SigLIP
- DINOv2
- instruction-driven pruning
- spatial-aggregation pruning
- SH-Fuser
- semantic-complementary hierarchical fusion
- SA-Coupler
- semantic-conditioned action coupler
- action token compression
- parallel decoding
- SemanticVLA-Lite
- LIBERO
- real-world manipulation

## Data Pointer
- 摘要与整体命题：[[raw/2511_10518_SemanticVLA.pdf]] 第 1 页摘要与 Fig. 1。这里给出“semantic-aligned sparsification + enhancement”的总框架，以及 `21.1% / 3.0× / 2.7×` 的 headline。
- 方法总览：[[raw/2511_10518_SemanticVLA.pdf]] 第 3-4 页 Fig. 2 与 Fig. 3 及相邻章节。这里定义 `SD-Pruner`、`SH-Fuser`、`SA-Coupler` 如何分别作用于视觉稀疏化、跨编码器融合与动作表示重构。
- 主模拟结果：[[raw/2511_10518_SemanticVLA.pdf]] 第 4-5 页 Table 1。这里是 `LIBERO` 四个 suite 与 overall 的主对比结果，也是 `97.7%` 与对 `OpenVLA` 提升 `21.1%` 的主要来源。
- 稀疏率与模块消融：[[raw/2511_10518_SemanticVLA.pdf]] 第 8-9 页 Tables 4-6。这里可回查 `SemanticVLA-Lite`、`8×/16×` 稀疏率 tradeoff，以及 `SD-Pruner / SH-Fuser / SA-Coupler` 的增益归因。
- 效率与真实机器人结果：[[raw/2511_10518_SemanticVLA.pdf]] 附录 Table 9；以及 real-world Tables 7-8。这里对应 training cost、latency、throughput、LIBERO SR 的效率-性能折中，以及多平台真实机器人结果。

## 待核点
- `3.0× training cost` 与 `2.7× inference latency` 的 headline 实际来自附录效率表，并依赖具体 baseline 和 token compression 设置；后续不能脱离 Table 9 的比较对象单独引用。
- 论文同时存在 `SemanticVLA` 与 `SemanticVLA-Lite` 两个主变体，且 `Lite` 更偏极致效率、主模型更偏 Pareto 最优；后续需要明确 paper-level 默认强调哪一个。
- `21.1%` 的 success rate 提升是相对 `OpenVLA` 的 overall LIBERO 结果，不是相对所有 baseline 的统一提升幅度。
- 论文强调 semantic alignment 与 interpretable behavior modeling，但这些更偏机制主张；若后续要把“可解释性”写成核心结论，需要补更多直接证据，而不能只靠命名和可视化描述。
