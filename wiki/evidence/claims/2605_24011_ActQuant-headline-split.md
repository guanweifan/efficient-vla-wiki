# 2605_24011_ActQuant-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_24011_ActQuant.md|2605_24011_ActQuant]] 的单篇证据落点，用来拆分 action-guided PTQ、sub-4-bit compression、OmniModel.cpp runtime、memory / latency / robot success headline。
- 本页聚焦的 headline bundle：`2.5-3.0 bpw`、`5.3x backbone compression`、`1.5x per-token latency speedup`、`UR3 success-rate retention` 需要分层阅读。

## Evidence
- 方法证据命题：ActQuant 用 inter-tensor bit allocation 和 intra-tensor scale optimization 两级 action-guided PTQ，把 bit allocation 与 quantization scale tied to action prediction relevance。来源：[[raw/2605_24011_ActQuant.pdf]]，Abstract、Introduction、method section。
- 系统证据命题：OmniModel.cpp 把 VLA models 转成 native C/C++ runtime，并通过 GGML low-bit kernels 支撑 edge/on-device deployment。来源：[[raw/2605_24011_ActQuant.pdf]]，Abstract、Figure 4。
- 结果证据命题：论文分别在 LIBERO、per-token latency table 和 UR3 real-world tasks 中报告 success retention、memory compression 与 runtime latency；这些不是单一指标。来源：[[raw/2605_24011_ActQuant.pdf]]，Figure 1、Table 2、Table 3、Table 4。

## Table / Metric Anchors
- **Figure 1**：success rate and memory footprint across bit-widths。
- **Table 1**：LIBERO simulation success across PTQ settings。
- **Table 2**：OpenVLA per-token latency across hardware / runtime modes。
- **Table 3**：UR3 real-world success and memory comparison。
- **Table 4**：component ablation on LIBERO。
- **Figure 4**：OmniModel.cpp conversion and deployment pipeline。

## Table / Metric Split
- LIBERO success retention, backbone memory footprint, per-token latency and UR3 success are four distinct evidence口径。
- `ActQuant` algorithmic PTQ and `OmniModel.cpp` runtime are coupled in the paper, but their contributions should still be distinguished.
- `bpw` is a model compression / quantization setting, not by itself a runtime guarantee.

## 不可混写项
- 不应把 ActQuant 的 sub-4-bit mixed precision 写成 uniform full-stack W4A4。
- 不应把 PyTorch-vs-C/C++ runtime speedup attributed only to quantization algorithm。
- 不应把 UR3 four-task success rates merged with LIBERO suite averages。

## 影响页面
- [[wiki/papers/2605_24011_ActQuant.md|2605_24011_ActQuant]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
