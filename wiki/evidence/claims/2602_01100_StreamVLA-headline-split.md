# 2602_01100_StreamVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_01100_StreamVLA.md|2602_01100_StreamVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`98.5% success rate`、`72% skip ratio`、`244 ms -> 128 ms`、`48% latency reduction` 分别对应不同实验层面；仍需拆清哪些属于主 benchmark 结果，哪些属于 inference ablation。

## Evidence
- 这篇论文提出 **StreamVLA**，目标是在长时程机器人操作里打破“每个控制步都重新做高成本推理”的耦合范式。作者的基本判断是：现有 reasoning-heavy VLA 把高层规划和低层控制缠在一起，哪怕子任务状态没有变化，也会在每一步重复进行昂贵的自回归推理和视觉生成，导致计算冗余和实时性不足。来源：[[raw/2602_01100_StreamVLA.pdf]]，第 1-2 页 Abstract、Introduction。
- 核心方法主张是一个 **dual-system**、但仍在**单一共享 backbone** 内实现的框架：`System 2` 负责低频的文本子任务生成和 completion-state imagination，`System 1` 负责高频动作生成。论文用一个 **Lock-and-Gated** 机制，只在检测到子任务切换或失败时才触发慢速推理；在平稳执行阶段，则锁定高层意图，直接条件化 **Flow Matching** 动作头。来源：[[raw/2602_01100_StreamVLA.pdf]]，第 1 页 Abstract；第 2-4 页 Fig. 1、Fig. 2、Sec. III。
- 主证据锚点 1：来源：[[raw/2602_01100_StreamVLA.pdf]]，**Abstract**：第 1 页。可直接承载 `98.5%`、`72%`、`48% latency reduction` 和 dual-system framing。
- 主证据锚点 2：来源：[[raw/2602_01100_StreamVLA.pdf]]，**Fig. 1 + Introduction**：第 1-2 页。用于锚定 slow thinking / fast action、`244 ms -> 128 ms` 以及为何 fixed-offset future prediction 不适合机器人控制。
- 主证据锚点 3：来源：[[raw/2602_01100_StreamVLA.pdf]]，**Fig. 2 + Sec. III-A/B**：第 3-4 页。用于锚定 unified architecture、shared backbone、System 2 / System 1 的模块分工。

## Table / Metric Anchors
- **Table I / benchmark comparison**：第 6-7 页。用于锚定 LIBERO 与 RoboTwin 的 success-rate 结果，以及与 π0/π0.5、CoT-VLA 等方法的对比。

## Table / Metric Split
- `**Table I / benchmark comparison**` 这一层应单独承载 `**Table I / benchmark comparison**` 相关的 benchmark / metric / operating point。 这一层对应 LIBERO 与 RoboTwin 的 success-rate 结果，以及与 π0/π0.5、CoT-VLA 等方法的对比。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_01100_StreamVLA.pdf]]，`**Table I / benchmark comparison**`。

## 不可混写项
- `98.5% success rate`、`72% skip ratio`、`244 ms -> 128 ms`、`48% latency reduction` 分别对应不同实验层面；仍需拆清哪些属于主 benchmark 结果，哪些属于 inference ablation。
- 论文同时覆盖 LIBERO、RoboTwin 2.0 和真实世界 interference recovery；仍需决定单篇主 claim 里保留多强的“robust recovery”语气。
- StreamVLA 同时可被理解为 `dual-system VLA`、`completion-state gated VLA`、`unified foresight-driven gating framework`；后续 taxonomy 需要统一其主定位。

## 影响页面
- [[wiki/papers/2602_01100_StreamVLA.md|2602_01100_StreamVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
