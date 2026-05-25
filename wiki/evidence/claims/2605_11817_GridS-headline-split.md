# 2605_11817_GridS-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_11817_GridS.md|2605_11817_GridS]] 的单篇证据落点，用来拆分 differentiable visual-token resampling、FLOPs reduction、token retention 与 task result。

## Evidence
- 核心证据命题：GridS 预测 salient coordinates，并通过 differentiable interpolation 从视觉特征图中连续重采样 task-aware tokens。来源：[[raw/2605_11817_GridS.pdf]]，Abstract、Figure 2、Figure 3。
- 效率证据命题：论文报告使用少于 10% 原始视觉 tokens、约 76% FLOPs reduction，并展示 real-world latency / OOD result headline。来源：[[raw/2605_11817_GridS.pdf]]，Abstract、Figure 1。
- 适用范围证据命题：论文在 π0、π0.5、SmolVLA 以及 LIBERO、ALOHA、real robot、RoboTwin 等设置中验证。来源：[[raw/2605_11817_GridS.pdf]]，Abstract、experiment sections。

## Table / Metric Anchors
- **Figure 1**：headline performance and efficiency。
- **Figure 2**：discrete selection vs grid sampling。
- **Figure 3**：GridS framework。

## Table / Metric Split
- token retention、FLOPs、latency 与 success / OOD result 必须分开写。
- plug-and-play 需要回到已验证 backbone 和 benchmark。

## 不可混写项
- 不应写成 temporal cache。
- 不应把 continuous resampling 简化为普通 hard pruning。

## 影响页面
- [[wiki/papers/2605_11817_GridS.md|2605_11817_GridS]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
