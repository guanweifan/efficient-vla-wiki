# 2608_07361_Planning-Token-Pruning-headline-split

## 用途
- 服务于 [[wiki/papers/2608_07361_Planning-Token-Pruning.md|Planning-Token Pruning]]，拆分 early decodability、planner compatibility、decoder speedup 与 projected end-to-end gain。

## Evidence
- probing 证据命题：command probe 在首个 decoder layer 达 97.7%，但 frozen native planner 的 Avg-L2 只在 final layer 达最小 2.11 m；前者表示线性可读，后者表示下游格式兼容。来源：[[raw/2608_07361_Planning-Token-Pruning.pdf]]，Abstract、Sec. 6、Table 2。
- pruning 证据命题：按 planning-token angular deviation 排序移除 8/32 层，decoder latency 从 497.52 降至 373.22 ms，测得 1.33x speedup，Avg-L2 保持在约 5% relative increase 内。来源：[[raw/2608_07361_Planning-Token-Pruning.pdf]]，Sec. 7、Fig. 5。
- projection 证据命题：约 1.13x end-to-end speedup 是按 decoder 约占 half per-frame latency 的 Amdahl projection，论文未端到端计时。来源：[[raw/2608_07361_Planning-Token-Pruning.pdf]]，Sec. 10。

## Table / Metric Anchors
- **Table 2 / Fig. 5**：depth probe 与 pruning frontier。
- **Sec. 10-11**：projection 与 limitations。

## Table / Metric Split
- linear probe accuracy、native-planner trajectory error 与 pruned-model latency 不同。
- decoder-only measurement 与 end-to-end projection 必须分开。

## 不可混写项
- 不把 early linear decodability 写成 early native-planner readiness。
- 不把 open-loop pruning result 写成 closed-loop deployment safety。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 当前结论只覆盖单一 ORION checkpoint、Bench2Drive 与 FP32 A100 decoder forward。
