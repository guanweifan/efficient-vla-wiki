# 2505_21432_Hume-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2505_21432_Hume.md|2505_21432_Hume]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：引言中的 `+25.9%` 与 `+12.9%` headline 数字需要和正文表格逐项对齐；当前页面将这些数字保留为作者 headline claim，并明确它们尚未自动等同于单一结构化证据单元。

## Evidence
- 论文给出的 headline 能力叙述需要拆开理解：`System 2` 低频运行约 **4 Hz**、`System 1` 异步高频运行约 **90 Hz**，这是系统运行频率，不等同于 benchmark 结果；性能 headline 则分别来自 `LIBERO`、`Simpler` 和 real-world deployment，不应压成单一“统一 SOTA”结论。 来源：[[raw/2505_21432_Hume.pdf]]，第 1-2 页，Abstract / Introduction。
- 作者在引言中给出三组 headline numeric claims：相对 `π0`，Hume 在 `LIBERO` 上约 **+4.4%** success rate、在 `Simpler` 上约 **+25.9%**、在 real-world deployments 上约 **+12.9%**。更稳的写法是：Hume 在不同 evaluation layer 上都报告了提升，但这些数字分别绑定不同 benchmark、platform 与 comparison protocol。 来源：[[raw/2505_21432_Hume.pdf]]，第 2 页，Introduction 结尾贡献列表。 caveat：这些 headline 数字聚合了不同平台和评测口径，后续 `L2` 需要拆到具体表与具体 setting。
- 主证据锚点 1：来源：[[raw/2505_21432_Hume.pdf]]，**Abstract + Intro**：论文整体问题设定、dual-system framing、以及最紧凑的 headline 主张。 来源：[[raw/2505_21432_Hume.pdf]]，第 1-2 页。
- 主证据锚点 2：来源：[[raw/2505_21432_Hume.pdf]]，**Method core**：`Sec. 3 Methodology`，尤其 `Figure 2`，是`System 2 / value-query / best-of-N / cascaded denoising` 结构证据的主锚点。 来源：[[raw/2505_21432_Hume.pdf]]，第 3-4 页，Sec. 3 / Fig. 2。
- 主证据锚点 3：来源：[[raw/2505_21432_Hume.pdf]]，**Main LIBERO result**：`Table 1`，这里也是`LIBERO-Spatial/Object/Goal/Long` 的具体增益的主表。 来源：[[raw/2505_21432_Hume.pdf]]，第 8 页，Table 1。

## Table / Metric Anchors
- **Main LIBERO result**：`Table 1`，这里也是`LIBERO-Spatial/Object/Goal/Long` 的具体增益的主表。  
  来源：[[raw/2505_21432_Hume.pdf]]，第 8 页，Table 1。
- **Main Simpler result**：`Table 2`，这里也是WidowX / Google Robot 的 Simpler 指标的主表。  
  来源：[[raw/2505_21432_Hume.pdf]]，第 8 页，Table 2。

## Table / Metric Split
- `**Main LIBERO result**` 这一层支撑 `**Main LIBERO result**` 对应的 benchmark / metric / operating point。 `Table 1`，这里也是`LIBERO-Spatial/Object/Goal/Long` 的具体增益的主表。 来源：[[raw/2505_21432_Hume.pdf]]，第 8 页，Table 1。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2505_21432_Hume.pdf]]，`**Main LIBERO result**`。
- `**Main Simpler result**` 这一层支撑 `**Main Simpler result**` 对应的 benchmark / metric / operating point。 `Table 2`，这里也是WidowX / Google Robot 的 Simpler 指标的主表。 来源：[[raw/2505_21432_Hume.pdf]]，第 8 页，Table 2。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2505_21432_Hume.pdf]]，`**Main Simpler result**`。

## 不可混写项
- 引言中的 `+25.9%` 与 `+12.9%` headline 数字需要和正文表格逐项对齐；当前页面将这些数字保留为作者 headline claim，并明确它们尚未自动等同于单一结构化证据单元。
- 论文同时汇报 `LIBERO`、`SimplerEnv`、`WidowX`、`Franka`、`AgiBot G-1` 等多平台结果；如果进入 `L2`，需要决定是按 benchmark 拆 evidence，还是按 “simulation / real-world” 两层拆。
- “state-of-the-art” 的表述覆盖了多个不同 comparison set；chief-editor 需决定是否把 `OpenVLA-OFT`、`π0`、`GR00T` 等主要对手单独列为 comparison anchor，并把 `4 Hz / 90 Hz` 的系统频率与 benchmark headline 明确分栏。

## 影响页面
- [[wiki/papers/2505_21432_Hume.md|2505_21432_Hume]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
