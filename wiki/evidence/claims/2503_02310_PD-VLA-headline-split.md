# 2503_02310_PD-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2503_02310_PD-VLA.md|2503_02310_PD-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`2.52× execution frequency` 目前只保留为 headline claim；后续 `L2` 需要精确钉到具体表格、对比对象和实验设置，明确“fundamental VLA model”到底是哪一个实现。

## Evidence
- 这篇论文提出 **PD-VLA**，目标不是重做一个更小的 VLA，而是专门加速**已经集成 action chunking 的主流 VLA**。作者的问题定义是：action chunking 会随着 chunk size 线性放大动作维度，而 autoregressive decoding 会把这种维度膨胀直接转成推理延迟。来源：[[raw/2503_02310_PD-VLA.pdf]]，第 1 页 Abstract；第 1-2 页 Introduction。
- 核心主张是：把 action decoding 从逐 token 的 autoregressive 过程，重写为通过**parallel fixed-point iteration**求解的并行解码过程，可以在**不改基础模型结构**的前提下提升解码速度，并保持 action performance。来源：[[raw/2503_02310_PD-VLA.pdf]]，第 1 页 Abstract；第 2 页 Introduction；第 3-4 页 Method。
- 主证据锚点 1：来源：[[raw/2503_02310_PD-VLA.pdf]]，**Abstract + Fig. 1**：第 1 页。用于锚定“为什么 action chunking + AR decoding 会拖慢 VLA”以及 PD-VLA 的 headline positioning。
- 主证据锚点 2：来源：[[raw/2503_02310_PD-VLA.pdf]]，**Table I + Introduction contributions**：第 1-2 页。用于锚定 `training-free / model-redesign-free / modification-free` 的方法定位与相对其他 acceleration 方法的区别。
- 主证据锚点 3：来源：[[raw/2503_02310_PD-VLA.pdf]]，**Method / Fig. 2**：第 3-4 页。用于锚定 PD-VLA 的网络结构、parallel decoding 如何接入 VLA with action chunking。

## Table / Metric Anchors
- **Table I + Introduction contributions**：第 1-2 页。用于锚定 `training-free / model-redesign-free / modification-free` 的方法定位与相对其他 acceleration 方法的区别。
- **Ablation / Table III**：第 5-6 页。用于锚定 action chunking 与 parallel decoding 两个核心组件各自的作用。

## Table / Metric Split
- `**Table I + Introduction contributions**` 这一层应单独承载 `**Table I + Introduction contributions**` 相关的 benchmark / metric / operating point。 这里收口为：**Table I + Introduction contributions**：第 1-2 页。当前对应 `training-free / model-redesign-free / modification-free` 的方法定位与相对其他 acceleration 方法的区别。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2503_02310_PD-VLA.pdf]]，`**Table I + Introduction contributions**`。
- `**Ablation / Table III**` 这一层应单独承载 `**Ablation / Table III**` 相关的 benchmark / metric / operating point。 这一层对应 action chunking 与 parallel decoding 两个核心组件各自的作用。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2503_02310_PD-VLA.pdf]]，`**Ablation / Table III**`。

## Wording / Boundary Split
- `training-free acceleration without redesign and modification of models` 在本文里是 **decoding-process-only acceleration** 的更精确说法：PD-VLA 只改 inference-time decoding，不重训 backbone，也不重写基础 VLA 架构。来源：[[raw/2503_02310_PD-VLA.pdf]]，第 2 页 Introduction / contributions。
- `preserves model performance with mathematical guarantees` 绑定的是把 AR decoding 重写成 fixed-point iteration 的方法设定；它不是对所有部署场景、所有任务都“有保证”的经验性结论。来源：[[raw/2503_02310_PD-VLA.pdf]]，第 2-4 页 Introduction、Method。

## 不可混写项
- `2.52× execution frequency` 目前只保留为 headline claim；后续 `L2` 需要精确钉到具体表格、对比对象和实验设置，明确“fundamental VLA model”到底是哪一个实现。
- 文中强调 `performance preserved with mathematical guarantees`，但当前页面还没展开其 guarantee 的具体条件与适用边界；仍需回方法推导部分核实，也不要把这条 guarantee 外推成通用部署结论。
- real-world 部分当前只记录“跨不同任务有效、尤其适用于 dexterous tasks”，仍需由主编决定是否把具体任务（如 pour water）提升为更显式的单篇 claim。

## 影响页面
- [[wiki/papers/2503_02310_PD-VLA.md|2503_02310_PD-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
