# q0001-efficient-vla-research-map

## Canonical Question
- 当前 Efficient VLA 领域大致可以分成哪些核心研究方向？
- 每一类分别在解决什么问题、为什么重要、彼此之间的边界和联系是什么？
- 如果结合代表性工作，怎样才能快速建立对这一领域整体格局的清晰认识？

## Scope
- 本文基于当前 `wiki/` 已沉淀的 `108` 篇 `papers/` 页面与现有 `synthesis` 页面，目标是给出一份**结构化全景综述**，而不是穷举所有论文或做单一 benchmark 排名。
- 默认把 Efficient VLA 理解为：在 embodied control 闭环里，以更低总代价保留足够能力。
- 分类原则不是按 `manipulation / driving / navigation` 场景分，也不是按 `pruning / quantization / Mamba` 这类局部技巧分，而是按**作者把哪一层成本当成首要瓶颈**来分。
- 这份 thread 主要服务“快速建图”和“建立正确边界”，不把它当成事实来源；关键事实仍应回到对应 `wiki` 页面，必要时再回 `raw/`。

## Current Answer
- 目前最稳定的全景划分是：**`3` 个宏观家族、`5` 条主路线**。
- `供给侧效率`
  - `model-and-representation efficiency`
  - `training-and-adaptation efficiency`
- `运行时效率`
  - `inference-time compute allocation`
  - `reasoning efficiency`
- `落地侧效率`
  - `deployment-oriented efficiency`
- 这套划分背后的核心判断是：Efficient VLA 并不是单一“加速”问题，而是 embodied loop 中至少 `5` 层成本同时可能成为瓶颈：
  - policy substrate 本身是否过大、过密、过难部署；
  - 模型是否需要高昂训练、蒸馏或数据成本才能得到；
  - 单步控制时是否把计算花在真正必要的 token / step / chunk 上；
  - reasoning 收益是否必须依赖 always-on 显式思维开销；
  - 前述收益在真实硬件、网络、控制周期和 jitter 约束下是否仍然成立。
- 因而，当前领域更像是在回答“**哪一层成本最值得被一等设计**”，而不是在争论某一种局部技巧是否统一胜出。

## Structured Notes

### 1. 先用一个总图来理解这个领域
- 如果从综述视角看，Efficient VLA 的主线不是“更快模型”，而是“如何让 VLA 从训练到部署都更接近真实可用”。
- 现有语料显示，这个方向已经从早期的 `smaller / faster` headline，演化成更明确的多轴议程：
  - `model size / memory / representation efficiency`
  - `training cost / data efficiency / adaptation cost`
  - `runtime latency / throughput / frequency`
  - `reasoning overhead`
  - `deployment constraint / placement / jitter / memory ceiling`
- 从这个角度看，五条主路线其实分别对应五种不同的“效率瓶颈诊断”。

### 2. `model-and-representation efficiency`
- 它在解决什么问题：
  - 不把“大底座先搭好，再事后加速”当成默认前提，而是直接重写 policy substrate 本身，让 VLA 更小、更稀、更低比特，或者让动作表示本身更利于优化。
- 为什么重要：
  - 这是最底层的效率路线。若底座本身过重，后续 pruning、cache、async 或部署技巧的收益都会被上限卡住。
  - 它决定的是“VLA 从一开始是不是一个可承受的对象”，而不只是“一个昂贵对象能否被补救”。
- 代表性工作：
  - `compact / small VLA design`：[[wiki/papers/2409_12514_TinyVLA.md|TinyVLA]]、[[wiki/papers/2506_01844_SmolVLA.md|SmolVLA]]、[[wiki/papers/2507_14049_EdgeVLA.md|EdgeVLA]]
  - `efficient architecture replacement`：[[wiki/papers/2406_04339_RoboMamba.md|RoboMamba]]
  - `action representation / tokenizer / codec`：[[wiki/papers/2501_09747_FAST.md|FAST]]、[[wiki/papers/2602_15397_ActionCodec.md|ActionCodec]]
  - `low-bit / quantized substrate`：[[wiki/papers/2602_20309_QuantVLA.md|QuantVLA]]
- 这类工作的共同点：
  - 它们压的不是“某一步 runtime 冗余”，而是**模型和表示层的基本形态**。
  - `TinyVLA / SmolVLA / EdgeVLA` 把小模型、低延迟、弱硬件部署当成一等目标。
  - `FAST / ActionCodec` 把动作 tokenization 从“重建问题”改写成“VLA 优化接口”问题。
  - `QuantVLA` 则把部署瓶颈直接下沉到低比特可行性，说明“可量化”本身是 substrate 设计的一部分。
- 和相邻路线的边界：
  - 它不同于 `training-and-adaptation efficiency`，因为这里关注的是**模型/表示本体是否高效**，而不是“同一个模型如何更便宜地学出来”。
  - 它也不同于 `deployment-oriented efficiency`，因为小模型或低比特是模型层设计；而 deployment 关注的是这些设计在真实系统里是否成立。

### 3. `training-and-adaptation efficiency`
- 它在解决什么问题：
  - 如何更便宜地得到一个可用 VLA，而不是默认接受高昂训练步数、GPU 小时、数据量或 teacher 成本。
- 为什么重要：
  - 如果训练成本本身不可承受，Efficient VLA 就只能停留在少数大团队的能力范围内。
  - 这条路线把“谁能做 VLA、能多快迭代 VLA”变成了效率问题，而不是纯粹资源问题。
- 代表性工作：
  - `tokenization-driven training efficiency`：[[wiki/papers/2501_09747_FAST.md|FAST]]
  - `teacher / action-expert distillation`：[[wiki/papers/2510_09607_VITA-VLA.md|VITA-VLA]]、[[wiki/papers/2511_18082_ActDistill.md|ActDistill]]
  - `data-centric efficiency`：[[wiki/papers/2511_16233_FT-NCFM.md|FT-NCFM]]
  - `train-to-infer bridge`：[[wiki/papers/2603_25661_Fast-dVLA.md|Fast-dVLA]]
- 这类工作的共同点：
  - `FAST` 通过动作压缩降低训练 steps / GPU hours，本质上是在提高 token efficiency。
  - `VITA-VLA / ActDistill` 把 expensive teacher 或 action expert 的知识转成更廉价的 student 适配过程。
  - `FT-NCFM` 更激进，它不先压模型，而是直接把“训练数据冗余”视为根因，在 data layer 生成高信息密度 synthetic coreset。
- 和相邻路线的边界：
  - 训练效率不等于推理更快。更少 GPU 小时、更多数据效率，不应直接改写成 runtime acceleration。
  - 这条路线和 `model-and-representation efficiency` 联系很紧，因为 tokenizer 或表示重写经常同时影响训练和模型本体。
  - 但分类时仍应看 headline 主问题是否是 `training steps / GPU hours / data ratio / adaptation cost`。

### 4. `inference-time compute allocation`
- 它在解决什么问题：
  - 当底座已经固定后，如何只在真正必要的位置花计算，把单步控制成本压下来。
- 为什么重要：
  - 这是当前最显性的 Efficient VLA 主战场，因为它直接回应“现有 VLA 太慢、太贵、每一步都算过头”的现实痛点。
  - 它让研究重心从“把模型做小”转向“让已有模型少做无效计算”。
- 代表性工作：
  - `cache-and-reuse`：[[wiki/papers/2502_02175_VLA-Cache.md|VLA-Cache]]
  - `pruning-and-selection`：[[wiki/papers/2505_21200_FlashVLA.md|FlashVLA]]、[[wiki/papers/2509_05614_SpecPrune-VLA.md|SpecPrune-VLA]]、[[wiki/papers/2511_16449_VLA-Pruner.md|VLA-Pruner]]、[[wiki/papers/2603_22991_VLA-IAP.md|VLA-IAP]]、[[wiki/papers/2603_25766_ETA-VLA.md|ETA-VLA]]
  - `sampling / decoding compression`：[[wiki/papers/2603_25661_Fast-dVLA.md|Fast-dVLA]]、[[wiki/papers/2604_05656_SnapFlow.md|SnapFlow]]、[[wiki/papers/2604_01567_AnchorVLA.md|AnchorVLA]]
  - `async / streaming / chunk scheduling`：[[wiki/papers/2511_14148_AsyncVLA.md|AsyncVLA]]、[[wiki/papers/2602_01100_StreamVLA.md|StreamVLA]]、[[wiki/papers/2603_28565_StreamingVLA.md|StreamingVLA]]、[[wiki/papers/2604_04161_AAC.md|AAC]]
- 这类工作的共同点：
  - 它们默认底座基本不变，关键是**重新分配推理预算**。
  - `VLA-Cache` 强调跨帧复用，说明不是所有计算都值得每帧重做。
  - `FlashVLA / SpecPrune-VLA / ETA-VLA` 一路说明 pruning 议程已从单纯 semantic saliency，转向更 action-aware、interaction-aware、phase-aware 的预算分配。
  - `Fast-dVLA / SnapFlow / AnchorVLA` 则把问题转成 action decoding / diffusion sampling 的步数与调度设计。
  - `AsyncVLA / StreamVLA / StreamingVLA` 进一步说明“何时算、算多久、和控制节奏如何对齐”本身就是 compute allocation 问题。
- 和相邻路线的边界：
  - 它不同于 `model-and-representation efficiency`，因为这里通常默认底座不被根本重写。
  - 它又不同于 `deployment-oriented efficiency`，因为 inference route 主要关心方法上如何省算，而 deployment route 关心这些收益在系统层是否仍然成立。

### 5. `reasoning efficiency`
- 它在解决什么问题：
  - 如何保留 planning、self-correction、few-shot adaptation 等 reasoning 收益，同时避免 always-on 显式 CoT 带来的执行延迟与控制开销。
- 为什么重要：
  - 许多高能力 VLA 收益来自“会想”，但真实机器人又很难承受持续 verbal reasoning。
  - 因此，reasoning efficiency 回答的是：VLA 是否能既保留 deliberation，又不被 deliberation 拖慢。
- 代表性工作：
  - `explicit reasoning cost compression`：[[wiki/papers/2505_08243_ECoT-Lite.md|ECoT-Lite]]
  - `dual-system reasoning-action split`：[[wiki/papers/2507_16815_ThinkAct.md|ThinkAct]]
  - `latent planning / compact reasoning substrate`：[[wiki/papers/2601_09708_Fast-ThinkAct.md|Fast-ThinkAct]]、[[wiki/papers/2602_01166_LaRA-VLA.md|LaRA-VLA]]
  - `gated / routed reasoning`：[[wiki/papers/2602_01100_StreamVLA.md|StreamVLA]]、[[wiki/papers/2603_05147_ActThinkAbstain.md|ActThinkAbstain]]
- 这类工作的共同点：
  - `ECoT-Lite` 说明 reasoning gain 不一定非要在测试时完整生成出来，收益可以通过更轻训练配方保留下来。
  - `ThinkAct` 把 planning system 和 action system 结构性拆开，避免每一步都付 reasoning 成本。
  - `Fast-ThinkAct / LaRA-VLA` 把显式思维压到 latent substrate。
  - `StreamVLA / ActThinkAbstain` 则继续推进到“只在需要时才想”。
- 和相邻路线的边界：
  - 它和 `inference-time compute allocation` 都属于 runtime efficiency，但前者主要压的是**感知/动作推理链路的计算冗余**，后者压的是**reasoning substrate 本身的额外开销**。
  - 一篇工作若只是更快，但没有显式 reasoning substrate 或 reasoning policy，就不应算入 reasoning efficiency 主链。

### 6. `deployment-oriented efficiency`
- 它在解决什么问题：
  - 如何让前面这些效率收益在真实硬件、网络、控制周期、冷启动和 jitter 约束下仍然成立。
- 为什么重要：
  - 这是把“实验室里的效率”变成“系统里的可用性”的最后一道关。
  - 很多论文的 headline latency 或 frequency 在真实系统里未必成立，因为 placement、显存上限、网络波动、pipeline 切分都会改变结果。
- 代表性工作：
  - `edge-native model design`：[[wiki/papers/2507_14049_EdgeVLA.md|EdgeVLA]]、[[wiki/papers/2603_03380_LiteVLA-Edge.md|LiteVLA-Edge]]
  - `representation-for-throughput`：[[wiki/papers/2507_05116_VOTE.md|VOTE]]
  - `system throughput tuning`：[[wiki/papers/2603_26360_Realtime-VLA-V2.md|Realtime-VLA V2]]
  - `real-time serving / async deployment`：[[wiki/papers/2512_03044_Video2Act.md|Video2Act]]、[[wiki/papers/2603_19199_FASTER.md|FASTER]]
  - `system / placement analysis`：[[wiki/papers/2602_18397_VLA-Perf.md|VLA-Perf]]
- 这类工作的共同点：
  - `EdgeVLA` 说明边缘部署不是事后考虑，而是可以直接嵌入模型和动作头设计。
  - `VOTE` 说明输出表示本身也可以为了 edge throughput 而设计。
  - `Realtime-VLA V2`、`Video2Act`、`FASTER` 把“真正能在闭环里反应过来”作为主要目标，而不是只报告 benchmark latency。
  - `VLA-Perf` 则进一步把部署问题提升为系统分析对象，提醒我们 placement、network 和 async pipeline 不是附录细节，而是效率定义的一部分。
- 和相邻路线的边界：
  - 它不是简单的“又一种加速方法”，而更像是对前几类工作的**系统真实性过滤器**。
  - 一篇工作只有在 deployability 本身是主问题时，才应进入 deployment 主链；否则最多提供边界说明。

### 7. 五类之间最重要的边界
- 最核心的边界不是“技术长得像不像”，而是“主 headline 压的是哪层成本”。
- 当前最容易混写的跨界点有三类：
  - `tokenization`
    - 既可能属于 `model-and-representation efficiency`，因为它重写了 action interface；
    - 也可能属于 `training-and-adaptation efficiency`，因为它直接改变训练成本。
  - `quantization`
    - 既可能属于 `model-and-representation efficiency`，因为它重塑 substrate；
    - 也可能服务 `deployment-oriented efficiency`，因为它直接影响显存与设备可部署性。
  - `async / streaming`
    - 既可能属于 `inference-time compute allocation`，因为它在 runtime 重新调度计算；
    - 也可能属于 `deployment-oriented efficiency`，因为它最终解决的是闭环控制和系统周期问题。
- 因此，面对跨界论文，更稳妥的做法不是多重归类，而是问：
  - 这篇工作的首要瓶颈是什么？
  - 它的主收益落在哪一层？
  - 它的 headline 最需要和哪类 cost metric 一起读？

### 8. 五类之间最重要的联系
- `model-and-representation efficiency` 往往决定后续一切优化的上限，是底层供给侧路线。
- `training-and-adaptation efficiency` 决定这个底座能否被便宜地得到，是供给侧的另一半。
- `inference-time compute allocation` 决定部署前的单步 runtime 成本，是最直接的在线效率路线。
- `reasoning efficiency` 是 runtime 路线里更高层的一支，专门处理 deliberation overhead。
- `deployment-oriented efficiency` 则负责检验上述收益是否能穿透到真实系统。
- 所以，一个更成熟的 Efficient VLA 工作往往不会只落在一层：
  - `FAST` 同时连接表示层与训练层；
  - `Fast-dVLA` 同时连接训练适配与解码加速；
  - `SmolVLA / EdgeVLA` 同时连接小模型设计与部署导向；
  - `StreamVLA` 同时连接 reasoning routing 与 streaming control。
- 这说明 Efficient VLA 正在从“单点优化”走向“多层联动设计”。

### 9. 从综述视角看，这个领域当前最清楚的总体趋势
- 趋势一：从“更小更快”的粗口号，走向**按成本层分治**的清晰议程。
- 趋势二：从“静态压缩”走向“按任务阶段动态分配计算”。
- 趋势三：从“只看 benchmark latency”走向“把 deployability、jitter、placement 也算进效率”。
- 趋势四：从“reasoning 越多越好”走向“reasoning 只在必要时触发”。
- 趋势五：从“压模型参数”扩展到“压数据、压训练、压动作表示、压系统调度”的全链路效率观。

### 10. 如果只想用最短路径建立全局认知，建议这样读
- 先读 [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]
  - 作用：先把“效率到底在比较什么”这件事固定住。
- 再读 [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
  - 作用：快速获得 `3` 个宏观家族、`5` 条主路线的总图。
- 然后按兴趣分支深入：
  - 若关心“已有模型怎么加速”：先读 [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
  - 若关心“如何更便宜训练出 VLA”：先读 [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
  - 若关心“thinking 值不值、怎么更便宜地想”：先读 [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
  - 若关心“能不能真上边缘设备或真实系统”：先读 [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]

## Related Wiki Pages
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/evidence/metrics/runtime-vs-task-metrics.md|runtime-vs-task-metrics]]
- [[wiki/evidence/metrics/training-cost-vs-performance.md|training-cost-vs-performance]]
- [[wiki/evidence/wording/training-free-vs-no-retraining.md|training-free-vs-no-retraining]]
- [[wiki/evidence/wording/model-agnostic-vs-validated-compatibility.md|model-agnostic-vs-validated-compatibility]]

## Evidence Notes
- 当前全景分类最主要依赖 `wiki/synthesis/*` 的跨论文建模，而不是某一篇论文的单独 headline。
- 两条最重要的口径边界是：
  - `runtime / latency / frequency` 不能和 `task performance` 混写；
  - `training cost / data ratio / adaptation cost` 不能和 `inference speedup` 混写。
- 因此，任何“更高效”的结论都必须补一句：它究竟是在压哪一层成本。
- 当前 thread 刻意不做路线优劣排序，因为不同路线压的是不同层成本，很多结果本来就不可直接比较。

## Open Uncertainties
- `model-and-representation efficiency` 目前在仓库里已经足够稳定到可作为主路线，但还缺一页独立 `synthesis` 子主题页；当前主要由总地图页兼任。
- `energy`、`memory ceiling`、`network variability`、`closed-loop failure mode` 还没有完全被统一进一套跨论文共享的效率语言。
- 多数论文仍以单层优化为主，真正同时显式建模 `model / training / runtime / reasoning / deployment` 五层 tradeoff 的工作还不多。
- 一些跨界路线如 `tokenization`、`quantization`、`async` 仍需要持续防止被写成“独立于上下文的统一大类”。

## Update Log
- `2026-04-22`：新建本 thread。基于现有 `wiki/synthesis` 与代表性 `papers` 页面，整理出面向综述写作的 Efficient VLA 全景地图，明确 `3` 个宏观家族、`5` 条主路线，以及各路线的边界与联系。
