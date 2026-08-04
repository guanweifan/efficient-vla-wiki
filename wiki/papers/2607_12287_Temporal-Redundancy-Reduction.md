# 2607_12287_Temporal-Redundancy-Reduction

## Source
- Raw: [[raw/2607_12287_Temporal-Redundancy-Reduction.pdf]]
- Extracts manifest: [[extracts/parses/2607_12287_Temporal-Redundancy-Reduction/manifest.json]]
- Primary text fallback: [[extracts/parses/2607_12287_Temporal-Redundancy-Reduction/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **Temporal Redundancy Reduction** 相关的增量论文；当前 L1 记录 perception/action 双侧加速入口。
- 核心机制：相邻帧只更新动态区域对应的 visual tokens，同时把 flow-matching action generation 压到 learned two-step schedule。来源：[[raw/2607_12287_Temporal-Redundancy-Reduction.pdf]]，Abstract、Sec. 1。
- 维护分类：主路线为 `3.1 Raw Action Generation`，次级相关为 `2.2 Temporal Sharing and Reuse`。

## Methodology Index
- temporal redundancy
- selective token refresh
- two-step flow matching
- system-level acceleration

## Data Pointer
- **Abstract / Sec. 1**：回读两类 temporal redundancy 与联合设计。
- **Method**：回读 dynamic-region token update 和 two-step policy training。
- **Experiments**：后续拆分 perception、action head、end-to-end latency 与 task success。

## Evidence Links
- [[wiki/evidence/claims/2607_12287_Temporal-Redundancy-Reduction-headline-split.md|2607_12287_Temporal-Redundancy-Reduction-headline-split]]

## 待核点
- 视觉复用与两步 action policy 的独立贡献需要回到 ablation。
- 系统 speedup 不能只由单模块数值推断。
