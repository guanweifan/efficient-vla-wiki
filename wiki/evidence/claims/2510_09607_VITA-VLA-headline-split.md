# 2510_09607_VITA-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2510_09607_VITA-VLA.md|2510_09607_VITA-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`CALVIN ABC-D` 的 headline 是 “first task success rate 92.5%”，但正文同时明确承认平均 task success length 低于 `Seer-Large`；后续不能只保留 92.5% 而丢掉这个 long-horizon caveat。

## Evidence
- 作者提出 `VITA-VLA`，以 `VITA-1.5-7B` 为 backbone，先做 action-space alignment，再做 selective fine-tuning。headline 结果需要拆开理解：`97.3%` 是 `LIBERO overall`，相对前 SOTA 提升 `11.8%`；`93.5%` 是 `LIBERO-LONG`，其中相对 `Seer-Large` 的直接提升是 `5.8%`，相对先前最佳 VLA 的提升才是 `24.5%`；`CALVIN ABC-D` 的 `92.5%` 只对应 first-task success，而不是平均 success length；real-world `82.0%` 则是五个任务平均，相对 teacher `Seer` 提升 `17%`。来源：[[raw/2510_09607_VITA-VLA.pdf]]，第 1-2 页摘要；第 7-9 页 Tables 1-4。
- 补充证据命题：核心主张是：可以在基本保留原始 VLM 结构的前提下，只增加 `action token` 与 `state encoder`，再通过一个两阶段蒸馏训练流程，把 pretrained small action model 的 action knowledge 转移到大 VLM 中，从而避免从头进行昂贵的 end-to-end VLA pretraining。 来源：[[raw/2510_09607_VITA-VLA.pdf]]，模型结构：[[raw/2510_09607_VITA-VLA.pdf]] 第 3-4 页 Fig. 2 与相邻章节。这里定义 `action token`、`state encoder`、`action mapper` 和复用的 pretrained action decoder 如何连接到 VLM。
- 主证据锚点 1：来源：[[raw/2510_09607_VITA-VLA.pdf]]，摘要与总体架构：[[raw/2510_09607_VITA-VLA.pdf]] 第 1-2 页摘要与 Fig. 1。这里给出“distill action expert into VLM”的总命题，以及 `97.3 / 93.5 / 92.5 / 82.0` 的 headline 结果。
- 主证据锚点 2：来源：[[raw/2510_09607_VITA-VLA.pdf]]，模型结构：[[raw/2510_09607_VITA-VLA.pdf]] 第 3-4 页 Fig. 2 与相邻章节。这里定义 `action token`、`state encoder`、`action mapper` 和复用的 pretrained action decoder 如何连接到 VLM。
- 主证据锚点 3：来源：[[raw/2510_09607_VITA-VLA.pdf]]，两阶段训练：[[raw/2510_09607_VITA-VLA.pdf]] 第 4-6 页方法章节与 Fig. 3。这里分别是 Stage 1 alignment 和 Stage 2 selective fine-tuning 的细节。

## Table / Metric Anchors
- **Table 1 (CALVIN ABC→D)**：[[raw/2510_09607_VITA-VLA.pdf]] 第 7 页。这里给出 `CALVIN` 的 `task-1 ... task-5` success 与 `Avg.Len`，用于区分 `92.5% first-task success` 和 `3.18 average task success length`。
- **Table 2 (LIBERO)**：[[raw/2510_09607_VITA-VLA.pdf]] 第 7 页。这里给出 `SPATIAL / OBJECT / GOAL / LONG / Average` 五列，是 `97.3% overall` 与 `93.5% LONG` 的主锚点。
- **Table 3 (LIBERO-LONG per-task)**：[[raw/2510_09607_VITA-VLA.pdf]] 第 7-8 页。这里给出 `Avg.Success` 与 10 个 task 的逐项结果，用于区分 `93.5 avg`、`100/95/80/75/90` 等 task-level operating point。
- **Table 4 (real-world)**：[[raw/2510_09607_VITA-VLA.pdf]] 第 8-9 页。这里给出 `Close Drawer / Stack Cups / Stack Blocks / Pick Place Sponge / Pick Place Block / Avg.Score` 六列，是 `82.0` real-world average 的主锚点。

## Table / Metric Split
- `Table 1 | CALVIN ABC→D`：`VITA-VLA(two-stage)` 的 headline 不是一个统一的 “92.5% on CALVIN”，而是 `Task 1 = 92.5`、`Task 2 = 77.1`、`Task 3 = 61.0`、`Task 4 = 49.2`、`Task 5 = 38.2`，`Avg.Len = 3.18`；对照 `Seer-large`，它在 `Task 1` 只有 `88.4`，但 `Avg.Len = 3.76`。因此 `92.5` 只能表述为 first-task success，不能写成 long-horizon chain length 全面领先。来源：[[raw/2510_09607_VITA-VLA.pdf]]，第 7 页，Table 1。
- `Table 2 | LIBERO overall`：`VITA-VLA(two-stage)` 在 `SPATIAL / OBJECT / GOAL / LONG / Average` 五列分别是 `98.0 / 99.8 / 97.9 / 93.5 / 97.3`；这里支撑的是 `97.3%` overall 与 `93.5%` LONG column，不应与 `CALVIN` 的 `92.5 first-task` 或 real-world `82.0` 混成一个总 headline。来源：[[raw/2510_09607_VITA-VLA.pdf]]，第 7 页，Table 2。
- `Table 3 | LIBERO-LONG per-task`：`VITA-VLA(two-stage)` 的 `Avg.Success = 93.5`，10 个 task 分别是 `100 / 100 / 100 / 100 / 100 / 95 / 95 / 80 / 75 / 90`；与 `Seer-large` 的 `87.7` 相比，直接增益是 `+5.8`，而不是常被 bundled 成的 `+24.5`。`+24.5` 只适用于 Table 2 的 `LONG` 列相对先前 VLA best (`69.0`) 的对比。来源：[[raw/2510_09607_VITA-VLA.pdf]]，第 7-8 页，Table 3。
- `Table 4 | real-world`：`VITA-VLA(two-stage)` 在 `Close Drawer / Stack Cups / Stack Blocks / Pick Place Sponge / Pick Place Block` 上分别为 `97.5 / 52.5 / 80.0 / 87.5 / 92.5`，`Avg.Score = 82.0`；对照 `Seer` 的 `65.0` 与 `VITA-VLA(only-ft)` 的 `79.0`，这里支撑的是 real-world success 平均表现，不是推理频率优势。部署速度的 `0.15s (~6-7Hz)` 需要回附录单独表述。来源：[[raw/2510_09607_VITA-VLA.pdf]]，第 8-9 页，Table 4。

## 不可混写项
- `CALVIN ABC-D` 的 headline 是 “first task success rate 92.5%”，但正文同时明确承认平均 task success length 低于 `Seer-Large`；后续不能只保留 92.5% 而丢掉这个 long-horizon caveat。
- `97.3%` 与 `93.5%` 分别对应 `LIBERO` overall 和 `LIBERO-LONG`；其中 `24.5% improvement` 具体是相对之前 `LIBERO-LONG` 最佳 VLA 结果，不应写成对所有基线统一提升 24.5%。
- 论文核心卖点是“更高训练效率 / 更低训练成本”，但正文主要通过两阶段蒸馏和复用 pretrained action decoder 来论证，缺少统一 wall-clock / FLOPs headline；如果要写“efficiently”需要注意它更多是训练范式效率，而不是推理速度优势。

## 影响页面
- [[wiki/papers/2510_09607_VITA-VLA.md|2510_09607_VITA-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
