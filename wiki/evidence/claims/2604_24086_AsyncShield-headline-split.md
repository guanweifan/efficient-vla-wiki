# 2604_24086_AsyncShield-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_24086_AsyncShield.md|2604_24086_AsyncShield]] 的单篇证据落点，用来拆分 cloud VLA latency、spatial re-projection、CMDP safety adapter 与 plug-and-play headline。
- 本页聚焦的 headline bundle：`Latency is Geometry`、`plug-and-play edge adapter`、`no cloud VLA fine-tuning`、`success/safety under jitter` 需要分层阅读。

## Evidence
- 核心证据命题：AsyncShield 维护 temporal pose buffer，并用 analytical SE(2) transform 把 delayed VLA waypoints realign 到当前 ego frame。来源：[[raw/2604_24086_AsyncShield.pdf]]，Abstract、Figure 1、Section III-A。
- 安全机制命题：edge adapter 被建模为 CMDP，并通过 PPO-Lagrangian 在 VLA intent tracking 和 LiDAR obstacle avoidance constraints 之间权衡。来源：[[raw/2604_24086_AsyncShield.pdf]]，Abstract、Figure 1、Section III-B。
- 结果证据命题：论文在 injected stochastic latency / mixed degradation 与 real-world jitter setting 下报告 simulation 和 real-world success/safety results，并强调不 fine-tune cloud-based foundation models。来源：[[raw/2604_24086_AsyncShield.pdf]]，Table I、Table II、Table IV、Conclusion。

## Table / Metric Anchors
- **Figure 1**：framework overview。
- **Figure 2**：trajectory qualitative comparison under Mixed Degradation。
- **Table I**：simulation performance under asynchronous control。
- **Table II / Table III**：ablation and safety adapter component analysis。
- **Table IV**：real-world success rates across cloud VLA models。

## Table / Metric Split
- success rate、risk/safety metric、time-to-goal 是不同口径，不应合并。
- delayed waypoint correction 属于 cloud-edge deployment/control loop，不是 VLA backbone 压缩。
- no fine-tuning 指 cloud-based foundation model 不被 fine-tune，不等于 edge adapter 没有训练。

## 不可混写项
- 不应把 AsyncShield 写成 visual token efficiency。
- 不应把 navigation 下的 cloud-edge delay 结果外推到 fixed-base manipulation。
- 不应把 plug-and-play 写成无条件模型无关；它依赖 standardized waypoint/sub-goal interface。

## 影响页面
- [[wiki/papers/2604_24086_AsyncShield.md|2604_24086_AsyncShield]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
