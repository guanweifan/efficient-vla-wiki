# 2510_18337_MOTVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2510_18337_MOTVLA.md|2510_18337_MOTVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：论文把 reasoning、latency、language steerability、policy performance 统一写成系统优势；后续 evidence 层需要把这些拆开，而不是继续沿用 bundled superiority claim。

## Evidence
- 核心证据命题：MoTVLA 的核心主张不是单纯“把 reasoning 接进 policy”，而是要在一个统一架构中同时保住 language steerability 与 inference efficiency。论文认为，现有路线要么不显式生成 reasoning，因此语言引导不足；要么把 reasoning 作为 next-token 生成结果再喂给 diffusion policy，导致推理延迟过高。为了解这个矛盾，MoTVLA 提出一种 Mixture-of-Transformers (MoT) 式的 VLA：用 generalist 负责 slow reasoning，用与其共享全局注意力的 domain expert 负责 fast reasoning，再把 fast reasoning 生成的 motion decomposition 与视觉 / 机器人状态一起送入 action expert（DiT）生成动作。 来源：[[raw/2510_18337_MOTVLA.pdf]]，**Abstract / introduction**：最直接说明论文要解决的矛盾是 language steerability vs reasoning latency，并给出 unified fast-slow reasoning 的总框架。
- 补充证据命题：更稳的 headline 应拆开理解：`fast reasoning` 的质量与 token accuracy 主要来自 `Table 1`；manipulation performance 来自 `Table 2`；language steerability 在 `table bussing` 上主要还是 qualitative evidence；reasoning latency 则来自附录 `Table 4`，且主实验使用的是 `MoTVLA-14B`，`1B/0.5B` 主要用于 latency illustration。更准确的写法是：**MoTVLA 在统一架构里同时改善 reasoning latency、language-conditioned behavior 和 manipulation performance，但这些优势来自不同实验层面，不应压成单一 bundled superiority claim。** 来源：[[raw/2510_18337_MOTVLA.pdf]]，**Figure 1 (p.2)**：统一 fast-slow reasoning 的总图，也是“Mixture-of-Transformers 为什么能兼顾效率和 reasoning” 的第一锚点。
- 主证据锚点 1：来源：[[raw/2510_18337_MOTVLA.pdf]]，**Abstract / introduction**：最直接说明论文要解决的矛盾是 language steerability vs reasoning latency，并给出 unified fast-slow reasoning 的总框架。
- 主证据锚点 2：来源：[[raw/2510_18337_MOTVLA.pdf]]，**Figure 1 (p.2)**：统一 fast-slow reasoning 的总图，也是“Mixture-of-Transformers 为什么能兼顾效率和 reasoning” 的第一锚点。
- 主证据锚点 3：来源：[[raw/2510_18337_MOTVLA.pdf]]，**Figure 2 (p.4)**：MoTVLA 整体框架图，若要补 `L2`，这是 generalist / domain expert / action expert 三者关系的第一方法锚点。

## Table / Metric Anchors
- **Table 1 (p.7)**：fast reasoning 在 robotics 与 LLaVA-OV VQA 任务上的主要结果锚点，用来支撑“fast reasoning 既快又有用”。
- **Table 2 (p.10)**：manipulation task 的主要对比表，用来支撑 simulation / real-world policy performance 的主张。
- **Table 3 (p.11)**：架构消融锚点，用来区分 generalist、domain expert、global attention 共享机制分别贡献了什么。
- **Appendix latency section / Table 4 (p.16)**：关于 `MoTVLA-14B`、`1B/0.5B` reasoning latency 的主要锚点，但应注意这些缩放结果主要服务于 latency 分析，而不是主任务结论。

## Table / Metric Split
- `**Table 1 (p.7)**` 这一层应单独承载 `**Table 1 (p.7)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2510_18337_MOTVLA.pdf]]，`**Table 1 (p.7)**`。
- `**Table 2 (p.10)**` 这一层应单独承载 `**Table 2 (p.10)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2510_18337_MOTVLA.pdf]]，`**Table 2 (p.10)**`。
- `**Table 3 (p.11)**` 这一层应单独承载 `**Table 3 (p.11)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2510_18337_MOTVLA.pdf]]，`**Table 3 (p.11)**`。
- `**Appendix latency section / Table 4 (p.16)**` 这一层应单独承载 `**Appendix latency section / Table 4 (p.16)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2510_18337_MOTVLA.pdf]]，`**Appendix latency section / Table 4 (p.16)**`。

## 不可混写项
- 论文把 reasoning、latency、language steerability、policy performance 统一写成系统优势；后续 evidence 层需要把这些拆开，而不是继续沿用 bundled superiority claim。
- `MoTVLA-14B` 是主实验模型，`1B/0.5B` 主要用于 latency 比较；若写模型规模相关结论，需要显式区分，不可混用。
- table bussing 里的 language steerability 目前主要是 qualitative 证据；仍需决定这类行为证据在 wiki 中是单独归档到 qualitative evidence，还是仍保留在单篇页 narrative 中。

## 影响页面
- [[wiki/papers/2510_18337_MOTVLA.md|2510_18337_MOTVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
