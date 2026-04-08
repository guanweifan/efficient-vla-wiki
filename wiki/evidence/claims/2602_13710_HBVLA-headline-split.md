# 2602_13710_HBVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_13710_HBVLA.md|2602_13710_HBVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`92.2%` 与 `93.6%` 是“保留 full-precision performance 的相对比例”，不是绝对 success rate；仍需在 evidence 层明确换算或保留原口径。

## Evidence
- 这篇论文提出 **HBVLA**，目标是把 VLA 的 post-training quantization 推进到 **1-bit** 级别，同时尽量维持闭环控制稳定性。作者的核心判断是：直接把 LLM/VLM 的 binary PTQ 套到 VLA 上往往无效，因为 VLA 的动作输出在闭环物理执行中会放大量化误差，微小偏差会沿长时程轨迹累积成抓取失败、轨迹漂移等灾难性后果。来源：[[raw/2602_13710_HBVLA.pdf]]，第 1-2 页 Abstract、Introduction。
- 方法上的主张是一个面向 VLA 的 **1-bit post-training binarization framework**。HBVLA 先用 **policy-aware enhanced Hessian** 判断哪些权重对动作最关键；对 non-salient weights 施加 **sparse orthogonal transform** 以形成低熵中间状态；然后在 **Haar domain** 中对 salient 与 non-salient 两部分分别做 group-wise 1-bit quantization。作者强调这不是一般 Haar/binarization 套件，而是围绕动作敏感性和模态混合特性重写的量化流程。来源：[[raw/2602_13710_HBVLA.pdf]]，第 1-3 页 Abstract、Introduction、Fig. 1、Fig. 2；第 3-7 页 Methodology。
- 主证据锚点 1：来源：[[raw/2602_13710_HBVLA.pdf]]，**Abstract**：第 1 页。可直接承载 `1-bit PTQ`、`92.2% / 93.6% retain`、以及 real-world deployability 的 headline。
- 主证据锚点 2：来源：[[raw/2602_13710_HBVLA.pdf]]，**Figure 1 + Introduction**：第 2-3 页。用于锚定 dual dominance problem、为何普通 Hessian / Haar 在 VLA 上失效，以及 action sensitivity 的问题定义。
- 主证据锚点 3：来源：[[raw/2602_13710_HBVLA.pdf]]，**Figure 2 + Methodology**：第 3-7 页。用于锚定 policy-aware Hessian、salient/non-salient partition、sparse orthogonal transform 与 Haar-domain quantization 的完整流程。

## Table / Metric Anchors
- **Table 2**：第 7-8 页。用于锚定 OpenVLA / OpenVLA-OFT 在 LIBERO 上的 1.08-bit quantization 结果。
- **Figure 3 / Figure 4 / Table 3 / Table 4**：第 8-9 页。用于锚定 Mobile ALOHA real-world evaluation、component sensitivity、non-salient permutation criterion 与 rectified Hessian 的 ablation。

## Table / Metric Split
- `**Table 2**` 这一层应单独承载 `**Table 2**` 相关的 benchmark / metric / operating point。 这一层对应 OpenVLA / OpenVLA-OFT 在 LIBERO 上的 1.08-bit quantization 结果。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_13710_HBVLA.pdf]]，`**Table 2**`。
- `**Figure 3 / Figure 4 / Table 3 / Table 4**` 这一层应单独承载 `**Figure 3 / Figure 4 / Table 3 / Table 4**` 相关的 benchmark / metric / operating point。 这一层对应 Mobile ALOHA real-world evaluation、component sensitivity、non-salient permutation criterion 与 rectified Hessian 的 ablation。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_13710_HBVLA.pdf]]，`**Figure 3 / Figure 4 / Table 3 / Table 4**`。

## 不可混写项
- `92.2%` 与 `93.6%` 是“保留 full-precision performance 的相对比例”，不是绝对 success rate；仍需在 evidence 层明确换算或保留原口径。
- 论文在不同地方使用 `1-bit`, `ultra-low-bit`, `weight 1.08 bit` 等表述；仍需统一其量化位宽叙述口径。
- HBVLA 同时强调 `policy-aware Hessian`、`Haar-domain quantization`、`sparse orthogonal transform`；后续 taxonomy 需要统一其主定位。

## 影响页面
- [[wiki/papers/2602_13710_HBVLA.md|2602_13710_HBVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
