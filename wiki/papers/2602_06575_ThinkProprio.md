# 2602_06575_ThinkProprio

## Source
- Raw: [[raw/2602_06575_ThinkProprio.pdf]]
- Extracts manifest: [[extracts/parses/2602_06575_ThinkProprio/manifest.json]]
- Primary text fallback: [[extracts/parses/2602_06575_ThinkProprio/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **proprioception-guided visual token selection** 论文；它的核心贡献是让 proprioception 以 text-like token 形式更早进入视觉推理，而不是单纯在动作头后部追加状态条件。
- 这篇论文要解决的是：现有 VLA 往往把 proprioception 作为后期 conditioning signal 注入 action head，导致机器人状态难以在早期就参与 instruction understanding、visual token selection 与后续视觉推理，因此既浪费视觉计算，也难以充分利用 embodiment state。
- 核心主张是：如果把 proprioception 离散化成 text-like tokens，直接送入 VLM embedding space，并与 instruction 一起作为 query 去引导 visual token retention，那么机器人状态就能更早地塑造视觉推理过程；在这种设置下，只保留大约 `15%` 的 visual tokens 也可以维持甚至提升任务性能。
- 作者提出 `ThinkProprio`，将 proprioception 以 text token 形式在输入端与 instruction 融合，并用 `instruction + proprio` 共同指导 token selection。
- headline 结果需要拆开理解：
  - **latency claim**：端到端 inference latency 降低 `50%+`，在 `CALVIN ABC→D` 上从 `52 ms` 降到 `22 ms`；
  - **CALVIN task-performance claim**：`Avg. Len.` 从 `4.44` 提到 `4.55`；
  - **LIBERO claim**：average success 从 `96.9%` 到 `97.3%`，而 `LIBERO-Long` 上达到 `95.2%`；
  - **real-world claim**：real-world manipulation 仅是有限范围 sanity check，不应与前述 benchmark 表现混成强 generalization 结论。来源：[[raw/2602_06575_ThinkProprio.pdf]]，第 1 页摘要与 Fig. 1；第 5-7 页 Tables 3-8。
- 更稳的单篇主命题应写成：`ThinkProprio` 证明让 proprioception 以 text-like token 更早进入 VLM 空间，并由 `instruction + proprio` 联合引导 token selection，可以在维持性能的同时显著压缩视觉计算；它更像 embodied visual reasoning / token selection 论文，而不是一般的动作头条件化设计。来源：[[raw/2602_06575_ThinkProprio.pdf]]，第 1 页摘要与 Fig. 1；第 3-4 页方法章节。

## Methodology Index
- ThinkProprio
- proprioceptive tokenization
- text-tokenized proprioception
- proprioception in VLM space
- early fusion
- embodied visual reasoning
- physically grounded token selection
- query-guided token retention
- instruction + proprio query
- visual token pruning
- Hctx global context token
- cross-attention action head
- FLOWER backbone
- CALVIN
- LIBERO
- real-world manipulation sanity check
- latency / VRAM tradeoff
- proprioceptive encoding and entry point ablation

## Data Pointer
- 摘要与总体命题：[[raw/2602_06575_ThinkProprio.pdf]] 第 1 页摘要与 Fig. 1。这里给出 “proprio tokenized into VLM space” 的总思路，以及 `15% visual tokens`、`58% lower latency` 的 headline。
- 架构与 token 选择机制：[[raw/2602_06575_ThinkProprio.pdf]] 第 3-4 页 Fig. 2 与方法章节。这里定义 proprio text tokenization、query-guided retention、`Hctx`，以及为什么 instruction 与 proprio 的联合查询比单独使用更有效。
- 主性能结果：[[raw/2602_06575_ThinkProprio.pdf]] 第 5-6 页 Table 2 与 Table 3。这里对应 `CALVIN ABC→D` 的 `4.55` Avg. Len.、`LIBERO` 的 `97.3%` avg. success，以及 `LIBERO-Long` 的 `95.2%`。
- 效率结果：[[raw/2602_06575_ThinkProprio.pdf]] 第 5-6 页 Table 4 与 Table 5。这里对应 `15/100` 与 `6/34` token retention、`22 ms vs 52 ms` latency、以及 `1899 MB vs 1848 MB` 的 VRAM 对比。
- 关键消融：[[raw/2602_06575_ThinkProprio.pdf]] 第 6-7 页 Tables 6-8。这里说明 `text tokenization` 优于 `MLP projector`，`instruction + proprio` 联合 query 优于单独 `Hl` 或 `Hp`，以及为什么 `Hctx` 能弥补激进 token selection 的上下文损失。

## Evidence Links
- [[wiki/evidence/claims/2602_06575_ThinkProprio-headline-split.md|2602_06575_ThinkProprio-headline-split]]

## 待核点
- `58% lower latency` 主要锚定 `CALVIN ABC→D` 上 `22 ms vs 52 ms` 的 end-to-end inference setting，不应直接泛化到所有 benchmark 与部署环境。
- `ThinkProprio` 的 real-world 结果在正文里被明确描述为有限范围的 sanity check，不是广泛 real-world generalization 证明；后续不应把它写成强 real-robot benchmark 论文。
- 在 `LIBERO` 上 `ThinkProprio` 并非 overall 最优（`LightVLA` 为 `97.4%`，`ThinkProprio` 为 `97.3%`），但它在 `LIBERO-Long` 上最强；后续 headline 需要决定更强调整体接近最优还是长时程优势。
- 这篇既可以被理解为“proprioception integration design paper”，也可以被理解为“proprio-guided visual token selection paper”；后续需要决定页面主轴。
- 若后续把它并入一般 `token pruning` 路线，需要保留 “核心增益来自 proprio-guided query，而不是纯视觉 saliency pruning” 这一边界。
