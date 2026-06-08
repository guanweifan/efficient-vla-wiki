# 2605_28803_QVLA-Omega-QVLA

## Source
- Raw: [[raw/2605_28803_QVLA-Omega-QVLA.pdf]]
- Extracts manifest: [[extracts/parses/2605_28803_QVLA-Omega-QVLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2605_28803_QVLA-Omega-QVLA/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **training-free full-stack VLA PTQ** 论文；它的核心效率问题是把 language backbone 与 DiT action head 都压到 uniform W4A4，而不是只量化 LLM 或保留 action head 高精度。
- Omega-QVLA 组合 composite SVD-Hadamard rotation 与 per-step DiT activation scaling，用于处理 channel-level energy imbalance 和 denoising-step dynamic-range drift。来源：[[raw/2605_28803_QVLA-Omega-QVLA.pdf]]，Abstract、Figure 1、Figure 3、Table 4。
- 论文明确挑战“DiT action head cannot survive uniform low-bit quantization”的前提，并在 Pi-0.5 / GR00T N1.5 上报告 W4A4 full-stack quantization。来源：[[raw/2605_28803_QVLA-Omega-QVLA.pdf]]，Abstract、Introduction、Table 1。
- headline 结果需要拆开：LIBERO task success、real-world progress score、static memory footprint 与 ablation 分属不同证据口径。来源：[[raw/2605_28803_QVLA-Omega-QVLA.pdf]]，Table 1、Table 2、Table 3、Table 4。

## Methodology Index
- post-training quantization
- training-free PTQ
- full-stack W4A4
- DiT action head quantization
- composite SVD-Hadamard rotation
- per-step activation scaling
- dynamic-range drift
- static memory footprint
- LIBERO / real-world manipulation

## Data Pointer
- **Abstract / Introduction**：uniform W4A4 full-stack quantization framing。
- **Figure 1**：overall quantization pipeline。
- **Table 1**：LIBERO quantization performance with calibration sample size `n=10`。
- **Table 2**：real-world manipulation results under W4A4 quantization。
- **Table 3**：static model footprint and storage savings。
- **Figure 3**：activation outlier suppression under SVD-Hadamard rotation。
- **Table 4**：rotation matrix and per-step scaling ablation。

## Evidence Links
- [[wiki/evidence/claims/2605_28803_QVLA-Omega-QVLA-headline-split.md|2605_28803_QVLA-Omega-QVLA-headline-split]]

## 待核点
- Omega-QVLA 的主张是 uniform W4A4 full-stack PTQ；不要和 ActQuant 的 sub-4-bit mixed-precision / runtime pipeline 互相替代。
- static memory saving 不是完整 deployment success；需要与 hardware placement / runtime latency 分层。
- real-world manipulation result 使用 progress score 口径，不能直接和 LIBERO success rate 合并。
