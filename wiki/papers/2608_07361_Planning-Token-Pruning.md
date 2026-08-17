# 2608_07361_Planning-Token-Pruning

## Source
- Raw: [[raw/2608_07361_Planning-Token-Pruning.pdf]]
- Extracts manifest: [[extracts/parses/2608_07361_Planning-Token-Pruning/manifest.json]]
- Primary text fallback: [[extracts/parses/2608_07361_Planning-Token-Pruning/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **Planning-Token Pruning** 相关的增量论文；当前 L1 记录 driving VLA planning-token 的 depth-wise probing 与 post-hoc layer removal。
- 核心机制：用 frozen native planner 从每层 planning token 解码轨迹，并按层对该 token 造成的 angular deviation 排序移除 decoder layers。来源：[[raw/2608_07361_Planning-Token-Pruning.pdf]]，Abstract、Sec. 4、Sec. 7。
- 维护分类：主路线为 `1.2 Dynamic Computation Pathways`。

## Methodology Index
- trajectory-space logit lens
- planning-token probe
- cosine-ranked layer pruning
- open-loop driving evaluation

## Data Pointer
- **Sec. 6 / Table 2**：回读 semantic intent decodability 与 native-planner compatibility 的 depth split。
- **Sec. 7 / Fig. 5**：回读 k=8 pruning frontier 与 decoder latency。
- **Sec. 10-11**：回读 projected end-to-end speedup、single-checkpoint 与 open-loop limits。

## Evidence Links
- [[wiki/evidence/claims/2608_07361_Planning-Token-Pruning-headline-split.md|2608_07361_Planning-Token-Pruning-headline-split]]

## 待核点
- 1.33x 是 physically shortened decoder 的实测 speedup；约 1.13x end-to-end 是按 decoder latency share 推算，未端到端计时。
- 结论限于一个 ORION checkpoint 与 Bench2Drive open-loop setup，不建立 closed-loop safety。
