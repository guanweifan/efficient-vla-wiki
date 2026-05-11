# 2605_01194_VLA-ATTC-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_01194_VLA-ATTC.md|2605_01194_VLA-ATTC]] 的单篇证据落点，用来拆分 adaptive TTC、cognitive clutch、RAC pairwise selection 与 control-frequency headline。
- 本页聚焦的 headline bundle：`adaptive test-time compute`、`uncertainty-based cognitive clutch`、`Relative Action Critic`、`failure rate reduction`、`20.8 Hz control frequency` 需要分层阅读。

## Evidence
- 核心证据命题：VLA-ATTC 用 uncertainty score 触发 cognitive clutch，在高不确定状态进入 TTC deliberation，否则继续 reflexive execution。来源：[[raw/2605_01194_VLA-ATTC.pdf]]，Abstract、Algorithm 1、Figure 3。
- RAC 机制命题：Relative Action Critic 对 action candidates 做 pairwise preference comparison，避免绝对 action score 的不稳定估计。来源：[[raw/2605_01194_VLA-ATTC.pdf]]，Abstract、Figure 4、method section。
- 结果证据命题：论文在 LIBERO-LONG、real-world Piper tasks 与 control-frequency 表中分别报告 task improvement 和 execution overhead。来源：[[raw/2605_01194_VLA-ATTC.pdf]]，Table 1、Table 2、Table 5。

## Table / Metric Anchors
- **Figure 1 / Figure 2**：overall motivation and inference paradigm comparison。
- **Algorithm 1 / Figure 3**：adaptive TTC inference。
- **Figure 4**：RAC architecture。
- **Table 1**：LIBERO-LONG success rates。
- **Table 2**：real-world task success rates。
- **Table 3 / Table 4**：threshold and candidate ablations。
- **Table 5**：control frequency。

## Table / Metric Split
- failure-rate reduction、success rate、control frequency 是不同口径。
- Full VLA-ATTC 与 cognitive-clutch version 的成本边界不同。
- candidate sampling count 影响 performance 与 overhead，不能脱离 threshold 配置读。

## 不可混写项
- 不应把 VLA-ATTC 写成 action denoising-step reduction。
- 不应把 RAC pairwise selection 写成 language CoT。
- 不应把 adaptive TTC 写成 always-on parallel deliberation。

## 影响页面
- [[wiki/papers/2605_01194_VLA-ATTC.md|2605_01194_VLA-ATTC]]
- [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
