# 2603_26360_Realtime-VLA-V2-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_26360_Realtime-VLA-V2.md|2603_26360_Realtime-VLA-V2]] 的单篇证据落点，用来拆开 task-level demo 时间、系统延迟校准和 system stack 叙事。

## Evidence
- 核心证据命题：论文把 faster-than-demonstration VLA execution 写成系统工程问题，主目标是同时满足 fast、smooth、accurate。来源：[[raw/2603_26360_Realtime-VLA-V2.pdf]]，Abstract；Introduction。
- 补充证据命题：主要工具链包括 latency calibration、trajectory temporal / spatial optimization、speed adaptation model 与 human-in-the-loop throttle。来源：[[raw/2603_26360_Realtime-VLA-V2.pdf]]，Sec. 3-5。

## Table / Metric Anchors
- **Fig. 1**：task-level human demonstration vs VLA execution 时间例子。
- **delay calibration table**：`t_readout / t_camera / t_proprio / t_motion` 的系统延迟分解。
- **Sec. 4 / Sec. 5**：post-processing 与 speed adaptation 的主要实现位置。

## 不可混写项
- `75.3s -> 18.9s`
- `89.5s -> 37.8s`
- `98.6s -> 42.6s`
- 这些是任务级例子，不是统一 benchmark 指标。
- system delay calibration、trajectory shaping 和 learned speed modulation 也不能压成单一“模型更强”结论。

## 影响页面
- [[wiki/papers/2603_26360_Realtime-VLA-V2.md|2603_26360_Realtime-VLA-V2]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]

## 边界
- 本页只服务单篇 system report 的 claim 收口，不替代部署主题页的跨论文边界判断。
