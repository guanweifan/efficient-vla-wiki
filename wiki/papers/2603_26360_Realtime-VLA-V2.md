# 2603_26360_Realtime-VLA-V2

## Source
- Raw: [[raw/2603_26360_Realtime-VLA-V2.pdf]]
- Extracts manifest: [[extracts/parses/2603_26360_Realtime-VLA-V2/manifest.json]]
- Primary text fallback: [[extracts/parses/2603_26360_Realtime-VLA-V2/pdftotext.txt]]
- Fine-grained locator: [[extracts/parses/2603_26360_Realtime-VLA-V2/pdftotext.bbox.html]]

## Claim
- 页面定位：这是一篇 **system-level faster-than-demonstration deployment report**；它的主贡献是把 calibration、trajectory post-processing、control 和 speed adaptation 组合成一套真实机器人执行框架，而不是单一模型结构创新。
- 这篇论文要解决的是：VLA 在真实机器人上“跑得快”并不只是 GPU inference 更快，还同时受制于 control latency、trajectory smoothness、hardware dynamics 和 faster-than-demonstration mismatch。作者把问题写成 `fast + smooth + accurate` 的联合系统目标。来源：[[raw/2603_26360_Realtime-VLA-V2.pdf]]，Abstract；Introduction。
- `Realtime-VLA V2` 给出的解法是一套分层系统栈：先做 camera / proprio / motion latency calibration，再对 VLA 轨迹做 temporal optimization 与 spatial optimization，并通过 speed adaptation model 学习什么时候加速、什么时候减速。来源：[[raw/2603_26360_Realtime-VLA-V2.pdf]]，Sec. 3-5。
- 论文展示了多组 demo-level headline，例如某些任务里 human demonstration `75.3s / 89.5s / 98.6s` 对应 VLA execution `18.9s / 37.8s / 42.6s`，并强调真实运行速度已经接近日常人类操作与轻量机械臂的硬件上限。这些任务级时间例子不能直接压成统一 benchmark claim。来源：[[raw/2603_26360_Realtime-VLA-V2.pdf]]，Fig. 1；Abstract。
- 更稳的主张是：这篇工作把“让 VLA 真正在机器人上高速而稳定地跑起来”写成系统工程问题，并用 latency calibration、trajectory shaping 和 human-in-the-loop speed modulation 去逼近 faster-than-demonstration execution。

## Methodology Index
- Realtime-VLA V2
- faster-than-demonstration execution
- system latency calibration
- camera / proprio / motion delay compensation
- temporal optimization
- spatial optimization
- speed adaptation model
- human-in-the-loop throttle
- hardware-friendly smooth trajectory
- deployment-oriented VLA

## Data Pointer
- **Abstract + Introduction**：适合后续补 `fast + smooth + accurate` 的问题设定和系统级定位。
- **Fig. 1**：适合后续补 human demonstration 与 VLA execution 的任务级时间例子。
- **Sec. 3 + Fig. 2**：适合后续补 camera / proprio / motion delay 的校准方法与系统延迟分解。
- **Sec. 4 + Fig. 4**：适合后续补 temporal optimization、spatial optimization 与 client-server post-processing 框架。
- **Sec. 5 + Fig. 5 / Fig. 6**：适合后续补 human-in-the-loop speed modulation 数据采集与 speed adaptation 训练逻辑。
- **后续实验章节**：适合后续补速度上界分析、失败阶段分布与不同 speed-up factor 的影响。

## Evidence Links
- [[wiki/evidence/claims/2603_26360_Realtime-VLA-V2-headline-split.md|2603_26360_Realtime-VLA-V2-headline-split]]

## 待核点
- 当前 paper 更像 system report；后续若要和单一模型方法并排比较，需要把“系统调参收益”和“模型结构收益”分开。
- `18.9s / 37.8s / 42.6s` 这类时间 headline 是任务级例子，不是统一 benchmark 结果。
- 论文强调 approach 接近硬件上限，但其可迁移性仍依赖具体 robot、camera 与 control stack，后续不能写成普适部署结论。
