# 2601_22153_DynamicVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2601_22153_DynamicVLA.md|2601_22153_DynamicVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`47.06%` 是 `DOM` simulation benchmark 上九个子维度的平均 success rate，不应被误读成任一单任务或 real-world 平均表现。

## Evidence
- `88 Hz` 与 `1.8 GB` 则是 `RTX A6000` 上的部署口径，而不是全部 real-world 系统的统一控制频率。来源：[[raw/2601_22153_DynamicVLA.pdf]]，第 1-2 页摘要与引言；第 6-7 页 Table I；第 12 页 implementation details。
- 补充证据命题：核心主张是：动态操作的主失败模式不是单纯视觉歧义，而是时序失配；因此如果同时做 `compact low-latency VLA backbone`、`Continuous Inference` 和 `Latent-aware Action Streaming (LAAS)`，让推理与执行重叠、并丢弃过时 action，就能显著提升 closed-loop reactivity、dynamic adaptation 与 long-horizon sequencing。 来源：[[raw/2601_22153_DynamicVLA.pdf]]，方法总览：[[raw/2601_22153_DynamicVLA.pdf]] 第 3-5 页 Fig. 2 与 Section III。这里定义 `Continuous Inference` 如何重叠推理和执行，以及 `LAAS` 如何丢弃过时 action、恢复 temporal alignment。
- 主证据锚点 1：来源：[[raw/2601_22153_DynamicVLA.pdf]]，摘要与总体命题：[[raw/2601_22153_DynamicVLA.pdf]] 第 1-2 页摘要、引言与 Fig. 1。这里给出 `0.4B backbone + CI + LAAS + DOM benchmark` 的总框架，以及 dynamic manipulation 的问题定义。
- 主证据锚点 2：来源：[[raw/2601_22153_DynamicVLA.pdf]]，方法总览：[[raw/2601_22153_DynamicVLA.pdf]] 第 3-5 页 Fig. 2 与 Section III。这里定义 `Continuous Inference` 如何重叠推理和执行，以及 `LAAS` 如何丢弃过时 action、恢复 temporal alignment。
- 主证据锚点 3：来源：[[raw/2601_22153_DynamicVLA.pdf]]，DOM simulation 主结果：[[raw/2601_22153_DynamicVLA.pdf]] 第 6-7 页 Table I。这里是九个子维度、整体 `47.06%` 平均 success rate、以及 `Path Length / Time` 对比的主要来源。

## Table / Metric Anchors
- DOM simulation 主结果：[[raw/2601_22153_DynamicVLA.pdf]] 第 6-7 页 Table I。这里是九个子维度、整体 `47.06%` 平均 success rate、以及 `Path Length / Time` 对比的主要来源。
- 组件与速度消融：[[raw/2601_22153_DynamicVLA.pdf]] 第 8-9 页 Table II；第 12 页 implementation details。这里说明 `0.4B` 容量、`FastViT`、`CI`、`LAAS` 的各自贡献，以及 `1.8 GB / 88 Hz` 的部署信息。

## Table / Metric Split
- `DOM simulation 主结果` 这一层应单独承载 `DOM simulation 主结果` 相关的 benchmark / metric / operating point。 这里收口为：DOM simulation 主结果：[[raw/2601_22153_DynamicVLA.pdf]] 第 6-7 页 Table I。这里是九个子维度、整体 `47.06%` 平均 success rate、以及 `Path Length / Time` 对比的主要来源。；`47.06%` 是 `DOM` simulation benchmark 上九个子维度的平均 success rate，不应被误读成任一单任务或 real-world 平均表现。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2601_22153_DynamicVLA.pdf]]，`DOM simulation 主结果`。
- `组件与速度消融` 这一层应单独承载 `组件与速度消融` 相关的 benchmark / metric / operating point。 这里收口为：页面定位：这是一篇 **dynamic object manipulation VLA + execution design** 论文；它的核心不是单纯做小模型，而是同时用 compact backbone、continuous inference 和 `LAAS` 去解决 perception-execution gap。；作者提出 `DynamicVLA`，使用 `0.4B` 参数量 backbone，并配套 `DOM` benchmark 与自动化仿真/真实世界数据管线。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2601_22153_DynamicVLA.pdf]]，`组件与速度消融`。

## 不可混写项
- `47.06%` 是 `DOM` simulation benchmark 上九个子维度的平均 success rate，不应被误读成任一单任务或 real-world 平均表现。
- `88 Hz` 与 `1.8 GB` 来自 `RTX A6000` 上的 inference setting；这更像模型级推理能力，不等于整个真实机器人闭环系统在所有平台上的端到端控制频率。
- 论文的强点既可以写成“compact low-latency VLA architecture”，也可以写成“CI + LAAS 解决 perception-execution gap 的 execution design”；仍需决定页面主轴。

## 影响页面
- [[wiki/papers/2601_22153_DynamicVLA.md|2601_22153_DynamicVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
