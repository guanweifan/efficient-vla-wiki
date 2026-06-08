# 2605_30011_VisualThink-VLA

## Source
- Raw: [[raw/2605_30011_VisualThink-VLA.pdf]]
- Extracts manifest: [[extracts/parses/2605_30011_VisualThink-VLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2605_30011_VisualThink-VLA/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **visual intermediate reasoning for low-latency VLA control** 论文；它的核心效率问题是替代高延迟 textual CoT，用紧凑视觉证据接口保留 reasoning 收益。
- VisualThink-VLA 构造 compact visual-evidence interface，并用 selective routing 只暴露 task-relevant evidence tokens，以避免 long textual decoding 和 dense side-information interference。来源：[[raw/2605_30011_VisualThink-VLA.pdf]]，Abstract、Figure 1、Figure 2。
- 论文引入 VisualEvidence-Kit / VisualEvidence-Set，用 route-grounded supervision 和 counterfactual faithfulness tests 支撑 evidence routing。来源：[[raw/2605_30011_VisualThink-VLA.pdf]]，Abstract、Figure 3、Figure 4、Table 7。
- headline 结果需要拆开：success-latency trade-off、backbone portability、real-robot closed-loop task performance、evidence-channel ablations 分属不同证据层。来源：[[raw/2605_30011_VisualThink-VLA.pdf]]，Table 2、Figure 5、Table 3、Table 5。

## Methodology Index
- visual intermediate reasoning
- compact visual evidence interface
- selective evidence routing
- VisualEvidence-Kit
- VisualEvidence-Set
- route-grounded supervision
- counterfactual faithfulness audit
- success-latency trade-off
- backbone portability

## Data Pointer
- **Abstract / Figure 1**：visual reasoning framing 与 ECoT latency comparison headline。
- **Figure 2**：VisualThink-VLA pipeline；dashed arrows denote training-only supervision。
- **Figure 3 / Figure 4**：VisualEvidence-Set statistics and VisualEvidence-Kit workflow。
- **Table 2 / Figure 5**：multi-benchmark success-latency comparison。
- **Table 3**：backbone portability across representative VLA base policies。
- **Table 4 / Figure 6 / Figure 9**：interface and evidence orchestration ablations。
- **Table 5 / Table 8**：real-robot closed-loop evaluation and task definitions。

## Evidence Links
- [[wiki/evidence/claims/2605_30011_VisualThink-VLA-headline-split.md|2605_30011_VisualThink-VLA-headline-split]]

## 待核点
- VisualThink-VLA 的 `speedup` 主要相对 textual reasoning baselines；不能直接和 pruning / quantization 的 FLOPs 或 memory 口径混写。
- 视觉证据 routing 是 reasoning substrate 变化，不等于传统 visual token pruning。
- VisualEvidence-Kit 是 supervision / audit 资源；不能把训练期监督路径写成推理期额外模块成本。
