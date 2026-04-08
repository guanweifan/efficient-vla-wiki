# 2603_03380_LiteVLA-Edge-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_03380_LiteVLA-Edge.md|2603_03380_LiteVLA-Edge]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`150.5 ms / 6.6 Hz` 是特定 deployment configuration（Jetson AGX Orin、`n_ctx=512`、最多 `12` 输出 token、全 `42` 层 offload）的结果，不应无条件泛化到所有 embedded hardware。

## Evidence
- 约 `220%` improvement 则是相对早期 LiteVLA baseline / extreme-edge setup 的系统级比较，不是统一 task benchmark 胜率。来源：[[raw/2603_03380_LiteVLA-Edge.pdf]]，第 1-2 页摘要与引言；第 3-5 页 Table I、Table II 与讨论章节。
- 补充证据命题：核心主张是：如果采用 compact multimodal backbone，并结合全精度监督式 image-to-action fine-tuning、后训练 `4-bit GGUF` 量化，以及 `llama.cpp` 的 GPU-accelerated runtime，就能在 Jetson Orin-class 硬件上把 VLA 推理压到接近 reactive control 的范围内，同时保持完整的本地 ROS 2 perception–reasoning–action pipeline。 来源：[[raw/2603_03380_LiteVLA-Edge.pdf]]，系统结构与实现：[[raw/2603_03380_LiteVLA-Edge.pdf]] 第 2-4 页 Fig. 1、Section III-IV。这里说明 `SmolVLM-256M` backbone、FP32 + LoRA 微调、`Q4_K_M GGUF` 量化、以及在 Jetson 上的 CUDA offloading 配置。
- 主证据锚点 1：来源：[[raw/2603_03380_LiteVLA-Edge.pdf]]，摘要与总体定位：[[raw/2603_03380_LiteVLA-Edge.pdf]] 第 1-2 页摘要、引言与贡献列表。这里定义“不是新 policy，而是 practical on-device execution path”，以及 `150.5 ms / 6.6 Hz / fully offline / ROS 2` 的 headline。
- 主证据锚点 2：来源：[[raw/2603_03380_LiteVLA-Edge.pdf]]，系统结构与实现：[[raw/2603_03380_LiteVLA-Edge.pdf]] 第 2-4 页 Fig. 1、Section III-IV。这里说明 `SmolVLM-256M` backbone、FP32 + LoRA 微调、`Q4_K_M GGUF` 量化、以及在 Jetson 上的 CUDA offloading 配置。
- 主证据锚点 3：来源：[[raw/2603_03380_LiteVLA-Edge.pdf]]，主要性能结果：[[raw/2603_03380_LiteVLA-Edge.pdf]] 第 4 页 Table I 与 Table II。这里对应 `150.5 ms`、`6.64 Hz`、`σ = 0.13 ms`、以及与 `OpenVLA / EdgeVLA` 等系统在 design space 中的位置比较。

## Table / Metric Anchors
- 主要性能结果：[[raw/2603_03380_LiteVLA-Edge.pdf]] 第 4 页 Table I 与 Table II。这里对应 `150.5 ms`、`6.64 Hz`、`σ = 0.13 ms`、以及与 `OpenVLA / EdgeVLA` 等系统在 design space 中的位置比较。

## Table / Metric Split
- `主要性能结果` 这一层应单独承载 `主要性能结果` 相关的 benchmark / metric / operating point。 这里收口为：主要性能结果：[[raw/2603_03380_LiteVLA-Edge.pdf]] 第 4 页 Table I 与 Table II。这里对应 `150.5 ms`、`6.64 Hz`、`σ = 0.13 ms`、以及与 `OpenVLA / EdgeVLA` 等系统在 design space 中的位置比较。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_03380_LiteVLA-Edge.pdf]]，`主要性能结果`。

## 不可混写项
- `150.5 ms / 6.6 Hz` 是特定 deployment configuration（Jetson AGX Orin、`n_ctx=512`、最多 `12` 输出 token、全 `42` 层 offload）的结果，不应无条件泛化到所有 embedded hardware。
- 论文强调 `~220% improvement over previous baselines`，但比较对象主要是早期 LiteVLA / extreme-edge setup 与 design-space 位置，不是同条件下对所有 VLA 的 head-to-head task benchmark。
- `LiteVLA-Edge` 的主要贡献是 deployment path 与 latency feasibility，不是任务成功率或新控制算法；后续 taxonomy 需要避免把它写成 policy-method paper。

## 影响页面
- [[wiki/papers/2603_03380_LiteVLA-Edge.md|2603_03380_LiteVLA-Edge]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
