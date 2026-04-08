# 2502_19645_OFT-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2502_19645_OFT.md|2502_19645_OFT]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`26x`、`43x`、`15%` 这些 headline 数字来自不同实验上下文；后续 `L2` 需要拆清它们分别对应 `LIBERO` throughput、`ALOHA` throughput、以及 real-world average success 的哪组比较。

## Evidence
- OFT 的三项核心设计被作者明确写成： 1. **parallel decoding + action chunking** 2. **continuous action representation** 3. **L1 regression objective** 来源：[[raw/2502_19645_OFT.pdf]]，第 1 页，Abstract；第 7 页，Sec. E。
- 作者的 headline claim 是：基于这套 recipe 的 **OpenVLA-OFT** 在 `LIBERO` 上把平均 success rate 从 **76.5% 提升到 97.1%**，同时把 action generation throughput 提升 **26x**；在真实世界 `ALOHA` 设置中，增强版 **OFT+** 还能以最高 **43x** 的 throughput 相对 base `OpenVLA` 执行高频双臂任务，并在平均成功率上最多超过其他 fine-tuned VLA / from-scratch baseline **15% absolute**。更稳的写法是：这些数字分别绑定 `LIBERO`、`ALOHA` 与 `OFT+ FiLM` 等不同比较上下文，不应压成单一统一 headline。 来源：[[raw/2502_19645_OFT.pdf]]，第 1 页，Abstract；第 8-9 页，Fig. 4 / Fig. 5 附近结果段落。
- 主证据锚点 1：来源：[[raw/2502_19645_OFT.pdf]]，**Abstract / Introduction**：最直接的 recipe、headline numbers 与问题设定入口。 来源：[[raw/2502_19645_OFT.pdf]]，第 1-2 页。
- 主证据锚点 2：来源：[[raw/2502_19645_OFT.pdf]]，**Design-space framing**：`Fig. 2` 把论文真正比较的三类 design choice 画得很清楚，是`claims/wording` 的最佳锚点。 来源：[[raw/2502_19645_OFT.pdf]]，第 3 页，Fig. 2。
- 主证据锚点 3：来源：[[raw/2502_19645_OFT.pdf]]，**Main LIBERO performance**：`TABLE I`，若要拆“PD/AC/Cont-L1/Cont-Diffusion` 分别带来的 success-rate 变化，这里是主表。 来源：[[raw/2502_19645_OFT.pdf]]，第 6 页，Table I。

## Table / Metric Anchors
- **Main LIBERO performance**：`TABLE I`，若要拆“PD/AC/Cont-L1/Cont-Diffusion` 分别带来的 success-rate 变化，这里是主表。  
  来源：[[raw/2502_19645_OFT.pdf]]，第 6 页，Table I。
- **Main efficiency comparison**：`TABLE II`，这里直接给出 `4x`、`26x`、以及 diffusion 步数变化对 latency / throughput / LIBERO-Long SR 的影响。  
  来源：[[raw/2502_19645_OFT.pdf]]，第 6 页，Table II。

## Table / Metric Split
- `TABLE I` 是 **recipe choice -> LIBERO success rate** 的主表：它负责区分 `parallel decoding / action chunking / continuous action / L1 / diffusion` 各个设计对 success-rate 的贡献，`76.5 -> 97.1` 这类主结果应优先锚定在这里，而不是锚定到 ALOHA 实机图。来源：[[raw/2502_19645_OFT.pdf]]，第 6 页，Table I。
- `TABLE II` 是 **效率口径** 的主表：这里承载 `4x`、`26x`、以及 diffusion steps 变化对 throughput / latency / LIBERO-Long SR 的影响；它与 `TABLE I` 的 recipe-performance 比较是不同层，不应把 success-rate 与 throughput 混写成同一 headline。来源：[[raw/2502_19645_OFT.pdf]]，第 6 页，Table II。
- `Fig. 4 / Fig. 5` 对应 **ALOHA real-world**：`43x` throughput 和 `15% absolute` real-world average success gain 属于另一组实机比较，必须与 `TABLE I / II` 的 LIBERO 结果分开表述。来源：[[raw/2502_19645_OFT.pdf]]，第 8-9 页，Fig. 4、Fig. 5。

## 不可混写项
- `26x`、`43x`、`15%` 这些 headline 数字来自不同实验上下文；后续 `L2` 需要拆清它们分别对应 `LIBERO` throughput、`ALOHA` throughput、以及 real-world average success 的哪组比较。
- 这篇论文同时讨论 `OFT` 与 `OFT+`；当前页面先放在同一篇的 `Claim` 里，chief-editor 需决定是否在 evidence/synthesis 层把 `FiLM` 相关结论单列。
- 论文中 `parallel decoding + action chunking` 与 `continuous + L1` 的贡献是层层叠加的；当前 `L1` 页面只保留了 recipe 级概括，若要做更细比较，需要按 `Table I / Table II` 单独补证，并区分 simulation recipe 与 real-world OFT+。

## 影响页面
- [[wiki/papers/2502_19645_OFT.md|2502_19645_OFT]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
