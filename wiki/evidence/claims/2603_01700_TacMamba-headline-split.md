# 2603_01700_TacMamba-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_01700_TacMamba.md|2603_01700_TacMamba]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`100% success` 主要来自特定物理任务（尤其 sequential button pressing）与特定训练步数下的结果，不应直接泛化为所有 tactile-rich manipulation 的统一水平。

## Evidence
- `100Hz` 描述的是快触觉控制回路的硬实时要求，不等于整套视觉+触觉系统的统一端到端 VLA latency。来源：[[raw/2603_01700_TacMamba.pdf]]，第 1-2 页摘要与 Fig. 1；第 4-6 页 Table I、Table II、Fig. 4-6。
- 补充证据命题：核心主张是：如果把触觉流与视觉 VLA 解耦成一个“快触觉 / 慢视觉”的双系统结构，用一个 Mamba-based tactile encoder 在 `100Hz` 持续压缩触觉历史，再把压缩状态按需注入低频 VLA planner，就能同时满足硬实时约束与长时 tactile memory 需求。 来源：[[raw/2603_01700_TacMamba.pdf]]，架构与训练策略：[[raw/2603_01700_TacMamba.pdf]] 第 3-5 页 Fig. 3 与方法章节。这里说明 `Mamba` 触觉编码器、`Ternary Temporal Discrimination`、`Phase-Uniform Sampling`、以及 tactile soft prompt 如何与 VLA 解耦式集成。
- 主证据锚点 1：来源：[[raw/2603_01700_TacMamba.pdf]]，摘要与总体命题：[[raw/2603_01700_TacMamba.pdf]] 第 1-2 页摘要、引言与 Fig. 1。这里定义 `100Hz tactile System 1 + ~1Hz VLA System 2` 的异步架构，以及 `0.45 ms / 100% success / hard real-time` 的 headline。
- 主证据锚点 2：来源：[[raw/2603_01700_TacMamba.pdf]]，架构与训练策略：[[raw/2603_01700_TacMamba.pdf]] 第 3-5 页 Fig. 3 与方法章节。这里说明 `Mamba` 触觉编码器、`Ternary Temporal Discrimination`、`Phase-Uniform Sampling`、以及 tactile soft prompt 如何与 VLA 解耦式集成。
- 主证据锚点 3：来源：[[raw/2603_01700_TacMamba.pdf]]，编码器效率与离线精度：[[raw/2603_01700_TacMamba.pdf]] 第 5 页 Table I 与 Fig. 4。这里对应 `88.89%` accuracy、`0.45 ms` latency、与 Transformer / LSTM / CNN 的效率-精度比较。

## Table / Metric Anchors
- 编码器效率与离线精度：[[raw/2603_01700_TacMamba.pdf]] 第 5 页 Table I 与 Fig. 4。这里对应 `88.89%` accuracy、`0.45 ms` latency、与 Transformer / LSTM / CNN 的效率-精度比较。
- 真实任务主结果：[[raw/2603_01700_TacMamba.pdf]] 第 6-7 页 Table II、Fig. 5、Fig. 6。这里是 sequential button pressing、blind fries packing 的全局 success 与 atomic action success，尤其是 `TacMamba 100%` vs `π0.5 0%` 的强对比。

## Table / Metric Split
- `编码器效率与离线精度` 这一层应单独承载 `编码器效率与离线精度` 相关的 benchmark / metric / operating point。 这里收口为：编码器效率与离线精度：[[raw/2603_01700_TacMamba.pdf]] 第 5 页 Table I 与 Fig. 4。这里对应 `88.89%` accuracy、`0.45 ms` latency、与 Transformer / LSTM / CNN 的效率-精度比较。；`0.45 ms` 是 tactile encoder 本身的 inference latency，不等于整套视觉+触觉系统的端到端 VLA latency；若写效率结论，需要明确这是 System 1 编码器口径。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_01700_TacMamba.pdf]]，`编码器效率与离线精度`。
- `真实任务主结果` 这一层应单独承载 `真实任务主结果` 相关的 benchmark / metric / operating point。 这里收口为：真实任务主结果：[[raw/2603_01700_TacMamba.pdf]] 第 6-7 页 Table II、Fig. 5、Fig. 6。这里是 sequential button pressing、blind fries packing 的全局 success 与 atomic action success，尤其是 `TacMamba 100%` vs `π0.5 0%` 的强对比。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_01700_TacMamba.pdf]]，`真实任务主结果`。

## 不可混写项
- `100% success` 主要来自特定物理任务（尤其 sequential button pressing）与特定训练步数下的结果，不应直接泛化为所有 tactile-rich manipulation 的统一水平。
- `0.45 ms` 是 tactile encoder 本身的 inference latency，不等于整套视觉+触觉系统的端到端 VLA latency；若写效率结论，需要明确这是 System 1 编码器口径。
- 论文的 system baseline 主要是视觉-only `π0.5`；虽然表中列出其他视觉 memory baseline 的已发表数字，但当前工作更像是在证明“高频 tactile memory”这条路径，而不是全面 benchmark 所有 tactile-VLA。

## 影响页面
- [[wiki/papers/2603_01700_TacMamba.md|2603_01700_TacMamba]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
