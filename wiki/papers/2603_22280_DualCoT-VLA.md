# 2603_22280_DualCoT-VLA

## Source
- Raw: [[raw/2603_22280_DualCoT-VLA.pdf]]
- Extracts manifest: [[extracts/parses/2603_22280_DualCoT-VLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2603_22280_DualCoT-VLA/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **visual-linguistic latent CoT** 方法论文；它的核心是把 reasoning 压入并行 latent space，同时增强空间感知与高层规划，而不是单纯做 system-level latency 优化。
- 这篇论文要解决的问题是：现有带 CoT 的 VLA 往往只能在**单一模态**里思考，并且依赖**自回归**方式逐步生成 reasoning token，因此同时面临两类限制：一是很难兼顾高层逻辑规划与低层空间感知，二是推理 latency 高且容易产生 compounding errors。作者据此提出 **DualCoT-VLA**，希望把 visual CoT 与 linguistic CoT 结合起来，并把 reasoning 从 step-by-step autoregressive decoding 改成 single-step parallel reasoning。来源：[[raw/2603_22280_DualCoT-VLA.pdf]]，第 1-2 页 Abstract、Introduction。
- 方法上的主张是一个 **visual-linguistic CoT paradigm**：用一组 visual CoT query tokens 蒸馏来自 **Depth Anything 3** 的几何 / 深度先验，用一组 linguistic CoT query tokens 通过 frozen auxiliary LLM 内化高层任务规划，再把两路 reasoning-enriched hidden states 一次性送入下游 action expert。其关键 framing 不是“显式生成更多思维文本”，而是**把 multimodal CoT 压入连续 latent space，并在单次 forward pass 中完成 reasoning**。来源：[[raw/2603_22280_DualCoT-VLA.pdf]]，第 2-4 页 Fig. 1、Sec. 3.1-3.2。
- 论文的 headline 结果需要拆成两层：
  - **task-performance claim**：在 **LIBERO** 上给出 `98.8% average success rate`，在 **RoboCasa GR1** 上给出 `55.1% average success rate across 24 tasks`，并报告 real-world 平台优于若干 baseline。
  - **reasoning-efficiency claim**：强调并行 latent reasoning 把 autoregressive CoT 的 `O(N)` sequential forward passes 改成 `O(1)`，并在单张 **H100 GPU** 上把总 latency 控制在 `83.2 ms`、接近 Non-CoT baseline。
- 更稳的单篇主命题应写成：DualCoT-VLA 是一篇 **multimodal implicit CoT + parallel latent reasoning** 论文；其核心创新是把 visual reasoning 与 linguistic reasoning 压入单次 forward pass，而不是继续显式逐 token 解码。性能结果、latency 结果与训练依赖边界应分开描述。来源：[[raw/2603_22280_DualCoT-VLA.pdf]]，第 8-11 页 Table 1、Table 2、Table 3、real-world section。

## Methodology Index
- visual-linguistic CoT
- parallel reasoning
- single-step forward reasoning
- implicit CoT
- learnable query tokens
- visual CoT query tokens
- linguistic CoT query tokens
- latent-space reasoning
- Depth Anything 3 distillation
- auxiliary LLM supervision
- action expert
- Flow-Matching DiT
- non-autoregressive reasoning
- multimodal planning
- spatial perception + logical planning

## Data Pointer
- **Abstract + Introduction**：第 1-2 页。适合后续补 “single-modal CoT + autoregressive reasoning” 的双重瓶颈，以及论文的总体 framing。
- **Figure 1 + Sec. 3.1-3.2**：第 3-4 页。适合后续补 dual query token、single forward reasoning、teacher modules 在训练 / 推理阶段的不同角色。
- **Table 1 / LIBERO results**：第 8-9 页。适合后续补 `98.8%` average SR、四个 suite 的具体表现，以及它与 LaRA-VLA / OpenVLA-OFT / Fast-ThinkAct 的差异。
- **Table 2 / RoboCasa GR1 results**：第 10 页。适合后续补 `55.1% across 24 tasks` 的具体 benchmark 语境及各类 task 的分布。
- **Table 3 / Table 4 / real-world section**：第 11 页及前后。适合后续补 `83.2 ms` latency、visual-only vs linguistic-only vs dual-stream 的互补性，以及 real-world baselines 对比。

## Evidence Links
- [[wiki/evidence/claims/2603_22280_DualCoT-VLA-headline-split.md|2603_22280_DualCoT-VLA-headline-split]]

## 待核点
- `98.8%`、`55.1%`、`83.2 ms` 分别对应 LIBERO、RoboCasa GR1 和单卡 H100 latency analysis；后续需要避免把这些数字误写成同一层面的综合结论。
- 论文同时强调 `parallel CoT`、`visual-linguistic CoT`、`implicit latent reasoning` 三种 framing；后续 taxonomy 需要统一其主定位。
- 真实世界部分目前只保留了“优于 OpenVLA-OFT / GR00T-N1.6”等高层 claim；后续需要进一步钉清任务种类、成功率和 platform setting。
- DualCoT-VLA 的 reasoning 增强依赖训练阶段的 auxiliary teacher modules；虽推理时可丢弃，但后续单篇页需要继续保留这一训练依赖边界，避免误写成完全 free lunch。
- 后续若把它放进“CoT acceleration”路线，需要明确它加速的是 reasoning realization 方式，而不是一般意义上的系统推理加速。
