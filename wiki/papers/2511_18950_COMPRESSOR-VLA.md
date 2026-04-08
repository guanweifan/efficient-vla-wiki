# 2511_18950_COMPRESSOR-VLA

## Source
- Raw: [[raw/2511_18950_COMPRESSOR-VLA.pdf]]
- Extracts manifest: [[extracts/parses/2511_18950_COMPRESSOR-VLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2511_18950_COMPRESSOR-VLA/pdftotext.txt]]

## Claim
- 这篇论文提出 **Compressor-VLA**，目标是把 VLA 的视觉 token 压缩从 task-agnostic pruning 改成**instruction-guided compression**。作者的核心判断是：在机器人操作里，视觉信息的相关性高度依赖语言指令，因此仅按通用 token importance 做 hard pruning 容易丢掉 task-critical 视觉信息。来源：[[raw/2511_18950_COMPRESSOR-VLA.pdf]]，第 1-2 页 Abstract、Introduction。
- 方法上的主张不是直接删 token，而是用一个 **hybrid instruction-conditioned compressor** 重建出更紧凑的视觉表示。框架由两个互补模块组成：**Semantic Task Compressor (STC)** 负责抽取整体、任务导向的上下文；**Spatial Refinement Compressor (SRC)** 负责保留细粒度空间细节。两条路径都受到语言指令调制，从而让压缩过程与当前任务绑定。来源：[[raw/2511_18950_COMPRESSOR-VLA.pdf]]，第 1-4 页 Abstract、Fig. 1、Fig. 2、Sec. 3。
- 论文保留了明确 headline numeric claims，但这些数字应拆开到具体 setting：相对 **OpenVLA-OFT** baseline，在 **LIBERO** 上，Compressor-VLA 将 FLOPs 从 **3.95T** 降到 **1.62T**（约 **59%** reduction），视觉 token 数从 **512** 压到 **160**（超过 **3x** compression），同时平均 success rate 从 **97.1%** 变为 **97.3%**。这更像“在 OpenVLA-OFT + LIBERO 设定下保持同级甚至略优表现”，而不是对所有 VLA 的无条件效率-性能结论。来源：[[raw/2511_18950_COMPRESSOR-VLA.pdf]]，第 1-2 页 Abstract；第 5-6 页 Table 1。
- 从当前证据看，Compressor-VLA 更像一篇**面向 OpenVLA-style manipulation VLA 的 instruction-guided visual token compression 模块**，而不是一般意义上的轻量化 VLA 重构。它的重点在于通过 STC / SRC 的双路径设计，同时保留 holistic context 与 fine-grained spatial detail，并用指令引导二者的关注分工；真实机器人实验则主要补充 sim-to-real 可行性，而不是重新定义它的主贡献。来源：[[raw/2511_18950_COMPRESSOR-VLA.pdf]]，第 2-5 页 Fig. 1、Fig. 2、Sec. 3；第 6-9 页 Table 2-4、Fig. 4-5。

## Methodology Index
- instruction-guided compression
- visual token compression
- hybrid token compressor
- Semantic Task Compressor
- STC
- Spatial Refinement Compressor
- SRC
- Feature-wise Linear Modulation
- FiLM
- query-based aggregation
- local attention
- task-conditioned visual compression
- OpenVLA-OFT backbone
- LIBERO benchmark
- dual-arm real-robot deployment

## Data Pointer
- **Abstract**：第 1 页。适合后续回收 “STC + SRC + instruction-guided compression + 59% FLOPs reduction + over 3x token compression”。
- **Figure 1 + Introduction**：第 2 页。适合后续补 standard VLA / task-agnostic pruning / Compressor-VLA 三种视觉处理流程的差异。
- **Figure 2 + Sec. 3.2-3.3**：第 4-5 页。适合后续补 STC、SRC、FiLM 调制和双路径压缩的具体机制。
- **Table 1**：第 5-6 页。适合后续补与 OpenVLA-OFT、CogACT、π0 及多种 efficient VLA 的 success / FLOPs / token count 对比。
- **Table 2 / Table 3**：第 6-7 页。适合后续补 `STC+SRC`、`No Guidance`、`STC-Only`、`SRC-Only` 的 ablation，以及超参数 `k`、`w` 的 trade-off。
- **Figure 4 / Figure 5**：第 8-9 页。适合后续补 instruction-conditioned attention 与 STC / SRC 分工的可视化证据。

## 待核点
- `59% FLOPs reduction`、`over 3x token compression`、`97.1% -> 97.3% average success rate` 都绑定在 `OpenVLA-OFT + LIBERO` 这组主设置；后续如果横向比较，不应把它们与 `CogACT/π0` 或 real-robot 结果混成一个统一 headline。
- 文中同时有 `competitive success rate` 与 `superior efficiency-performance trade-off` 两种较强措辞；当前更稳的写法是“在 OpenVLA-OFT + LIBERO 上保持同级甚至略优平均 success，同时显著压缩计算”，chief editor 可决定最终保留多强的 performance 语气。
- `STC+SRC`、`STC+SRC-FiLM`、`No Guidance`、`STC-Only`、`SRC-Only` 的关系对方法理解很关键；后续需要决定哪些属于主线，哪些只保留在 evidence 层。
- 真实机器人实验只在 dual-arm 平台上做了验证，目前更适合当作 sim-to-real 可行性证据，而不是广泛 real-robot generalization 结论。
