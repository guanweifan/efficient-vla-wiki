# 2511_18950_COMPRESSOR-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2511_18950_COMPRESSOR-VLA.md|2511_18950_COMPRESSOR-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`59% FLOPs reduction`、`over 3x token compression`、`97.1% -> 97.3% average success rate` 都绑定在 `OpenVLA-OFT + LIBERO` 这组主设置；如果横向比较，不应把它们与 `CogACT/π0` 或 real-robot 结果混成一个统一 headline。

## Evidence
- 这篇论文提出 **Compressor-VLA**，目标是把 VLA 的视觉 token 压缩从 task-agnostic pruning 改成**instruction-guided compression**。作者的核心判断是：在机器人操作里，视觉信息的相关性高度依赖语言指令，因此仅按通用 token importance 做 hard pruning 容易丢掉 task-critical 视觉信息。来源：[[raw/2511_18950_COMPRESSOR-VLA.pdf]]，第 1-2 页 Abstract、Introduction。
- 方法上的主张不是直接删 token，而是用一个 **hybrid instruction-conditioned compressor** 重建出更紧凑的视觉表示。框架由两个互补模块组成：**Semantic Task Compressor (STC)** 负责抽取整体、任务导向的上下文；**Spatial Refinement Compressor (SRC)** 负责保留细粒度空间细节。两条路径都受到语言指令调制，从而让压缩过程与当前任务绑定。来源：[[raw/2511_18950_COMPRESSOR-VLA.pdf]]，第 1-4 页 Abstract、Fig. 1、Fig. 2、Sec. 3。
- 主证据锚点 1：来源：[[raw/2511_18950_COMPRESSOR-VLA.pdf]]，**Abstract**：第 1 页。可直接承载 “STC + SRC + instruction-guided compression + 59% FLOPs reduction + over 3x token compression”。
- 主证据锚点 2：来源：[[raw/2511_18950_COMPRESSOR-VLA.pdf]]，**Figure 1 + Introduction**：第 2 页。用于锚定 standard VLA / task-agnostic pruning / Compressor-VLA 三种视觉处理流程的差异。
- 主证据锚点 3：来源：[[raw/2511_18950_COMPRESSOR-VLA.pdf]]，**Figure 2 + Sec. 3.2-3.3**：第 4-5 页。用于锚定 STC、SRC、FiLM 调制和双路径压缩的具体机制。

## Table / Metric Anchors
- **Table 1**：第 5-6 页。用于锚定与 OpenVLA-OFT、CogACT、π0 及多种 efficient VLA 的 success / FLOPs / token count 对比。
- **Table 2 / Table 3**：第 6-7 页。用于锚定 `STC+SRC`、`No Guidance`、`STC-Only`、`SRC-Only` 的 ablation，以及超参数 `k`、`w` 的 trade-off。

## Table / Metric Split
- `**Table 1**` 这一层应单独承载 `**Table 1**` 相关的 benchmark / metric / operating point。 这一层对应与 OpenVLA-OFT、CogACT、π0 及多种 efficient VLA 的 success / FLOPs / token count 对比。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2511_18950_COMPRESSOR-VLA.pdf]]，`**Table 1**`。
- `**Table 2 / Table 3**` 这一层应单独承载 `**Table 2 / Table 3**` 相关的 benchmark / metric / operating point。 这里收口为：**Table 2 / Table 3**：第 6-7 页。当前对应 `STC+SRC`、`No Guidance`、`STC-Only`、`SRC-Only` 的 ablation，以及超参数 `k`、`w` 的 trade-off。；`STC+SRC`、`STC+SRC-FiLM`、`No Guidance`、`STC-Only`、`SRC-Only` 的关系对方法理解很关键；这里需要决定哪些属于主线，哪些只保留在 evidence 层。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2511_18950_COMPRESSOR-VLA.pdf]]，`**Table 2 / Table 3**`。

## 不可混写项
- `59% FLOPs reduction`、`over 3x token compression`、`97.1% -> 97.3% average success rate` 都绑定在 `OpenVLA-OFT + LIBERO` 这组主设置；如果横向比较，不应把它们与 `CogACT/π0` 或 real-robot 结果混成一个统一 headline。
- 文中同时有 `competitive success rate` 与 `superior efficiency-performance trade-off` 两种较强措辞；当前更稳的写法是“在 OpenVLA-OFT + LIBERO 上保持同级甚至略优平均 success，同时显著压缩计算”，chief editor 可决定最终保留多强的 performance 语气。
- `STC+SRC`、`STC+SRC-FiLM`、`No Guidance`、`STC-Only`、`SRC-Only` 的关系对方法理解很关键；仍需决定哪些属于主线，哪些只保留在 evidence 层。

## 影响页面
- [[wiki/papers/2511_18950_COMPRESSOR-VLA.md|2511_18950_COMPRESSOR-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
