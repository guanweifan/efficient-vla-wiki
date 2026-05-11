# 2604_24622_CF-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_24622_CF-VLA.md|2604_24622_CF-VLA]] 的单篇证据落点，用来拆分 coarse-to-fine action generation、low-NFE sampling、latency-performance headline。
- 本页聚焦的 headline bundle：`NFE=2`、`AP-guided initialization`、`single-step refinement`、`75.4% latency reduction`、`83.0% real-robot success` 需要分层阅读。

## Evidence
- 核心证据命题：CF-VLA 用 coarse initialization 构造 AP-guided noise initialization，再用 single-step refinement 生成最终动作；这不同于从 Gaussian noise 多步迭代恢复 action structure。来源：[[raw/2604_24622_CF-VLA.pdf]]，Abstract、Figure 1、Figure 2。
- 训练机制命题：stepwise strategy 先训练 controlled coarse predictor 与 refinement proxy，再进行 full joint optimization，以稳定 coarse/fine 耦合。来源：[[raw/2604_24622_CF-VLA.pdf]]，Figure 2、Algorithm 1、method section。
- 结果证据命题：论文在 LIBERO、CALVIN 和 real-robot settings 中报告低 NFE operating point；Figure 4 把 action sampling latency 从 29.17 ms 到 7.81 ms 的对比作为 latency-performance anchor。来源：[[raw/2604_24622_CF-VLA.pdf]]，Table 1、Table 2、Figure 4、Figure 5。

## Table / Metric Anchors
- **Figure 1**：coarse-to-fine teaser 与 sampling latency headline。
- **Figure 2 / Algorithm 1**：training and inference procedure。
- **Table 1 / Table 2**：LIBERO / CALVIN comparison。
- **Table 3 / Table 4**：component ablations。
- **Figure 4**：latency-performance frontier。
- **Figure 5**：real-robot results。

## Table / Metric Split
- NFE 是 action-generation function evaluation budget，不等同于完整 control-loop latency。
- latency reduction 与 task success 属于不同口径，需要 paired operating point 才能比较。
- coarse stage、fine stage、Phase I、Phase II 各自承担不同功能，不能只写成“少一步采样”。

## 不可混写项
- 不应把 CF-VLA 写成 training-efficiency method；stepwise training 是稳定机制，效率收益主要来自 action generation。
- 不应把 low-NFE 成功写成任意 diffusion/flow policy 都可直接 NFE=2。
- 不应把 real-robot success 与 LIBERO latency 合并成同一 headline。

## 影响页面
- [[wiki/papers/2604_24622_CF-VLA.md|2604_24622_CF-VLA]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
