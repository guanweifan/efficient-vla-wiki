# 2602_20309_QuantVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_20309_QuantVLA.md|2602_20309_QuantVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`70%` 内存节省与 “超过 full-precision baseline” 目前仍是 bundled headline，仍需拆到具体模型、比特宽度与 benchmark 表格。

## Evidence
- 核心证据命题：QuantVLA 的核心命题是：VLA 的部署瓶颈不只来自模型规模本身，还来自 language backbone 与 diffusion-style action head 在低比特下的耦合失稳；因此，若想把 post-training quantization 真正用于 VLA，关键不是直接套用 LLM/VLM PTQ，而是显式校准 **attention temperature** 与 **output-head residual energy** 这两类在 DiT 动作头中最容易被量化破坏的尺度。 来源：[[raw/2602_20309_QuantVLA.pdf]]，**Abstract / introduction**：最清楚地给出 QuantVLA 的总 framing：为什么已有 PTQ 难以直接迁移到 VLA，尤其是带 DiT action head 的 VLA。
- 补充证据命题：论文将 `QuantVLA` 定位为一个 **training-free**、**post-training** 的 VLA 量化框架，claim 自己是首个面向 VLA 的 PTQ 方法，也是首个成功量化 diffusion transformer action head 的方案。其主要设计包括 selective quantization layout、attention temperature matching (`ATM`) 和 output head balancing (`OHB`)。 来源：[[raw/2602_20309_QuantVLA.pdf]]，**Figure 1 (p.2)**：QuantVLA 在 VLA efficiency 方法谱系中的定位图，也是 “不改架构、直接做 PTQ” 这一命题的第一锚点。
- 主证据锚点 1：来源：[[raw/2602_20309_QuantVLA.pdf]]，**Abstract / introduction**：最清楚地给出 QuantVLA 的总 framing：为什么已有 PTQ 难以直接迁移到 VLA，尤其是带 DiT action head 的 VLA。
- 主证据锚点 2：来源：[[raw/2602_20309_QuantVLA.pdf]]，**Figure 1 (p.2)**：QuantVLA 在 VLA efficiency 方法谱系中的定位图，也是 “不改架构、直接做 PTQ” 这一命题的第一锚点。
- 主证据锚点 3：来源：[[raw/2602_20309_QuantVLA.pdf]]，**Method section on scale drift / ATM / OHB**：若补 `L2`，这里是“attention temperature drift”和“output energy drift”为何成为关键 failure mode 的最好入口。

## Table / Metric Anchors
- **Table 1 (p.7)**：Selective layer-quantization 的先导结果锚点，用来说明为什么单纯量化而不做 ATM/OHB 会失稳。
- **Table 2 (p.8)**：LIBERO 主结果锚点，用来核对 QuantVLA 在 OpenPI π0.5、GR00T N1.5 上的 success、memory 与 relative memory savings。
- **Table 3 (p.8) / Table 4 (p.9)**：分别对应 π0.5 的精度设置与 GR00T N1.5 的 denoising-step 变化，用来支撑“不同 precision / noise settings 下仍保持稳定”。
- **Table 7 (p.13)**：OpenVLA 附加结果锚点，用来判断 QuantVLA 对非-DiT action head 的外推边界。

## Table / Metric Split
- `Table 1` 对应 **layout selection / method necessity**：它回答的是“为什么不能把整个 action head 一起量化”，不是 `70% memory savings` 或 “超过 baseline” 的主结果来源。来源：[[raw/2602_20309_QuantVLA.pdf]]，第 7 页，Table 1。
- `Table 2` 是 **主 LIBERO performance-memory 表**：在 `π0.5` 上，`FP16 97.1 / 4.27GB` 对比 `QuantVLA 97.6 / 1.28GB`；在 `GR00T N1.5` 上，`FP16 86.5 / 2.02GB` 对比 `QuantVLA 88.0 / 0.91GB`。`70%` 内存节省与“超过 full-precision baseline”主要都应回到这里核对。来源：[[raw/2602_20309_QuantVLA.pdf]]，第 8 页，Table 2。
- `Table 3 / Table 4` 对应 **precision / denoising-step robustness**：`π0.5` 在 `W4A4` 下仍有 `95.3` Avg，`GR00T N1.5` 在不同 denoising steps 下维持 `88.0-88.5` Avg；这层证据说明的是鲁棒性边界，不应与 Table 2 的主 memory headline 混成同一结论。来源：[[raw/2602_20309_QuantVLA.pdf]]，第 8-9 页，Table 3、Table 4。
- `Table 7` 对应 **non-DiT boundary**：它只说明 QuantVLA 对 `OpenVLA` 这种非-DiT action head 也有一定可迁移性，不等于前面那些 DiT-specific headline 自动推广到所有 VLA。来源：[[raw/2602_20309_QuantVLA.pdf]]，第 13 页，Table 7。

## 不可混写项
- `70%` 内存节省与 “超过 full-precision baseline” 目前仍是 bundled headline，仍需拆到具体模型、比特宽度与 benchmark 表格。
- 论文把 selective layout、ATM、OHB 一起包装成 QuantVLA 主体；后续 evidence 层可能需要区分“layout 选择本身”的贡献与“两类尺度校准”的贡献。
- 论文一方面强调自己是 DiT-based VLA 的首个成功 PTQ，另一方面又在附录中扩展到 OpenVLA；仍应明确哪些结论是 DiT-specific，哪些只是更一般的 VLA quantization 经验。

## 影响页面
- [[wiki/papers/2602_20309_QuantVLA.md|2602_20309_QuantVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
