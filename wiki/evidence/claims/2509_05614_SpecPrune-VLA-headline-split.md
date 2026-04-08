# 2509_05614_SpecPrune-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2509_05614_SpecPrune-VLA.md|2509_05614_SpecPrune-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：论文报告了多种 speedup 数字（`1.45x`、`1.31x`、`1.46x`、`1.57x`、`1.70x`、以及 `2.09x` 的 LLM-only inference）；引用时应把 end-to-end latency 与 LLM-only latency 分开，并为每个数字标注具体硬件与 baseline。

## Evidence
- 核心证据命题：这篇论文提出 **SpecPrune-VLA**，把它定位成一种面向 **compute-bound single-step VLA inference** 的 training-free 加速方法。论文认为，之前的 token-pruning 方法过度关注当前动作步，而忽略了更长时间尺度上的全局 temporal structure，因此在机器人控制里常出现较大的性能损失。 来源：[[raw/2509_05614_SpecPrune-VLA.pdf]]，**Abstract / Introduction**：可直接承载 training-free、two-level pruning、action-aware control 以及 `1.57x / 1.70x` 的顶层效率主张。
- 补充证据命题：为此，作者提出一个两级 pruning recipe：同时结合 **global history reuse**、**local token importance** 与 **action-aware controller**。其中 controller 会根据动作粒度动态调节 pruning 强度，以降低对精细 manipulation 步骤的伤害。 来源：[[raw/2509_05614_SpecPrune-VLA.pdf]]，**Figure 1 (p.1)**：最适合说明 VLA inference 是 compute-bound，且主要瓶颈在 LLM 而不是 tokenizer 或 action head。
- 主证据锚点 1：来源：[[raw/2509_05614_SpecPrune-VLA.pdf]]，**Abstract / Introduction**：可直接承载 training-free、two-level pruning、action-aware control 以及 `1.57x / 1.70x` 的顶层效率主张。
- 主证据锚点 2：来源：[[raw/2509_05614_SpecPrune-VLA.pdf]]，**Figure 1 (p.1)**：最适合说明 VLA inference 是 compute-bound，且主要瓶颈在 LLM 而不是 tokenizer 或 action head。
- 主证据锚点 3：来源：[[raw/2509_05614_SpecPrune-VLA.pdf]]，**Figure 2 (p.2)**：SpecPrune-VLA 方法总览图，是 static pruning、dynamic pruning 与 action-aware controller 如何协同工作的第一锚点。

## Table / Metric Anchors
- **Table 1 (p.8)**：simulation 主结果，用于锚定 LIBERO 上的 end-to-end success rate、latency、FLOP reduction 与 speedup。
- **Table 2 / Table 3 (p.8)**：global attention reuse 与 entropy-based layer weighting 的主消融入口，适合检验“local + global” 的方法叙事是否站得住。
- **Table 4 (p.9)**：real-world `1.70x` speedup 且 success rate 不明显崩溃的主证据入口。

## Table / Metric Split
- `**Table 1 (p.8)**` 这一层应单独承载 `**Table 1 (p.8)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2509_05614_SpecPrune-VLA.pdf]]，`**Table 1 (p.8)**`。
- `**Table 2 / Table 3 (p.8)**` 这一层应单独承载 `**Table 2 / Table 3 (p.8)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2509_05614_SpecPrune-VLA.pdf]]，`**Table 2 / Table 3 (p.8)**`。
- `**Table 4 (p.9)**` 这一层应单独承载 `**Table 4 (p.9)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2509_05614_SpecPrune-VLA.pdf]]，`**Table 4 (p.9)**`。

## Figure / Caption / Wording Split
- `training-free` 在本文里对应 **two-level pruning + heuristic controller at inference time**；它强调不重训 backbone，但不意味着完全没有 hand-crafted control logic。来源：[[raw/2509_05614_SpecPrune-VLA.pdf]]，第 1-2 页 Abstract / Introduction。
- `Fig. 1` 支撑的是 **VLA inference is compute-bound and bottlenecked by the LLM rather than tokenizer or action head**，这是为什么 pruning 要围绕 history reuse + local importance 展开的诊断入口。来源：[[raw/2509_05614_SpecPrune-VLA.pdf]]，第 1 页 Fig. 1 与 Abstract。
- `Fig. 2` 支撑的是 **static pruning + dynamic pruning + action-aware controller** 的组合逻辑；它不是速度结果图。若后续解释 controller 的必要性，应优先回到这里，而不是只看主表。来源：[[raw/2509_05614_SpecPrune-VLA.pdf]]，第 2 页 Fig. 2 与方法章节。
- `demonstrated scope` 目前仍以 `OpenVLA-OFT`、`π0` 和 real-world `OpenVLA-OFT` 为主，因此“适用于 VLA inference”需要和“已直接验证的 backbone / environment”区分开来。来源：[[raw/2509_05614_SpecPrune-VLA.pdf]]，实验主表与 real-world 表。

## 不可混写项
- 论文报告了多种 speedup 数字（`1.45x`、`1.31x`、`1.46x`、`1.57x`、`1.70x`、以及 `2.09x` 的 LLM-only inference）；引用时应把 end-to-end latency 与 LLM-only latency 分开，并为每个数字标注具体硬件与 baseline。
- 方法被写成普遍适用于 VLA inference，但当前最强的直接证据仍集中在 OpenVLA-OFT、`π0` 与 real-world OpenVLA-OFT setting；引用时应区分 demonstrated scope 与更宽的 rhetorical scope。
- `action-aware controller` 当前仍被概括在 unified method 里，但从 ablation 看，它更像是保障 success rate 的独立组件；后续 evidence 层可能需要把 “pruning core” 与 “controller for robustness” 分开。

## 影响页面
- [[wiki/papers/2509_05614_SpecPrune-VLA.md|2509_05614_SpecPrune-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
