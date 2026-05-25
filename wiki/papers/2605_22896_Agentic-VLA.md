# 2605_22896_Agentic-VLA

## Source
- Raw: [[raw/2605_22896_Agentic-VLA.pdf]]
- Extracts manifest: [[extracts/parses/2605_22896_Agentic-VLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2605_22896_Agentic-VLA/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **agentic online adaptation / language-guided exploration for VLA** 论文；它把效率收益主要放在更快在线适配、长程任务泛化和跨任务迁移上。
- Agentic-VLA 由 Adaptive Reward Synthesis、Language-Guided Exploration 与 Experience Memory 组成，用语言分解、奖励调整和经验复用辅助 VLA 在线训练。来源：[[raw/2605_22896_Agentic-VLA.pdf]]，Abstract、Figure 1、Algorithm 1。
- 论文在 LIBERO 和 RoboTwin 2.0 上报告 long-horizon、one-shot、cross-task transfer 与 training efficiency 结果，包括 2.4x faster convergence 的训练效率主张。来源：[[raw/2605_22896_Agentic-VLA.pdf]]，Abstract、Tables 1-6、Table 8。
- 更稳的主张是：Agentic-VLA 属于 online adaptation / training efficiency，不是测试时 always-on reasoning compression。

## Methodology Index
- online adaptation
- Adaptive Reward Synthesis
- Language-Guided Exploration
- Experience Memory
- long-horizon tasks
- one-shot adaptation
- cross-task transfer
- LIBERO
- RoboTwin 2.0
- training convergence

## Data Pointer
- **Figure 1 / Algorithm 1**：framework and training procedure。
- **Tables 1-4**：LIBERO main、one-shot、cross-task transfer 与 training efficiency。
- **Tables 5-6**：ablation and controlled comparisons。
- **Table 8**：RoboTwin 2.0 hard setting。
- **Figures 2-5**：reward adjustment、learning curves、experience memory 与 emergent capabilities。

## Evidence Links
- [[wiki/evidence/claims/2605_22896_Agentic-VLA-headline-split.md|2605_22896_Agentic-VLA-headline-split]]

## 待核点
- language-guided exploration 发生在在线训练 / 适配过程中，不应写成推理期 reasoning 路线。
- long-horizon、one-shot、cross-task transfer 与 convergence speed 是不同结果口径。
- 经验记忆的作用需要保留训练闭环和任务设置边界。
