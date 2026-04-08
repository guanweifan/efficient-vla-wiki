# 2512_20276_ActionFlow

## Source
- Raw: [[raw/2512_20276_ActionFlow.pdf]]
- Extracts manifest: [[extracts/parses/2512_20276_ActionFlow/manifest.json]]
- Primary text fallback: [[extracts/parses/2512_20276_ActionFlow/pdftotext.txt]]

## Claim
- 这篇论文提出 **ActionFlow**，它不是新的 VLA 架构或训练方法，而是一个面向边缘设备的 **system-level inference framework**。作者的核心判断是：当前 VLA 在 edge hardware 上真正的瓶颈不是视觉编码，而是 LLM autoregressive decoding 的 memory-bound decode phase，因此仅做量化、蒸馏或训练式并行解码，无法根治低频控制问题。来源：[[raw/2512_20276_ActionFlow.pdf]]，第 1-2 页 Abstract、Introduction。
- 核心方法主张是把单个 VLA 请求重构成由一个 Prefill 和多个 Decode 组成的 **macro-pipeline of micro-requests**，再通过 **Cross-Request Pipelining** 跨连续时间步把 compute-bound Prefill 与 memory-bound Decode 重叠执行。为支持这一调度，论文进一步提出 **Cross-Request State Packed Forward** 与 **Unified KV Ring Buffer**，把碎片化的 memory operations 融合成更致密的计算。来源：[[raw/2512_20276_ActionFlow.pdf]]，第 1-2 页 Abstract、贡献段；第 3-7 页 Sec. 3、Fig. 3、Fig. 4。
- 论文保留了非常清晰的 headline numeric claims：在 **OpenVLA-7B** 上，无需 retraining 即可取得约 **2.55×** FPS 提升；在 **Jetson AGX Orin** 上从 **1.25 FPS** 提升到 **3.20 FPS**，在 **RTX 5090** 上从 **7.62 FPS** 提升到 **19.45 FPS**。这些数字有信息量，但它们绑定在特定模型、特定实现和特定硬件上，更适合作为系统优化结果，而不是对所有 VLA 的普适速度结论。来源：[[raw/2512_20276_ActionFlow.pdf]]，第 1 页 Abstract；第 8-9 页 Table 1、Sec. 4。
- 从当前证据看，ActionFlow 的重点是**不改模型、不改训练、只改执行时系统组织方式**。它更像一篇 VLA serving / scheduler / runtime 系统论文，而不是 model compression 或 policy learning 论文。来源：[[raw/2512_20276_ActionFlow.pdf]]，第 1-3 页 Abstract、Introduction、Background；第 8-10 页 Evaluation、Conclusion。

## Methodology Index
- system-level VLA acceleration
- edge inference framework
- no-retraining acceleration
- Cross-Request Pipelining
- macro-pipeline of micro-requests
- Prefill / Decode overlap
- Cross-Request State Packed Forward
- Unified KV Ring Buffer
- packed execution
- autoregressive decode bottleneck
- memory-bound decode
- OpenVLA-7B serving
- Jetson AGX Orin
- RTX 5090
- real-time dynamic manipulation

## Data Pointer
- **Abstract**：第 1 页。适合后续回收 `20–30 Hz` 目标、`3–5 Hz` 现状、`2.55×` 提升和无 retraining 的 headline。
- **Figure 1 + Introduction**：第 1-2 页。适合后续补 VLA autoregressive action generation 的 latency framing，以及 edge deployment 问题定义。
- **Figure 2**：第 3 页。适合后续补为何 decode phase 是主要瓶颈，以及 Roofline 视角下的 memory-bound 问题。
- **Figure 3 / Sec. 3**：第 4-7 页。适合后续补 Cross-Request Pipelining 的流水线设计、Prefill/Decode overlap 和 pipeline state shift。
- **Figure 4 / Sec. 3.3**：第 6-7 页。适合后续补 Packed Forward 与 Unified KV Ring Buffer 的实现细节。
- **Table 1 / Table 2 / Figure 5**：第 8-10 页。适合后续补端到端性能、功能正确性验证、以及不同 workload 下的 sensitivity analysis。

## 待核点
- `2.55×`、`1.25 -> 3.20 FPS`、`7.62 -> 19.45 FPS`、`4.06×` 等数字来自不同硬件和 workload；后续需要拆清哪些属于默认 headline，哪些属于 sensitivity analysis。
- 论文围绕 OpenVLA-7B 展开，虽然方法表述更一般，但当前证据仍主要来自单一模型；后续需要决定在主题页里保留多强的泛化语气。
- ActionFlow 同时强调 `system-level`, `scheduler`, `operator fusion`, `KV cache management`；后续 taxonomy 需要统一它的主定位。
- 论文使用 `FPS` 与机器人控制 `Hz` 讨论实时性，后续需要在 evidence 层更清楚地区分“吞吐/帧率提升”和“真正闭环控制频率需求”的关系。
