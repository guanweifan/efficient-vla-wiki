# WIKI_SCHEMA.md

## 1. 角色与优先级
1. 本文件定义 agent 维护 `wiki/` 的内部规范。
2. 执行顺序：**用户当前明确指令 > `AGENTS.md` > 本文件**。
3. 当现有 schema 无法稳定支撑 `wiki/` 维护时，agent 应主动更新本文件。

## 2. Knowledge Model
1. `raw/` 是唯一证据层；`wiki/` 只能建立在 `raw/` 之上。
2. `threads/` 是问题与修正来源，不是事实来源。
3. `extracts/` 是参考层，不是事实层，也不是 wiki 本体。
4. `extracts/` 中的解析结果只能作为阅读辅助、定位辅助与结构化辅助；不能直接替代对 `raw/` 的核对。
5. `extracts/` 不是默认主阅读上下文；除非当前任务明确需要结构化辅助，否则不应整份加载 `Docling/Marker` 全量结果。
6. 先做 evidence，再做 synthesis；先逐篇建立理解，再归纳跨篇结构。
7. taxonomy 必须自底向上归纳，不得预设外部分类框架。
8. `wiki/` 是人读的持久知识层；其默认骨架包括：
   - `wiki/index.md`
   - `wiki/log.md`
   - `wiki/status.json`
   - `wiki/papers/`
   - `wiki/evidence/`
   - `wiki/synthesis/`
9. `papers/` 是默认原子层；`synthesis/` 不应长期绕开 `papers/` 独立生长。
10. supporting evidence pages 可按需要组织，当前常用类型包括：
   - `figures`
   - `tables`
   - `claims`
   - `wording`
11. 当前工作前端是 Obsidian；内部链接默认优先使用 `wikilink`。
12. 单篇论文的处理深度采用分层推进，而不是默认一次打满。
13. `papers/` 页面主要承载 source-grounded note；`synthesis/` 页面主要承载跨论文的聚类、冲突与建模。

## 2.1 Execution Principles
1. `raw/` 永远是事实源；`extracts/` 只是参考层，不得反客为主。
2. 每个 `synthesis/` 页面都必须能回落到具体的 `papers/`、`evidence/` 或 `raw/`；不允许空中建模。

## 3. Evidence Model
1. 只回到“某一页”通常只算临时态，不算理想态。
2. 优先提取可验证命题，不优先写泛摘要。
3. 第一轮单篇处理默认只要求提取：
   - `Claim`
   - `Methodology Index`
   - `Data Pointer`
4. 对重要事实，优先记录：
   - 页码
   - section / figure / table 编号
   - 局部片段或局部描述
5. 对图、表、重要 claim 与重要 wording，优先回到具体局部锚点，而不是仅写页码。
6. 必要时可使用 bbox 或 word 级坐标，尤其是在关键措辞、复杂表格或 parser 冲突场景。
7. 重要证据默认写成统一格式，例如：`来源：[[raw/2602_00686_LAC.pdf]]，第 3 页，Fig. 2 caption。`
8. 无法直接从 `raw/` 支持的内容，不进入 `wiki/` 正文。
9. 解析器输出、旧 wiki 页面或 thread 结论都不能单独构成证据闭环；最终必须落回 `raw/`。
10. `synthesis/` 页面不得只引用其他 `synthesis/` 页面；证据链必须能落回 `papers/`、`evidence/` 或 `raw/`。
11. `synthesis/` 应显式区分：
   - 论文原始事实
   - 跨论文共识
   - 分歧
   - agent 的归纳
12. 若多个论文不可直接比较，应明确写“不可直接比较”，不要强行并表。

## 4. Depth Levels
1. `L1 | Scan Layer`
   - 目标：让该论文进入全局地图。
   - 最小产物：`papers/<stem>.md`
   - 最小内容：`Claim`、`Methodology Index`、`Data Pointer`
2. `L2 | Evidence Layer`
   - 目标：把高价值命题锚定到具体证据。
   - 常见产物：`figures`、`tables`、`claims`、`wording`
3. `L3 | Integration Layer`
   - 目标：让该论文稳定参与跨论文比较与主题建模。
   - 进入条件：关键命题已有足够 evidence 支撑
4. 一篇论文在 `L1` 完成后即可先进入下一篇；不要求第一轮就到 `L2` 或 `L3`。
