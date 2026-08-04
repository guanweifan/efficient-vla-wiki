# 2608_00569_CloudEdgeVLA

## Source
- Raw: [[raw/2608_00569_CloudEdgeVLA.pdf]]
- Extracts manifest: [[extracts/parses/2608_00569_CloudEdgeVLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2608_00569_CloudEdgeVLA/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **CloudEdgeVLA** 相关的增量论文；当前 L1 记录 latency-tolerant cloud-edge dual system。
- 核心机制：cloud VLA 提供慢变 task features，edge head 结合最新 cloud feature 与当前 local vision；paired fresh/stale training 使 cloud representation 在非阻塞延迟下仍可用。来源：[[raw/2608_00569_CloudEdgeVLA.pdf]]，Abstract、Introduction。
- 维护分类：主路线为 `1.3 Dual-system Design`，次级相关为 `4.2 Inference Efficiency Techniques`。

## Methodology Index
- CloudEdgeVLA
- cloud-edge dual system
- stale feature robustness
- non-blocking control

## Data Pointer
- **Abstract / Introduction**：回读 cloud semantics、edge correction 与 representation specialization。
- **Method**：回读 paired-frame dual-path training 和 non-blocking interface。
- **Experiments**：后续拆分 uniform-delay robustness、communication assumptions、edge compute 与 real-robot sanity check。

## Evidence Links
- [[wiki/evidence/claims/2608_00569_CloudEdgeVLA-headline-split.md|2608_00569_CloudEdgeVLA-headline-split]]

## 待核点
- 论文主要验证 delay robustness，不能写成已测得实际网络端到端加速。
- cloud compute、edge compute、communication cost 与 control success 需要分开。
