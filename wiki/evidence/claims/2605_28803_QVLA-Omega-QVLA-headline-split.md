# 2605_28803_QVLA-Omega-QVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_28803_QVLA-Omega-QVLA.md|2605_28803_QVLA-Omega-QVLA]] 的单篇证据落点，用来拆分 full-stack W4A4 PTQ、DiT action-head quantization、memory savings 与 real-world progress score。
- 本页聚焦的 headline bundle：`training-free PTQ`、`uniform W4A4`、`composite SVD-Hadamard rotation`、`per-step DiT activation scaling`、`71.3% static memory reduction` 需要分层阅读。

## Evidence
- 方法证据命题：Omega-QVLA compresses both language backbone and entire DiT action head to uniform W4A4 through composite rotation and per-step activation scaling. 来源：[[raw/2605_28803_QVLA-Omega-QVLA.pdf]]，Abstract、Figure 1、Table 4。
- 失败模式证据命题：the paper frames full DiT action-head quantization as sensitive because quantization errors propagate through closed-loop continuous control; the method targets channel imbalance and denoising-step dynamic-range drift. 来源：[[raw/2605_28803_QVLA-Omega-QVLA.pdf]]，Abstract、Introduction、Figure 3。
- 结果证据命题：LIBERO success, real-world manipulation progress and static memory footprint are separately reported and should not be collapsed. 来源：[[raw/2605_28803_QVLA-Omega-QVLA.pdf]]，Table 1、Table 2、Table 3。

## Table / Metric Anchors
- **Figure 1**：quantization pipeline。
- **Table 1**：LIBERO quantization performance。
- **Table 2**：real-world manipulation progress score。
- **Table 3**：static memory footprint and storage savings。
- **Figure 3**：activation outlier suppression。
- **Table 4**：rotation and per-step scaling ablation。

## Table / Metric Split
- uniform W4A4 full-stack compression differs from mixed precision or weight-only PTQ.
- static memory footprint is not the same as measured latency or control frequency.
- real-world progress score is not the same口径 as LIBERO task success.

## 不可混写项
- 不应把 Omega-QVLA 与 QVLA/ActQuant 的 bit-allocation approach 混写。
- 不应把 training-free PTQ written as training-cost reduction unless calibration protocol is explicitly discussed.
- 不应把 action-head quantization success generalized beyond evaluated backbones.

## 影响页面
- [[wiki/papers/2605_28803_QVLA-Omega-QVLA.md|2605_28803_QVLA-Omega-QVLA]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
