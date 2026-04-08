# 2602_06575_ThinkProprio-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_06575_ThinkProprio.md|2602_06575_ThinkProprio]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`58% lower latency` 主要锚定 `CALVIN ABC→D` 上 `22 ms vs 52 ms` 的 end-to-end inference setting，不应直接泛化到所有 benchmark 与部署环境。

## Evidence
- **real-world claim**：real-world manipulation 仅是有限范围 sanity check，不应与前述 benchmark 表现混成强 generalization 结论。来源：[[raw/2602_06575_ThinkProprio.pdf]]，第 1 页摘要与 Fig. 1；第 5-7 页 Tables 3-8。
- 更稳的单篇主命题应写成：`ThinkProprio` 证明让 proprioception 以 text-like token 更早进入 VLM 空间，并由 `instruction + proprio` 联合引导 token selection，可以在维持性能的同时显著压缩视觉计算；它更像 embodied visual reasoning / token selection 论文，而不是一般的动作头条件化设计。来源：[[raw/2602_06575_ThinkProprio.pdf]]，第 1 页摘要与 Fig. 1；第 3-4 页方法章节。
- 主证据锚点 1：来源：[[raw/2602_06575_ThinkProprio.pdf]]，摘要与总体命题：[[raw/2602_06575_ThinkProprio.pdf]] 第 1 页摘要与 Fig. 1。这里给出 “proprio tokenized into VLM space” 的总思路，以及 `15% visual tokens`、`58% lower latency` 的 headline。
- 主证据锚点 2：来源：[[raw/2602_06575_ThinkProprio.pdf]]，架构与 token 选择机制：[[raw/2602_06575_ThinkProprio.pdf]] 第 3-4 页 Fig. 2 与方法章节。这里定义 proprio text tokenization、query-guided retention、`Hctx`，以及为什么 instruction 与 proprio 的联合查询比单独使用更有效。
- 主证据锚点 3：来源：[[raw/2602_06575_ThinkProprio.pdf]]，主性能结果：[[raw/2602_06575_ThinkProprio.pdf]] 第 5-6 页 Table 2 与 Table 3。这里对应 `CALVIN ABC→D` 的 `4.55` Avg. Len.、`LIBERO` 的 `97.3%` avg. success，以及 `LIBERO-Long` 的 `95.2%`。

## Table / Metric Anchors
- 主性能结果：[[raw/2602_06575_ThinkProprio.pdf]] 第 5-6 页 Table 2 与 Table 3。这里对应 `CALVIN ABC→D` 的 `4.55` Avg. Len.、`LIBERO` 的 `97.3%` avg. success，以及 `LIBERO-Long` 的 `95.2%`。
- 效率结果：[[raw/2602_06575_ThinkProprio.pdf]] 第 5-6 页 Table 4 与 Table 5。这里对应 `15/100` 与 `6/34` token retention、`22 ms vs 52 ms` latency、以及 `1899 MB vs 1848 MB` 的 VRAM 对比。
- 关键消融：[[raw/2602_06575_ThinkProprio.pdf]] 第 6-7 页 Tables 6-8。这里说明 `text tokenization` 优于 `MLP projector`，`instruction + proprio` 联合 query 优于单独 `Hl` 或 `Hp`，以及为什么 `Hctx` 能弥补激进 token selection 的上下文损失。

## Table / Metric Split
- `主性能结果` 这一层应单独承载 `主性能结果` 相关的 benchmark / metric / operating point。 这里收口为：主性能结果：[[raw/2602_06575_ThinkProprio.pdf]] 第 5-6 页 Table 2 与 Table 3。这里对应 `CALVIN ABC→D` 的 `4.55` Avg. Len.、`LIBERO` 的 `97.3%` avg. success，以及 `LIBERO-Long` 的 `95.2%`。；`58% lower latency` 主要锚定 `CALVIN ABC→D` 上 `22 ms vs 52 ms` 的 end-to-end inference setting，不应直接泛化到所有 benchmark 与部署环境。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_06575_ThinkProprio.pdf]]，`主性能结果`。
- `效率结果` 这一层应单独承载 `效率结果` 相关的 benchmark / metric / operating point。 这里收口为：效率结果：[[raw/2602_06575_ThinkProprio.pdf]] 第 5-6 页 Table 4 与 Table 5。这里对应 `15/100` 与 `6/34` token retention、`22 ms vs 52 ms` latency、以及 `1899 MB vs 1848 MB` 的 VRAM 对比。；`58% lower latency` 主要锚定 `CALVIN ABC→D` 上 `22 ms vs 52 ms` 的 end-to-end inference setting，不应直接泛化到所有 benchmark 与部署环境。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_06575_ThinkProprio.pdf]]，`效率结果`。
- `关键消融` 这一层应单独承载 `关键消融` 相关的 benchmark / metric / operating point。 这里收口为：作者提出 `ThinkProprio`，将 proprioception 以 text token 形式在输入端与 instruction 融合，并用 `instruction + proprio` 共同指导 token selection。；更稳的单篇主命题应写成：`ThinkProprio` 证明让 proprioception 以 text-like token 更早进入 VLM 空间，并由 `instruction + proprio` 联合引导 token selection，可以在维持性能的同时显著压缩视觉计算；它更像 embodied visual reasoning / token selection 论文，而不是一般的动作头条件化设计。来源：[[raw/2602_06575_ThinkProprio.pdf]]，第 1 页摘要与 Fig. 1；第 3-4 页方法章节。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_06575_ThinkProprio.pdf]]，`关键消融`。

## 不可混写项
- `58% lower latency` 主要锚定 `CALVIN ABC→D` 上 `22 ms vs 52 ms` 的 end-to-end inference setting，不应直接泛化到所有 benchmark 与部署环境。
- `ThinkProprio` 的 real-world 结果在正文里被明确描述为有限范围的 sanity check，不是广泛 real-world generalization 证明；后续不应把它写成强 real-robot benchmark 论文。
- 在 `LIBERO` 上 `ThinkProprio` 并非 overall 最优（`LightVLA` 为 `97.4%`，`ThinkProprio` 为 `97.3%`），但它在 `LIBERO-Long` 上最强；后续 headline 需要决定更强调整体接近最优还是长时程优势。

## 影响页面
- [[wiki/papers/2602_06575_ThinkProprio.md|2602_06575_ThinkProprio]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
