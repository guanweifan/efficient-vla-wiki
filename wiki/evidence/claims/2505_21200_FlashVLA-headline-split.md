# 2505_21200_FlashVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2505_21200_FlashVLA.md|2505_21200_FlashVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`55.7%` 的 FLOPs 降幅是 `visual-token FLOPs` 口径，不是整模型端到端 FLOPs；若进入 evidence/synthesis，需要明确写清。

## Evidence
- 作者提出 `FLASHVLA`，包含 `token-aware action reuse` 与 `information-guided visual token selection` 两条路径，并声称在 `OpenVLA + LIBERO` 主设置下，当视觉 token 减到原始输入的 `62.5%` 时，可把 **visual-token FLOPs** 降低 `55.7%`、时延降低 `36.0%`，平均成功率从 `74.4%` 到 `73.7%`，即下降 `0.7%`。更稳的写法是：这些 headline 来自特定 token budget 与 benchmark 平均值，而不是所有 VLA / 所有 budget 的统一结论。来源：[[raw/2505_21200_FlashVLA.pdf]]，第 1-2 页摘要；第 7 页 Table 1。
- 补充证据命题：核心主张是：VLA 推理中同时存在 `action-level redundancy` 和 `token-level redundancy`，因此可以用一个训练免费、可插拔的推理时框架同时做动作复用和视觉 token 剪枝，而不必改模型结构或重新训练。 来源：[[raw/2505_21200_FlashVLA.pdf]]，框架总览：[[raw/2505_21200_FlashVLA.pdf]] 第 4 页 Fig. 2。这里定义 `FlashTrigger`、`Action Memory`、`Token Memory`、pruned inference 与 reuse action 的整体交互。
- 主证据锚点 1：来源：[[raw/2505_21200_FlashVLA.pdf]]，摘要与动机：[[raw/2505_21200_FlashVLA.pdf]] 第 1-2 页摘要与 Fig. 1。这里给出 dual redundancy 观察、`Think Twice, Act Once` 的总体思路，以及 `55.7% / 36.0% / 0.7%` 的 headline 结果。
- 主证据锚点 2：来源：[[raw/2505_21200_FlashVLA.pdf]]，框架总览：[[raw/2505_21200_FlashVLA.pdf]] 第 4 页 Fig. 2。这里定义 `FlashTrigger`、`Action Memory`、`Token Memory`、pruned inference 与 reuse action 的整体交互。
- 主证据锚点 3：来源：[[raw/2505_21200_FlashVLA.pdf]]，两个核心机制：[[raw/2505_21200_FlashVLA.pdf]] 第 4-6 页 Sections 3.2-3.3。这里分别定义基于 `ICS` 的视觉 token 选择，以及基于动作变化角度和 token set 交并比的 action reuse 策略。

## Table / Metric Anchors
- 主结果与 ablation：[[raw/2505_21200_FlashVLA.pdf]] 第 7 页 Table 1；第 7-8 页 Section 4.2-4.3；第 8 页 Fig. 4 / Table 2。这里对应不同 token budget 下的效率-性能折中，以及去掉 pruning / reuse 后的消融。
- 泛化结果：[[raw/2505_21200_FlashVLA.pdf]] 第 10 页 Table 4。这里是作者在 VLAbench `Select Painting` 上做的额外验证。

## Table / Metric Split
- `Table 1` 是 **token budget / LIBERO average** 的主表：在 `62.5%` visual-token budget 下，`FLASHVLA` 把 `visual-token FLOPs` 降低 `55.7%`、latency 降低 `36.0%`，同时把平均 success rate 从 `74.4` 变成 `73.7`；这里的 `0.7` drop 绑定的就是这个 operating point，而不是所有 token budget 的统一损失。来源：[[raw/2505_21200_FlashVLA.pdf]]，第 7 页，Table 1。
- `Table 2 / Fig. 4` 对应 **机制拆分**：它们回答的是 action reuse 和 token pruning 分别贡献了什么，而不是重新给一组新的主结果 headline；因此不应把 ablation 数字和 `Table 1` 的主 operating point 混成同一句 superiority claim。来源：[[raw/2505_21200_FlashVLA.pdf]]，第 8 页，Table 2、Fig. 4。
- `Table 4` 只承担 **额外泛化验证**，它的绝对成绩与 `LIBERO` 主表不是一个 benchmark layer；若写 “泛化也成立”，必须把它标成 VLABench supplementary evidence。来源：[[raw/2505_21200_FlashVLA.pdf]]，第 10 页，Table 4。

## 不可混写项
- `55.7%` 的 FLOPs 降幅是 `visual-token FLOPs` 口径，不是整模型端到端 FLOPs；若进入 evidence/synthesis，需要明确写清。
- `0.7%` 的成功率下降来自 LIBERO 四个 task suite 平均值从 `74.4%` 到 `73.7%`，对应的是 `160-token` 配置；不能把它泛化成所有 token budget 都只有这一点损失。
- 论文把方法描述为 training-free 和 plug-and-play，但实验主体是 `OpenVLA` 在 LIBERO 上的加速；对其他 VLA backbone 的适配强度目前更多是兼容性主张，不是大规模实证。

## 影响页面
- [[wiki/papers/2505_21200_FlashVLA.md|2505_21200_FlashVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
