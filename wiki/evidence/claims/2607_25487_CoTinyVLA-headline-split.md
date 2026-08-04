# 2607_25487_CoTinyVLA-headline-split

## 用途
- 服务于 [[wiki/papers/2607_25487_CoTinyVLA.md|CoTinyVLA]]，拆分 teacher supervision、student footprint 与 online reasoning。

## Evidence
- 方法证据命题：CoTinyVLA 将 episode Plan 与 chunk Think 从 35B teacher 蒸馏到 0.9B student，并联合训练 action generation。来源：[[raw/2607_25487_CoTinyVLA.pdf]]，Abstract、Sec. 1。
- 分类证据命题：compact student 通过训练期 distillation 获得，主路线为 training efficiency；student 推理期仍生成 reasoning spans，形成 reasoning boundary。
- 待核证据命题：memory、cache gain、benchmark result 与 teacher cost 要分层回读。

## Table / Metric Anchors
- **Method**：hierarchical CoT、temporal input、augmentation。
- **Experiments / Interventions**：memory、Plan cache、robustness 与 success 待核。

## Table / Metric Split
- model parameters、allocated inference memory、latency 与 teacher-generation cost 不同。
- robustness gain 与 efficiency footprint 不能压成单一 superiority claim。

## 不可混写项
- 不把 distillation 写成推理期无需 reasoning。
- 不把小模型成功率对比直接泛化到其他 benchmark。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页保留 teacher cost、student footprint 与 inference reasoning 三层。
