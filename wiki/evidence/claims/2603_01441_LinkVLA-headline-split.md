# 2603_01441_LinkVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_01441_LinkVLA.md|2603_01441_LinkVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`86%` 的速度节省是相对本论文的 `AR` variant 而不是对所有 baseline 的统一加速倍数；引用时要保留比较对象。

## Evidence
- 核心证据命题：这篇论文要解决的是：自动驾驶 VLA 虽然具备语言推理与交互潜力，但现有方法仍有两个核心问题，一是语言指令与动作轨迹之间存在 persistent misalignment，二是典型 autoregressive action generation 推理过慢，不利于实时部署。 来源：[[raw/2603_01441_LinkVLA.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 补充证据命题：作者提出 `LinkVLA`，核心思路是同时解决“对齐”和“速度”两件事：一方面把语言 token 与动作 token 放入统一离散 codebook，在结构上建立 language-action link；另一方面加入 `action understanding objective`，要求模型从轨迹反向生成描述性文本，在训练中显式强化双向语言-动作语义绑定；同时用 `coarse-to-fine (C2F)` 两阶段轨迹生成替代逐步 AR 解码。 来源：[[raw/2603_01441_LinkVLA.pdf]]，论文的双重问题设定、`action understanding` 与 `C2F` 的高层动机、以及 `saving 86% inference time` 的 headline 都在这里。
- 主证据锚点 1：来源：[[raw/2603_01441_LinkVLA.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 主证据锚点 2：来源：[[raw/2603_01441_LinkVLA.pdf]]，论文的双重问题设定、`action understanding` 与 `C2F` 的高层动机、以及 `saving 86% inference time` 的 headline 都在这里。
- 主证据锚点 3：来源：[[raw/2603_01441_LinkVLA.pdf]]，`PDF p.3-5` Fig. 2 + Sec. 3：

## Table / Metric Anchors
- `PDF p.6-7` Table 1 + closed-loop result discussion：
  - `Bench2Drive` 主结果、`91.01` driving score、`74.55%` success rate、多能力评估都应回这里核定。
- `PDF p.7` Table 2 + latency discussion：
  - `AR 361 ms -> C2F 48 ms`、与 `SimLingo` / `Orion` 的 latency-performance 对比在这里。
- `PDF p.7-8` Table 3 + instruction-following discussion：
  - `87.16%` mean success、tokenization / C2F / alignment 的逐步增益，以及各类 instruction task 的提升应回这里。

## Table / Metric Split
- ``PDF p.6-7` Table 1 + closed-loop result discussion` 这一层支撑 ``PDF p.6-7` Table 1 + closed-loop result discussion` 对应的 benchmark / metric / operating point。 - `Bench2Drive` 主结果、`91.01` driving score、`74.55%` success rate、多能力评估都应回这里核定。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2603_01441_LinkVLA.pdf]]，``PDF p.6-7` Table 1 + closed-loop result discussion`。
- ``PDF p.7` Table 2 + latency discussion` 这一层支撑 ``PDF p.7` Table 2 + latency discussion` 对应的 benchmark / metric / operating point。 - `AR 361 ms -> C2F 48 ms`、与 `SimLingo` / `Orion` 的 latency-performance 对比在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2603_01441_LinkVLA.pdf]]，``PDF p.7` Table 2 + latency discussion`。
- ``PDF p.7-8` Table 3 + instruction-following discussion` 这一层支撑 ``PDF p.7-8` Table 3 + instruction-following discussion` 对应的 benchmark / metric / operating point。 - `87.16%` mean success、tokenization / C2F / alignment 的逐步增益，以及各类 instruction task 的提升应回这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2603_01441_LinkVLA.pdf]]，``PDF p.7-8` Table 3 + instruction-following discussion`。

## 不可混写项
- `86%` 的速度节省是相对本论文的 `AR` variant 而不是对所有 baseline 的统一加速倍数；引用时要保留比较对象。
- `91.01` / `74.55%` 与 `87.16%` 分别来自 closed-loop driving 与 instruction-following 两套评测，不能混成单一 headline。
- latency 分析里作者明确不计入 `CoT` 生成成本；如果写“整体推理延迟”，要保留这一 caveat。

## 影响页面
- [[wiki/papers/2603_01441_LinkVLA.md|2603_01441_LinkVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
