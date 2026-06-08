# 2605_29438_ElegantVLA

## Source
- Raw: [[raw/2605_29438_ElegantVLA.pdf]]
- Extracts manifest: [[extracts/parses/2605_29438_ElegantVLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2605_29438_ElegantVLA/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **phase-adaptive intra-model compute scheduling for VLA inference** 论文；它的核心效率问题是不同控制阶段不应固定花同等计算。
- ElegantVLA 在 frozen base policy 上加入 lightweight scheduler，基于 temporal representation similarity、robot-motion cues 和 episode progress，在 Vision-LLM 与 action head 两侧选择不同 recompute / reuse levels。来源：[[raw/2605_29438_ElegantVLA.pdf]]，Abstract、Figure 1、Figure 2、method section。
- 该方法把 VLA acceleration 写成 sequential compute allocation problem，并用 two-stage RL scheduler 学习跨 perception-language reasoning 与 action generation 的复用策略。来源：[[raw/2605_29438_ElegantVLA.pdf]]，method section、Table 6、Table 12、Figure 11。
- headline 结果覆盖 GR00T / CogACT simulation 与 Franka real-world tasks；success、FLOPs speedup、control frequency 和 per-step wall-clock latency 需要分层阅读。来源：[[raw/2605_29438_ElegantVLA.pdf]]，Table 2、Table 3、Table 4、Table 9。

## Methodology Index
- phase-adaptive compute scheduling
- temporal reuse
- Vision-LLM compute mode
- action-head denoising reuse
- lightweight scheduler
- CKA temporal similarity
- robot-motion cues
- Maskable PPO scheduler
- frozen base VLA
- control frequency

## Data Pointer
- **Abstract / Figure 1**：non-uniform inference demand and phase-adaptive motivation。
- **Figure 2**：ElegantVLA overview and scheduler inputs。
- **Table 2**：GR00T / SIMPLER success-speedup comparison。
- **Table 3**：Franka real-world success-speedup results。
- **Table 4**：latency / frequency on GR00T in SimplerEnv。
- **Table 6 / Table 12 / Table 13**：scheduler and signal ablations。
- **Table 9**：real-world per-step latency breakdown。
- **Figure 11**：rollout-level scheduling diagnostic。

## Evidence Links
- [[wiki/evidence/claims/2605_29438_ElegantVLA-headline-split.md|2605_29438_ElegantVLA-headline-split]]

## 待核点
- ElegantVLA 不修改或重训 base model，但 scheduler 本身有 RL training；不要把它写成纯 training-free pruning。
- `thinking` 在本篇主要是 per-step compute allocation / temporal reuse，不等于显式 CoT reasoning。
- real-world speedup 与 frequency 绑定 Franka / GR00T setting；不能直接和 LIBERO-only latency 并表。
