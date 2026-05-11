# 2604_24086_AsyncShield

## Source
- Raw: [[raw/2604_24086_AsyncShield.pdf]]
- Extracts manifest: [[extracts/parses/2604_24086_AsyncShield/manifest.json]]
- Primary text fallback: [[extracts/parses/2604_24086_AsyncShield/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **cloud-edge asynchronous VLA navigation / edge safety adapter** 论文；它把 cloud VLA latency 和 network jitter 写成部署侧核心问题。
- AsyncShield 的核心机制是 edge-side temporal pose buffer + SE(2) geometric re-projection，把 delayed cloud VLA waypoints 从历史 ego frame 对齐到当前 ego frame。来源：[[raw/2604_24086_AsyncShield.pdf]]，Abstract、Introduction、Figure 1、method section。
- 为了在 intent restoration 和 physical safety 之间折中，论文把 edge adaptation 表述为 CMDP，并用 PPO-Lagrangian adapter 在 tracking VLA intent 与 high-frequency LiDAR obstacle avoidance constraints 之间做动态权衡。来源：[[raw/2604_24086_AsyncShield.pdf]]，Abstract、Figure 1、method section。
- headline 结果需要拆开理解：
  - 主要场景是 asynchronous cloud-based VLA navigation；
  - plug-and-play 指不 fine-tune cloud-based foundation model，并通过 standardized sub-goal interface 适配不同 cloud VLA / chassis；
  - success rate / safety improvement 依赖 simulation degradation 与 real-world network jitter setting。
- 更稳的主张是：AsyncShield 是 deployment-oriented efficiency 的云边协同边界案例，重点不是压缩 VLA 参数，而是修复 latency-induced spatial misalignment 和安全执行闭环。

## Methodology Index
- cloud-based VLA navigation
- asynchronous control
- temporal pose buffer
- SE(2) geometric re-projection
- stale waypoint realignment
- CMDP
- PPO-Lagrangian
- LiDAR safety constraints
- universal local sub-goal
- network jitter / latency degradation

## Data Pointer
- **Abstract / Introduction**：主 framing，说明 cloud-to-edge latency 与 stale intent misalignment。
- **Figure 1**：AsyncShield pipeline 与 edge adaptation 主锚点。
- **Method section III-A / III-B**：temporal pose buffer、SE(2) re-projection 与 CMDP adapter。
- **Figure 2**：Mixed Degradation network condition 下的 qualitative trajectory comparison。
- **Table I**：simulation under network degradation 的主结果。
- **Table II / Table III**：ablation 与 adapter component 分析。
- **Table IV**：real-world cloud VLA compatibility / success rates。

## Evidence Links
- [[wiki/evidence/claims/2604_24086_AsyncShield-headline-split.md|2604_24086_AsyncShield-headline-split]]

## 待核点
- AsyncShield 的任务域是 mobile navigation / VLN，不应直接和 manipulation VLA 的 action generation latency 并表。
- “plug-and-play” 当前指不改 cloud VLA 权重与标准化 sub-goal interface；不能写成任意 cloud model / 任意机器人均已验证。
- 该论文更适合 deployment/system 路线；如放入 inference 页，应保留 network jitter 与 edge safety adapter 边界。
