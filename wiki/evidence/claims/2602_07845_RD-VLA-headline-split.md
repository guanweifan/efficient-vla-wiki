# 2602_07845_RD-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_07845_RD-VLA.md|2602_07845_RD-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`80x`、`93.0%`、`92.5%`、`3.39`、`45.3%` 目前仍是 bundled headline，仍需分别拆到具体 benchmark、baseline 和 fixed/adaptive 设置。

## Evidence
- 核心证据命题：RD-VLA 的核心命题是：VLA 的 test-time compute scaling 不一定要通过显式 reasoning token 自回归展开来实现，更合适的做法是把“思考”移到动作头内部的 latent recurrent refinement 里，让模型在 constant-memory 条件下按任务难度动态增加推理深度。 来源：[[raw/2602_07845_RD-VLA.pdf]]，**Abstract / introduction**：最清楚地说明论文为何反对显式 token reasoning，以及为什么把 test-time compute scaling 改写成 latent recurrent depth 问题。
- 补充证据命题：论文认为，现有 reasoning-centric VLA 往往把推理外显成 token generation，这会在连续动作场景里带来明显的 decoding 开销和 memory cost；而 RD-VLA 通过 weight-tied recurrent action head、latent scratchpad refinement 和 uncertainty-based adaptive stopping，把推理深度变成一个可在推理时弹性伸缩的内部变量。 来源：[[raw/2602_07845_RD-VLA.pdf]]，**Fig. 1 (p.3)**：RD-VLA 与显式 reasoning-token VLA 的 framing 对比，也是 “comparable performance, much faster latent reasoning” 的第一锚点。
- 主证据锚点 1：来源：[[raw/2602_07845_RD-VLA.pdf]]，**Abstract / introduction**：最清楚地说明论文为何反对显式 token reasoning，以及为什么把 test-time compute scaling 改写成 latent recurrent depth 问题。
- 主证据锚点 2：来源：[[raw/2602_07845_RD-VLA.pdf]]，**Fig. 1 (p.3)**：RD-VLA 与显式 reasoning-token VLA 的 framing 对比，也是 “comparable performance, much faster latent reasoning” 的第一锚点。
- 主证据锚点 3：来源：[[raw/2602_07845_RD-VLA.pdf]]，**Fig. 2 (p.3)**：Prelude / Recurrent Core / Coda 三段式架构图，若补 `L2`，这里是方法拆解的最佳锚点。

## Table / Metric Anchors
- **TABLE II (p.6)**：LIBERO recurrence-depth / adaptive-compute 主结果锚点，用来区分 fixed recurrence、binary adaptation 与 mean iteration `k̄`。
- **TABLE III (p.7)**：CALVIN ABC→D 主结果锚点，用来核对 `3.39 Avg.Len`、`45.3 task-5` 与 `0.5B` 模型相对 baseline 的位置。

## Table / Metric Split
- `TABLE II | LIBERO fixed recurrence`：`Fixed Rec=12` 给出 `Spatial 92.0 / Object 99.0 / Goal 96.0 / Long 84.8 / Avg 93.0`；`Fixed Rec=8` 给出 `93.0 / 97.8 / 94.2 / 85.2 / 92.6`。因此 `93.0%` 这个 headline 对应的是 `LIBERO avg` 在 `Rec=12` 的 fixed-depth operating point，而不是所有 compute setting 的统一结果。来源：[[raw/2602_07845_RD-VLA.pdf]]，第 6 页，Table II。
- `TABLE II | LIBERO adaptive compute`：`Binary Adaptation, τ = 5e-4` 时，`Spatial / Object / Goal / Long / Avg = 88.6 / 98.8 / 96.8 / 85.8 / 92.5`，`k̄ = 7.93`，`σ = 1.03`。这组结果支撑的是“接近 fixed-depth peak (`93.0`) 但平均迭代数从 `12` 降到 `7.93`”的 compute-saving story，而不是直接支撑 `80x` 这种跨方法 headline。来源：[[raw/2602_07845_RD-VLA.pdf]]，第 6 页，Table II。
- `TABLE III | CALVIN ABC→D`：`RD-VLA (0.5B)` 在 `task 1 ... task 5` 上是 `91.4 / 79.5 / 67.9 / 54.9 / 45.3`，`Avg.Len = 3.39`；对照 `OpenVLA (7B)` 的 `91.3 / 77.8 / 62.0 / 52.1 / 43.5`，`Avg.Len = 3.27`。因此 `45.3%` 和 `3.39` 只能表述为 CALVIN chain-length / task-5 指标，不应与 LIBERO 的 `92.5/93.0` 混成同一 benchmark headline。来源：[[raw/2602_07845_RD-VLA.pdf]]，第 6-7 页，Table III。

## 不可混写项
- `80x`、`93.0%`、`92.5%`、`3.39`、`45.3%` 目前仍是 bundled headline，仍需分别拆到具体 benchmark、baseline 和 fixed/adaptive 设置。
- `80x speedup` 与 `14x smaller` 是相对 token-reasoning VLA 的 framing-level headline，不是由 Table II/III 直接给出的同层指标；引用时不能和 `LIBERO avg 93.0/92.5`、`CALVIN Avg.Len 3.39` 写成同一表层结论。
- 论文把 latent recurrent reasoning 与 adaptive stopping 共同包装成 RD-VLA 主体；后续 evidence 层可能需要区分“latent reasoning 本身有效”与“adaptive compute allocation 带来的附加收益”。
- 论文强调其 constant-memory、non-autoregressive reasoning 优势，但当前最强直接证据主要针对 reasoning-centric VLAs；仍应明确它相对普通 non-reasoning VLA 的比较边界。

## 影响页面
- [[wiki/papers/2602_07845_RD-VLA.md|2602_07845_RD-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
