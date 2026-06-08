# 2606_04968_ForesightFlow-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2606_04968_ForesightFlow.md|2606_04968_ForesightFlow]] 的单篇证据落点，用来拆分 self-guided flow policy、decoupled AWR、one-step foresight estimator、training compute and best-of-K inference headline。
- 本页聚焦的 headline bundle：`success-potential trajectory`、`no separate critic`、`38% training compute reduction`、`K=5 self-guided inference` 需要分层阅读。

## Evidence
- 方法证据命题：ForesightFlow augments action chunks with success-potential coordinates so the same flow proposes and scores candidate actions. 来源：[[raw/2606_04968_ForesightFlow.pdf]]，Abstract、Figure 1、method section。
- 训练目标证据命题：decoupled AWR applies advantage weights to action velocities but trains potential velocities uniformly, preventing value hallucination on failures. 来源：[[raw/2606_04968_ForesightFlow.pdf]]，Abstract、Figure 2、Figure 5、Table 4。
- 效率证据命题：Table 3 compares GPU hours, critic parameters and latency with IDQL; the compute reduction is relative to a separate-critic baseline, not a general inference speedup. 来源：[[raw/2606_04968_ForesightFlow.pdf]]，Table 3。

## Table / Metric Anchors
- **Figure 1**：self-guided flow policy。
- **Figure 2**：decoupled AWR。
- **Table 2 / Figure 4**：real-world task score and SR。
- **Table 3**：GPU hours, critic params and K=1/K=5 latency。
- **Figure 5 / Table 4**：value hallucination and stage-wise completion。
- **Table 5**：NFE=1 vs NFE=100 ranking fidelity。
- **Table 6**：best-of-K self-guided sampling effect。

## Table / Metric Split
- training GPU hours, critic parameter count, K=1/K=5 latency and task success are different口径.
- one-step estimator is used for efficient foresight / ranking fidelity, not necessarily one-step action decoding.
- self-guided best-of-K can improve selection while still adding candidate sampling overhead.

## 不可混写项
- 不应把 ForesightFlow 写成 deployment-oriented runtime compression method。
- 不应 compare its 38% compute reduction with pure data-ratio or GPU-hour results unless baseline definitions match.
- 不应 treat generated potentials as externally validated critic scores outside paper protocol.

## 影响页面
- [[wiki/papers/2606_04968_ForesightFlow.md|2606_04968_ForesightFlow]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
