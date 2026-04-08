# 2507_22424_Spec-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2507_22424_Spec-VLA.md|2507_22424_Spec-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`1.22×` 到 `1.42×` 的速度提升是 LIBERO 各 task suite 上的范围，不是单一无条件数值；引用时需要保留 benchmark-dependent caveat。

## Evidence
- 核心证据命题：这篇论文要解决的是：Vision-Language-Action (`VLA`) 模型的自回归 action-token 生成较慢，而直接套用通用 speculative decoding 往往收益有限，因为 VLA 的 action prediction 更难、greedy acceptance 过于严格。 来源：[[raw/2507_22424_Spec-VLA.pdf]]，`PDF p.1` Abstract + Fig. 1：
- 补充证据命题：作者提出 `Spec-VLA`，把 speculative decoding 引入 VLA 推理，并在标准 draft-and-verify 框架上加入面向 action token 的 `relaxed acceptance` 机制：只要候选 token 与验证模型输出在相对距离上足够接近，就允许接受，而不再要求严格相等。 来源：[[raw/2507_22424_Spec-VLA.pdf]]，问题设定、`relaxed acceptance` 的核心动机，以及 `1.42× speedup` / `44% acceptance length improvement` 的 headline 都在这里。
- 主证据锚点 1：来源：[[raw/2507_22424_Spec-VLA.pdf]]，`PDF p.1` Abstract + Fig. 1：
- 主证据锚点 2：来源：[[raw/2507_22424_Spec-VLA.pdf]]，问题设定、`relaxed acceptance` 的核心动机，以及 `1.42× speedup` / `44% acceptance length improvement` 的 headline 都在这里。
- 主证据锚点 3：来源：[[raw/2507_22424_Spec-VLA.pdf]]，`PDF p.2-4` Method / Fig. 2：

## Table / Metric Anchors
- `PDF p.5` Table 1：
  - LIBERO-Goal / Object / Spatial / Long 上的主结果在这里；AR baseline、普通 speculative decoding、以及 relaxed Spec-VLA 的 success rate、acceptance length、speedup 都在这里对照。
- `PDF p.7` Table 2 / Table 3：
  - acceptance length distribution 和各 token position 的平均 acceptance length 分析在这里，用于锚定“为什么 relaxed acceptance 有效”的局部证据。

## Table / Metric Split
- ``PDF p.5` Table 1` 这一层支撑 ``PDF p.5` Table 1` 对应的 benchmark / metric / operating point。 - LIBERO-Goal / Object / Spatial / Long 上的主结果在这里；AR baseline、普通 speculative decoding、以及 relaxed Spec-VLA 的 success rate、acceptance length、speedup 都在这里对照。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2507_22424_Spec-VLA.pdf]]，``PDF p.5` Table 1`。
- ``PDF p.7` Table 2 / Table 3` 这一层支撑 ``PDF p.7` Table 2 / Table 3` 对应的 benchmark / metric / operating point。 - acceptance length distribution 和各 token position 的平均 acceptance length 分析在这里，当前对应“为什么 relaxed acceptance 有效”的局部证据。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2507_22424_Spec-VLA.pdf]]，``PDF p.7` Table 2 / Table 3`。

## 不可混写项
- `1.22×` 到 `1.42×` 的速度提升是 LIBERO 各 task suite 上的范围，不是单一无条件数值；引用时需要保留 benchmark-dependent caveat。
- “without compromising success rate” 更准确地说是：在主实验设置下 success rate 大体保持，但具体 suite 上仍有小幅波动；后续不能写成绝对无损。
- 论文的验证主要基于 OpenVLA-style 离散 action token 预测；若引用时要把结论推广到更一般的连续控制或不同 tokenization 方案，需要保留适用范围。

## 影响页面
- [[wiki/papers/2507_22424_Spec-VLA.md|2507_22424_Spec-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
