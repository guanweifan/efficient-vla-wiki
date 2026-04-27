# 2604_19730_FASTER-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_19730_FASTER.md|2604_19730_FASTER]] 的单篇证据落点，用来拆分 value-guided sampling、best-of-N compute reduction 与 VLA-adjacent 边界。
- 本页聚焦的 headline bundle：`best-of-N benefits`、`4.5x update speedup`、`1.7x inference speedup`、`8x FLOP reduction` 不能被写成一般 VLA 推理加速结论。

## Evidence
- 核心证据命题：FASTER 试图保留 best-of-N / test-time sampling 的收益，但避免完整 denoise 所有候选；它用 denoise critic 在早期候选状态上评分，并只 denoise 最终选中的候选。来源：[[raw/2604_19730_FASTER.pdf]]，Abstract、Figure 1、Algorithm 2。
- 方法证据命题：论文将 candidate filtering 建模为 denoising MDP；实践中常用 initial-noise filtering，将选择问题简化为 `argmax_i Qdn(s, eps_i)`，再只 denoise被选中的 `eps_i`。来源：[[raw/2604_19730_FASTER.pdf]]，Section 4、Algorithm 1-2。
- 结果证据命题：在 FASTER-EXPO / pi0.5 LIBERO 相关设置中，论文报告 update time 从约 `11.6s` 降到 `2.5s`，inference latency 从 `566ms` 降到 `335ms`，inference FLOPs 从 `3.75e13` 降到 `4.70e12`。来源：[[raw/2604_19730_FASTER.pdf]]，Figure 6、compute savings section。

## Table / Metric Anchors
- **Figure 1**：best-of-N denoise-all 与 FASTER early filtering 的结构对比。
- **Algorithm 1 / Algorithm 2**：training / inference procedure。
- **Figure 3-5**：Robomimic / LIBERO success and compute comparisons。
- **Figure 6**：training and inference timing / FLOP comparison。
- **Figure 7**：FASTER-EXPO vs EXPO on pi0.5 task suite。

## Table / Metric Split
- `4.5x` update speedup 属于训练/online update compute 口径。
- `1.7x` inference latency speedup 属于 per-action inference timing 口径。
- `8x` FLOP reduction 属于 model compute 口径，不等同于 wall-clock speedup。
- VLA relevance 来自 pretrained VLA / LIBERO setting；方法本身仍是 general RL / diffusion-policy candidate filtering。

## 不可混写项
- 不应把该论文与 [[wiki/papers/2603_19199_FASTER.md|2603_19199_FASTER]] 混为同一篇。
- 不应把 general RL diffusion-policy 结果直接写成 VLA-specific architecture claim。
- 不应把 best-of-N sampling benefit 与 compute reduction 写成无代价收益；需要保留 denoise critic 与 filtering policy 的训练依赖。

## 影响页面
- [[wiki/papers/2604_19730_FASTER.md|2604_19730_FASTER]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
