# 2605_13778_Realtime-VLA-FLASH-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_13778_Realtime-VLA-FLASH.md|2605_13778_Realtime-VLA-FLASH]] 的单篇证据落点，用来拆分 speculative inference、draft/verify/fallback 与 latency / task result。

## Evidence
- 核心证据命题：FLASH 使用 lightweight draft model 产生候选动作，由 Action Expert 并行验证，并用 phase-aware fallback 处理关键阶段。来源：[[raw/2605_13778_Realtime-VLA-FLASH.pdf]]，Abstract、Figures 1、3、4、5。
- 延迟证据命题：论文区分 full-inference rounds、speculative rounds 与 task-level average latency，并报告 3.04x speedup headline。来源：[[raw/2605_13778_Realtime-VLA-FLASH.pdf]]，Abstract、Table 2、Table 6。
- 结果证据命题：论文在 LIBERO 与真实 conveyor sorting 上报告任务表现和 ablations。来源：[[raw/2605_13778_Realtime-VLA-FLASH.pdf]]，Tables 1、3、4。

## Table / Metric Anchors
- **Figures 1-6**：framework, roofline, verification, fallback。
- **Tables 1-4**：LIBERO, path stats, ablation, real setup。
- **Table 6**：inference cost breakdown。

## Table / Metric Split
- speculative latency、full inference latency、average task latency 与 success rate 是不同口径。
- phase-aware fallback 是可靠性机制，不能只按速度读。

## 不可混写项
- 不应写成训练效率。
- 不应写成 cloud-edge jitter correction。

## 影响页面
- [[wiki/papers/2605_13778_Realtime-VLA-FLASH.md|2605_13778_Realtime-VLA-FLASH]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
