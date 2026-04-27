# 2604_11572_DA-PTQ-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_11572_DA-PTQ.md|2604_11572_DA-PTQ]] 的单篇证据落点，用来把 DA-PTQ 的 drift-aware PTQ、memory/speed headline 与 control performance 拆开。
- 本页聚焦的 headline bundle：`42.5% memory reduction`、`54.8% inference speedup`、`reduces kinematic drift` 与 “接近 full-precision control quality” 不能写成同一层结论。

## Evidence
- 核心证据命题：DA-PTQ 把 VLA 低比特量化的主要 failure mode 解释为 temporal error accumulation：量化扰动在 vision-language-to-action interface 进入控制链，并在 sequential control 中逐步放大为 kinematic drift。来源：[[raw/2604_11572_DA-PTQ.pdf]]，Abstract、Introduction。
- 方法证据命题：DA-PTQ 由 Cross-Space Representation Compensation 与 Motion-Driven / Drift-Aware Mixed-Precision Allocation 两部分构成，前者校正 interface representation distortion，后者按 trajectory-level motion error 分配 bit-width。来源：[[raw/2604_11572_DA-PTQ.pdf]]，Abstract、Figure 2、method section。
- 结果证据命题：Table 1 把 task success、memory reduction 和 speedup 放在同一表中；DA-PTQ 的主报告值是 `48.9` success rate、`42.5%` memory reduction、`54.8%` speedup。来源：[[raw/2604_11572_DA-PTQ.pdf]]，Table 1。

## Table / Metric Anchors
- **Table 1**：效率-性能主表，用来核对 success rate、memory reduction、speedup。
- **Table 2**：WidowX in-domain performance；适合核对 DA-PTQ 与 QuantVLA、VLA-Cache、full-precision CogACT 的差距。
- **Table 3**：Google Robot cross-domain performance；适合核对跨 embodiment / distribution shift 下的稳定性。
- **Table 4 / Figure 3**：组件消融；适合区分 CSRC 与 drift-aware mixed precision 的贡献。

## Table / Metric Split
- `42.5% memory reduction` 与 `54.8% inference speedup` 是效率口径；它们不能单独推出控制质量更好。
- `48.9` success rate 属于 SimplerEnv 表中的 task performance 口径；它需要和 benchmark、robot setting、baseline 一起阅读。
- `kinematic drift` 是方法解释的 failure mode；只有在论文给出 drift-aware allocation、trajectory-level error 或 qualitative trajectory evidence 时，才可支撑这一层表述。

## 不可混写项
- 不应把 DA-PTQ 写成一般训练效率方法；它是 post-training compression / calibration。
- 不应把 benchmark speedup 直接写成真实边缘部署结论，除非同时说明 hardware、placement 与控制循环设定。
- 不应把 “接近 full precision” 外推到任意 VLA、任意 action head 或任意低比特配置。

## 影响页面
- [[wiki/papers/2604_11572_DA-PTQ.md|2604_11572_DA-PTQ]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
