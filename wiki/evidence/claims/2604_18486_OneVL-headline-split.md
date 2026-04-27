# 2604_18486_OneVL-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_18486_OneVL.md|2604_18486_OneVL]] 的单篇证据落点，用来拆分 OneVL 的 latent reasoning、world-model supervision、prefill latency 与 benchmark performance。
- 本页聚焦的 headline bundle：`one-step latent reasoning`、`surpass explicit CoT`、`answer-only latency` 和 `world model` 不能混写成“免费推理”。

## Evidence
- 核心证据命题：OneVL 认为纯语言 latent CoT 对驾驶 trajectory prediction 不足，因为它缺少对 road geometry、agent motion 和 scene dynamics 的约束；因此用 language auxiliary decoder 与 visual world-model decoder 共同监督 compact latent tokens。来源：[[raw/2604_18486_OneVL.pdf]]，Abstract、Introduction、Figure 2。
- 推理证据命题：推理期 auxiliary decoders 被丢弃，视觉和语言 latent tokens 被放入 prefill phase，而不是逐 token autoregressive decode；论文据此宣称 latency 接近 answer-only prediction。来源：[[raw/2604_18486_OneVL.pdf]]，Section 3.6、Figure 3。
- 结果证据命题：论文在 NAVSIM、ROADWork、Impromptu、APR1 上报告 accuracy / trajectory metrics 与 latency；例如 NAVSIM 中 OneVL latency `4.46s` 接近 AR answer-only `4.49s`，ROADWork 与 Impromptu 也给出对应 latency 表。来源：[[raw/2604_18486_OneVL.pdf]]，Table 1-5、Main Results。

## Table / Metric Anchors
- **Figure 1**：四个 benchmark 上的 accuracy / efficiency overview。
- **Table 1**：NAVSIM PDM-score 与 latency。
- **Table 2**：ROADWork ADE / FDE 与 latency。
- **Table 3 / Table 4**：Impromptu 结果。
- **Table 5**：APR1 结果。
- **Table 7**：language decoder、visual decoder、three-stage training 的 ablation。
- **Table 8**：MLP-head deployment variant 的 accuracy-latency trade-off。

## Table / Metric Split
- `answer-only latency` 对应 prefill inference；不表示训练期没有 auxiliary supervision。
- `surpass explicit CoT` 是 benchmark-specific performance claim；必须和 NAVSIM / ROADWork / Impromptu / APR1 的指标口径一起读。
- `world model` 在此页指 visual auxiliary decoder 的 future-frame token prediction objective；不是通用 world-model deployment stack。

## 不可混写项
- 不应把 OneVL 写成 teacher-free 或 supervision-free latent reasoning；它依赖文本 CoT 与视觉 future prediction supervision。
- 不应把 0.24s MLP head 变体与 full OneVL 的 4.46s NAVSIM latency 混写。
- 不应把 autonomous-driving trajectory prediction 的结论直接外推到 manipulation setting。

## 影响页面
- [[wiki/papers/2604_18486_OneVL.md|2604_18486_OneVL]]
- [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
