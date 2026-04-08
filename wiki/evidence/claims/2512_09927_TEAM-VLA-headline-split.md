# 2512_09927_TEAM-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2512_09927_TEAM-VLA.md|2512_09927_TEAM-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`109 ms -> 72.1 ms`、`1.5x+ speedup`、以及 “无平均性能下降/甚至超过 full model” 目前仍是 bundled summary，仍需拆到具体 benchmark split 与具体比较对象上。

## Evidence
- 核心证据命题：TEAM-VLA 将自己定位为一种 **training-free、observation-only** 的 VLA visual token compression 方法，目标是在不依赖 retraining、可学习查询或历史帧缓存的前提下，改善 VLA 的 success-latency tradeoff。论文的核心主张是：已有 VLA / VLM token pruning 方法要么依赖 temporal buffering，要么依赖稀疏且不稳定的 text-image salience，因此很难在真实机器人部署中同时兼顾速度、鲁棒性和上下文完整性。 来源：[[raw/2512_09927_TEAM-VLA.pdf]]，**Abstract / introduction**：最清楚地给出 TEAM-VLA 的总 framing：training-free、observation-only、Expand + Merge、以及为什么现有 temporal 或 semantic-only 方法不够实用。
- 补充证据命题：为此，TEAM-VLA 提出 “Expand + Merge” 两阶段压缩策略：先在当前帧中用 similarity seed + context sampling + spatial expansion 重建较完整的前景区域，再在 backbone 中层用 action-guided soft bipartite merging 压缩深层 token。 来源：[[raw/2512_09927_TEAM-VLA.pdf]]，**Fig. 1 (p.1)**：前景提取策略的核心直观对比，也是“为什么要先 expand 再 prune”的第一锚点。
- 主证据锚点 1：来源：[[raw/2512_09927_TEAM-VLA.pdf]]，**Abstract / introduction**：最清楚地给出 TEAM-VLA 的总 framing：training-free、observation-only、Expand + Merge、以及为什么现有 temporal 或 semantic-only 方法不够实用。
- 主证据锚点 2：来源：[[raw/2512_09927_TEAM-VLA.pdf]]，**Fig. 1 (p.1)**：前景提取策略的核心直观对比，也是“为什么要先 expand 再 prune”的第一锚点。
- 主证据锚点 3：来源：[[raw/2512_09927_TEAM-VLA.pdf]]，**Fig. 2 (p.3)**：TEAM-VLA 整体 pipeline 图，若补 `L2`，这是 similarity sampling、context sampling、expansion、action-guided merging 如何串起来的最好入口。

## Table / Metric Anchors
- **TABLE I (p.6)**：LIBERO 主结果锚点，用来核对 `TEAM-VLA` 相对 `OpenVLA-OFT`、`EfficientVLA`、`VLA-Cache` 的 `SR / latency / FLOPs` 对比。
- **TABLE II (p.6)**：组件消融锚点，用来区分 `Context Sampling`、`Token Expanding`、`Action-Guided Merging` 分别带来的 `SR / latency / pruned tokens` 变化。
- **TABLE IV (p.6)**：阈值 `τ` operating point 锚点，用来核对 `avg success / avg latency / avg patch count` 的 tradeoff。

## Table / Metric Split
- `TABLE I | LIBERO main result`：`TEAM-VLA(Ours)` 的四个子套件结果是 `spatial 99.2 / 68.1 ms`、`object 96.5 / 74.7 ms`、`goal 97.0 / 72.9 ms`、`long 93.8 / 72.8 ms`，平均 `96.6 / 72.1 ms / 39% FLOPs`。这里支撑的是“相对 `OpenVLA-OFT` 从 `109 ms` 降到 `72.1 ms` 且平均 success 仍为 `96.6`”这组特定对比；它不能被写成对所有 baseline 都“无性能下降”。对 `EfficientVLA` 的对比则是 `88.9 / 70.6 ms`，说明增加约 `1.5 ms` 换来 `+7.7` 平均 success。来源：[[raw/2512_09927_TEAM-VLA.pdf]]，第 6 页，Table I。
- `TABLE II | component ablation`：如果只做 `Context Sampling (u=0.1)`，结果是 `80.1 SR / 67.4 ms / 461 pruned`，说明单纯 aggressive pruning 会明显掉点；加入 `Token Expanding (K=3)` 后可回到 `93.8 / 76.8 / 302`；最终 `Action-Guided Merging (top-80)` 给出 `93.8 / 72.8 / 432`，是本文主 operating point。这里支撑的是 Expand + Merge 两阶段组合，而不是单独任何一步的充分性。来源：[[raw/2512_09927_TEAM-VLA.pdf]]，第 6 页，Table II。
- `TABLE IV | threshold operating point`：`τ=0` 时平均 `97.2 success / 86.0 ms / 342.3 patches`；`τ=1` 时 `96.6 / 75.3 / 196.0`；`τ=2` 时 `94.6 / 71.8 / 151.0`。因此 “速度更快且不降平均性能” 更准确地对应 `τ=1` 的 operating point，而不是所有阈值都成立。来源：[[raw/2512_09927_TEAM-VLA.pdf]]，第 6 页，Table IV。

## 不可混写项
- `109 ms -> 72.1 ms`、`1.5x+ speedup`、以及 “无平均性能下降/甚至超过 full model” 目前仍是 bundled summary，仍需拆到具体 benchmark split 与具体比较对象上。
- 论文把 Token Expanding 与 action-guided merging 一起包装成 TEAM-VLA 主方法；后续 evidence 层可能需要区分“前景重建贡献”和“深层合并贡献”。
- 当前最强直接证据主要基于 LIBERO + OpenVLA-OFT；仍应明确 TEAM-VLA 的跨架构、跨环境外推边界，而不是直接泛化成一般性 VLA compression 结论。

## 影响页面
- [[wiki/papers/2512_09927_TEAM-VLA.md|2512_09927_TEAM-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
