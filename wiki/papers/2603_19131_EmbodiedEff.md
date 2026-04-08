# 2603_19131_EmbodiedEff

## Source

- Raw: [[raw/2603_19131_EmbodiedEff.pdf]]
- Primary text fallback: [[extracts/parses/2603_19131_EmbodiedEff/pdftotext.txt]]
- Fine-grained locator: [[extracts/parses/2603_19131_EmbodiedEff/pdftotext.bbox.html]]

## Claim

- 页面定位：这是一篇 **evaluation / metric critique** 论文，不是新的 VLA 加速方法论文；它的核心贡献是重写“效率”评估口径，而不是提出新的 inference recipe。
- 这篇论文的核心命题是：当前 VLA 研究里流行的 “efficiency” 几乎都在看参数量、FLOPs、decoding throughput 等 inference-side 指标，但这些指标并不能真实反映机器人系统在物理世界中的整体执行效率。
- 论文主张应把评估重心从单纯的 **inference efficiency** 扩展到 **embodied efficiency**，显式纳入 task completion time、end-effector / joint path length、motion smoothness、action rate 等 system-level 指标。
- 作者通过 weight pruning、quantization、visual token pruning、FAST action tokenizer、in-context prompting 和 supervised fine-tuning 等一系列 controlled studies，论证了一个反直觉结论：很多在传统指标下“更高效”的方法，可能会在 embodied metrics 上表现更差，例如让动作更抖、更绕路、更耗时，哪怕 task success rate 基本不变。
- headline 数字必须拆开理解：`13.6%`、`46.2%`、`34.5%`、`13.2%`、`25.8%` 等分别来自不同 intervention、不同 benchmark 和不同模型，不能压成一个统一的 “高效方法会更差” 总指标。
- 更稳的主张是：**仅凭 inference-side efficiency metrics 不足以比较 VLA 的真实部署效率，必须补入 embodied efficiency metrics 才能看见动作策略层面的差异。**

## Methodology Index

- **Embodied efficiency framing**：把效率从模型推理阶段扩展到机器人执行阶段。
- **System-level embodied metrics**：显式引入 task completion time、end-effector path length、joint-space path length、average jerk、action rate 等指标。
- **Controlled evaluation across compression domains**：分别在 model compression、token sparsification、action sequence compression 上做对照实验。
- **Prompting / SFT as adaptation studies**：把 in-context prompting 与 supervised fine-tuning 也纳入 embodied-efficiency 评估，而不是只看 success rate。
- **Inference-efficient vs embodied-efficient distinction**：明确把 “参数/FLOPs 更少” 与 “机器人执行更省时/更平滑/更省能” 区分开。
- **Metric trade-off analysis**：强调某些方法可以改善单一 embodied metric，但会在其他指标上付代价。

## Data Pointer

- **Abstract / introduction**：最清楚地给出论文为什么要从 inference efficiency 转向 embodied efficiency，以及两者为何会错位。
- **Fig. 1 (p.1)**：最直接的反例图，展示 `5%` vs `20%` 剪枝下 success rate 相同但 completion time 明显不同，说明 “inference-efficient” 不等于 “embodied-efficient”。
- **Fig. 2 (p.2)**：模型推理阶段与机器人执行阶段的分层示意图，是这篇论文评估口径重构的核心 framing 图。
- **TABLE I (p.4)**：weight pruning 的 embodied metrics 主表，用来核对剪枝后 success rate、completion time、path length、jerk、action rate 的变化。
- **TABLE II (p.5)**：weight quantization 的 embodied metrics 主表，用来判断低比特量化对 smoothness / path cost 的影响。
- **TABLE III (p.6)**：FAST tokenizer 的 action compression 主表，用来核对 “更快完成” 与 “jerk 更高” 之间的 trade-off。
- **TABLE IV (p.6) / TABLE V (p.6)**：分别对应 in-context prompting 与 supervised fine-tuning 的 embodied-efficiency 影响，用来核对 jerk、action rate 与 completion time 的联动变化。

## Evidence Links
- [[wiki/evidence/claims/2603_19131_EmbodiedEff-headline-split.md|2603_19131_EmbodiedEff-headline-split]]

## 待核点

- `13.6%`、`46.2%`、`34.5%`、`13.2%`、`25.8%` 等 headline 数字目前仍是 bundled summary，后续需要拆到具体 intervention、模型与 benchmark。
- 论文把 pruning、quantization、token sparsification、action compression、prompting、SFT 全部放进同一篇评估框架；后续 evidence 层可能需要区分“评估论点本身”与“各具体 intervention 的实证结论”。
- 这篇论文的核心贡献更偏 evaluation / metric critique，而不是新 VLA method；后续在 synthesis 层需要明确它是“评估框架重构”类型，避免被误并入普通 efficiency 方法页。
- 后续若横向引用某个 intervention 的数字，必须显式标明它来自评估性对照，而不是作者提出的新方法本身。
