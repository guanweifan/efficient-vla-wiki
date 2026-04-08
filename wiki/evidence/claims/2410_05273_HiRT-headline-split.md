# 2410_05273_HiRT-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2410_05273_HiRT.md|2410_05273_HiRT]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`double the control frequency` 在正文主表里对应的是 `4.1 Hz -> 9.8 Hz`，更接近 `2.39x`；如果要引用“翻倍”这一说法，需区分 abstract headline 与具体实验设置。

## Evidence
- 核心证据命题：这篇论文聚焦 VLA / VLM 后端带来的低控制频率和高延迟问题，目标是在尽量保留泛化能力的同时，把系统推到更适合动态操作的控制速度。 来源：[[raw/2410_05273_HiRT.pdf]]，`PDF p.1` Abstract：
- 补充证据命题：作者提出 `HiRT`，把慢速、高层语义理解的 VLM 与高速、低层动作执行策略做成层级式异步系统：VLM 低频更新 latent，轻量视觉策略高频读取 latent 并连续输出动作。 来源：[[raw/2410_05273_HiRT.pdf]]，问题定义、HiRT 总体主张、`double the control frequency`、动态真实任务 `48% -> 75%` 的 headline 结果都在这里。
- 主证据锚点 1：来源：[[raw/2410_05273_HiRT.pdf]]，`PDF p.1` Abstract：
- 主证据锚点 2：来源：[[raw/2410_05273_HiRT.pdf]]，问题定义、HiRT 总体主张、`double the control frequency`、动态真实任务 `48% -> 75%` 的 headline 结果都在这里。
- 主证据锚点 3：来源：[[raw/2410_05273_HiRT.pdf]]，`PDF p.2` Fig. 1：

## Table / Metric Anchors
- `PDF p.6` Table 1 + Fig. 4：
  - 静态任务的 success rate 与 speed 对照；`9.8 Hz`、接近 Vanilla-VLA 性能但更高推理速度的核心证据在这里。
- `PDF p.7` Table 2 + Fig. 6：
  - 动态真实任务的核心结果；`Time/s`、`Seen/Unseen/Average` 以及高延迟 baseline 失败的可视化对比都在这里。
- `PDF p.7-8` Table 3：
  - 说明 image context 与 combined conditioning 对性能的作用，用于锚定 ablation evidence。

## Table / Metric Split
- `Table 1` 对应 **quasi-static / static real-world** 这一层：`HiRT` 的 `9.8 Hz` 应与 `Vanilla-VLA` 的 `4.1 Hz` 放在同一个控制频率口径下比较；同表里的静态真实任务平均值则是 `70.0` 对 `71.3`，因此这张表支持的是“更高控制频率且静态性能大体可比”，不是“全 setting 全面优于 baseline”。来源：[[raw/2410_05273_HiRT.pdf]]，第 6 页，Table 1。
- `Table 2` 对应 **dynamic real-world** 这一层：`HiRT` 的 `6.18 s` completion time 与 `80 / 70 / 75`（Seen / Unseen / Average）应和 `Vanilla-VLA` 的 `9.25 s` 与 `55 / 40 / 48` 成对阅读；这张表支撑的是动态任务下的反应与完成时间优势，而不是 quasi-static 频率 headline。来源：[[raw/2410_05273_HiRT.pdf]]，第 7 页，Table 2。
- `Table 3` 只负责解释 **为什么 full HiRT 比去掉 image context / combined conditioning 的版本更稳**；它是组件归因层，不能与 Table 1 / Table 2 的主 headline 混成同一性能结论。来源：[[raw/2410_05273_HiRT.pdf]]，第 7-8 页，Table 3。

## 不可混写项
- `double the control frequency` 在正文主表里对应的是 `4.1 Hz -> 9.8 Hz`，更接近 `2.39x`；如果要引用“翻倍”这一说法，需区分 abstract headline 与具体实验设置。
- 静态真实任务里，HiRT 的平均值 `70.0` 低于 Vanilla-VLA 的 `71.3`；若写“整体优于 baseline”，必须明确区分 simulation、static real-world、dynamic real-world 三类结果，也不要把动态场景的系统收益外推到全部 setting。
- Table 1 的 `Speed/Hz` 与 Table 2 的 `Time/s` 分别对应控制频率和任务完成时间；后续不能把二者都写成同一种 latency/speedup 指标。

## 影响页面
- [[wiki/papers/2410_05273_HiRT.md|2410_05273_HiRT]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
