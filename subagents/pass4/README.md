# Pass 4 准备说明

## 目标
1. `Pass 4` 负责在已稳定的 `papers + evidence` 之上，完成历史整合、主题聚类与建模。
2. `Pass 4` 不再承担新的大规模 evidence 补挖；若发现个别证据缺口，只允许局部回补。
3. `Pass 4` 的主产物是 `wiki/synthesis/*`，不是继续大面积改写 `papers/*.md`。

## 默认工作模式
1. `chief-editor` 串行写正式 `wiki/synthesis/*`。
2. `sidecar` 只允许做只读锚点检索，不允许并发写正式页面。
3. 单个主题必须先通过阶段 gate，才能进入下一阶段。
4. 未通过 gate 的主题不得靠“整体感觉差不多”推进。

## 主题准入 gate
1. 只有同时满足以下条件的问题，才可升格为正式主题：
   - 能压缩成一句明确的 `theme question`
   - 至少涉及 `3` 篇论文
   - 至少有 `3` 个可回链的 `papers/evidence` 支点；若 evidence 稀疏，可用 `2` 个 evidence 支点加 `1` 个 `raw` fallback
   - 能明确写出纳入边界与排除边界
2. 不满足准入 gate 的问题只能保留为局部观察或待核列表，不能写成正式主题页。

## 四个阶段
1. `Historical Reconciliation`
   - 为每个主题形成连续历史理解链。
   - 退出条件：所有正式主题都补齐 `history_chain_template.md` 中的必需段落，且 `themes_missing_*` 计数清零。
2. `Clustering Setup`
   - 固定比较轴、纳入边界、排除边界与路线分化。
   - 退出条件：`themes_with_fixed_axes == target_theme_count`、`themes_with_exclusion_rules == target_theme_count`、`taxonomy_conflict_count = 0`。
3. `Modeling and Synthesis`
   - 正式写出主题级 synthesis 页面。
   - 退出条件：所有主题页补齐 `synthesis_page_template.md` 的必需段落，且 `unscoped_comparative_claims = 0`。
4. `Convergence / Closeout`
   - 收口 taxonomy、链接和跨层口径。
   - 这一阶段允许把 `synthesis/` 中已经隐含的总纲/子主题层级显式写清，但不得新增正式主题。
   - 退出条件：`cross_layer_link_issues = 0`、`orphan_shared_evidence_pages = 0`、`open_pass4_structural_gaps = 0`。

## 阶段退出原则
1. 每阶段都要满足 `WIKI_SCHEMA.md` 中对应的硬指标。
2. 任一计数项未归零，或任一目标计数未达标，都不得宣布阶段完成。
