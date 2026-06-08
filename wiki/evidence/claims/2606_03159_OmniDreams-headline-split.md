# 2606_03159_OmniDreams-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2606_03159_OmniDreams.md|2606_03159_OmniDreams]] 的单篇证据落点，用来拆分 real-time generative world model、closed-loop AV simulation、inference serving optimization 与 WAM boundary。
- 本页聚焦的 headline bundle：`real-time action-conditioned video generation`、`closed-loop AlpaSim integration`、`multi-GPU GB300 timings`、`OmniDreams as WAM boundary` 需要分层阅读。

## Evidence
- 方法证据命题：OmniDreams autoregressively generates action-conditioned sensor videos from past frames, simulator state and immediate driving actions, for closed-loop AV simulation. 来源：[[raw/2606_03159_OmniDreams.pdf]]，Abstract、Figure 1、Figure 3。
- 系统证据命题：training-free inference optimization, multi-GPU inference, streaming KV cache and FlashDreams serving infra support the real-time simulator path. 来源：[[raw/2606_03159_OmniDreams.pdf]]，Contents、Table 2、Table 3、Figure 6。
- 边界证据命题：post-training OmniDreams as a WAM is a separate section and preliminary policy-architecture evidence; it should not replace the paper's main simulator contribution. 来源：[[raw/2606_03159_OmniDreams.pdf]]，Abstract、Section 7、Figure 13。

## Table / Metric Anchors
- **Figure 1**：closed-loop simulation workflow。
- **Table 1**：training dataset summary。
- **Figure 3 / Figure 4 / Figure 5**：conditioning and autoregressive multi-view generation。
- **Table 2 / Table 3**：per-chunk inference timings on NVIDIA GB300。
- **Figure 6**：end-to-end inference pipeline and KV-cache update path。
- **Table 4 / Table 5 / Table 6**：quality / latency / long-rollout tradeoffs。
- **Figure 13 / Figure 14**：closed-loop policy ranking preservation and visual realism。

## Table / Metric Split
- real-time sensor generation, closed-loop evaluation fidelity and WAM policy performance are separate claims.
- single-view / four-view timing depends on chunk size, camera count and GPU count.
- simulator quality metrics and policy incident metrics should not be collapsed into task success.

## 不可混写项
- 不应把 OmniDreams 写成 manipulation VLA acceleration method。
- 不应 compare GB300 simulator FPS directly with robot control Hz。
- 不应 treat WAM post-training result as the main evidence for VLA efficiency.

## 影响页面
- [[wiki/papers/2606_03159_OmniDreams.md|2606_03159_OmniDreams]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
