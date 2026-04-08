# 2511_16449_VLA-Pruner-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2511_16449_VLA-Pruner.md|2511_16449_VLA-Pruner]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`1.99x` speedup、`50%` pruning 可能带来性能提升、以及在 `87.5%` pruning 下仍保持鲁棒，这几类数字来自不同 retention ratio / backbone / benchmark，仍需逐项拆证据。

## Evidence
- 核心证据命题：VLA-Pruner 的核心主张是：VLM 里的 semantic-only visual token pruning 直接迁移到 VLA 上会失效，因为 VLA 推理同时包含 high-level semantic understanding 与 low-level action execution，不能只靠 prefill attention 做 token 保留。论文据此提出一个 plug-and-play、training-free 的 VLA token pruning 方法：同时考虑 vision-language prefill attention 与 action decode attention，并利用机器人操作中的 temporal continuity 去估计 prefill 时刻尚不可见的 action-side importance。 来源：[[raw/2511_16449_VLA-Pruner.pdf]]，**Abstract / introduction**：最清楚地说明 semantic-only pruning 为什么不适用于 VLA，以及 dual-system + temporal continuity 的总思路。
- 补充证据命题：作者关于效果的 headline 需要拆开理解：`1.99x` speedup 来自主结果表中的特定 retention ratio / backbone / benchmark 设置；`50%` pruning ratio 下的性能反升主要对应 `LIBERO-Long` 一类具体子集现象；“cross-architecture” 证据则由主文的 OpenVLA / OpenVLA-OFT 与附录中的 `π0` 结果共同支撑，而不是来自同一张统一主表。更稳的写法是：**dual-system-aware token retention 在已验证的几类 VLA 上，比 semantic-only pruning 更能维持 speed-performance tradeoff。** 来源：[[raw/2511_16449_VLA-Pruner.pdf]]，**Figure 1 (p.1)**：不同 pruning/caching 方法在 LIBERO 上的总体 tradeoff 对比，是 VLA-Pruner headline 优势的第一锚点。
- 主证据锚点 1：来源：[[raw/2511_16449_VLA-Pruner.pdf]]，**Abstract / introduction**：最清楚地说明 semantic-only pruning 为什么不适用于 VLA，以及 dual-system + temporal continuity 的总思路。
- 主证据锚点 2：来源：[[raw/2511_16449_VLA-Pruner.pdf]]，**Figure 1 (p.1)**：不同 pruning/caching 方法在 LIBERO 上的总体 tradeoff 对比，是 VLA-Pruner headline 优势的第一锚点。
- 主证据锚点 3：来源：[[raw/2511_16449_VLA-Pruner.pdf]]，**Figure 2 (p.4)**：论文最关键的诊断证据，直接展示 prefill attention 与 action decode attention 的差异，以及 temporal continuity 为何可被利用。

## Table / Metric Anchors
- **Table 1 (p.7)**：OpenVLA / OpenVLA-OFT 在 LIBERO 上的主结果锚点，包含 success rate、speedup、latency、FLOPs；`1.99x` 与高 ratio 下的主 headline 需要回到这里按 backbone 与 retention ratio 分开核对。
- **Table 2 (p.7)**：SIMPLER 上的 cross-environment generalization 结果，用来补“并非只在一个仿真环境有效”；它不是 `1.99x` speedup 的直接出处。
- **Table 4 (p.16)**：`π0` 上的跨架构结果锚点，用来支撑“不是只对 OpenVLA 家族有效”。

## Table / Metric Split
- `Table 1` 是 **LIBERO 主 tradeoff 表**：`1.99x` speedup 对应的是高压缩 `OpenVLA-OFT` 行，而 `50%` ratio 下的“性能反升”更多是 `LIBERO-Long` 这类子集现象；`1.63x / 1.80x` 也来自不同 backbone / retention ratio，不能 bundled 成一个统一速度结论。来源：[[raw/2511_16449_VLA-Pruner.pdf]]，第 7 页，Table 1。
- `Table 2` 对应 **SIMPLER cross-environment generalization**：它支撑的是“并非只在单一仿真环境有效”，不是 `1.99x` speedup 的出处。来源：[[raw/2511_16449_VLA-Pruner.pdf]]，第 7 页，Table 2。
- `Table 4` 对应 **π0 cross-architecture extension**：它说明方法不只对 `OpenVLA` 家族有效，但这层证据与主文 `OpenVLA / OpenVLA-OFT` 主表不属于同一 benchmark layer。来源：[[raw/2511_16449_VLA-Pruner.pdf]]，第 16 页，Table 4。

## Figure / Caption / Wording Split
- `Fig. 1` 支撑的是 **overall speed-performance tradeoff framing**，不是单一 retention ratio 的精确 operating point；真正的 ratio-level 数字仍要回 `Table 1`。来源：[[raw/2511_16449_VLA-Pruner.pdf]]，第 1 页 Fig. 1 与第 7 页 Table 1。
- `Fig. 2` 支撑的是 **why semantic-only pruning fails for VLA**：prefill attention 与 action decode attention 呈现不同关注模式，因此 dual-level token selection 才有必要。来源：[[raw/2511_16449_VLA-Pruner.pdf]]，第 4 页 Fig. 2 与相邻正文。
- `training-free / plug-and-play` 的边界是：方法不需要重新训练被加速的 backbone，但已验证范围主要集中在 `OpenVLA`、`OpenVLA-OFT` 和 `π0`；不能把它外推成所有 VLA pruning 场景都同样成立。来源：[[raw/2511_16449_VLA-Pruner.pdf]]，第 2-3 页 Introduction；第 7 页 Table 1；第 16 页 Table 4。
- `maintaining robustness even at 87.5% pruning ratio` 指的是高压缩下仍保持 relative accuracy / transfer tradeoff，不等于所有 retention ratio、所有 benchmark 都“无损”。来源：[[raw/2511_16449_VLA-Pruner.pdf]]，第 2-3 页 Introduction；第 7 页 Table 1；附录高压缩分析。

## 不可混写项
- `1.99x` speedup、`50%` pruning 可能带来性能提升、以及在 `87.5%` pruning 下仍保持鲁棒，这几类数字来自不同 retention ratio / backbone / benchmark，仍需逐项拆证据。
- 论文把 dual-system diagnosis、temporal smoothing heuristic、dual-level selection strategy 合并成一个总方法叙述；后续 evidence 层可能需要拆开“诊断成立”与“具体 heuristic 是否最优”。
- 论文强调 plug-and-play generality，但最强直接证据主要集中在带 action-to-vision cross-attention 的几类 VLA；仍应明确它的适用边界，而不是泛化成所有 VLA pruning 场景。

## 影响页面
- [[wiki/papers/2511_16449_VLA-Pruner.md|2511_16449_VLA-Pruner]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
