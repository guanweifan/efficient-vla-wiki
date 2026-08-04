# 2607_26657_Enfold-Enfold-Flash

## Source
- Raw: [[raw/2607_26657_Enfold-Enfold-Flash.pdf]]
- Extracts manifest: [[extracts/parses/2607_26657_Enfold-Enfold-Flash/manifest.json]]
- Primary text fallback: [[extracts/parses/2607_26657_Enfold-Enfold-Flash/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **Enfold / Enfold-Flash** 相关的增量论文；当前 L1 记录 world-generator-to-representation transfer。
- 核心机制：训练时用 generator processing observed future 时的 multi-level states 监督 current-only encoder，部署时直接从该 representation 预测动作，不执行 world generator。来源：[[raw/2607_26657_Enfold-Enfold-Flash.pdf]]，Abstract、Sec. 1。
- 维护分类：主路线为 `4.1 Training Efficiency Techniques`；推理期绕过 generator 构成 train-to-infer bridge。

## Methodology Index
- Enfold
- generator-to-representation distillation
- current-only predictive representation
- Enfold-Flash

## Data Pointer
- **Abstract / Sec. 1**：回读 deployment asymmetry 与 representation objective。
- **Method**：回读 G2R、R2G 与 detached task heads。
- **Experiments**：后续拆分 Enfold model path、Enfold-Flash TensorRT、latency 与 task result。

## Evidence Links
- [[wiki/evidence/claims/2607_26657_Enfold-Enfold-Flash-headline-split.md|2607_26657_Enfold-Enfold-Flash-headline-split]]

## 待核点
- Enfold 的 representation-level gain 与 Enfold-Flash 的 TensorRT gain 必须分开。
- world-generator supervision cost 与部署期 action latency 不是同一层。
