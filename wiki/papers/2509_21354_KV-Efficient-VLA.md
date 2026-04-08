# 2509_21354_KV-Efficient-VLA

## Source
- Raw: [[raw/2509_21354_KV-Efficient-VLA.pdf]]
- Extracts manifest: [[extracts/parses/2509_21354_KV-Efficient-VLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2509_21354_KV-Efficient-VLA/pdftotext.txt]]
- Fine-grained locator: [[extracts/parses/2509_21354_KV-Efficient-VLA/pdftotext.bbox.html]]

## Claim
- 页面定位：这是一篇 **KV-cache compression / long-horizon inference efficiency** 论文；核心贡献是对历史上下文做 chunked KV compression 与 recurrent gating，而不是新 policy、本体训练或泛 benchmark 报告。
- 这篇论文要解决的是：VLA 在长时序推理中需要持续保留历史图像 token 的 key-value (`KV`) cache，导致 attention 计算和 KV 存储都随上下文增长而变重，难以满足实时机器人控制。
- 作者提出 `KV-Efficient VLA`，这是一个面向推理期的 memory compression 模块。它把历史 KV cache 按固定长度切成 chunk，对每个 chunk 做聚合，再用一个轻量 LSTM gate 决定哪些压缩后的 chunk 应该保留、哪些可以丢弃，同时保留最近窗口的原始细粒度 tokens。
- 论文主张：VLA 的推理瓶颈不只是模型规模，而是历史上下文在 KV cache 中的无界积累；通过 `chunked KV cache + recurrent gating`，可以在不改 downstream control logic 的前提下显著降低 FLOPs、推理延迟和 KV memory。
- headline numeric claims 包括：
  - 平均约 `24.6%` FLOPs savings。
  - 平均约 `1.34×` inference speedup。
  - 平均约 `1.87×` KV memory reduction。
  - 理论 cost-model 下 attention-level speedup 约 `1.61×`，memory speedup 约 `2.44×`。
  - 这些 empirical numbers 分别来自 `OpenVLA / CogACT / HybridVLA` 三个 baseline 的平均；而精度与收敛曲线的直接实验又主要围绕 `HybridVLA` 的 illustrative fine-tuning 展开。

## Methodology Index
- VLA inference efficiency
- KV cache compression
- chunked KV strategy
- recurrent gating
- LSTM gate
- fixed recent window
- compressed historical context
- attention FLOPs reduction
- KV memory reduction
- long-horizon inference
- LoRA compensation
- Open X-Embodiment fine-tuning
- RLBench evaluation
- OpenVLA / CogACT / HybridVLA comparison

## Data Pointer
- `PDF p.1` Abstract + Fig. 1：
  - 问题设定、`chunked KV + recurrent gating` 的核心思路，以及 `24.6% FLOPs savings / 1.34× speedup / 1.87× memory reduction` 的 headline 都在这里。
- `PDF p.2-5` Sec. 3 + Fig. 2：
  - KV-Efficient framework、chunking、MLP aggregation、LSTM gating、recent-window 保留策略，以及计算复杂度分析都在这里。
- `PDF p.6` Sec. 4.1：
  - 理论 cost-model 分析在这里；`1.61×` attention-level speedup 与 `2.44×` memory speedup 来自这一节。
- `PDF p.6-7` Sec. 4.2 + Fig. 3：
  - 实验设置、HybridVLA 上的 illustrative fine-tuning、以及 “only a single benchmark task” 的实验约束在这里。
- `PDF p.7` Table 1：
  - OpenVLA / CogACT / HybridVLA 及其 KV-Efficient 版本的 `Infer. Speed (Hz)`、`Total-FLOPs (T)` 与 speedup 对照都在这里。

## Evidence Links
- [[wiki/evidence/claims/2509_21354_KV-Efficient-VLA-headline-split.md|2509_21354_KV-Efficient-VLA-headline-split]]
- [[wiki/evidence/wording/model-agnostic-vs-validated-compatibility.md|model-agnostic-vs-validated-compatibility]]

## 待核点
- `1.34×` 是三种 baseline 平均 speedup；单个模型的提升不同，后续不能写成统一无条件倍数。
- 理论 `1.61×` attention-level speedup 与经验 `1.34×` inference speedup 不是同一指标，后续引用时需要明确区分 theoretical vs empirical。
- 论文明确写到 accuracy 和 inference speed 只在单一 benchmark task 上评估，泛化到更广任务族的结论仍需收紧。
- 文中说方法对 OpenVLA 与 CogACT 也可迁移，但实验设置部分又说明只在 HybridVLA 上进行 illustrative fine-tuning；后续若写“model-agnostic / transferable”，要保留这一证据强度 caveat。
