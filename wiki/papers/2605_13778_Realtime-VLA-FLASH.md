# 2605_13778_Realtime-VLA-FLASH

## Source
- Raw: [[raw/2605_13778_Realtime-VLA-FLASH.pdf]]
- Extracts manifest: [[extracts/parses/2605_13778_Realtime-VLA-FLASH/manifest.json]]
- Primary text fallback: [[extracts/parses/2605_13778_Realtime-VLA-FLASH/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **speculative inference for diffusion-based VLA / real-time replanning** 论文；它通过 draft model、parallel verification 与 fallback 机制降低 diffusion VLA 的推理延迟。
- FLASH 使用轻量 draft model 先提出动作，再由 Action Expert 并行验证，并在关键阶段用 phase-aware fallback 保持可靠性。来源：[[raw/2605_13778_Realtime-VLA-FLASH.pdf]]，Abstract、Figure 1、Figure 3、Figure 4。
- 论文在 LIBERO 与真实 conveyor sorting setting 中报告延迟和任务结果，并将 full-inference round 与 speculative round 的 latency 分开统计。来源：[[raw/2605_13778_Realtime-VLA-FLASH.pdf]]，Abstract、Tables 1-4、Table 6。
- 更稳的主张是：FLASH 是 action-generation / diffusion inference 的 speculative execution 路线；它与训练效率、visual token pruning 和云边 jitter correction 不是同一层。

## Methodology Index
- speculative inference
- diffusion VLA
- draft model
- Action Expert verification
- phase-aware fallback
- high-frequency replanning
- LIBERO
- real conveyor sorting
- latency breakdown

## Data Pointer
- **Figure 1**：sync inference vs FLASH overview。
- **Figure 2**：π0 inference roofline。
- **Figure 3 / Figure 4**：framework 与 parallel verification。
- **Figure 5 / Figure 6**：phase-aware fallback / keyframes。
- **Tables 1-4**：LIBERO、flash path stats、ablation 与 conveyor-belt results。
- **Table 6**：inference cost breakdown。

## Evidence Links
- [[wiki/evidence/claims/2605_13778_Realtime-VLA-FLASH-headline-split.md|2605_13778_Realtime-VLA-FLASH-headline-split]]

## 待核点
- speculative round latency、task-level average latency 与 full-inference round latency 不应混写。
- draft/verify/fallback 是推理期 action-generation 控制面，不是训练侧压缩。
- 真实 conveyor sorting 结果不能直接外推到所有 manipulation VLA 部署。
