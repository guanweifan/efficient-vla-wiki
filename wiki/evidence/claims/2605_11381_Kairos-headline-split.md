# 2605_11381_Kairos-headline-split

## 用途
- 服务于 [[wiki/papers/2605_11381_Kairos.md|Kairos]]，拆分 fleet serving、execution horizon 与模型推理成本。

## Evidence
- 方法证据命题：Kairos 参与每个任务的 generate-execute loop，并把 execution horizon 与机器人执行时长纳入跨任务调度。来源：[[raw/2605_11381_Kairos.pdf]]，Abstract、Sec. 1。
- 分类证据命题：主贡献位于 serving/runtime 层，不是新的 action decoder。
- 待核证据命题：端到端任务时延收益需要绑定 fleet size、workload 与基线 serving policy。

## Table / Metric Anchors
- **Sec. 1 / System overview**：problem model 与 scheduler knobs。
- **Evaluation**：task latency、serving load、accuracy 与 fleet scaling 待核。

## Table / Metric Split
- model latency、queueing、execution duration 与 end-to-end task latency属于不同层。
- dynamic horizon 的 load reduction 与任务准确率需要配对阅读。

## 不可混写项
- 不把 multi-robot serving 收益写成单模型 FLOPs 降低。
- 不把 fleet-level latency 直接换算成机器人控制频率。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页只承担 Kairos 的 system-level headline 拆分。
