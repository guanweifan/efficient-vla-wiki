---
name: wiki-lint
description: 用于在维护态对 wiki core 做缺陷审计和局部修复。在需要检查证据回链、结构漂移、控制文件同步和局部断链，并判断哪些问题应转交给 ingest、reflect 或 periodic maintenance 时使用。
---

# Wiki Lint

## 核心目标

- `wiki-lint` 只处理维护态缺陷：确认现有 `wiki/` 仍然可回链、可维护、结构不漂移。
- 它的主产物是：问题清单、局部修复、明确转交。
- 它不是新知识写入流程，不替代 `wiki-ingest`、`wiki-reflect`、`wiki-query`。

## 何时使用

- 冷启动完成后，进入周期维护或增量维护收尾阶段。
- 完成一轮 `wiki-ingest` 后，做轻量收口。
- 完成一轮 `wiki-reflect` 后，检查回流是否带来局部漂移。
- 在回答重要问题前，怀疑 `wiki/` 已经漂移或失真。
- 定期检查 `wiki core + control files` 时。

## 何时不使用

- 不用它代替冷启动建库。
- 不在 `wiki/` 还过薄、页面大面积缺失时，把“未建立”误当成“待 lint 的已建立系统”。
- 不用它吸收新论文或新建 paper-level 页面；这属于 `wiki-ingest`。
- 不用它把 thread 结论回流到 `wiki/`；这属于 `wiki-reflect`。
- 不用它围绕具体问题写 thread 答案；这属于 `wiki-query`。
- 不用它做大面积 taxonomy 重组、主题重写或再建模。

## 先读什么

- 仓库根下的 `AGENTS.md`
- 仓库根下的 `WIKI_SCHEMA.md`
- `wiki/index.md`
- `wiki/log.md`
- 目标范围内的 `wiki/` 页面

## 默认范围

- `wiki/papers/`
- `wiki/evidence/`
- `wiki/synthesis/`
- `wiki/index.md`
- `wiki/log.md`
- `wiki/status.json`

## 扩展范围

- 只有在用户明确要求，或问题已经指向 control/docset convergence 时，再检查 `WIKI_SCHEMA.md`、skills、subagents 等说明文档。

## 核心原则

- 按 `WIKI_SCHEMA.md` 的 Knowledge Model、Evidence Model 和 Maintenance Workflows 检查。
- 这是维护态校验 skill，不承担首次整库阅读和建图。
- 先找证据、结构和控制文件问题，再考虑局部措辞。
- 默认只做局部修复；一旦问题开始要求新建知识或大范围重写，就应转交。

## 负责检查什么

- 证据链缺口：页面缺少 `raw` 锚点、paper 页漏挂 evidence、`synthesis` 结论回不落下层页面。
- 结构漂移：`paper / evidence / synthesis` 三层职责开始串位，或局部比较句已经越界。
- 控制文件失配：`wiki/index.md`、`wiki/log.md`、`wiki/status.json` 与当前 `wiki/` 实际内容不同步。
- 局部链接问题：wiki 内链断裂、影响页面漏链、交叉引用已经失效。

## 不负责什么

- 不因为“这个主题还可以继续补”就扩写新知识。
- 不把新增论文、缺失 paper page 或新 evidence page 的建立流程并入 lint。
- 不在未回读 `raw/` 的情况下裁决冲突信息。
- 不做纯文风统一或无边界润色。
- 不生成低价值的中间 registry、packet 或过程文件。

## 执行约定

1. 先定 `scope`：整库、某个目录、某个主题，或 `control files`。
2. 再定 `focus`：`links`、`raw-anchor`、`evidence-chain`、`control-sync`、`role-boundary`。
3. 最后定 `mode`：`report-only` 或 `small-fix`。
4. 先看 `index.md`、`log.md` 与目标页面，再按高、中、低严重度记录问题。
5. 只有在问题局部、低风险、边界清楚时才直接修。
6. 如果问题本质上是新知识未吸收、冲突待核、或大范围结构失衡，应停止扩大 lint，并明确转交给 `wiki-ingest`、`wiki-reflect` 或 `Periodic Maintenance`。
7. 如果问题本质上是冷启动未完成，应明确标成 bootstrap gap，而不是伪装成普通 lint 项。

## 输出

lint 输出至少包含：

- 检查范围
- 检查重点
- 发现的问题与严重度
- 已修复项
- 转交项

如果做了修复，还应同步更新 `wiki/log.md`；如果控制文件发生变化，再更新 `wiki/status.json`。

## 可直接修复的典型问题

- paper 页缺少已有 evidence 页的回链。
- evidence 页缺少已经明确的 `raw` 锚点。
- `synthesis` 页正文已经使用某个 page anchor，但 `Evidence Links` 漏挂。
- `wiki/index.md`、`wiki/log.md`、`wiki/status.json` 的计数或状态不同步。
- 局部 wiki 内链失效、标题改名后漏改引用。

## 应转交的典型问题

- 新论文已经进入 `raw/`，但尚未建立 `wiki/papers/*` 页面：转 `wiki-ingest`。
- thread 里的稳定结论值得回流到 `wiki/`：转 `wiki-reflect`。
- 用户的问题本质上是检索和回答，而不是修库：转 `wiki-query`。
- 某个主题需要大面积重写、再聚类或重新建模：转 `Periodic Maintenance`。

## 禁止事项

- 不把 lint 变成无边界的全面重写。
- 不在未回读 `raw/` 的情况下修正关键事实。
- 不为了“统一风格”删除仍然有价值的差异表述。
- 不跳过问题分级，直接堆砌观察。
- 不把“页面存在”误判为“问题已解决”。
- 不把“尚未建库完成”误判成“已有页面质量差”。
- 不默认把全仓库说明文档都卷入一次日常 lint。

## 验收标准

完成前至少自查：

- 每个问题是否都落到了具体页面，而不是泛泛而谈。
- 严重度是否清楚，且能支持“直接修 / 转交 / 暂停”判断。
- 已修内容是否局部、可回溯、不会引入新的结构噪音。
- 如果没有发现问题，是否明确写清楚检查范围与剩余风险。
- 本轮结果是否真的降低了维护风险，而不是只做了表面整理。
