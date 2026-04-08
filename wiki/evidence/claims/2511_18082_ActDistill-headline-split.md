# 2511_18082_ActDistill-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2511_18082_ActDistill.md|2511_18082_ActDistill]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`over 50% computation reduction`、`up to 1.67× speedup`、`comparable or superior performance` 已经拆到 `OpenVLA/LIBERO` 与 `CogACT/SIMPLER` 两组设置；主编仍需决定单篇首页统一保留 `computation` 还是 `FLOPs/latency` 作为 headline 口径。

## Evidence
- 这篇论文提出 **ActDistill**，目标不是直接在视觉或语言侧做压缩，而是把大规模 VLA 的 **action prediction capability** 迁移到更轻量的 student 上，形成一个以动作语义为中心的高效化框架。作者的基本判断是：既有高效 VLA 策略多沿用 VLM 的压缩逻辑，重视 vision-language correlation，却不够关注 action semantics 的连续性与稳定性。来源：[[raw/2511_18082_ActDistill.pdf]]，第 1-2 页 Abstract、Introduction。
- 核心方法主张由三个紧耦合组件构成：以现成 VLA 作为 **teacher**，先做 **graph-structured encapsulation** 来建模动作语义的层级演化；再由 **self-derived student** 重建这些结构化语义；同时引入 **dynamic router**，按动作预测需求动态选择执行层。作者强调，推理时图相关辅助模块会被移除，仅保留 student 和 router 做选择性执行。来源：[[raw/2511_18082_ActDistill.pdf]]，第 1 页 Abstract；第 3-5 页 Fig. 2、Sec. 3。
- 主证据锚点 1：来源：[[raw/2511_18082_ActDistill.pdf]]，**Abstract**：第 1 页。可直接承载 “action-guided self-derived distillation + over 50% computation reduction + up to 1.67× speedup”。
- 主证据锚点 2：来源：[[raw/2511_18082_ActDistill.pdf]]，**Figure 1 + Introduction**：第 1-2 页。用于锚定它与 token pruning / cache / early-exit / model pruning 的差别，以及 “action-oriented efficiency” 的 framing。
- 主证据锚点 3：来源：[[raw/2511_18082_ActDistill.pdf]]，**Figure 2 + Sec. 3.2-3.5**：第 3-5 页。用于锚定 graph-structured encapsulation、teacher-student distillation、dynamic router 和 inference-time selective execution。

## Table / Metric Anchors
- **Table 1**：第 6 页。用于锚定 OpenVLA backbone 在 LIBERO 上的 success / latency / computation 对比，尤其是 `1.59×` 与 `49.5%` computation 的结果。
- **Table 2**：第 6-7 页。用于锚定 CogACT backbone 在 SIMPLER 的 Visual Matching / Variant Aggregation 结果，以及 `1.67× / 1.65×` 的 speedup。
- **Table 3 + Figure 4 / Figure 5**：第 7-8 页。用于锚定 graph / loss / routing threshold 的 ablation，以及 layer activation 与 trajectory comparison。

## Table / Metric Split
- `**Table 1**` 这一层应单独承载 `**Table 1**` 相关的 benchmark / metric / operating point。 这里收口为：论文保留了明确的 headline efficiency claim，但应拆到具体 backbone / benchmark：在 **OpenVLA + LIBERO** 上，ActDistill 将 latency 从 `48.91 ms` 降到 `30.74 ms`，对应 `1.59×` speedup，并把 computation 降到 full model 的 `49.5%`；在 **CogACT + SIMPLER** 上，不同场景对应 `1.67× / 1.65×` acceleration 和 `55%+` FLOPs reduction。性能侧则更接近“总体 success 基本保持、局部场景略升略降”，而不是所有设置都统一优于 full-scale VLA。来源：[[raw/2511_18082_ActDistill.pdf]]，第 1-2 页 Abstract、贡献段；第 6-8 页 Table 1-3、Sec. 4。；**Table 1**：第 6 页。当前对应 OpenVLA backbone 在 LIBERO 上的 success / latency / computation 对比，尤其是 `1.59×` 与 `49.5%` computation 的结果。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2511_18082_ActDistill.pdf]]，`**Table 1**`。
- `**Table 2**` 这一层应单独承载 `**Table 2**` 相关的 benchmark / metric / operating point。 这里收口为：论文保留了明确的 headline efficiency claim，但应拆到具体 backbone / benchmark：在 **OpenVLA + LIBERO** 上，ActDistill 将 latency 从 `48.91 ms` 降到 `30.74 ms`，对应 `1.59×` speedup，并把 computation 降到 full model 的 `49.5%`；在 **CogACT + SIMPLER** 上，不同场景对应 `1.67× / 1.65×` acceleration 和 `55%+` FLOPs reduction。性能侧则更接近“总体 success 基本保持、局部场景略升略降”，而不是所有设置都统一优于 full-scale VLA。来源：[[raw/2511_18082_ActDistill.pdf]]，第 1-2 页 Abstract、贡献段；第 6-8 页 Table 1-3、Sec. 4。；**Table 2**：第 6-7 页。当前对应 CogACT backbone 在 SIMPLER 的 Visual Matching / Variant Aggregation 结果，以及 `1.67× / 1.65×` 的 speedup。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2511_18082_ActDistill.pdf]]，`**Table 2**`。
- `**Table 3 + Figure 4 / Figure 5**` 这一层应单独承载 `**Table 3 + Figure 4 / Figure 5**` 相关的 benchmark / metric / operating point。 这一层对应 graph / loss / routing threshold 的 ablation，以及 layer activation 与 trajectory comparison。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2511_18082_ActDistill.pdf]]，`**Table 3 + Figure 4 / Figure 5**`。

## Figure / Caption Anchors
- `Figure 1`：第 2 页。ActDistill 与 token pruning / early-exit / lightweight VLA 的效率范式对比。
- `Figure 2`：第 3 页。teacher、graph-structured encapsulation、student、dynamic router 的总流程。
- `Figure 4 / Figure 5`：第 8 页。routing intensity 与 trajectory stability 的可视化证据。
- `Conclusion + Limitation and Future Work`：第 9 页。`generality`、teacher dependency、temporal awareness 不足的 wording 边界。

## Figure / Caption / Wording Split
- `Figure 1` 支撑的是 **ActDistill 的问题 framing**：作者把既有效率路线批评为“偏 vision-language correlation、弱化 action semantics”，所以这张图主要用来说明它为什么不是普通 token pruning / early-exit，而不是用来支撑任何具体 speedup 数字。来源：[[raw/2511_18082_ActDistill.pdf]]，第 2 页 Figure 1 与紧随其后的 Introduction。
- `Figure 2` 支撑的是 **方法机制本身**：teacher 先做 graph-structured encapsulation，student 再重建层级动作语义，并由 dynamic router 按 action semantics 选择执行层。因此 “action-oriented distillation + adaptive routed execution” 的 claim 必须回到这张图和 Sec. 3.2，而不能只靠 abstract headline。来源：[[raw/2511_18082_ActDistill.pdf]]，第 3-5 页 Figure 2 与 Sec. 3.2。
- `Figure 4` 支撑的是 **moderate skipping preserves performance、aggressive skipping hurts fine spatial/temporal refinement** 这类 routing boundary。它说明的是 activation frequency 与 routing intensity 的关系，不等同于 Table 1/2 的 benchmark performance headline。来源：[[raw/2511_18082_ActDistill.pdf]]，第 7-8 页 Figure 4 与 `Dynamic Routing Intensity` 段。
- `Figure 5` 支撑的是 **trajectory stability**：ActDistill 与 full model 在 LIBERO 上都能保持较平滑、较准确的轨迹，因此它更适合支撑 “trajectory-level fidelity” 而不是“所有 success rate 都 superior”。来源：[[raw/2511_18082_ActDistill.pdf]]，第 8 页 Figure 5 与 `Trajectory Comparison` 段。
- `Conclusion + Limitation` 里的 `general action-guided self-derived distillation framework` 与 `strong efficiency and generality` 必须和 caveat 一起读：作者紧接着明确写出方法依赖 pretrained teacher，且 routing 缺少 continuous control 所需的 temporal awareness，所以 `generality` 只能理解成 **跨 autoregressive / diffusion backbone 的已验证范围内 generality**，不能写成 teacher-free 或对 unseen skills 已稳健泛化。来源：[[raw/2511_18082_ActDistill.pdf]]，第 9 页 Conclusion / Limitation and Future Work。

## 不可混写项
- `over 50% computation reduction`、`up to 1.67× speedup`、`comparable or superior performance` 已经拆到 `OpenVLA/LIBERO` 与 `CogACT/SIMPLER` 两组设置；主编仍需决定单篇首页统一保留 `computation` 还是 `FLOPs/latency` 作为 headline 口径。
- 论文在不同地方同时使用 `computation`、`FLOPs`、`speedup`、`latency`，仍需统一这些效率指标在单篇页中的口径，并避免把 `relative FLOPs` 与 wall-clock latency 混成一句。
- ActDistill 同时可被理解为 `action-oriented distillation`、`graph-based semantic transfer`、`adaptive routed inference`；后续 taxonomy 需要统一它的主定位。

## 影响页面
- [[wiki/papers/2511_18082_ActDistill.md|2511_18082_ActDistill]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
