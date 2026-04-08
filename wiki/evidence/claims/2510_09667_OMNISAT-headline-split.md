# 2510_09667_OMNISAT-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2510_09667_OMNISAT.md|2510_09667_OMNISAT]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`6.8x` 压缩与 “millimeter-level reconstruction fidelity” 目前仍是 bundled headline，仍应明确它们分别落在哪个 DROID 对比表和哪种误差指标上。

## Evidence
- 核心证据命题：OMNISAT 将自己定位为一种面向 AR-VLA 的高质量动作 tokenizer，而不只是单纯的压缩器。论文的核心主张是：如果要让自回归 VLA 在长时域、高维动作 chunk 上真正具备可扩展训练能力，动作离散化不仅要压缩得足够狠，还必须保住高保真重建与跨 embodiment 可迁移性。为此，OMNISAT 先用 consistency encoding 将不同数值范围、不同时间长度的动作轨迹对齐成固定长度表示，再对位置、旋转、夹爪三个子空间分别做 multi-stage residual quantization，得到统一的 compact action token space。作者进一步把这个统一 token 空间用于 cross-embodiment manipulation learning，将机器人演示与 human egocentric videos 混合起来做辅助监督。 来源：[[raw/2510_09667_OMNISAT.pdf]]，**Abstract / introduction**：最清楚地给出论文的总命题，包括 `6.8x` 压缩、Droid 预训练、cross-embodiment learning，以及“更快收敛 + 更强下游性能”的系统叙述。
- 补充证据命题：论文 headline claim 需要拆开：`6.8x` 压缩与 millimeter-level reconstruction fidelity 来自 DROID 上的 tokenizer quality 分析；`8% / 13% lower step time` 来自 AR training efficiency，不是下游任务 success 本身；LIBERO 的 “SOTA / competitive” 和 SimplerEnv / real-robot 的性能提升则来自不同 benchmark 与不同 training recipe。更稳的写法是：**OMNISAT 首先是一个高保真动作 tokenizer，其次才通过 cross-embodiment mixed training 在 AR-VLA 下游任务中体现出更快收敛和更强性能。** 来源：[[raw/2510_09667_OMNISAT.pdf]]，**Figure 1 (p.2)**：最适合作为论文总 framing 的第一锚点，说明 OmniSAT 想解决的是 diffusion 与 AR-VLA 在效率 / 精度 / 可扩展性之间的 tradeoff。
- 主证据锚点 1：来源：[[raw/2510_09667_OMNISAT.pdf]]，**Abstract / introduction**：最清楚地给出论文的总命题，包括 `6.8x` 压缩、Droid 预训练、cross-embodiment learning，以及“更快收敛 + 更强下游性能”的系统叙述。
- 主证据锚点 2：来源：[[raw/2510_09667_OMNISAT.pdf]]，**Figure 1 (p.2)**：最适合作为论文总 framing 的第一锚点，说明 OmniSAT 想解决的是 diffusion 与 AR-VLA 在效率 / 精度 / 可扩展性之间的 tradeoff。
- 主证据锚点 3：来源：[[raw/2510_09667_OMNISAT.pdf]]，**Figure 2 (p.4)**：OmniSAT tokenization pipeline 的核心结构图，若要补 `L2`，这是 consistency encoding 与 quantization compression 的第一方法锚点。

## Table / Metric Anchors
- **Table 1 (p.7)**：DROID 上压缩质量对比的第一证据锚点，用来核对 reconstruction quality 与 compression ratio。
- **Table 2 / Table 3 (p.8)**：LIBERO 与 SimplerEnv-WidowX 的主要下游性能锚点，用来支撑“tokenizer + AR recipe”带来更强下游性能，而不是把功劳全压到 compression ratio 本身。
- **Table 4 / Table 5 (p.9)**：组件消融与 backbone/vision supervision 消融，是判断“OMNISAT 究竟是 tokenizer 本身起作用，还是搭配更强 backbone 才起作用”的第一位置。
- **Table 7 (p.17)**：`L=8` 与 `6.8x` 压缩 tradeoff 的关键锚点。

## Table / Metric Split
- `**Table 1 (p.7)**` 这一层应单独承载 `**Table 1 (p.7)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2510_09667_OMNISAT.pdf]]，`**Table 1 (p.7)**`。
- `**Table 2 / Table 3 (p.8)**` 这一层应单独承载 `**Table 2 / Table 3 (p.8)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2510_09667_OMNISAT.pdf]]，`**Table 2 / Table 3 (p.8)**`。
- `**Table 4 / Table 5 (p.9)**` 这一层应单独承载 `**Table 4 / Table 5 (p.9)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2510_09667_OMNISAT.pdf]]，`**Table 4 / Table 5 (p.9)**`。
- `**Table 7 (p.17)**` 这一层应单独承载 `**Table 7 (p.17)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2510_09667_OMNISAT.pdf]]，`**Table 7 (p.17)**`。

## 不可混写项
- `6.8x` 压缩与 “millimeter-level reconstruction fidelity” 目前仍是 bundled headline，仍应明确它们分别落在哪个 DROID 对比表和哪种误差指标上。
- 论文把 OmniSAT 和 cross-embodiment learning 一起包装成整体贡献；后续 evidence 层可能需要把“tokenizer 贡献”和“human+robot mixed training 贡献”拆开。
- `SoTA on LIBERO`、`competitive on Long`、`faster convergence` 等表述依赖不同 benchmark 与训练曲线，仍需逐项拆到具体表格和 setting，而不是继续保留成总括式性能话语。

## 影响页面
- [[wiki/papers/2510_09667_OMNISAT.md|2510_09667_OMNISAT]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
