# 2603_06480_A-MMR-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_06480_A-MMR.md|2603_06480_A-MMR]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`17.81%`、`10.96 ms` 等 headline 数字目前仍是 bundled summary，仍需分别拆到 R2R、RxR、具体 pruning ratio 与具体比较对象。

## Evidence
- 核心证据命题：这篇论文的核心命题是：VLA-based vision-language navigation 的 token pruning 不应把所有视觉 token 视为同质对象，因为 VLN 是一个显式依赖历史观测的长时序任务；如果像单帧 VLM 那样统一裁剪，就会破坏当前视角与历史记忆之间的时空关系。 来源：[[raw/2603_06480_A-MMR.pdf]]，**Abstract / introduction**：最清楚地给出“为什么 VLN pruning 不能等同于普通 VLM pruning”的任务 framing。
- 补充证据命题：为此，论文提出一个 training-free 的 history-conditioned spatio-temporal visual token pruning 框架，其关键思想是**把 current frame 与 history frames 区别对待**：当前视角做 spatial token selection，历史记忆做 query-guided spatio-temporal compression，并统一由 Adaptive Maximal Marginal Relevance (A-MMR) 来平衡 saliency 与 diversity。 来源：[[raw/2603_06480_A-MMR.pdf]]，**Fig. 1 (p.1)**：不同 pruning 方法在 R2R 上的 SPL-效率图，是 “高 pruning 下仍保持性能” 的第一锚点。
- 主证据锚点 1：来源：[[raw/2603_06480_A-MMR.pdf]]，**Abstract / introduction**：最清楚地给出“为什么 VLN pruning 不能等同于普通 VLM pruning”的任务 framing。
- 主证据锚点 2：来源：[[raw/2603_06480_A-MMR.pdf]]，**Fig. 1 (p.1)**：不同 pruning 方法在 R2R 上的 SPL-效率图，是 “高 pruning 下仍保持性能” 的第一锚点。
- 主证据锚点 3：来源：[[raw/2603_06480_A-MMR.pdf]]，**Fig. 2 (p.3)**：current/history 两类 token 如何分别进入 A-MMR 与 query-guided reweighting 的总流程图。

## Table / Metric Anchors
- **TABLE I (p.5)**：R2R / RxR 主结果锚点，用来核对不同 pruning ratio 下的 SR、SPL、OS、NE、nDTW 变化。
- **TABLE II (p.6)**：A-MMR 与 Query-Guided Reweighting 的消融锚点，用来判断 saliency、diversity、merging 等组件是否都有独立贡献。
- **TABLE III (p.6)**：FPS / TFLOPs / CUDA latency 的效率表，用来核对 `10.96 ms` 等 latency 优势。

## Table / Metric Split
- `**TABLE I (p.5)**` 这一层应单独承载 `**TABLE I (p.5)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_06480_A-MMR.pdf]]，`**TABLE I (p.5)**`。
- `**TABLE II (p.6)**` 这一层应单独承载 `**TABLE II (p.6)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_06480_A-MMR.pdf]]，`**TABLE II (p.6)**`。
- `**TABLE III (p.6)**` 这一层应单独承载 `**TABLE III (p.6)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_06480_A-MMR.pdf]]，`**TABLE III (p.6)**`。

## 不可混写项
- `17.81%`、`10.96 ms` 等 headline 数字目前仍是 bundled summary，仍需分别拆到 R2R、RxR、具体 pruning ratio 与具体比较对象。
- 论文把 A-MMR 与 Query-Guided Reweighting 一起包装成整体方法；后续 evidence 层可能需要区分“current-frame saliency/diversity 选择”的贡献与“history-memory reweighting”的贡献。
- 论文强调方法是 training-free、plug-and-play 的 VLN pruning 框架，但当前直接证据主要基于 StreamVLN 与 VLN benchmark；仍应明确它向更一般 VLA navigation / non-navigation setting 的外推边界。

## 影响页面
- [[wiki/papers/2603_06480_A-MMR.md|2603_06480_A-MMR]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
