# 2511_16233_FT-NCFM-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2511_16233_FT-NCFM.md|2511_16233_FT-NCFM]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`5%`、`85-90%`、`80%+` 目前仍是 bundled headline，仍需分别落到具体 benchmark、metric 和 training-cost 表格上，尤其要把 CALVIN `Avg. Len` 和 Meta-World / LIBERO 的 success rate 分开。

## Evidence
- 核心证据命题：FT-NCFM 将自己定位为一种 data-centric 的 VLA 效率优化框架，而不是模型压缩或 policy distillation 的变体。论文的核心主张是：当前 VLA 的效率瓶颈不只在模型结构，也在大规模训练数据本身存在大量冗余、噪声和价值不均；因此，与其继续围绕模型参数做压缩或教师-学生蒸馏，不如直接在数据层生成一个更高信息密度、可重用的 synthetic coreset。为此，FT-NCFM 先用 FT engine 对样本做 influence-aware 价值评估，再用受这些权重引导的 NCFM 对抗式蒸馏生成 synthetic coreset。 来源：[[raw/2511_16233_FT-NCFM.pdf]]，**Abstract / introduction**：最清楚地给出论文的总 framing：数据冗余是根因，FT-NCFM 是 data-level generative distillation，而不是 model-centric optimization。
- 补充证据命题：作者 headline 需要拆开理解：`5%` synthetic data、`85-90%` performance 和 `80%+` 训练时间缩减来自不同 benchmark 与不同比较口径。CALVIN 上主指标是 `Avg. Len`，Meta-World 与 LIBERO 上主指标是 success rate，而训练时间缩减主要来自 CALVIN 的 paradigm comparison 与 LIBERO 的 cost-benefit 分析。更稳的写法是：**高价值 synthetic coreset 能在多个 benchmark 上用显著更少的数据和训练成本逼近 full-data / SOTA baseline，但不能把这些比例压成一组统一、场景无关的固定数字。** 来源：[[raw/2511_16233_FT-NCFM.pdf]]，**Figure 1 (p.2)**：FT-NCFM 整体三阶段 pipeline 的第一锚点，也是理解 FT engine 与 influence-guided NCFM 如何衔接的最好入口。
- 主证据锚点 1：来源：[[raw/2511_16233_FT-NCFM.pdf]]，**Abstract / introduction**：最清楚地给出论文的总 framing：数据冗余是根因，FT-NCFM 是 data-level generative distillation，而不是 model-centric optimization。
- 主证据锚点 2：来源：[[raw/2511_16233_FT-NCFM.pdf]]，**Figure 1 (p.2)**：FT-NCFM 整体三阶段 pipeline 的第一锚点，也是理解 FT engine 与 influence-guided NCFM 如何衔接的最好入口。
- 主证据锚点 3：来源：[[raw/2511_16233_FT-NCFM.pdf]]，**Table 1 (p.6)**：CALVIN ABC→D 的主结果锚点，用来核对不同 data ratio 下的 zero-shot long-horizon performance；这里的主指标是 `Avg. Len`，不是 success rate。

## Table / Metric Anchors
- **Table 1 (p.6)**：CALVIN ABC→D 的主结果锚点，用来核对不同 data ratio 下的 zero-shot long-horizon performance；这里的主指标是 `Avg. Len`，不是 success rate。
- **Table 2 (p.6)**：Meta-World 多任务 success rate 锚点；这是“5% data 仍保留较强多任务性能”的第二条独立证据。
- **Table 3 (p.7)**：LIBERO success rate 锚点；`10% data` 下接近 SpatialVLA 的 headline 主要来自这里，而不是 `5%` headline。
- **Table 4 (p.7)**：与 model-centric / coreset baselines 的 paradigm comparison；训练时间显著下降与“约 1/7 资源消耗”的说法应优先回到这里核对。
- **Table 5 (p.7)**：LIBERO 上 preprocessing + policy training 的 cost-benefit 分析；`20.3% of standard OpenVLA training time` 这类表述主要来自这里。

## Table / Metric Split
- `Table 1` 的主指标是 **CALVIN Avg. Len**，而不是 success rate：`FT-NCFM` 在 `5%` data 时达到 `3.11`，在 `10%` data 时达到 `3.47`；这张表支撑的是 long-horizon CALVIN performance scaling，不能拿去和 Meta-World / LIBERO 的 success rate 一起写成统一 `85-90%`。来源：[[raw/2511_16233_FT-NCFM.pdf]]，第 6 页，Table 1。
- `Table 2` 对应 **Meta-World Avg. SR**：`FT-NCFM` 在 `5%` / `10%` data 下分别达到 `50.5` / `54.5`，对照 `GR-1` 的 `57.4`；这张表支撑的是 multi-task success-rate scaling，而不是 long-horizon chain-length。来源：[[raw/2511_16233_FT-NCFM.pdf]]，第 6 页，Table 2。
- `Table 3` 对应 **LIBERO success rate split**：`FT-NCFM` 在 `10%` data 时达到 `Avg. 74.2`，其中 `Long = 56.6`；这张表比 bundled headline 更适合支撑“接近 SpatialVLA / 在 long-horizon 上保持竞争力”的表述。来源：[[raw/2511_16233_FT-NCFM.pdf]]，第 7 页，Table 3。
- `Table 4 / Table 5` 对应 **训练成本**：Table 4 是 CALVIN 上与 model-centric / coreset baselines 的 paradigm comparison，Table 5 是 LIBERO 上的 one-time preprocessing + policy training cost-benefit；因此 `80%+ time reduction`、`1/7 resource` 和 `20.3% of OpenVLA training time` 这些说法不能互相替代。来源：[[raw/2511_16233_FT-NCFM.pdf]]，第 7 页，Table 4、Table 5。
- **Table 6 (p.7)**：CALVIN 上关键组件消融的第一锚点，用来判断 FT engine 与 contrastive verification 是否真的是框架成功的关键。

## 不可混写项
- `5%`、`85-90%`、`80%+` 目前仍是 bundled headline，仍需分别落到具体 benchmark、metric 和 training-cost 表格上，尤其要把 CALVIN `Avg. Len` 和 Meta-World / LIBERO 的 success rate 分开。
- 论文把 FT engine、contrastive verification 和 influence-guided NCFM 一起包装成整体框架；后续 evidence 层可能需要拆开“价值评估贡献”和“生成式蒸馏贡献”。
- 论文强调 synthetic coreset 是 model-agnostic reusable data asset，但当前直接证据主要来自固定 VLA 架构设置；仍需区分“理论上的模型无关性”与“已直接验证的迁移范围”。

## 影响页面
- [[wiki/papers/2511_16233_FT-NCFM.md|2511_16233_FT-NCFM]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
