---
name: wiki-reflect
description: 用于把 threads/ 中已经稳定、可复用、且能回到 raw 复核的命题定向回写到 wiki/。在需要从 thread 抽取候选命题、判断哪些应写入 wiki、哪些应留在 threads、哪些应转交给 ingest、lint 或 periodic maintenance 时使用。
---

# Wiki Reflect

## 核心目标

- `wiki-reflect` 只处理 thread-driven knowledge consolidation：把 thread 暴露出的稳定命题定向沉淀进 `wiki/`。
- 它的主产物是：少量高价值回写、未回写项说明、明确转交。
- 它不是回答 thread 的 skill，也不是吸收新论文、修维护缺陷或重做整库结构的 skill。

## 何时使用

- 冷启动已完成，`wiki/` 已具备基本可用结构。
- 某个 thread 产生了长期有价值的比较或结论。
- 同一类问题在多个 thread 中反复出现。
- 现有 `wiki/` 结构无法承载 thread 中已稳定的理解。

## 何时不使用

- 不用它代替 bootstrap。
- 不用它在 `papers/` 原子层还大面积缺失时硬做高级 synthesis。
- 不用它把 thread 直接转存成 wiki。
- 不用它吸收新论文、补 `raw/` 或新建本该由 `wiki-ingest` 建的基础页面。
- 不用它修断链、计数失配、控制文件不同步这类维护缺陷；这属于 `wiki-lint`。
- 不用它继续扩写 thread 本身；这属于 `wiki-query`。
- 不用它做大面积 taxonomy 重构或整库再平衡；那属于 `Periodic Maintenance`。

## 先读什么

- 仓库根下的 `AGENTS.md`
- 仓库根下的 `WIKI_SCHEMA.md`
- 相关的 `threads/*.md`
- 对应的 `wiki/` 页面

## 默认单位

- reflect 的默认处理单位是 **可核证命题**，不是整篇 thread。
- 先从 thread 中拆命题，再判断这些命题分别属于：
  - `write_to_wiki`
  - `thread_only`
  - `unresolved`
  - `handoff`

## 输入

- 一个 thread，或一组相关 thread
- 相关 `wiki/` 页面
- 必要时回读对应 `raw/*.pdf`

## 核心原则

- 按 `WIKI_SCHEMA.md` 的 Evidence Model 与 Maintenance Workflows 执行。
- 这是维护态 skill，不承担首次整库建图。
- `threads/` 不是事实来源。
- reflect 的目标是沉淀稳定知识，不是转存整段问答。
- 默认优先补现有页面；只有现有结构承载不了，才考虑新页。
- 新写入 `wiki/` 的内容，必须能回到 `raw/` 或已经 source-grounded 的 paper/evidence 页面。

## 负责什么

- 从一个或一组 thread 中抽取值得沉淀的候选命题。
- 回到 `wiki/` 与必要的 `raw/` 重新核证。
- 判断命题的最小落点：`paper`、`evidence`、`synthesis`。
- 对现有 `wiki/` 做小范围、定向更新。
- 在 `wiki/log.md` 记录本次 reflect。

## 不负责什么

- 不把 thread 当事实来源直接搬运。
- 不补 `raw/`、不补 `extracts/`、不做新论文 ingest。
- 不把维护态断链、漏链、控制文件失配混入 reflect。
- 不因为一个 thread 看起来重要，就顺手扩写一串不相干页面。

## 执行约定

1. 先定范围：一个 thread，或一组明显相关的 threads。
2. 再拆命题：把 thread 中值得沉淀的内容拆成若干可核证命题。
3. 做四分：
   - `write_to_wiki`
   - `thread_only`
   - `unresolved`
   - `handoff`
4. 对 `write_to_wiki` 的命题回到 `raw/` 或对应的 source-grounded page 复核。
5. 按最小落点回写：
   - 优先补 `paper / evidence`
   - 必要时再改 `synthesis`
   - 只有结构真的变化时再更新 `index / status`
6. 对 `handoff` 项明确转交方向，不在 reflect 中继续扩大范围。
7. 在 `wiki/log.md` 记录：来自哪些 thread、回写了什么、什么没有进入 `wiki`。

## 适合回流的命题

- 一致可复用的比较维度
- 被 thread 暴露出的页面缺口
- 已核证的跨论文共识与分歧
- 更清楚的术语边界

## 不适合回流的命题

- 一次性措辞
- 未回证的推理
- 只依赖 thread 上下文成立的临时判断
- 为了回答问题而做的夸张压缩
- 明显还是研究建议、idea 发散或 speculative roadmap 的内容

## 输出

- `wiki/` 的小范围、定向更新
- 至少说明：
  - 从哪些 thread 得到启发
  - 回写了什么
  - 哪些内容仍留在 `threads`
  - 哪些内容被转交给其他 skill

## 禁止事项

- 不直接把 thread 文本复制进 wiki 当证据。
- 不因为一个 thread 看起来“合理”就跳过原文复核。
- 不把争议点写成共识。
- 不把 schema 调整和内容调整混在一起无说明地大改。
- 不在基础页面缺口很大时，用 reflect 硬补出高级结论。
- 不默认新建大而全的专题页；除非现有结构确实承载不了。

## 转交条件

- 新论文已进 `raw/`，但缺基础 page / evidence 落点：转 `wiki-ingest`。
- 只是断链、漏链、计数不同步、Evidence Links 未收口：转 `wiki-lint`。
- 问题仍在探索，尚未形成稳定命题：留在 `threads/`，由 `wiki-query` 继续承接。
- 需要跨多个主题页重写、再聚类或再建模：转 `Periodic Maintenance`。

## 验收标准

完成前至少自查：

- 新写入 `wiki` 的每条关键信息能否回到 `raw` 或 source-grounded page。
- 是否清楚区分了“作者说了什么”和“agent 归纳了什么”。
- 改动是否小而集中，而不是借 reflect 做无边界扩写。
- 未进入 `wiki` 的内容是否被明确保留在 `threads` 或转交。
- `wiki/log.md` 是否记录了本次 reflect。
