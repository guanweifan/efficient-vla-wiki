# 2605_29662_SAFE-Pruner

## Source
- Raw: [[raw/2605_29662_SAFE-Pruner.pdf]]
- Extracts manifest: [[extracts/parses/2605_29662_SAFE-Pruner/manifest.json]]
- Primary text fallback: [[extracts/parses/2605_29662_SAFE-Pruner/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **future-aware visual token pruning for VLA inference acceleration** 论文；它的核心效率问题是避免 shallow-only pruning 过早丢掉后续层需要的视觉 token。
- SAFE-Pruner 观察到 semantic attention consistency，并用 historical late-stage attention 预测当前 timestep deeper-layer token saliency；同时用 adaptive subtask segmentation 处理 attention shift。来源：[[raw/2605_29662_SAFE-Pruner.pdf]]，Abstract、Figure 1、method section。
- 论文强调 plug-and-play pruning，目标是在不改 base model 的情况下改善 latency / FLOPs 与 success trade-off。来源：[[raw/2605_29662_SAFE-Pruner.pdf]]，Introduction、Table 1、Table 2。
- 结果证据覆盖 LIBERO、SIMPLER 和真实机器人任务；headline speedup 与 success degradation 必须绑定具体 backbone / benchmark / latency 测量。来源：[[raw/2605_29662_SAFE-Pruner.pdf]]，Table 1、Table 2、Table 3、Table 4。

## Methodology Index
- visual token pruning
- semantic attention consistency
- future-aware saliency forecast
- adaptive subtask division
- plug-and-play inference acceleration
- shallow-only pruning boundary
- LIBERO / SIMPLER / real-robot evaluation

## Data Pointer
- **Abstract / Figure 1**：future-aware pruning framing and shallow-only failure mode。
- **Method section**：semantic attention consistency, forecast mechanism, adaptive subtask division。
- **Table 1**：LIBERO comparison across OpenVLA, OpenVLA-OFT and π0.5。
- **Table 2**：SIMPLER Visual Matching / Variant Aggregation speedup and success。
- **Table 3**：real robot manipulation success, FLOPs and VLM backbone latency。
- **Table 4**：forecast and division ablation。

## Evidence Links
- [[wiki/evidence/claims/2605_29662_SAFE-Pruner-headline-split.md|2605_29662_SAFE-Pruner-headline-split]]

## 待核点
- SAFE-Pruner 应和 semantic-only pruning 分开：它显式使用 future / late-stage attention cues，但仍属于 token pruning route。
- `plug-and-play` 需要绑定论文验证的 architectures and settings，不应泛化成任意 VLA。
- real-robot latency 指 VLM backbone inference latency，不等于完整 robot control-loop latency。
