# 2608_09492_TempoWAM-headline-split

## 用途
- 服务于 [[wiki/papers/2608_09492_TempoWAM.md|TempoWAM]]，拆分 action-chunk execution policy、WAM call count、monitor cost 与 per-call runtime。

## Evidence
- 方法证据命题：RPM 预测执行候选动作后的 progress，AEP 经 offline / intra-episode / inter-episode calibration 判断继续 chunk 或 replanning。来源：[[raw/2608_09492_TempoWAM.pdf]]，Fig. 2、Sec. 3。
- real-world 证据命题：easy take-drinks task 在 90.0% success 不变时 calls 从 32.7 降至 23.9；hard pack-hand-cream task success 从 50.0% 升至 63.3，但 calls 从 49.4 升至 57.2。来源：[[raw/2608_09492_TempoWAM.pdf]]，Table 5。
- cost 证据命题：RPM decision 为一次 optimized WAM call 的 3.54%（含 visual encoding）或 0.34%（shared features）；同表的 per-call latency 来自独立 runtime stack。来源：[[raw/2608_09492_TempoWAM.pdf]]，Table 6。

## Table / Metric Anchors
- **Table 1 / 3 / 5**：不同 benchmark 的 SR、calls、steps。
- **Table 6 / Sec. 4.4**：monitor overhead 与 progress-label limits。

## Table / Metric Split
- fewer calls、earlier replanning、executed steps 与 single-call latency 是不同层。
- easy-stage efficiency 与 hard-stage recovery 可能改变 calls 的相反方向。

## 不可混写项
- 不把 TempoWAM 写成总会减少调用次数。
- 不把 runtime-stack 3.1x/4.3x 归因于 progress monitor。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- time-based progress supervision 依赖 progress-monotonic state sequence，state aliasing task 需要其他 supervision。
