# 2602_15397_ActionCodec-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_15397_ActionCodec.md|2602_15397_ActionCodec]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`95.5%` 是 `SmolVLM2-2.2B + ActionCodec` 在**无 robotics pre-training**条件下的 headline；`97.4%` 则显式依赖 `advanced architectural enhancements`，后续不能把它写成纯 tokenizer 单因素结果。

## Evidence
- 核心证据命题：这篇论文要解决的是：当前离散动作 tokenization 的设计通常围绕 reconstruction fidelity 展开，但它是否真正有利于 `autoregressive VLA` 的优化、训练效率与泛化，缺少系统回答；因此作者把问题改写为“什么样的 action tokenizer 才适合 VLA optimization”。 来源：[[raw/2602_15397_ActionCodec.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 补充证据命题：作者从 `information-theoretic` 视角提出四条设计原则：更高的 temporal token overlap、更低的 vocabulary redundancy、更强的 multimodal mutual information、以及更高的 token independence；并据此提出 `ActionCodec`，把 action tokenizer 从“重建模块”变成直接服务 VLA 训练动态的设计对象。 来源：[[raw/2602_15397_ActionCodec.pdf]]，论文问题设定、四条设计原则的总览、`95.5% / 97.4%` headline，以及 `5K steps -> 89.5%` 的训练效率主张都在这里。
- 主证据锚点 1：来源：[[raw/2602_15397_ActionCodec.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 主证据锚点 2：来源：[[raw/2602_15397_ActionCodec.pdf]]，论文问题设定、四条设计原则的总览、`95.5% / 97.4%` headline，以及 `5K steps -> 89.5%` 的训练效率主张都在这里。
- 主证据锚点 3：来源：[[raw/2602_15397_ActionCodec.pdf]]，`PDF p.2-4` Introduction + Sec. 4：

## Table / Metric Anchors
- `PDF p.6-7` Table 1：
  - `LIBERO` benchmark 主结果、`95.5%`、`97.4%`、不同 model size / architectural variant 的主表结果应回这里核定。
- `PDF p.10+` Fig. 10 / Table 4 / cross-embodiment discussion：
  - cross-embodiment transfer、pre-training / co-training、以及 real-world robotic deployment 相关证据可从这里继续补。

## Table / Metric Split
- ``PDF p.6-7` Table 1` 这一层支撑 ``PDF p.6-7` Table 1` 对应的 benchmark / metric / operating point。 - `LIBERO` benchmark 主结果、`95.5%`、`97.4%`、不同 model size / architectural variant 的主表结果应回这里核定。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2602_15397_ActionCodec.pdf]]，``PDF p.6-7` Table 1`。
- ``PDF p.10+` Fig. 10 / Table 4 / cross-embodiment discussion` 这一层支撑 ``PDF p.10+` Fig. 10 / Table 4 / cross-embodiment discussion` 对应的 benchmark / metric / operating point。 - cross-embodiment transfer、pre-training / co-training、以及 real-world robotic deployment 相关证据可从这里继续补。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2602_15397_ActionCodec.pdf]]，``PDF p.10+` Fig. 10 / Table 4 / cross-embodiment discussion`。

## 不可混写项
- `95.5%` 是 `SmolVLM2-2.2B + ActionCodec` 在**无 robotics pre-training**条件下的 headline；`97.4%` 则显式依赖 `advanced architectural enhancements`，后续不能把它写成纯 tokenizer 单因素结果。
- “without robotics pre-training” 不等于“没有进一步的 robotics fine-tuning / benchmark-specific adaptation”；引用时要避免把这一点过度外推。
- `89.5% @ 5K steps` 与 `FAST 38.6%` 更像训练效率 headline，建立在特定 `LIBERO-Goal` 与 `SmolVLM2` 设置上；若后续写成普适训练加速结论，需要保留实验范围 caveat。

## 影响页面
- [[wiki/papers/2602_15397_ActionCodec.md|2602_15397_ActionCodec]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
