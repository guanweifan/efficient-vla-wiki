# 2509_21354_KV-Efficient-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2509_21354_KV-Efficient-VLA.md|2509_21354_KV-Efficient-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`1.34×` 是三种 baseline 平均 speedup；单个模型的提升不同，后续不能写成统一无条件倍数。

## Evidence
- 核心证据命题：这篇论文要解决的是：VLA 在长时序推理中需要持续保留历史图像 token 的 key-value (`KV`) cache，导致 attention 计算和 KV 存储都随上下文增长而变重，难以满足实时机器人控制。 来源：[[raw/2509_21354_KV-Efficient-VLA.pdf]]，`PDF p.1` Abstract + Fig. 1：
- 补充证据命题：作者提出 `KV-Efficient VLA`，这是一个面向推理期的 memory compression 模块。它把历史 KV cache 按固定长度切成 chunk，对每个 chunk 做聚合，再用一个轻量 LSTM gate 决定哪些压缩后的 chunk 应该保留、哪些可以丢弃，同时保留最近窗口的原始细粒度 tokens。 来源：[[raw/2509_21354_KV-Efficient-VLA.pdf]]，问题设定、`chunked KV + recurrent gating` 的核心思路，以及 `24.6% FLOPs savings / 1.34× speedup / 1.87× memory reduction` 的 headline 都在这里。
- 主证据锚点 1：来源：[[raw/2509_21354_KV-Efficient-VLA.pdf]]，`PDF p.1` Abstract + Fig. 1：
- 主证据锚点 2：来源：[[raw/2509_21354_KV-Efficient-VLA.pdf]]，问题设定、`chunked KV + recurrent gating` 的核心思路，以及 `24.6% FLOPs savings / 1.34× speedup / 1.87× memory reduction` 的 headline 都在这里。
- 主证据锚点 3：来源：[[raw/2509_21354_KV-Efficient-VLA.pdf]]，`PDF p.2-5` Sec. 3 + Fig. 2：

## Table / Metric Anchors
- `PDF p.7` Table 1：
  - OpenVLA / CogACT / HybridVLA 及其 KV-Efficient 版本的 `Infer. Speed (Hz)`、`Total-FLOPs (T)` 与 speedup 对照都在这里。

## Table / Metric Split
- ``PDF p.7` Table 1` 这一层支撑 ``PDF p.7` Table 1` 对应的 benchmark / metric / operating point。 - OpenVLA / CogACT / HybridVLA 及其 KV-Efficient 版本的 `Infer. Speed (Hz)`、`Total-FLOPs (T)` 与 speedup 对照都在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2509_21354_KV-Efficient-VLA.pdf]]，``PDF p.7` Table 1`。

## Wording / Boundary Split
- `model-agnostic memory compression` 在本文里有明确但有限的操作性含义：模块通过 chunked KV aggregation + recurrent gate 压缩历史 memory，并声称能无缝集成到近期 VLA stack、且**不修改 downstream control logic**。来源：[[raw/2509_21354_KV-Efficient-VLA.pdf]]，第 1 页 Abstract。
- 但当前直接验证的架构范围仍主要是 `OpenVLA / CogACT / HybridVLA`；因此 `model-agnostic` 应理解为 **validated on several recent VLA families**，而不是“任何 VLA 都已验证”。来源：[[raw/2509_21354_KV-Efficient-VLA.pdf]]，第 7 页 Table 1 与实验章节。

## 不可混写项
- `1.34×` 是三种 baseline 平均 speedup；单个模型的提升不同，后续不能写成统一无条件倍数。
- 理论 `1.61×` attention-level speedup 与经验 `1.34×` inference speedup 不是同一指标，引用时需要明确区分 theoretical vs empirical。
- 论文明确写到 accuracy 和 inference speed 只在单一 benchmark task 上评估，泛化到更广任务族的结论仍需收紧。

## 影响页面
- [[wiki/papers/2509_21354_KV-Efficient-VLA.md|2509_21354_KV-Efficient-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
