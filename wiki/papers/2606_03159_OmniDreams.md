# 2606_03159_OmniDreams

## Source
- Raw: [[raw/2606_03159_OmniDreams.pdf]]
- Extracts manifest: [[extracts/parses/2606_03159_OmniDreams/manifest.json]]
- Primary text fallback: [[extracts/parses/2606_03159_OmniDreams/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **real-time generative world model for closed-loop AV simulation** 论文；它靠近 efficient VLA 的边界在 real-time world model serving、closed-loop simulation integration 与 WAM post-training，而不是 manipulation VLA inference route。
- OmniDreams 从 Cosmos diffusion model mid/post-train 出 action-conditioned autoregressive video generator，条件包括 past frames、simulator state 与 immediate driving actions，用于闭环自动驾驶仿真。来源：[[raw/2606_03159_OmniDreams.pdf]]，Abstract、Figure 1、Figure 3。
- 论文包含 training-free inference optimization、multi-GPU inference、streaming KV cache、FlashDreams serving infra 与 AlpaSim closed-loop integration，用来支撑 real-time sensor generation。来源：[[raw/2606_03159_OmniDreams.pdf]]，Contents、Table 2、Table 3、Figure 6。
- WAM 相关部分应作为边界证据：论文展示 post-training OmniDreams as a World-Action Model，并报告其在 Physical AI NuRec dataset 上的初步 policy performance；这不能直接等同于通用 VLA policy compression。来源：[[raw/2606_03159_OmniDreams.pdf]]，Abstract、Section 7、Figure 13。

## Methodology Index
- generative world model
- closed-loop autonomous vehicle simulation
- action-conditioned video generation
- autoregressive generation
- streaming KV cache
- multi-view DiT
- multi-GPU inference
- FlashDreams serving infra
- AlpaSim integration
- WAM post-training boundary

## Data Pointer
- **Abstract / Figure 1**：closed-loop simulation workflow and policy-environment interaction。
- **Table 1**：OmniDreams training dataset summary。
- **Figure 3 / Figure 4 / Figure 5**：conditioning, multi-view architecture and autoregressive generation。
- **Table 2 / Table 3**：single-view and four-view per-chunk inference timings on NVIDIA GB300。
- **Figure 6**：end-to-end inference pipeline and KV-cache maintenance。
- **Table 4 / Table 5 / Table 6**：training-stage, decoder latency-quality and long-rollout quality tradeoffs。
- **Figure 13 / Figure 14**：closed-loop policy evaluation proxy and visual realism comparison。

## Evidence Links
- [[wiki/evidence/claims/2606_03159_OmniDreams-headline-split.md|2606_03159_OmniDreams-headline-split]]

## 待核点
- OmniDreams 属于 AV closed-loop simulation / world model infrastructure；不能直接并入 manipulation VLA acceleration 主比较。
- `real-time` 绑定 NVIDIA GB300、chunk size、camera count 和 serving path；需要保留 hardware / pipeline layer。
- WAM post-training result 是 preliminary / boundary evidence，应和主 simulator 贡献分开读。
