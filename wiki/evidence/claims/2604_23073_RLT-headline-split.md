# 2604_23073_RLT-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_23073_RLT.md|2604_23073_RLT]] 的单篇证据落点，用来拆分 RL token、online actor-critic adaptation、critical-phase success / speed headline。
- 本页聚焦的 headline bundle：`RL token`、`sample-efficient online RL`、`few hours / minutes`、`up to 3x speedup` 与 `real-robot precision tasks` 需要分层阅读。

## Evidence
- 核心证据命题：RLT 让 pretrained VLA 暴露 compact RL token，并用该 token 训练轻量 actor-critic；actor 还被 reference action chunk conditioning 与 regularizer 锚定到 VLA 行为附近。来源：[[raw/2604_23073_RLT.pdf]]，Abstract、Figure 1、Figure 2、method section。
- 实验设定命题：论文在 screw installation、zip tie fastening、Ethernet insertion、charger insertion 四类 real-robot precision tasks 上评估，并重点隔离 critical phase。来源：[[raw/2604_23073_RLT.pdf]]，Figure 3、experiment section。
- 结果证据命题：论文报告 RLT 在 critical phases 同时提升 throughput/speed 和 success rate，并在 abstract 中给出 `up to 3x` 的 speed headline。来源：[[raw/2604_23073_RLT.pdf]]，Abstract、Figure 4、Figure 5。

## Table / Metric Anchors
- **Figure 1**：RLT system overview。
- **Figure 2**：RL token extraction details。
- **Figure 3**：real-robot task definitions。
- **Figure 4 / Figure 5**：critical-phase throughput 与 success rate。
- **Figure 6**：RL baseline comparison。
- **Figure 7-9**：ablation、learning curve 与 speed distribution。

## Table / Metric Split
- `3x` 是 critical-phase execution speed / throughput 口径，不等同于 VLA forward-pass latency。
- success rate 与 speed 是两类结果，需要分开读。
- `few minutes / few hours` 是 online robot practice 口径，不等同于 full VLA retraining cost。

## 不可混写项
- 不应把 RL token 写成 visual token pruning。
- 不应把 RLT 写成减少 diffusion denoising steps 或 action tokenizer 长度。
- 不应把 critical-phase 结果直接外推为完整任务端到端吞吐。

## 影响页面
- [[wiki/papers/2604_23073_RLT.md|2604_23073_RLT]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
