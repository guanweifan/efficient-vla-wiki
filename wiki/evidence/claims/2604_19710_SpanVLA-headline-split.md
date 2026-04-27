# 2604_19710_SpanVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_19710_SpanVLA.md|2604_19710_SpanVLA]] 的单篇证据落点，用来拆分 action bridging、flow matching、GRPO/RFT 与 NAVSIM latency/performance headline。
- 本页聚焦的 headline bundle：`efficient action bridging`、`negative-recovery samples`、`NAVSIM SOTA` 与 `inference time reduction` 需要分层阅读。

## Evidence
- 核心证据命题：SpanVLA 将 autoregressive VLM reasoning 与 flow-matching action expert 相连，用 action bridge 和 historical trajectory initialization 生成未来轨迹，以降低长动作序列 autoregressive decoding 的延迟。来源：[[raw/2604_19710_SpanVLA.pdf]]，Abstract、Figure 1、action bridging method section。
- 补充证据命题：GRPO-based RFT 与 negative-recovery samples 主要被用于提高性能和 robustness；它们支持 SpanVLA 的长尾恢复能力，但不是 action-generation latency 的直接来源。来源：[[raw/2604_19710_SpanVLA.pdf]]，RFT section、mReasoning section、Figure 4 / Figure 5。
- 结果证据命题：Table 4 把 Autoregressive Decoding、SpanVLA L1 Head 与 SpanVLA FM 的 action policy 时间拆成 VLM encoding/prefilling、reasoning generation、trajectory generation 和 total time；SpanVLA FM 在 10/50 waypoint 设置下报告 `0.67s` total time。来源：[[raw/2604_19710_SpanVLA.pdf]]，Table 4。

## Table / Metric Anchors
- **Table 1-3**：NAVSIM v1/v2 主结果，用于 performance 层核对。
- **Table 4**：action policy efficiency 主表，用于拆 action generation time 与 total latency。
- **Table 5**：bridging layers 与 historical initialization ablation。
- **Figure 4 / Figure 5**：RFT 与 negative/recovery sample 配方影响。

## Table / Metric Split
- `0.67s` total time 是 action policy comparison 表中的 latency 口径，不等同于完整自动驾驶系统端到端部署 latency。
- PDMS / EPDMS 是 driving task performance 口径，不能直接替代 runtime 结论。
- GRPO/RFT 与 mReasoning 的收益属于 alignment / robustness / long-tail recovery，不应写成 action decoding 加速机制本身。

## 不可混写项
- 不应把 SpanVLA 归为单纯 latent reasoning；其主要效率设计是 action bridge + flow matching。
- 不应把 NAVSIM driving benchmark 的 action policy timing 外推到 manipulation control loop。
- 不应把 negative-recovery samples 写成减少推理开销的直接机制。

## 影响页面
- [[wiki/papers/2604_19710_SpanVLA.md|2604_19710_SpanVLA]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
