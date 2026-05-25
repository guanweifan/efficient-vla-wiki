# 2605_08168_Async-VLA-Inference

## Source
- Raw: [[raw/2605_08168_Async-VLA-Inference.pdf]]
- Extracts manifest: [[extracts/parses/2605_08168_Async-VLA-Inference/manifest.json]]
- Primary text fallback: [[extracts/parses/2605_08168_Async-VLA-Inference/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **asynchronous VLA inference evaluation / delay-robust control analysis** 论文；它主要比较异步执行策略在 observation staleness 与 control delay 下的鲁棒性，而不是提出单一新的模型压缩方法。
- 论文在统一代码库中比较 IT-RTC、TT-RTC、VLASH 与 A2C2，并分别在 Kinetix 与 LIBERO 设置下分析 delay、chunk length、training-time augmentation 与 inference-time correction 的权衡。来源：[[raw/2605_08168_Async-VLA-Inference.pdf]]，Abstract、Figure 1、Figure 4。
- Kinetix 结果显示 A2C2 在更高 delay 下保持较强 solve rate；LIBERO 结果显示 delay 增大后 A2C2 领先，IT-RTC 在低 delay 可用但长 chunk / 高 delay 下退化。来源：[[raw/2605_08168_Async-VLA-Inference.pdf]]，Figure 1、Figure 2、Figure 4。
- 更稳的主张是：该文提供了 async inference 方法的对照框架和边界条件，适合放在 deployment / inference 边界，而不是当作单一 speedup 方法。

## Methodology Index
- asynchronous inference
- observation staleness
- control delay
- IT-RTC
- TT-RTC
- VLASH
- A2C2
- Kinetix
- LIBERO
- SmolVLA
- chunked action prediction

## Data Pointer
- **Table 1**：deployment scenario 与 delay 映射。
- **Figure 1 / Figure 2**：Kinetix 下不同 delay 与 chunk length 的 solve rate。
- **Figure 3**：TT-RTC / VLASH 中 dmax 的影响。
- **Figure 4**：LIBERO success rate vs delay。
- **Table 2**：LIBERO chunk-generation latency。
- **Tables 5-10**：FLOPs 与 training cost 细节。

## Evidence Links
- [[wiki/evidence/claims/2605_08168_Async-VLA-Inference-headline-split.md|2605_08168_Async-VLA-Inference-headline-split]]

## 待核点
- 该文主要是方法对照与 delay robustness 分析；不应写成新的 token pruning、cache 或 decoding compression。
- Kinetix 与 LIBERO 的模型、delay 范围和 action horizon 不同，不能直接合成单一异步方法排名。
- FLOPs / training cost 表服务于方法开销对照，不等同于真实机器人部署延迟。
