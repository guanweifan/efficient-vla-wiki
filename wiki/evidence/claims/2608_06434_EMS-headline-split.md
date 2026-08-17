# 2608_06434_EMS-headline-split

## 用途
- 服务于 [[wiki/papers/2608_06434_EMS.md|EMS]]，拆分 fast-slow switching、effective frequency、success 与 task completion time。

## Evidence
- 方法证据命题：System 1 / System 2 独立端到端生成 action，switching module 只在 action level 选择并以 action fusion 稳定 handoff。来源：[[raw/2608_06434_EMS.pdf]]，Fig. 1、Sec. III。
- LIBERO 证据命题：EMS 平均 success 92.40%、mean slow-system switch ratio 0.153、effective action frequency 93.37 Hz；独立 PI0 为 94.15% / 50 Hz。来源：[[raw/2608_06434_EMS.pdf]]，Table I。
- real-world 证据命题：dual-arm 中 System 2 / EMS 为 100% / 70% success 与 29 / 23 s task completion time，每模型 10 次测试。来源：[[raw/2608_06434_EMS.pdf]]，Table II、Sec. IV-D。

## Table / Metric Anchors
- **Table I**：LIBERO S.R.、switch ratio、effective action frequency。
- **Table II**：simulation/real-robot S.R. 与 completion time。

## Table / Metric Split
- fast-policy rate、slow-policy rate 与 switched effective rate 必须分开。
- simulation success、real-world success 与 completion time 不合并。

## 不可混写项
- 不把 93.37 Hz 写成 PI0 inference frequency。
- 不把 plug-and-play interface 写成未经训练即可替换任意策略。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- action-level decoupling 仍依赖 trajectory distillation、switch-policy training 与 action fusion，不是零适配组合。
