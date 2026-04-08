# 2603_17573_HeiSD-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_17573_HeiSD.md|2603_17573_HeiSD]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`2.45×`、`2.06×∼2.41×` 与 success rate 结果分别来自不同 benchmark 与部署设置，后续不能压成一个无条件的统一提速结论。

## Evidence
- 更稳的主张是：`HeiSD` 证明 retrieval-based SD 与 drafter-based SD 在 VLA 中具有互补性，且 retrieval-side accept/reject 机制若不做专门修复，就难以稳定进入 embodied deployment。来源：[[raw/2603_17573_HeiSD.pdf]]，第 1-3 页摘要、引言与 Fig. 1；第 6-8 页 Table 3、Table 4 与相关正文。
- 补充证据命题：核心主张是：针对 VLA 的多步推理轨迹，不同阶段适合不同类型的 speculative decoding；如果把 retrieval-based SD 与 drafter-based SD 按轨迹运动学特征进行混合使用，并补上 retrieval 侧的 verify-skip 与 sequence-wise relaxed acceptance，就能同时保留两类 SD 的优势，在较高 success rate 下获得更好的推理加速。 来源：[[raw/2603_17573_HeiSD.pdf]]，retrieval 分析与 hybrid 动机：[[raw/2603_17573_HeiSD.pdf]] 第 3-5 页 Fig. 2、Table 1、Table 2。这里说明 retrieval-only 在 `LIBERO` 上的能力边界、trajectory overlap 的观察，以及为何要把 retrieval-based SD 和 drafter-based SD 混合使用。
- 主证据锚点 1：来源：[[raw/2603_17573_HeiSD.pdf]]，摘要与核心命题：[[raw/2603_17573_HeiSD.pdf]] 第 1-3 页摘要、引言与 Fig. 1。这里定义 hybrid SD 的总思路，以及 `2.45×` simulation / `2.06×∼2.41×` real-world 的 headline。
- 主证据锚点 2：来源：[[raw/2603_17573_HeiSD.pdf]]，retrieval 分析与 hybrid 动机：[[raw/2603_17573_HeiSD.pdf]] 第 3-5 页 Fig. 2、Table 1、Table 2。这里说明 retrieval-only 在 `LIBERO` 上的能力边界、trajectory overlap 的观察，以及为何要把 retrieval-based SD 和 drafter-based SD 混合使用。
- 主证据锚点 3：来源：[[raw/2603_17573_HeiSD.pdf]]，retrieval 优化机制：[[raw/2603_17573_HeiSD.pdf]] 第 5-6 页 Fig. 3、Fig. 4 与相邻正文。这里对应 `adaptive verify-skip` 与 `sequence-wise relaxed acceptance` 的具体作用和目标。

## Table / Metric Anchors
- retrieval 分析与 hybrid 动机：[[raw/2603_17573_HeiSD.pdf]] 第 3-5 页 Fig. 2、Table 1、Table 2。这里说明 retrieval-only 在 `LIBERO` 上的能力边界、trajectory overlap 的观察，以及为何要把 retrieval-based SD 和 drafter-based SD 混合使用。
- simulation 与 real-world 主结果：[[raw/2603_17573_HeiSD.pdf]] 第 7-8 页 Table 3、Table 4、Fig. 8。这里可回查 `LIBERO` 四个 suite 的 speedup / success rate，以及 real-world `2.06×∼2.41×` 与 `1.2%∼3.9%` 的 minor SR loss 口径。

## Table / Metric Split
- `retrieval 分析与 hybrid 动机` 这一层应单独承载 `retrieval 分析与 hybrid 动机` 相关的 benchmark / metric / operating point。 这里收口为：retrieval 分析与 hybrid 动机：[[raw/2603_17573_HeiSD.pdf]] 第 3-5 页 Fig. 2、Table 1、Table 2。这里说明 retrieval-only 在 `LIBERO` 上的能力边界、trajectory overlap 的观察，以及为何要把 retrieval-based SD 和 drafter-based SD 混合使用。；simulation 与 real-world 主结果：[[raw/2603_17573_HeiSD.pdf]] 第 7-8 页 Table 3、Table 4、Fig. 8。这里可回查 `LIBERO` 四个 suite 的 speedup / success rate，以及 real-world `2.06×∼2.41×` 与 `1.2%∼3.9%` 的 minor SR loss 口径。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_17573_HeiSD.pdf]]，`retrieval 分析与 hybrid 动机`。
- `simulation 与 real-world 主结果` 这一层应单独承载 `simulation 与 real-world 主结果` 相关的 benchmark / metric / operating point。 这里收口为：摘要与核心命题：[[raw/2603_17573_HeiSD.pdf]] 第 1-3 页摘要、引言与 Fig. 1。这里定义 hybrid SD 的总思路，以及 `2.45×` simulation / `2.06×∼2.41×` real-world 的 headline。；retrieval 分析与 hybrid 动机：[[raw/2603_17573_HeiSD.pdf]] 第 3-5 页 Fig. 2、Table 1、Table 2。这里说明 retrieval-only 在 `LIBERO` 上的能力边界、trajectory overlap 的观察，以及为何要把 retrieval-based SD 和 drafter-based SD 混合使用。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2603_17573_HeiSD.pdf]]，`simulation 与 real-world 主结果`。

## 不可混写项
- `2.45×`、`2.06×∼2.41×` 与 success rate 结果分别来自不同 benchmark 与部署设置，后续不能压成一个无条件的统一提速结论。
- 这篇强调的是 runtime decoding framework，不是新的 VLA backbone / policy；后续 taxonomy 需要避免把它误写成 policy architecture 创新。
- 论文同时使用 simulation `LIBERO` 与 real-world tabletop tasks 验证，但 real-world 结果是基于特定 fine-tuned model 与任务集合，不能泛化成所有 VLA/任务上都能达到相同 speedup。

## 影响页面
- [[wiki/papers/2603_17573_HeiSD.md|2603_17573_HeiSD]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
