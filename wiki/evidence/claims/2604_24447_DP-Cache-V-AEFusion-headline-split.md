# 2604_24447_DP-Cache-V-AEFusion-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_24447_DP-Cache-V-AEFusion.md|2604_24447_DP-Cache-V-AEFusion]] 的单篇证据落点，用来拆分 VLA-XPU leaderboard、two-phase profiling、DP-Cache 与 V-AEFusion headline。
- 本页聚焦的 headline bundle：`CET leaderboard`、`compute-bound VLM / memory-bound Action Expert`、`DP-Cache`、`V-AEFusion`、`up to 2.9x / 6x speedup` 需要分层阅读。

## Evidence
- 核心证据命题：论文通过 heterogeneous accelerators 上的 VLA-XPU leaderboard，把 latency/control rate、cost 和 energy 一起作为 on-robot deployment 选择指标。来源：[[raw/2604_24447_DP-Cache-V-AEFusion.pdf]]，Abstract、Section 3、Figure 2、Figure 4。
- profiling 命题：论文报告 mainstream VLA pipeline 中 VLM backbone 主要 compute-bound，而 Action Expert 主要 memory-bound，导致 phase-dependent hardware underutilization。来源：[[raw/2604_24447_DP-Cache-V-AEFusion.pdf]]，Abstract、Figure 5、Figure 6。
- 加速机制命题：DP-Cache 作用于 diffusion action expert 的冗余 denoising steps；V-AEFusion 作用于 VLM backbone 与 Action Expert 的 pipeline-level serialization。来源：[[raw/2604_24447_DP-Cache-V-AEFusion.pdf]]，Figure 7、Figure 9、Table 4、Table 8。

## Table / Metric Anchors
- **Table 1 / Figure 2 / Figure 4**：leaderboard 与 CET hardware selection。
- **Figure 5 / Figure 6**：profiling and roofline analysis。
- **Figure 7 / Table 4**：DP-Cache。
- **Figure 9 / Table 8 / Table 9**：V-AEFusion。
- **Table 10**：tested hardware specifications。

## Table / Metric Split
- `2.9x`、`6x`、`1.3x` 等 speedup 口径依赖具体优化组合、模型和硬件平台。
- control-rate feasibility、energy、cost 与 success rate 是不同轴。
- DP-Cache 是 action expert 内部 redundancy reduction；V-AEFusion 是 pipeline overlap；两者不能混成同一机制。

## 不可混写项
- 不应把 leaderboard 推荐写成单一最优硬件结论；CET priority 不同，推荐不同。
- 不应把 DP-Cache 的 denoising-step cache 写成 temporal visual token cache。
- 不应把 deployment profiling 直接写成训练效率结论。

## 影响页面
- [[wiki/papers/2604_24447_DP-Cache-V-AEFusion.md|2604_24447_DP-Cache-V-AEFusion]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
