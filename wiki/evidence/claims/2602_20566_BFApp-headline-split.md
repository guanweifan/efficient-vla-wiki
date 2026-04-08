# 2602_20566_BFApp-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_20566_BFApp.md|2602_20566_BFApp]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`1.8x`、`1.5x` 与 `~10%` 提升目前仍是 bundled headline，仍需分别拆到 `π0`、`RDT`、RoboTwin、real-world 和 OOD setting。

## Evidence
- 核心证据命题：这篇论文的核心命题是：多视角 VLA 的效率问题不能只靠通用 VLM token pruning 思路解决，因为机器人 manipulation 中真正重要的视觉信息同时受到 **视角间动态重要性** 和 **视角内任务相关区域** 两层结构影响；如果 pruning 忽略这两层差异，就会在加速的同时丢掉操作关键线索。 来源：[[raw/2602_20566_BFApp.pdf]]，**Abstract / introduction**：最清楚地给出论文为何认为通用 token pruning 在 multi-view VLA 中失效，以及为什么需要 two-level importance。
- 补充证据命题：为此，论文提出 `BFA++`，一个专门面向 multi-view VLA 的 hierarchical dynamic token pruning 框架。它先用 `Intra-IP` 在每个视角内部筛选 task-relevant token，再用 `Inter-IP` 对不同视角的重要性做阶段性评估，最后进行 local-to-global hierarchical pruning。 来源：[[raw/2602_20566_BFApp.pdf]]，**Fig. 1 (p.1)**：BFA++ 与基线方法的 speed-success 对比图，是“同时提速且提成功率”的第一锚点。
- 主证据锚点 1：来源：[[raw/2602_20566_BFApp.pdf]]，**Abstract / introduction**：最清楚地给出论文为何认为通用 token pruning 在 multi-view VLA 中失效，以及为什么需要 two-level importance。
- 主证据锚点 2：来源：[[raw/2602_20566_BFApp.pdf]]，**Fig. 1 (p.1)**：BFA++ 与基线方法的 speed-success 对比图，是“同时提速且提成功率”的第一锚点。
- 主证据锚点 3：来源：[[raw/2602_20566_BFApp.pdf]]，**Fig. 2 (p.3)**：BFA++ 总 pipeline 图，若补 `L2`，这是 Intra-IP、Inter-IP、local pruning、global pruning 如何串联的最好入口。

## Table / Metric Anchors
- **TABLE I (p.6)**：RoboTwin 主结果锚点，用来核对 `π0` / `RDT` 上的 success rate 与 inference speed 变化。
- **TABLE II (p.6)**：real-world 主结果锚点，用来核对论文在真实机器人环境中的收益是否仍成立。
- **TABLE III (p.6)**：RoboTwin2 OOD 结果锚点，用来判断其对 clutter / unseen environment 的泛化边界。
- **TABLE IV (p.7)**：组件与方法消融锚点，用来验证 hierarchical pruning、Inter-IP、Intra-IP 是否都在提供独立贡献。

## Table / Metric Split
- `**TABLE I (p.6)**` 这一层应单独承载 `**TABLE I (p.6)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_20566_BFApp.pdf]]，`**TABLE I (p.6)**`。
- `**TABLE II (p.6)**` 这一层应单独承载 `**TABLE II (p.6)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_20566_BFApp.pdf]]，`**TABLE II (p.6)**`。
- `**TABLE III (p.6)**` 这一层应单独承载 `**TABLE III (p.6)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_20566_BFApp.pdf]]，`**TABLE III (p.6)**`。
- `**TABLE IV (p.7)**` 这一层应单独承载 `**TABLE IV (p.7)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2602_20566_BFApp.pdf]]，`**TABLE IV (p.7)**`。

## 不可混写项
- `1.8x`、`1.5x` 与 `~10%` 提升目前仍是 bundled headline，仍需分别拆到 `π0`、`RDT`、RoboTwin、real-world 和 OOD setting。
- 论文把 Intra-IP、Inter-IP 与 hierarchical pruning 一起包装成 BFA++ 主体；后续 evidence 层可能需要区分“importance supervision 有效”与“hierarchical pruning 结构有效”。
- 论文强调方法是 plug-and-play multi-backbone token pruning，但当前直接证据主要集中在 `π0` 与 `RDT` 的 multi-view setting；仍应明确它对其他 VLA 架构或非多视角设定的适用边界。

## 影响页面
- [[wiki/papers/2602_20566_BFApp.md|2602_20566_BFApp]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
