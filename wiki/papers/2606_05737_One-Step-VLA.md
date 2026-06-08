# 2606_05737_One-Step-VLA

## Source
- Raw: [[raw/2606_05737_One-Step-VLA.pdf]]
- Extracts manifest: [[extracts/parses/2606_05737_One-Step-VLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2606_05737_One-Step-VLA/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **one-step continuous action generation for diffusion-based VLA** 论文；它的核心效率问题是 VLA action chunk 的 condition-target structure 可能让 standard flow matching 在单步解码下足够强。
- 论文不引入 teacher model、distillation stage 或 auxiliary objective，而是把 training time distribution bias toward high-noise states，用标准 velocity prediction 训练 one-step policy。来源：[[raw/2606_05737_One-Step-VLA.pdf]]，Abstract、Introduction、method section。
- 论文把 VLA action generation 与 image diffusion 区分开：VLA 条件包含图像、语言和状态，target 是低维 action chunk，因此不必直接照搬 image one-step machinery。来源：[[raw/2606_05737_One-Step-VLA.pdf]]，Abstract、Introduction、Figure 1、Figure 2。
- headline 结果应读成特定 LIBERO-family 和 real-robot checks 下的 sampler-step trend；horizon、condition richness 和 schedule 仍是边界变量。来源：[[raw/2606_05737_One-Step-VLA.pdf]]，Table 1、Table 2、Table 3、Table 5、Table 6。

## Methodology Index
- one-step action generation
- diffusion-based VLA
- flow matching
- high-noise training schedule
- velocity prediction
- condition-target asymmetry
- action horizon ablation
- condition ablation
- LIBERO / LIBERO-Plus / LIBERO-Pro
- YAM RSS real-robot check

## Data Pointer
- **Abstract / Introduction**：condition-target framing and no-teacher/no-distillation recipe。
- **Figure 1 / Figure 2**：controlled toy diagnostics for rich-condition compact-target setting。
- **Figure 3**：VLA architecture。
- **Table 1**：H10 time-schedule controls on standard LIBERO。
- **Table 2**：action-horizon controls on LIBERO-Long。
- **Table 3**：condition ablations。
- **Table 5**：LIBERO-Pro robustness probe。
- **Table 6**：bimanual YAM RSS real-robot success comparison。
- **Figure 4 / Figure 5**：velocity-field diagnostics and LIBERO-Plus full-condition sweep。

## Evidence Links
- [[wiki/evidence/claims/2606_05737_One-Step-VLA-headline-split.md|2606_05737_One-Step-VLA-headline-split]]

## 待核点
- 本篇支持“simple one-step can work in evaluated VLA action-generation settings”，不支持所有 diffusion policies 都能无损单步化。
- high-noise schedule 对 one-step 有益，但对 ten-step 或超长 action horizon 可能不稳定；不能写成单调改进。
- YAM RSS 结果是 small-sample cross-architecture check，需要保留样本量边界。
