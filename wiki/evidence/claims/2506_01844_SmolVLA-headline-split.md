# 2506_01844_SmolVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2506_01844_SmolVLA.md|2506_01844_SmolVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：abstract 里的 “comparable to VLAs that are 10× larger” 是 headline 级概括；仍应明确它具体对应哪些 baseline 与哪些任务。

## Evidence
- 论文在 abstract 中给出的 headline 主张是：SmolVLA 可以在 **single GPU** 上训练、在消费级 GPU 甚至 **CPU** 上部署；借助异步推理与 chunked action generation 获得更高 control rate；尽管模型更小，性能仍与 **约 10× larger** 的 VLA 可比。 来源：[[raw/2506_01844_SmolVLA.pdf]]，第 1 页，Abstract。
- 论文在贡献部分进一步明确了训练数据规模：SmolVLA 端到端预训练使用 **22.9K episodes / 10.6M frames**，来自 **481** 个公开 community datasets；作者把这一规模描述为相较 prior art 至少低一个数量级。 来源：[[raw/2506_01844_SmolVLA.pdf]]，第 2 页，贡献列表；第 5 页，Table 1。
- 主证据锚点 1：来源：[[raw/2506_01844_SmolVLA.pdf]]，**Abstract + contribution bullets**：最直接的项目定位、硬件主张、`10× larger` headline、以及开源与社区数据叙事入口。 来源：[[raw/2506_01844_SmolVLA.pdf]]，第 1-2 页。
- 主证据锚点 2：来源：[[raw/2506_01844_SmolVLA.pdf]]，**Architecture**：`Figure 1` + `Sec. 3.1`，结构细节时应先回这里。 来源：[[raw/2506_01844_SmolVLA.pdf]]，第 1 页，Fig. 1；第 3-4 页，Sec. 3.1。
- 主证据锚点 3：来源：[[raw/2506_01844_SmolVLA.pdf]]，**Community data scale**：`Table 1`，这里也是正式写社区数据规模、episodes / frames 与 prior-art 对比的主锚点。 来源：[[raw/2506_01844_SmolVLA.pdf]]，第 5 页，Table 1。

## Table / Metric Anchors
- **Community data scale**：`Table 1`，这里也是正式写社区数据规模、episodes / frames 与 prior-art 对比的主锚点。  
  来源：[[raw/2506_01844_SmolVLA.pdf]]，第 5 页，Table 1。
- **Main simulation result**：`Table 2`，若要拆 `LIBERO` / `Meta-World` 上相对 `OpenVLA`、`π0`、`Diffusion Policy` 的位置，这里是主表。  
  来源：[[raw/2506_01844_SmolVLA.pdf]]，第 11 页，Table 2。
- **Main real-world result**：`Table 3` 与 `Table 4` 给 `SO100/SO101`；`Table 5` 给 pretraining / multitask learning 的效果；`Figure 5` 给 sync vs async 的真实部署对比。  
  来源：[[raw/2506_01844_SmolVLA.pdf]]，第 11 页，Table 3 / Table 4；第 12 页，Table 5 / Fig. 5。

## Table / Metric Split
- `**Community data scale**` 这一层支撑 `**Community data scale**` 对应的 benchmark / metric / operating point。 `Table 1`，这里也是正式写社区数据规模、episodes / frames 与 prior-art 对比的主锚点。 来源：[[raw/2506_01844_SmolVLA.pdf]]，第 5 页，Table 1。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2506_01844_SmolVLA.pdf]]，`**Community data scale**`。
- `**Main simulation result**` 这一层支撑 `**Main simulation result**` 对应的 benchmark / metric / operating point。 `Table 2`，若要拆 `LIBERO` / `Meta-World` 上相对 `OpenVLA`、`π0`、`Diffusion Policy` 的位置，这里是主表。 来源：[[raw/2506_01844_SmolVLA.pdf]]，第 11 页，Table 2。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2506_01844_SmolVLA.pdf]]，`**Main simulation result**`。
- `**Main real-world result**` 这一层支撑 `**Main real-world result**` 对应的 benchmark / metric / operating point。 `Table 3` 与 `Table 4` 给 `SO100/SO101`；`Table 5` 给 pretraining / multitask learning 的效果；`Figure 5` 给 sync vs async 的真实部署对比。 来源：[[raw/2506_01844_SmolVLA.pdf]]，第 11 页，Table 3 / Table 4；第 12 页，Table 5 / Fig. 5。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2506_01844_SmolVLA.pdf]]，`**Main real-world result**`。

## 不可混写项
- abstract 里的 “comparable to VLAs that are 10× larger” 是 headline 级概括；仍应明确它具体对应哪些 baseline 与哪些任务。
- “single GPU 训练 / CPU 部署” 当前仅保留为作者主张；如果若写成更硬的系统能力描述，需要回到 implementation details 与硬件配置部分补证。
- 论文既强调 community pretraining，又在真实世界表格里讨论 multitask finetuning 与 pretraining 效果；chief-editor 需决定，是否把 “community datasets” 单独升成一个 evidence / synthesis 主题，而不只留在单篇页里。

## 影响页面
- [[wiki/papers/2506_01844_SmolVLA.md|2506_01844_SmolVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
