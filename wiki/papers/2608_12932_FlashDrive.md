# 2608_12932_FlashDrive

## Source
- Raw: [[raw/2608_12932_FlashDrive.pdf]]
- Extracts manifest: [[extracts/parses/2608_12932_FlashDrive/manifest.json]]
- Primary text fallback: [[extracts/parses/2608_12932_FlashDrive/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **FlashDrive** 相关的增量论文；当前 L1 记录 driving VLA encode-prefill-decode-action 全流水线的 algorithm-system co-design。
- 核心机制：跨帧 streaming encode/KV reuse、diffusion-draft speculative reasoning、adaptive-step flow velocity reuse 与 CUDA Graph/kernel fusion/W4A8 共同覆盖四阶段瓶颈。来源：[[raw/2608_12932_FlashDrive.pdf]]，Abstract、Sec. 3。
- 维护分类：主路线为 `4.2 Inference Efficiency Techniques`。

## Methodology Index
- streaming KV reuse
- speculative reasoning
- adaptive-step flow matching
- CUDA Graph and W4A8

## Data Pointer
- **Table 1**：回读逐阶段 latency ablation、combined stack 与 open-loop error。
- **Table 2**：回读跨五类 GPU、sample count 与 OOM boundary。
- **Table 3 / Appendix Table A3**：回读 AlpaSim closed-loop metric 与 rollout latency scope。

## Evidence Links
- [[wiki/evidence/claims/2608_12932_FlashDrive-headline-split.md|2608_12932_FlashDrive-headline-split]]

## 待核点
- 4.7x 是 Alpamayo 1.5-10B 在 RTX PRO 6000 上由多项算法、系统与量化技术组合得到，不能归因于单一组件。
- closed-loop 结果来自 AlpaSim；collision/off-road 改善与 Wrong Lane 退化应同时保留，不能写成无条件 safety improvement。
