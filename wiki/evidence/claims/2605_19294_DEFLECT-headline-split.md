# 2605_19294_DEFLECT-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_19294_DEFLECT.md|2605_19294_DEFLECT]] 的单篇证据落点，用来拆分 stale action delay、offline preference tuning、no-extra-inference-cost 与 multi-setting delay robustness。

## Evidence
- 核心证据命题：DEFLECT 从 frozen reference model 构造 fresh / stale counterfactual action pairs，并用 flow-matching likelihood-ratio surrogate 形成 label-free preference signal。来源：[[raw/2605_19294_DEFLECT.pdf]]，Abstract、Figure 3、Algorithm 1。
- delay 证据命题：论文把 async inference 的 prediction-execution mismatch 作为 stale action 问题，并报告 naive async 在 Kinetix delay 下退化。来源：[[raw/2605_19294_DEFLECT.pdf]]，Abstract、Figure 2、Figure 4、Table 1。
- 结果证据命题：论文在 Kinetix、LIBERO / real-scale VLA 与真实机器人任务中报告 delay robustness gains，并声明不增加额外 inference cost。来源：[[raw/2605_19294_DEFLECT.pdf]]，Abstract、Figures 4-5、Tables 4-6。

## Table / Metric Anchors
- **Figures 1-3 / Algorithm 1**：problem and method。
- **Figure 4 / Table 1**：Kinetix delay robustness。
- **Figure 5 / Tables 4-6**：real robot, LIBERO, uncertainty。

## Table / Metric Split
- delay robustness、offline tuning cost 和 inference-time cost 必须分层。
- fresh/stale pair 是 latency-derived surrogate，不是人工偏好。

## 不可混写项
- 不应写成 denoising step reduction。
- 不应写成 online rollout RL。

## 影响页面
- [[wiki/papers/2605_19294_DEFLECT.md|2605_19294_DEFLECT]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
