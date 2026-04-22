# q0003-vla-token-pruning-landscape

## Canonical Question
- 当前 VLA 中与 token 剪枝相关的工作已经有哪些代表性方法？
- 它们各自的核心思路、适用场景与边界是什么？
- 与传统 VLM token pruning 相比，VLA 场景的问题特殊性在哪里？
- 现有方法还存在哪些不足，未来最值得继续推进的方向是什么？

## Scope
- 本文聚焦 **VLA 中与 visual token pruning / token selection / token sparsification 直接相关** 的路线，不把所有推理加速方法都纳入同一主线。
- 但为了说明边界，会有选择地提到几类相邻工作：
  - `token caching / reuse`：如 [[wiki/papers/2502_02175_VLA-Cache.md|VLA-Cache]]
  - `holistic acceleration`：如 [[wiki/papers/2506_10100_EfficientVLA.md|EfficientVLA]]
  - `attention correction / post-pruning recovery / embodied evaluation`：如 [[wiki/papers/2601_16065_DTP.md|DTP]]、[[wiki/papers/2510_08464_GLUESTICK.md|GLUESTICK]]、[[wiki/papers/2603_19131_EmbodiedEff.md|EmbodiedEff]]
- 这份 thread 主要基于当前 `wiki` 的已有论文页与子主题页，目标是梳理**路线图、边界和演化逻辑**，而不是做单一 benchmark 排行榜。

## Current Answer
- 当前 VLA token 剪枝方向已经从早期的 **semantic-only / perception-first visual token pruning**，演化成更明确的 **embodiment-aware compute allocation** 议程。
- 如果用更稳定的综述视角来归纳，这条方向目前大致可以分成 `5` 类主路线：
  - `static or perception-first pruning`
  - `action-aware / phase-aware dynamic pruning`
  - `interaction-first / structure-aware pruning`
  - `multi-view / temporal / multi-modal pruning`
  - `training-based differentiable / semantic-aligned pruning`
- 代表性方法可以按这条线看：
  - `early perception-first`：[[wiki/papers/2505_21200_FlashVLA.md|FlashVLA]]、[[wiki/papers/2509_05614_SpecPrune-VLA.md|SpecPrune-VLA]]
  - `action/phase-aware`：[[wiki/papers/2509_22093_ADP.md|ADP]]、[[wiki/papers/2511_16449_VLA-Pruner.md|VLA-Pruner]]
  - `interaction-first / structure-aware`：[[wiki/papers/2603_22991_VLA-IAP.md|VLA-IAP]]
  - `embodiment-guided query`：[[wiki/papers/2602_06575_ThinkProprio.md|ThinkProprio]]
  - `multi-view / multi-modal`：[[wiki/papers/2602_20566_BFApp.md|BFApp]]、[[wiki/papers/2603_25766_ETA-VLA.md|ETA-VLA]]、[[wiki/papers/2604_09244_Tri-Stage-Token-Pruning-Framework.md|Tri-Stage Token Pruning Framework]]
  - `differentiable / learned`：[[wiki/papers/2509_12594_LightVLA.md|LightVLA]]、[[wiki/papers/2511_10518_SemanticVLA.md|SemanticVLA]]
- 这条方向与传统 VLM token pruning 的最大区别是：VLA 的 token 重要性不只由“当前图像是否语义显著”决定，还受 **动作生成、操控阶段、物理交互、机器人状态、视角布局、历史记忆与闭环执行** 共同影响。
- 因而，VLA 剪枝的真正核心问题已经不是“怎么把 token 变少”，而是“**在 embodied control 中，哪些 token 在哪个时刻、对哪一类动作决策真正关键**”。

## Structured Notes

### 1. 这条方向的总体演化
- 如果从路线演化看，VLA token 剪枝已经出现一个很清楚的转向：
  - 最早的问题是：`VLA 太慢，视觉 token 太多，能不能像 VLM 一样删掉一部分？`
  - 后来的问题变成：`哪些 token 对动作真正关键，删错的代价为何比 VLM 更大？`
  - 再往后，问题又变成：`token 重要性会不会随 manipulation phase、视角、历史、甚至 proprioception 一起动态变化？`
- 因此，当前最稳的主线不是按“论文先后顺序”看，而是按 pruning signal 的增强来理解：
  - `semantic-only`
  - `action-aware`
  - `phase-aware`
  - `interaction-first`
  - `multi-view / multi-modal-aware`
  - `performance-driven differentiable`

### 2. 第一类：`static or perception-first pruning`

#### 2.1 `FlashVLA`
- 核心思路：
  - 认为 VLA 推理里同时存在 `action-level redundancy` 和 `token-level redundancy`，因此一边做动作复用，一边做视觉 token 剪枝。
  - 视觉 token 侧主要依赖 `information contribution score (ICS)` 与 SVD 选择重要 token。
- 适用场景：
  - 更像 `OpenVLA` 这类单视角、manipulation、training-free inference acceleration。
- 它代表什么阶段：
  - 它仍然属于较早的 `perception-first / information-guided` 路线，主要还在回答“哪些视觉 token 看起来更重要”。
- 价值：
  - 证明 VLA 上的 pruning 确实能获得可观效率收益，而不必一开始就重训练整个模型。
- 局限：
  - `55.7%` 降的是 visual-token FLOPs，不是端到端全系统 FLOPs。
  - 更重要的是，它对 “哪些 token 对动作精细控制关键” 的建模还比较弱，更多停留在 perception saliency。

#### 2.2 `SpecPrune-VLA`
- 核心思路：
  - 用一个 `two-level pruning recipe` 结合 `global history reuse`、`local token importance` 与 `action-aware controller`。
  - 比早期方法多走了一步：不只看当前帧，还把更长时域 history 拉进 pruning 决策。
- 适用场景：
  - `compute-bound single-step VLA inference`，尤其是 `OpenVLA-OFT / π0` 这类需要在有限 wall-clock budget 下做单步决策的 setting。
- 价值：
  - 它开始明确指出：单看当前步的 token 重要性不够，机器人控制需要全局 temporal structure。
- 局限：
  - 依然偏 heuristic/controller-heavy。
  - 文中多组 speedup 数字来自不同硬件、不同 baseline、不同口径，说明这一类方法还缺统一比较协议。

### 3. 第二类：`action-aware / phase-aware dynamic pruning`

#### 3.1 `ADP`
- 核心思路：
  - 把 pruning 明确写成一个 **action-aware、phase-dependent** 问题。
  - 用 `Text-driven Anticipatory Pruning` 先筛 task-relevant token，再用近期 end-effector trajectory 决定当前 step 应该剪还是回到 full vision。
- 适用场景：
  - manipulation 尤其合适，因为它天然有粗到细的动作阶段变化。
- 价值：
  - 它很清楚地把一个 VLA 特有事实说透了：**冗余不是固定的，而是和操作阶段一起变**。
  - coarse motion 阶段可以更 aggressive，delicate manipulation 阶段则要更保守。
- 局限：
  - 这种 phase structure 在 manipulation 上很自然，但推广到 driving、navigation 或非抓取类任务时不一定同样成立。
  - 目前很多收益仍建立在 OpenVLA-OFT 风格实现与固定窗口规则上。

#### 3.2 `VLA-Pruner`
- 核心思路：
  - 直接批评把 VLM 里的 `semantic-only pruning` 迁移到 VLA 上会失效。
  - 关键不是只看 prefill attention，而是同时看 `vision-language prefill attention`、`action decode attention` 和 `temporal continuity`。
- 适用场景：
  - 当前最适合作为 manipulation VLA token pruning 主线代表作之一，尤其是 `OpenVLA / OpenVLA-OFT / π0` 这类带 action-to-vision 关系的模型。
- 价值：
  - 它把 VLA token pruning 与传统 VLM pruning 的差别说得最明确：
    - VLA 不只是做语义理解；
    - 它还要做低层动作执行；
    - 所以 token 重要性必须同时对 semantic understanding 和 action execution 负责。
- 局限：
  - 虽然它已经走向 dual-system-aware，但主线仍是 training-free heuristic。
  - cross-architecture 证据虽有，但 strongest evidence 还是集中在少数 backbone。

### 4. 第三类：`interaction-first / structure-aware pruning`

#### `VLA-IAP`
- 核心思路：
  - 把既有方法概括为 `Perception-First` 偏置，认为它们容易过早删掉视觉上不显眼、但对物理操作关键的结构性区域。
  - 为此引入 `Geometric Prior` 和 `Interaction-Aligned Dynamic Strategy`，通过几何结构与 semantic-motion IoU 来决定 conservative 还是 aggressive pruning。
- 适用场景：
  - manipulation，特别是需要依赖结构边缘、接触点、相对几何关系的场景。
- 价值：
  - 这类工作把 pruning 从“图像过滤问题”改写成了“交互对齐问题”。
  - 它说明 VLA 中很多关键 token 并不一定最显眼，但在即将接触、对齐、插入、抓取时极其关键。
- 局限：
  - 很多收益仍与特定 retention ratio、特定 backbone、特定 benchmark 绑定。
  - `interaction-first` 很强，但当前仍多靠手工几何先验与规则化门控，而不是统一可学习策略。

### 5. 第四类：`multi-view / temporal / multi-modal pruning`

#### 5.1 `BFApp`
- 核心思路：
  - 多视角 VLA 不能再按单视角 saliency 做剪枝，而要拆成：
    - `Intra-view Importance`
    - `Inter-view Importance`
  - 先做视角内 task-relevant 筛选，再做跨视角全局 hierarchical pruning。
- 适用场景：
  - multi-view manipulation。
- 价值：
  - 它说明 VLA 中“同一个 token 重要不重要”不仅取决于内容本身，还取决于**这个信息来自哪个相机视角、当前阶段这个视角值不值得保留**。
- 局限：
  - 当前 strongest evidence 集中在 `π0 / RDT` 的 multi-view setting。
  - 它更像专门为 multi-view 写的 pruning 框架，不宜直接泛化为所有 VLA 通用 recipe。

#### 5.2 `ETA-VLA`
- 核心思路：
  - 面向 driving VLA，同时压缩：
    - 进入 LLM 前的多帧多视角历史
    - LLM 内部的视觉 token
  - 即 `Temporal Fusion Module + Intra-LLM Sparse Aggregator`
- 适用场景：
  - driving VLA，尤其是长历史、多视角输入导致 token bloat 的 setting。
- 价值：
  - 它把 VLA pruning 从 manipulation 单帧问题推进到了**时空历史压缩**问题。
  - 也提示我们：在 driving / navigation 中，真正的冗余往往不是单帧视觉 patch，而是冗长 history 的重复语义。
- 局限：
  - 当前 strongest evidence 仍集中在 `NAVSIM v2` driving，不宜直接外推到 manipulation。

#### 5.3 `Tri-Stage Token Pruning Framework`
- 核心思路：
  - 当输入从 2D-only 变成 2D+3D multi-visual-modal 后，不同模态在不同阶段的重要性不一样。
  - 因而把 token pruning 显式拆成 `data preprocessing`、`semantic synthesis`、`action iteration` 三阶段。
- 适用场景：
  - MVLA，尤其是 2D / 3D 混合输入。
- 价值：
  - 它把这条线继续推向 modality-aware compute allocation，而不是单纯继续优化单视角 RGB token selection。
- 局限：
  - strongest evidence 还是 MVLA / RLBench setting，对 2D-only VLA 的统一改进尚不能直接声称。

#### 5.4 `ThinkProprio`
- 核心思路：
  - 不是纯视觉 saliency，而是让 `instruction + proprioception` 一起当 query 去引导 token retention。
- 适用场景：
  - 机器人状态对视觉判断很关键的任务，特别是 manipulation。
- 价值：
  - 它代表一种很重要的转向：VLA 的 token 选择不该只由视觉和文本决定，**机器人自身状态也应更早进入 pruning 决策**。
- 局限：
  - 它既像 pruning 论文，也像 proprio integration 论文，路线边界相对混合。

### 6. 第五类：`training-based differentiable / semantic-aligned pruning`

#### 6.1 `LightVLA`
- 核心思路：
  - 把 token pruning 从启发式、固定保留比例，改成 **performance-driven differentiable pruning**。
  - 用 dynamic query + Gumbel-softmax 做可微 token selection。
- 适用场景：
  - 更适合有 finetuning 预算、希望把 pruning 行为直接学出来的 setting。
- 价值：
  - 它很重要，因为它把 VLA token pruning 的目标从“尽量少掉点”改成“**让任务表现自己决定该保留谁**”。
  - 这条线比纯 heuristic 更像长期可扩展方向。
- 局限：
  - 它不再是 training-free。
  - 当前 strongest evidence 仍主要集中在 `OpenVLA-OFT + LIBERO`。

#### 6.2 `SemanticVLA`
- 核心思路：
  - 不只做视觉稀疏化，还把：
    - semantic-aligned pruning
    - 跨视觉骨干的层级融合
    - semantic-conditioned action coupling
    合在一起。
- 适用场景：
  - manipulation，尤其是希望把语义 grounding 与效率一起提升的 setting。
- 价值：
  - 它代表更激进的一类思路：不是把 pruning 当后处理插件，而是把“semantic alignment + sparsification + action coupling”写进统一高效架构。
- 局限：
  - 它已经不再是纯粹的 token pruning paper，而更像 efficient VLA redesign。
  - 因此它适合被当作“pruning 走向 semantic-aligned architecture co-design”的信号，而不是单独与 training-free 方法简单并比。

### 7. 与传统 VLM token pruning 的关键区别
- 传统 VLM token pruning 通常默认：
  - 任务是静态图像理解或多模态问答；
  - token 重要性主要由语义显著性、文本相关性、attention score、similarity/diversity 决定；
  - 评价重点是回答准确率、VQA 分数、prefill latency、FLOPs。
- 从当前 VLA 论文反复提出的批评看，可以稳定归纳出一个对比：
  - `VLM pruning` 更像 **single-pass semantic filtering**
  - `VLA pruning` 更像 **closed-loop embodied compute allocation**
- 具体差异主要有六点：
  - `动作耦合`
    - VLA token 重要性必须对 action execution 负责，而不只是对视觉理解负责。
  - `阶段性`
    - manipulation 的 coarse / fine phase 对 token 需求不同，静态 ratio 往往不够。
  - `时间性`
    - 当前 token 是否重要，常和近期动作窗口、历史观测、未来接触状态有关。
  - `视角性`
    - 多相机场景下，不同 view 在不同阶段的重要性不同。
  - `具身状态`
    - proprioception、末端执行器状态、动作轨迹都可能改变视觉 token 的价值。
  - `闭环代价`
    - VLM pruning 只要不掉答题准确率即可；VLA pruning 删错 token 可能带来接触失败、轨迹抖动、绕路、动作延迟，代价更连续也更难补救。
- 更直接地说：
  - 在 VLM 里，“看哪里”往往接近“答题需要哪里”；
  - 在 VLA 里，“看哪里”未必等于“动作真正依赖哪里”。

### 8. VLA 场景下问题的特殊性
- 当前语料已经比较稳定地暴露出五个 VLA 特有难点：
  - `semantic saliency 不够`
    - 视觉上不起眼的结构边缘、接触区域、夹爪附近 token，可能对操控最关键。
  - `prefill attention 不够`
    - 只看 VLM prefill 阶段，不足以判断 action decode 时真正关键的信息。
  - `重要性是动态的`
    - token 价值会随 manipulation phase、视角切换、历史推进而改变。
  - `输入结构更复杂`
    - 多视角、长历史、2D+3D、proprioception 都会把 token 选择问题从单一排序变成结构化调度问题。
  - `评估更苛刻`
    - 同样的 success rate 下，completion time、smoothness、jerk、path length 可能已经变差；这正是 [[wiki/papers/2603_19131_EmbodiedEff.md|EmbodiedEff]] 想提醒的边界。

### 9. 当前方法的主要不足
- `一类方法只在少数 backbone 上证实`
  - 很多工作 strongest evidence 仍集中在 `OpenVLA / OpenVLA-OFT`，或少数 `π / CogACT` setting。
- `训练免费方法仍 heavily heuristic`
  - 很多 action-aware / interaction-aware 方法仍依赖 hand-crafted controller、阈值、ratio schedule 或 geometric heuristics。
- `跨 benchmark 不可直接比较`
  - speedup、latency、FLOPs、retention ratio、success rate 常常不在同一 operating point。
- `很多方法只处理视觉 token`
  - 但 VLA 的真实瓶颈往往同时分布在语言层、视觉 token、action head、sampling schedule 上。
- `真实机器人证据仍偏少`
  - 不少方法在 simulation 上很好，但 real-world 证据仍窄。
- `缺少统一 embodied-aware 评估协议`
  - 现有论文多看 speedup + success rate，较少系统纳入 completion time、smoothness、failure mode。
- `overhead 问题未完全解决`
  - 动态选择、controller、importance predictor、额外 scoring 本身也会吃掉一部分收益。

### 10. 最值得继续推进的方向

#### 10.1 从 `semantic saliency` 继续走向 `action-grounded token value`
- 当前最值得推进的，不是更复杂的注意力打分，而是更直接地把 token 价值与 action quality、contact success、future state relevance 绑定。
- 这也是 `VLA-Pruner`、`ADP`、`VLA-IAP` 共同指向的方向。

#### 10.2 从单模态 pruning 走向 `embodiment-aware multimodal compute allocation`
- 最有潜力的下一步不是只剪 RGB token，而是联合建模：
  - RGB / depth / 3D
  - multi-view
  - proprioception
  - history memory
  - action head state

#### 10.3 从 heuristic training-free 走向 `learned pruning policy`
- `LightVLA` 已经展示了 differentiable pruning 的价值。
- 更长期看，可能需要把 pruning 从 rule-based controller 发展成可泛化的 learned compute policy。

#### 10.4 从单点剪枝走向 `与 cache / quantization / routing / sampling 的协同设计`
- 现实里最强收益未必来自单独 pruning。
- 更可能的方向是：
  - pruning + cache reuse
  - pruning + quantization
  - pruning + layer routing
  - pruning + action decoding compression
- 当前 [[wiki/papers/2509_09090_SQAP-VLA.md|SQAP-VLA]]、[[wiki/papers/2506_10100_EfficientVLA.md|EfficientVLA]] 已经开始显露这种 co-design 趋势。

#### 10.5 从 `success-rate preservation` 走向 `embodied efficiency optimization`
- 未来最值得推进的，不是只回答“剪了以后 success 掉没掉”，而是同时回答：
  - completion time 变了吗？
  - smoothness 变了吗？
  - failure mode 有无恶化？
  - safety margin 有无缩小？
- 不然 token pruning 很容易在 paper 指标上高效，在真实机器人上却变得更脆弱。

### 11. 哪些工作更像“边界补充”而不是主线方法
- [[wiki/papers/2601_16065_DTP.md|DTP]]
  - 更像 attention correction / performance upper bound exploration，不是标准 latency-oriented pruning。
- [[wiki/papers/2510_08464_GLUESTICK.md|GLUESTICK]]
  - 更像 post-pruning recovery，说明 “VLA pruning 后会坏得比 LLM/VLM 更严重”。
- [[wiki/papers/2603_19131_EmbodiedEff.md|EmbodiedEff]]
  - 更像评估框架重构，提醒 token sparsification 不能只看 inference 指标。
- 这些工作虽不是 pruning 主线方法，但它们对理解“VLA 为何难剪、剪完如何评、剪坏后怎么补”很关键。

### 12. 如果只想快速建立这条方向的阅读顺序
- 先读：
  - [[wiki/evidence/wording/semantic-only-vs-embodiment-aware-pruning.md|semantic-only-vs-embodiment-aware-pruning]]
  - 作用：先固定 “为什么 VLM-style semantic-only pruning 不够”。
- 再读三篇主线代表：
  - [[wiki/papers/2511_16449_VLA-Pruner.md|VLA-Pruner]]
  - [[wiki/papers/2509_22093_ADP.md|ADP]]
  - [[wiki/papers/2603_22991_VLA-IAP.md|VLA-IAP]]
  - 作用：把 `action-aware`、`phase-aware`、`interaction-first` 三个核心转向读清楚。
- 然后按兴趣分支：
  - 多视角 / 多模态：[[wiki/papers/2602_20566_BFApp.md|BFApp]]、[[wiki/papers/2604_09244_Tri-Stage-Token-Pruning-Framework.md|Tri-Stage Token Pruning Framework]]
  - 可微学习：[[wiki/papers/2509_12594_LightVLA.md|LightVLA]]
  - 具身状态引导：[[wiki/papers/2602_06575_ThinkProprio.md|ThinkProprio]]
  - 评估边界：[[wiki/papers/2603_19131_EmbodiedEff.md|EmbodiedEff]]

## Related Wiki Pages
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/evidence/wording/semantic-only-vs-embodiment-aware-pruning.md|semantic-only-vs-embodiment-aware-pruning]]
- [[wiki/evidence/metrics/retention-ratio-vs-speed-performance.md|retention-ratio-vs-speed-performance]]
- [[wiki/papers/2505_21200_FlashVLA.md|2505_21200_FlashVLA]]
- [[wiki/papers/2509_05614_SpecPrune-VLA.md|2509_05614_SpecPrune-VLA]]
- [[wiki/papers/2509_22093_ADP.md|2509_22093_ADP]]
- [[wiki/papers/2511_16449_VLA-Pruner.md|2511_16449_VLA-Pruner]]
- [[wiki/papers/2603_22991_VLA-IAP.md|2603_22991_VLA-IAP]]
- [[wiki/papers/2602_20566_BFApp.md|2602_20566_BFApp]]
- [[wiki/papers/2603_25766_ETA-VLA.md|2603_25766_ETA-VLA]]
- [[wiki/papers/2604_09244_Tri-Stage-Token-Pruning-Framework.md|2604_09244_Tri-Stage-Token-Pruning-Framework]]
- [[wiki/papers/2509_12594_LightVLA.md|2509_12594_LightVLA]]
- [[wiki/papers/2511_10518_SemanticVLA.md|2511_10518_SemanticVLA]]
- [[wiki/papers/2602_06575_ThinkProprio.md|2602_06575_ThinkProprio]]
- [[wiki/papers/2601_16065_DTP.md|2601_16065_DTP]]
- [[wiki/papers/2510_08464_GLUESTICK.md|2510_08464_GLUESTICK]]
- [[wiki/papers/2603_19131_EmbodiedEff.md|2603_19131_EmbodiedEff]]

## Evidence Notes
- 当前最稳定的共识不是“哪篇方法最好”，而是：
  - `semantic-only pruning` 对 VLA 不够；
  - pruning signal 需要越来越多地吸收 action、phase、interaction、embodiment、view、history 信息。
- 当前不同论文的 `speedup / latency / FLOPs / pruning ratio / success rate` 常常不在同一 operating point，不能压成单一排行榜。
- 当前 thread 刻意把 `DTP / GLUESTICK / EmbodiedEff` 放在边界层，而不是和主线 pruning 方法混成一类。

## Open Uncertainties
- 当前仓库里虽然已经能看到一条清晰主线，但还缺一个正式的 `wiki/synthesis` 级 token pruning 专题页；目前相关结论仍分散在 `inference-efficiency-routes` 与单篇页里。
- 很多方法 strongest evidence 仍局限在 `OpenVLA-OFT` 或少数 manipulation benchmark；跨架构、跨任务、跨模态的统一证据仍不够。
- 训练免费和可学习 pruning 之间，目前还没有出现一个同时兼顾强泛化、低开销和高稳定性的统一方案。

## Update Log
- `2026-04-22`：新建本 thread。基于现有 `wiki` 梳理 VLA token pruning 路线、代表方法、VLM 对比、VLA 特殊性、当前不足与未来方向，形成一份面向综述写作的 token pruning landscape 笔记。
