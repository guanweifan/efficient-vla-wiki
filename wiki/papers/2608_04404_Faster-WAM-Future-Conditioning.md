# 2608_04404_Faster-WAM-Future-Conditioning

## Source
- Raw: [[raw/2608_04404_Faster-WAM-Future-Conditioning.pdf]]
- Extracts manifest: [[extracts/parses/2608_04404_Faster-WAM-Future-Conditioning/manifest.json]]
- Primary text fallback: [[extracts/parses/2608_04404_Faster-WAM-Future-Conditioning/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **Faster-WAM (Future Conditioning)** 相关的增量论文；当前 L1 记录 WAM action denoising 中的 sparse future conditioning。
- 核心机制：先用一次 video-expert pass 构造可复用 future context，再以 SparseMoT 选择交互层、以 Interval KV-Fusion 聚合 interval 内多深度 future representations。来源：[[raw/2608_04404_Faster-WAM-Future-Conditioning.pdf]]，Abstract、Method / Fig. 2。
- 维护分类：主路线为 `3.1 Raw Action Generation`。

## Methodology Index
- SparseMoT
- Interval KV-Fusion
- one-pass future context
- action denoising

## Data Pointer
- **Abstract / Fig. 2**：回读 inference-time future conditioning 与 sparse interaction。
- **Table 5**：回读 current-only、dense/sparse interaction 与 OOD success 的消融。
- **Appendix Table A4**：回读单张 L20、10-step action denoising 下的 latency scope。

## Evidence Links
- [[wiki/evidence/claims/2608_04404_Faster-WAM-Future-Conditioning-headline-split.md|2608_04404_Faster-WAM-Future-Conditioning-headline-split]]

## 待核点
- future K/V 只在同一 action chunk 的 denoising 中复用，不是跨 observation 的 temporal cache。
- Table A4 排除了 image preprocessing、language embedding、action denormalization 与 gripper post-processing。
