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
2. `Pass 1` 求全不求深；`Pass 3` 求关键证据最扎实，不追求平均深挖。
3. 默认主阅读路径始终是：
   - `raw PDF`
   - `pdftotext`
   - `pdftotext -bbox-layout`
   - 只有在需要章节、表格、图片、caption 或局部锚点时，才调用 `Docling/Marker`
4. 每个 `synthesis/` 页面都必须能回落到具体的 `papers/`、`evidence/` 或 `raw/`；不允许空中建模。
5. 新论文进入后，默认动作不是“只新建一个 paper page”，而是：
   - 建立或补强该论文的 `papers/<stem>.md`
   - 做 impact analysis
   - 更新受影响页面
6. `Pass 5` 不是收尾装饰，而是常规质量控制；每完成一轮显著增量维护或一个主题块后，都应至少执行一次轻量 `lint/reflect`。

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

## 4. Workflow Modes
### 4.1 Bootstrap Build
1. 这一模式只用于冷启动建库，或现有 `wiki/` 过薄、需要重新建立全局地图时。
2. `Pass 0 | Parse Baseline`
   - 对全量 `raw/*.pdf` 执行 full parse baseline。
   - 目标是建立可定位、可检索、可回读的 `extracts/` 参考层。
   - 默认只写 `extracts/`、`extracts/pass0_status.json` 与 `extracts/pass0_index.jsonl`，不默认写 `wiki/` 页面。
3. `Pass 1 | Semantic Scan`
   - 默认按时间顺序从旧到新遍历。
   - 对每篇论文先建立 `papers/<stem>.md` 的第一版。
   - 第一版只要求写清 `Claim`、`Methodology Index`、`Data Pointer`，不默认深挖所有细节。
4. `Pass 2 | Reverse Calibration`
   - 默认按时间顺序从新到旧遍历。
   - 目标不是重写单篇页面，而是用较新的论文校准旧术语、旧问题定义与早期 `Claim` 边界。
   - 只在必要时回读原 PDF 局部，不默认重读全文。
   - 正式启动前，优先先做一轮可整体删除的 pilot；通过后再进入全量 `Pass 2`。
   - 当前推荐的启动配置是：
     - 1 个 chief editor
     - 2 个 worker subagent
     - 每个 worker 3 篇
   - 正式执行准备文件放在：
     - `subagents/pass2/README.md`
     - `subagents/pass2/worker_prompt.md`
     - `subagents/pass2/queue.md`
   - 只有在至少两波证明 worker 仍在做“校正页面”而不是“重写页面”，且 chief editor 收口成本可控后，才考虑提升 worker 数量。
5. `Pass 3 | Evidence Mining`
   - 回到关键图、关键表、关键 claim 与关键 wording。
   - 这一轮按信息价值排序，优先补：
     - 高频 claim
     - 关键术语定义
     - 常被引用的图表
     - 明显存在冲突的命题
   - 补足 supporting evidence pages，并把高价值命题从“指针”提升为“锚定证据”。
6. `Pass 4 | Clustering and Modeling`
   - 以主题而非单篇为中心，聚类共识、分歧与条件边界。
   - 在 `synthesis/` 中沉淀跨论文结构。
7. `Pass 5 | Audit and Reflect`
   - 执行 lint。
   - 把 `threads/` 中高价值、已核证的结论回写到 `wiki/`。
   - 不把 `Pass 5` 推迟到“全部完成以后”才做；冷启动过程中也应在关键里程碑后插入轻量检查。
8. `Pass 1` 在模板稳定后允许并行执行；默认编制是：
   - 1 个 chief editor
   - 4 个 worker subagent
   - 全部使用 `gpt-5.4` + `xhigh`
9. `Pass 1` 并行时，worker 只负责各自分配到的 `wiki/papers/<stem>.md`；chief editor 负责：
   - 批次切分
   - 模板与口径
   - 抽查与归一化
   - `wiki/index.md`
   - `wiki/log.md`
   - `wiki/status.json`
   - 所有 `synthesis/` 页面
10. `Pass 1` 的推荐波次是按时间顺序连续切块；早期波次优先采用每波 8 篇、4 个 worker 各处理 2 篇。
11. 只有在至少一轮已完成波次证明口径稳定、chief editor 收口成本可控后，才把 `Pass 1` 提升到每波 12 篇、4 个 worker 各处理 3 篇。

### 4.2 Incremental Update
1. 这一模式用于 `raw/` 新增论文后的日常维护，不重跑整库冷启动流程。
2. 新 PDF 进入 `raw/` 后，先对新增论文执行局部 `Pass 0`，只更新对应的 `extracts/` 目录与全局 parse 状态文件。
3. 对新增论文执行 `L1 | Scan Layer`：
   - 建立或更新 `papers/<stem>.md`
   - 提取 `Claim`
   - 提取 `Methodology Index`
   - 提取 `Data Pointer`
4. 对新增论文执行 impact analysis，识别其会影响的已有页面，例如：
   - 相关 `papers/`
   - 相关 `evidence/`
   - 相关 `synthesis/`
   - `wiki/index.md`
5. 增量维护的默认动作是定点传播，不是整库重写：
   - 更新受影响页面
   - 补链接
   - 补冲突
   - 补条件边界
6. 只有当新增论文实质改变某个命题、图表比较、术语定义或主题边界时，才推进局部 `L2` 或局部 synthesis 更新。
7. 增量维护结束时，应同步更新 `wiki/log.md` 与 `wiki/status.json`。
8. 每轮显著增量维护结束后，应至少执行一次轻量 `Pass 5`，检查断链、遗漏回链与口径漂移。

### 4.3 Periodic Maintenance
1. 这一模式用于低频全库再平衡，不随每次新增论文自动触发。
2. 触发条件通常包括：
   - 新增论文积累到一定数量
   - 同一主题被多次增量修改
   - `threads/` 反复暴露同类结构缺口
   - taxonomy、术语边界或关键 synthesis 出现明显漂移
3. 周期维护可选择性重做：
   - 局部 `Reverse Calibration`
   - 局部 `Evidence Mining`
   - 主题级 `Clustering and Modeling`
   - 全库 `lint / reflect`
4. 周期维护的目标是全局一致性，不是重复冷启动。
5. query support：优先用 `wiki/` 回答；只要结论关键或 `wiki` 不足，就回读 `raw/` 与必要的 `extracts/` 局部结果。
6. `threads/` 中反复出现的问题，可促使新建或重构 wiki 页面。
7. `threads/` 中形成的稳定结论，只有在重新核对 `raw/` 后，才可写入 `wiki/`。
8. reflect 不应只改 narrative page；必要时应同步更新相关 evidence 页面与链接结构。
9. 论文未明确给出时，不替作者补观点。
10. 图像、表格或文字存在歧义时，明确标记为“待核”。
11. parser 之间冲突时，以原 PDF 复核结果为准。
12. 证据不足时，宁可保留空缺，也不要伪装成稳定知识。

## 5. Tooling Policy
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
14. 在 `Pass 1-5` 中，默认主阅读路径不是 `Docling/Marker` 全量文本，而是：
   - `raw PDF`
   - `pdftotext`
   - `pdftotext -bbox-layout`
   - 在需要章节、表格、图片或局部锚点时再查 `Docling/Marker`
15. `Docling/Marker` 结果默认按特定需求调用，不应作为首轮语义扫描的唯一输入，也不应替代对 `raw/` 的最终核对。
16. 后续 pass 默认不得把某篇论文的 `Docling/Marker` 全量输出整份塞入当前主上下文；应只读取与当前问题直接相关的局部片段、表格、caption 或结构化字段。
17. `Pass 0` 的脚本需要维护全局状态文件，例如 `extracts/pass0_status.json` 与 `extracts/pass0_index.jsonl`，便于后续 pass 与人工检查。
18. 默认不保留常规运行日志、`Marker JSON`、`Docling HTML/TXT`、`pdfinfo.txt` 与 `pdfimages.list.txt`；这些属于可再生或低收益产物，应在 parse 后清理。
19. `Pass 1` 使用 subagent 时，worker 默认模型配置可固定为：
   - `model = gpt-5.4`
   - `reasoning_effort = xhigh`
20. `Pass 1` 使用 subagent 时，chief editor 不应把共享文件写权限下放给 worker；共享文件统一由 chief 收口。
21. `Pass 1` 的 `L1` 页面允许略高于最小模板的信息密度；只要仍停留在单篇层、未越界到 synthesis，且待核点写清，就不必为了“更短”而硬压缩。
22. `Pass 1` 的 headline 数字主张允许保留在 `Claim` 中，但必须同时保留相应 caveat 或待核点，避免误写成已完全钉实的结构化证据。
23. 若 worker 接手时发现目标页面已经存在且满足 `L1`，可以选择做轻量审校而不是强行重写；但需明确报告自己实际修改了哪些内容，避免无意义 churn。

## 6. Depth Levels
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
