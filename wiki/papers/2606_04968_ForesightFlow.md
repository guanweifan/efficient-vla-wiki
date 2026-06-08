# 2606_04968_ForesightFlow

## Source
- Raw: [[raw/2606_04968_ForesightFlow.pdf]]
- Extracts manifest: [[extracts/parses/2606_04968_ForesightFlow/manifest.json]]
- Primary text fallback: [[extracts/parses/2606_04968_ForesightFlow/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **self-guided flow-matching VLA policy improvement** 论文；它的核心效率问题是不用 separate critic，也能利用 mixed-quality deployment experience 做 policy improvement。
- ForesightFlow 在 action chunk endpoint 中加入 success-potential coordinates，使同一个 flow 同时 propose candidate actions 并 score them for best-of-K inference。来源：[[raw/2606_04968_ForesightFlow.pdf]]，Abstract、Figure 1、method section。
- 论文用 decoupled advantage-weighted flow matching，把 advantage weights 只用于 action velocities，同时 uniform train potential velocities，以避免 value hallucination。来源：[[raw/2606_04968_ForesightFlow.pdf]]，Abstract、Figure 2、Figure 5、Table 4。
- 训练效率 headline 主要来自与 separate-critic IDQL pipeline 对比的 GPU hours / critic parameters；推理 best-of-K latency 是另一个口径。来源：[[raw/2606_04968_ForesightFlow.pdf]]，Table 2、Table 3、Table 5、Table 6。

## Methodology Index
- flow matching
- self-guided action-potential flow
- success-potential trajectory
- decoupled advantage-weighted regression
- one-step boundary estimator
- best-of-K inference
- mixed-quality rollouts
- separate-critic avoidance
- BEHAVIOR-1K / real-world bimanual tasks

## Data Pointer
- **Abstract / Figure 1**：self-guided flow policy and success-potential framing。
- **Figure 2**：decoupled AWR mechanism。
- **Table 2 / Figure 4**：real-world score and success-rate breakdown。
- **Table 3**：GPU hours, critic parameters and K=1/K=5 latency comparison with IDQL。
- **Figure 5 / Table 4**：value hallucination and decoupling effect。
- **Table 5**：NFE=1 vs NFE=100 ranking fidelity。
- **Table 6**：self-guided sampling / best-of-K inference effect。

## Evidence Links
- [[wiki/evidence/claims/2606_04968_ForesightFlow-headline-split.md|2606_04968_ForesightFlow-headline-split]]

## 待核点
- ForesightFlow 是 VLA policy improvement / training-adaptation route，不是单纯 action sampler acceleration。
- `reduces training compute by 38%` 对比的是 IDQL-style separate-critic pipeline；不能写成所有 flow-matching training 的通用节省。
- best-of-K inference 可能增加 candidate generation / scoring成本；需要和 K=1/K=5 latency 分开读。
