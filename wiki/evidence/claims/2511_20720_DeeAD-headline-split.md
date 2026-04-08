# 2511_20720_DeeAD-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2511_20720_DeeAD.md|2511_20720_DeeAD]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`29% latency reduction` 来自最激进的 `δ = 2.0 m` operating point；更保守的阈值对应的是更小但更稳的收益，后续不能把最佳点写成默认无条件结论。

## Evidence
- 核心证据命题：这篇论文要解决的是：自动驾驶 VLA 虽然统一了 perception、reasoning 和 trajectory generation，但深层 transformer 堆叠带来很高的 planning latency，难以满足实时部署需求。 来源：[[raw/2511_20720_DeeAD.pdf]]，`PDF p.1-2` Abstract + Introduction：
- 补充证据命题：作者提出 `DeeAD`，这是一个 training-free、action-guided 的 dynamic early-exit 框架，主要作为 **ORION driving VLA/planner** 上的推理加速模块来使用。它不再用 feature confidence 决定是否提前退出，而是直接检查中间层预测出的轨迹是否已经与轻量规划先验（如 navigation 或 low-precision planning）足够接近；若空间偏差落入允许范围，就提前停止后续层的推理。 来源：[[raw/2511_20720_DeeAD.pdf]]，问题设定、为何用 action-space deviation 而不是 confidence 做 early exit，以及 `28% sparsity / 29% latency reduction` 的 headline 都在这里。
- 主证据锚点 1：来源：[[raw/2511_20720_DeeAD.pdf]]，`PDF p.1-2` Abstract + Introduction：
- 主证据锚点 2：来源：[[raw/2511_20720_DeeAD.pdf]]，问题设定、为何用 action-space deviation 而不是 confidence 做 early exit，以及 `28% sparsity / 29% latency reduction` 的 headline 都在这里。
- 主证据锚点 3：来源：[[raw/2511_20720_DeeAD.pdf]]，`PDF p.2-4` Fig. 2 / Fig. 3 + motivation analysis：

## Table / Metric Anchors
- `PDF p.6-7` Table 2：
  - Bench2Drive open-loop 主结果在这里；不同 `δ` 下的 `L2`、`Collision`、`Sparsity`、`Latency`，以及与 ORION / Fixed-EE 的比较都在这里，适合拆开“balanced operating point”和“max-speed operating point”。
- `PDF p.7-8` Table 3 / Table 4：
  - per-layer early-exit overhead、不同 exit depth 的端到端 latency、以及 `203 ms` / `440 ms` 的运行时边界分析在这里；这些结果属于 runtime envelope，不应直接替代主表 operating point。
- `PDF p.8` Table 5：
  - action-guided exit、multi-hop controller、tolerance threshold 的 ablation 在这里，用于锚定“为什么不是 fixed-depth / full-scan”的证据。

## Table / Metric Split
- ``PDF p.6-7` Table 2` 这一层支撑 ``PDF p.6-7` Table 2` 对应的 benchmark / metric / operating point。 - Bench2Drive open-loop 主结果在这里；不同 `δ` 下的 `L2`、`Collision`、`Sparsity`、`Latency`，以及与 ORION / Fixed-EE 的比较都在这里，适合拆开“balanced operating point”和“max-speed operating point”。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2511_20720_DeeAD.pdf]]，``PDF p.6-7` Table 2`。
- ``PDF p.7-8` Table 3 / Table 4` 这一层支撑 ``PDF p.7-8` Table 3 / Table 4` 对应的 benchmark / metric / operating point。 - per-layer early-exit overhead、不同 exit depth 的端到端 latency、以及 `203 ms` / `440 ms` 的运行时边界分析在这里；这些结果属于 runtime envelope，不应直接替代主表 operating point。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2511_20720_DeeAD.pdf]]，``PDF p.7-8` Table 3 / Table 4`。
- ``PDF p.8` Table 5` 这一层支撑 ``PDF p.8` Table 5` 对应的 benchmark / metric / operating point。 - action-guided exit、multi-hop controller、tolerance threshold 的 ablation 在这里，当前对应“为什么不是 fixed-depth / full-scan”的证据。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2511_20720_DeeAD.pdf]]，``PDF p.8` Table 5`。

## Figure / Caption / Wording Split
- `training-free` 在本文里的具体含义是：以 action-space deviation 与 lightweight planning priors 决定 exit，不重训 ORION backbone；它不是“无需任何 controller / threshold design”。来源：[[raw/2511_20720_DeeAD.pdf]]，第 1-2 页 Abstract / Introduction。
- `real-time planning` 的直接证据边界是 **ORION + Bench2Drive**；文中说 hundreds of milliseconds latency 是 embedded deployment barrier，而 `29% latency reduction` 只对应主表里最激进的 tolerance operating point。来源：[[raw/2511_20720_DeeAD.pdf]]，第 1-2 页；第 6-7 页 Table 2。
- `Fig. 1` 在本文里主要承担 paradigm evolution framing，不是主结果图；真正解释为什么 action-guided exit 成立的是 `Fig. 2 / Fig. 3` 的 motivation analysis。来源：[[raw/2511_20720_DeeAD.pdf]]，第 1-4 页 Fig. 1-3 与相邻正文。

## 不可混写项
- `29% latency reduction` 来自最激进的 `δ = 2.0 m` operating point；更保守的阈值对应的是更小但更稳的收益，后续不能把最佳点写成默认无条件结论。
- `47% speed-up` 来自 `l*=16` 的特定 exit-depth runtime analysis，不等同于主表里的平均运行点。
- DeeAD 主要在 ORION 上集成并在 Bench2Drive open-loop 评估；如果写“适用于 driving VLA planning”，最好明确这是针对 ORION + Bench2Drive 的证据，而不是已经覆盖 closed-loop 或多后端框架。

## 影响页面
- [[wiki/papers/2511_20720_DeeAD.md|2511_20720_DeeAD]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
