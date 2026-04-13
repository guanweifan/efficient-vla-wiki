# semantic-only-vs-embodiment-aware-pruning

## 用途
- 当前页收敛 `semantic-only saliency`、`perception-first pruning` 与 `action-aware / phase-aware / interaction-aware / view-sensitive pruning` 这组容易被混写的 token pruning 表述。
- 当前页只记录 source-grounded wording boundary，不承担完整的 token pruning 主题级 synthesis。

## Evidence
- [[wiki/papers/2511_16449_VLA-Pruner.md|2511_16449_VLA-Pruner]]：论文明确指出，VLM 里的 `semantic-only visual token pruning` 直接迁移到 VLA 上会失效，因为 VLA 推理同时包含 high-level semantic understanding 与 low-level action execution；其替代方案是同时考虑 prefill attention、action decode attention 与 temporal continuity。来源：[[raw/2511_16449_VLA-Pruner.pdf]]，Abstract / Introduction；Fig. 2。
- [[wiki/papers/2509_22093_ADP.md|2509_22093_ADP]]：论文把 manipulation visual token redundancy 写成一个随阶段变化的问题，并明确主张 visual compression 应该是 `action-aware` 和 `phase-dependent`；因此静态 pruning 或只看 attention score 的 schedule 不够。来源：[[raw/2509_22093_ADP.pdf]]，Abstract；Method；Table 3。
- [[wiki/papers/2603_22991_VLA-IAP.md|2603_22991_VLA-IAP]]：论文把既有方法概括为 `Perception-First` 偏置，认为它们会过早丢掉视觉上不显眼但对物理操作关键的结构区域；其替代 framing 是 `Interaction-First`，并通过 geometric prior 与 dynamic strategy 让 pruning 强度和交互阶段对齐。来源：[[raw/2603_22991_VLA-IAP.pdf]]，Abstract；Introduction；Fig. 1-2。
- [[wiki/papers/2602_20566_BFApp.md|2602_20566_BFApp]]：论文指出，多视角 VLA 里真正重要的视觉信息同时受 `intra-view` 与 `inter-view` 两层动态重要性控制；因此通用单视角 saliency pruning 不足，必须显式做 view-sensitive hierarchical selection。来源：[[raw/2602_20566_BFApp.pdf]]，Abstract / Introduction；Fig. 1-2。

## 不可混写项
- `semantic-only saliency`、`action-aware pruning`、`interaction-aware pruning`、`view-sensitive pruning` 不是同一层控制信号；不能只因为都在“剪 token”，就写成同一条统一 superiority claim。
- 一篇论文只证明了某种 signal 比纯语义显著性更合适，不等于它已经覆盖了所有 embodied setting；仍要保留其 task、view setup、benchmark 与 backbone 边界。
- `perception-first` 的批评、`phase-aware` 的调度、`interaction-first` 的结构保护、`multi-view hierarchical` 的 importance decomposition 彼此相关，但不能互相替代。

## 影响页面
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/papers/2511_16449_VLA-Pruner.md|2511_16449_VLA-Pruner]]
- [[wiki/papers/2509_22093_ADP.md|2509_22093_ADP]]
- [[wiki/papers/2603_22991_VLA-IAP.md|2603_22991_VLA-IAP]]
- [[wiki/papers/2602_20566_BFApp.md|2602_20566_BFApp]]

## 边界
- 当前页只收敛 pruning signal 的 wording boundary。
- 若后续要系统比较 token pruning 子路线的演化、评价协议与研究空白，应留到对应 synthesis 页面或新的主题页。
