# 2603_01581_KERV-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_01581_KERV.md|2603_01581_KERV]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`27%∼37% acceleration` 是相对 `SpecVLA` 的 headline；`1.48×∼1.57× speedup` 则是相对 naive `VLA+SD`，后续不能把两组数字混成同一比较口径。

## Evidence
- 核心证据命题：这篇论文要解决的是：把 `speculative decoding (SD)` 用到 VLA 上时，现有做法仍有两个主要瓶颈，一是 token error 需要依赖高成本 `re-inference` 修正，二是 relaxed acceptance threshold 很难稳定设定，导致 speed-accuracy trade-off 不稳。 来源：[[raw/2603_01581_KERV.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 补充证据命题：作者提出 `KERV`，核心是把 token-domain VLA 与 kinematic-domain prediction 结合起来：用基于 `Kalman Filter` 的运动学预测补偿 SD 误差，从而减少昂贵的 re-inference；再用基于 `kinematic variability` 的动态阈值调整替代固定 acceptance threshold。 来源：[[raw/2603_01581_KERV.pdf]]，两个核心问题、`Kalman Filter + dynamic threshold` 的高层方案，以及 `27%∼37% acceleration` headline 都在这里。
- 主证据锚点 1：来源：[[raw/2603_01581_KERV.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 主证据锚点 2：来源：[[raw/2603_01581_KERV.pdf]]，两个核心问题、`Kalman Filter + dynamic threshold` 的高层方案，以及 `27%∼37% acceleration` headline 都在这里。
- 主证据锚点 3：来源：[[raw/2603_01581_KERV.pdf]]，`PDF p.3-6` Fig. 2 / Fig. 3 / Fig. 4 / Fig. 5：

## Table / Metric Anchors
- `PDF p.8-9` Table 2：
  - `KERV` 与 naive `VLA+SD`、`SpecVLA` 在不同 `LIBERO` task suites 上的 end-to-end speedup / SR 对比应回这里。
- `PDF p.9` Table 3：
  - `CM`、`TA` 等组件 ablation 在这里，适合后续拆“加速来自补偿机制还是阈值调整”。
- `PDF p.9-10` Table 4 + system implementation discussion：
  - `CPU+GPU` 实现与额外 `7%∼13%` acceleration contribution 的硬件实现分析应回这里。

## Table / Metric Split
- ``PDF p.8-9` Table 2` 这一层支撑 ``PDF p.8-9` Table 2` 对应的 benchmark / metric / operating point。 - `KERV` 与 naive `VLA+SD`、`SpecVLA` 在不同 `LIBERO` task suites 上的 end-to-end speedup / SR 对比应回这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2603_01581_KERV.pdf]]，``PDF p.8-9` Table 2`。
- ``PDF p.9` Table 3` 这一层支撑 ``PDF p.9` Table 3` 对应的 benchmark / metric / operating point。 - `CM`、`TA` 等组件 ablation 在这里，适合后续拆“加速来自补偿机制还是阈值调整”。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2603_01581_KERV.pdf]]，``PDF p.9` Table 3`。
- ``PDF p.9-10` Table 4 + system implementation discussion` 这一层支撑 ``PDF p.9-10` Table 4 + system implementation discussion` 对应的 benchmark / metric / operating point。 - `CPU+GPU` 实现与额外 `7%∼13%` acceleration contribution 的硬件实现分析应回这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2603_01581_KERV.pdf]]，``PDF p.9-10` Table 4 + system implementation discussion`。

## 不可混写项
- `27%∼37% acceleration` 是相对 `SpecVLA` 的 headline；`1.48×∼1.57× speedup` 则是相对 naive `VLA+SD`，后续不能把两组数字混成同一比较口径。
- “nearly no SR loss” 是整体摘要式说法，但正文也提到相对 `SpecVLA` 在部分环境上仍有约 `1.5%` 和 `0.4%` 的 `SR` 下降；引用时要保留这种 tradeoff。
- 当前主实验建立在 `LIBERO` 四个 task suites 与作者的实现配置上；推广到更广泛 real-world robotic arms，作者自己也保留了泛化 caveat。

## 影响页面
- [[wiki/papers/2603_01581_KERV.md|2603_01581_KERV]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
