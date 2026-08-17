# 2608_11521_RIFT-headline-split

## 用途
- 服务于 [[wiki/papers/2608_11521_RIFT.md|RIFT]]，拆分 future-cache intervention、one-pass cache production、success 与 action-chunk latency。

## Evidence
- intervention 证据命题：mask / spatial shuffle / temporal swap 会改变 execution；在 original keys 下 replay final-clean K/V 则使 Joint / Cosmos-2 接近原执行。来源：[[raw/2608_11521_RIFT.pdf]]，Fig. 2、Sec. 4。
- 方法证据命题：RIFT 以 anticipation tokens 和 one-pass video backbone 产生完整 future-position K/V，保留 action expert 的 explicit future-read interface，部署不做 video denoising / decode。来源：[[raw/2608_11521_RIFT.pdf]]，Sec. 3、Appendix A。
- operating-point 证据命题：单张 A800 上 RIFT 为 98.8% success / 247.9 ms per chunk；rollout-based Joint / IDM / LingBot-VA 为 98.4%-98.6% / 780.2-2270.3 ms。来源：[[raw/2608_11521_RIFT.pdf]]，Table 1。

## Table / Metric Anchors
- **Fig. 2**：paired cache intervention 的 EE-ADE / SR。
- **Table 1**：future-read、rollout、SR 与 latency。

## Table / Metric Split
- future-cache necessity、cache construction process 与 learned RIFT performance 是三层证据。
- LIBERO、LIBERO-Plus 与 RoboTwin operating points 分开。

## 不可混写项
- 不把 final-clean value replay 直接写成完整 cache 可冻结。
- 不把 simulation result 写成 physical-robot deployment。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 当前 physical evaluation 缺失，且 non-WAM fusion backbone 尚未验证。
