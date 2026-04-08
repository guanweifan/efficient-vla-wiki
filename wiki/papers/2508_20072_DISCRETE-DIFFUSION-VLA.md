# 2508_20072_DISCRETE-DIFFUSION-VLA

## Source
- Raw: [[raw/2508_20072_DISCRETE-DIFFUSION-VLA.pdf]]
- Extracts manifest: [[extracts/parses/2508_20072_DISCRETE-DIFFUSION-VLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2508_20072_DISCRETE-DIFFUSION-VLA/pdftotext.txt]]
- Fine-grained locator: [[extracts/parses/2508_20072_DISCRETE-DIFFUSION-VLA/pdftotext.bbox.html]]

## Claim
- 页面定位：这是一篇 **unified discrete-diffusion action decoder** 论文；核心贡献是把动作离散化并在同一 transformer 内做 masked-token refinement，而不是一般性的 speed benchmark 论文。
- 这篇论文要解决的是：现有 VLA action decoding 要么是 autoregressive 的左到右离散 token 生成，要么是在 backbone 外再接连续 diffusion / MLP head，这会导致动作生成与 vision-language backbone 脱耦，或者受制于 AR bottleneck。
- 核心主张是：可以把动作 chunk 离散化为 token，并在同一个 transformer 内部用 discrete diffusion 做 masked-token refinement，从而保留 diffusion 的 progressive refinement，同时兼容 VLM 的离散 token 接口，实现统一结构、并行解码、可回看修正和更少的 function evaluations。
- 作者提出 `Discrete Diffusion VLA`，强调两点：一是将 action generation 保持在 unified transformer 内部；二是通过 adaptive decoding order + secondary re-masking 让“先易后难”的并行 refinement 生效。论文 headline 结果需要拆开：`96.3%` 来自 `LIBERO`，`71.2% / 64.1%` 来自 `SimplerEnv–Fractal` 的 visual matching / overall，`54.2%` 来自 `SimplerEnv–Bridge` overall；`68.8 ms` 与 “约 `2×` faster than AR” 则来自 `LIBERO-Goal`、`7B backbone`、单张 `H800` 上的 action-chunk latency 测试。来源：[[raw/2508_20072_DISCRETE-DIFFUSION-VLA.pdf]]，第 1-2 页摘要与引言；第 7-8 页 Tables 1-3；第 11 页 Table 8。

## Methodology Index
- discrete diffusion
- unified transformer policy
- tokenized action chunks
- masked-token denoising
- adaptive decoding order
- easy-first decoding
- secondary re-masking
- parallel decoding
- fewer NFEs
- cross-entropy training objective
- unified vision-language-action architecture
- LIBERO
- SimplerEnv–Fractal
- SimplerEnv–Bridge
- LIBERO-OOD

## Data Pointer
- 摘要与问题设定：[[raw/2508_20072_DISCRETE-DIFFUSION-VLA.pdf]] 第 1-2 页摘要与引言。这里给出 unified transformer + discrete diffusion 的总命题，以及 `96.3 / 71.2 / 64.1 / 54.2` 等 headline benchmark 结果。
- 范式与方法总览：[[raw/2508_20072_DISCRETE-DIFFUSION-VLA.pdf]] 第 2 页 Fig. 1；第 4 页 Fig. 2。前者比较 continuous diffusion、AR、BERT-style 与本文的 discrete diffusion 范式；后者是统一 transformer 的 action decoding 框架。
- 主 benchmark 结果：[[raw/2508_20072_DISCRETE-DIFFUSION-VLA.pdf]] 第 7-8 页 Tables 1-3。这里分别覆盖 `LIBERO`、`SimplerEnv–Fractal (Google Robot)` 与 `SimplerEnv–Bridge (WidowX)` 的主对比结果。
- OOD 与解码策略证据：[[raw/2508_20072_DISCRETE-DIFFUSION-VLA.pdf]] 第 9-10 页 Tables 4-7。这里说明 discrete diffusion 对 vision-language ability retention、adaptive decoding order 和 secondary re-masking 的增益。
- 推理速度：[[raw/2508_20072_DISCRETE-DIFFUSION-VLA.pdf]] 第 11 页 Table 8 与相邻文字。这里给出 `68.8 ms` vs. `136.2 ms` 的 latency 对比，并明确是一台 `H800` 上的 action-chunk 级速度测试。

## 待核点
- headline benchmark 数字跨多个环境与指标：`LIBERO` 是 success rate，`SimplerEnv–Fractal` 同时有 visual matching 与 overall，`SimplerEnv–Bridge` 是 overall；后续不能把它们压成一个单一“泛化性能”结论。
- `68.8 ms / 2× faster than AR` 的速度结论来自 `LIBERO-Goal`、`7B backbone`、单张 GPU 的 action-chunk latency，对比对象也包含 one-shot parallel 和 optimized continuous diffusion；后续不能把它泛化成所有场景下的统一加速倍数。
- 论文的强主张之一是“unified transformer preserves vision-language priors”，但这主要由 `LIBERO-OOD` 与 degradation 对比支撑；如果后续要把“保留预训练能力”写成主命题，需要同时保留 benchmark 依赖和对比基线。
- 这篇是 hybrid paper：既讲架构统一，也讲 decoding strategy，还讲速度与 OOD；后续 chief editor 需要决定页面主轴是“统一 discrete diffusion 架构”还是“adaptive decoding / fewer NFEs”。
