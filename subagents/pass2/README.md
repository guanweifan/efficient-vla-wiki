# Pass 2 Subagent 配置

## 目标
用于 `Pass 2 | Reverse Calibration` 的正式执行配置。

## 编制
1. chief editor：1 个
2. worker subagent：2 个
3. 全部模型固定为：
   - `gpt-5.4`
   - `reasoning_effort = xhigh`

## 角色分工
### chief editor
负责：
1. 维护 `subagents/pass2/queue.md`
2. 按逆时间顺序切分 wave
3. 给 worker 下发统一校正规则
4. 抽查 worker 结果
5. 收紧全库口径
6. 更新共享文件：
   - `wiki/index.md`
   - `wiki/log.md`
   - `wiki/status.json`
   - `WIKI_SCHEMA.md`

### worker 1-2
每个 worker 只负责：
1. 处理分配给自己的 `wiki/papers/<stem>.md`
2. 必要时回读对应 `raw/*.pdf`
3. 必要时查对应 `extracts/` 的局部结果
4. 报告：
   - 修改了哪些页面
   - 哪些表述被收紧或拆开
   - 哪些问题仍需 chief editor 决策

## 写入边界
worker 允许写：
1. 自己负责的 `wiki/papers/<stem>.md`

worker 不允许写：
1. `wiki/index.md`
2. `wiki/log.md`
3. `wiki/status.json`
4. `WIKI_SCHEMA.md`
5. `wiki/evidence/*`
6. `wiki/synthesis/*`
7. 其他 worker 负责的 `wiki/papers/*.md`

## 工作目标
1. 校正，而不是重写。
2. 收紧过宽 `Claim`。
3. 拆开混写的 metric、benchmark、deployment setting。
4. 澄清 `method / system / evaluation` 的页面边界。
5. 提高 `Data Pointer` 的可用性，但不提前进入 `Pass 3` 的深证据模式。

## 默认阅读路径
1. `wiki/papers/<stem>.md`
2. `raw PDF`
3. `pdftotext`
4. `pdftotext -bbox-layout`
5. 仅在需要章节、表格、图片、caption 或局部锚点时，再查 `extracts/` 中的 `Docling/Marker`

## 波次建议
1. 每波 6 篇
2. 2 个 worker 各 3 篇
3. 按时间顺序从新到旧连续切块
4. 每波结束后由 chief editor 收口，再进入下一波

## 质量门槛
1. 不把 `Pass 2` 做成 `Pass 1` 的重写版。
2. 不把 `Pass 2` 提前做成 `Pass 3` 的深证据补全。
3. 证据不足时，可以保留 `待核`，不要硬压成稳定结论。
4. 若页面已经基本达标，允许做轻量校正，不强求大改。
