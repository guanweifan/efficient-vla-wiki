# 2607_06370_ActionCache-headline-split

## 用途
- 服务于 [[wiki/papers/2607_06370_ActionCache.md|ActionCache]]，拆分 retrieval、refinement、action-head latency 与 end-to-end cost。

## Evidence
- 方法证据命题：ActionCache 存储带 multimodal keys 的 intermediate actions，并用检索结果直接生成或 warm-start flow refinement。来源：[[raw/2607_06370_ActionCache.pdf]]，Abstract、Sec. 1。
- 分类证据命题：核心减少 action-head denoising evaluations，主路线为 `Raw Action Generation`。
- 待核证据命题：不同 backbone 的 action-head acceleration 需要和整模型 latency、cache overhead 分开。

## Table / Metric Anchors
- **Method**：key construction、retrieval、refinement、fallback。
- **Experiments**：action-head latency、NFE、success 与 cache setting 待核。

## Table / Metric Split
- action-head speedup、full-policy speedup 与 task completion time 不是同一层。
- direct reuse、few-step refinement 与 full fallback 是不同 operating point。

## 不可混写项
- 不把 cache 命中路径的最好结果泛化到所有输入。
- 不把 external action cache 写成视觉 KV cache。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页只承担 ActionCache 的 action-head 证据拆分。
