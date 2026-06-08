# 2606_05254_Flash-WAM-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2606_05254_Flash-WAM.md|2606_05254_Flash-WAM]] 的单篇证据落点，用来拆分 modality-aware step distillation、joint video-action diffusion、real-time per-chunk latency and simulation/real-world success headline。
- 本页聚焦的 headline bundle：`1v/1a or 1v/2a WAM inference`、`23x speedup`、`348 ms per chunk`、`RoboTwin / LIBERO / Unitree G1 success` 需要分层阅读。

## Evidence
- 方法证据命题：Flash-WAM selects modality-specific consistency functions for video and action streams because their SNR-shifted noise schedules concentrate in different regimes. 来源：[[raw/2606_05254_Flash-WAM.pdf]]，Abstract、Figure 2、method section。
- 失败模式证据命题：naive joint LCM collapses in the joint video-action setting because the standard consistency loss gives inadequate gradient signal for the action stream at low noise. 来源：[[raw/2606_05254_Flash-WAM.pdf]]，Introduction、Figure 2、Table 4。
- 结果证据命题：per-chunk latency and success are reported for LingBot-VA on specific NFE configurations across RoboTwin, LIBERO and Unitree G1; hardware and NFE settings are part of the claim. 来源：[[raw/2606_05254_Flash-WAM.pdf]]，Figure 1、Table 1、Table 2、Table 3。

## Table / Metric Anchors
- **Figure 1**：per-chunk latency and RoboTwin success headline。
- **Figure 2**：Flash-WAM training and deployment pipeline。
- **Table 1**：RoboTwin 2.0 success under NFE configurations。
- **Table 2**：LIBERO success under NFE configurations。
- **Table 3**：Unitree G1 real-world success。
- **Table 4**：distillation strategy ablation。
- **Figure 4**：open-loop video qualitative comparison。

## Table / Metric Split
- per-chunk latency, success rate and NFE are jointly necessary to interpret the result.
- video denoising and action denoising are separate streams with separate noise regimes.
- simulation success and Unitree G1 real-world success are separate evidence layers.

## 不可混写项
- 不应 treat Flash-WAM as generic one-step VLA action generation; it targets WAM video-action diffusion.
- 不应 compare `23x` speedup without LingBot-VA / L40S / NFE context.
- 不应 conclude all consistency distillation fails; the failure is specific to naive uniform joint video-action distillation.

## 影响页面
- [[wiki/papers/2606_05254_Flash-WAM.md|2606_05254_Flash-WAM]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
