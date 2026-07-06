# 2606_31160_Reasoning-aware-Speculative-Decoding-FlatRoPE-AARL

## Source
- Raw: [[raw/2606_31160_Reasoning-aware-Speculative-Decoding-FlatRoPE-AARL.pdf]]
- Extracts manifest: [[extracts/parses/2606_31160_Reasoning-aware-Speculative-Decoding-FlatRoPE-AARL/manifest.json]]
- Primary text fallback: [[extracts/parses/2606_31160_Reasoning-aware-Speculative-Decoding-FlatRoPE-AARL/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **Reasoning-aware Speculative Decoding / FlatRoPE / AARL** 相关的增量论文；当前 L1 只记录 title / abstract / method-level 的稳定入口，详细数值和 benchmark 结论等待后续细读。
- 核心机制：Accelerate autonomous-driving VLA chain-of-causation reasoning by using a specialized routine draft reasoner for predictable tokens and the full visual target model only for verification and visually grounded deliberation. 来源：[[raw/2606_31160_Reasoning-aware-Speculative-Decoding-FlatRoPE-AARL.pdf]]，Title、Abstract、method section。
- 维护分类：当前按主效率瓶颈放入 `4.2 Inference Efficiency Techniques`；次级相关为 `3.2 Reasoning-Aware Action Generation`；领域标签为 `Autonomous Driving`。该分类是 wiki 维护定位，不替代论文原文事实。

## Methodology Index
- Reasoning-aware Speculative Decoding
- Inference Efficiency Techniques
- Reasoning-Aware Action Generation
- speculative decoding
- autonomous driving

## Data Pointer
- **Title / Abstract**：回读问题设定、目标成本口径和方法 headline。
- **Method section**：回读核心机制、模块边界和分类依据。
- **Experiments / Results**：后续回读 latency、memory、training cost、task performance 或 deployment setting；本轮不摘录未细读的 headline 数值。
- **Ablation / Analysis**：后续确认该方法的效率收益来自哪个具体组件。

## Evidence Links
- [[wiki/evidence/claims/2606_31160_Reasoning-aware-Speculative-Decoding-FlatRoPE-AARL-headline-split.md|2606_31160_Reasoning-aware-Speculative-Decoding-FlatRoPE-AARL-headline-split]]

## 待核点
- 需要回读实验表格，拆分 task performance、runtime / memory / training cost 与 deployment setting，避免混写。
- 需要确认 secondary relevance 是否只是辅助机制，还是足以影响对应 synthesis 页。
- 若存在官方代码或项目页，本页不把外部仓库内容当作事实来源；代码只作为检索入口。
