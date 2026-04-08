# 2511_18082_ActDistill

## Source
- Raw: [[raw/2511_18082_ActDistill.pdf]]
- Extracts manifest: [[extracts/parses/2511_18082_ActDistill/manifest.json]]
- Primary text fallback: [[extracts/parses/2511_18082_ActDistill/pdftotext.txt]]

## Claim
- 这篇论文提出 **ActDistill**，目标不是直接在视觉或语言侧做压缩，而是把大规模 VLA 的 **action prediction capability** 迁移到更轻量的 student 上，形成一个以动作语义为中心的高效化框架。作者的基本判断是：既有高效 VLA 策略多沿用 VLM 的压缩逻辑，重视 vision-language correlation，却不够关注 action semantics 的连续性与稳定性。来源：[[raw/2511_18082_ActDistill.pdf]]，第 1-2 页 Abstract、Introduction。
- 核心方法主张由三个紧耦合组件构成：以现成 VLA 作为 **teacher**，先做 **graph-structured encapsulation** 来建模动作语义的层级演化；再由 **self-derived student** 重建这些结构化语义；同时引入 **dynamic router**，按动作预测需求动态选择执行层。作者强调，推理时图相关辅助模块会被移除，仅保留 student 和 router 做选择性执行。来源：[[raw/2511_18082_ActDistill.pdf]]，第 1 页 Abstract；第 3-5 页 Fig. 2、Sec. 3。
- 论文保留了明确的 headline efficiency claim，但应拆到具体 backbone / benchmark：在 **OpenVLA + LIBERO** 上，ActDistill 将 latency 从 `48.91 ms` 降到 `30.74 ms`，对应 `1.59×` speedup，并把 computation 降到 full model 的 `49.5%`；在 **CogACT + SIMPLER** 上，不同场景对应 `1.67× / 1.65×` acceleration 和 `55%+` FLOPs reduction。性能侧则更接近“总体 success 基本保持、局部场景略升略降”，而不是所有设置都统一优于 full-scale VLA。来源：[[raw/2511_18082_ActDistill.pdf]]，第 1-2 页 Abstract、贡献段；第 6-8 页 Table 1-3、Sec. 4。
- 从当前证据看，ActDistill 更像一篇**action-oriented distillation + adaptive routed execution** 论文，而不是单纯的 token pruning / early-exit 方法。其新意在于把 teacher 的层级动作语义图显式结构化，并让 router 围绕动作语义而非一般多模态相关性来决定计算路径；但它的效率与泛化结论明显受 `teacher` 质量和 backbone 结构影响。来源：[[raw/2511_18082_ActDistill.pdf]]，第 2-5 页 Sec. 3；第 7-8 页 Ablation；第 9 页 Limitations。

## Methodology Index
- action-guided distillation
- action priors
- teacher-student framework
- graph-structured encapsulation
- graph-encapsulated teacher
- self-derived student
- dynamic router
- layer-wise gating
- adaptive computation path
- action-centric semantics
- graph-informed supervision
- routed inference
- OpenVLA backbone
- CogACT backbone
- LIBERO
- SIMPLER

## Data Pointer
- **Abstract**：第 1 页。适合后续回收 “action-guided self-derived distillation + over 50% computation reduction + up to 1.67× speedup”。
- **Figure 1 + Introduction**：第 1-2 页。适合后续补它与 token pruning / cache / early-exit / model pruning 的差别，以及 “action-oriented efficiency” 的 framing。
- **Figure 2 + Sec. 3.2-3.5**：第 3-5 页。适合后续补 graph-structured encapsulation、teacher-student distillation、dynamic router 和 inference-time selective execution。
- **Table 1**：第 6 页。适合后续补 OpenVLA backbone 在 LIBERO 上的 success / latency / computation 对比，尤其是 `1.59×` 与 `49.5%` computation 的结果。
- **Table 2**：第 6-7 页。适合后续补 CogACT backbone 在 SIMPLER 的 Visual Matching / Variant Aggregation 结果，以及 `1.67× / 1.65×` 的 speedup。
- **Table 3 + Figure 4 / Figure 5**：第 7-8 页。适合后续补 graph / loss / routing threshold 的 ablation，以及 layer activation 与 trajectory comparison。
- **Limitations / Failure Analysis**：第 9 页与附录 E。适合后续补 teacher dependency、temporal awareness 缺失、以及 teacher-inherited failures 这些边界条件。

## Evidence Links
- [[wiki/evidence/claims/2511_18082_ActDistill-headline-split.md|2511_18082_ActDistill-headline-split]]

## 待核点
- `over 50% computation reduction`、`up to 1.67× speedup`、`comparable or superior performance` 已经拆到 `OpenVLA/LIBERO` 与 `CogACT/SIMPLER` 两组设置；chief editor 后续仍需要决定单篇首页统一保留 `computation` 还是 `FLOPs/latency` 作为 headline 口径。
- 论文在不同地方同时使用 `computation`、`FLOPs`、`speedup`、`latency`，后续需要统一这些效率指标在单篇页中的口径，并避免把 `relative FLOPs` 与 wall-clock latency 混成一句。
- ActDistill 同时可被理解为 `action-oriented distillation`、`graph-based semantic transfer`、`adaptive routed inference`；后续 taxonomy 需要统一它的主定位。
- 当前结论明显依赖 pretrained teacher；作者也在结尾指出 teacher dependency 与 temporal awareness 不足都是限制。后续需要决定这些限制是否应前移到主 claim 层，而不只留在待核点。
