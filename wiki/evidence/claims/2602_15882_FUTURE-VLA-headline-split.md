# 2602_15882_FUTURE-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_15882_FUTURE-VLA.md|2602_15882_FUTURE-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`99.2% / 75.4% / 78.0%` 分别来自三个不同 benchmark / platform，后续不能写成一个统一的“平均 headline”。

## Evidence
- 核心证据命题：这篇论文要解决的是：机器人上的 `VLA + world model` 体系在长时序、多视角、实时执行场景下仍存在三重瓶颈，即长历史带来的 visual-token cost 爆炸、预测与控制之间的表征/执行脱节、以及高维未来预测无法跟上闭环执行频率。 来源：[[raw/2602_15882_FUTURE-VLA.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 补充证据命题：作者提出 `FUTURE-VLA`，把 long-horizon control 与 future forecasting 重写成单一的 sequence-generation 任务，并采用 `dual-sided efficiency paradigm`：输入侧做受 token budget 约束的时空压缩，输出侧在紧凑 latent space 中做 future autoregression，从而在单次 forward pass 中同步生成 action chunks 与 future previews。 来源：[[raw/2602_15882_FUTURE-VLA.pdf]]，任务设定、modular fragmentation 问题、`99.2% / 75.4% / 78.0% / 16×` headline，以及 unified architecture 的整体动机都在这里。
- 主证据锚点 1：来源：[[raw/2602_15882_FUTURE-VLA.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 主证据锚点 2：来源：[[raw/2602_15882_FUTURE-VLA.pdf]]，任务设定、modular fragmentation 问题、`99.2% / 75.4% / 78.0% / 16×` headline，以及 unified architecture 的整体动机都在这里。
- 主证据锚点 3：来源：[[raw/2602_15882_FUTURE-VLA.pdf]]，`PDF p.3-4` Fig. 2 + Sec. 3：

## Table / Metric Anchors
- `PDF p.5-6` Table 1：
  - `LIBERO` 主结果在这里；`FUTURE-VLA (w/o HIL)` 与 `FUTURE-VLA (w/ HIL)` 的差异都应回这张表。
- `PDF p.6-7` Table 2：
  - `RoboTwin` 主结果在这里；`75.4%` headline 与 `w/o HIL` / `w/ HIL` 的对比应回这里核定。
- `PDF p.7` Table 3 + real-world result discussion：
  - `Piper` real-world 主结果、`78%` headline，以及 `Table Cleanup` 从 `40%` 到 `64%` 的 HIL 提升都在这里。

## Table / Metric Split
- ``PDF p.5-6` Table 1` 这一层支撑 ``PDF p.5-6` Table 1` 对应的 benchmark / metric / operating point。 - `LIBERO` 主结果在这里；`FUTURE-VLA (w/o HIL)` 与 `FUTURE-VLA (w/ HIL)` 的差异都应回这张表。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2602_15882_FUTURE-VLA.pdf]]，``PDF p.5-6` Table 1`。
- ``PDF p.6-7` Table 2` 这一层支撑 ``PDF p.6-7` Table 2` 对应的 benchmark / metric / operating point。 - `RoboTwin` 主结果在这里；`75.4%` headline 与 `w/o HIL` / `w/ HIL` 的对比应回这里核定。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2602_15882_FUTURE-VLA.pdf]]，``PDF p.6-7` Table 2`。
- ``PDF p.7` Table 3 + real-world result discussion` 这一层支撑 ``PDF p.7` Table 3 + real-world result discussion` 对应的 benchmark / metric / operating point。 - `Piper` real-world 主结果、`78%` headline，以及 `Table Cleanup` 从 `40%` 到 `64%` 的 HIL 提升都在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2602_15882_FUTURE-VLA.pdf]]，``PDF p.7` Table 3 + real-world result discussion`。

## 不可混写项
- `99.2% / 75.4% / 78.0%` 分别来自三个不同 benchmark / platform，后续不能写成一个统一的“平均 headline”。
- `FUTURE-VLA` 的核心结果明显依赖 `HIL` 版本；同时正文也给出 autonomous `w/o HIL` 的 `LIBERO 91.3%` 等结果，仍应明确默认叙述到底以 `w/ HIL` 还是模型自主能力为中心。
- `16× extended spatiotemporal window while maintaining single-frame latency` 是建立在固定 token budget 压缩设计上的架构级主张，若引用到其他部署条件，需要保留实现前提。

## 影响页面
- [[wiki/papers/2602_15882_FUTURE-VLA.md|2602_15882_FUTURE-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
