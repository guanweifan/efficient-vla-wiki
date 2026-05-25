# 2605_16154_PCM-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_16154_PCM.md|2605_16154_PCM]] 的单篇证据落点，用来拆分 GRPO training cost、gradient chunk masking、wall-clock speedup 与 activation memory。

## Evidence
- 核心证据命题：PCM 用 success-failure action variance 估计 phase-level gradient variance，并在 actor update 中只对部分 trajectory chunks 做 backprop。来源：[[raw/2605_16154_PCM.pdf]]，Abstract、Figure 1、Figure 2、Algorithm 1。
- 成本证据命题：论文指出 gradient compute 约占 step wall-clock 的主要部分，并报告 wall-clock、gradient update 与 peak activation memory 改善。来源：[[raw/2605_16154_PCM.pdf]]，Abstract、Figure 1、Figure 4。
- 结果证据命题：论文在 LIBERO 上报告 convergence / time-to-target success 与 phase-wise allocation。来源：[[raw/2605_16154_PCM.pdf]]，Figure 3、Table 1、Figures 5-6。

## Table / Metric Anchors
- **Figures 1-2 / Algorithm 1**：cost analysis and PCM。
- **Figure 3 / Table 1**：convergence and time-to-target。
- **Figures 4-6**：efficiency, ablation, phase allocation。

## Table / Metric Split
- wall-clock speedup、gradient-update speedup、activation memory 和 success rate 是不同口径。
- chunk masking 是训练梯度选择，不是 inference action skipping。

## 不可混写项
- 不应写成 reward-model / critic method。
- 不应写成部署时降低 action horizon。

## 影响页面
- [[wiki/papers/2605_16154_PCM.md|2605_16154_PCM]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
