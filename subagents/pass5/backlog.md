# Pass 5 Backlog

## 状态
1. 本文件记录 `Pass 5` 的审计范围、文档保留判定与阶段推进状态。
2. `Pass 5` 不新增新的知识主题；它只审计、修正、精炼、删除、合并与收口已有内容。

## 审计范围
1. `wiki/papers/`
2. `wiki/evidence/`
3. `wiki/synthesis/`
4. `wiki/index.md`
5. `wiki/log.md`
6. `wiki/status.json`
7. `WIKI_SCHEMA.md`
8. `subagents/pass1-5/`
9. `skills/*`
10. 其他除 `AGENTS.md` 之外仍承担控制或说明作用的 `.md/.json` 文档

## 阶段目标
1. `Inventory and Retention Audit`
   - 固定所有文档的保留 / 精炼 / 合并 / 删除判定。
2. `Wiki Core Audit`
   - 固定 `papers / evidence / synthesis` 三层的结构与语义问题清单，并清零结构性缺口。
3. `Control and Docset Convergence`
   - 固定 `index / log / status / schema / subagent docs / skills docs` 的最终形态，并校正 Git 历史中的阶段表述与 commit message。
4. `Final Closeout`
   - 确认剩余问题全部降级为维护项。

## Stage 1 结果
1. 文档清单已固定，详见 `subagents/pass5/doc_inventory.md`。
2. 当前没有未决保留判定文档。
3. 已删除低保留价值运行态文档：`subagents/pass2/queue.md`。
4. 已精炼高噪声控制文件：`wiki/index.md`、`wiki/log.md`、`wiki/status.json`。
5. 已校正文档范围描述，使 `Pass 5` 明确覆盖 `subagents/pass1-5/` 与 `skills/*`。

## Stage 2 结果
1. `papers / evidence / synthesis` 三层结构与语义审计已完成。
2. 当前 gate 已清零：
   - `broken_wiki_links = 0`
   - `paper_pages_missing_evidence_links = 0`
   - `evidence_pages_missing_raw_anchor = 0`
   - `synthesis_claims_without_evidence = 0`
   - `unscoped_comparative_claims = 0`
   - `cross_layer_role_conflicts = 0`
3. 已修复 `VLA-Cache` 正式证据链中越界依赖 `extracts` 的问题，确保事实链回到 `raw/`。
4. 已补齐 `inference-efficiency-routes` 中正文已使用但未显式列入 `Evidence Links` 的 paper anchors。

## Stage 3 结果
1. 当前控制文件与文档系统已收口到完成态。
2. Git 历史中的阶段快照已校正，阶段性 `index / log / status` 现与对应阶段语义一致。
3. 低保留价值运行态文档 `subagents/pass2/queue.md` 已从历史中移除。
4. commit subject 已统一为中文、阶段式、里程碑式表达。
5. 当前可进入 `Pass 5 Stage 4 | Final Closeout`。

## Stage 4 结果
1. 已复核 `Pass 5 Stage 1-3` 的全部 gate，确认没有阶段回退或控制文件再次漂移。
2. 已确认 `papers / evidence / synthesis` 三层、当前控制文件与重写后的 `main` 历史主线保持一致。
3. 已确认剩余问题全部属于后续维护项，而不再是 bootstrap 结构性缺口。
4. 当前仓库已从“构建态”切换为“可维护态”。
5. 冷启动建库已正式结束；后续默认模式改为 `Incremental Update` 与 `Periodic Maintenance`。
