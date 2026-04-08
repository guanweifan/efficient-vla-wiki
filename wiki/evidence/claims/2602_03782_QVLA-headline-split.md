# 2602_03782_QVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_03782_QVLA.md|2602_03782_QVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`29.2% VRAM / 98.9% performance / 1.49× speedup` 是针对 `OpenVLA-OFT` 在 LIBERO 上的 headline，不应直接泛化到所有 base model 和所有 quantization setting。

## Evidence
- 核心证据命题：这篇论文要解决的是：VLA 模型虽然很适合 embodied control，但部署时显存和推理成本过高；而现有从 LLM/MLLM 直接迁移来的 uniform-bit quantization 方法，只关注被动表示保真度，没有针对 action-space 的敏感性，容易把微小量化误差放大成实际控制失败。 来源：[[raw/2602_03782_QVLA.pdf]]，`PDF p.1-2` Abstract + Introduction：
- 补充证据命题：作者提出 `QVLA`，这是一个面向 VLA 的 `action-centric`、`channel-wise` quantization 框架。它不再做粗粒度的统一 bit 分配，而是直接评估“某个通道被量化到不同 bit-width 后会对最终 action 造成多大扰动”，再据此做全局 bit allocation；同时把 `0-bit` 视作 pruning，从而把 quantization 与 pruning 统一到同一个框架里。 来源：[[raw/2602_03782_QVLA.pdf]]，VLA quantization 的问题设定、为什么 LLM-style uniform quantization 不适用于 embodied control、以及 `29.2% VRAM / 98.9% performance / 1.49× speedup` 的 headline 都在这里。
- 主证据锚点 1：来源：[[raw/2602_03782_QVLA.pdf]]，`PDF p.1-2` Abstract + Introduction：
- 主证据锚点 2：来源：[[raw/2602_03782_QVLA.pdf]]，VLA quantization 的问题设定、为什么 LLM-style uniform quantization 不适用于 embodied control、以及 `29.2% VRAM / 98.9% performance / 1.49× speedup` 的 headline 都在这里。
- 主证据锚点 3：来源：[[raw/2602_03782_QVLA.pdf]]，`PDF p.3-5` Sec. 3 + Fig. 1 / Fig. 2：

## Table / Metric Anchors
- `PDF p.7-8` Table 1：
  - weight-activation quantization 主结果在这里；`W4A4` 下与 SmoothQuant、OmniQuant 的比较都应回到这张表。
- `PDF p.7-8` Table 2：
  - weight-only quantization 主结果在这里；`OpenVLA` / `OpenVLA-OFT` 在 `W8A16`、`W4A16` 下与 AWQ 的比较都在这里。
- `PDF p.8` Table 3：
  - channel-wise quantization 与 layer-wise quantization 的对比在这里，用于锚定“为什么必须 channel-wise”的证据。

## Table / Metric Split
- ``PDF p.7-8` Table 1` 这一层支撑 ``PDF p.7-8` Table 1` 对应的 benchmark / metric / operating point。 - weight-activation quantization 主结果在这里；`W4A4` 下与 SmoothQuant、OmniQuant 的比较都应回到这张表。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2602_03782_QVLA.pdf]]，``PDF p.7-8` Table 1`。
- ``PDF p.7-8` Table 2` 这一层支撑 ``PDF p.7-8` Table 2` 对应的 benchmark / metric / operating point。 - weight-only quantization 主结果在这里；`OpenVLA` / `OpenVLA-OFT` 在 `W8A16`、`W4A16` 下与 AWQ 的比较都在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2602_03782_QVLA.pdf]]，``PDF p.7-8` Table 2`。
- ``PDF p.8` Table 3` 这一层支撑 ``PDF p.8` Table 3` 对应的 benchmark / metric / operating point。 - channel-wise quantization 与 layer-wise quantization 的对比在这里，当前对应“为什么必须 channel-wise”的证据。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2602_03782_QVLA.pdf]]，``PDF p.8` Table 3`。

## 不可混写项
- `29.2% VRAM / 98.9% performance / 1.49× speedup` 是针对 `OpenVLA-OFT` 在 LIBERO 上的 headline，不应直接泛化到所有 base model 和所有 quantization setting。
- `99.3% full-precision performance`、`0.5% drop`、`28.2% original memory`、`1.47× speedup` 对应的是 `OpenVLA` 在 `W4A4` 下的具体结果，引用时需保留 setting。
- projector 与 action head 在最终部署里保持 BF16 精度；因此 QVLA 的节省主要来自 vision backbone 和 language module 的量化，若写“全模型低比特量化”需要收紧口径。

## 影响页面
- [[wiki/papers/2602_03782_QVLA.md|2602_03782_QVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
