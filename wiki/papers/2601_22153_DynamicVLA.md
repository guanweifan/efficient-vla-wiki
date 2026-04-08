# 2601_22153_DynamicVLA

## Source
- Raw: [[raw/2601_22153_DynamicVLA.pdf]]
- Extracts manifest: [[extracts/parses/2601_22153_DynamicVLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2601_22153_DynamicVLA/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **dynamic object manipulation VLA + execution design** 论文；它的核心不是单纯做小模型，而是同时用 compact backbone、continuous inference 和 `LAAS` 去解决 perception-execution gap。
- 这篇论文要解决的是：现有 VLA 在静态 manipulation 上已经有较强泛化，但在 dynamic object manipulation 中会因为 perception-execution gap、inter-chunk waiting 和推理延迟，导致观测与执行脱节，难以应对快速运动、突发轨迹变化和长时间闭环交互。
- 核心主张是：动态操作的主失败模式不是单纯视觉歧义，而是时序失配；因此如果同时做 `compact low-latency VLA backbone`、`Continuous Inference` 和 `Latent-aware Action Streaming (LAAS)`，让推理与执行重叠、并丢弃过时 action，就能显著提升 closed-loop reactivity、dynamic adaptation 与 long-horizon sequencing。
- 作者提出 `DynamicVLA`，使用 `0.4B` 参数量 backbone，并配套 `DOM` benchmark 与自动化仿真/真实世界数据管线。
- headline 数字需要拆开理解：
  - `47.06%` 是 `DOM` simulation benchmark 上九个子维度的总平均 success rate；
  - `60.5 / 38.5 / 40.5`、`51.5 / 48.0 / 33.5`、`59.5 / 65.0 / 26.5` 分别对应不同子维度，不应压成单一“全面更强”指标；
  - `88 Hz` 与 `1.8 GB` 则是 `RTX A6000` 上的部署口径，而不是全部 real-world 系统的统一控制频率。来源：[[raw/2601_22153_DynamicVLA.pdf]]，第 1-2 页摘要与引言；第 6-7 页 Table I；第 12 页 implementation details。
- 更稳的主张是：`DynamicVLA` 通过 compact backbone、continuous inference 和 `LAAS` 同时收紧推理延迟与执行时序错位问题；它既是方法论文，也是 benchmark/data pipeline 驱动的系统性方案。

## Methodology Index
- DynamicVLA
- dynamic object manipulation
- compact 0.4B VLA
- FastViT vision encoder
- SmolLM2-360M
- action expert
- temporal reasoning
- closed-loop adaptation
- Continuous Inference
- CI
- Latent-aware Action Streaming
- LAAS
- perception-execution gap
- pipelined inference and execution
- temporally aligned action execution
- sparse temporal observation window
- DOM benchmark
- automatic simulation and real-world data collection
- Franka
- PiPER

## Data Pointer
- 摘要与总体命题：[[raw/2601_22153_DynamicVLA.pdf]] 第 1-2 页摘要、引言与 Fig. 1。这里给出 `0.4B backbone + CI + LAAS + DOM benchmark` 的总框架，以及 dynamic manipulation 的问题定义。
- 方法总览：[[raw/2601_22153_DynamicVLA.pdf]] 第 3-5 页 Fig. 2 与 Section III。这里定义 `Continuous Inference` 如何重叠推理和执行，以及 `LAAS` 如何丢弃过时 action、恢复 temporal alignment。
- DOM simulation 主结果：[[raw/2601_22153_DynamicVLA.pdf]] 第 6-7 页 Table I。这里是九个子维度、整体 `47.06%` 平均 success rate、以及 `Path Length / Time` 对比的主要来源。
- 真实机器人 interaction / perception / generalization：[[raw/2601_22153_DynamicVLA.pdf]] 第 6-8 页 Fig. 4、Fig. 5、Fig. 6。这里可回查六个 interaction task、六个 perception task、四个 generalization task 的 real-world success rate。
- 组件与速度消融：[[raw/2601_22153_DynamicVLA.pdf]] 第 8-9 页 Table II；第 12 页 implementation details。这里说明 `0.4B` 容量、`FastViT`、`CI`、`LAAS` 的各自贡献，以及 `1.8 GB / 88 Hz` 的部署信息。

## Evidence Links
- [[wiki/evidence/claims/2601_22153_DynamicVLA-headline-split.md|2601_22153_DynamicVLA-headline-split]]

## 待核点
- `47.06%` 是 `DOM` simulation benchmark 上九个子维度的平均 success rate，不应被误读成任一单任务或 real-world 平均表现。
- `88 Hz` 与 `1.8 GB` 来自 `RTX A6000` 上的 inference setting；这更像模型级推理能力，不等于整个真实机器人闭环系统在所有平台上的端到端控制频率。
- 论文的强点既可以写成“compact low-latency VLA architecture”，也可以写成“CI + LAAS 解决 perception-execution gap 的 execution design”；后续需要决定页面主轴。
- `DOM` benchmark 与自动化数据采集管线是这篇的重要组成部分；后续若只把它当成模型论文，可能会低估 benchmark/data pipeline 在整体主张中的权重。
- 若后续把它放进一般 `compact VLA` 路线，需要保留“核心是 dynamic object manipulation 与 execution design，不是单纯缩模型”这一边界。
