# 2506_07530_BitVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2506_07530_BitVLA.md|2506_07530_BitVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：文中同时使用 “与 OpenVLA-OFT 可比” 和 “优于某些 baseline” 两类表述；若写稳定结论，需要按 simulation、real-world base tasks、OOD tasks 分开，不宜压成单句。

## Evidence
- 核心证据命题：这篇论文要解决的是：现有 VLA 即使性能强，也往往体积大、显存占用高、端到端延迟高，不适合部署到受限的边缘机器人平台。 来源：[[raw/2506_07530_BitVLA.pdf]]，`PDF p.1` Abstract + Fig. 1：
- 补充证据命题：作者提出 `BitVLA`，宣称这是首个 fully native `1-bit` VLA：语言骨干和最终模型参数采用 ternary 表示 `{−1, 0, 1}`，同时把视觉编码器也压到 `1.58-bit weights + INT8 activations`。 来源：[[raw/2506_07530_BitVLA.pdf]]，BitVLA 的问题设定、`1.4 GB`、`11.0× memory reduction`、`4.4× speedup`、以及 “fully native 1-bit VLA” 的 headline 都在这里。
- 主证据锚点 1：来源：[[raw/2506_07530_BitVLA.pdf]]，`PDF p.1` Abstract + Fig. 1：
- 主证据锚点 2：来源：[[raw/2506_07530_BitVLA.pdf]]，BitVLA 的问题设定、`1.4 GB`、`11.0× memory reduction`、`4.4× speedup`、以及 “fully native 1-bit VLA” 的 headline 都在这里。
- 主证据锚点 3：来源：[[raw/2506_07530_BitVLA.pdf]]，`PDF p.3-5` Sec. III + Fig. 2：

## Table / Metric Anchors
- `PDF p.6-8` LIBERO 主结果表（Table I / Table II）：
  - BitVLA 与 OpenVLA-OFT、π0、post-training quantization baseline 的主比较在这里；simulation evidence 时应优先回这里。
- `PDF p.9-10` Analysis / Table III：
  - `Quantize-then-Distill` 的 representation alignment、数据规模与多模态能力保留分析在这里。

## Table / Metric Split
- ``PDF p.6-8` LIBERO 主结果表（Table I / Table II）` 这一层支撑 ``PDF p.6-8` LIBERO 主结果表（Table I / Table II）` 对应的 benchmark / metric / operating point。 - BitVLA 与 OpenVLA-OFT、π0、post-training quantization baseline 的主比较在这里；simulation evidence 时应优先回这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2506_07530_BitVLA.pdf]]，``PDF p.6-8` LIBERO 主结果表（Table I / Table II）`。
- ``PDF p.9-10` Analysis / Table III` 这一层支撑 ``PDF p.9-10` Analysis / Table III` 对应的 benchmark / metric / operating point。 - `Quantize-then-Distill` 的 representation alignment、数据规模与多模态能力保留分析在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2506_07530_BitVLA.pdf]]，``PDF p.9-10` Analysis / Table III`。

## 不可混写项
- 文中同时使用 “与 OpenVLA-OFT 可比” 和 “优于某些 baseline” 两类表述；若写稳定结论，需要按 simulation、real-world base tasks、OOD tasks 分开，不宜压成单句。
- `1.4 GB`、`73 ms`、`341.1 Hz` 等 efficiency 指标是在指定硬件和固定 query 设置下测得；若做横向效率比较，需要保留硬件/benchmark 条件。
- `BitVLA` 与 `NORA-Long` 类似，论文里也有“不同 setting 下不同优势”的结构；如果拿它和全精度大模型比较，必须区分 “总体接近” 与 “某些具体任务超过/落后”。

## 影响页面
- [[wiki/papers/2506_07530_BitVLA.md|2506_07530_BitVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
