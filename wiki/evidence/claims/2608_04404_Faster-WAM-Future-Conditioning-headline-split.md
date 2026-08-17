# 2608_04404_Faster-WAM-Future-Conditioning-headline-split

## 用途
- 服务于 [[wiki/papers/2608_04404_Faster-WAM-Future-Conditioning.md|Faster-WAM (Future Conditioning)]]，拆分 future representation、interaction sparsity、OOD success 与 latency。

## Evidence
- 方法证据命题：Faster-WAM 只执行一次 video expert，并在 action denoising 中通过 SparseMoT 与 Interval KV-Fusion 稀疏读取多深度 future context。来源：[[raw/2608_04404_Faster-WAM-Future-Conditioning.pdf]]，Fig. 2、Method。
- OOD 证据命题：Table 5 的 controlled current-only counterpart 与 Fast-WAM 平均为 51.00% / 49.14%，full Faster-WAM 为 73.57%；该表同时显示 interaction stride 的非单调 tradeoff。来源：[[raw/2608_04404_Faster-WAM-Future-Conditioning.pdf]]，Table 5。
- latency 证据命题：单张 L20、BF16、10 action-denoising steps 下，Joint-WAM / Faster-WAM overall latency 为 559.84 / 252.95 ms。来源：[[raw/2608_04404_Faster-WAM-Future-Conditioning.pdf]]，Appendix Table A4。

## Table / Metric Anchors
- **Table 5**：future-conditioning 与 component / stride ablation。
- **Table A4**：overall、visual、action latency 及 excluded preprocessing。

## Table / Metric Split
- OOD success、in-distribution success 与 real-world success 不合并。
- one-pass video context、sparse interaction、KV fusion 的收益不能只归给 cache。

## 不可混写项
- 不把 same-chunk future K/V 写成 cross-observation cache。
- 不把 2.21x 写成包含完整 robot I/O 的 closed-loop speedup。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- latency 与 OOD result 来自不同实验读数，必须作为同一方法的两条证据而非单一 operating point。
