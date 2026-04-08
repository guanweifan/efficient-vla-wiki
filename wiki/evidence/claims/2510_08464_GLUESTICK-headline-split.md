# 2510_08464_GLUESTICK-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2510_08464_GLUESTICK.md|2510_08464_GLUESTICK]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：这篇的 headline 数字是“相对 dense baseline 的恢复幅度”，不是一个统一的绝对成功率 headline；后续进入 evidence/synthesis 时要避免把 `up to 100% recovery` 误写成“在所有任务上恢复到 dense 水平”。

## Evidence
- 论文的 headline 不是单一 benchmark 数字，而是一组 recovery 命题：在 manipulation 任务上，`GLUESTICK-500` 将 pruned VLA 的平均成功率降幅从 `-72.4%` 缩小到 `-35.7%`；在 navigation 上，它把 success 变化从 `-43.0%` 恢复到 `+1.0%`，并把 unsafe-episode 变化从 `+23.0%` 降到 `-4.0%`。`up to 100% recovery` 主要是 navigation success relative to full sparse 的说法，不应外推成 manipulation 与 navigation 都完全恢复到 dense 水平。作者更稳的主张是：**GLUESTICK 在保留 structured sparsity 的前提下，显著恢复成功率并改善安全指标。** 来源：[[raw/2510_08464_GLUESTICK.pdf]]，第 1-2 页摘要与引言；第 7-8 页 Tables 2-4。
- 补充证据命题：核心主张是：VLA 在 pruning 后丢失的能力可以通过一个 `post-hoc`、`training-free`、完全在 weight space 中操作的恢复步骤部分甚至大幅找回，而不必重新训练整个模型。作者把这个恢复步骤命名为 `GLUESTICK`，其做法是在 dense 与 pruned 权重之间构造 gap matrix，并用低秩修正项把被 pruning 掉的关键方向重新注入到每个 pruned layer 中。 来源：[[raw/2510_08464_GLUESTICK.pdf]]，方法定义：[[raw/2510_08464_GLUESTICK.pdf]] 第 5-6 页 Section 3.2 与 Fig. 3。这里明确给出 `W_gap = W_dense - W_pruned`、截断 SVD、以及推理时在 pruned layer 外包一层低秩修正项的具体公式。
- 主证据锚点 1：来源：[[raw/2510_08464_GLUESTICK.pdf]]，摘要与问题设定：[[raw/2510_08464_GLUESTICK.pdf]] 第 1-2 页摘要、引言与 Fig. 1。这里先给出 “pruning 会让 VLA 崩掉” 和 “GLUESTICK fixes them” 的核心命题，也给出 `up to 100%` navigation 恢复与 manipulation recovery 的 headline。
- 主证据锚点 2：来源：[[raw/2510_08464_GLUESTICK.pdf]]，方法定义：[[raw/2510_08464_GLUESTICK.pdf]] 第 5-6 页 Section 3.2 与 Fig. 3。这里明确给出 `W_gap = W_dense - W_pruned`、截断 SVD、以及推理时在 pruned layer 外包一层低秩修正项的具体公式。
- 主证据锚点 3：来源：[[raw/2510_08464_GLUESTICK.pdf]]，manipulation 主结果：[[raw/2510_08464_GLUESTICK.pdf]] 第 7 页 Table 2。这里报告 `LIBERO` 上相对 dense baseline 的 success rate 变化，是 `-72.4% -> -35.7%` 等结论的主要来源。

## Table / Metric Anchors
- manipulation 主结果：[[raw/2510_08464_GLUESTICK.pdf]] 第 7 页 Table 2。这里报告 `LIBERO` 上相对 dense baseline 的 success rate 变化，是 `-72.4% -> -35.7%` 等结论的主要来源。
- navigation 与 safety 主结果：[[raw/2510_08464_GLUESTICK.pdf]] 第 8 页 Tables 3-4。这里分别给出 `NaVILA` 的 success / unsafe / path-length / distance-to-goal 变化，以及 manipulation unsafe-episode 的恢复情况。
- rank tradeoff：[[raw/2510_08464_GLUESTICK.pdf]] 第 8 页 Q4 与 Table 3。这里说明 `r` 是控制 recovery-memory tradeoff 的单一超参数，并比较 `GLUESTICK-200` 与 `GLUESTICK-500`。

## Table / Metric Split
- `manipulation 主结果` 这一层应单独承载 `manipulation 主结果` 相关的 benchmark / metric / operating point。 这里收口为：manipulation 主结果：[[raw/2510_08464_GLUESTICK.pdf]] 第 7 页 Table 2。这里报告 `LIBERO` 上相对 dense baseline 的 success rate 变化，是 `-72.4% -> -35.7%` 等结论的主要来源。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2510_08464_GLUESTICK.pdf]]，`manipulation 主结果`。
- `navigation 与 safety 主结果` 这一层应单独承载 `navigation 与 safety 主结果` 相关的 benchmark / metric / operating point。 这里收口为：navigation 与 safety 主结果：[[raw/2510_08464_GLUESTICK.pdf]] 第 8 页 Tables 3-4。这里分别给出 `NaVILA` 的 success / unsafe / path-length / distance-to-goal 变化，以及 manipulation unsafe-episode 的恢复情况。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2510_08464_GLUESTICK.pdf]]，`navigation 与 safety 主结果`。
- `rank tradeoff` 这一层应单独承载 `rank tradeoff` 相关的 benchmark / metric / operating point。 这里收口为：论文的 headline 不是单一 benchmark 数字，而是一组 recovery 命题：在 manipulation 任务上，`GLUESTICK-500` 将 pruned VLA 的平均成功率降幅从 `-72.4%` 缩小到 `-35.7%`；在 navigation 上，它把 success 变化从 `-43.0%` 恢复到 `+1.0%`，并把 unsafe-episode 变化从 `+23.0%` 降到 `-4.0%`。`up to 100% recovery` 主要是 navigation success relative to full sparse 的说法，不应外推成 manipulation 与 navigation 都完全恢复到 dense 水平。作者更稳的主张是：**GLUESTICK 在保留 structured sparsity 的前提下，显著恢复成功率并改善安全指标。** 来源：[[raw/2510_08464_GLUESTICK.pdf]]，第 1-2 页摘要与引言；第 7-8 页 Tables 2-4。；rank tradeoff：[[raw/2510_08464_GLUESTICK.pdf]] 第 8 页 Q4 与 Table 3。这里说明 `r` 是控制 recovery-memory tradeoff 的单一超参数，并比较 `GLUESTICK-200` 与 `GLUESTICK-500`。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2510_08464_GLUESTICK.pdf]]，`rank tradeoff`。

## 不可混写项
- 这篇的 headline 数字是“相对 dense baseline 的恢复幅度”，不是一个统一的绝对成功率 headline；后续进入 evidence/synthesis 时要避免把 `up to 100% recovery` 误写成“在所有任务上恢复到 dense 水平”。
- manipulation 结果主要写成 `change relative to Full Dense`，而 navigation 同时给出绝对 path quality 指标；如果引用时要跨任务比较，必须保留这两种指标口径不同。
- `GLUESTICK` 的主要收益目前是性能恢复和安全恢复，论文最后还提到未来可能研究速度/能耗收益，但这部分当前不是主结果，不能提前写成已验证优势。

## 影响页面
- [[wiki/papers/2510_08464_GLUESTICK.md|2510_08464_GLUESTICK]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
