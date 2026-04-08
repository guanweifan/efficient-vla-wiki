# 2603_03380_LiteVLA-Edge

## Source
- Raw: [[raw/2603_03380_LiteVLA-Edge.pdf]]
- Extracts manifest: [[extracts/parses/2603_03380_LiteVLA-Edge/manifest.json]]
- Primary text fallback: [[extracts/parses/2603_03380_LiteVLA-Edge/pdftotext.txt]]

## Claim
- 这篇论文要解决的是：多数 VLA 虽然具备统一的 perception-language-action 能力，但仍依赖云端或桌面级 GPU，难以在嵌入式机器人上实现完全离线、低延迟、可闭环的本地控制。
- 核心主张是：如果采用 compact multimodal backbone，并结合全精度监督式 image-to-action fine-tuning、后训练 `4-bit GGUF` 量化，以及 `llama.cpp` 的 GPU-accelerated runtime，就能在 Jetson Orin-class 硬件上把 VLA 推理压到接近 reactive control 的范围内，同时保持完整的本地 ROS 2 perception–reasoning–action pipeline。
- 作者提出 `LiteVLA-Edge`，它不是新的 policy objective，而是一条 deployment-oriented、fully on-device 的系统路径。论文 headline claim 是：在 Jetson AGX Orin 上 achieves `150.5 ms` mean end-to-end latency、约 `6.6 Hz` 推理频率，并保持极低 jitter（`σ = 0.125 ms`）；作者把这表述为相对之前 LiteVLA baseline 的约 `220%` improvement，并强调系统完全 offline、闭环可用。来源：[[raw/2603_03380_LiteVLA-Edge.pdf]]，第 1-2 页摘要与引言；第 3-5 页 Table I、Table II 与讨论章节。

## Methodology Index
- LiteVLA-Edge
- deployment-oriented VLA
- on-device multimodal control
- embedded robotics
- Jetson AGX Orin
- SmolVLM-256M
- supervised image-to-action fine-tuning
- FP32 training
- LoRA
- GGUF quantization
- 4-bit Q4_K_M
- llama.cpp CUDA runtime
- ROS 2 integration
- geometry_msgs/Twist
- closed-loop visuomotor control
- deterministic decoding
- low jitter
- offline execution
- reasoning-to-Hz tradeoff

## Data Pointer
- 摘要与总体定位：[[raw/2603_03380_LiteVLA-Edge.pdf]] 第 1-2 页摘要、引言与贡献列表。这里定义“不是新 policy，而是 practical on-device execution path”，以及 `150.5 ms / 6.6 Hz / fully offline / ROS 2` 的 headline。
- 系统结构与实现：[[raw/2603_03380_LiteVLA-Edge.pdf]] 第 2-4 页 Fig. 1、Section III-IV。这里说明 `SmolVLM-256M` backbone、FP32 + LoRA 微调、`Q4_K_M GGUF` 量化、以及在 Jetson 上的 CUDA offloading 配置。
- 主要性能结果：[[raw/2603_03380_LiteVLA-Edge.pdf]] 第 4 页 Table I 与 Table II。这里对应 `150.5 ms`、`6.64 Hz`、`σ = 0.13 ms`、以及与 `OpenVLA / EdgeVLA` 等系统在 design space 中的位置比较。
- 闭环可行性论证：[[raw/2603_03380_LiteVLA-Edge.pdf]] 第 4-5 页 closed-loop simulation evaluation 与 discussion。这里解释为什么 `150 ms` 被视为从 deliberative 转向 reactive / visual servoing 的阈值。
- 有效性边界：[[raw/2603_03380_LiteVLA-Edge.pdf]] 第 5 页 threats to validity 与 conclusion。这里明确论文只 claim deployability、timing feasibility 和 software integration，而不是 broad task-level superiority。

## 待核点
- `150.5 ms / 6.6 Hz` 是特定 deployment configuration（Jetson AGX Orin、`n_ctx=512`、最多 `12` 输出 token、全 `42` 层 offload）的结果，不应无条件泛化到所有 embedded hardware。
- 论文强调 `~220% improvement over previous baselines`，但比较对象主要是早期 LiteVLA / extreme-edge setup 与 design-space 位置，不是同条件下对所有 VLA 的 head-to-head task benchmark。
- `LiteVLA-Edge` 的主要贡献是 deployment path 与 latency feasibility，不是任务成功率或新控制算法；后续 taxonomy 需要避免把它写成 policy-method paper。
- 文中同时引用 `Jetson AGX Orin` 与 `Jetson Orin NX` 的实验描述，后续页面如果要统一硬件口径，需要再核对具体主结果到底锚定哪一套平台表述。
