# 2603_25661_Fast-dVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_25661_Fast-dVLA.md|2603_25661_Fast-dVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`2.8×–4.1×` 是相对现有 dVLA acceleration 范式与特定 base model / benchmark 的 headline，不应直接写成所有 dVLA 都能获得的统一倍数。

## Evidence
- 核心证据命题：这篇论文要解决的是：离散 diffusion VLA (`dVLA`) 虽然比离散 autoregressive VLA 具有更强的并行解码潜力，但当前推理速度仍远低于真实机器人通常需要的 `30 Hz` 实时控制频率，因此很难真正落地到物理系统。 来源：[[raw/2603_25661_Fast-dVLA.pdf]]，`PDF p.1-2` Abstract + Fig. 1 + Fig. 2：
- 补充证据命题：作者提出 `Fast-dVLA`，核心思路是利用 dVLA 内部隐含的 `block-wise autoregressive tendency`，改写为一种可复用 `KV cache` 的 `block-wise diffusion` 解码范式：把动作序列拆成 block，按 block 逐步展开，同时在 block 内与跨 block 做并行解码，以兼顾 decoding reliability 与 throughput。 来源：[[raw/2603_25661_Fast-dVLA.pdf]]，dVLA 的速度瓶颈、`2.8×–4.1×` headline、以及 `Fast-dVLA` 为什么比 AR / vanilla dVLA / block diffusion 更快的高层直觉都在这里。
- 主证据锚点 1：来源：[[raw/2603_25661_Fast-dVLA.pdf]]，`PDF p.1-2` Abstract + Fig. 1 + Fig. 2：
- 主证据锚点 2：来源：[[raw/2603_25661_Fast-dVLA.pdf]]，dVLA 的速度瓶颈、`2.8×–4.1×` headline、以及 `Fast-dVLA` 为什么比 AR / vanilla dVLA / block diffusion 更快的高层直觉都在这里。
- 主证据锚点 3：来源：[[raw/2603_25661_Fast-dVLA.pdf]]，`PDF p.3-5` Fig. 3 + Sec. 3：

## Table / Metric Anchors
- `PDF p.6-8` Table 1 / Table 2 / Table 3 / Table 4：
  - `LIBERO`、`CALVIN`、`SimplerEnv` 与不同 base model 的主结果和 speed-performance tradeoff 应回这些表核定。
- `PDF p.10+` Fig. 9 + Table 5：
  - confidence threshold、block size 等超参数对 speed-success tradeoff 的影响在这里，用于锚定最优配置与稳定性证据。

## Table / Metric Split
- ``PDF p.6-8` Table 1 / Table 2 / Table 3 / Table 4` 这一层支撑 ``PDF p.6-8` Table 1 / Table 2 / Table 3 / Table 4` 对应的 benchmark / metric / operating point。 - `LIBERO`、`CALVIN`、`SimplerEnv` 与不同 base model 的主结果和 speed-performance tradeoff 应回这些表核定。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2603_25661_Fast-dVLA.pdf]]，``PDF p.6-8` Table 1 / Table 2 / Table 3 / Table 4`。
- ``PDF p.10+` Fig. 9 + Table 5` 这一层支撑 ``PDF p.10+` Fig. 9 + Table 5` 对应的 benchmark / metric / operating point。 - confidence threshold、block size 等超参数对 speed-success tradeoff 的影响在这里，当前对应最优配置与稳定性证据。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2603_25661_Fast-dVLA.pdf]]，``PDF p.10+` Fig. 9 + Table 5`。

## 不可混写项
- `2.8×–4.1×` 是相对现有 dVLA acceleration 范式与特定 base model / benchmark 的 headline，不应直接写成所有 dVLA 都能获得的统一倍数。
- real-world 部分的 `30 Hz` 是 execution frequency headline，但 success rate / completion time 在不同任务间是 tradeoff 结构；后续不能把它写成“各任务都全面领先”。
- `Fast-dVLA` 的收益同时混合了 block-wise diffusion、KV cache reuse、pipeline decoding 与 asymmetric distillation；若引用时要单独归因于某一组件，需要继续回主表与 ablation 拆分。

## 影响页面
- [[wiki/papers/2603_25661_Fast-dVLA.md|2603_25661_Fast-dVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
