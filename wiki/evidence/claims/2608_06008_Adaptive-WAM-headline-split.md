# 2608_06008_Adaptive-WAM-headline-split

## 用途
- 服务于 [[wiki/papers/2608_06008_Adaptive-WAM.md|Adaptive-WAM]]，拆分 adaptive routing、full-depth planning 与 full-video generation。

## Evidence
- 方法证据命题：六个 intermediate exits 各解码一条 trajectory，DINOv2-Small scorer 达阈值则返回累计最佳候选，否则从 cached state 继续。来源：[[raw/2608_06008_Adaptive-WAM.pdf]]，Fig. 1、Appendix J。
- routing 证据命题：单张 A100 上，eta=90 adaptive policy 为 90.79 PDMS / 170 ms，fixed B15 为 90.62 / 190 ms，full path 为 85.82 / 320 ms。来源：[[raw/2608_06008_Adaptive-WAM.pdf]]，Appendix Table 23。
- generation 证据命题：完整 nine-frame video path 包含 40-step conditional/unconditional denoising 与 VAE decode，deployment-comparable total 为 13.22 s；论文明确与 320-to-170 ms planning claim 分开。来源：[[raw/2608_06008_Adaptive-WAM.pdf]]，Appendix Table 24、Sec. K。

## Table / Metric Anchors
- **Table 23**：single-trajectory threshold sweep。
- **Table 24**：full-video generation decomposition。

## Table / Metric Split
- adaptive-vs-fixed-exit、adaptive-vs-full-depth 与 planning-vs-video-generation 是三层比较。
- scorer diagnostic、planner PDMS 与 safety certificate 不等价。

## 不可混写项
- 不把移除 rollout 的收益归因于 early-exit routing。
- 不把 quality threshold 写成安全保证。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 结论来自 NAVSIM / nuScenes driving setup，不能直接转写为 manipulation VLA 的 depth policy。
