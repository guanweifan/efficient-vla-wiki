# 2608_06008_Adaptive-WAM

## Source
- Raw: [[raw/2608_06008_Adaptive-WAM.pdf]]
- Extracts manifest: [[extracts/parses/2608_06008_Adaptive-WAM/manifest.json]]
- Primary text fallback: [[extracts/parses/2608_06008_Adaptive-WAM/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **Adaptive-WAM** 相关的增量论文；当前 L1 记录 quality-guided multi-exit video-DiT planning。
- 核心机制：在六个 DiT depth 挂接 trajectory diffusion head，由 DINOv2-Small quality scorer 判断是否返回累计候选中的最佳轨迹，否则从缓存 hidden state 继续到更深 exit。来源：[[raw/2608_06008_Adaptive-WAM.pdf]]，Abstract、Fig. 1、Appendix J。
- 维护分类：主路线为 `1.2 Dynamic Computation Pathways`。

## Methodology Index
- multi-exit planner
- trajectory-quality scorer
- adaptive DiT depth
- rollout-free deployment

## Data Pointer
- **Table 1 / Appendix G**：回读 layer-wise planning quality 与 depth complementarity。
- **Appendix Table 23**：回读 fixed B15、adaptive routing 与 full path 的同层 planning latency。
- **Appendix Table 24 / Sec. M**：回读 full-video generation 的独立成本与 learned-scorer failure boundary。

## Evidence Links
- [[wiki/evidence/claims/2608_06008_Adaptive-WAM-headline-split.md|2608_06008_Adaptive-WAM-headline-split]]

## 待核点
- 190 ms 到 170 ms 是 adaptive routing 相对最佳 fixed single-trajectory exit 的收益；320 ms 到 170 ms 是相对 full-depth planning path，不能合并成一个百分比。
- quality threshold 是 learned verifier，不构成 safety certificate。
