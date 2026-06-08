# 2605_25477_EXPO-FT-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_25477_EXPO-FT.md|2605_25477_EXPO-FT]] 的单篇证据落点，用来拆分 online RL fine-tuning、human intervention、online data minutes 与 real-world success headline。
- 本页聚焦的 headline bundle：`sample-efficient RL finetuning`、`19.1 minutes online robot data`、`30/30 successes`、`human-in-the-loop feedback` 需要分层阅读。

## Evidence
- 方法证据命题：EXPO-FT 在 pretrained π0.5 VLA 上做 RL fine-tuning，并扩展到 temporally extended actions；human-in-the-loop feedback 被用于在线训练中的 targeted interventions。来源：[[raw/2605_25477_EXPO-FT.pdf]]，Abstract、Introduction、Figure 2。
- 结果证据命题：论文报告八个真实 manipulation tasks，在平均 19.1 minutes online robot data 内达到 `30/30` successes；这一结果与 Figure 4 / Table 2 的 task-wise training success and intervention rates 对应。来源：[[raw/2605_25477_EXPO-FT.pdf]]，Abstract、Figure 4、Table 2。
- 路线证据命题：本篇效率收益落在 training / adaptation side，尤其是 online robot data efficiency and fine-tuning reliability，而不是 per-step inference latency。来源：[[raw/2605_25477_EXPO-FT.pdf]]，Abstract、Introduction。

## Table / Metric Anchors
- **Figure 1**：average training success rate against prior methods。
- **Figure 2**：EXPO-FT system overview。
- **Figure 3 / Figure 6**：eight-task real-world evaluation suite。
- **Figure 4**：training success and intervention rates across tasks。
- **Table 2**：success rates against SFT and HG-DAgger。
- **Figure 5**：episode time across tasks。

## Table / Metric Split
- `online data minutes` 是训练/适配成本口径，不是 inference runtime。
- `30/30 successes` 是本论文 evaluation suite 下的 real-world task success，不是跨 benchmark 平均成功率。
- human intervention affects learning protocol and should be kept separate from pure autonomous online RL comparisons。

## 不可混写项
- 不应把 EXPO-FT 写成推理提速或部署 latency 方法。
- 不应把 `perfect task performance` 外推到未评估的机器人平台或任务分布。
- 不应把 SFT / HG-DAgger / RL-from-scratch comparison 混成同一训练预算，除非回到表格设定。

## 影响页面
- [[wiki/papers/2605_25477_EXPO-FT.md|2605_25477_EXPO-FT]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
