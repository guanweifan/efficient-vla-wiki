# 2606_05737_One-Step-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2606_05737_One-Step-VLA.md|2606_05737_One-Step-VLA]] 的单篇证据落点，用来拆分 condition-target framing、high-noise training schedule、one-step vs ten-step decoding 与 horizon/condition boundary。
- 本页聚焦的 headline bundle：`one-step action generation`、`standard velocity objective`、`no teacher / no distillation`、`LIBERO-family sampler trend` 需要分层阅读。

## Evidence
- 方法证据命题：One-Step VLA keeps standard flow-matching velocity prediction and shifts the training time distribution toward high-noise states, without teacher or distillation stage. 来源：[[raw/2606_05737_One-Step-VLA.pdf]]，Abstract、Introduction、method section。
- 解释证据命题：the paper frames VLA action chunks as rich-condition / compact-target generation, contrasting them with image generation where one-step sampling is harder. 来源：[[raw/2606_05737_One-Step-VLA.pdf]]，Abstract、Introduction、Figure 1、Figure 2。
- 结果证据命题：Table 1 and Table 2 show schedule and horizon controls; Table 3 shows condition ablations; Table 5 and Table 6 provide robustness and real-robot checks. 来源：[[raw/2606_05737_One-Step-VLA.pdf]]，Table 1、Table 2、Table 3、Table 5、Table 6。

## Table / Metric Anchors
- **Figure 1 / Figure 2**：condition-target toy diagnostics。
- **Figure 3**：VLA architecture。
- **Table 1**：H10 time-schedule controls。
- **Table 2**：action-horizon controls。
- **Table 3**：condition ablations。
- **Table 5**：LIBERO-Pro robustness probe。
- **Table 6**：YAM RSS real-robot check。
- **Figure 4 / Figure 5**：velocity diagnostics and LIBERO-Plus sweep。

## Table / Metric Split
- one-step vs ten-step comparisons must keep schedule, horizon and model recipe fixed.
- high-noise bias affects one-step and ten-step differently; it is not a universal sampler improvement.
- real-robot YAM RSS uses small trial counts and should remain boundary evidence.

## 不可混写项
- 不应 write this as distillation or consistency-model method.
- 不应 claim one-step dominates ten-step across all horizons and settings.
- 不应 compare one-step decoding gains directly with WAM video-action distillation without noting target/substrate difference.

## 影响页面
- [[wiki/papers/2606_05737_One-Step-VLA.md|2606_05737_One-Step-VLA]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
