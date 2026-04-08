# 2512_20276_ActionFlow-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2512_20276_ActionFlow.md|2512_20276_ActionFlow]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`2.55×`、`1.25 -> 3.20 FPS`、`7.62 -> 19.45 FPS`、`4.06×` 等数字来自不同硬件和 workload；仍需拆清哪些属于默认 headline，哪些属于 sensitivity analysis。

## Evidence
- 这篇论文提出 **ActionFlow**，它不是新的 VLA 架构或训练方法，而是一个面向边缘设备的 **system-level inference framework**。作者的核心判断是：当前 VLA 在 edge hardware 上真正的瓶颈不是视觉编码，而是 LLM autoregressive decoding 的 memory-bound decode phase，因此仅做量化、蒸馏或训练式并行解码，无法根治低频控制问题。来源：[[raw/2512_20276_ActionFlow.pdf]]，第 1-2 页 Abstract、Introduction。
- 核心方法主张是把单个 VLA 请求重构成由一个 Prefill 和多个 Decode 组成的 **macro-pipeline of micro-requests**，再通过 **Cross-Request Pipelining** 跨连续时间步把 compute-bound Prefill 与 memory-bound Decode 重叠执行。为支持这一调度，论文进一步提出 **Cross-Request State Packed Forward** 与 **Unified KV Ring Buffer**，把碎片化的 memory operations 融合成更致密的计算。来源：[[raw/2512_20276_ActionFlow.pdf]]，第 1-2 页 Abstract、贡献段；第 3-7 页 Sec. 3、Fig. 3、Fig. 4。
- 主证据锚点 1：来源：[[raw/2512_20276_ActionFlow.pdf]]，**Abstract**：第 1 页。可直接承载 `20–30 Hz` 目标、`3–5 Hz` 现状、`2.55×` 提升和无 retraining 的 headline。
- 主证据锚点 2：来源：[[raw/2512_20276_ActionFlow.pdf]]，**Figure 1 + Introduction**：第 1-2 页。用于锚定 VLA autoregressive action generation 的 latency framing，以及 edge deployment 问题定义。
- 主证据锚点 3：来源：[[raw/2512_20276_ActionFlow.pdf]]，**Figure 2**：第 3 页。用于锚定为何 decode phase 是主要瓶颈，以及 Roofline 视角下的 memory-bound 问题。

## Table / Metric Anchors
- **Table 1 / Table 2 / Figure 5**：第 8-10 页。用于锚定端到端性能、功能正确性验证、以及不同 workload 下的 sensitivity analysis。

## Table / Metric Split
- `**Table 1 / Table 2 / Figure 5**` 这一层应单独承载 `**Table 1 / Table 2 / Figure 5**` 相关的 benchmark / metric / operating point。 这一层对应端到端性能、功能正确性验证、以及不同 workload 下的 sensitivity analysis。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2512_20276_ActionFlow.pdf]]，`**Table 1 / Table 2 / Figure 5**`。

## 不可混写项
- `2.55×`、`1.25 -> 3.20 FPS`、`7.62 -> 19.45 FPS`、`4.06×` 等数字来自不同硬件和 workload；仍需拆清哪些属于默认 headline，哪些属于 sensitivity analysis。
- 论文围绕 OpenVLA-7B 展开，虽然方法表述更一般，但当前证据仍主要来自单一模型；仍需决定在主题页里保留多强的泛化语气。
- ActionFlow 同时强调 `system-level`, `scheduler`, `operator fusion`, `KV cache management`；后续 taxonomy 需要统一它的主定位。

## 影响页面
- [[wiki/papers/2512_20276_ActionFlow.md|2512_20276_ActionFlow]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
