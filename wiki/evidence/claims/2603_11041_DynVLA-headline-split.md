# 2603_11041_DynVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_11041_DynVLA.md|2603_11041_DynVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：当前可稳定抓到的是“最高 PDMS / 最佳 Bench2Drive / 更低 ADE 和 Collision Rate”这类排序性主张；若仍需精确 headline 数值，必须回 Table 1-4 逐项核定。

## Evidence
- 核心证据命题：这篇论文要解决的是：自动驾驶 VLA 中常见的 `Textual CoT` 难以表达真实世界中的时空演化，而 `Visual CoT` 又引入大量像素级冗余与推理延迟；因此现有 CoT 设计要么语义太抽象，要么成本太高。 来源：[[raw/2603_11041_DynVLA.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 补充证据命题：作者提出 `DynVLA`，核心是引入 `Dynamics CoT`：先用 `Dynamics Tokenizer` 把相邻观测间的未来世界演化压缩成少量 dynamics tokens，再让模型在 action tokens 之前先生成 dynamics tokens 进行显式 reasoning。为适配驾驶场景，它进一步把 dynamics 拆成 `ego-centric` 与 `environment-centric` 两部分，并用物理正则和 cross-view consistency 强化表示。 来源：[[raw/2603_11041_DynVLA.pdf]]，`Textual CoT / Visual CoT / Dynamics CoT` 的问题对比、`over an order of magnitude` latency headline 与整体动机都在这里。
- 主证据锚点 1：来源：[[raw/2603_11041_DynVLA.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 主证据锚点 2：来源：[[raw/2603_11041_DynVLA.pdf]]，`Textual CoT / Visual CoT / Dynamics CoT` 的问题对比、`over an order of magnitude` latency headline 与整体动机都在这里。
- 主证据锚点 3：来源：[[raw/2603_11041_DynVLA.pdf]]，`PDF p.3-5` Fig. 2 + Fig. 3 + Sec. 3：

## Table / Metric Anchors
- `PDF p.5-6` Table 1 + Table 2 + Table 3：
  - `NAVSIM`、`Bench2Drive`、大规模 in-house dataset 的主结果都在这里；若要精确写 `PDMS / SR / ADE / Collision Rate`，应回这几张表核定。
- `PDF p.6` Table 4：
  - 不同 CoT 设计与 latency 对比在这里，用于锚定“为什么 Dynamics CoT 比 textual / visual CoT 更高效”的证据。
- `PDF p.6-7` Table 5 + Table 6：
  - `Dynamics CoT` 对 `SFT / RFT` 的增益，以及 tokenizer decoupling / regularization 的作用都在这里。

## Table / Metric Split
- ``PDF p.5-6` Table 1 + Table 2 + Table 3` 这一层支撑 ``PDF p.5-6` Table 1 + Table 2 + Table 3` 对应的 benchmark / metric / operating point。 - `NAVSIM`、`Bench2Drive`、大规模 in-house dataset 的主结果都在这里；若要精确写 `PDMS / SR / ADE / Collision Rate`，应回这几张表核定。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2603_11041_DynVLA.pdf]]，``PDF p.5-6` Table 1 + Table 2 + Table 3`。
- ``PDF p.6` Table 4` 这一层支撑 ``PDF p.6` Table 4` 对应的 benchmark / metric / operating point。 - 不同 CoT 设计与 latency 对比在这里，当前对应“为什么 Dynamics CoT 比 textual / visual CoT 更高效”的证据。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2603_11041_DynVLA.pdf]]，``PDF p.6` Table 4`。
- ``PDF p.6-7` Table 5 + Table 6` 这一层支撑 ``PDF p.6-7` Table 5 + Table 6` 对应的 benchmark / metric / operating point。 - `Dynamics CoT` 对 `SFT / RFT` 的增益，以及 tokenizer decoupling / regularization 的作用都在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2603_11041_DynVLA.pdf]]，``PDF p.6-7` Table 5 + Table 6`。

## 不可混写项
- 当前可稳定抓到的是“最高 PDMS / 最佳 Bench2Drive / 更低 ADE 和 Collision Rate”这类排序性主张；若仍需精确 headline 数值，必须回 Table 1-4 逐项核定。
- “over an order of magnitude” 的 latency 优势是相对 textual / visual CoT 设计，而不是相对所有 non-CoT baseline 的统一倍率。
- `DynVLA` 的增益同时混合了 compact dynamics tokenization、ego/environment decoupling、`Dynamics CoT SFT` 与 `RFT`；若后续单独归因于某一层，需要继续回 Table 5 / Table 6。

## 影响页面
- [[wiki/papers/2603_11041_DynVLA.md|2603_11041_DynVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
