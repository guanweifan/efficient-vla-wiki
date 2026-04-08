# 2512_04952_FASTER-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2512_04952_FASTER.md|2512_04952_FASTER]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：论文没有一个统一适用于所有 benchmark 的单一 headline；`112 ms`、`17.3%`、`95.5 -> 96.7 -> 97.7` 分别来自不同设置，后续不能压成一个无条件结论。

## Evidence
- `17.3%`、`96.65` 这类 tokenizer headline 又属于跨 backbone / tokenization 结果，不应与前述 latency 数字压成单一 superiority claim。来源：[[raw/2512_04952_FASTER.pdf]]，第 1 页摘要；第 7-8 页 efficiency tables；第 11-12 页 ablation。
- 补充证据命题：核心主张是：如果把 action chunk 重新表示成 single-channel image，并用 neural tokenizer 学习非均匀的动作 patch 分组与离散压缩，再配合 block-wise autoregressive decoding 与 lightweight action expert，就能同时提升 AR-VLA 的动作重建质量、任务成功率和推理效率。 来源：[[raw/2512_04952_FASTER.pdf]]，tokenizer 方法细节：[[raw/2512_04952_FASTER.pdf]] 第 3-5 页 Fig. 2 与方法章节。这里说明 `FASTerVQ` 如何把 action chunk 映射为 single-channel image、做非均匀 patch grouping，并在时域和频域联合重建。
- 主证据锚点 1：来源：[[raw/2512_04952_FASTER.pdf]]，摘要与总体框架：[[raw/2512_04952_FASTER.pdf]] 第 1-2 页摘要、引言与 Fig. 1。这里给出“tokenizer + AR policy”的总结构，以及论文为什么把 action tokenization 视为 AR-VLA 的关键瓶颈。
- 主证据锚点 2：来源：[[raw/2512_04952_FASTER.pdf]]，tokenizer 方法细节：[[raw/2512_04952_FASTER.pdf]] 第 3-5 页 Fig. 2 与方法章节。这里说明 `FASTerVQ` 如何把 action chunk 映射为 single-channel image、做非均匀 patch grouping，并在时域和频域联合重建。
- 主证据锚点 3：来源：[[raw/2512_04952_FASTER.pdf]]，推理效率主结果：[[raw/2512_04952_FASTER.pdf]] 第 7-8 页 Table 2 与 Table 5。这里对应 observation encoding、tokenizer latency、以及在共享 backbone 下 `112 ms vs 176 ms vs 197-556 ms` 的 runtime 对比。

## Table / Metric Anchors
- 推理效率主结果：[[raw/2512_04952_FASTER.pdf]] 第 7-8 页 Table 2 与 Table 5。这里对应 observation encoding、tokenizer latency、以及在共享 backbone 下 `112 ms vs 176 ms vs 197-556 ms` 的 runtime 对比。
- 组件消融：[[raw/2512_04952_FASTER.pdf]] 第 11-12 页 Table 7 与相邻正文。这里说明 `BAR`、`AE pretraining` 与 full `FASTer` 分别带来的 success-latency tradeoff，也是 `95.5 -> 96.7 -> 97.7` 与 `323 ms -> 140 ms` 的主要出处。

## Table / Metric Split
- `推理效率主结果` 这一层应单独承载 `推理效率主结果` 相关的 benchmark / metric / operating point。 这里收口为：推理效率主结果：[[raw/2512_04952_FASTER.pdf]] 第 7-8 页 Table 2 与 Table 5。这里对应 observation encoding、tokenizer latency、以及在共享 backbone 下 `112 ms vs 176 ms vs 197-556 ms` 的 runtime 对比。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2512_04952_FASTER.pdf]]，`推理效率主结果`。
- `组件消融` 这一层应单独承载 `组件消融` 相关的 benchmark / metric / operating point。 这里收口为：组件消融：[[raw/2512_04952_FASTER.pdf]] 第 11-12 页 Table 7 与相邻正文。这里说明 `BAR`、`AE pretraining` 与 full `FASTer` 分别带来的 success-latency tradeoff，也是 `95.5 -> 96.7 -> 97.7` 与 `323 ms -> 140 ms` 的主要出处。；论文没有一个统一适用于所有 benchmark 的单一 headline；`112 ms`、`17.3%`、`95.5 -> 96.7 -> 97.7` 分别来自不同设置，后续不能压成一个无条件结论。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2512_04952_FASTER.pdf]]，`组件消融`。

## 不可混写项
- 论文没有一个统一适用于所有 benchmark 的单一 headline；`112 ms`、`17.3%`、`95.5 -> 96.7 -> 97.7` 分别来自不同设置，后续不能压成一个无条件结论。
- `112 ms` 等 runtime 结论依赖共享 `PaliGemma` backbone、PyTorch 实现与 `RTX 5090` 硬件条件，不能直接写成一般性的端到端部署速度。
- 论文明确指出大部分性能提升来自 `FASTerVQ` tokenizer，本体 `BAR + AE` 进一步补充速度和性能；仍需决定页面主轴是 tokenizer 创新还是完整 `FASTerVLA` 系统。

## 影响页面
- [[wiki/papers/2512_04952_FASTER.md|2512_04952_FASTER]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
