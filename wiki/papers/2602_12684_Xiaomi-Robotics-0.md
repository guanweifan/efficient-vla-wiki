# 2602_12684_Xiaomi-Robotics-0

## Source
- Raw: [[raw/2602_12684_Xiaomi-Robotics-0.pdf]]
- Extracts manifest: [[extracts/parses/2602_12684_Xiaomi-Robotics-0/manifest.json]]
- Primary text fallback: [[extracts/parses/2602_12684_Xiaomi-Robotics-0/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **VLA recipe / deployment system report**；它的核心是把 pre-training、post-training、asynchronous execution 和 rollout alignment 组合成一套可实时部署的完整方案，而不是单一算法模块论文。
- 这篇论文提出 **Xiaomi-Robotics-0**，目标是在保持大规模 VLA 泛化能力的同时，实现**fast and smooth real-time execution**。作者的基本判断是：VLA 的主要落地难点并不只是精度，而是高推理延迟会让连续 action chunk 难以平滑衔接，导致真实机器人 rollout 出现 jerkiness 和 OOD motion。来源：[[raw/2602_12684_Xiaomi-Robotics-0.pdf]]，第 1-2 页 Abstract、Introduction。
- 方法上的主张不是单一模块创新，而是一套完整的 **training recipe + deployment strategy**。模型本身由 **Qwen3-VL-4B-Instruct** 作为 VLM 骨干，加上一个基于 **flow-matching** 的 diffusion transformer 动作生成器，整体约 **4.7B 参数**。训练上分为 pre-training 和 post-training 两阶段；post-training 中又专门针对 **asynchronous execution** 设计了 action prefix conditioning、`Λ-shape attention mask` 等机制，以兼顾连续性和反应性。来源：[[raw/2602_12684_Xiaomi-Robotics-0.pdf]]，第 1-4 页 Abstract、Fig. 1、Sec. 2。
- 论文保留了多组 headline numeric claims，但需要拆开理解：
  - **simulation benchmark claim**：`LIBERO 98.7%`、`SimplerEnv 85.5% / 74.7% / 79.2%` 属于不同 benchmark 与 setting 的任务表现；
  - **chain-completion claim**：`CALVIN` 的 `4.54 -> 4.75`、`4.67 -> 4.80` 属于另一种连续任务指标；
  - **real-world deployment claim**：`Lego Disassembly` 与 `Towel Folding` 更强调高 throughput 与平滑实时执行，而不是和前述 benchmark 完全同口径的 success headline。来源：[[raw/2602_12684_Xiaomi-Robotics-0.pdf]]，第 1-2 页 Abstract、Introduction；第 5-8 页 Table 1、Table 2、Fig. 6。
- 更稳的单篇主命题应写成：Xiaomi-Robotics-0 是一篇 **面向真实部署的完整 VLA recipe / system report**；其重点在于 cross-embodiment pretraining、异步执行训练、chunk alignment 与 consumer-grade GPU rollout 的整体联动，而不是某个单独 acceleration module。来源：[[raw/2602_12684_Xiaomi-Robotics-0.pdf]]，第 1-4 页 Abstract、Introduction、Sec. 2；第 7-8 页 real-robot experiments。

## Methodology Index
- real-time VLA execution
- training recipe
- deployment strategy
- asynchronous execution
- action prefix conditioning
- Λ-shape attention mask
- flow-matching action generation
- diffusion transformer
- Qwen3-VL-4B-Instruct
- 4.7B parameter VLA
- Choice Policies
- cross-embodiment pretraining
- bimanual manipulation
- chunk alignment
- consumer-grade GPU deployment

## Data Pointer
- **Abstract**：第 1 页。适合后续回收 `real-time execution`、`asynchronous rollout`、`consumer-grade GPU` 和 simulation / real-robot headline。
- **Figure 1 + Introduction**：第 2 页。适合后续补为什么高延迟会导致 jerky motion，以及 training recipe + deployment strategy 的总体 framing。
- **Sec. 2.2 / Figure 3 / Figure 4**：第 3-5 页。适合后续补 `Qwen3-VL-4B + DiT flow-matching`、Choice Policies、pre-training / post-training、Λ-shape attention mask 与 async execution。
- **Table 1 / CALVIN results**：第 5-7 页。适合后续补 LIBERO、SimplerEnv、CALVIN 上的 benchmark 数字与不同指标口径。
- **Figure 6 + real-robot section**：第 7-8 页。适合后续补 Lego Disassembly 与 Towel Folding 上的 success / throughput 对比，以及 async vs sync vs π0.5 的差异。
- **VLM benchmark section**：后续章节。适合后续补它与底层预训练 VLM 的对齐关系，以及是否保留了通用视觉语言能力。

## Evidence Links
- [[wiki/evidence/claims/2602_12684_Xiaomi-Robotics-0-headline-split.md|2602_12684_Xiaomi-Robotics-0-headline-split]]

## 待核点
- `98.7%`、`85.5% / 74.7% / 79.2%`、`4.75 / 4.80`、真实机器人 throughput 都来自不同 benchmark 与不同指标；后续需要拆清各自的比较对象和评价方式。
- 论文同时使用 `Xiaomi-Robotics-0`、`advanced VLA model`、`open-sourced VLA model with real-time execution` 等 framing；后续 taxonomy 需要统一其主定位。
- 真实机器人部分更强调 throughput 和 smooth rollout，而不是单纯 success rate；后续需要决定在单篇主 claim 中把“实时平滑执行”放多高。
- 论文是 “report” 风格，覆盖 recipe、数据、模型、部署、VLM benchmark 对齐；后续需要决定哪些属于主线，哪些降为 supporting evidence。
- 若后续把它与一般方法论文并列，需要显式保留“这是 recipe / system report，不是单模块算法 paper”这一边界。
