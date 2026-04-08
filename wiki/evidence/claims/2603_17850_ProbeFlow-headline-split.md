# 2603_17850_ProbeFlow-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_17850_ProbeFlow.md|2603_17850_ProbeFlow]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`14.8×` 是 action head decoding speedup，`2.8×` 是 end-to-end system latency cut；若写 headline，需要明确这两个数字不是同一口径。

## Evidence
- 更稳的单篇主命题应写成：`ProbeFlow` 是一条 **training-free、作用于 flow-matching action head 的 adaptive inference 路线**；它针对的是 action head 的迭代积分开销，而不是一般意义上的 VLM backbone 加速。来源：[[raw/2603_17850_ProbeFlow.pdf]]，第 1-3 页摘要、引言与 Fig. 1；第 5-7 页 Table I、Table II、Fig. 3-5。
- 补充证据命题：核心主张是：FM 轨迹在不同阶段具有不同曲率，固定步长积分会在近似线性区域浪费大量计算；如果使用一个 training-free 的 lookahead probe 去估计局部轨迹线性度，并据此动态分配 integration steps，就能在不重新训练模型的情况下显著减少 action head 的 NFE 与解码延迟。 来源：[[raw/2603_17850_ProbeFlow.pdf]]，几何原理与算法：[[raw/2603_17850_ProbeFlow.pdf]] 第 3-5 页 Fig. 2、Algorithm 1 与方法章节。这里说明如何用 `v_start` 与 `v_probe` 的 cosine similarity 近似曲率，并据此在 `Nmin` 与 `Nmax` 之间自适应分配步数。
- 主证据锚点 1：来源：[[raw/2603_17850_ProbeFlow.pdf]]，摘要与总框架：[[raw/2603_17850_ProbeFlow.pdf]] 第 1-3 页摘要、引言与 Fig. 1。这里定义 action-head bottleneck、`lookahead probe + dynamic scheduler` 的基本思路，以及 `14.8× / 2.8×` 的 headline。
- 主证据锚点 2：来源：[[raw/2603_17850_ProbeFlow.pdf]]，几何原理与算法：[[raw/2603_17850_ProbeFlow.pdf]] 第 3-5 页 Fig. 2、Algorithm 1 与方法章节。这里说明如何用 `v_start` 与 `v_probe` 的 cosine similarity 近似曲率，并据此在 `Nmin` 与 `Nmax` 之间自适应分配步数。
- 主证据锚点 3：来源：[[raw/2603_17850_ProbeFlow.pdf]]，MetaWorld 主结果：[[raw/2603_17850_ProbeFlow.pdf]] 第 5-6 页 Table I 与相邻正文。这里对应 `N = 50 -> avg. 2.6 steps`、`14.8×` action-head speedup、`2.8×` end-to-end latency cut，以及 success rate 保持。

## Table / Metric Anchors
- MetaWorld 主结果：[[raw/2603_17850_ProbeFlow.pdf]] 第 5-6 页 Table I 与相邻正文。这里对应 `N = 50 -> avg. 2.6 steps`、`14.8×` action-head speedup、`2.8×` end-to-end latency cut，以及 success rate 保持。
- LIBERO 主结果：[[raw/2603_17850_ProbeFlow.pdf]] 第 6-7 页 Table II、Fig. 3。这里对应 average `4.5` steps、`32.7 ms` flow solver latency、在 semantic bottleneck 上自动升到约 `14.1` steps 以恢复 success rate 的结果。
- real-world 与阈值敏感性：[[raw/2603_17850_ProbeFlow.pdf]] 第 7-9 页 Table V、Fig. 4-5。这里可回查 real-world pick-and-place 的 latency reduction、probe horizon `Δt_probe` 的敏感性，以及 training-free cross-domain deployability 的边界。

## Table / Metric Split
- `MetaWorld 主结果` 这一层应单独承载 `MetaWorld 主结果` 相关的 benchmark / metric / operating point。 这里收口为：MetaWorld 主结果：[[raw/2603_17850_ProbeFlow.pdf]] 第 5-6 页 Table I 与相邻正文。这里对应 `N = 50 -> avg. 2.6 steps`、`14.8×` action-head speedup、`2.8×` end-to-end latency cut，以及 success rate 保持。；`14.8×` 是 action head decoding speedup，`2.8×` 是 end-to-end system latency cut；若写 headline，需要明确这两个数字不是同一口径。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_17850_ProbeFlow.pdf]]，`MetaWorld 主结果`。
- `LIBERO 主结果` 这一层应单独承载 `LIBERO 主结果` 相关的 benchmark / metric / operating point。 这里收口为：LIBERO 主结果：[[raw/2603_17850_ProbeFlow.pdf]] 第 6-7 页 Table II、Fig. 3。这里对应 average `4.5` steps、`32.7 ms` flow solver latency、在 semantic bottleneck 上自动升到约 `14.1` steps 以恢复 success rate 的结果。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_17850_ProbeFlow.pdf]]，`LIBERO 主结果`。
- `real-world 与阈值敏感性` 这一层应单独承载 `real-world 与阈值敏感性` 相关的 benchmark / metric / operating point。 这里收口为：real-world 与阈值敏感性：[[raw/2603_17850_ProbeFlow.pdf]] 第 7-9 页 Table V、Fig. 4-5。这里可回查 real-world pick-and-place 的 latency reduction、probe horizon `Δt_probe` 的敏感性，以及 training-free cross-domain deployability 的边界。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_17850_ProbeFlow.pdf]]，`real-world 与阈值敏感性`。

## 不可混写项
- `14.8×` 是 action head decoding speedup，`2.8×` 是 end-to-end system latency cut；若写 headline，需要明确这两个数字不是同一口径。
- `MetaWorld` 与 `LIBERO` 呈现不同难度结构：前者更像短时程动作瓶颈，后者有更多 long-horizon semantic bottleneck；后续不能把两组结果压成单一无条件结论。
- `ProbeFlow` 是 training-free inference framework，不是新 action head；后续 taxonomy 需要避免把它误写成新的 flow policy architecture。

## 影响页面
- [[wiki/papers/2603_17850_ProbeFlow.md|2603_17850_ProbeFlow]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
