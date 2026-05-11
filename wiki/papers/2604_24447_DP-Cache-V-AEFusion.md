# 2604_24447_DP-Cache-V-AEFusion

## Source
- Raw: [[raw/2604_24447_DP-Cache-V-AEFusion.pdf]]
- Extracts manifest: [[extracts/parses/2604_24447_DP-Cache-V-AEFusion/manifest.json]]
- Primary text fallback: [[extracts/parses/2604_24447_DP-Cache-V-AEFusion/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **model-hardware co-characterization / on-robot VLA deployment acceleration** 论文；它同时给出 VLA-XPU leaderboard、two-phase profiling，以及 DP-Cache / V-AEFusion 两个训练无关加速机制。
- 论文先用 CET（Cost, Energy, Time）视角评估 VLA model-hardware pairs，强调 right-sized edge accelerators 在成本/能耗/控制频率约束下可能优于旗舰 GPU。来源：[[raw/2604_24447_DP-Cache-V-AEFusion.pdf]]，Abstract、Section 3、Figure 2、Figure 4。
- profiling 发现 VLA inference 存在 compute-bound VLM backbone 与 memory-bound Action Expert 的 two-phase pattern；这解释了同一硬件在不同阶段的利用率不均。来源：[[raw/2604_24447_DP-Cache-V-AEFusion.pdf]]，Abstract、Figure 5、Figure 6。
- DP-Cache 跳过 / 缓存 diffusion process 中冗余 intermediate steps；V-AEFusion 利用 VLM backbone 与 Action Expert 的 latency ratio 做 pipeline parallelism。来源：[[raw/2604_24447_DP-Cache-V-AEFusion.pdf]]，Figure 7、Figure 9、Table 4、Table 8。
- 更稳的主张是：这篇论文属于 deployment-oriented efficiency 主线，同时为 action-generation sampling redundancy 提供 DP-Cache 这个 secondary evidence。

## Methodology Index
- VLA-XPU leaderboard
- model-hardware co-characterization
- CET: Cost / Energy / Time
- control-rate feasibility
- VLM backbone profiling
- Action Expert profiling
- compute-bound / memory-bound phase split
- DP-Cache
- V-AEFusion
- pipeline parallelism
- edge GPU / XPU / NPU deployment

## Data Pointer
- **Abstract / Section 3**：leaderboard、CET 与 right-sized accelerator framing。
- **Figure 2 / Figure 4**：control-rate feasibility 与 CET hardware selection。
- **Figure 5 / Figure 6**：VLM backbone / Action Expert profiling 与 roofline analysis。
- **Figure 7 / Table 4**：DP-Cache mechanism 与 latency/capability trade-off。
- **Figure 9 / Table 8 / Table 9**：V-AEFusion pipeline parallelism 与 cross-platform comparison。
- **Table 10**：hardware specification。

## Evidence Links
- [[wiki/evidence/claims/2604_24447_DP-Cache-V-AEFusion-headline-split.md|2604_24447_DP-Cache-V-AEFusion-headline-split]]

## 待核点
- DP-Cache / V-AEFusion 是训练无关推理优化，但其 speedup 和 success degradation 依赖具体模型、硬件和 cache/stale-step 配置。
- VLA-XPU leaderboard 属于 deployment analysis；不能直接替代 robot task success comparison。
- 该论文同时影响 deployment 和 inference/action-generation 路线；当前主落点是 deployment-oriented efficiency。
