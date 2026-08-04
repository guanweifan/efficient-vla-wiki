# 2607_14695_Reflex-headline-split

## 用途
- 服务于 [[wiki/papers/2607_14695_Reflex.md|Reflex]]，拆分 context partition、cache validity 与 streaming overlap。

## Evidence
- 方法证据命题：Reflex 将 flow-VLA context 划分为 static、sliding 与 dynamic regions，以支持数学上有效的增量 KV reuse，并采用异步 pipeline。来源：[[raw/2607_14695_Reflex.pdf]]，Abstract、Sec. 1、method overview。
- 分类证据命题：主贡献位于 streaming runtime；跨控制步 KV reuse 是次级 temporal route。
- 待核证据命题：reaction latency、inference rate、interpolated control rate 与 task result 需分别记录。

## Table / Metric Anchors
- **Method**：context regions、incremental prefill、future compensation。
- **Experiments**：latency breakdown、Hz、success 与 ablation 待核。

## Table / Metric Split
- perception encode、policy generation、execution overlap 与 reaction time 不同。
- model invocation frequency 与 low-level command output frequency 不同。

## 不可混写项
- 不把 streaming overlap 写成单次模型 FLOPs reduction。
- 不把所有 KV cache 都视为对 flow timestep 条件天然有效。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页保留 cache validity 与 streaming scheduling 两层。
