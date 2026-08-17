# 2608_10824_Gated-VLA-Cache

## Source
- Raw: [[raw/2608_10824_Gated-VLA-Cache.pdf]]
- Extracts manifest: [[extracts/parses/2608_10824_Gated-VLA-Cache/manifest.json]]
- Primary text fallback: [[extracts/parses/2608_10824_Gated-VLA-Cache/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **Gated VLA-Cache** 相关的增量论文；当前 L1 记录 action-confidence-gated cross-frame KV reuse。
- 核心机制：在 VLA-Cache 的 visual-similarity reuse 上增加 top-1 / top-2 action-logit margin；低于阈值时整体 invalidate cache 并 full recompute，否则执行原有 selective reuse。来源：[[raw/2608_10824_Gated-VLA-Cache.pdf]]，Abstract、Fig. 2、Algorithm 1。
- 维护分类：主路线为 `2.2 Temporal Sharing and Reuse`。

## Methodology Index
- cross-frame KV reuse
- logit-margin gate
- cache invalidation
- training-free inference

## Data Pointer
- **Table I-II**：回读 OpenVLA / OpenVLA-OFT 的 success 与 TFLOPs/step。
- **Fig. 5 / Sec. V-E**：回读 gating frequency 与 task phase trace。
- **Sec. VI**：回读 one-step lag、per-family calibration 与 simulation-only limits。

## Evidence Links
- [[wiki/evidence/claims/2608_10824_Gated-VLA-Cache-headline-split.md|2608_10824_Gated-VLA-Cache-headline-split]]

## 待核点
- 论文报告 TFLOPs/step，没有 wall-clock latency；compute saving 不能改写成实测 speedup。
- threshold 每个 model family 校准一次，且 gate 使用上一步 margin，存在 one-step reactive lag。
