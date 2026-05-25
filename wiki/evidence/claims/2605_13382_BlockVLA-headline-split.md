# 2605_13382_BlockVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_13382_BlockVLA.md|2605_13382_BlockVLA]] 的单篇证据落点，用来拆分 block diffusion、prefix KV-cache reuse、training convergence 与 inference acceleration。

## Evidence
- 核心证据命题：BlockVLA 保留 block 间 AR dependency，并在 block 内做并行 denoising；已完成 block 的 prefix KV-cache 可被复用。来源：[[raw/2605_13382_BlockVLA.pdf]]，Abstract、Table 1。
- 结果证据命题：论文在 LIBERO 和 SimplerEnv 上报告任务表现，并声称相对标准 discrete diffusion VLA 有 3.3x inference acceleration。来源：[[raw/2605_13382_BlockVLA.pdf]]，Abstract、Figure 1。
- 训练证据命题：论文把 block diffusion 作为从 AR backbone 到 diffusion fine-tuning 的更平滑转换，并报告训练效率 / 收敛改善。来源：[[raw/2605_13382_BlockVLA.pdf]]，Figure 1、method / experiment sections。

## Table / Metric Anchors
- **Figure 1**：training efficiency and inference throughput。
- **Table 1**：AR / discrete diffusion / block diffusion comparison。

## Table / Metric Split
- inference throughput、training convergence 与 success rate 不能合并。
- prefix KV-cache reuse 属于 action block generation。

## 不可混写项
- 不应写成 perception cache。
- 不应把 3.3x acceleration 外推到所有 diffusion VLA。

## 影响页面
- [[wiki/papers/2605_13382_BlockVLA.md|2605_13382_BlockVLA]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
