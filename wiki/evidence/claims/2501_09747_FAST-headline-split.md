# 2501_09747_FAST-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2501_09747_FAST.md|2501_09747_FAST]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：论文把“training time by up to 5x”写得很强，但不同图里对应的是 training steps、GPU hours 和 compute-matched checkpoint 三种口径；后续 L2 需要把这些口径拆开，并避免把训练效率写成 inference latency。

## Evidence
- 论文还提出 `FAST+` 作为在 `1M` 条真实机器人动作轨迹上训练得到的通用 tokenizer，并声称把 FAST 接到 `π0` 上后，可以在大规模机器人数据上达到与 diffusion `π0` 相当的性能，同时把 training steps / GPU hours 降低到原来的约 `1/5`。更稳的写法是：这些 headline 绑定在 `π0` generalist training 这组比较里；它主要说明 **tokenization 带来的训练效率与 token efficiency**，不应被外推成自回归 VLA 的统一推理加速结论。来源：[[raw/2501_09747_FAST.pdf]]，第 1 页摘要；第 10 页 Figure 11 附近正文。
- 补充证据命题：核心主张是：在训练自回归 VLA 前，应先对动作序列做压缩；作者提出基于 `DCT + quantization + BPE` 的 `FAST` 动作分词方案，用频域压缩来降低 token 冗余，从而让自回归 VLA 能学会高频、灵巧控制任务。 来源：[[raw/2501_09747_FAST.pdf]]，高频 tokenization 失效现象：[[raw/2501_09747_FAST.pdf]] 第 2 页 Fig. 2；第 3-4 页 Figure 3 case study。这里说明为什么 naive per-timestep binning 在高频动作上会退化。
- 主证据锚点 1：来源：[[raw/2501_09747_FAST.pdf]]，摘要与总览：[[raw/2501_09747_FAST.pdf]] 第 1 页摘要与 Fig. 1。这里给出问题定义、FAST/FAST+ 的 headline，以及“与 diffusion VLA 相当但训练快 5x”的总主张。
- 主证据锚点 2：来源：[[raw/2501_09747_FAST.pdf]]，高频 tokenization 失效现象：[[raw/2501_09747_FAST.pdf]] 第 2 页 Fig. 2；第 3-4 页 Figure 3 case study。这里说明为什么 naive per-timestep binning 在高频动作上会退化。
- 主证据锚点 3：来源：[[raw/2501_09747_FAST.pdf]]，核心算法：[[raw/2501_09747_FAST.pdf]] 第 5 页 Fig. 4 与 Algorithm 1；第 5-6 页 Section V。这里是 DCT、量化、BPE 压缩流水线和 FAST+ 的直接定义位置。

## Table / Metric Anchors
- 压缩与单任务训练结果：[[raw/2501_09747_FAST.pdf]] 第 7 页 Table I；第 8 页 Fig. 6；第 8 页 Fig. 7。这里分别对应 token 压缩率、不同 tokenizer 的训练表现，以及 DROID zero-shot 展示。

## Table / Metric Split
- `压缩与单任务训练结果` 这一层应单独承载 `压缩与单任务训练结果` 相关的 benchmark / metric / operating point。 当前这一层分别对应 token 压缩率、不同 tokenizer 的训练表现，以及 DROID zero-shot 展示。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2501_09747_FAST.pdf]]，`压缩与单任务训练结果`。

## 不可混写项
- 论文把“training time by up to 5x”写得很强，但不同图里对应的是 training steps、GPU hours 和 compute-matched checkpoint 三种口径；后续 L2 需要把这些口径拆开，并避免把训练效率写成 inference latency。
- 这篇工作主要是在“tokenization / training efficiency”上占优，但文中也明确承认 autoregressive `π0-FAST` 的推理速度慢于 diffusion `π0`；若进入 synthesis，不能只保留训练优势。
- `FAST+` 是否应在后续 wiki 中作为独立概念页，仍待主编决定；它既是 tokenizer 实例，也是“通用 tokenizer”这个更大的 claim。

## 影响页面
- [[wiki/papers/2501_09747_FAST.md|2501_09747_FAST]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
