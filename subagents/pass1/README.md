# Pass 1 Subagent 配置

## 目标
用于 `Pass 1 | Semantic Scan` 的并行执行配置。

## 编制
1. chief editor：1 个
2. worker subagent：4 个
3. 全部模型固定为：
   - `gpt-5.4`
   - `reasoning_effort = xhigh`
4. 推荐模板见：
   - `subagents/pass1/paper_l1_template.md`
   - 它是推荐骨架，不是硬模板。

## 角色分工
### chief editor
负责：
1. 选择当前 wave 的论文
2. 把论文按时间顺序切成 4 个连续小块
3. 向 worker 下发统一模板
4. 抽查 worker 结果
5. 统一修正口径
6. 更新共享文件：
   - `wiki/index.md`
   - `wiki/log.md`
   - `wiki/status.json`
   - `WIKI_SCHEMA.md`
   - `wiki/synthesis/*`

### worker 1-4
每个 worker 只负责：
1. 读取自己分配到的 `raw/*.pdf`
2. 必要时读取对应 `extracts/`
3. 写自己负责的 `wiki/papers/<stem>.md`
4. 在结果里明确：
   - 完成的页面
   - 待核点
   - 需要 chief editor 决策的问题

## 写入边界
worker 允许写：
1. 自己负责的 `wiki/papers/<stem>.md`

worker 不允许写：
1. `wiki/index.md`
2. `wiki/log.md`
3. `wiki/status.json`
4. `WIKI_SCHEMA.md`
5. `wiki/synthesis/*`
6. 其他 worker 负责的 `wiki/papers/*.md`

## 默认阅读路径
1. `raw PDF`
2. `pdftotext`
3. `pdftotext -bbox-layout`
4. 仅在需要章节、表格、图片、caption 或局部锚点时，再查 `Docling/Marker`

## 每篇论文最低交付
1. `Claim`
2. `Methodology Index`
3. `Data Pointer`
4. `待核点`

## 波次建议
1. 早期波次优先每波 8 篇
2. 4 个 worker 各 2 篇
3. 按时间顺序连续切块
4. 每波结束后由 chief editor 抽查至少 20% 页面，再决定是否提升到 3 篇/worker

## 质量门槛
1. 不把 `Docling/Marker` 全量文本当作默认主阅读材料
2. 不提前写 synthesis
3. 不把泛摘要写成 `Claim`
4. `Data Pointer` 必须能回到具体页码、图、表或局部锚点
5. 证据不足时写 `待核`，不要硬补
6. 可以保留 headline 数字主张，但必须同时暴露 caveat 或待核点
7. 如果接手时页面已满足 `L1`，允许做轻量审校，不强制重写
