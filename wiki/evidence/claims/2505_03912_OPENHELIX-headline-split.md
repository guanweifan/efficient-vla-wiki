# 2505_03912_OPENHELIX-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2505_03912_OPENHELIX.md|2505_03912_OPENHELIX]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：这篇论文同时是 survey、ablation report 和 prototype proposal；如归类，仍待主编决定它在 taxonomy 上更偏“method paper”还是“analysis/report”。

## Evidence
- 核心证据命题：这篇论文的直接目标不是单纯再提一个新 VLA SOTA，而是围绕 `dual-system VLA` 做三件事：短综述、受控经验分析、以及一个低成本开源 dual-system 原型 `Helix`。 来源：[[raw/2505_03912_OPENHELIX.pdf]]，`PDF p.1-3` Short Survey + Table 1：
- 补充证据命题：作者认为当前 dual-system VLA 在 `MLLM 选择`、`latent feature representation`、`MLLM / policy training strategy`、`integration strategy`、`asynchronous strategy` 等方面差异很大，缺少系统性的公平比较。 来源：[[raw/2505_03912_OPENHELIX.pdf]]，dual-system VLA 的定义、现有方法对比、以及 7 个关键设计维度都在这里，是理解本文问题设定的入口。
- 主证据锚点 1：来源：[[raw/2505_03912_OPENHELIX.pdf]]，`PDF p.1-3` Short Survey + Table 1：
- 主证据锚点 2：来源：[[raw/2505_03912_OPENHELIX.pdf]]，dual-system VLA 的定义、现有方法对比、以及 7 个关键设计维度都在这里，是理解本文问题设定的入口。
- 主证据锚点 3：来源：[[raw/2505_03912_OPENHELIX.pdf]]，`PDF p.4-8` Empirical Evaluations：

## Table / Metric Anchors
- `PDF p.1-3` Short Survey + Table 1：
  - dual-system VLA 的定义、现有方法对比、以及 7 个关键设计维度都在这里，是理解本文问题设定的入口。
- `PDF p.5-6` Table 3 / Table 4 / Table 6：
  - “预训练 policy 优于从零训练”“prompt tuning 可行”“projector pre-alignment 必要”这些结论的主证据位置。
- `PDF p.7-8` Figure 4 / Figure 5 / Table 7：
  - async inference 影响有限、现有 latent 对环境变化不敏感、auxiliary task 有帮助，这些分析的主证据在这里。
- `PDF p.8-10` Sec. 3 + Figure 7 + Table 8：
  - Helix 的具体框架、prompt tuning + auxiliary task + pretrained policy 的组合方式，以及最终 CALVIN / CALVIN-E 结果都在这里。

## Table / Metric Split
- ``PDF p.1-3` Short Survey + Table 1` 这一层支撑 ``PDF p.1-3` Short Survey + Table 1` 对应的 benchmark / metric / operating point。 - dual-system VLA 的定义、现有方法对比、以及 7 个关键设计维度都在这里，是理解本文问题设定的入口。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2505_03912_OPENHELIX.pdf]]，``PDF p.1-3` Short Survey + Table 1`。
- ``PDF p.5-6` Table 3 / Table 4 / Table 6` 这一层支撑 ``PDF p.5-6` Table 3 / Table 4 / Table 6` 对应的 benchmark / metric / operating point。 - “预训练 policy 优于从零训练”“prompt tuning 可行”“projector pre-alignment 必要”这些结论的主证据位置。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2505_03912_OPENHELIX.pdf]]，``PDF p.5-6` Table 3 / Table 4 / Table 6`。
- ``PDF p.7-8` Figure 4 / Figure 5 / Table 7` 这一层支撑 ``PDF p.7-8` Figure 4 / Figure 5 / Table 7` 对应的 benchmark / metric / operating point。 - async inference 影响有限、现有 latent 对环境变化不敏感、auxiliary task 有帮助，这些分析的主证据在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2505_03912_OPENHELIX.pdf]]，``PDF p.7-8` Figure 4 / Figure 5 / Table 7`。
- ``PDF p.8-10` Sec. 3 + Figure 7 + Table 8` 这一层支撑 ``PDF p.8-10` Sec. 3 + Figure 7 + Table 8` 对应的 benchmark / metric / operating point。 - Helix 的具体框架、prompt tuning + auxiliary task + pretrained policy 的组合方式，以及最终 CALVIN / CALVIN-E 结果都在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2505_03912_OPENHELIX.pdf]]，``PDF p.8-10` Sec. 3 + Figure 7 + Table 8`。

## Figure / Caption Anchors
- `Figure 1`：第 3 页。dual-system VLA 的七个设计维度与问题框架。
- `Figure 4 / Figure 5`：第 8 页。异步推理步数影响与 latent token 对环境变化不敏感的直接图证。
- `Figure 7`：第 9 页。Helix 的高层 `<ACT>` latent、auxiliary action prediction 与低层 policy 组合机制。
- `Discussion & Limitation`：第 10-11 页。`full open-source reproduction of Helix` 仍未实现的成熟度边界。

## Figure / Caption / Wording Split
- `Figure 1` 支撑的是 **dual-system VLA 的设计空间与分析框架**，不是 Helix 实验效果本身。后续引用 `MLLM selection`、`latent feature representation`、`asynchronous strategy` 这些设计维度时，应把它当作 survey / problem framing，而不是把它写成“作者已经实验验证七个维度都最优”的结果。来源：[[raw/2505_03912_OPENHELIX.pdf]]，第 3 页 Figure 1 与 Sec. 1.5。
- `Figure 4` 支撑的是 **异步步长从 1 到 60 的层级推理实验**。图注已经明确这里的 `step=60` 对应 “一个 MLLM 推理周期内动作 policy 最多执行 60 步”，也就是最典型的异步场景；因此 “asynchronous inference 影响有限” 的结论必须限定在该 CALVIN 层级推理实验，而不是泛化成 dual-system VLA 普遍规律。来源：[[raw/2505_03912_OPENHELIX.pdf]]，第 8 页 Figure 4 与配套分析段。
- `Figure 5` 支撑的是 **当前 latent token 更多编码文本指令与目标对象，而不是实时环境变化**。图注和正文都把结论落在 “latent embedding mainly summarizes the textual instruction” 这一点上，所以这页更适合支撑 “现有 latent feature 设计仍不敏感” 的 deficiency claim，而不是直接支撑某个性能数字。来源：[[raw/2505_03912_OPENHELIX.pdf]]，第 8 页 Figure 5 与后续两条分析结论。
- `Figure 7` 支撑的是 **Helix 的具体机制**：高层 `LLaVA-7B` 冻结参数，仅通过 `<ACT>` prompt token 输出 latent goal，并额外做 auxiliary action prediction；低层 `3D Diffuser Actor` 再结合 3D scene tokens 与 proprioception 做轨迹去噪。这里支持的是“simple yet effective prototype 的结构组成与低训练成本来源”，不是最终 benchmark headline。来源：[[raw/2505_03912_OPENHELIX.pdf]]，第 9 页 Figure 7 与 Sec. 3.1-3.2。
- `Discussion & Limitation` 明确写出 “there is still a long way to go before we achieve a full open-source reproduction of Helix”，并把 real robot deployment、humanoid deployment、fast downstream policy execution 都列为未完成目标。因此 `open-source dual-system VLA model` 只能理解为 **初版技术报告中的低成本 prototype**，不能写成已经成熟可复现的开放系统。来源：[[raw/2505_03912_OPENHELIX.pdf]]，第 10-11 页 Discussion & Limitation。

## 不可混写项
- 这篇论文同时是 survey、ablation report 和 prototype proposal；如归类，仍待主编决定它在 taxonomy 上更偏“method paper”还是“analysis/report”。
- `Helix` 的结果目前主要是 CALVIN / CALVIN-E 模拟环境，没有真实机器人闭环部署结果；若写“open-source dual-system VLA model”，需要保留这一成熟度 caveat。
- 作者在 Discussion 里明确写到距离 `full open-source reproduction of Helix` 还有较长距离，并承认部分 claim 尚未完全验证；这意味着本页里的 headline 结果应视为阶段性结果，不宜写成“已经完成的成熟系统”。

## 影响页面
- [[wiki/papers/2505_03912_OPENHELIX.md|2505_03912_OPENHELIX]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
