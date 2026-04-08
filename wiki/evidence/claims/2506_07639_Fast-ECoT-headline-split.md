# 2506_07639_Fast-ECoT-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2506_07639_Fast-ECoT.md|2506_07639_Fast-ECoT]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：abstract 写 `up to 7.5× reduction in latency`，正文 real-world 段落又给出 `7.7×`（相对原始 ECoT）；引用时需要统一成“headline vs measured setting”。

## Evidence
- 核心证据命题：这篇论文要解决的是：Embodied Chain-of-Thought (`ECoT`) 虽然能提升 VLA 的成功率和可解释性，但每个时间步都要自回归地产生大量 reasoning token，延迟过高，不适合实时机器人控制。 来源：[[raw/2506_07639_Fast-ECoT.pdf]]，`PDF p.1` Abstract：
- 补充证据命题：作者提出 `Fast ECoT`，这是一个纯 inference-time acceleration 方法，不改模型结构、不重新训练，只通过三件事提速： 来源：[[raw/2506_07639_Fast-ECoT.pdf]]，Fast ECoT 的问题设定、三项核心机制、`up to 7.5× reduction in latency` 的 headline 都在这里。
- 主证据锚点 1：来源：[[raw/2506_07639_Fast-ECoT.pdf]]，`PDF p.1` Abstract：
- 主证据锚点 2：来源：[[raw/2506_07639_Fast-ECoT.pdf]]，Fast ECoT 的问题设定、三项核心机制、`up to 7.5× reduction in latency` 的 headline 都在这里。
- 主证据锚点 3：来源：[[raw/2506_07639_Fast-ECoT.pdf]]，`PDF p.3-5` Sec. IV + Fig. 2 / Fig. 3 / Fig. 4 / Fig. 6：

## Table / Metric Anchors
- `PDF p.5-6` Table I：
  - LIBERO simulation 主结果；`Fast ECoT = 80.0% avg`、`Fast ECoT (Async) = 77.5% avg`、以及各 baseline latency 对比都在这里。
- `PDF p.6` Table II：
  - real-world household tasks 的核心结果；`68.3% average`、`65.3% average`、`716 ± 529 ms` 等核心数据在这里。
- `PDF p.6-7` Table III：
  - AutoEval / BridgeData V2 上的外部 real-robot 结果入口，用于锚定“跨平台外部验证”证据。
- `PDF p.7` Table IV + Fig. 9：
  - reasoning update frequency 与 action faithfulness 的分析；若要写 reuse 频率或 async 对 faithfulness 的影响，应回这里。

## Table / Metric Split
- ``PDF p.5-6` Table I` 这一层支撑 ``PDF p.5-6` Table I` 对应的 benchmark / metric / operating point。 - LIBERO simulation 主结果；`Fast ECoT = 80.0% avg`、`Fast ECoT (Async) = 77.5% avg`、以及各 baseline latency 对比都在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2506_07639_Fast-ECoT.pdf]]，``PDF p.5-6` Table I`。
- ``PDF p.6` Table II` 这一层支撑 ``PDF p.6` Table II` 对应的 benchmark / metric / operating point。 - real-world household tasks 的核心结果；`68.3% average`、`65.3% average`、`716 ± 529 ms` 等核心数据在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2506_07639_Fast-ECoT.pdf]]，``PDF p.6` Table II`。
- ``PDF p.6-7` Table III` 这一层支撑 ``PDF p.6-7` Table III` 对应的 benchmark / metric / operating point。 - AutoEval / BridgeData V2 上的外部 real-robot 结果入口，当前对应“跨平台外部验证”证据。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2506_07639_Fast-ECoT.pdf]]，``PDF p.6-7` Table III`。
- ``PDF p.7` Table IV + Fig. 9` 这一层支撑 ``PDF p.7` Table IV + Fig. 9` 对应的 benchmark / metric / operating point。 - reasoning update frequency 与 action faithfulness 的分析；若要写 reuse 频率或 async 对 faithfulness 的影响，应回这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2506_07639_Fast-ECoT.pdf]]，``PDF p.7` Table IV + Fig. 9`。

## 不可混写项
- abstract 写 `up to 7.5× reduction in latency`，正文 real-world 段落又给出 `7.7×`（相对原始 ECoT）；引用时需要统一成“headline vs measured setting”。
- `Fast ECoT` 与 `Fast ECoT (Async)` 各自优势不同：前者平均成功率更高，后者 latency 最低；chief-editor 若写方法总结，需要决定默认突出哪一版。
- 方法强调 “no model changes or additional training”，但其评估建立在已有 ECoT 模型和特定 reasoning structure 上；若要泛化成更广泛 VLA acceleration 结论，需要保留这一适用范围 caveat。

## 影响页面
- [[wiki/papers/2506_07639_Fast-ECoT.md|2506_07639_Fast-ECoT]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
