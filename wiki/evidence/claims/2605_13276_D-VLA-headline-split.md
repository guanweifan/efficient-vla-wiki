# 2605_13276_D-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_13276_D-VLA.md|2605_13276_D-VLA]] 的单篇证据落点，用来拆分 distributed RL training throughput、asynchronous pipeline、VRAM / topology system knobs。

## Evidence
- 核心证据命题：D-VLA 通过 Plane Decoupling 与四线程 Swimlane pipeline 重叠 rollout、inference、gradient computation 与 parameter distribution。来源：[[raw/2605_13276_D-VLA.pdf]]，Abstract、Figure 2。
- 系统证据命题：论文引入 dual-pool VRAM management 与 topology-aware replication，用于多节点训练吞吐和资源利用。来源：[[raw/2605_13276_D-VLA.pdf]]，Abstract、Figure 3。
- 结果证据命题：论文在 π0.5 / OpenVLA-OFT setting 中报告 throughput、training success 与 scaling。来源：[[raw/2605_13276_D-VLA.pdf]]，Table 1、Figures 4-7。

## Table / Metric Anchors
- **Figure 1-3**：placement, training architecture, communication。
- **Table 1**：throughput comparison。
- **Figures 4-7**：benchmarking, success rate, scaling。

## Table / Metric Split
- training throughput、VRAM management、success rate 和 scaling 是不同训练系统口径。
- asynchronous inference 在这里属于训练流水线组件，不是部署时控制策略。

## 不可混写项
- 不应写成 deployment-time async VLA。
- 不应把多 GPU throughput 当成单步模型 latency。

## 影响页面
- [[wiki/papers/2605_13276_D-VLA.md|2605_13276_D-VLA]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
