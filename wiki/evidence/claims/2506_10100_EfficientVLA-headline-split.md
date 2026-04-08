# 2506_10100_EfficientVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2506_10100_EfficientVLA.md|2506_10100_EfficientVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`FLOPs 降到 28.9%` 与 `71.1% reduction` 在论文里是同一件事的两种写法；后续进入 evidence/synthesis 时需要统一成单一口径，避免重复写成两个独立结论。

## Evidence
- 作者提出 `EfficientVLA`，包含三条主路径：基于层间相似性的语言层剪枝、任务感知且兼顾多样性的视觉 token 选择、以及 diffusion action head 的中间特征缓存复用。论文声称在 `CogACT + SIMPLER` 上可实现 `1.93×` 推理加速，并把 FLOPs 降到 baseline 的 `28.9%`，平均成功率仅下降 `0.6%`；更稳的写法是：这些 headline 都绑定在 `CogACT + SIMPLER` 的特定 operating point 上，而不是对所有 diffusion VLA 的统一加速结论。来源：[[raw/2506_10100_EfficientVLA.pdf]]，第 1 页摘要；第 7-8 页 Table 2 与相关结果分析。
- 补充证据命题：核心主张是：可以用一个 `training-free`、结构化的推理时框架，联合处理三类冗余：语言层间冗余、视觉 token 冗余、以及 diffusion action head 的时间冗余，从而在不重新训练模型的前提下得到系统级加速。 来源：[[raw/2506_10100_EfficientVLA.pdf]]，瓶颈与冗余分析：[[raw/2506_10100_EfficientVLA.pdf]] 第 2-3 页 Table 1 与 Fig. 1。这里说明语言模块、视觉输入和 diffusion action head 分别对应的内存/计算瓶颈，以及层间相似性、token 冗余、跨 timestep 特征相似性的经验依据。
- 主证据锚点 1：来源：[[raw/2506_10100_EfficientVLA.pdf]]，摘要与 headline claim：[[raw/2506_10100_EfficientVLA.pdf]] 第 1 页摘要。这里给出 `1.93× / 28.9% / 0.6%` 的主结果和三段式方法概览。
- 主证据锚点 2：来源：[[raw/2506_10100_EfficientVLA.pdf]]，瓶颈与冗余分析：[[raw/2506_10100_EfficientVLA.pdf]] 第 2-3 页 Table 1 与 Fig. 1。这里说明语言模块、视觉输入和 diffusion action head 分别对应的内存/计算瓶颈，以及层间相似性、token 冗余、跨 timestep 特征相似性的经验依据。
- 主证据锚点 3：来源：[[raw/2506_10100_EfficientVLA.pdf]]，方法总览：[[raw/2506_10100_EfficientVLA.pdf]] 第 4 页 Fig. 2。这里是 `EfficientVLA` 的整体框架图，集中展示三条加速路径如何协同工作。

## Table / Metric Anchors
- 瓶颈与冗余分析：[[raw/2506_10100_EfficientVLA.pdf]] 第 2-3 页 Table 1 与 Fig. 1。这里说明语言模块、视觉输入和 diffusion action head 分别对应的内存/计算瓶颈，以及层间相似性、token 冗余、跨 timestep 特征相似性的经验依据。
- 主实验结果：[[raw/2506_10100_EfficientVLA.pdf]] 第 7-8 页 Table 2 与相关文字。这里是 `CogACT` 在 `SIMPLER` 上对比各 baseline 的主结果，也是 headline numeric claim 的主要证据来源。
- 效率与可扩展性补充：[[raw/2506_10100_EfficientVLA.pdf]] 第 8 页 Table 3 / Fig. 3；第 9 页 Table 4。这里分别对应速度-FLOPs-成功率折中、不同设置下的可扩展性，以及 token reduction ratio / cache interval 的敏感性。

## Table / Metric Split
- `Table 2` 是 **主 operating point**：`1.93×` speedup、FLOPs 下降到 baseline 的 `28.9%`、平均成功率仅下降 `0.6%` 这三项应被视为同一 `CogACT + SIMPLER` operating point 下的 paired claim，而不是可拆开的三条独立普适结论。来源：[[raw/2506_10100_EfficientVLA.pdf]]，第 7-8 页，Table 2。
- `Table 3 / Fig. 3` 负责 **速度-精度折中曲线**：不同 `L/T` 组合和不同 reduction ratio 对 latency / FLOPs / success 的影响应留在这里阅读，不能把次优配置和主 operating point 混成统一 headline。来源：[[raw/2506_10100_EfficientVLA.pdf]]，第 8 页，Table 3、Fig. 3。
- `Table 4` 负责 **cache interval / token reduction sensitivity**：它解释为什么 `training-free` 方案仍存在精度-速度 tradeoff，因此 paper page 不应把 EfficientVLA 写成“无条件零代价加速”。来源：[[raw/2506_10100_EfficientVLA.pdf]]，第 9 页，Table 4。

## 不可混写项
- `FLOPs 降到 28.9%` 与 `71.1% reduction` 在论文里是同一件事的两种写法；后续进入 evidence/synthesis 时需要统一成单一口径，避免重复写成两个独立结论。
- headline 结果主要锚定在 `CogACT + SIMPLER` 的特定配置，不能提前泛化成“diffusion-based VLA 普遍都能达到 1.93× 加速”。
- 论文强调自己是 `training-free`，但也明确承认当前主要验证集中在 `CogACT`，且固定 cache interval 仍有精度-速度 tradeoff；这部分限制后续不能在总结里被抹掉。

## 影响页面
- [[wiki/papers/2506_10100_EfficientVLA.md|2506_10100_EfficientVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
