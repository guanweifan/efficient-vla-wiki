# 2605_07931_OneWM-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_07931_OneWM-VLA.md|2605_07931_OneWM-VLA]] 的单篇证据落点，用来拆分 one-token-per-frame visual bandwidth、joint latent/action flow matching、long-horizon benchmark headline。
- 本页聚焦的 headline bundle：`one token per frame`、`Adaptive Attention Pooling`、`14.71M LoRA parameters`、`MetaWorld / LIBERO-Long / real Piper gains` 需要分层阅读。

## Evidence
- 核心证据命题：OneWM-VLA 使用 Adaptive Attention Pooling 将每个 view 每帧压缩为一个 semantic latent token，并通过 joint flow-matching objective 生成 latent world stream 与 action trajectory。来源：[[raw/2605_07931_OneWM-VLA.pdf]]，Abstract、Figure 1、Figure 2、Figure 3。
- 资源/参数命题：论文在 π0 (2B) backbone 上训练 14.71M LoRA parameters，并在 token-count sweep / throughput-memory table 中分析 visual bandwidth。来源：[[raw/2605_07931_OneWM-VLA.pdf]]，Abstract、Table 4、Table 14。
- 结果证据命题：论文在 MetaWorld MT50、LIBERO-Long 和 real Piper Fold Cloth 上报告 benchmark improvement；这些结果分别属于不同任务与评测设置。来源：[[raw/2605_07931_OneWM-VLA.pdf]]，Table 1、Table 2、Table 3。

## Table / Metric Anchors
- **Figure 1**：one-token-per-frame motivation。
- **Figure 2 / Figure 3**：framework and adaptive pooling。
- **Table 1 / Table 2 / Table 3**：main results。
- **Table 4**：per-frame token sweep。
- **Table 7 / Table 8**：semantic compression and joint latent/action ablation。
- **Table 14**：throughput and memory。
- **Figure 5**：pooled visual feature visualization。

## Table / Metric Split
- visual bandwidth token count、throughput/memory 和 task success 是不同口径。
- single-token conclusion 依赖论文 setup 与 matched training budget。
- latent world token rollout 与 action branch execution 在推理期作用不同，需要分开写。

## 不可混写项
- 不应把 OneWM-VLA 写成 temporal KV/cache reuse。
- 不应把 world-module token compression 写成 VLA perception token pruning 的同一机制。
- 不应把 joint flow matching 写成直接减少 action denoising NFE。

## 影响页面
- [[wiki/papers/2605_07931_OneWM-VLA.md|2605_07931_OneWM-VLA]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
