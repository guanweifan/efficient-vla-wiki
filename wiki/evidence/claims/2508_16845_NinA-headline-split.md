# 2508_16845_NinA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2508_16845_NinA.md|2508_16845_NinA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`7x-10x` 的速度结论只测量 `action generation module`，明确排除了 VLM forward pass；后续不能写成完整 VLA 端到端控制频率提升。

## Evidence
- 作者提出 `NinA (Normalizing Flows in Action)`，把 `FLOWER` 的 diffusion action expert 替换成 NF，并分别测试 `MLP` 与 `Transformer` 两种 flow backbone。论文声称 `NinA Transformer (38M)` 在 `LIBERO` 上几乎追平 diffusion baseline（平均 `0.938` vs. `0.952`），同时参数量显著更小、推理更快；`NinA MLP (2M)` 也维持了有竞争力的平均成绩 (`0.909`)。另据 Figure 1 / Table 3，NinA 在**仅测 action generation module** 的设置下可达到 `7x-10x` 级别的推理加速。来源：[[raw/2508_16845_NinA.pdf]]，第 1 页摘要与 Fig. 1；第 4 页 Table 1；第 8 页 Table 3。
- 补充证据命题：核心主张是：可以把 diffusion-based action expert 换成 normalizing flow，并保持 VLA 其余部分不变，从而用 one-shot invertible sampling 取代 iterative denoising，在基本不牺牲任务表现的情况下显著降低动作生成延迟。 来源：[[raw/2508_16845_NinA.pdf]]，方法定义：[[raw/2508_16845_NinA.pdf]] 第 2-3 页 Section 3。这里说明如何在 `FLOWER` 中替换 action expert，以及 `MLP` / `Transformer` 两种 normalizing flow 结构。
- 主证据锚点 1：来源：[[raw/2508_16845_NinA.pdf]]，摘要与 headline 动机：[[raw/2508_16845_NinA.pdf]] 第 1 页摘要与 Fig. 1。这里给出 “用 NF 替代 diffusion expert” 的总命题，以及 up-to-`10x` 更快、参数更小但性能接近的 headline 表述。
- 主证据锚点 2：来源：[[raw/2508_16845_NinA.pdf]]，方法定义：[[raw/2508_16845_NinA.pdf]] 第 2-3 页 Section 3。这里说明如何在 `FLOWER` 中替换 action expert，以及 `MLP` / `Transformer` 两种 normalizing flow 结构。
- 主证据锚点 3：来源：[[raw/2508_16845_NinA.pdf]]，主实验结果：[[raw/2508_16845_NinA.pdf]] 第 4 页 Table 1。这里是 `LIBERO Spatial/Object/Goal/10/90` 上与 diffusion expert 的主对比，也是 `0.938 vs. 0.952`、`0.909` 等关键数字的主要证据。

## Table / Metric Anchors
- 主实验结果：[[raw/2508_16845_NinA.pdf]] 第 4 页 Table 1。这里是 `LIBERO Spatial/Object/Goal/10/90` 上与 diffusion expert 的主对比，也是 `0.938 vs. 0.952`、`0.909` 等关键数字的主要证据。
- 速度结果：[[raw/2508_16845_NinA.pdf]] 第 8 页 Table 3。这里报告 H100 与 RTX 3060 上的 action generation latency，是 `7x-10x` 速度优势的具体来源。

## Table / Metric Split
- `主实验结果` 这一层应单独承载 `主实验结果` 相关的 benchmark / metric / operating point。 这里收口为：作者提出 `NinA (Normalizing Flows in Action)`，把 `FLOWER` 的 diffusion action expert 替换成 NF，并分别测试 `MLP` 与 `Transformer` 两种 flow backbone。论文声称 `NinA Transformer (38M)` 在 `LIBERO` 上几乎追平 diffusion baseline（平均 `0.938` vs. `0.952`），同时参数量显著更小、推理更快；`NinA MLP (2M)` 也维持了有竞争力的平均成绩 (`0.909`)。另据 Figure 1 / Table 3，NinA 在**仅测 action generation module** 的设置下可达到 `7x-10x` 级别的推理加速。来源：[[raw/2508_16845_NinA.pdf]]，第 1 页摘要与 Fig. 1；第 4 页 Table 1；第 8 页 Table 3。；主实验结果：[[raw/2508_16845_NinA.pdf]] 第 4 页 Table 1。这里是 `LIBERO Spatial/Object/Goal/10/90` 上与 diffusion expert 的主对比，也是 `0.938 vs. 0.952`、`0.909` 等关键数字的主要证据。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2508_16845_NinA.pdf]]，`主实验结果`。
- `速度结果` 这一层应单独承载 `速度结果` 相关的 benchmark / metric / operating point。 这里收口为：作者提出 `NinA (Normalizing Flows in Action)`，把 `FLOWER` 的 diffusion action expert 替换成 NF，并分别测试 `MLP` 与 `Transformer` 两种 flow backbone。论文声称 `NinA Transformer (38M)` 在 `LIBERO` 上几乎追平 diffusion baseline（平均 `0.938` vs. `0.952`），同时参数量显著更小、推理更快；`NinA MLP (2M)` 也维持了有竞争力的平均成绩 (`0.909`)。另据 Figure 1 / Table 3，NinA 在**仅测 action generation module** 的设置下可达到 `7x-10x` 级别的推理加速。来源：[[raw/2508_16845_NinA.pdf]]，第 1 页摘要与 Fig. 1；第 4 页 Table 1；第 8 页 Table 3。；速度结果：[[raw/2508_16845_NinA.pdf]] 第 8 页 Table 3。这里报告 H100 与 RTX 3060 上的 action generation latency，是 `7x-10x` 速度优势的具体来源。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2508_16845_NinA.pdf]]，`速度结果`。

## 不可混写项
- `7x-10x` 的速度结论只测量 `action generation module`，明确排除了 VLM forward pass；后续不能写成完整 VLA 端到端控制频率提升。
- 主实验基于 `FLOWER` fine-tuning，而不是完整重跑其原始预训练；论文也明确写了所有 action expert 都重新初始化，因此后续比较时要避免把结果误读成“完整继承原 FLOWER 训练管线后的最终上限”。
- `NinA Transformer` 接近 diffusion baseline，但最高平均分仍低于 `Diffusion (330M, Original)`；若写“match diffusion”需要保留这是“same training regime / reinitialized expert”下的近似追平，不是全面超越。

## 影响页面
- [[wiki/papers/2508_16845_NinA.md|2508_16845_NinA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
