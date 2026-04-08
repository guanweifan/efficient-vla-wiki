# 2406_04339_RoboMamba-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2406_04339_RoboMamba.md|2406_04339_RoboMamba]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：“**3 times faster than existing VLA models**”在 Abstract 中是泛指，后文又出现“**7 times faster** than LLaMA-AdapterV2 and ManipLLM”。仍需在 `L2` 明确不同 speed claim 对应的 baseline、指标和实验位置。

## Evidence
- 这篇论文提出 **RoboMamba**，试图同时解决两类问题：现有 robotic VLA 的复杂任务推理能力不足，以及基于 attention 的 VLA 在 fine-tuning 和 inference 上计算成本过高。来源：[[raw/2406_04339_RoboMamba.pdf]]，第 1 页 Abstract。
- 核心主张是：把视觉编码器接到 **Mamba** 语言模型上，并把 manipulation 学习拆成“先获得视觉与机器人推理能力，再用极小 policy head 学动作”的两阶段流程，可以同时保留推理能力和效率。来源：[[raw/2406_04339_RoboMamba.pdf]]，第 1-2 页 Abstract、Fig. 1；第 4-6 页 Sec. 3.2-3.4、Fig. 2。
- 主证据锚点 1：来源：[[raw/2406_04339_RoboMamba.pdf]]，**Abstract**：第 1 页。可直接承载“问题定义 + headline claim + 3x faster + 0.1% parameters”。
- 主证据锚点 2：来源：[[raw/2406_04339_RoboMamba.pdf]]，**Fig. 1**：第 2 页。用于锚定证“control frequency / parameter budget / reasoning + manipulation overview”。
- 主证据锚点 3：来源：[[raw/2406_04339_RoboMamba.pdf]]，**Sec. 3.2 + Fig. 2**：第 4-5 页。用于锚定 architecture，包括 CLIP -> projector -> Mamba -> policy head 的连接方式。

## Table / Metric Anchors
- **Table 1 / Sec. 4.2**：第 8 页。用于锚定 reasoning benchmark，尤其是 RoboVQA BLEU-4 = 42.8。
- **Table 2 / Sec. 4.3**：第 8-9 页。用于锚定 manipulation success rate、seen/unseen 结果与相对 baseline 的效率对比。

## Table / Metric Split
- `**Table 1 / Sec. 4.2**` 这一层应单独承载 `**Table 1 / Sec. 4.2**` 相关的 benchmark / metric / operating point。 这一层对应 reasoning benchmark，尤其是 RoboVQA BLEU-4 = 42.8。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2406_04339_RoboMamba.pdf]]，`**Table 1 / Sec. 4.2**`。
- `**Table 2 / Sec. 4.3**` 这一层应单独承载 `**Table 2 / Sec. 4.3**` 相关的 benchmark / metric / operating point。 这一层对应 manipulation success rate、seen/unseen 结果与相对 baseline 的效率对比。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2406_04339_RoboMamba.pdf]]，`**Table 2 / Sec. 4.3**`。

## 不可混写项
- “**3 times faster than existing VLA models**”在 Abstract 中是泛指，后文又出现“**7 times faster** than LLaMA-AdapterV2 and ManipLLM”。仍需在 `L2` 明确不同 speed claim 对应的 baseline、指标和实验位置。
- 文中同时出现 **2.7B / 2.8B / 3.2B** 等模型规模表述；仍需统一到底是在说 language model、full model 还是不同实验/叙事层的口径，也不要把 reasoning branch 的模型规模和 manipulation adaptation 的参数预算混写。
- “**SOTA manipulation performance in SAPIEN**”目前只作为论文主张记录，仍需在 Table 2 附近把具体比较对象和 seen/unseen 拆清楚，也不要把 reasoning benchmark 提升与 manipulation headline 自动绑定成同一结论。

## 影响页面
- [[wiki/papers/2406_04339_RoboMamba.md|2406_04339_RoboMamba]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
