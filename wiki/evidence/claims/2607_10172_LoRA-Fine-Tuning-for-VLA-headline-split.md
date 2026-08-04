# 2607_10172_LoRA-Fine-Tuning-for-VLA-headline-split

## 用途
- 服务于 [[wiki/papers/2607_10172_LoRA-Fine-Tuning-for-VLA.md|LoRA Fine-Tuning for VLA]]，拆分 PEFT capacity、memory scope 与任务表现。

## Evidence
- 方法证据命题：论文比较多个 LoRA ranks、VLM/action-expert capacity allocation，以及 vision encoder 的 frozen/LoRA/full-finetuning 选择。来源：[[raw/2607_10172_LoRA-Fine-Tuning-for-VLA.pdf]]，Abstract、Sec. 1。
- 分类证据命题：主要成本是 adaptation trainable parameters 与静态显存，属于 training efficiency。
- 待核证据命题：rank saturation、VRAM 和 task result 要回到同一实验设置核对。

## Table / Metric Anchors
- **Experimental setup**：rank、allocation、freezing ablations。
- **Results**：static peak VRAM、task success 与统计分析待核。

## Table / Metric Split
- parameters/optimizer-state memory 与 activation memory 必须分开。
- real-robot task success 与 memory reduction 需要配对但不能合并为单一指标。

## 不可混写项
- 不把静态 VRAM reduction 写成完整训练显存 reduction。
- 不把 PEFT 收益写成 inference latency acceleration。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页保留 static memory 与 full training memory 的口径边界。
