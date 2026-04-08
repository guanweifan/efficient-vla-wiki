# Pass 5 准备说明

## 目标
1. `Pass 5` 负责对当前仓库执行最终审计与收口，证明其已从“构建态”进入“可维护态”。
2. `Pass 5` 不再承担新的大规模知识扩写；只允许修正、精炼、删除、合并或收口现有内容。
3. `Pass 5` 的审计范围包括：
   - `wiki/papers/`
   - `wiki/evidence/`
   - `wiki/synthesis/`
   - `wiki/index.md`
   - `wiki/log.md`
   - `wiki/status.json`
   - `WIKI_SCHEMA.md`
   - `subagents/pass1-5/`
   - `skills/*`
   - 其他除 `AGENTS.md` 之外仍承担控制或说明作用的 `.md/.json` 文档
4. `Pass 5` 的后半段还负责校正 Git 历史中的阶段表述、控制文件快照与 commit subject 风格，使当前仓库与历史演化叙事保持一致。

## 默认工作模式
1. `chief-editor` 串行审计和收口正式仓库内容。
2. `sidecar` 只允许做只读核查、链接检索或锚点定位，不允许并发写正式页面。
3. `Pass 5` 不负责建立 `threads/`；`threads/` 由用户主导。

## 四个阶段
1. `Inventory and Retention Audit`
   - 建立文档清单，并为每个文档做：保留 / 精炼 / 合并 / 删除 判定。
2. `Wiki Core Audit`
   - 审计 `papers / evidence / synthesis` 三层是否仍然可回链、无错链、无无证据归纳。
3. `Control and Docset Convergence`
   - 收口 `index / log / status / schema / subagent docs / skills docs`，并对 Git 历史中的阶段表述与 commit message 做一致性校正。
4. `Final Closeout`
   - 确认剩余问题都已降级为维护项，并将冷启动流程正式关闭。

## 阶段退出原则
1. 每阶段都要满足 `WIKI_SCHEMA.md` 中对应的硬指标。
2. 任何 `*_unresolved`、`*_missing_*`、`*_conflict_*`、`*_gaps` 计数不为 `0`，都不得宣布阶段完成。
