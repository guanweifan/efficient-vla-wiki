# 2607_13960_GigaWorld-Policy-0.5-GWP-0.5

## Source
- Raw: [[raw/2607_13960_GigaWorld-Policy-0.5-GWP-0.5.pdf]]
- Extracts manifest: [[extracts/parses/2607_13960_GigaWorld-Policy-0.5-GWP-0.5/manifest.json]]
- Primary text fallback: [[extracts/parses/2607_13960_GigaWorld-Policy-0.5-GWP-0.5/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **GigaWorld-Policy-0.5 / GWP-0.5** 相关的增量论文；当前 L1 记录 action-only WAM deployment path。
- 核心机制：训练时保留 visual-dynamics supervision，部署时跳过 future-video generation，仅运行轻量 action expert，并用 native runtime 优化执行。来源：[[raw/2607_13960_GigaWorld-Policy-0.5-GWP-0.5.pdf]]，Abstract、Sec. 1、deployment method。
- 维护分类：主路线为 `3.1 Raw Action Generation`，次级相关为 `4.2 Inference Efficiency Techniques`。

## Methodology Index
- GWP-0.5
- action-only WAM inference
- lightweight action expert
- native runtime

## Data Pointer
- **Abstract / Sec. 1**：回读 action-centered formulation 与 AutoResearch scope。
- **Method / Deployment**：回读 action-only path、KV cache、graph compilation 与 C++ runtime。
- **Experiments**：后续拆分 model-level latency、runtime gain、training recipe 与 task performance。

## Evidence Links
- [[wiki/evidence/claims/2607_13960_GigaWorld-Policy-0.5-GWP-0.5-headline-split.md|2607_13960_GigaWorld-Policy-0.5-GWP-0.5-headline-split]]

## 待核点
- 85 ms 等 headline 包含 runtime contribution，不能只归因于 model formulation。
- AutoResearch 是训练 recipe 搜索，当前不自动构成训练成本下降证据。
