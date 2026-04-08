# 2507_14049_EdgeVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2507_14049_EdgeVLA.md|2507_14049_EdgeVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`7x speedup`、`20 ms -> 5 ms`、`16 GB -> 4 GB` 目前都保留为论文 headline；仍需精确拆清对应 baseline、硬件、实现设置和是否同属一个 claim。

## Evidence
- 这篇论文提出 **EdgeVLA / EVLA**，目标不是继续放大 VLA 规模，而是让 VLA 更适合部署到资源受限的移动操作与边缘设备上。作者把问题明确写成：现有 VLM/VLA 虽然性能提升明显，但在 Jetson Nano 一类平台上因推理延迟和显存占用过高而难以实际部署。来源：[[raw/2507_14049_EdgeVLA.pdf]]，第 1 页 Abstract、Introduction。
- 核心主张有两条：一是把末端执行器控制从自回归逐步预测改成**联合预测（joint end-effector prediction）**，从而去掉 action decoding 的 autoregressive requirement；二是把语言主干收缩到 **Qwen2-0.5B** 级别，并与 **SigLIP + DINOv2** 视觉编码器结合，构成约 **1B 参数** 的 EdgeVLA。来源：[[raw/2507_14049_EdgeVLA.pdf]]，第 1 页 Abstract；第 2 页 Fig. 1、Sec. 2。
- 主证据锚点 1：来源：[[raw/2507_14049_EdgeVLA.pdf]]，**Abstract**：第 1 页。可直接承载“边缘部署动机 + 7x speedup + SLM + comparable training characteristics”。
- 主证据锚点 2：来源：[[raw/2507_14049_EdgeVLA.pdf]]，**Fig. 1 + Sec. 2**：第 2 页。用于锚定 EdgeVLA 架构，包括 `Qwen2-0.5B + SigLIP + DINOv2` 以及两阶段训练流程。
- 主证据锚点 3：来源：[[raw/2507_14049_EdgeVLA.pdf]]，**BridgeData V2 训练描述**：第 2 页右栏。用于锚定 “similar training performance to 7.5B counterpart” 的具体语境。

## Table / Metric Anchors
- **Table I**：第 3 页。用于锚定 `20 ms -> 5 ms` 与 `16 GB -> 4 GB` 的效率 claim 及其实现 caveat。

## Table / Metric Split
- `Table I` 对应 **部署效率主表**：在 `A100-40GB GPU` 上，`OpenVLA` 的 inference time / memory 是 `20 ms / 16 GB`，`EVLA` 是 `5 ms / 4 GB`；这里支撑的是具体硬件上的部署效率，不应与摘要里的 `7x speedup` 直接视作同一数字。来源：[[raw/2507_14049_EdgeVLA.pdf]]，第 3 页，Table I。
- `Abstract` 中的 `7x speedup` 更接近 **联合末端执行器预测相对自回归解码的总体 headline**，而 `Table I` 是具体部署表；两者都指向效率提升，但不应压成同一 operating point。来源：[[raw/2507_14049_EdgeVLA.pdf]]，第 1 页 Abstract；第 3 页 Table I。

## 不可混写项
- `7x speedup`、`20 ms -> 5 ms`、`16 GB -> 4 GB` 目前都保留为论文 headline；仍需精确拆清对应 baseline、硬件、实现设置和是否同属一个 claim。
- 文中同时使用 `EdgeVLA` 与 `EVLA`；仍需统一单篇页与主题页的命名口径。
- “comparable training characteristics” 目前只按作者原话保守记录；引用时要决定是否继续保持这个措辞，还是进一步降格为“训练曲线相近、但证据仍偏早期”。

## 影响页面
- [[wiki/papers/2507_14049_EdgeVLA.md|2507_14049_EdgeVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
