# 2607_06370_ActionCache

## Source
- Raw: [[raw/2607_06370_ActionCache.pdf]]
- Extracts manifest: [[extracts/parses/2607_06370_ActionCache/manifest.json]]
- Primary text fallback: [[extracts/parses/2607_06370_ActionCache/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **ActionCache** 相关的增量论文；当前 L1 记录 action-state retrieval 与 refinement 的入口。
- 核心机制：把 intermediate actions 与 compact multimodal keys 存入外部 cache，在相似上下文中直接复用或以少量 flow steps refinement。来源：[[raw/2607_06370_ActionCache.pdf]]，Abstract、Sec. 1。
- 维护分类：主路线为 `3.1 Raw Action Generation`。

## Methodology Index
- ActionCache
- action caching
- warm-start refinement
- training-free acceleration

## Data Pointer
- **Abstract / Sec. 1**：回读外部 action cache 与 zero/few-step path。
- **Method**：回读 multimodal key、retrieval、fallback 与 intermediate action selection。
- **Experiments**：后续拆分 action-head latency、end-to-end latency、NFE 与 task success。

## Evidence Links
- [[wiki/evidence/claims/2607_06370_ActionCache-headline-split.md|2607_06370_ActionCache-headline-split]]

## 待核点
- action-head speedup 不能直接写成整模型 speedup。
- cache hit、fallback 与跨任务复用范围需要回到实验条件。
