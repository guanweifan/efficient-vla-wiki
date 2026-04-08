# 2506_13725_CEED-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2506_13725_CEED-VLA.md|2506_13725_CEED-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`4x`、`4.1x`、`4.3x`、`3.6x` 与 `2.0x` 来自不同 backbone 或评测 setting；引用时应把每个数字明确对齐到具体模型与 benchmark。

## Evidence
- 核心证据命题：这篇论文提出 **CEED-VLA**，目标是为自回归 Vision-Language-Action 模型提供一种基于 **consistency** 的推理加速 recipe。论文认为，直接使用 Jacobi 式并行解码仍会浪费迭代步数，并且会积累误差；因此作者把 **consistency distillation**、**mixed-label supervision** 和 **early-exit decoding** 结合起来，希望在保持 manipulation success 的同时显著提升推理速度。 来源：[[raw/2506_13725_CEED-VLA.pdf]]，**Abstract / Introduction**：可直接承载 `4x+ inference acceleration`、simulation 与 real-world success preservation 等顶层主张。
- 补充证据命题：作者把 CEED-VLA 定位成对现有 VLA backbone 的通用加速附加层，而不是一套全新 policy architecture。headline 结果中多次出现 **`4x+` inference acceleration** 一类表述，同时也讨论了速度更激进但精度更敏感的 `CEED-VLA-Turbo` 变体。 来源：[[raw/2506_13725_CEED-VLA.pdf]]，**Figure 1**：最适合补 OpenVLA 与 LLaVA-VLA 上的直接速度比较，也是 `CEED-VLA-Turbo` 与标准版 tradeoff 的第一入口。
- 主证据锚点 1：来源：[[raw/2506_13725_CEED-VLA.pdf]]，**Abstract / Introduction**：可直接承载 `4x+ inference acceleration`、simulation 与 real-world success preservation 等顶层主张。
- 主证据锚点 2：来源：[[raw/2506_13725_CEED-VLA.pdf]]，**Figure 1**：最适合补 OpenVLA 与 LLaVA-VLA 上的直接速度比较，也是 `CEED-VLA-Turbo` 与标准版 tradeoff 的第一入口。
- 主证据锚点 3：来源：[[raw/2506_13725_CEED-VLA.pdf]]，**Figure 2**：方法总览图，是 consistency distillation、mixed-label supervision 和 early-exit decoding 三件事如何组合的最佳方法锚点。

## Figure / Caption Anchors
- **Fig. 1 (p.2)**：caption 直接给出 `OpenVLA 3.6×`、`LLaVA-VLA 2.0×` speedup，并说明 `CEED-VLA-Turbo` 通过更激进的 exit point 获得更高速度，但伴随轻微性能下降。
- **Fig. 2 (p.3)**：caption 与相邻正文解释了 consistency distillation、auxiliary AR loss、mixed-label supervision 如何协同，说明 `student` 为什么能在 Jacobi decoding 下更快收敛。
- **Fig. 5 (results section)**：作者用它展示经过 consistency loss 的模型在更少迭代下仍能保持可接受 manipulation performance；它支撑的是“加速同时保留任务能力”的局部机制证据。

## Figure / Caption / Wording Split
- `universal acceleration method` 不能直接理解成“所有 VLA backbone 都已验证”。当前最强的直接证据来自 **OpenVLA、LLaVA-VLA、两个 simulation 环境和 real robotic arm deployment**。来源：[[raw/2506_13725_CEED-VLA.pdf]]，第 2-3 页 Introduction / Contributions；实验章节。
- `maintaining manipulation performance` 或 `without sacrificing efficiency` 需要回到 `Fig. 1` 和实验表理解：标准 `CEED-VLA` 与 `CEED-VLA-Turbo` 的 speed-accuracy tradeoff 并不相同，不能把 Turbo 的更高速度写成同样稳的默认 operating point。来源：[[raw/2506_13725_CEED-VLA.pdf]]，第 2 页 Fig. 1 caption；实验结果章节。
- `Fig. 2` 支撑的是 **why consistency distillation + mixed-label supervision unlocks Jacobi decoding under incorrect prefixes**，不是 benchmark outcome 本身；若解释“为什么 CEED-VLA 能加速”，应优先引用这一机制图。来源：[[raw/2506_13725_CEED-VLA.pdf]]，第 2-3 页 Fig. 2 与相邻正文。

## 不可混写项
- `4x`、`4.1x`、`4.3x`、`3.6x` 与 `2.0x` 来自不同 backbone 或评测 setting；引用时应把每个数字明确对齐到具体模型与 benchmark。
- `CEED-VLA` 与 `CEED-VLA-Turbo` 当前还放在同一页 `Claim` 中；后续 evidence 层可能需要把两者拆开，因为它们的 speed-accuracy tradeoff 并不相同。
- 论文把方法写成对现有 VLA backbone 的通用加速层；引用时应核验这种兼容性在 OpenVLA、LLaVA-VLA、simulation、real-world 上是否同样充分。

## 影响页面
- [[wiki/papers/2506_13725_CEED-VLA.md|2506_13725_CEED-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
