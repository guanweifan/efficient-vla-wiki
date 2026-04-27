# WIKI_SCHEMA.md

## 1. 角色与优先级
1. 本文件定义 agent 维护 `wiki/` 的结构规范、证据规则和维护流程。
2. 优先级始终为：**用户当前明确指令 > `AGENTS.md` > 本文件**。
3. 当现有 schema 已经不能稳定支撑维护时，agent 应直接更新本文件，使其与当前仓库状态保持一致。

## 2. Knowledge Model

### 2.1 层级边界
1. `raw/` 是唯一事实来源。
2. `extracts/` 是阅读辅助层，用于定位、检索和结构化辅助；它不是事实来源。
3. `wiki/` 是稳定知识层，只收录已经核证、可维护、可复用的内容。
4. `threads/` 是问题讨论层，用于承载问题、推理、分歧、阶段性判断和未决项；它不是事实来源。
5. `scripts/release/`、`scripts/release/manifests/`、`docs/` 都属于工具或说明层，不得作为事实来源。

### 2.2 `wiki/` 的默认骨架
1. `wiki/index.md`
   - 对外展示当前结构、规模和入口。
2. `wiki/log.md`
   - 本地维护日志；只记录 `wiki/` 知识层及其 `index/status` 控制面的显著更新。
3. `wiki/status.json`
   - 保存机器可读的控制面和摘要状态。
4. `wiki/papers/`
   - 单篇论文页，默认原子层。
5. `wiki/evidence/`
   - 可复用证据页。
6. `wiki/synthesis/`
   - 跨论文的稳定建模页。

### 2.3 页面职责
1. `papers/`
   - 承载单篇论文的稳定笔记。
   - 默认是所有跨论文比较的下层落点。
2. `evidence/`
   - 承载会被多个页面复用的图表、claim、metric、wording 或边界说明。
   - 不承担主题级总结。
3. `synthesis/`
   - 承载跨论文的聚类、关系、冲突、比较轴和主题建模。
   - 必须能回落到 `papers/`、`evidence/` 或 `raw/`。

### 2.4 结构原则
1. `papers/` 是默认原子层；不要长期绕开 `papers/` 直接堆主题页。
2. taxonomy 必须自底向上归纳，不预设外部框架。
3. 若已有页面足以承载信息，就不要新增页面。
4. 若多个页面重复搬运同一证据，应优先抽取为 `evidence/` 页面。
5. 若某个内容仍依赖具体问题上下文才能成立，就应留在 `threads/`，不要提前写入 `wiki/`。

## 3. Page Model

### 3.1 `papers/<stem>.md`
1. 目标：建立单篇论文的稳定落点。
2. 最低要求：
   - `Source`
   - `Claim`
   - `Methodology Index`
   - `Data Pointer`
3. 可按需要补：
   - `Evidence Links`
   - `Pending / 待核点`
4. 单篇页优先写：
   - 论文想解决什么问题
   - 核心方法组件
   - 后续应回读的图、表、章节、实验段
5. 单篇页不应提前变成主题综述页。

### 3.2 `wiki/evidence/*`
1. 目标：沉淀可复用、可回链、不可混写的证据单元。
2. 常见类型：
   - `claims`
   - `metrics`
   - `wording`
3. 推荐内容：
   - `用途`
   - `Evidence`
   - `不可混写项`
   - `影响页面`
   - `边界`
4. evidence 页只做最小必要归纳，不做主题级 synthesis。

### 3.3 `wiki/synthesis/*`
1. 目标：沉淀跨论文的稳定结构。
2. 当前正式主题页应尽量包含：
   - `Question`
   - `Shared Ground`
   - `Route Split`
   - `Boundary Conditions`
   - `Not Directly Comparable`
   - `Evidence Links`
   - `Open Questions`
3. synthesis 页必须显式区分：
   - 论文原始事实
   - 跨论文共识
   - 冲突或不可直接比较项
   - agent 的归纳
4. synthesis 页不得只引用其他 synthesis 页；证据链必须能回到下层。

### 3.4 控制文件
1. `wiki/index.md`
   - 应反映当前结构和入口，不写过细历史。
2. `wiki/log.md`
   - 本地私有维护日志；只记录有维护价值的 `wiki/` 更新，不写低价值流水账。
   - 不记录外部子模块、release 工具、docs、skills、Git 历史清理等非 wiki 内容。
   - 若 `wiki/log.md` 已被 `.gitignore` 忽略，则公开维护时不要求同步它，公开控制面以 `wiki/index.md` 与 `wiki/status.json` 为准。
3. `wiki/status.json`
   - 应至少包含：
     - `mode`
     - `current_stage`
     - `initial_build.status`
     - `summary`
     - `updated_at`
   - 其余字段按当前维护需要保留，不要求为历史阶段保留整套冗余结构。

## 4. Evidence Model

### 4.1 基本规则
1. 所有事实性表述都必须能回到 `raw/`。
2. 解析器输出、旧 wiki 页面、thread 结论、文件名和常识都不能单独构成证据闭环。
3. 无法直接从 `raw/` 支持的内容，不进入 `wiki/` 正文。
4. 证据不足时必须写明：
   - `未提及`
   - `不确定`
   - `待核`

### 4.2 默认阅读路径
1. `raw PDF`
2. `pdftotext`
3. `pdftotext -bbox-layout`
4. 仅在需要章节、表格、图片、caption 或局部锚点时，再查 `Docling/Marker`

### 4.3 证据粒度
1. 只回到“某一页”通常只是临时态，不是理想态。
2. 对重要事实，优先记录：
   - 页码
   - section / figure / table 编号
   - 局部片段或局部描述
3. 对关键图、关键表、关键 claim 和关键 wording，优先回到具体局部锚点。
4. 复杂表格、关键措辞或 parser 冲突场景下，可使用 bbox 或更细粒度定位。

### 4.4 写法要求
1. 优先提取可验证命题，不优先写泛摘要。
2. 重要证据推荐写成统一格式，例如：
   - `来源：[[raw/2602_00686_LAC.pdf]]，第 3 页，Fig. 2 caption。`
3. 若多个论文不可直接比较，必须明确写“不可直接比较”及其原因。
4. 不把不同 benchmark、metric、setting、deployment layer 的结果压成同一句 superiority claim。

### 4.5 何时抽 evidence 页
1. 同一证据会被两个及以上页面复用。
2. 同一表 / 图 / 定义已经开始承载共享 metric、共享 wording 或共享边界说明。
3. 某个 bundled claim 已经影响跨论文比较，必须拆开。
4. 某个证据如果只服务单篇页，就先留在 `papers/`，不要提前抽页。

## 5. Maintenance Workflows

### 5.1 总原则
1. 默认工作流是：先读 `wiki/` 建立上下文，再在关键判断、细节敏感、存在冲突或 `wiki/` 不足时回到 `raw/` 复核。
2. 默认优先做最小必要更新，不做无边界扩写。
3. 每次改动都要明确：
   - 哪些内容写进 `wiki/`
   - 哪些内容保留在 `threads/`
   - 哪些内容只是中间过程

### 5.2 Initial Build
1. 只在两种情况下使用：
   - 仓库刚建立；
   - 现有 `wiki/` 过薄，无法支撑维护。
2. 基本顺序：
   - 全量 extract build
   - 建立 `papers/`
   - 补可复用 `evidence/`
   - 建立 `synthesis/`
   - 做 closeout audit
3. 这一模式用于建立全局地图，不是日常入口。

### 5.3 Incremental Update
1. 这是默认维护模式。
2. 适用场景：
   - `raw/` 新增论文；
   - 新论文改变了现有页面的边界、比较轴或共享证据。
3. 基本顺序：
   - 为新增论文补 `raw/` 与局部 `extracts/`
   - 建立或补强对应 `papers/<stem>.md`
   - 做 impact analysis
   - 只更新受影响的 `evidence/`、`synthesis/`
   - 同步 `index / status`；若维护者本地启用 `wiki/log.md`，可补记本轮 `wiki/` 更新，但不公开跟踪。
4. 默认动作是定点传播，不是整库重写。
5. 若新增论文只是重复已有模式，可停在 `papers/` 层。

### 5.4 Thread-driven Reflect
1. 当 `threads/` 中已经出现稳定、可复核、可复用的命题时，才回写到 `wiki/`。
2. reflect 的默认单位是“可核证命题”，不是整篇 thread。
3. 基本顺序：
   - 从 thread 拆命题
   - 回到 `raw/` 或下层页面复核
   - 以最小落点回写 `paper / evidence / synthesis`
   - 未稳定内容继续留在 `threads/`

### 5.5 Lint and Closeout Audit
1. lint 用于维护态缺陷检查和局部修复。
2. closeout audit 用于显著维护之后的收口检查。
3. 重点检查：
   - 断链
   - `raw` 锚点缺失
   - paper 页漏挂 evidence
   - synthesis 页 Evidence Links 漏挂
   - `index / status` 失配；若本地启用 `wiki/log.md`，可同时检查本地日志是否漏记 `wiki/` 更新。
   - 页面职责串位
4. 这两类流程不负责吸收新论文，也不负责凭空生成新知识。

### 5.6 Periodic Maintenance
1. 这是低频全库再平衡。
2. 触发条件通常包括：
   - 新增论文积累到一定数量
   - 同一主题被多次定点修改
   - `threads/` 反复暴露同类结构缺口
   - taxonomy、术语边界或关键 synthesis 漂移
3. 周期维护可以重做局部校正、补证据、重写主题页或全库 lint/reflect。
4. 目标是恢复全局一致性，不是重复做一次初始建库。

## 6. Tooling Policy
1. extract build 的当前脚本是：
   - `scripts/build_extracts.py`
2. 增量吸收新论文的当前脚本是：
   - `scripts/ingest_update.py`
3. 同步与分发相关脚本位于：
   - `scripts/release/`
4. `scripts/release/`、`scripts/release/manifests/` 只负责分发和操作元数据，不负责事实。

### 6.1 `extracts/` 的角色
1. `extracts/` 是参考材料，不是 wiki 本体。
2. 当前解析目录布局是：
   - `extracts/parses/<stem>/`
   - `extracts/meta/extract_build_status.json`
   - `extracts/meta/extract_build_index.jsonl`
3. 对单篇论文，常用解析产物包括：
   - `pdftotext.txt`
   - `pdftotext.bbox.html`
   - `manifest.json`
   - `docling/`
   - `marker/markdown/`

### 6.2 工具使用原则
1. `uv run python ...` 是公开文档的默认命令入口。
2. 不在脚本或文档里写死本机 Python 解释器路径。
3. extract build 默认只处理目标 PDF，不主动重写无关 parse 结果。
4. `Docling` 和 `Marker` 默认按需局部读取，不整份灌入上下文。
5. `pdfinfo`、运行日志等低价值、可再生产物不作为长期保留对象。

## 7. Depth Levels
1. `L1 | Scan Layer`
   - 目标：让论文进入全局地图。
   - 最小产物：`papers/<stem>.md`
   - 最小内容：`Claim`、`Methodology Index`、`Data Pointer`
2. `L2 | Evidence Layer`
   - 目标：把高价值命题钉到具体证据。
   - 常见产物：`claims`、`metrics`、`wording`
3. `L3 | Integration Layer`
   - 目标：让论文稳定参与跨论文比较与主题建模。
4. 一篇论文完成 `L1` 后即可先进入下一篇，不要求第一轮就做到 `L2` 或 `L3`。

## 8. 维护时的硬约束
1. 不把 parser 输出当事实来源。
2. 不把 thread 文本直接复制进 wiki 当证据。
3. 不把 README、仓库名、历史写法或常识印象写成事实。
4. 不为“可能以后会用到”而预留大量结构。
5. 不为了统一文风而抹平本应保留的边界、冲突和 caveat。
