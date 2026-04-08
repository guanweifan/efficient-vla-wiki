# retention-ratio-vs-speed-performance

## 用途
- 当前页收敛 `token budget / token retention ratio / pruning ratio` 与 `speed / FLOPs / latency / performance` 的对应关系。
- 当前页只记录 source-grounded evidence 与不可混写项，不承担主题级 synthesis。

## Evidence
- [[wiki/papers/2505_21200_FlashVLA.md|2505_21200_FlashVLA]]：`62.5%` visual-token budget 对应 `55.7%` visual-token FLOPs reduction、`36.0%` latency reduction 与 `74.4 -> 73.7` 的 LIBERO average success；这是一组绑定在同一 operating point 上的 paired claim。来源：[[raw/2505_21200_FlashVLA.pdf]]，第 7 页，Table 1。
- [[wiki/papers/2506_10100_EfficientVLA.md|2506_10100_EfficientVLA]]：主 headline `1.93x / 28.9% / 0.6%` 绑定在 `CogACT + SIMPLER` 的特定 operating point；不同 `L/T` 组合与不同 token reduction / cache interval 仍要回到 `Table 3 / Table 4`。来源：[[raw/2506_10100_EfficientVLA.pdf]]，第 7-9 页，Table 2-4。
- [[wiki/papers/2511_16449_VLA-Pruner.md|2511_16449_VLA-Pruner]]：`1.99x` speedup、`50%` ratio 下的性能反升、`87.5%` pruning ratio 下的 robustness 来自不同 retention ratio / backbone / benchmark；主文 `Table 1` 与附录 `π0 Table 4` 不能 bundled 成同一 tradeoff line。来源：[[raw/2511_16449_VLA-Pruner.pdf]]，第 7 页，Table 1；第 16 页，Table 4。

## 不可混写项
- `token budget`、`retention ratio`、`pruning ratio` 虽然都描述“保留多少 token”，但具体论文的定义位置和主比较对象不同。
- `FLOPs reduction`、`latency reduction`、`speedup` 与 `accuracy / success-rate drop` 必须保持同一 operating point 配对。
- 不同 backbone、不同 benchmark、不同 token budget 下的 headline，不能压成单一“某方法通常更快且几乎不掉点”的普适结论。

## 影响页面
- [[wiki/papers/2505_21200_FlashVLA.md|2505_21200_FlashVLA]]
- [[wiki/papers/2506_10100_EfficientVLA.md|2506_10100_EfficientVLA]]
- [[wiki/papers/2511_16449_VLA-Pruner.md|2511_16449_VLA-Pruner]]

## 边界
- 当前页只收敛 budget / retention / pruning 口径，不讨论这些方法之间的主题级优劣。
- 若后续要比较 token pruning、token reuse 与 layer reduction 的路线关系，应留到 `Pass 4`。
