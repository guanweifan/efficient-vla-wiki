# 2602_18397_VLA-Perf-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_18397_VLA-Perf.md|2602_18397_VLA-Perf]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：这篇的“performance”专指 inference latency 和 throughput，而非 task success rate；如果进入 wiki 的效率 taxonomy，需要避免把它误读成任务性能论文。

## Evidence
- 作者提出 `VLA-Perf`，一个面向 VLA 的 analytical、roofline-based performance model，用来预测任意模型-系统组合下的最优 inference latency / throughput，并据此对 VLA inference landscape 做首次系统性研究。论文不是提出新的 VLA policy，而是从模型尺度、长上下文视频、action generation 方式、异步推理、dual-system pipeline、部署位置、GPU 规格和网络条件等维度总结出 `15` 条设计经验。来源：[[raw/2602_18397_VLA-Perf.pdf]]，第 1-3 页摘要、引言与 Fig. 1。
- 补充证据命题：核心主张是：在设计未来 VLA 模型与推理系统时，应当把 inference latency 和 throughput 视为一等公民问题；为此需要一个能统一分析“模型设计 knobs + system knobs”组合效应的分析工具，而不是只依赖零散 benchmark。 来源：[[raw/2602_18397_VLA-Perf.pdf]]，背景与分析维度：[[raw/2602_18397_VLA-Perf.pdf]] 第 3-6 页 Section 2。这里说明 VLA-Perf 如何把模型架构、action chunk、denoising steps、异步、dual-system，以及 hardware / placement / network 统一进一个推理分析框架。
- 主证据锚点 1：来源：[[raw/2602_18397_VLA-Perf.pdf]]，摘要与研究问题：[[raw/2602_18397_VLA-Perf.pdf]] 第 1-3 页摘要、引言与 Fig. 1。这里定义论文的三个核心问题：给定模型和系统能跑多快、整体性能版图长什么样、未来如何设计模型与系统来支持实时推理。
- 主证据锚点 2：来源：[[raw/2602_18397_VLA-Perf.pdf]]，背景与分析维度：[[raw/2602_18397_VLA-Perf.pdf]] 第 3-6 页 Section 2。这里说明 VLA-Perf 如何把模型架构、action chunk、denoising steps、异步、dual-system，以及 hardware / placement / network 统一进一个推理分析框架。
- 主证据锚点 3：来源：[[raw/2602_18397_VLA-Perf.pdf]]，分析模型本体：[[raw/2602_18397_VLA-Perf.pdf]] 第 6-10 页 Section 3。这里是 roofline-style analytical model 的细节，也是后续所有性能结论的出处。

## Figure / Caption Anchors
- **Fig. 1 (p.2)**：caption 明确说 VLA-Perf 的任务是分析 `model architectures × deployment configurations` 的 performance landscape，并抽出 `15 actionable insights`；它支撑的是分析框架定位，不是某个 benchmark 的 headline 数字。
- **Fig. 2 (p.3)**：caption 把 `camera-rate inference latency` 明确成目标，并用 synchronous VLA inference timeline 解释为什么 real-time 问题本质上是 latency / ingestion rate matching。
- **Fig. 3 (p.5)**：caption 说明 VLA-Perf 把 inference workflow 抽象成 interleaved model components + data transfers；这才是 roofline analysis 的机制入口。

## Figure / Caption / Wording Split
- 本文里的 `performance` 有严格定义：**只指 inference latency 与 throughput，不指 task success rate**。若把它与 manipulation benchmark 并列，必须保留这个定义差异。来源：[[raw/2602_18397_VLA-Perf.pdf]]，第 1-2 页 Abstract / Introduction；第 6 页 Metrics 定义。
- `real-time` 也有显式边界：作者把 **10 Hz** 视作 acceptable、**100 Hz** 视作 high-performance，并进一步对应到 **10–100 ms latency** 的区间；这不是任意论文都共享的默认标准。来源：[[raw/2602_18397_VLA-Perf.pdf]]，第 2-3 页 Fig. 2、Introduction；第 14-15 页结论总结。
- `asynchronous inference` 在本文主要支撑 **throughput gain under networked / server-side deployment**，而不是保证更低 end-to-end latency；作者明确写到 async 可以提吞吐但不降低端到端 latency，并可能引入 staleness。来源：[[raw/2602_18397_VLA-Perf.pdf]]，第 12-13 页 Table 8 与相邻正文。

## 不可混写项
- 这篇的“performance”专指 inference latency 和 throughput，而非 task success rate；如果进入 wiki 的效率 taxonomy，需要避免把它误读成任务性能论文。
- `15 key takeaways` 是跨大量假设与模型-系统组合蒸馏出的结论，不是单一 benchmark headline；引用时应尽量指向具体问题和具体场景，而不是泛化成统一定律。
- `VLA-Perf` 是 analytical model，不是实际 serving runtime；若将其与真实部署论文并列，需要保留“预测/分析工具”这一身份差异。

## 影响页面
- [[wiki/papers/2602_18397_VLA-Perf.md|2602_18397_VLA-Perf]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
