# 2603_22991_VLA-IAP-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_22991_VLA-IAP.md|2603_22991_VLA-IAP]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`97.8%`、`1.25×`、`1.54×`、`1.48×` 分别对应不同 retention ratio、不同 benchmark 和不同 deployment setting；仍需拆清比较对象和配置。

## Evidence
- 这篇论文要解决的问题是：现有 VLA visual token pruning 方法大多延续了 **Perception-First** 偏置，主要根据 semantic saliency 或简单 temporal cue 做裁剪，因此容易在任务早期把“视觉上不显眼但对物理操作关键”的结构性区域提前裁掉。作者据此提出 **VLA-IAP**，把 pruning 从被动的 perception filtering 改成 **Interaction-First** 的显式交互对齐机制。来源：[[raw/2603_22991_VLA-IAP.pdf]]，第 1-3 页 Abstract、Introduction、Fig. 1。
- 方法上的主张是一个 **training-free** 的 token pruning 框架，由两部分构成：一是 **Geometric Prior Mechanism**，通过 edge enhancement 保留结构锚点；二是 **Interaction-Aligned Dynamic Strategy**，根据 semantic-motion IoU 在 conservative pruning 和 aggressive pruning 之间动态切换。其关键 framing 不是“更好的注意力裁剪”，而是借助几何先验和交互状态判断，让 pruning 强度与 manipulation phase 对齐。来源：[[raw/2603_22991_VLA-IAP.pdf]]，第 2-5 页 Fig. 1、Fig. 2、Sec. 3。
- 主证据锚点 1：来源：[[raw/2603_22991_VLA-IAP.pdf]]，**Abstract + Introduction + Fig. 1**：第 1-3 页。用于锚定 perception-first 的问题定义，以及 Interaction-First 的总体 framing。
- 主证据锚点 2：来源：[[raw/2603_22991_VLA-IAP.pdf]]，**Fig. 2 + Sec. 3**：第 4-5 页。用于锚定 `Geometric Prior`、`Motion Prior`、`IoU-guided dynamic strategy` 和 conservative/aggressive 两种模式。
- 主证据锚点 3：来源：[[raw/2603_22991_VLA-IAP.pdf]]，**Fig. 3 + benchmark setup**：第 8-9 页。用于锚定它覆盖的三类 simulation benchmark（LIBERO、CALVIN、VLABench）及不同 backbone。

## Table / Metric Anchors
- **Table 2 / Table 3**：第 10-11 页。用于锚定在 OpenVLA-OFT / LIBERO 上的 `97.8% + 1.25×` 与 `1.54×` 等结果，以及 component ablation 的具体语境。

## Table / Metric Split
- `**Table 2 / Table 3**` 这一层应单独承载 `**Table 2 / Table 3**` 相关的 benchmark / metric / operating point。 这里收口为：**Table 2 / Table 3**：第 10-11 页。当前对应在 OpenVLA-OFT / LIBERO 上的 `97.8% + 1.25×` 与 `1.54×` 等结果，以及 component ablation 的具体语境。；`97.8%`、`1.25×`、`1.54×`、`1.48×` 分别对应不同 retention ratio、不同 benchmark 和不同 deployment setting；这里需要拆清比较对象和配置。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_22991_VLA-IAP.pdf]]，`**Table 2 / Table 3**`。

## 不可混写项
- `97.8%`、`1.25×`、`1.54×`、`1.48×` 分别对应不同 retention ratio、不同 benchmark 和不同 deployment setting；仍需拆清比较对象和配置。
- 论文同时使用 `Interaction-Aligned Pruning`、`Interaction-First paradigm`、`training-free visual token pruning` 三种 framing；后续 taxonomy 需要统一主定位。
- 当前 headline 结果强依赖 `OpenVLA-OFT` 等 backbone 与特定 benchmark；仍需决定单篇主 claim 中是否显式保留这些验证边界。

## 影响页面
- [[wiki/papers/2603_22991_VLA-IAP.md|2603_22991_VLA-IAP]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
