# 2509_04996_FLOWER-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2509_04996_FLOWER.md|2509_04996_FLOWER]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：论文最强的是一个 bundled systems claim；后续 `L2` 需要把架构效率（`950M`、`200 GPU hours`、memory / throughput）与 benchmark 竞争力（`4.53`、LIBERO / SIMPLER / real-world 等）分开补证。

## Evidence
- 核心证据命题：这篇论文把 **FLOWER** 定位成一个高效、开放、参数规模低于 `1B` 的 diffusion / flow 风格 VLA，试图在不承担大模型预训练与部署成本的前提下，恢复大多数更大 VLA 的性能。 来源：[[raw/2509_04996_FLOWER.pdf]]，**Abstract / Introduction**：用于锚定 `950M`、`200 H100 GPU hours`、`190 tasks / 10 benchmarks`、`4.53 CALVIN ABC` 等系统级 headline。
- 补充证据命题：核心主张不是简单“把 backbone 缩小”，而是把容量从最深层的 VLM backbone 重新分配到更关键的动作生成模块。具体做法是把 **intermediate-modality fusion** 和 **action-specific Global-AdaLN conditioning** 结合起来，构成一个约 `950M` 参数的系统。作者声称该模型可在 `200 H100 GPU hours` 内完成预训练，覆盖 `10` 个 benchmark 的 `190 tasks`，并在 CALVIN ABC 上达到新的 `4.53` 结果，同时在更宽的 benchmark 集上保持与更大 VLA 竞争的能力。 来源：[[raw/2509_04996_FLOWER.pdf]]，**Figure 1 (p.2)**：最适合回收“为什么 intermediate fusion 有效”以及“小模型 + 强性能”的总体 framing。
- 主证据锚点 1：来源：[[raw/2509_04996_FLOWER.pdf]]，**Abstract / Introduction**：用于锚定 `950M`、`200 H100 GPU hours`、`190 tasks / 10 benchmarks`、`4.53 CALVIN ABC` 等系统级 headline。
- 主证据锚点 2：来源：[[raw/2509_04996_FLOWER.pdf]]，**Figure 1 (p.2)**：最适合回收“为什么 intermediate fusion 有效”以及“小模型 + 强性能”的总体 framing。
- 主证据锚点 3：来源：[[raw/2509_04996_FLOWER.pdf]]，**Figure 2 (p.4)**：FLOWER 主架构入口，用于锚定中间层特征注入和 action-space conditioning。

## Table / Metric Anchors
- **Table 1 / Table 2 (p.6)**：用于锚定 intermediate fusion 和 VLM pruning 的核心证据，尤其是与 early/late fusion 的直接比较。
- **Table 4 (p.8)**：主效率锚点，用于锚定 `311 Hz` throughput 与 memory footprint。
- **Table 10 (p.17)**：CALVIN `4.53` headline 的主锚点。
- **Table 11 / Table 12 (p.19) + Table 13 (p.20)**：Bridge、Google Robot、LIBERO 等多 benchmark 表现的主锚点，用于锚定“competitive across 10 benchmarks”这一更宽的系统性主张。

## Table / Metric Split
- `**Table 1 / Table 2 (p.6)**` 这一层应单独承载 `**Table 1 / Table 2 (p.6)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2509_04996_FLOWER.pdf]]，`**Table 1 / Table 2 (p.6)**`。
- `**Table 4 (p.8)**` 这一层应单独承载 `**Table 4 (p.8)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2509_04996_FLOWER.pdf]]，`**Table 4 (p.8)**`。
- `**Table 10 (p.17)**` 这一层应单独承载 `**Table 10 (p.17)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2509_04996_FLOWER.pdf]]，`**Table 10 (p.17)**`。
- `**Table 11 / Table 12 (p.19) + Table 13 (p.20)**` 这一层应单独承载 `**Table 11 / Table 12 (p.19) + Table 13 (p.20)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2509_04996_FLOWER.pdf]]，`**Table 11 / Table 12 (p.19) + Table 13 (p.20)**`。

## 不可混写项
- 论文最强的是一个 bundled systems claim；后续 `L2` 需要把架构效率（`950M`、`200 GPU hours`、memory / throughput）与 benchmark 竞争力（`4.53`、LIBERO / SIMPLER / real-world 等）分开补证。
- `FLOWER` 存在多种变体与 ablation 形态（fusion strategy、不同 pruning 方案、更小 backbone、late-fusion 对照等）；后续 evidence work 不能把它们压成一个无条件性能结论。
- “competitive with bigger VLAs across 190 tasks in 10 benchmarks” 需要后续按 benchmark 逐一拆开，因为有些表支持明显领先，有些更接近 competitive / second-best，而不是普遍压制。

## 影响页面
- [[wiki/papers/2509_04996_FLOWER.md|2509_04996_FLOWER]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
