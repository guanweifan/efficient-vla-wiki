# 2602_20200_OptimusVLA

## Source
- Raw: [[raw/2602_20200_OptimusVLA.pdf]]
- Extracts manifest: [[extracts/parses/2602_20200_OptimusVLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2602_20200_OptimusVLA/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **dual-memory hierarchical VLA / action-generation efficiency+robustness** 论文；它的核心不是一般视觉 backbone 压缩，而是围绕 action generation 的 prior alignment 与 temporal consistency 重写 memory 结构。
- 这篇论文要解决的是：层次化 VLA 往往已经拥有很强的 perception 与 language backbone，但 action generation 仍然是效率与鲁棒性的共同瓶颈。一方面，Gaussian noise prior 与目标 action distribution 的 gap 很大，导致需要较多 denoising / function evaluations；另一方面，仅依赖当前 observation 会忽略 task progress 与历史执行一致性，进而造成 jitter 和阶段感知不足。
- 核心主张是：如果同时给 action generation 引入一个面向全局任务先验的 memory 和一个面向局部时间一致性的 memory，就能在不显著牺牲灵活性的前提下，缩短 generative path、减少 NFE，并提升长时程和真实机器人场景下的稳定性。
- 作者提出 `OptimusVLA`，一个由 `Global Prior Memory (GPM)` 与 `Local Consistency Memory (LCM)` 共同驱动的 dual-memory VLA framework。
- headline 数字需要拆开理解：
  - `98.6%` 对应 `LIBERO` 的 average success rate；
  - 相对 `π0` 的 `13.5%` 提升对应 `CALVIN`；
  - `38%` 对应 `RoboTwin 2.0 Hard` 的 average success rate；
  - `42.9%` 与 `52.4%` 分别对应 real-world `Generalization` 与 `Long-horizon` suites 相对 `π0` 的提升；
  - `2.9×` 则是 inference speedup 口径，并与 `NFE` 从 `10` 降到 `3.2 / 3.4` 强相关。来源：[[raw/2602_20200_OptimusVLA.pdf]]，第 1-3 页摘要、引言与 Fig. 1；第 5-7 页 Tables 1-5；第 6-7 页 Fig. 3-5。
- 更稳的主张是：`OptimusVLA` 证明在 hierarchical VLA 中，把全局任务先验和局部时间一致性分别写入双 memory，可以同时改善 action generation 的稳定性与推理效率，尤其对 long-horizon 与 real-world rollout 更有帮助。

## Methodology Index
- OptimusVLA
- dual-memory VLA
- hierarchical VLA
- Global Prior Memory
- GPM
- Local Consistency Memory
- LCM
- prior-aware sampler
- task-level prior retrieval
- memory bank
- adaptive noise scale
- adaptive NFE
- consistency layer
- dynamic-awareness module
- temporal consistency constraint
- progress awareness
- flow policy
- LIBERO
- CALVIN
- RoboTwin 2.0
- real-world generalization
- long-horizon manipulation

## Data Pointer
- 摘要与总框架：[[raw/2602_20200_OptimusVLA.pdf]] 第 1-3 页摘要、引言与 Fig. 1。这里给出 `GPM + LCM` 如何分别处理 prior-target gap 与 temporal dependence，以及 `98.6 / 13.5 / 38 / 2.9×` 的 headline。
- 方法总览：[[raw/2602_20200_OptimusVLA.pdf]] 第 3-5 页 Fig. 2 与 Section 3。这里定义 `Prior Head`、`Memory Bank`、`Prior-Aware Sampler`、`Consistency Layer` 和 `Dynamic-Awareness module` 的作用分工。
- Simulation 主结果：[[raw/2602_20200_OptimusVLA.pdf]] 第 5-6 页 Table 1、Table 2、Table 3。这里对应 `LIBERO` 的 `98.6%`、`CALVIN` 的 `4.45 Avg. Len.` 与相对 `π0` 的 `13.5%` 提升，以及 `RoboTwin 2.0 Hard` 的 `38%` average success rate。
- Real-world 与效率结果：[[raw/2602_20200_OptimusVLA.pdf]] 第 6-7 页 Fig. 3、Fig. 5 与相邻正文。这里对应 Generalization / Long-horizon suites 的 real-world 结果、`2.9×` inference speedup，以及 `NFE` 从 `10` 降到 `3.2 / 3.4` 的比较。
- 组件归因：[[raw/2602_20200_OptimusVLA.pdf]] 第 6-7 页 Table 4、Table 5。这里说明去掉 `GPM` 或 `LCM` 带来的性能下降，以及 memory size / retrieved trajectory 数量对 `LIBERO-Long` 的影响。

## 待核点
- `98.6% / 13.5% / 38% / 42.9% / 52.4% / 2.9×` 分别来自不同 benchmark 与不同口径，后续不能压成一个无条件统一 headline。
- `2.9× inference speedup` 与 `NFE` 减少强相关，但具体口径依赖与 `π0 / π0.5` 的比较设置；后续若写效率结论，需要保留 benchmark 和 baseline 条件。
- 论文同时强调 efficiency 和 robustness，其中 `GPM` 更偏 prior alignment / NFE reduction，`LCM` 更偏 temporal consistency / progress awareness；后续页面主轴需要决定更强调哪一侧。
- real-world 结果集中在 `GALAXEA R1 Lite` 的 Generalization 与 Long-horizon suites，不应直接泛化成任意机器人或任意 manipulation setup 的普适优势。
