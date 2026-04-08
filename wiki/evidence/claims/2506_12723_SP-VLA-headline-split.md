# 2506_12723_SP-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2506_12723_SP-VLA.md|2506_12723_SP-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：论文同时使用了多种 acceleration 口径：`1.5× lossless acceleration`、`1.5× with <3% drop`、`2.4× in SimplerEnv`、`2.2× latency/frequency improvement`、`1.4× in LIBERO`；仍需固定主口径，避免把不同设定混成同一句 headline。

## Evidence
- 作者提出 `SP-VLA`，并声称在 `LIBERO` 上可实现 `1.5× lossless acceleration`，在 `SimplerEnv` 上可达 `2.4×` 加速并获得最高 `6%` 的平均性能提升；同时在 RTX 4090 上，推理频率/时延相对基线分别提升 `1.4×`（LIBERO）与 `2.2×`（SimplerEnv）。这些 headline 来自不同 benchmark、不同 speedup 口径与不同 operating point，更稳的写法是：**SP-VLA 通过联合调度和 dual-aware pruning，在 LIBERO 与 SimplerEnv 上取得一组 benchmark-dependent 的速度-性能 trade-off。** 来源：[[raw/2506_12723_SP-VLA.pdf]]，第 1 页摘要；第 7-9 页 Tables 1、2、4。
- 补充证据命题：核心主张是：VLA 推理中同时存在时间冗余和空间冗余，因此可以把“模型调度”和“token 剪枝”联合起来做，而不是把它们分开处理。具体来说，先区分 `deliberative` 与 `intuitive` 动作，在高精度 VLA 与轻量 action generator 之间做协同调度；再对被调用的 VLA 分支进行 `spatio-semantic dual-aware` token pruning。 来源：[[raw/2506_12723_SP-VLA.pdf]]，主思路概览：[[raw/2506_12723_SP-VLA.pdf]] 第 2 页 Fig. 1。这里展示 `intuitive` 动作走轻量 generator、`deliberative` 动作走 VLA、且 VLA 分支再做 token pruning 的整体流程。
- 主证据锚点 1：来源：[[raw/2506_12723_SP-VLA.pdf]]，摘要与总体问题设定：[[raw/2506_12723_SP-VLA.pdf]] 第 1 页摘要。这里给出联合调度 + 剪枝的总命题，以及 `1.5× / 2.4× / 6% / 2.2× / 1.4×` 的 headline 结果。
- 主证据锚点 2：来源：[[raw/2506_12723_SP-VLA.pdf]]，主思路概览：[[raw/2506_12723_SP-VLA.pdf]] 第 2 页 Fig. 1。这里展示 `intuitive` 动作走轻量 generator、`deliberative` 动作走 VLA、且 VLA 分支再做 token pruning 的整体流程。
- 主证据锚点 3：来源：[[raw/2506_12723_SP-VLA.pdf]]，方法细节：[[raw/2506_12723_SP-VLA.pdf]] 第 5 页 Fig. 3 与相邻方法章节。这里定义 action-aware scheduling、Ridge Regression action generator、以及 `spatio-semantic dual-aware` pruning 的细节。

## Table / Metric Anchors
- 主结果：[[raw/2506_12723_SP-VLA.pdf]] 第 7-8 页 Table 1 与 Table 2。这里分别对应 `LIBERO` 与 `SimplerEnv` 的主实验结果，也是 `lossless acceleration`、`2.4×` 和 `6%` 等结论的核心证据位置。
- 延迟与频率：[[raw/2506_12723_SP-VLA.pdf]] 第 9 页 Table 4。这里是 RTX 4090 上的 latency / frequency 指标，支撑 `2.2×` 与 `1.4×` 的主表述。

## Table / Metric Split
- `主结果` 这一层应单独承载 `主结果` 相关的 benchmark / metric / operating point。 这里收口为：作者提出 `SP-VLA`，并声称在 `LIBERO` 上可实现 `1.5× lossless acceleration`，在 `SimplerEnv` 上可达 `2.4×` 加速并获得最高 `6%` 的平均性能提升；同时在 RTX 4090 上，推理频率/时延相对基线分别提升 `1.4×`（LIBERO）与 `2.2×`（SimplerEnv）。这些 headline 来自不同 benchmark、不同 speedup 口径与不同 operating point，更稳的写法是：**SP-VLA 通过联合调度和 dual-aware pruning，在 LIBERO 与 SimplerEnv 上取得一组 benchmark-dependent 的速度-性能 trade-off。** 来源：[[raw/2506_12723_SP-VLA.pdf]]，第 1 页摘要；第 7-9 页 Tables 1、2、4。；主结果：[[raw/2506_12723_SP-VLA.pdf]] 第 7-8 页 Table 1 与 Table 2。这里分别对应 `LIBERO` 与 `SimplerEnv` 的主实验结果，也是 `lossless acceleration`、`2.4×` 和 `6%` 等结论的核心证据位置。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2506_12723_SP-VLA.pdf]]，`主结果`。
- `延迟与频率` 这一层应单独承载 `延迟与频率` 相关的 benchmark / metric / operating point。 这里收口为：作者提出 `SP-VLA`，并声称在 `LIBERO` 上可实现 `1.5× lossless acceleration`，在 `SimplerEnv` 上可达 `2.4×` 加速并获得最高 `6%` 的平均性能提升；同时在 RTX 4090 上，推理频率/时延相对基线分别提升 `1.4×`（LIBERO）与 `2.2×`（SimplerEnv）。这些 headline 来自不同 benchmark、不同 speedup 口径与不同 operating point，更稳的写法是：**SP-VLA 通过联合调度和 dual-aware pruning，在 LIBERO 与 SimplerEnv 上取得一组 benchmark-dependent 的速度-性能 trade-off。** 来源：[[raw/2506_12723_SP-VLA.pdf]]，第 1 页摘要；第 7-9 页 Tables 1、2、4。；延迟与频率：[[raw/2506_12723_SP-VLA.pdf]] 第 9 页 Table 4。这里是 RTX 4090 上的 latency / frequency 指标，支撑 `2.2×` 与 `1.4×` 的主表述。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2506_12723_SP-VLA.pdf]]，`延迟与频率`。

## 不可混写项
- 论文同时使用了多种 acceleration 口径：`1.5× lossless acceleration`、`1.5× with <3% drop`、`2.4× in SimplerEnv`、`2.2× latency/frequency improvement`、`1.4× in LIBERO`；仍需固定主口径，避免把不同设定混成同一句 headline。
- `lossless acceleration` 更准确地说是 `LIBERO` 上某组配置的结果；论文自己也给出 `1.5×` 但伴随约 `3%` 精度下降的配置，因此后续不能把“1.5×”一概表述成无损。
- `SimplerEnv` 主结果里正文有 `2× speedup` 的总结性表述，而摘要/结论与表格上限又写到 `2.4×`；仍应明确默认是写“最高可达 2.4×”还是“主结果约 2×-2.4×”。

## 影响页面
- [[wiki/papers/2506_12723_SP-VLA.md|2506_12723_SP-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
