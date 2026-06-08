# 2605_29438_ElegantVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_29438_ElegantVLA.md|2605_29438_ElegantVLA]] 的单篇证据落点，用来拆分 phase-adaptive compute scheduling、cross-module temporal reuse、scheduler RL training 与 frequency / latency headline。
- 本页聚焦的 headline bundle：`learn when to think`、`Vision-LLM five-level compute mode`、`action-head three-level denoising mode`、`2.18x real-world FLOPs speedup / 26.3 Hz` 需要分层阅读。

## Evidence
- 方法证据命题：ElegantVLA uses a lightweight scheduler to allocate computation across vision encoder, LLM and action head based on representation similarity, robot motion cues and episode progress. 来源：[[raw/2605_29438_ElegantVLA.pdf]]，Abstract、Figure 1、Figure 2、method section。
- 训练机制命题：scheduler is trained as a sequential decision problem with two-stage RL while the base VLA stays frozen; this is not the same as fixed-rule pruning. 来源：[[raw/2605_29438_ElegantVLA.pdf]]，method section、Table 6、Table 12。
- 结果证据命题：simulation and real-world results report success / speedup, frequency / latency and per-step wall-clock breakdown, which need separate口径. 来源：[[raw/2605_29438_ElegantVLA.pdf]]，Table 2、Table 3、Table 4、Table 9。

## Table / Metric Anchors
- **Figure 1**：temporal variation in inference demand。
- **Figure 2**：framework overview。
- **Table 2**：GR00T / SIMPLER success-speedup results。
- **Table 3**：Franka real-world success-speedup results。
- **Table 4**：latency and control frequency on GR00T。
- **Table 9**：real-world latency breakdown。
- **Figure 11**：scheduler diagnostic。
- **Table 12 / Table 13**：scheduler and signal ablations。

## Table / Metric Split
- FLOPs speedup, wall-clock speedup and control frequency are distinct but related deployment/inference口径.
- scheduler training cost and frozen-base inference acceleration should be separated.
- `think` here means compute allocation / recomputation, not necessarily textual reasoning.

## 不可混写项
- 不应把 ElegantVLA 写成 no-training plug-and-play pruning; scheduler is learned.
- 不应 merge GR00T, CogACT and Franka results into a single benchmark average.
- 不应 equate temporal reuse with cache reuse without noting phase-adaptive scheduler.

## 影响页面
- [[wiki/papers/2605_29438_ElegantVLA.md|2605_29438_ElegantVLA]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
