# 2608_02365_Faster-WAM-DoT

## Source
- Raw: [[raw/2608_02365_Faster-WAM-DoT.pdf]]
- Extracts manifest: [[extracts/parses/2608_02365_Faster-WAM-DoT/manifest.json]]
- Primary text fallback: [[extracts/parses/2608_02365_Faster-WAM-DoT/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **Faster-WAM / DoT** 相关的增量论文；当前 L1 记录 shallow action-module WAM architecture。
- 核心机制：把 pretrained video Transformer 作为 representation hub，通过 cross-layer KV fusion 与 RoPE realignment 接入 single-layer action head。来源：[[raw/2608_02365_Faster-WAM-DoT.pdf]]，Abstract、Sec. 1。
- 维护分类：主路线为 `1.1 Static Backbone Selection`。

## Methodology Index
- Faster-WAM
- Dock of Transformer
- single-layer action head
- cross-layer KV fusion

## Data Pointer
- **Abstract / Sec. 1**：回读 deep action-module overhead 与 DoT premise。
- **Method**：回读 docking interface、KV fusion、RoPE alignment。
- **Experiments**：后续拆分 action-head depth、end-to-end latency、hardware 与 task/generalization result。

## Evidence Links
- [[wiki/evidence/claims/2608_02365_Faster-WAM-DoT-headline-split.md|2608_02365_Faster-WAM-DoT-headline-split]]

## 待核点
- 论文未减少 flow denoising NFE，不能归为 action-step compression。
- controlled latency comparison 需要绑定 model size、backbone、hardware 与 implementation。
