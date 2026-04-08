# 2511_10518_SemanticVLA

## Source
- Raw: [[raw/2511_10518_SemanticVLA.pdf]]
- Extracts manifest: [[extracts/parses/2511_10518_SemanticVLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2511_10518_SemanticVLA/pdftotext.txt]]
- Fine-grained locator: [[extracts/parses/2511_10518_SemanticVLA/pdftotext.bbox.html]]

## Claim
- 页面定位：这是一篇 **semantic-aligned visual sparsification + enhancement for manipulation VLA** 论文；核心贡献是把语义对齐的视觉稀疏化、跨视觉骨干的层级融合和动作耦合放进同一套高效架构，而不是一般意义上的通用 grounding 或纯 tokenizer 压缩论文。
- 这篇论文要解决的是：现有 VLA 在机器人操作中常同时受到两类问题约束，一是视觉输入冗余导致计算浪费，二是 instruction 与视觉之间的语义对齐过浅，导致模型难以抓住真正与任务相关的语义锚点和空间关系。
- 核心主张是：如果把“语义对齐的视觉稀疏化”“跨 SigLIP / DINOv2 的层级融合”“语义条件化动作耦合”联合设计，就能在减少视觉与动作表示冗余的同时，提升语义 grounding、动作可解释性和整体效率。
- 作者提出 `SemanticVLA`，由 `SD-Pruner`、`SH-Fuser` 和 `SA-Coupler` 三部分组成。它的 headline 需要拆开读：`21.1%` 指的是 **LIBERO overall success rate** 相对 `OpenVLA` 的提升；`97.7%` 与 `95.8%` 则分别对应主模型 `SemanticVLA` 与高压缩版本 `SemanticVLA-Lite` 的 overall LIBERO success；`3.0× training cost` 与 `2.7× inference latency` 来自附录 real-world efficiency 表，不是和主模拟结果同一张表里的统一 trade-off。更稳的写法是：**SemanticVLA 在 LIBERO 上给出更高 success rate，而 SemanticVLA-Lite 提供更激进的效率折中；训练成本和推理延迟优势需要单独回到 Table 9 理解。** 来源：[[raw/2511_10518_SemanticVLA.pdf]]，第 1 页摘要；第 4-5 页 Table 1；附录 Table 9。

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

## Data Pointer
- 摘要与整体命题：[[raw/2511_10518_SemanticVLA.pdf]] 第 1 页摘要与 Fig. 1。这里给出“semantic-aligned sparsification + enhancement”的总框架，并把 `21.1% / 3.0× / 2.7×` 打包成 headline。
- 方法总览：[[raw/2511_10518_SemanticVLA.pdf]] 第 3-4 页 Fig. 2 与 Fig. 3 及相邻章节。这里定义 `SD-Pruner`、`SH-Fuser`、`SA-Coupler` 如何分别作用于视觉稀疏化、跨编码器融合与动作表示重构。
- 主模拟结果：[[raw/2511_10518_SemanticVLA.pdf]] 第 4-5 页 Table 1。这里是 `LIBERO` 四个 suite 与 overall 的主对比结果，也是 `97.7%`、`95.8%` 与相对 `OpenVLA` 提升 `21.1%` 的主要来源。
- 稀疏率与模块消融：[[raw/2511_10518_SemanticVLA.pdf]] 第 8-9 页 Tables 4-6。这里可回查 `SemanticVLA-Lite`、`8×/16×` 稀疏率 tradeoff，以及 `SD-Pruner / SH-Fuser / SA-Coupler` 的增益归因。
- 效率与真实机器人结果：[[raw/2511_10518_SemanticVLA.pdf]] 第 6-7 页 Tables 2-3；附录 Table 9。前者对应真实机器人 success / throughput，后者才是 `training cost`、`latency`、`GPU memory` 这类效率 headline 的直接出处。

## Evidence Links
- [[wiki/evidence/claims/2511_10518_SemanticVLA-headline-split.md|2511_10518_SemanticVLA-headline-split]]

## 待核点
- `3.0× training cost` 与 `2.7× inference latency` 的 headline 实际来自附录效率表，并依赖具体 real-world setup、baseline 和 token compression 设置；后续不能脱离 Table 9 的比较对象单独引用。
- 论文同时存在 `SemanticVLA` 与 `SemanticVLA-Lite` 两个主变体，且 `Lite` 更偏极致效率、主模型更偏 Pareto 最优；后续如写单一 headline，需要显式说明到底是在强调主模型还是 `Lite`。
- `21.1%` 的 success rate 提升是相对 `OpenVLA` 的 overall LIBERO 结果，不是相对所有 baseline 的统一提升幅度。
- 论文强调 semantic alignment 与 interpretable behavior modeling，但这些更偏机制主张；若后续要把“可解释性”写成核心结论，需要补更多直接证据，而不能只靠命名和可视化描述。
