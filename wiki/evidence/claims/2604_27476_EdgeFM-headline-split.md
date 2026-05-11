# 2604_27476_EdgeFM-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_27476_EdgeFM.md|2604_27476_EdgeFM]] 的单篇证据落点，用来拆分 edge runtime、agent-tuned kernels、cross-platform deployment 与 VLA case boundary。
- 本页聚焦的 headline bundle：`lightweight edge inference framework`、`agent-tuned kernels`、`1.49x over TensorRT-Edge-LLM`、`first end-to-end VLA deployment on Horizon Journey` 需要分层阅读。

## Evidence
- 核心证据命题：EdgeFM 以 edge single-request latency 和 stable execution 为目标，通过 thin runtime、operator table、agent-tuned reusable kernels 和 KV cache design 做 inference framework optimization。来源：[[raw/2604_27476_EdgeFM.pdf]]，Abstract、Figure 2、Figure 3、method section。
- 跨平台命题：论文报告 x86、NVIDIA Orin 和 Horizon Journey support，并在 Horizon platform 上给出 SmolVLA deployment case。来源：[[raw/2604_27476_EdgeFM.pdf]]，Abstract、Figure 1、Section 4.3、Appendix B。
- 结果证据命题：论文在 Orin 上相对 TensorRT-Edge-LLM 报告最高 `1.49x` speedup，并给出 Horizon BPU prefill/action expert latency details。来源：[[raw/2604_27476_EdgeFM.pdf]]，Table 2、Table 9、Table 10。

## Table / Metric Anchors
- **Figure 1**：cross-platform performance overview。
- **Figure 2 / Figure 3**：architecture and serving pipeline。
- **Table 1**：operator implementation table。
- **Table 2**：Orin platform benchmark。
- **Table 9 / Table 10**：SmolVLA on Horizon BPU details。

## Table / Metric Split
- Orin speedup 是 framework latency benchmark，不是 VLA task performance。
- Horizon deployment 是 hardware/runtime feasibility case，不等同于完整 closed-loop robot evaluation。
- x86、Orin、Horizon 结果不能直接合并为单一 speedup。

## 不可混写项
- 不应把 EdgeFM 写成 VLA policy architecture。
- 不应把 kernel/runtime 优化写成 action-generation method。
- 不应把 hardware portability 写成所有 edge chips 已被验证。

## 影响页面
- [[wiki/papers/2604_27476_EdgeFM.md|2604_27476_EdgeFM]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
