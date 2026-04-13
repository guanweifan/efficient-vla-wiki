# 2603_28565_StreamingVLA

## Source
- Raw: [[raw/2603_28565_StreamingVLA.pdf]]
- Extracts manifest: [[extracts/parses/2603_28565_StreamingVLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2603_28565_StreamingVLA/pdftotext.txt]]
- Fine-grained locator: [[extracts/parses/2603_28565_StreamingVLA/pdftotext.bbox.html]]

## Claim
- 页面定位：这是一篇 **stage-wise streaming execution** 论文；它的核心贡献是让 observation、action generation 和 execution 以异步重叠的方式运行，而不是继续依赖同步 action chunking pipeline。
- 这篇论文要解决的是：当前多阶段 VLA 的 observation、action generation 和 execution 通常串行推进，因此会在控制过程中反复出现 halting gap 与明显 latency。作者把这个问题写成 multi-stage VLA 的同步阻塞，而不是单点模型压缩问题。来源：[[raw/2603_28565_StreamingVLA.pdf]]，Abstract；Introduction；Sec. 3。
- `StreamingVLA` 给出的核心做法有两部分：一是用 **action flow matching** 替代 chunk-wise denoising，使 action generation 与 execution 可以重叠；二是用 **action-saliency-aware adaptive early observation** 让 observation 与 execution 也能够部分重叠。来源：[[raw/2603_28565_StreamingVLA.pdf]]，Sec. 4.1；Sec. 4.2。
- headline 数字需要拆开理解：论文报告了约 `2.4×` latency speedup 与 `6.5×` execution halting reduction；这些都是运行时 pipeline 指标，不等于统一 task-performance superiority claim。来源：[[raw/2603_28565_StreamingVLA.pdf]]，Abstract；Fig. 1。
- 更稳的主张是：`StreamingVLA` 通过改写 action generation 形式与 observation timing，让 VLA 的 compute allocation 更贴近连续控制节奏，重点是 fluent execution，而不是普通的 token pruning 或 cache reuse。

## Methodology Index
- StreamingVLA
- stage-wise parallelism
- streaming execution
- action flow matching
- adaptive early observation
- action saliency
- halting reduction
- latency overlap
- asynchronous observation / generation / execution
- edge-platform VLA

## Data Pointer
- **Abstract + Fig. 1**：适合后续补 `2.4×` latency speedup、`6.5×` halting reduction 与 streaming framing。
- **Sec. 3 runtime analysis**：适合后续补 `Thalt` 定义、multi-stage latency 分解与为什么同步 pipeline 会停顿。
- **Sec. 4.1**：适合后续补 state-based action flow matching 与 action-wise generation。
- **Sec. 4.2**：适合后续补 adaptive early observation 与 action saliency-aware 观测策略。
- **实验章节的 latency / halting / success 表**：适合后续拆 speedup、halting reduction 和 task performance 的具体对照。

## Evidence Links
- [[wiki/evidence/claims/2603_28565_StreamingVLA-headline-split.md|2603_28565_StreamingVLA-headline-split]]

## 待核点
- `2.4×` 与 `6.5×` 分别对应 latency 与 halting 口径，后续需要继续和 task success 分开。
- 论文同时修改了 action generation 与 observation scheduling；后续若要单独归因，需要回主实验与 ablation 拆开。
- 当前论文与现有 `StreamVLA` 名称接近但方法不同；后续 taxonomy 里需要避免误并为同一工作。
