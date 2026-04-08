# 2505_08243_ECoT-Lite-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2505_08243_ECoT-Lite.md|2505_08243_ECoT-Lite]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`10-19%` 的提升口径来自 BridgeData V2 相对“state-of-the-art conventional VLAs”的表述；后续 L2 需要把具体 split、具体 baseline 和绝对数值拆开。

## Evidence
- 作者最终主推的轻量方案是 `reasoning pre-training` 和 `reasoning dropout`。论文声称它们在 `LIBERO-90` 上达到或接近 SOTA，并且在 BridgeData V2 上相对标准非 reasoning VLA 提升 `10-19%`；另一方面，`1-1.2 Hz -> 3.5+ Hz` 的 headline 是相对 **full ECoT / 标准 embodied reasoning** 的推理频率比较，不应误写成相对普通标准 VLA 的统一提速。来源：[[raw/2505_08243_ECoT-Lite.pdf]]，第 1 页摘要；第 7-8 页 Fig. 5 与 Section 7。
- 补充证据命题：核心主张是：embodied reasoning 的收益并不完全来自“测试时真的生成长 reasoning”，而可以拆成表示学习、训练课程化、表达能力等若干机制来分析；基于这种拆解，可以设计更轻量的 `ECoT-Lite` 训练配方，在不保留测试时 reasoning 生成的情况下，仍保住大部分性能收益。 来源：[[raw/2505_08243_ECoT-Lite.pdf]]，轻量 training recipes 的定义：[[raw/2505_08243_ECoT-Lite.pdf]] 第 4-5 页 Section 5 与 Fig. 3。这里系统定义 `reasoning pre-training`、`co-training`、`reasoning dropout`、`reasoning scaffolding`、`thinking tokens` 这几种 recipe。
- 主证据锚点 1：来源：[[raw/2505_08243_ECoT-Lite.pdf]]，摘要与总览：[[raw/2505_08243_ECoT-Lite.pdf]] 第 1 页摘要与 Fig. 1。这里给出问题设定、三种机制假设，以及 `3x` 推理提速与实用化动机。
- 主证据锚点 2：来源：[[raw/2505_08243_ECoT-Lite.pdf]]，轻量 training recipes 的定义：[[raw/2505_08243_ECoT-Lite.pdf]] 第 4-5 页 Section 5 与 Fig. 3。这里系统定义 `reasoning pre-training`、`co-training`、`reasoning dropout`、`reasoning scaffolding`、`thinking tokens` 这几种 recipe。
- 主证据锚点 3：来源：[[raw/2505_08243_ECoT-Lite.pdf]]，主实验结果：[[raw/2505_08243_ECoT-Lite.pdf]] 第 7 页 Fig. 5；第 17 页 Table 1；第 19-20 页 Table 2。这里分别对应 LIBERO-90 总体结果、数值化 benchmark 结果，以及 Bridge 上的 per-task 表现。

## Table / Metric Anchors
- 主实验结果：[[raw/2505_08243_ECoT-Lite.pdf]] 第 7 页 Fig. 5；第 17 页 Table 1；第 19-20 页 Table 2。这里分别对应 LIBERO-90 总体结果、数值化 benchmark 结果，以及 Bridge 上的 per-task 表现。

## Table / Metric Split
- `主实验结果` 这一层应单独承载 `主实验结果` 相关的 benchmark / metric / operating point。 当前这一层分别对应 LIBERO-90 总体结果、数值化 benchmark 结果，以及 Bridge 上的 per-task 表现。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2505_08243_ECoT-Lite.pdf]]，`主实验结果`。

## 不可混写项
- `10-19%` 的提升口径来自 BridgeData V2 相对“state-of-the-art conventional VLAs”的表述；后续 L2 需要把具体 split、具体 baseline 和绝对数值拆开。
- `3x inference speedup` 的比较对象是“标准 embodied reasoning / full ECoT”，不是所有 VLA；后续不要把它误写成相对标准 VLA 本身的 3x 提速。
- 论文中的 `ECoT-Lite` 是一个 umbrella term，包含多种 recipe，但真正表现最好的主要是 `reasoning pre-training` 和 `reasoning dropout`；chief-editor 需决定 paper-level 默认强调哪两个。

## 影响页面
- [[wiki/papers/2505_08243_ECoT-Lite.md|2505_08243_ECoT-Lite]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
