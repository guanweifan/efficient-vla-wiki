# 2604_09244_Tri-Stage-Token-Pruning-Framework

## Source
- Raw: [[raw/2604_09244_Tri-Stage-Token-Pruning-Framework.pdf]]
- Extracts manifest: [[extracts/parses/2604_09244_Tri-Stage-Token-Pruning-Framework/manifest.json]]
- Primary text fallback: [[extracts/parses/2604_09244_Tri-Stage-Token-Pruning-Framework/pdftotext.txt]]
- Fine-grained locator: [[extracts/parses/2604_09244_Tri-Stage-Token-Pruning-Framework/pdftotext.bbox.html]]

## Claim
- 页面定位：这是一篇 **tri-stage token pruning for multi-visual-modal VLA** 论文；它的主贡献是把 2D / 3D modality salience difference 显式纳入 pruning 设计，而不是把 MVLA 继续按 2D-only VLA 的 pruning 逻辑处理。
- 这篇论文要解决的是：当 VLA 从 2D-only 扩展到 2D+3D multi-visual-modal 输入后，token 数量显著上升，现有为 SVLA 设计的 token pruning 方法又忽略了 2D 与 3D 模态在不同阶段的 salience discrepancy。来源：[[raw/2604_09244_Tri-Stage-Token-Pruning-Framework.pdf]]，Abstract；Introduction。
- 论文把 MVLA 的数据利用过程拆成 `data preprocessing`、`semantic synthesis`、`action iteration` 三个阶段，并在每一阶段分别分析 2D / 3D token 的重要性动态，再据此设计对应的 tri-stage pruning framework。来源：[[raw/2604_09244_Tri-Stage-Token-Pruning-Framework.pdf]]，Fig. 1；Sec. 3。
- headline 数字需要拆开理解：论文报告 up to `2.55×` inference speedup、minimal accuracy loss、以及约 `5.8%` overhead；这些 headline 需要和 pruning ratio、specific MVLA setting 与 RLBench 任务 success 对齐阅读。来源：[[raw/2604_09244_Tri-Stage-Token-Pruning-Framework.pdf]]，Abstract；主实验表。
- 更稳的主张是：这篇工作把 token pruning 从单一视觉模态问题推进到了 2D / 3D modality-aware compute allocation，重点是 MVLA 的多模态 salience management。

## Methodology Index
- tri-stage token pruning
- multi-visual-modal VLA
- MVLA
- 2D / 3D modality salience
- stage-wise pruning
- data preprocessing stage
- semantic synthesis stage
- action iteration stage
- modality-aware token selection
- RLBench evaluation

## Data Pointer
- **Abstract + Introduction**：适合后续补 MVLA token explosion 与 2D / 3D salience discrepancy 的 framing。
- **Fig. 1**：适合后续补三阶段数据利用范式与 tri-stage pruning 对应关系。
- **Sec. 3**：适合后续补每一阶段的 salience 分析与 pruning 规则。
- **主实验表（RLBench）**：适合后续补 `2.55×`、accuracy loss、pruning rate 与 baseline 比较。
- **Overhead / ablation 表**：适合后续补 `5.8%` overhead 和三阶段各自贡献。

## Evidence Links
- [[wiki/evidence/claims/2604_09244_Tri-Stage-Token-Pruning-Framework-headline-split.md|2604_09244_Tri-Stage-Token-Pruning-Framework-headline-split]]

## 待核点
- `2.55×` 与 `5.8%` 分别对应哪一组 pruning ratio 与 RLBench setting，后续需要拆清。
- 当前 strongest evidence 来自 MVLA setting；后续不能把它写成对 2D-only VLA pruning 的统一改进。
- 论文当前更像 modality-aware pruning framework，而不是一般 deployment report；后续 route 定位要保持这一边界。
