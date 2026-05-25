# 2605_13757_FrameSkip-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_13757_FrameSkip.md|2605_13757_FrameSkip]] 的单篇证据落点，用来拆分 frame-level training data selection、retention ratio 与多 benchmark success。

## Evidence
- 核心证据命题：FrameSkip 根据 action variation、visual-action coherence、task-progress prior 与 gripper-transition preservation 选择训练关键帧。来源：[[raw/2605_13757_FrameSkip.pdf]]，Abstract、Figure 1、Figure 3。
- 结果证据命题：论文在 RoboCasa-GR1、SimplerEnv 与 LIBERO 上报告保留部分 frames 后的成功率，并分析 20% unique frame retention。来源：[[raw/2605_13757_FrameSkip.pdf]]，Abstract、Tables 1-4。
- 消融证据命题：论文分别分析 retention ratio、importance metric、warmup 和真实 GR1 robot evaluation。来源：[[raw/2605_13757_FrameSkip.pdf]]，Tables 4-7。

## Table / Metric Anchors
- **Figures 1-3**：motivation and pipeline。
- **Tables 1-3**：main results。
- **Tables 4-7**：retention, metric, warmup, robot evaluation。

## Table / Metric Split
- frame retention 是训练数据口径，不是 inference token retention。
- macro-average success 与各 benchmark per-task result 需要分开读。

## 不可混写项
- 不应写成 runtime frame skipping。
- 不应写成模型结构或 action head 改动。

## 影响页面
- [[wiki/papers/2605_13757_FrameSkip.md|2605_13757_FrameSkip]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
