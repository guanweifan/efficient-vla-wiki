# q0002-vla-baselines-recent

## Canonical Question
- 当前常用的 Efficient VLA baseline 都有哪些？
- 它们分别属于什么类型，在当前语料中的使用分布如何，各自的优缺点是什么？
- 如果要选择一个合适的开源 baseline 作为后续修改和实验的 code base，应该重点考虑哪些因素？

## Scope
- 本文以当前仓库 `wiki/` 为主入口，目标是回答“**在当前 Efficient VLA 语料里，哪些 baseline 最常被拿来比较，哪些更适合继续改代码**”。
- 这里的“社区使用分布”默认指**当前仓库语料内的出现分布**，而不是整个外部社区的精确统计份额。
- 这份 thread 优先服务后续研究选型，不追求枚举所有 baseline，只聚焦在当前语料中反复出现、且对后续代码实验最有意义的对象。
- 对于“是否开源、当前仓库形态是否成熟”这类会随时间变化的信息，应在真正决定 code base 前再去对应官方仓库核验；本 thread 只沉淀当前 `wiki` 能稳定支持的结论。

## Current Answer
- 如果只看当前 Efficient VLA 语料，最值得优先关注的 baseline 可以分成四类：
  - `OpenVLA family`：`OpenVLA / OpenVLA-OFT`
  - `pi family`：`π0 / π0.5`
  - `diffusion / cognition-action VLA`：`CogACT`
  - `lightweight efficient-first VLA`：`SmolVLA`
- 若只看当前语料中的**出现频次**，最明显的分布是：
  - `OpenVLA family`：出现在约 `43` 个 `papers` 页面里，是当前最主导的 baseline 家族。
  - `π family`：出现在约 `28` 个 `papers` 页面里，是第二主流 baseline 家族。
  - `CogACT`：约 `9` 个页面，主要集中在 diffusion / action-chunk / holistic acceleration 路线。
  - `SmolVLA`：约 `5` 个页面，更像在增长中的轻量高效基线，而不是当前最主导的统一比较对象。
  - `ACT / Diffusion Policy / SpatialVLA`：仍会出现，但在当前 efficient-VLA 语料里更多扮演历史对照、非 VLA sanity baseline、或局部任务对照。
- 如果目标是选一个最实用的开源 code base：
  - **默认首选**通常是 `OpenVLA / OpenVLA-OFT`，因为它在当前语料中的比较地位最稳，且大量高效方法直接围绕它展开。
  - 如果你更关心 **flow / diffusion-style VLA**，应优先考虑 `π family` 或 `CogACT`。
  - 如果你更关心 **低算力、快速迭代、尽快在自己任务上跑通**，`SmolVLA` 往往比前两类更合适。
- 最关键的一点是：**“最常见 baseline” 与 “最适合作为你自己的代码底座” 不是同一个问题。**

## Structured Notes

### 1. 先把“baseline”分成两种角色
- 在当前语料里，baseline 大致承担两种不同角色：
  - `comparison baseline`
    - 作用：论文里拿来做 head-to-head 对照，证明“更快”“更省”“更强”。
  - `engineering baseline`
    - 作用：真正适合你 fork 下来改、接新任务、插新模块、做消融实验的代码底座。
- 这两者经常重叠，但不总是重叠：
  - `OpenVLA family` 兼具两种角色；
  - `ACT / Diffusion Policy` 在很多论文里仍是比较 baseline，但如果你的问题是 Efficient VLA，本身未必是最合适的主代码底座；
  - `SmolVLA` 作为工程底座很有吸引力，但在当前语料里还不是最主导的统一比较对象。

### 2. 当前语料里最常见的 baseline 家族

#### 2.1 `OpenVLA family`
- 类型：
  - `OpenVLA` 是当前语料里最主流的 `autoregressive open-source generalist VLA`。
  - `OpenVLA-OFT` 不是全新 backbone，而是针对 `OpenVLA-style` VLA 的优化微调 recipe / 强化版本。
- 在当前语料中的分布：
  - `OpenVLA` 或 `OpenVLA-OFT` 共出现在约 `43` 个 `papers` 页面里，是最明显的第一主流。
  - 很多 Efficient VLA 方法直接以它为被加速对象、主比较对象，或 architecture scope 的第一验证对象。
- 为什么它会主导比较：
  - 它是当前语料中最稳定的开放式 manipulation VLA 参照物。
  - `OFT` 又把 `OpenVLA` 从“强但慢的自回归基线”，进一步推进成“可微调、可部署、速度显著更高”的 recipe baseline。
  - 因此很多高效方法会先证明“对 OpenVLA 家族有效”，再谈更广泛的外推。
- 优点：
  - 语料内可比性最强，最容易和已有 efficient-VLA 工作对齐。
  - 围绕它已经形成一串派生路线：`OFT`、`VLA-Cache`、`FlashVLA`、`SpecPrune-VLA`、`VLA-Pruner`、`BitVLA`、`VOTE`、`COMPRESSOR-VLA` 等。
  - 如果你想做 token pruning、cache、serving、量化、压缩、action representation 改写，这条生态最密集。
- 缺点：
  - 原始 `OpenVLA` 的动作生成与推理速度长期是被高效方法针对的主要瓶颈之一。
  - 如果你的核心研究问题是 flow / diffusion / cognition-action split，那么 `OpenVLA` 的 autoregressive 形态未必最贴切。
  - `OpenVLA` 和 `OpenVLA-OFT` 虽同属一族，但运行时行为和下游 recipe 已经差异很大，不能混成单一 baseline。
- 更稳的理解方式：
  - 把 `OpenVLA` 看成当前语料中的**主标准底座**。
  - 把 `OpenVLA-OFT` 看成当前最强、最常被直接对标的 **practical OpenVLA variant**。

#### 2.2 `π family`
- 类型：
  - `π0 / π0.5` 更接近 `flow / diffusion-style generalist VLA family`。
- 在当前语料中的分布：
  - `π family` 在约 `28` 个 `papers` 页面中出现，是第二主流 baseline 家族。
  - 它尤其常出现在和 `OpenVLA family` 做 route contrast 的论文里：一类代表 autoregressive VLA，一类代表 flow/diffusion VLA。
- 为什么它重要：
  - 它给 Efficient VLA 社区提供了一个与 `OpenVLA family` 明显不同的设计参照。
  - 很多论文要证明自己的方法不是只对 autoregressive VLA 有效，就会补 `π` 上的验证。
  - `VLA-Pruner`、`BitVLA`、`Shallow-π` 等工作都把 `π` 当作关键 cross-architecture baseline。
- 优点：
  - 对研究 flow / diffusion head、sampling/compression、layer reduction、real-time action generation 的工作尤其关键。
  - 当你不想把问题限定在 `OpenVLA` 这一路线时，`π family` 是最自然的第二锚点。
- 缺点：
  - 在当前语料里，它虽然常见，但很多高效方法对它的验证还没有 `OpenVLA family` 那么系统。
  - 有些论文对 `π` 的比较只停留在附录、局部 benchmark 或 narrower operating point，而不是完整主表。
- 更稳的理解方式：
  - 把 `π family` 看成当前 efficient-VLA 里最重要的**第二主流架构参照系**，尤其适合用来检验方法是否跨 autoregressive / flow 两类路线成立。

#### 2.3 `CogACT`
- 类型：
  - `CogACT` 属于 `cognition-action token + diffusion action module` 的 foundation VLA。
- 在当前语料中的分布：
  - 约出现在 `9` 个页面里，远少于 `OpenVLA family` 和 `π family`，但并不边缘。
  - 它主要集中出现在 `diffusion / holistic acceleration / action-chunk` 相关路线中。
- 为什么它重要：
  - 它不是单纯“又一个 baseline”，而是给这类工作提供了一个更明确的 cognition-action 分工结构。
  - `EfficientVLA` 就明确把 `CogACT` 当作被联合加速的主体。
- 优点：
  - 如果你的工作要处理语言层、视觉 token、action head 三类冗余的协同问题，它比单纯自回归 VLA 更合适。
  - 对 action chunk、diffusion head、system throughput 的研究更自然。
- 缺点：
  - 在当前语料里，它不是最主流的统一比较对象。
  - 如果你的目标是“尽量和多数 efficient-VLA 论文主表直接对齐”，`OpenVLA family` 往往仍然更优先。
- 更稳的理解方式：
  - 把 `CogACT` 看成**扩展 diffusion/cognition-action 路线的主锚点**，而不是全社区第一标准 baseline。

#### 2.4 `SmolVLA`
- 类型：
  - `SmolVLA` 属于 `small, efficient, community-driven VLA`，也是典型的 `lightweight efficient-first baseline`。
- 在当前语料中的分布：
  - 约出现在 `5` 个页面中。
  - 它在“作为统一比较 baseline”的频率上不高，但在“作为轻量高效底座”的吸引力上很强。
- 为什么它重要：
  - 它代表的是另一种 baseline 逻辑：不是先接受大模型再优化，而是直接从小、可部署、可社区化的角度设计。
  - 在一些结构压缩、蒸馏、轻量部署论文里，它作为 efficient-first baseline 很有代表性。
- 优点：
  - 更适合把“快速上手、低硬件门槛、快速迁移到自己任务”作为优先级。
  - 如果你的实验目标不是和所有大模型 SOTA 正面对齐，而是尽快做出稳定可改的系统，`SmolVLA` 很有吸引力。
- 缺点：
  - 当前语料里它还不是最常见的统一比较对象。
  - 若你的论文需要和大量 OpenVLA-based 高效方法正面并表，直接用 `SmolVLA` 做唯一主 baseline 可能不够对齐主流叙事。
- 更稳的理解方式：
  - 把 `SmolVLA` 看成**工程友好型、efficient-first 的增长中 baseline**，而不是当前最主导的 benchmark lingua franca。

### 3. `ACT / Diffusion Policy / SpatialVLA` 应该怎么看
- `ACT` 和 `Diffusion Policy`
  - 在当前语料里仍然会出现，但更像 `historical non-VLA baselines` 或 `from-scratch policy baselines`。
  - 在 `OFT` 等论文中，它们常被拿来和 fine-tuned VLA 做对照，说明“VLA 的语言和预训练收益是否值得”。
  - 如果你的问题其实更偏 action generation、不是 VLA 本体，保留它们很有意义。
  - 但如果你的问题是 Efficient VLA 主体路线，它们通常不该成为唯一主代码底座。
- `SpatialVLA`
  - 当前语料里有出现，但不是 dominant baseline family。
  - 更适合作为局部路线对照，而不是当前最稳的主 baseline 选择。

### 4. 为什么 `OpenVLA family` 会成为当前最稳的默认 baseline
- 因为它同时满足三件事：
  - 有足够强的基础能力，所以做高效化才有意义。
  - 有足够多的后续工作围绕它展开，所以方法对齐成本低。
  - `OpenVLA` 与 `OpenVLA-OFT` 之间形成了一个很自然的“从原始 base 到 practical optimized baseline”的连续谱。
- 这让它在当前语料里兼具：
  - `community comparison standard`
  - `engineering modification substrate`
  - `ablation-friendly target`
- 如果你今天只想选一个 baseline 去承接后续 Efficient VLA 改造，默认优先级仍然是它。

### 5. 但“最常见”不等于“最适合你”
- 真正选 code base 时，至少要先问五个问题：
  - 你的研究问题更像 `autoregressive VLA optimization`，还是 `flow / diffusion VLA optimization`？
  - 你最关心的是 `可比性`，还是 `低成本快速迭代`？
  - 你的实验对象是 `simulation benchmark` 还是 `real robot / edge deployment`？
  - 你打算改的是 `action representation / decoding`、`token pruning / cache`、`reasoning`、还是 `system serving`？
  - 你的硬件预算能否承受主 baseline 的正常训练 / finetune / inference 路径？
- 这五个问题基本决定了 baseline 选择，不应该被“哪篇 paper 最火”替代。

### 6. 选开源 code base 时最该看的因素

#### 6.1 `研究问题是否和 baseline 的主形态对齐`
- 若你研究的是：
  - `token pruning / cache / serving / autoregressive action compression`
    - 优先考虑 `OpenVLA / OpenVLA-OFT`
  - `flow / diffusion step compression / action-head acceleration / layer reduction`
    - 优先考虑 `π family` 或 `CogACT`
  - `低成本部署 / 快速 finetune / 小模型实验`
    - 优先考虑 `SmolVLA`

#### 6.2 `是否需要与主流论文直接可比`
- 若后续想把结果直接嵌进当前 efficient-VLA 主叙事，`OpenVLA family` 的对齐价值最高。
- 若只是为了证明方法原理成立，而不追求最大范围可比性，则 `SmolVLA` 或某个更轻量的底座可能更划算。

#### 6.3 `代码底座是否便于插模块`
- 最适合改造的 baseline，不一定是 paper 最强的那个，而是：
  - action path 清晰；
  - token / cache / decoding / head 结构边界清楚；
  - 训练、微调、评测脚本分工明确；
  - 很容易插入 profiling、ablation、替换模块。
- 从这个角度看，很多工作之所以反复使用 `OpenVLA family`，不仅因为它强，也因为它适合作为“被改造对象”。

#### 6.4 `训练与推理成本是否匹配你的节奏`
- 如果 baseline 太重，你的大部分时间会消耗在把环境跑通，而不是做方法创新。
- 因而：
  - 大模型强 baseline 适合做“主结果对齐”；
  - 轻量 baseline 适合做“快速原型验证”。
- 很多时候最实用的策略不是只选一个，而是：
  - 先用轻量 baseline 验证思路；
  - 再迁移到主流 baseline 做最终对齐。

### 7. 面向后续修改与实验的具体建议

#### 7.1 如果你没有特别强的先验路线
- 默认建议：
  - 主 baseline 选 `OpenVLA-OFT`
  - 备份 / 第二 baseline 选 `π family` 或 `SmolVLA`
- 原因：
  - `OpenVLA-OFT` 兼顾当前语料里的主流可比性和实践可用性；
  - 第二 baseline 用来判断你的方法是不是只对某一路线有效。

#### 7.2 如果你研究的是推理加速
- 优先：
  - `OpenVLA / OpenVLA-OFT`
- 原因：
  - pruning、cache、token compression、serving 类工作在当前语料里大多直接围绕它展开。
  - 你更容易和 `VLA-Cache`、`FlashVLA`、`SpecPrune-VLA`、`VLA-Pruner`、`COMPRESSOR-VLA` 一串工作对齐。

#### 7.3 如果你研究的是 flow / diffusion head
- 优先：
  - `π family`
  - 次选 `CogACT`
- 原因：
  - 这两类 baseline 更能暴露 sampling、step compression、layer reduction、action-chunk generation 的真实 tradeoff。
  - 若继续用 `OpenVLA`，很可能把问题扭曲成 autoregressive 路线专属优化。

#### 7.4 如果你研究的是轻量部署或小模型路线
- 优先：
  - `SmolVLA`
  - 次选 `EdgeVLA` 风格小模型路线
- 原因：
  - 这类问题最怕一开始就背上过重底座。
  - 从 efficient-first 底座出发，往往比从 7B 级别大底座往下裁剪更符合工程节奏。

#### 7.5 如果你想发论文、又想尽量减少实现风险
- 一个很实用的组合是：
  - `OpenVLA-OFT` 作为主结果底座
  - `SmolVLA` 作为快速原型底座
  - 如果方法声明跨架构，再补一个 `π family` 结果
- 这样做的好处是：
  - 有主流比较；
  - 有开发效率；
  - 还能避免方法只在单一路线成立。

### 8. 最终建议：按研究目标反推 baseline
- 若你的首要目标是：
  - `最大化与当前 efficient-VLA 主流论文可比`
    - 选 `OpenVLA / OpenVLA-OFT`
  - `研究 flow / diffusion-style VLA 的效率问题`
    - 选 `π family`
  - `在 diffusion/cognition-action 结构上做系统级效率改造`
    - 选 `CogACT`
  - `低成本快速改、尽快把任务跑起来`
    - 选 `SmolVLA`
- 如果只能给一个总体建议：
  - **主线研究用 `OpenVLA-OFT`，快速工程迭代用 `SmolVLA`，跨架构稳健性验证用 `π family`。**

## Related Wiki Pages
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/papers/2502_19645_OFT.md|2502_19645_OFT]]
- [[wiki/papers/2506_10100_EfficientVLA.md|2506_10100_EfficientVLA]]
- [[wiki/papers/2511_16449_VLA-Pruner.md|2511_16449_VLA-Pruner]]
- [[wiki/papers/2601_20262_Shallow-pi.md|2601_20262_Shallow-pi]]
- [[wiki/papers/2506_01844_SmolVLA.md|2506_01844_SmolVLA]]
- [[wiki/papers/2507_05116_VOTE.md|2507_05116_VOTE]]
- [[wiki/papers/2506_07530_BitVLA.md|2506_07530_BitVLA]]

## Evidence Notes
- 当前“使用分布”采用的是一个保守代理指标：在 `wiki/papers/*.md` 里，某 baseline family 作为比较对象或验证对象出现的频次。
- 这只能说明当前仓库语料内的比较习惯，不能直接等价为全社区真实份额。
- 当前语料对 `OpenVLA family` 的偏好非常明显，这也是为什么很多 efficient-VLA 工作会把它当成第一验证对象。
- `π family` 之所以重要，不只是出现频次高，更因为它提供了和 `OpenVLA` 不同的架构参照系。
- `SmolVLA` 的语料频次不高，不代表它不适合工程；它更像“工程友好型 baseline”，而不是“主流比较标准”。

## Open Uncertainties
- 当前 thread 对“是否开源、当前仓库是否仍活跃、安装是否顺手”的判断没有固化进 repo，因为这些信息会随时间变化，应该在真正做选型时重新核验。
- `GR00T`、`RDT-1B`、`SpatialVLA` 在当前语料里也会作为 baseline 出现，但出现频次和结构中心性还不足以进入本 thread 的第一梯队。
- 部分 baseline 的出现频次会受单篇论文写作风格影响，例如有的页会详细列多个 baseline，有的页只保留 headline 对照，因此当前计数只能视作近似分布。

## Update Log
- `2026-04-22`：新建本 thread。基于当前 `wiki` 语料整理 Efficient VLA 常见 baseline 家族、语料内出现分布、优缺点与 code base 选型逻辑，形成面向后续实验设计的 baseline 选型笔记。
