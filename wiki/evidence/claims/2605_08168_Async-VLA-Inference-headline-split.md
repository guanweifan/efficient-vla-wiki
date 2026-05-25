# 2605_08168_Async-VLA-Inference-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_08168_Async-VLA-Inference.md|2605_08168_Async-VLA-Inference]] 的单篇证据落点，用来拆分 async method comparison、delay robustness 与 overhead / FLOPs 口径。

## Evidence
- 核心证据命题：论文在统一框架中比较 IT-RTC、TT-RTC、VLASH 与 A2C2，并把问题设定为 observation staleness 与 control delay 下的 asynchronous VLA inference。来源：[[raw/2605_08168_Async-VLA-Inference.pdf]]，Abstract、Table 1、Figures 1-4。
- 结果证据命题：Kinetix 与 LIBERO 的结果分别报告不同 delay / horizon / model setting 下的 solve rate 或 success rate，A2C2 在更高 delay 区间更稳。来源：[[raw/2605_08168_Async-VLA-Inference.pdf]]，Figures 1、2、4。
- 成本证据命题：论文单独列出 LIBERO chunk-generation latency 与 FLOPs / training cost 表，用于方法开销对照。来源：[[raw/2605_08168_Async-VLA-Inference.pdf]]，Table 2、Tables 5-10。

## Table / Metric Anchors
- **Table 1**：deployment delay mapping。
- **Figures 1-4**：Kinetix / LIBERO delay robustness。
- **Table 2 / Tables 5-10**：latency、FLOPs、training cost。

## Table / Metric Split
- solve rate / success rate、delay robustness、FLOPs 与 training cost 是不同口径。
- Kinetix 和 LIBERO 的 operating point 不能合并成单一排名。

## 不可混写项
- 不应写成新的 model compression 或 token pruning。
- 不应把 benchmark delay robustness 等同于真实硬件实时部署。

## 影响页面
- [[wiki/papers/2605_08168_Async-VLA-Inference.md|2605_08168_Async-VLA-Inference]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
