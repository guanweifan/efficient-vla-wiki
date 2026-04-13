# 2604_05323_VLA-InfoEntropy

## Source
- Raw: [[raw/2604_05323_VLA-InfoEntropy.pdf]]
- Extracts manifest: [[extracts/parses/2604_05323_VLA-InfoEntropy/manifest.json]]
- Primary text fallback: [[extracts/parses/2604_05323_VLA-InfoEntropy/pdftotext.txt]]
- Fine-grained locator: [[extracts/parses/2604_05323_VLA-InfoEntropy/pdftotext.bbox.html]]

## Claim
- 页面定位：这是一篇 **training-free entropy-guided token selection** 论文；它的核心贡献是把 visual entropy、attention entropy 和 timestep 信息合并成一套推理期 token 选择策略，而不是单纯复用 `VLA-Cache` 的静态 token reuse。
- 这篇论文要解决的是：现有 VLA 加速方法往往把视觉冗余、语义相关性和时间变化拆开处理，因此在 sequential decision-making 中容易同时丢掉 task-critical cue 与动态上下文。作者把问题写成 spatial、semantic、temporal 三类信息线索没有被统一调度。来源：[[raw/2604_05323_VLA-InfoEntropy.pdf]]，Introduction；Abstract。
- `VLA-InfoEntropy` 用 image entropy 量化局部视觉信息量，用 attention entropy 捕捉 token 与任务文本的语义相关性，再结合 timestep 做动态切换，从而把模型注意力从全局感知逐步收缩到局部高价值区域。来源：[[raw/2604_05323_VLA-InfoEntropy.pdf]]，Abstract；方法部分。
- headline 数字需要拆开理解：论文在不同位置给出 `1.53×` speedup、`34.9%` FLOPs reduction、`39.8%` CUDA latency reduction、以及 `76.4%` average success / `86.4%` LIBERO-Spatial success 这几类结果；它们属于不同 benchmark 与指标层级，不能混写。来源：[[raw/2604_05323_VLA-InfoEntropy.pdf]]，实验部分。
- 更稳的主张是：这篇工作把 training-free VLA 加速从“单一启发式 token 筛选”推进到“基于 visual + semantic + temporal entropy 的联合选择”，重点仍是 inference-time token selection。

## Methodology Index
- VLA-InfoEntropy
- training-free acceleration
- visual entropy
- attention entropy
- timestep-aware token selection
- entropy-guided transition
- token selection
- VLA-Cache-based reuse
- spatial / semantic / temporal cues
- inference acceleration

## Data Pointer
- **Abstract + Introduction**：适合后续补 entropy 设计动机、与 `VLA-Cache / LightVLA / FLASH-VLA / SP-VLA` 的关系。
- **Fig. 1**：适合后续补传统 VLA、VLA-Cache 和 VLA-InfoEntropy 三者的 token 选择差别。
- **方法章节中的 entropy 定义**：适合后续补 visual entropy、attention entropy 和 timestep 之间的分工。
- **主实验表**：适合后续补 `1.53×`、`34.9%`、`39.8%`、`76.4%`、`86.4%` 的具体 benchmark / metric 对齐。
- **超参数敏感性图与后续消融**：适合后续补 entropy threshold、token 数量与 success / latency tradeoff。

## Evidence Links
- [[wiki/evidence/claims/2604_05323_VLA-InfoEntropy-headline-split.md|2604_05323_VLA-InfoEntropy-headline-split]]

## 待核点
- `76.4%`、`86.4%`、`1.53×`、`34.9%`、`39.8%` 对应的 benchmark 和指标仍需后续逐一拆开。
- 论文把 `VLA-Cache` 的 reuse 与 entropy-based selection 放在同一叙事里；后续要区分“继承的 cache mechanism”和“新增的 entropy selection policy”。
- 当前 strongest evidence 仍偏向 `LIBERO`；后续若要写成一般 VLA 通用加速方法，需要保留验证范围边界。
