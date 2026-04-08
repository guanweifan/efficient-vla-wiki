# 2602_20200_OptimusVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_20200_OptimusVLA.md|2602_20200_OptimusVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`98.6% / 13.5% / 38% / 42.9% / 52.4% / 2.9×` 分别来自不同 benchmark 与不同口径，后续不能压成一个无条件统一 headline。

## Evidence
- `2.9×` 则是 inference speedup 口径，并与 `NFE` 从 `10` 降到 `3.2 / 3.4` 强相关。来源：[[raw/2602_20200_OptimusVLA.pdf]]，第 1-3 页摘要、引言与 Fig. 1；第 5-7 页 Tables 1-5；第 6-7 页 Fig. 3-5。
- 补充证据命题：核心主张是：如果同时给 action generation 引入一个面向全局任务先验的 memory 和一个面向局部时间一致性的 memory，就能在不显著牺牲灵活性的前提下，缩短 generative path、减少 NFE，并提升长时程和真实机器人场景下的稳定性。 来源：[[raw/2602_20200_OptimusVLA.pdf]]，方法总览：[[raw/2602_20200_OptimusVLA.pdf]] 第 3-5 页 Fig. 2 与 Section 3。这里定义 `Prior Head`、`Memory Bank`、`Prior-Aware Sampler`、`Consistency Layer` 和 `Dynamic-Awareness module` 的作用分工。
- 主证据锚点 1：来源：[[raw/2602_20200_OptimusVLA.pdf]]，摘要与总框架：[[raw/2602_20200_OptimusVLA.pdf]] 第 1-3 页摘要、引言与 Fig. 1。这里给出 `GPM + LCM` 如何分别处理 prior-target gap 与 temporal dependence，以及 `98.6 / 13.5 / 38 / 2.9×` 的 headline。
- 主证据锚点 2：来源：[[raw/2602_20200_OptimusVLA.pdf]]，方法总览：[[raw/2602_20200_OptimusVLA.pdf]] 第 3-5 页 Fig. 2 与 Section 3。这里定义 `Prior Head`、`Memory Bank`、`Prior-Aware Sampler`、`Consistency Layer` 和 `Dynamic-Awareness module` 的作用分工。
- 主证据锚点 3：来源：[[raw/2602_20200_OptimusVLA.pdf]]，Simulation 主结果：[[raw/2602_20200_OptimusVLA.pdf]] 第 5-6 页 Table 1、Table 2、Table 3。这里对应 `LIBERO` 的 `98.6%`、`CALVIN` 的 `4.45 Avg. Len.` 与相对 `π0` 的 `13.5%` 提升，以及 `RoboTwin 2.0 Hard` 的 `38%` average success rate。

## Table / Metric Anchors
- Simulation 主结果：[[raw/2602_20200_OptimusVLA.pdf]] 第 5-6 页 Table 1、Table 2、Table 3。这里对应 `LIBERO` 的 `98.6%`、`CALVIN` 的 `4.45 Avg. Len.` 与相对 `π0` 的 `13.5%` 提升，以及 `RoboTwin 2.0 Hard` 的 `38%` average success rate。
- 组件归因：[[raw/2602_20200_OptimusVLA.pdf]] 第 6-7 页 Table 4、Table 5。这里说明去掉 `GPM` 或 `LCM` 带来的性能下降，以及 memory size / retrieved trajectory 数量对 `LIBERO-Long` 的影响。

## Table / Metric Split
- `Simulation 主结果` 这一层应单独承载 `Simulation 主结果` 相关的 benchmark / metric / operating point。 这里收口为：Simulation 主结果：[[raw/2602_20200_OptimusVLA.pdf]] 第 5-6 页 Table 1、Table 2、Table 3。这里对应 `LIBERO` 的 `98.6%`、`CALVIN` 的 `4.45 Avg. Len.` 与相对 `π0` 的 `13.5%` 提升，以及 `RoboTwin 2.0 Hard` 的 `38%` average success rate。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_20200_OptimusVLA.pdf]]，`Simulation 主结果`。
- `组件归因` 这一层应单独承载 `组件归因` 相关的 benchmark / metric / operating point。 这里收口为：组件归因：[[raw/2602_20200_OptimusVLA.pdf]] 第 6-7 页 Table 4、Table 5。这里说明去掉 `GPM` 或 `LCM` 带来的性能下降，以及 memory size / retrieved trajectory 数量对 `LIBERO-Long` 的影响。；论文同时强调 efficiency 和 robustness，其中 `GPM` 更偏 prior alignment / NFE reduction，`LCM` 更偏 temporal consistency / progress awareness；后续页面主轴需要决定更强调哪一侧。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_20200_OptimusVLA.pdf]]，`组件归因`。

## 不可混写项
- `98.6% / 13.5% / 38% / 42.9% / 52.4% / 2.9×` 分别来自不同 benchmark 与不同口径，后续不能压成一个无条件统一 headline。
- `2.9× inference speedup` 与 `NFE` 减少强相关，但具体口径依赖与 `π0 / π0.5` 的比较设置；若写效率结论，需要保留 benchmark 和 baseline 条件。
- 论文同时强调 efficiency 和 robustness，其中 `GPM` 更偏 prior alignment / NFE reduction，`LCM` 更偏 temporal consistency / progress awareness；后续页面主轴需要决定更强调哪一侧。

## 影响页面
- [[wiki/papers/2602_20200_OptimusVLA.md|2602_20200_OptimusVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
