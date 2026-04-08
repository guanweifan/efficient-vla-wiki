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
3. 默认主阅读路径在 `Pass 0` 建立后变为：
   - `raw PDF`
   - `pdftotext`
   - `pdftotext -bbox-layout`
   - 只有在需要章节、表格、图片、caption 或局部锚点时，才调用 `Docling/Marker`
4. `Pass 1` 求全不求深；在建立全局地图时，优先把单篇页面写稳，而不是过早扩写或建模。

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

## 5. Workflow Modes
### 5.1 Bootstrap Build
1. 这一模式只用于冷启动建库，或现有 `wiki/` 过薄、需要重新建立全局地图时。
2. `Pass 0 | Parse Baseline`
   - 对全量 `raw/*.pdf` 执行 full parse baseline。
   - 目标是建立可定位、可检索、可回读的 `extracts/` 参考层。
   - 默认只写 `extracts/`、`extracts/pass0_status.json` 与 `extracts/pass0_index.jsonl`，不默认写 `wiki/` 页面。
3. `Pass 1 | Semantic Scan`
   - 默认按时间顺序从旧到新遍历。
   - 对每篇论文先建立 `papers/<stem>.md` 的第一版。
   - 第一版只要求写清 `Claim`、`Methodology Index`、`Data Pointer`，不默认深挖所有细节。
4. `Pass 1` 在模板稳定后允许并行执行；默认编制是：
   - 1 个 chief editor
   - 4 个 worker subagent
   - 全部使用 `gpt-5.4` + `xhigh`
5. `Pass 1` 并行时，worker 只负责各自分配到的 `wiki/papers/<stem>.md`；chief editor 负责：
   - 批次切分
   - 模板与口径
   - 抽查与归一化
   - `wiki/index.md`
   - `wiki/log.md`
   - `wiki/status.json`
   - 所有 `synthesis/` 页面
6. `Pass 1` 的推荐波次是按时间顺序连续切块；早期波次优先采用每波 8 篇、4 个 worker 各处理 2 篇。
7. 只有在至少一轮已完成波次证明口径稳定、chief editor 收口成本可控后，才把 `Pass 1` 提升到每波 12 篇、4 个 worker 各处理 3 篇。

## 6. Tooling Policy
1. 解析层是参考材料，不是 wiki 本体；当前实现目录是 `extracts/parses/<stem>/`。
2. `Pass 0` 优先通过纯脚本流水线执行，而不是通过会话式 worker 执行。
3. `Pass 0` 既可用于冷启动全量解析，也可用于新增论文的局部解析；默认只处理目标 PDF，不主动重写无关 parse 结果。
4. steady-state 工具入口固定为仓库 `.venv/bin`：
   - `.venv/bin/docling`
   - `.venv/bin/marker_single`
5. `uvx` 只用于环境修复、冷启动诊断或确认工具可用性；不作为常规解析入口。
6. 对新论文，当前默认仍执行 `Docling + Marker` 的 full parse baseline，包括：
   - `Docling`：`md + json`
   - `Marker`：`md + meta + figure crops`
   - `pdftotext`
   - `pdftotext -bbox-layout`
   - `pdfinfo` 仅用于运行时提取页数，不默认落盘
7. `Pass 0` 应优先追求“最大化帮助后续 wiki 搭建”的解析粒度，而不是最小产物。
8. 当前建议的 `Docling` 持久化产物至少包括：
   - `md`
   - `json`
9. 当前建议的 `Marker` 持久化产物至少包括：
   - `markdown`
   - `meta`
   - figure/image crops
10. 为保证后续 pass 可直接消费，`extracts/parses/<stem>/` 默认采用可检索布局：
   - 根目录：`pdftotext.txt`、`pdftotext.bbox.html`、`manifest.json`
   - `docling/`：`md + json`
   - `marker/markdown/`：markdown、meta 与提取图片
11. `Docling` 是 canonical parser，优先承担结构化证据提取。
12. `Marker` 是 companion parser，优先承担 Markdown 可读性、图像裁剪与交叉校验。
13. `pdftotext` 与 `bbox-layout` 是精定位兜底层。
14. `Pass 0` 的脚本需要维护全局状态文件，例如 `extracts/pass0_status.json` 与 `extracts/pass0_index.jsonl`，便于后续 pass 与人工检查。
15. 默认不保留常规运行日志、`Marker JSON`、`Docling HTML/TXT`、`pdfinfo.txt` 与 `pdfimages.list.txt`；这些属于可再生或低收益产物，应在 parse 后清理。
16. 在 `Pass 1` 中，默认主阅读路径不是 `Docling/Marker` 全量文本，而是：
   - `raw PDF`
   - `pdftotext`
   - `pdftotext -bbox-layout`
   - 在需要章节、表格、图片或局部锚点时再查 `Docling/Marker`
17. `Docling/Marker` 结果默认按特定需求调用，不应作为首轮语义扫描的唯一输入，也不应替代对 `raw/` 的最终核对。
18. `Pass 1` 使用 subagent 时，worker 默认模型配置可固定为：
   - `model = gpt-5.4`
   - `reasoning_effort = xhigh`
19. `Pass 1` 使用 subagent 时，chief editor 不应把共享文件写权限下放给 worker；共享文件统一由 chief 收口。
20. `Pass 1` 的 `L1` 页面允许略高于最小模板的信息密度；只要仍停留在单篇层、未越界到 synthesis，且待核点写清，就不必为了“更短”而硬压缩。
21. `Pass 1` 的 headline 数字主张允许保留在 `Claim` 中，但必须同时保留相应 caveat 或待核点，避免误写成已完全钉实的结构化证据。
22. 若 worker 接手时发现目标页面已经存在且满足 `L1`，可以选择做轻量审校而不是强行重写；但需明确报告自己实际修改了哪些内容，避免无意义 churn。
