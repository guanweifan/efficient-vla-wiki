# 2608_10824_Gated-VLA-Cache-headline-split

## 用途
- 服务于 [[wiki/papers/2608_10824_Gated-VLA-Cache.md|Gated VLA-Cache]]，拆分 cache reliability、compute saving、gate calibration 与 latency claim。

## Evidence
- 方法证据命题：上一步 action-token top-1/top-2 probability margin 低于阈值时 full recompute，否则继续 VLA-Cache 的 patch-similarity selective KV reuse。来源：[[raw/2608_10824_Gated-VLA-Cache.pdf]]，Fig. 2、Algorithm 1。
- compute 证据命题：OpenVLA 四 suite 平均，full / VLA-Cache / gated 为 70.1% @ 1.87、68.1% @ 1.43、69.9% @ 1.53 TFLOPs/step。来源：[[raw/2608_10824_Gated-VLA-Cache.pdf]]，Table I。
- boundary 证据命题：gate 有 one-step lag，threshold 依 model-family calibration，实验仅 simulation；论文未报告 wall-clock latency。来源：[[raw/2608_10824_Gated-VLA-Cache.pdf]]，Sec. IV-B、Sec. VI。

## Table / Metric Anchors
- **Table I-II**：OpenVLA / OpenVLA-OFT success-compute points。
- **Fig. 5-7 / Sec. VI**：gate frequency、threshold sensitivity 与 limitations。

## Table / Metric Split
- TFLOPs/step、full-recompute frequency、success recovery 与 wall-clock latency 不可互换。
- OpenVLA 与 OpenVLA-OFT 的 calibration / robustness 分开。

## 不可混写项
- 不把 compute saving 写成 measured latency speedup。
- 不把 logit margin 写成 cache staleness 的直接因果识别器。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- margin 无法区分 cache-induced uncertainty 与模型固有 ambiguity；额外 recompute 可能只增加成本。
