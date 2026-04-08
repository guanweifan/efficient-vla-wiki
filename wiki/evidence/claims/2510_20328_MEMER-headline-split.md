# 2510_20328_MEMER-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2510_20328_MEMER.md|2510_20328_MEMER]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`outperforms prior methods on three real-world long-horizon tasks` 目前只保留为作者主张；仍需在 Table 1 / Figure 5 处精确拆清比较对象、任务指标和幅度。

## Evidence
- 这篇论文提出 **MemER**，目标是为原本缺乏长期记忆能力的机器人策略补上“可检索经验记忆”这一层，而不是简单把更长 observation history 直接塞进 policy。作者的基本判断是：对长时视觉历史做朴素条件化既昂贵又容易在 covariate shift 下失稳，而 indiscriminate subsampling 又会引入无关或冗余信息。来源：[[raw/2510_20328_MEMER.pdf]]，第 1 页 Abstract、Introduction。
- 核心方法主张是一个 **hierarchical memory policy**：高层策略负责从最近上下文里提名并跟踪与任务相关的 keyframes，同时输出低层策略要执行的语言 subtask；低层策略则专注于具体动作执行。也就是说，这篇论文把“记什么”和“怎么做”显式分开了。来源：[[raw/2510_20328_MEMER.pdf]]，第 1-2 页 Abstract、Fig. 1；第 3-5 页 Sec. 3。
- 主证据锚点 1：来源：[[raw/2510_20328_MEMER.pdf]]，**Abstract**：第 1 页。可直接承载“hierarchical memory policy + keyframe selection + three real-world long-horizon tasks”。
- 主证据锚点 2：来源：[[raw/2510_20328_MEMER.pdf]]，**Figure 1 + Introduction**：第 2 页。用于锚定 MemER 的总体 framing、`50 teleoperated demos` 与长时记忆任务动机。
- 主证据锚点 3：来源：[[raw/2510_20328_MEMER.pdf]]，**Sec. 3.1 / Figure 2**：第 3-4 页。用于锚定高层 policy、低层 policy、subtask interface 与 keyframe filter 的交互方式。

## Table / Metric Anchors
- **Table 1 + Figure 5**：第 7-8 页。用于锚定三类真实任务的主结果、任务指标和 overall accuracy 走势，明确“优于 prior methods”到底落在哪些 setting。

## Table / Metric Split
- `**Table 1 + Figure 5**` 这一层应单独承载 `**Table 1 + Figure 5**` 相关的 benchmark / metric / operating point。 这一层对应三类真实任务的主结果、任务指标和 overall accuracy 走势，明确“优于 prior methods”到底落在哪些 setting。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2510_20328_MEMER.pdf]]，`**Table 1 + Figure 5**`。

## 不可混写项
- `outperforms prior methods on three real-world long-horizon tasks` 目前只保留为作者主张；仍需在 Table 1 / Figure 5 处精确拆清比较对象、任务指标和幅度。
- `50 teleoperated demonstrations` 与 `10-15 interventions` 更像当前 recipe，而不是任务无关的数据效率结论；仍需决定在主题页里保留多强的推广语气。
- MemER 同时强调 `memory via experience retrieval`、`hierarchical VLA`、`visual-memory-only representation`；后续 taxonomy 需要统一它的主定位。

## 影响页面
- [[wiki/papers/2510_20328_MEMER.md|2510_20328_MEMER]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
