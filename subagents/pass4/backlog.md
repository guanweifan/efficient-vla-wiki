# Pass 4 Backlog

## 状态
1. 本文件记录 `Pass 4` 的主题候选、准入 gate 与阶段推进状态。
2. 在 `target_theme_set` 固定之前，不得开始正式 `Historical Reconciliation`。

## 主题准入 gate
1. 主题必须能压缩成一句明确问题。
2. 主题必须至少涉及 `3` 篇论文。
3. 主题必须至少有 `3` 个可回链的 `papers/evidence` 支点；若 evidence 稀疏，可用 `2` 个 evidence 支点加 `1` 个 `raw` fallback。
4. 主题必须能明确写出纳入边界与排除边界。

## 候选主题簇
1. efficiency definition evolution
2. inference efficiency routes: pruning / caching / speculative / async / streaming
3. training efficiency routes: distillation / compression / quantization / data-efficient adaptation
4. runtime / latency / frequency / task-performance metric boundaries
5. reasoning / think-act / dual-process efficiency routes
6. deployment-oriented efficiency: edge / memory / system-level constraints

## 正式 target_theme_set
1. `efficiency-definition-evolution`
   - 问题：高效 VLA 的“效率”如何从粗粒度的“更快/更小”宣传，演化成必须分开讨论 runtime、task performance、training cost、deployment constraint 与 wording boundary 的多轴定义？
   - 文件：`wiki/synthesis/efficiency-definition-evolution.md`
2. `inference-efficiency-routes`
   - 问题：推理期高效 VLA 如何从局部 token/cache 复用，演化到 pruning、caching、speculative / parallel decoding、async / streaming control 这些更广的 compute-allocation 路线？
   - 文件：`wiki/synthesis/inference-efficiency-routes.md`
3. `training-efficiency-routes`
   - 问题：高效 VLA 如何把“训练侧成本”从附属问题变成独立议程，逐步转向 tokenization、teacher distillation、synthetic coreset 与低成本 adaptation？
   - 文件：`wiki/synthesis/training-efficiency-routes.md`
4. `reasoning-efficiency-routes`
   - 问题：VLA 如何在保留 reasoning 收益的同时，逐步摆脱显式 CoT 的 latency / control overhead，转向 latent、gated 与 dual-process efficiency 设计？
   - 文件：`wiki/synthesis/reasoning-efficiency-routes.md`
5. `deployment-oriented-efficiency`
   - 问题：边缘部署、显存约束、频率目标、系统 placement 与 jitter 何时成为高效 VLA 的一等设计对象，而不是事后补充指标？
   - 文件：`wiki/synthesis/deployment-oriented-efficiency.md`
6. 上述 `5` 个主题已通过准入 gate，是当前 `Pass 4 Stage 1` 的正式目标集合。

## Stage 1 结果
1. `target_theme_set` 已固定，共 `5` 个正式主题。
2. 当前无 `Insufficient historical depth` 标记主题。
3. `5 / 5` 个历史链页面已建立在 `wiki/synthesis/`。
4. 这些历史链页面已作为 `Pass 4 Stage 2 | Clustering Setup` 的输入基线。

## Stage 2 结果
1. `5 / 5` 个正式主题都已固定 comparison axes。
2. `5 / 5` 个正式主题都已固定纳入边界与排除边界。
3. `5 / 5` 个正式主题都已固定 route split；当前无 `misc bucket` 主题。
4. 当前 `taxonomy_conflict_count = 0`。
5. 这些固定骨架已作为 `Pass 4 Stage 3 | Modeling and Synthesis` 的输入基线。

## Stage 3 结果
1. `5 / 5` 个正式主题页都已改写为正式 synthesis 页面。
2. 当前 `synthesis_pages_missing_required_sections = 0`。
3. 当前 `synthesis_pages_missing_evidence_links = 0`。
4. 当前 `unscoped_comparative_claims = 0`。
5. 当前 `themes_without_boundary_conditions = 0`。
6. 下一步：`Pass 4 Stage 4 | Convergence / Closeout`。

## Stage 4 结果
1. `papers / evidence / synthesis` 三层一致性审计已完成，当前 `cross_layer_link_issues = 0`。
2. 共享 `metrics / wording` evidence 页都已确认被正式主题页复用，当前 `orphan_shared_evidence_pages = 0`。
3. 当前主题层级已显式收口：
   - `efficiency-definition-evolution` 为总纲 / 入口页
   - 其余 `4` 个主题为路线或场景子主题页
4. 当前 `taxonomy_conflict_count = 0`，`open_pass4_structural_gaps = 0`。
5. `index / log / status` 已同步到 `Pass 4 Stage 4 | Convergence / Closeout completed`。

## 阶段 gate
1. Stage 1 不得开始，除非 `target_theme_set` 已固定。
2. Stage 2 不得开始，除非所有主题都有历史链草稿且通过阶段 1 验收。
3. Stage 3 不得开始，除非所有主题都有固定 comparison axes、纳入边界与 route split。
4. Stage 4 不得开始，除非所有主题页都已成稿并通过阶段 3 验收。
