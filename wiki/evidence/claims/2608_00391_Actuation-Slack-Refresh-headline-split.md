# 2608_00391_Actuation-Slack-Refresh-headline-split

## 用途
- 服务于 [[wiki/papers/2608_00391_Actuation-Slack-Refresh.md|Actuation-Slack Refresh]]，拆分 gate reliability、critical-path latency 与总资源成本。

## Evidence
- 方法证据命题：论文把 token reuse/deletion 与 gate provenance 交叉评估，并以 actuation-slack dense refresh 提供 clean gate/fresh KV。来源：[[raw/2608_00391_Actuation-Slack-Refresh.pdf]]，Abstract、Sec. 1。
- 成本边界命题：refresh 离开 serve critical path，但 Sec. 5.8 明确给出更高总 computation 与 energy cost。来源：[[raw/2608_00391_Actuation-Slack-Refresh.pdf]]，Sec. 5.6、Sec. 5.8。
- 分类证据命题：贡献位于 closed-loop scheduling 与 state maintenance，不是新的 token salience estimator。

## Table / Metric Anchors
- **Controlled gate study**：reuse/deletion x clean/self-harvested gate。
- **Sec. 5.6 / Table 5 / Sec. 5.8**：serve latency、FLOPs、energy 与 limitation。

## Table / Metric Split
- critical-path latency、total FLOPs、energy 与 success reliability 必须四分。
- simulation reliability 与 physical-platform latency 不能合成同一 operating point。

## 不可混写项
- 不把 off-critical-path 写成 zero-cost。
- 不把 clean-gate requirement 写成某一 cache/pruning mechanism 独有收益。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页明确保留 latency 与 total-resource tradeoff。
