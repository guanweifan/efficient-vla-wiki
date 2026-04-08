# 2601_09708_Fast-ThinkAct

## Source
- Raw: [[raw/2601_09708_Fast-ThinkAct.pdf]]
- Extracts manifest: [[extracts/parses/2601_09708_Fast-ThinkAct/manifest.json]]
- Primary text fallback: [[extracts/parses/2601_09708_Fast-ThinkAct/pdftotext.txt]]

## Claim
- 这篇论文要解决的是：reasoning VLA 虽然能通过显式 chain-of-thought 提升长时程规划、few-shot adaptation 和 failure recovery，但长文本 reasoning trace 带来的推理延迟过高，难以满足 embodied 场景的实时要求。
- 作者提出 `Fast-ThinkAct`，核心思路是把显式 textual CoT 压缩成 `verbalizable latent reasoning`。它通过一个 textual teacher 生成高质量 reasoning，再用 preference-guided distillation 和 visual trajectory alignment，把语言与视觉规划能力蒸馏到紧凑的连续 latent 与 spatial tokens 中，最后再由 reasoning-enhanced policy learning 把这些 latent planning 转成低层动作。
- 论文主张：reasoning VLA 的效率瓶颈不一定要通过“直接缩短文本 CoT”来解决；更有效的路线是把 reasoning 压缩为可 verbalize 的 latent thought，并保留 visual planning latent，这样既能保留 planning 能力，也能显著缩短推理时间。
- headline numeric claims 包括：
  - 相比现有 reasoning VLA，推理 latency 最多降低约 `89.3%`。
  - 相比 `ThinkAct-7B`，推理约 `9.3×` 更快。
  - 在 SimplerEnv-Google、LIBERO 各子任务和 RoboTwin2.0 上整体优于现有 reasoning VLAs。
  - 在同为 3B 规模下，正文明确给出 Fast-ThinkAct 在 LIBERO 上约 `89.7`，在 SimplerEnv-Google 上约 `68.7`，同时相较 baseline 仍可实现约 `7×` 级别推理加速。

## Methodology Index
- reasoning VLA
- latent chain-of-thought
- verbalizable latent reasoning
- preference-guided distillation
- reward-guided preference distillation
- teacher-student distillation
- manipulation trajectory alignment
- spatial tokens
- visual latent planning
- reasoning-enhanced policy learning
- compact reasoning
- SimplerEnv-Google
- LIBERO
- RoboTwin2.0

## Data Pointer
- `PDF p.1-2` Abstract + Fig. 1：
  - Fast-ThinkAct 的问题设定、从长 textual CoT 到 compact latent reasoning 的核心动机、以及 `89.3% reduced inference latency` / `9.3× faster than ThinkAct-7B` 的 headline 都在这里。
- `PDF p.3-5` Sec. 3 + Fig. 2：
  - teacher VLM、latent student、verbalizer、trajectory alignment、以及 reasoning-enhanced policy learning 的整体框架都在这里。
- `PDF p.6-7` Fig. 3：
  - LIBERO、SimplerEnv-Google 与 latency 对比都在这里；各 reasoning VLA 的 success rate 和 latency 对照应优先回这张图。
- `PDF p.7-8` Table 1：
  - RoboTwin2.0 的量化结果在这里，适合后续补双臂 manipulation 的具体证据。
- `PDF p.8-9` Table 2：
  - EgoPlan-Bench2、RoboVQA、OpenEQA 等 embodied reasoning benchmark 的结果在这里，适合后续补“reasoning quality 没丢”的证据。
- `PDF p.6-7` Sec. 3.3 / Sec. 4.2：
  - 从 latent planning 到 diffusion Transformer-based action model 的桥接，以及 training datasets / evaluation benchmarks 的范围说明在这里。

## 待核点
- `89.3% latency reduction` 与 `9.3× faster` 主要是相对具体 reasoning VLA baseline 的效率 headline，后续引用时要明确比较对象，而不是泛化成对所有 VLA 的统一提升。
- 主文当前最容易直接抓到的是 Fig. 3 的 benchmark 结果；若后续需要每个 LIBERO 子套件或 SimplerEnv 的精确数值，应回图表或附录进一步核定。
- 论文同时包含 teacher-student distillation、trajectory alignment 和 reasoning-enhanced policy learning 三层机制；后续若把增益全部归因于 latent reasoning 本身，需要谨慎拆分证据。
- 推理效率提升是相对 reasoning VLAs 而言；若与非-reasoning foundation VLA 比较，结论口径需要单独说明。
