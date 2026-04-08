# 2506_10100_EfficientVLA

## Source
- Raw: [[raw/2506_10100_EfficientVLA.pdf]]
- Extracts manifest: [[extracts/parses/2506_10100_EfficientVLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2506_10100_EfficientVLA/pdftotext.txt]]
- Fine-grained locator: [[extracts/parses/2506_10100_EfficientVLA/pdftotext.bbox.html]]

## Claim
- 页面定位：这是一篇 **training-free holistic inference acceleration for diffusion VLA** 论文；核心贡献是同时处理语言层、视觉 token 和 diffusion action head 三类冗余，而不是单一模块压缩。
- 这篇论文要解决的是：diffusion-based VLA 的推理瓶颈并不只来自单一模块，而是同时分布在语言模块、视觉 token 路径和迭代式 diffusion action head 中；如果只做局部优化，很难真正缓解端到端部署成本。
- 核心主张是：可以用一个 `training-free`、结构化的推理时框架，联合处理三类冗余：语言层间冗余、视觉 token 冗余、以及 diffusion action head 的时间冗余，从而在不重新训练模型的前提下得到系统级加速。
- 作者提出 `EfficientVLA`，包含三条主路径：基于层间相似性的语言层剪枝、任务感知且兼顾多样性的视觉 token 选择、以及 diffusion action head 的中间特征缓存复用。论文声称在 `CogACT + SIMPLER` 上可实现 `1.93×` 推理加速，并把 FLOPs 降到 baseline 的 `28.9%`，平均成功率仅下降 `0.6%`；更稳的写法是：这些 headline 都绑定在 `CogACT + SIMPLER` 的特定 operating point 上，而不是对所有 diffusion VLA 的统一加速结论。来源：[[raw/2506_10100_EfficientVLA.pdf]]，第 1 页摘要；第 7-8 页 Table 2 与相关结果分析。

## Methodology Index
- training-free acceleration
- structured holistic acceleration
- diffusion-based VLA
- CogACT
- language layer pruning
- inter-layer redundancy
- similarity-derived importance
- task-aware visual token selection
- task relevance and feature diversity
- diffusion action head caching
- temporal redundancy reduction
- SIMPLER benchmark

## Data Pointer
- 摘要与 headline claim：[[raw/2506_10100_EfficientVLA.pdf]] 第 1 页摘要。这里给出 `1.93× / 28.9% / 0.6%` 的主结果和三段式方法概览。
- 瓶颈与冗余分析：[[raw/2506_10100_EfficientVLA.pdf]] 第 2-3 页 Table 1 与 Fig. 1。这里说明语言模块、视觉输入和 diffusion action head 分别对应的内存/计算瓶颈，以及层间相似性、token 冗余、跨 timestep 特征相似性的经验依据。
- 方法总览：[[raw/2506_10100_EfficientVLA.pdf]] 第 4 页 Fig. 2。这里是 `EfficientVLA` 的整体框架图，集中展示三条加速路径如何协同工作。
- 主实验结果：[[raw/2506_10100_EfficientVLA.pdf]] 第 7-8 页 Table 2 与相关文字。这里是 `CogACT` 在 `SIMPLER` 上对比各 baseline 的主结果，也是 headline numeric claim 的主要证据来源。
- 效率与可扩展性补充：[[raw/2506_10100_EfficientVLA.pdf]] 第 8 页 Table 3 / Fig. 3；第 9 页 Table 4。这里分别对应速度-FLOPs-成功率折中、不同设置下的可扩展性，以及 token reduction ratio / cache interval 的敏感性。

## 待核点
- `FLOPs 降到 28.9%` 与 `71.1% reduction` 在论文里是同一件事的两种写法；后续进入 evidence/synthesis 时需要统一成单一口径，避免重复写成两个独立结论。
- headline 结果主要锚定在 `CogACT + SIMPLER` 的特定配置，不能提前泛化成“diffusion-based VLA 普遍都能达到 1.93× 加速”。
- 论文强调自己是 `training-free`，但也明确承认当前主要验证集中在 `CogACT`，且固定 cache interval 仍有精度-速度 tradeoff；这部分限制后续不能在总结里被抹掉。
- Table 2 中同时出现多个 `EfficientVLA` 配置（例如不同 `L/T` 组合）；后续需要明确 paper page 默认锚定的是哪一组配置，避免 headline claim 与次优配置混用。
