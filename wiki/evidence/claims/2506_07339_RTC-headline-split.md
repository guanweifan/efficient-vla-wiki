# 2506_07339_RTC-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2506_07339_RTC.md|2506_07339_RTC]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`20% faster`、`>300ms latency`、`12 tasks`、`6 real-world bimanual tasks` 目前只保留为 headline claim；后续 `L2` 需要分别钉到具体 figure / experiment setting / baseline。

## Evidence
- 这篇论文提出 **real-time chunking (RTC)**，目标是在**不重训模型**的前提下，让 action chunking policy 真正实现实时、异步执行。作者的问题定义是：虽然 action chunking 能改善高频控制中的时间一致性，但并没有真正解决大模型的高延迟问题，尤其会在 chunk 边界引入停顿、跳变或 out-of-distribution 的 jerk。来源：[[raw/2506_07339_RTC.pdf]]，第 1-2 页 Abstract、Introduction。
- 核心主张是：把异步 action chunking 重写成一个**inpainting problem**。RTC 在执行当前 chunk 的同时生成下一个 chunk，并对必然会被执行的 prefix action 进行 **freezing**，对剩余部分进行 **inpainting**，从而在存在 inference delay 时仍保持动作连续性和可执行性。来源：[[raw/2506_07339_RTC.pdf]]，第 1 页 Abstract；第 2-5 页 Sec. 1-3、Fig. 2、Fig. 3。
- 主证据锚点 1：来源：[[raw/2506_07339_RTC.pdf]]，**Abstract + Fig. 1**：第 1 页。用于锚定 “20% faster / >300ms latency / lighting a match” 的 headline evidence。
- 主证据锚点 2：来源：[[raw/2506_07339_RTC.pdf]]，**Introduction / contributions**：第 2 页。用于锚定 RTC 的问题定义、适用范围和 benchmark 设计。
- 主证据锚点 3：来源：[[raw/2506_07339_RTC.pdf]]，**Preliminaries + Fig. 2**：第 2-3 页。用于锚定 action chunking、execution horizon、inference delay 和 naive async failure mode。

## Figure / Caption Anchors
- **Fig. 1 (p.1)**：caption 明确把两类 headline 分开写：上半部分是 `>300 ms` inference delay 下的 `lighting a match` 精细任务；下半部分是同一 real rollout 中 `20% faster` 且更平滑的 shoulder-joint motion，对比对象是 synchronous inference 与 temporal ensembling。
- **Fig. 2 (p.3)**：caption 与相邻正文解释了 naive asynchronous chunking 在 chunk boundary 处出现 bifurcation / jerky behavior，说明“异步本身”不是 RTC 的充分条件。
- **Fig. 3 + Algorithm 1 (p.4-5)**：是 RTC 机制主锚点；这里才真正定义了 `freezing guaranteed prefix + inpainting remaining suffix` 的解法，而不是简单 overlap / averaging。
- **Fig. 6 (p.8)**：real-world 6 个双臂任务在 injected delay 下的 average throughput 与 robustness 结果；这里支撑的是 `delay robustness + task throughput`，不是 `Hz` 或固定 latency。

## Figure / Caption / Wording Split
- `real-time` 在本文不是泛指相机帧率或统一 `Hz` 数字，而是预备章节中的操作性定义：当新的 action chunk 能在当前 execution horizon 耗尽前准备好时，系统满足 real-time constraint。来源：[[raw/2506_07339_RTC.pdf]]，第 2-3 页 Preliminaries。
- `Fig. 1` 的两条 headline 不能混写：上半部分支撑的是 **precise-task robustness under >300 ms delay**，下半部分支撑的是 **同一 match-lighting rollout 上 20% faster and smoother than synchronous inference**。来源：[[raw/2506_07339_RTC.pdf]]，第 1 页 Fig. 1 caption。
- `Fig. 2` 支撑的是 **为什么 naive async / averaging 失败**，不是 RTC 自身的速度提升结果；它只能用来说明 jerk / mode-jumping failure mode。来源：[[raw/2506_07339_RTC.pdf]]，第 3 页 Fig. 2 与相邻正文。
- `Fig. 3 + Algorithm 1` 支撑的是 **freezing + inpainting mechanism**，而不是 benchmark 结果；若写“RTC works because ...”，应优先回到这里，而不是直接复述 abstract headline。来源：[[raw/2506_07339_RTC.pdf]]，第 4-5 页 Fig. 3、Algorithm 1。

## 不可混写项
- `20% faster`、`>300ms latency`、`12 tasks`、`6 real-world bimanual tasks` 目前只保留为 headline claim；后续 `L2` 需要分别钉到具体 figure / experiment setting / baseline。
- RTC 适用于 diffusion- 或 flow-based policy，这个适用边界对后续 taxonomy 很关键；需要主编决定在单篇页里是否更强调“algorithm overlay”而非“new policy family”。
- 论文多次把 `smoothness`、`throughput`、`success under delay` 放在一起讨论，仍需决定是否把其中一个明确设为主 claim，其余降为 supporting claim。

## 影响页面
- [[wiki/papers/2506_07339_RTC.md|2506_07339_RTC]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
