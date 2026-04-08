# 2507_05116_VOTE-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2507_05116_VOTE.md|2507_05116_VOTE]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：论文在不同位置/setting 下报告了 `39x`、`38.6x`、`48.8x` 等效率数字；引用时应把每个数字精确对齐到具体硬件与 baseline。

## Evidence
- 核心证据命题：这篇论文提出 **VOTE**，它认为现有自回归 VLA 效率低的原因有两个：一是动作 token 太多，二是已经预测出的动作没有被充分复用。为同时解决这两个问题，论文提出一套训练和推理结合的 recipe：先把整个 action chunk 压缩成一个特殊的 `<ACT>` token，再对当前与历史预测动作做 **trajectory ensemble voting**，以提升鲁棒性。 来源：[[raw/2507_05116_VOTE.pdf]]，**Abstract / Introduction**：可直接承载两类 bottleneck 的诊断，以及 `39x faster than OpenVLA`、`46 Hz` 等顶层效率主张。
- 补充证据命题：作者把 VOTE 同时定位成**速度提升方法**与**性能提升方法**。headline 结果包括：相对 OpenVLA 推理可快约 **`39x`**、在边缘设备上达到约 **`46 Hz`** throughput，同时在 LIBERO 和 SimplerEnv 上也报告了更高成功率。 来源：[[raw/2507_05116_VOTE.pdf]]，**Figure 1**：VOTE pipeline 总览图，是 `<ACT>` 动作生成与 ensemble voting 关系的最佳第一锚点。
- 主证据锚点 1：来源：[[raw/2507_05116_VOTE.pdf]]，**Abstract / Introduction**：可直接承载两类 bottleneck 的诊断，以及 `39x faster than OpenVLA`、`46 Hz` 等顶层效率主张。
- 主证据锚点 2：来源：[[raw/2507_05116_VOTE.pdf]]，**Figure 1**：VOTE pipeline 总览图，是 `<ACT>` 动作生成与 ensemble voting 关系的最佳第一锚点。
- 主证据锚点 3：来源：[[raw/2507_05116_VOTE.pdf]]，**Main benchmark tables**：SimplerEnv 与 LIBERO 主表是后续验证 `>20%` 与 `+7%` 这类性能提升的首要位置。

## Figure / Caption Anchors
- **Fig. 1 (p.2)**：caption 明确展示 `<ACT>` 单 token 训练框架与 trajectory ensemble voting 的完整 pipeline；它说明的是“训练时压缩 action token + 推理时做 voting”的组合，而不是单一 inference trick。
- **Fig. 2 (p.4)**：latency profile 直接说明当前 VLA 的主要计算瓶颈在 VLM backbone，且 `SpatialVLA / OpenVLA / CogACT` 的 overhead 结构并不相同；这是 `why speed matters` 的诊断证据。
- **Fig. 3 (p.6)**：Vote Action Ensemble 的示意图，是“历史预测给当前动作投票”这一推理机制的最佳局部锚点；它支撑鲁棒性来源，而不是 throughput 数字。

## Figure / Caption / Wording Split
- `plug-and-play` 只能用于 **ensemble voting inference strategy**，不能直接外推到整个 `VOTE` 训练框架；`<ACT>` 单 token 方案本身需要重新训练 / fine-tune。来源：[[raw/2507_05116_VOTE.pdf]]，第 2-3 页 Introduction、Contributions；第 2 页 Fig. 1 caption。
- `39x faster than OpenVLA` 与 `46 Hz throughput` 绑定的是 **Jetson Orin edge deployment**，而不是 A6000 latency 表或 LIBERO / SimplerEnv success rate。来源：[[raw/2507_05116_VOTE.pdf]]，第 2 页 Introduction；第 9 页 edge-device latency / throughput table。
- `Fig. 2` 支撑的是 **VLM decoding dominates latency** 的 bottleneck diagnosis，而不是 `VOTE` 自己的 benchmark advantage；后续引用它时不能把诊断图和最终性能表混成同一 headline。来源：[[raw/2507_05116_VOTE.pdf]]，第 4 页 Fig. 2 与相邻正文。
- `Fig. 3` 支撑的是 **why voting improves robustness**：当前 observation 获得更高权重，同时历史动作提供 committee-style correction；它不是单独的 speedup 证据。来源：[[raw/2507_05116_VOTE.pdf]]，第 6 页 Fig. 3 与相邻正文。

## 不可混写项
- 论文在不同位置/setting 下报告了 `39x`、`38.6x`、`48.8x` 等效率数字；引用时应把每个数字精确对齐到具体硬件与 baseline。
- `VOTE` 把两件大事合在同一页中：`<ACT>` 单 token 训练方案与 ensemble voting 推理机制。后续 evidence 层可能需要把它们拆开，而不是一直保留为一个 merged claim。
- 当前保留的 LIBERO 与 SimplerEnv 增益仍是带 caveat 的 headline；引用时应把每个数字钉到具体表格、benchmark split 与 comparison baseline。

## 影响页面
- [[wiki/papers/2507_05116_VOTE.md|2507_05116_VOTE]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
