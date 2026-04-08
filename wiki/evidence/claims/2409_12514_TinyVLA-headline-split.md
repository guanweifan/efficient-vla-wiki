# 2409_12514_TinyVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2409_12514_TinyVLA.md|2409_12514_TinyVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：Abstract 中“**eliminating the need for pre-training stage**”容易引起歧义；正文实际上仍有视觉语言预训练，更准确的说法应是**不需要大规模机器人数据预训练**。引用时需由 chief editor 统一措辞。

## Evidence
- 这篇论文提出 **TinyVLA**，目标是构建更快、更 data-efficient 的 VLA family，直接回应现有 VLA 在 real-world deployment 中的两大瓶颈：**慢 inference** 和 **对大规模 robot pretraining 的依赖**。来源：[[raw/2409_12514_TinyVLA.pdf]]，第 1 页 Abstract、Fig. 1；第 1-2 页 Introduction。
- 核心主张是：用 **小型预训练 VLM** 作为 policy backbone，再接 **diffusion policy decoder** 替代 autoregressive action token 生成，可以在不依赖 OpenX 这类大规模 robot pretraining 的前提下，取得更好的 speed / data efficiency / generalization 平衡。来源：[[raw/2409_12514_TinyVLA.pdf]]，第 1-2 页 Abstract、Introduction；第 3 页 Fig. 2、Sec. III。
- 主证据锚点 1：来源：[[raw/2409_12514_TinyVLA.pdf]]，**Abstract + Fig. 1**：第 1 页。用于锚定“fast inference + data efficiency + 20x latency reduction”的 headline evidence。
- 主证据锚点 2：来源：[[raw/2409_12514_TinyVLA.pdf]]，**Introduction contribution paragraph**：第 2 页。用于锚定“25.7% better than OpenVLA / 5.5x fewer parameters / bimanual advantage”。
- 主证据锚点 3：来源：[[raw/2409_12514_TinyVLA.pdf]]，**Sec. III + Fig. 2**：第 2-3 页。用于锚定 TinyVLA 的主结构：compact VLM backbone、LoRA、diffusion policy decoder。

## Table / Metric Anchors
- **Table I**：第 3 页。用于锚定 simulation multi-task 结果，尤其 TinyVLA-H 相对 Diffusion Policy 的提升。
- **Table II**：第 4 页。用于锚定 real-world 五任务结果与 TinyVLA-S/B/H 对 OpenVLA 的比较。
- **Table III**：第 4-5 页。用于锚定 bimanual UR5 结果，尤其 OpenVLA 全失败与 TinyVLA-H 的平均表现。

## Table / Metric Split
- `Table I` 对应 **simulation multi-task** 层：`TinyVLA-H` 在 MetaWorld 50 tasks 上的平均 success rate 是 `31.6`，而 `Diffusion Policy` 是 `10.5`；这张表支撑的是 compact VLM + diffusion decoder 在 simulation multi-task 上的整体可行性，不是 real-world headline。来源：[[raw/2409_12514_TinyVLA.pdf]]，第 3 页，Table I。
- `Table II` 对应 **single-arm real-world five-task** 层：`TinyVLA-H` 的平均 success rate 是 `94.0`，`OpenVLA` 是 `68.3`，这才是 paper page 里 `25.7%` 单臂平均优势的主锚点；这里也同时承载了 `TinyVLA-S/B/H` 的 family scaling，不应与 Fig. 1 的 latency headline 混写。来源：[[raw/2409_12514_TinyVLA.pdf]]，第 4 页，Table II。
- `Table III` 对应 **bimanual UR5** 层：`OpenVLA` 在三项任务上是 `0 / 0 / 0`，而 `TinyVLA-H` 在 `PlaceBread / StackCubes / PlaceTennisBag` 上分别是 `76.7 / 36.7 / 30.0`；这张表说明的是双臂协作层的能力边界，不能与 Table II 的单臂五任务平均结果压成同一 benchmark headline。来源：[[raw/2409_12514_TinyVLA.pdf]]，第 4-5 页，Table III。

## 不可混写项
- Abstract 中“**eliminating the need for pre-training stage**”容易引起歧义；正文实际上仍有视觉语言预训练，更准确的说法应是**不需要大规模机器人数据预训练**。引用时需由 chief editor 统一措辞。
- `20x lower inference latency` 来自 Fig. 1 的 family-level headline，对应的比较对象和测量条件与 Table II/III 的任务成功率结果不同；后续不能把它和 `25.7%`、`44.5%` 写成同一组同条件结论。
- `Table II` 的列在解析文本里有一定排版噪声；当前只保留 headline 结论，后续 `L2` 需要回原 PDF 精确钉住每个任务和平均值。

## 影响页面
- [[wiki/papers/2409_12514_TinyVLA.md|2409_12514_TinyVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
