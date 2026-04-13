# 2603_25766_ETA-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2603_25766_ETA-VLA.md|2603_25766_ETA-VLA]] 的单篇证据落点，用来拆开 temporal fusion、intra-LLM sparsification 与 headline 数字之间的边界。

## Evidence
- 核心证据命题：`ETA-VLA` 把 driving VLA 的效率问题写成“多帧多视角历史带来的时空 token bloat”，并提出 `TFM + ILSA` 的双层压缩方案。来源：[[raw/2603_25766_ETA-VLA.pdf]]，Abstract；Introduction。
- 补充证据命题：`TFM` 在进入 LLM 前压缩时间维，`ILSA` 在 LLM 内做 text-guided、RoPE-free、diversity-preserving 稀疏化。来源：[[raw/2603_25766_ETA-VLA.pdf]]，Sec. III-B/C；Algorithm 1。

## Table / Metric Anchors
- **Abstract / headline paragraph**：`32%`、`85%`、`61%`、`94%` 这组 headline 的第一入口。
- **Navtest / Navhard 主结果表**：适合后续拆主 benchmark performance 与 pruning ratio。
- **pruning-ratio / ablation 表**：适合后续拆 token 数量、FLOPs 与 accuracy 的 tradeoff。

## 不可混写项
- `32% computational FLOPs reduction`
- `85% visual token pruning`
- `61% inference FLOPs reduction`
- `94% of original accuracy`
- 这些数字不在同一比较层，后续必须按 benchmark、baseline 与指标口径拆开。

## 影响页面
- [[wiki/papers/2603_25766_ETA-VLA.md|2603_25766_ETA-VLA]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]

## 边界
- 本页只承担单篇 claim 的稳定落点，不承担 driving vs manipulation 的跨主题比较。
