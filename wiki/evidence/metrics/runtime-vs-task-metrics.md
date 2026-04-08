# runtime-vs-task-metrics

## 用途
- 当前页收敛 `runtime / frequency / latency / TTFA / task completion time` 这组最容易被混写的口径，并明确它们在不同论文里分别对应哪一层 headline。
- 当前页只记录 source-grounded evidence 与不可混写项，不承担主题级 synthesis。

## Evidence
- [[wiki/papers/2410_05273_HiRT.md|2410_05273_HiRT]]：`4.1 Hz -> 9.8 Hz` 来自 Table 1 的 quasi-static 频率层；`6.18s vs 9.25s` 与 `48% -> 75%` 来自 Table 2 的 dynamic task 完成时间 / 成功率层，不能压成同一 operating point。来源：[[raw/2410_05273_HiRT.pdf]]，第 6-7 页，Table 1、Table 2。
- [[wiki/papers/2409_12514_TinyVLA.md|2409_12514_TinyVLA]]：`20x lower inference latency` 来自 Fig. 1 的 family-level latency headline；`25.7%` single-arm 平均优势与 bimanual `44.5% vs 38.2%` 属于不同 evaluation layer，不能与 latency headline 混写。来源：[[raw/2409_12514_TinyVLA.pdf]]，第 1 页 Fig. 1；第 4-5 页 Table II、Table III。
- [[wiki/papers/2603_19199_FASTER.md|2603_19199_FASTER]]：`10x` 指 immediate reaction 的 denoising compression；`3x TTFA boost` 是 reaction-time 指标；simulation / real-world task performance 仍要回到 Table 2-4 与对应 figure 读取，不能把 reaction latency 与 task performance 混成同一种速度优势。来源：[[raw/2603_19199_FASTER.pdf]]，第 1 页 Fig. 1；第 12-14 页 Table 2-4。
- [[wiki/papers/2411_02359_DeeR-VLA.md|2411_02359_DeeR-VLA]]：`5.2-6.5x` compute reduction、`2-6x` memory reduction 与 `55ms -> 17.5ms` 主要是 **LLM-side** 指标；尤其 Table 5 的 `31.2 GFLOPs / 55ms -> 6 GFLOPs / 17.5ms` 不能被误写成整套 VLA 端到端频率提升。来源：[[raw/2411_02359_DeeR-VLA.pdf]]，第 9 页，Table 5。
- [[wiki/papers/2507_14049_EdgeVLA.md|2507_14049_EdgeVLA]]：`20 ms -> 5 ms` 与 `16 GB -> 4 GB` 来自 Table I 的 A100-40GB 部署表；摘要里的 `7x speedup` 是更宽的总体 headline，不应直接与 Table I 数字视作同一 operating point。来源：[[raw/2507_14049_EdgeVLA.pdf]]，第 1 页 Abstract；第 3 页，Table I。
- [[wiki/papers/2505_21200_FlashVLA.md|2505_21200_FlashVLA]]：`36.0%` latency reduction 与 `55.7%` visual-token FLOPs reduction 绑定在 `62.5%` token budget、`OpenVLA + LIBERO` 的同一 operating point 上；它们不是所有 token budget 都成立的统一 runtime headline。来源：[[raw/2505_21200_FlashVLA.pdf]]，第 7 页，Table 1。
- [[wiki/papers/2506_10100_EfficientVLA.md|2506_10100_EfficientVLA]]：`1.93x` speedup、FLOPs 降到 baseline 的 `28.9%`、平均成功率仅下降 `0.6%` 都来自 `CogACT + SIMPLER` 的同一主 operating point；后续不能把它们拆成独立普适的效率结论。来源：[[raw/2506_10100_EfficientVLA.pdf]]，第 7-8 页，Table 2。
- [[wiki/papers/2603_07904_DyQ-VLA.md|2603_07904_DyQ-VLA]]：`1.49x` simulation 与 `up to 1.43x` real-world speedup 分属 Table I 与 Table II；前者伴随 `30.9%` memory footprint 与 `99.5%` retained performance，后者对应不同任务类别下 `0.0%-3.4%` degradation，不能 bundled。来源：[[raw/2603_07904_DyQ-VLA.pdf]]，第 6-8 页，Table I、Table II。
- [[wiki/papers/2506_07339_RTC.md|2506_07339_RTC]]：本文里的 `real-time` 不是统一 `Hz`，而是“新 chunk 在当前 execution horizon 用尽前准备好”的操作性约束；`>300 ms` 与 `20% faster` 来自 Fig. 1 caption，`average throughput` 则在 real-world Fig. 6 中按 tasks/min 统计。来源：[[raw/2506_07339_RTC.pdf]]，第 1 页 Fig. 1；第 2-3 页 Preliminaries；第 8 页 Fig. 6。
- [[wiki/papers/2507_05116_VOTE.md|2507_05116_VOTE]]：`39x faster` 与 `46 Hz throughput` 绑定的是 Jetson Orin 边缘部署；`>20%` LIBERO 与 `+7%` SimplerEnv 属于 task performance，不是 runtime 指标。来源：[[raw/2507_05116_VOTE.pdf]]，第 2 页 Introduction；第 9 页 latency / throughput table。
- [[wiki/papers/2512_03044_Video2Act.md|2512_03044_Video2Act]]：`real-time action generation frequency` 主要由 asynchronous dual-system 机制支撑，但文中更硬的直接部署数字是 `587.9 ms` cold-start latency；不能把它改写成固定高 Hz 控制结论。来源：[[raw/2512_03044_Video2Act.pdf]]，第 5 页 Fig. 3；第 6-7 页 real-world section。
- [[wiki/papers/2602_18397_VLA-Perf.md|2602_18397_VLA-Perf]]：本文显式把 `performance` 定义为 inference latency / throughput，并把 `10 Hz` 视作 acceptable、`100 Hz` 视作 high-performance；`asynchronous inference` 主要改善 throughput，不必然降低 end-to-end latency。来源：[[raw/2602_18397_VLA-Perf.pdf]]，第 2-3 页 Fig. 1-2；第 12-13 页 Table 8 与相邻正文。
- [[wiki/papers/2506_13725_CEED-VLA.md|2506_13725_CEED-VLA]]：`3.6x / 2.0x` 是 Fig. 1 caption 中 OpenVLA / LLaVA-VLA 的 decoding speedup；`4x frequency` 则是 real robotic arm deployment headline。它们不属于同一 deployment layer。来源：[[raw/2506_13725_CEED-VLA.pdf]]，第 2 页 Fig. 1；实验章节。

## 不可混写项
- `Hz`、`Time/s`、`TTFA`、整体 inference latency、task completion time 不是同一种 runtime 指标。
- family-level latency headline、table-level task performance 和 dynamic reaction-time headline 不能压成统一 superiority claim。
- 只要 headline 同时跨 benchmark、metric family 或 deployment setting，就必须拆回各自的 table / figure layer。
- `real-time` 也不是统一指标：有的论文把它写成 camera-rate latency 目标，有的写成 edge throughput，有的写成异步 chunking 约束；引用前必须回到原文定义。

## 影响页面
- [[wiki/papers/2410_05273_HiRT.md|2410_05273_HiRT]]
- [[wiki/papers/2409_12514_TinyVLA.md|2409_12514_TinyVLA]]
- [[wiki/papers/2603_19199_FASTER.md|2603_19199_FASTER]]
- [[wiki/papers/2411_02359_DeeR-VLA.md|2411_02359_DeeR-VLA]]
- [[wiki/papers/2507_14049_EdgeVLA.md|2507_14049_EdgeVLA]]
- [[wiki/papers/2505_21200_FlashVLA.md|2505_21200_FlashVLA]]
- [[wiki/papers/2506_10100_EfficientVLA.md|2506_10100_EfficientVLA]]
- [[wiki/papers/2603_07904_DyQ-VLA.md|2603_07904_DyQ-VLA]]
- [[wiki/papers/2506_07339_RTC.md|2506_07339_RTC]]
- [[wiki/papers/2507_05116_VOTE.md|2507_05116_VOTE]]
- [[wiki/papers/2512_03044_Video2Act.md|2512_03044_Video2Act]]
- [[wiki/papers/2602_18397_VLA-Perf.md|2602_18397_VLA-Perf]]
- [[wiki/papers/2506_13725_CEED-VLA.md|2506_13725_CEED-VLA]]

## 边界
- 当前页只记录 runtime-related evidence 与不可混写项。
- 若如需讨论为什么某类效率路线在不同论文中演化成不同系统设计，应留到 `Pass 4`。
