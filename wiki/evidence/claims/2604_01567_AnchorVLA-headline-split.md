# 2604_01567_AnchorVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_01567_AnchorVLA.md|2604_01567_AnchorVLA]] 的单篇证据落点，用来拆开 anchored diffusion、residual correction 与 latency / success 指标。

## Evidence
- 核心证据命题：`AnchorVLA` 通过 anchor-guided truncated diffusion 保留 multimodal action generation，同时降低 sampling cost。来源：[[raw/2604_01567_AnchorVLA.pdf]]，Abstract；方法部分。
- 补充证据命题：residual correction module 用于减轻 chunking-induced drift。来源：[[raw/2604_01567_AnchorVLA.pdf]]，Abstract；Sec. 3.3。

## Table / Metric Anchors
- **主实验表**：`64.0%` ManiSkill-HAB average success。
- **long-horizon / horizon robustness 图表**：`61.5%` success at longer chunks。
- **anchored truncation 表**：`60.6 Hz -> 89.8 Hz` 与 `1.48×` speedup。
- **residual correction ablation**：适合后续补 drift correction 的增益与额外开销。

## 不可混写项
- `64.0% average success`
- `61.5% success at longer chunks`
- `60.6 Hz -> 89.8 Hz`
- `1.48× speedup`
- 这些分别属于主 benchmark、长 horizon robustness 与 specific denoising-speed setting。

## 影响页面
- [[wiki/papers/2604_01567_AnchorVLA.md|2604_01567_AnchorVLA]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]

## 边界
- 本页只承担单篇 anchored diffusion 的 claim 落点，不承担 mobile manipulation 全景综述。
