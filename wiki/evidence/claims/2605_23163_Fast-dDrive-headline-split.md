# 2605_23163_Fast-dDrive-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_23163_Fast-dDrive.md|2605_23163_Fast-dDrive]] 的单篇证据落点，用来拆分 driving VLA structured output、block diffusion、scaffold speculative decoding 与 serving throughput。

## Evidence
- 核心证据命题：Fast-dDrive 将自动驾驶 VLA 的 JSON-like structured output 切成 section-aligned block diffusion，并用 frozen scaffold tokens 保持结构。来源：[[raw/2605_23163_Fast-dDrive.pdf]]，Figure 1、Figure 2、Table 1。
- 推理证据命题：Scaffold Speculative Decoding 与 shared-prefix multi-trajectory rollout 用于并行生成和复用共同前缀。来源：[[raw/2605_23163_Fast-dDrive.pdf]]，Figure 3、Figure 4。
- 结果证据命题：论文在 WOD-E2E、nuScenes 与 SGLang serving setting 中报告 accuracy / trajectory metrics 和 throughput speedup。来源：[[raw/2605_23163_Fast-dDrive.pdf]]，Tables 2-4。

## Table / Metric Anchors
- **Figure 1-4 / Table 1**：method and output structure。
- **Tables 2-4**：driving benchmarks and inference efficiency。
- **Table 5 / Figures 5-9**：SASD ablation and qualitative examples。

## Table / Metric Split
- driving trajectory quality、serving throughput 与 structured-output ablation 不能合并。
- KV cache / shared prefix 属于 trajectory-output serving，不是 perception cache。

## 不可混写项
- 不应直接与 manipulation VLA action chunk results 并表。
- 不应把 SGLang serving throughput 写成机器人控制频率。

## 影响页面
- [[wiki/papers/2605_23163_Fast-dDrive.md|2605_23163_Fast-dDrive]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
