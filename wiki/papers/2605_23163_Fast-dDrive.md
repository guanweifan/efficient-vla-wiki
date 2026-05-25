# 2605_23163_Fast-dDrive

## Source
- Raw: [[raw/2605_23163_Fast-dDrive.pdf]]
- Extracts manifest: [[extracts/parses/2605_23163_Fast-dDrive/manifest.json]]
- Primary text fallback: [[extracts/parses/2605_23163_Fast-dDrive/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **block-diffusion driving VLA / structured action-output acceleration** 论文；它把自动驾驶 VLA 的结构化 JSON-like 输出改造成 section-aligned block diffusion。
- Fast-dDrive 使用 Section-Aware Structured Diffusion、frozen scaffold tokens、Scaffold Speculative Decoding 与 shared-prefix multi-trajectory rollout，在严格 causal ordering 下并行生成 section 内 token。来源：[[raw/2605_23163_Fast-dDrive.pdf]]，Figure 1、Figure 2、Figure 3、Figure 4。
- 论文在 WOD-E2E 与 nuScenes 上报告轨迹质量指标，并在 SGLang serving setting 中报告相对 AR baseline 的 throughput speedup。来源：[[raw/2605_23163_Fast-dDrive.pdf]]，Abstract-like opening、Tables 2-4。
- 更稳的主张是：Fast-dDrive 是 driving VLA 场景中的 action-output decoding / serving efficiency 例子；其 KV cache 与 scaffold speculative decoding 不应混写成 manipulation VLA perception cache。

## Methodology Index
- autonomous driving VLA
- block diffusion
- structured JSON-like output
- Section-Aware Structured Diffusion
- frozen scaffold tokens
- Scaffold Speculative Decoding
- shared-prefix rollout
- KV cache
- WOD-E2E
- nuScenes
- SGLang serving

## Data Pointer
- **Figure 1**：AR vs diffusion paradigm and speedup。
- **Table 1**：section value / scaffold token counts。
- **Figure 2**：training pipeline。
- **Figure 3**：Scaffold Speculative Decoding。
- **Figure 4**：shared-prefix multi-trajectory rollouts。
- **Tables 2-4**：WOD-E2E、nuScenes 与 inference efficiency。
- **Table 5 / Figures 5-9**：SASD ablation and qualitative driving examples。

## Evidence Links
- [[wiki/evidence/claims/2605_23163_Fast-dDrive-headline-split.md|2605_23163_Fast-dDrive-headline-split]]

## 待核点
- driving VLA 的结构化输出与 manipulation action chunk 不是同一对象。
- throughput speedup 依赖 SGLang serving / structured output setting，不能直接外推到机器人控制频率。
- KV cache 服务 shared-prefix trajectory rollout，不等于视觉 token temporal cache。
