---
name: wiki-ingest
description: 用于在冷启动完成后，把 raw/ 中新增或变更的论文增量吸收进 wiki/。在需要新建或补强 paper-level 页面、执行 impact analysis，并按 WIKI_SCHEMA 的增量维护流程更新相关页面时使用。
---

# Wiki Ingest

## 何时使用

- 冷启动已完成，`wiki/` 已具备基本骨架与已有页面。
- 需要从 `external/awesome-efficient-vla/update.md` 批量吸收新论文。
- `raw/` 中新增了论文 PDF。
- 某篇论文尚未进入 `wiki/`。
- 某篇论文已有页面，但因新增论文或新问题暴露而需要补强。

## 何时不使用

- 不用它代替整库冷启动建库。
- 不用它代替首次全库 `Pass 0-5`。
- 不用它处理“wiki 还几乎不存在”的状态；这种情况应先走 bootstrap。

## 先读什么

- 仓库根下的 `AGENTS.md`
- 仓库根下的 `WIKI_SCHEMA.md`

## 输入

- 默认入口：`external/awesome-efficient-vla/update.md`
- 一个或多个 `raw/*.pdf`
- 如有需要，可附带用户关注的问题，但它不能替代原文证据

## 核心原则

- 按 `WIKI_SCHEMA.md` 的 Knowledge Model、Evidence Model、Maintenance Workflows 和 Tooling Policy 执行。
- 这是增量维护 skill，不是 bootstrap 替代品。
- `raw/` 是唯一事实来源。
- `extracts/` 是参考层，不是主阅读层；后续 pass 不默认整份读取 `Docling/Marker` 全量输出。
- 工具链尽量薄：`update.md -> raw/ -> extracts/` 用脚本完成；`wiki/` 增量更新由 Codex 执行。
- 不额外保留低价值的 ingest 中间产物；以 `raw/`、`extracts/` 和最终 `wiki/` 结果为准。
- 先建 paper-level 证据，再扩写 synthesis。
- 默认先做到 `L1 | Scan Layer`；只有在当前论文或当前主题确实需要时，才立即推进到 `L2`。
- 默认执行 impact analysis，优先定点传播到受影响页面，而不是重写整库。

## 推荐流程

1. 用 `scripts/ingest_update.py` 读取 `external/awesome-efficient-vla/update.md`，提取 arXiv 链接，复用已有 `raw/*.pdf`，只下载缺失论文。
2. 由 `scripts/ingest_update.py` 调用 `scripts/pass0_parse.py --only ...`，只为新增论文生成局部 `extracts/`。
3. 确认本轮新增论文已经具备：
   - `raw/<stem>.pdf`
   - `extracts/parses/<stem>/manifest.json`
   - `pdftotext`
   - `bbox`
   - `Docling + Marker` 的局部参考材料
4. 先以原 PDF、`pdftotext` 与 `bbox` 为主阅读入口；仅在需要章节、表格、图片或局部锚点时再查 `Docling/Marker` 局部结果。
5. 回到原 PDF 与必要的 parse artifacts 建立或补强 `papers/<stem>.md` 的扫描层内容：
   - `Claim`
   - `Methodology Index`
   - `Data Pointer`
6. 对新增论文执行 impact analysis，识别它会影响的已有页面：
   - `papers/`
   - `evidence/`
   - `synthesis/`
   - `wiki/index.md`
7. 如当前论文包含高价值图表、关键定义或关键冲突，再按需补 supporting evidence。
8. 只有当新增论文实质改变某个命题、共享口径、主题边界或不可直接比较项时，才更新受影响的 `evidence/` 或 `synthesis/`。
9. 更新 `wiki/index.md`、`wiki/log.md` 与必要的 `wiki/status.json`。
10. 本轮改动显著时，再补一次轻量 `wiki-lint`。

## 工具入口

- 候选提取、下载与局部 parse：

```bash
.venv/bin/python scripts/ingest_update.py --source external/awesome-efficient-vla/update.md --json
```

- 只看计划，不落盘：

```bash
.venv/bin/python scripts/ingest_update.py --source external/awesome-efficient-vla/update.md --dry-run --json
```

- 只处理指定 arXiv：

```bash
.venv/bin/python scripts/ingest_update.py --source external/awesome-efficient-vla/update.md --only-arxiv 2604.04161 2604.05672 --json
```

- `scripts/ingest_update.py` 只负责：
  - 读取 `update.md`
  - 提取 arXiv
  - 去重
  - 下载缺失 PDF
  - 调用 `Pass 0`
- `wiki/` 的增量更新不脚本化，由 Codex 按证据执行。

## 执行约定

- 默认先跑一次 `--dry-run`，确认本轮唯一论文集合，再正式执行。
- 正式执行时，先收口 `raw/ + extracts/`，再开始改 `wiki/`；不要两段混着做。
- `wiki` 更新默认按 `papers -> evidence -> synthesis -> index/log/status` 的顺序推进。
- 一轮 ingest 默认只围绕本轮新增论文做定点传播；不顺手重写无关页面。
- 若新论文只是补了一个例子，没有改变共享口径、主题边界或冲突结构，就停在 `papers/` 层。
- 若某个主题页已经需要大面积重写，先停下并说明这更像一次 `Periodic Maintenance`，而不是继续把 ingest 扩大。

## 页面要求

- paper page 与 supporting evidence 的最小要求，以 `WIKI_SCHEMA.md` 为准。

## 增量更新判定

- `papers/<stem>.md`
  - 只要本轮新增论文进入仓库，就应新建或补强。
- `wiki/evidence/*`
  - 只有在以下情况才更新：
    - 单篇 headline 需要拆分；
    - 关键图表或 wording 会被复用；
    - 新论文直接影响已有共享 metric / wording 页。
- `wiki/synthesis/*`
  - 只有在以下情况才更新：
    - 新论文改变了主题边界；
    - 新论文引入了新的冲突或新的不可直接比较项；
    - 新论文让已有 route split 需要补代表或补边界。
- 若新论文只是重复已有模式，不新增共享信息单元，则停在 `papers/` 层，不向上扩写。

## 输出

- 主要输出是 `wiki/` 内的定向增量更新
- 必要时补一个简短 ingest 说明，交代：
  - 处理了哪些 PDF
  - 新建或修改了哪些页面
  - 哪些旧页面受影响并已更新
  - 还有哪些待核点

## 验收标准

- 本轮目标论文都已具备：
  - `raw/<stem>.pdf`
  - `extracts/parses/<stem>/manifest.json`
- 每篇新增论文都已有可用的 `papers/<stem>.md`。
- 若单篇 headline 明显 bundled，或当前论文已出现高复用证据点，则已补相应 `evidence` 页面；否则可以暂留在 `papers/`。
- 受影响的旧页面已经定点更新，或已明确说明本轮为何不更新。
- `wiki/index.md`、`wiki/log.md` 与必要的 `wiki/status.json` 已同步。
- 本轮修改范围仍然可解释：能清楚说出“为什么改这些页，而不是更多页”。

## 禁止事项

- 不把 README、历史讨论、仓库名、常识印象当作事实来源。
- 不把 parser 输出当作最终事实来源。
- 不额外生成长期保留的候选清单、download registry、impact packet 等中间文件。
- 不把 `Docling/Marker` 全量文本当作默认主阅读材料塞进上下文。
- 不把跑完工具当作完成 ingest。
- 不把新增论文只落成单篇页面就算结束；应检查受影响页面是否需要同步更新。
- 不在 `L1` 尚未稳定时直接扩写 synthesis。
- 不把新论文机械追加到 `synthesis` 末尾；如果需要更新主题页，应改写对应局部段落或边界描述。

## 质量检查

完成前至少自查：

- 关键结论能否回到 `raw`
- paper-level 页面是否已达到 schema 要求
- impact analysis 是否完整，受影响页面是否已处理
- `index.md` 与 `log.md` 是否同步
- 是否把自己的推断写成了作者原话
