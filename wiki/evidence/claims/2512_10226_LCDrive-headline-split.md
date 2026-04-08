# 2512_10226_LCDrive-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2512_10226_LCDrive.md|2512_10226_LCDrive]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：论文 headline 里同时包含 inference、trajectory quality、RL gain 三类改进，仍需拆到具体主表、分析表和 appendix cost-performance curve，而不是继续保留为 bundled superiority claim。

## Evidence
- 核心证据命题：LCDrive 的核心命题是：在 autonomous driving VLA 中，推理不一定要用自然语言来表达，text-based CoT 在驾驶场景下既不够高效，也未必与动作真正对齐。论文因此提出 latent CoT，把 reasoning 表达成与动作空间对齐的 latent language：一部分 token 是 action-proposal token，直接复用最终动作的 token vocabulary；另一部分 token 是 grounded in latent world model 的 world-model token，用来表达这些候选动作的未来后果。 来源：[[raw/2512_10226_LCDrive.pdf]]，**Abstract / introduction**：最清楚地说明为什么 text-based CoT 不适合 driving，以及 LCDrive 为什么改用 latent reasoning。
- 补充证据命题：模型在 latent space 中交替生成这两类 token，相当于在进行 action-conditioned counterfactual rollout。作者进一步用三阶段训练流程（cold-start latent CoT、world-model head training、closed-loop RL）把这种 latent reasoning 变成 driving policy 的有效条件。 来源：[[raw/2512_10226_LCDrive.pdf]]，**Figure 1 (p.1)**：latent CoT 相对于 text CoT 的总 framing 图，是“更 efficient and aligned reasoning traces” 的第一锚点。
- 主证据锚点 1：来源：[[raw/2512_10226_LCDrive.pdf]]，**Abstract / introduction**：最清楚地说明为什么 text-based CoT 不适合 driving，以及 LCDrive 为什么改用 latent reasoning。
- 主证据锚点 2：来源：[[raw/2512_10226_LCDrive.pdf]]，**Figure 1 (p.1)**：latent CoT 相对于 text CoT 的总 framing 图，是“更 efficient and aligned reasoning traces” 的第一锚点。
- 主证据锚点 3：来源：[[raw/2512_10226_LCDrive.pdf]]，**Figure 2 (p.3)**：LCDrive 架构图，若补 `L2`，这是 action proposal、latent world model、trajectory decoder 如何统一在一个 driving VLA 中的最佳锚点。

## Table / Metric Anchors
- **Table 1 (p.7)**：PhysicalAI-AV 主结果锚点，用来核对 latent CoT 相对 non-reasoning / text-reasoning baseline 的主性能收益。
- **Table 3 (p.12)**：有无 RL 时 latent reasoning 行为分析的关键锚点，用来判断 RL 是否真的改善 proposal quality、proposal-final alignment 和 final trajectory quality。

## Table / Metric Split
- `**Table 1 (p.7)**` 这一层应单独承载 `**Table 1 (p.7)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2512_10226_LCDrive.pdf]]，`**Table 1 (p.7)**`。
- `**Table 3 (p.12)**` 这一层应单独承载 `**Table 3 (p.12)**` 相关的 benchmark / metric / operating point。 当前这一层。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2512_10226_LCDrive.pdf]]，`**Table 3 (p.12)**`。

## 不可混写项
- 论文 headline 里同时包含 inference、trajectory quality、RL gain 三类改进，仍需拆到具体主表、分析表和 appendix cost-performance curve，而不是继续保留为 bundled superiority claim。
- LCDrive 的关键创新其实是 latent reasoning representation 与 latent world model 的耦合；后续 evidence 层可能需要区分“latent CoT 替代 text CoT 的收益”和“LWM / RL 带来的附加收益”。
- 当前最强直接证据主要围绕 autonomous driving benchmark 与 driving-specific world model 设定；后续应明确其结论边界，不直接外推成一般 VLA latent reasoning 规律。

## 影响页面
- [[wiki/papers/2512_10226_LCDrive.md|2512_10226_LCDrive]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
