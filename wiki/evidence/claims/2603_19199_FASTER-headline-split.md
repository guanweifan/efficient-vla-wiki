# 2603_19199_FASTER-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_19199_FASTER.md|2603_19199_FASTER]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`10x`、`3x`、TTFA 改进、以及实机任务优势目前仍是 bundled headline，仍需分别拆到模型、GPU 平台与任务设置。

## Evidence
- 核心证据命题：FASTER 的核心命题是：现有 real-time flow VLAs 虽然通过 asynchronous inference 改善了轨迹连续性，但仍然忽视了 **reaction latency** 这一更关键的实时性维度；真正限制机器人对动态环境做出快速响应的，不只是整体 inference latency，而是 **Time to First Action (TTFA)** 以及 inference-execution cycle 的频率。 来源：[[raw/2603_19199_FASTER.pdf]]，**Abstract / introduction**：最清楚地给出论文为何认为现有 async real-time VLA 仍然忽视 reaction latency，以及为什么要引入 TTFA。
- 补充证据命题：论文认为，flow-based action chunking 里广泛使用的 constant timestep schedule 会强迫所有 action 都完成同样多的 denoising steps，导致最紧急的 immediate action 也要等整段 action chunk 一起“去噪完”才能发出，这正是反应迟缓的根源。 来源：[[raw/2603_19199_FASTER.pdf]]，**Fig. 1 (p.1)**：FASTER 的总 framing 图，也是 “10× acceleration for immediate reaction” 的第一锚点。
- 主证据锚点 1：来源：[[raw/2603_19199_FASTER.pdf]]，**Abstract / introduction**：最清楚地给出论文为何认为现有 async real-time VLA 仍然忽视 reaction latency，以及为什么要引入 TTFA。
- 主证据锚点 2：来源：[[raw/2603_19199_FASTER.pdf]]，**Fig. 1 (p.1)**：FASTER 的总 framing 图，也是 “10× acceleration for immediate reaction” 的第一锚点。
- 主证据锚点 3：来源：[[raw/2603_19199_FASTER.pdf]]，**Fig. 2 (p.5)**：同步/异步 pipeline 的时间结构图，用来理解 TTFA、execution horizon 与 reaction time distribution 的关系。

## Table / Metric Anchors
- **Table 2 (p.12)**：RTX 4090 / RTX 4060 上 reaction capability 主表，用来核对 TTFA 与期望 reaction time 的改进。
- **Table 3 (p.12)**：reaction speed 的概率式比较表，用来判断 FASTER 相对 Sync / Async 的 probabilistic reactivity 优势。
- **Table 4 (p.14)**：LIBERO / CALVIN simulation 主表，用来核对在 aggressive sampling 下性能是否被显著破坏。

## Table / Metric Split
- `Table 2` 是 **TTFA / expected reaction time 主表**：在 `π0.5` 上，`RTX 4060` 的 `TTFA` 从 `303.3ms` 降到 `238.6ms`；在 `X-VLA` 上，同一平台从 `399.5ms` 降到 `129.2ms`，对应约 `3.09×` 的 TTFA speedup。这张表支撑的是 reaction-capability headline，而不是 simulation task performance。来源：[[raw/2603_19199_FASTER.pdf]]，第 12 页，Table 2。
- `Table 3` 对应 **probabilistic reaction superiority**：尤其 `X-VLA` 上，`FASTER` 在 `RTX 4090/4060` 对 `Sync` 与 `Async` 都达到 `1.00` 的概率优势；这说明的是反应分布层面的 dominance，不应和 Table 2 的具体 TTFA 数字混成一组单一 speed metric。来源：[[raw/2603_19199_FASTER.pdf]]，第 12 页，Table 3。
- `Table 4` 对应 **simulation tradeoff**：它回答的是在更激进的采样下，`LIBERO / CALVIN` 任务性能是否显著受损，因此属于“反应更快但长期精度可能有轻微代价”的另一层证据。来源：[[raw/2603_19199_FASTER.pdf]]，第 14 页，Table 4。

## 不可混写项
- `10x`、`3x`、TTFA 改进、以及实机任务优势目前仍是 bundled headline，仍需分别拆到模型、GPU 平台与任务设置。
- 论文把 HAS、streaming client-server、early stopping 一起包装成 FASTER 主体；后续 evidence 层可能需要区分“sampling schedule 本身”的贡献与“系统工程式 streaming / stopping”的贡献。
- 论文强调方法对 flow-based VLAs 是 plug-and-play，但当前直接证据主要集中在 `π0.5` 与 `X-VLA`；仍应明确它对其他 flow-based VLA 乃至非-flow action chunking policy 的外推边界。

## 影响页面
- [[wiki/papers/2603_19199_FASTER.md|2603_19199_FASTER]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
