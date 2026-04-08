# 2603_07904_DyQ-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_07904_DyQ-VLA.md|2603_07904_DyQ-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`30.9%`、`99.5%`、`1.49×`、`1.43×` 分别对应 memory、retained performance、simulation speedup、real-world speedup；仍需把比较对象和评测设置拆清。

## Evidence
- 这篇论文讨论的核心问题是：**VLA 的量化敏感性不是静态的，而是随执行阶段动态变化**。作者认为，机器人在粗粒度运动阶段可以容忍更大的量化误差，但在精细交互阶段，同样的误差可能直接导致任务失败；因此固定 bit-width 的 static quantization 会被最敏感时刻“绑架”，在整个 rollout 中持续维持过高精度，造成资源浪费。来源：[[raw/2603_07904_DyQ-VLA.pdf]]，第 1-2 页 Abstract、Introduction、Fig. 1。
- 基于这个观察，论文提出 **DyQ-VLA**：一种面向 VLA 的 **dynamic quantization framework**。它包含两部分：一是 **sensitivity-aware switching strategy**，用实时运动学 proxy 触发 bit-width 切换；二是 **kinematic-guided bit allocation**，根据运动学指标动态分配最合适的 bit-width。它的 framing 不是“更好的静态 PTQ”，而是把量化从静态配置改成与 manipulation phase 对齐的 step-wise dynamic control。来源：[[raw/2603_07904_DyQ-VLA.pdf]]，第 1-4 页 Abstract、Introduction、Sec. IV。
- 主证据锚点 1：来源：[[raw/2603_07904_DyQ-VLA.pdf]]，**Abstract + Introduction + Fig. 1**：第 1-2 页。用于锚定“temporal-dynamic sensitivity”问题定义，以及为什么 static quantization 对 VLA 次优。
- 主证据锚点 2：来源：[[raw/2603_07904_DyQ-VLA.pdf]]，**Sec. III / Fig. 2 / Fig. 3**：第 3-4 页。用于锚定 sensitivity 与 kinematic metrics（Motion Fineness、Angular Jerk）的对应关系。
- 主证据锚点 3：来源：[[raw/2603_07904_DyQ-VLA.pdf]]，**Sec. IV + Fig. 4**：第 4-5 页。用于锚定 `sensitivity-aware switching` 与 `kinematic-guided bit allocation` 的具体机制。

## Table / Metric Anchors
- **Table I + simulation results**：第 6-7 页。用于锚定在 LIBERO 上与 full-precision、SmoothQuant、QVLA 的 speed / memory / success-rate 比较。

## Table / Metric Split
- `Table I` 对应 **simulation tradeoff 主表**：`DyQ-VLA` 在四个 `LIBERO` suite 上大致保持 `76.1` Avg success，并把峰值显存从 `15.2GB` 压到 `4.7GB`，同时获得约 `1.47×-1.51×` 的仿真 speedup；这里才是 `30.9% memory footprint` 与 `99.5% retained performance` 的主要出处。来源：[[raw/2603_07904_DyQ-VLA.pdf]]，第 6-7 页，Table I。
- `Table II` 对应 **real-world speed / degradation**：`Atomic` / `Spatial` / `Composite` 三类任务分别是 `1.43×`、`1.32×`、`1.38×` speedup，对应 `0.0%-3.4%` 的性能退化范围；因此 `up to 1.43× real-world speedup` 不能和 Table I 的仿真 `1.49×` 混写。来源：[[raw/2603_07904_DyQ-VLA.pdf]]，第 7-8 页，Table II。

## 不可混写项
- `30.9%`、`99.5%`、`1.49×`、`1.43×` 分别对应 memory、retained performance、simulation speedup、real-world speedup；仍需把比较对象和评测设置拆清。
- 论文当前主要以 **OpenVLA** 为 base model 展开，仍需决定单篇主 claim 中是否显式保留这一验证边界，避免泛化到所有 VLA。
- 文中同时使用 `dynamic quantization`、`precision switching`、`kinematic-guided bit allocation` 三种 framing；后续 taxonomy 需要统一其主定位。

## 影响页面
- [[wiki/papers/2603_07904_DyQ-VLA.md|2603_07904_DyQ-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
