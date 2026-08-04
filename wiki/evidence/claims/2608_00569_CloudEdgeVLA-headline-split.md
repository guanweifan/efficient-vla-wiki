# 2608_00569_CloudEdgeVLA-headline-split

## 用途
- 服务于 [[wiki/papers/2608_00569_CloudEdgeVLA.md|CloudEdgeVLA]]，拆分 dual-system organization、delay robustness 与 deployment measurement。

## Evidence
- 方法证据命题：CloudEdgeVLA 把慢速 cloud semantic backbone 与当前 local vision edge head 解耦，并用 fresh/stale paired paths 训练 representation。来源：[[raw/2608_00569_CloudEdgeVLA.pdf]]，Abstract、Introduction、method overview。
- 分类证据命题：功能和 placement 双重 slow-fast separation 构成主 dual-system route；非阻塞 network execution 是次级 deployment route。
- 待核证据命题：uniform-delay result、communication setting、edge footprint 与 real-robot check 需分别记录。

## Table / Metric Anchors
- **Method**：Vision-Augmented Action Head 与 paired-frame training。
- **Experiments**：delay window、success、compute/communication setting 待核。

## Table / Metric Split
- latency robustness、network latency、model latency 与 control rate 不同。
- simulation delay sweep 与真实 cloud-edge measurement 不同。

## 不可混写项
- 不把 stale-feature robustness 写成 backbone FLOPs reduction。
- 不把非阻塞 control 写成通信成本消失。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页保留 delay robustness 与实测 deployment efficiency 的边界。
