---
name: wiki-query
description: 用于围绕一个具体问题检索 wiki，并把答案写进 threads/。适合判断是追问旧问题还是新开问题时使用。
---

# Wiki Query

## 用途

这个技能用来围绕一个具体问题查 `wiki/`，并把答案写进 `threads/`。

适合这些情况：

- 用户要一份结构化回答
- 用户在一个已有问题上继续追问
- 需要把问答结果整理成可继续维护的本地报告

## 不适合的情况

- 吸收新论文
- 把稳定结论写回 `wiki/`
- 修断链、修控制文件

## 先读什么

- `AGENTS.md`
- `WIKI_SCHEMA.md`
- `wiki/index.md`
- 相关的 `wiki/synthesis/`、`wiki/evidence/`、`wiki/papers/`
- 如果命中已有问题，再读对应的 `threads/` 文件

## 核心规则

- `wiki/` 是检索入口。
- `raw/` 是事实兜底。
- `threads/` 用来保存问题报告。
- 回答要先讲清结论，再补证据。
- 正文保持清楚，不把页码和细证据全堆进去。
- 关键结论站不稳时，要回原文补核。

## 新问题还是追问

先看三件事：

1. 还是同一个问题主轴。
2. 还是同一批核心页面在支撑答案。
3. 把新内容写进旧 thread 后，会不会把旧文件写乱。

前三项大体成立，就按追问处理；否则新开文件。

## 建议检索顺序

1. 先看 `wiki/synthesis/`
2. 再看 `wiki/evidence/`
3. 最后看 `wiki/papers/`
4. 关键处不稳，再回 `raw/`

`extracts/` 只在需要定位时使用。

## thread 文件

默认放在：

- `threads/query/`

命名建议：

- `q0001-vla-baselines-recent.md`
- `q0002-token-pruning-tricks.md`

文件里建议保留这些部分：

- `Canonical Question`
- `Scope`
- `Current Answer`
- `Structured Notes`
- `Related Wiki Pages`
- `Evidence Notes`
- `Open Uncertainties`
- `Update Log`

## 建议流程

1. 先把用户问题收成一句稳定的问题表述。
2. 判断是追问还是新问题。
3. 按 `synthesis -> evidence -> papers` 检索。
4. 按子问题组织答案，不按文件顺序堆摘录。
5. 关键处回原文核对。
6. 更新或新建 `threads/query/*.md`。
7. 在 `Update Log` 记录本次补充。

## 输出

- 一个新增或更新后的 `threads/query/*.md`
- 一段面向用户的当前答案

必要时可以补一句说明，指出当前 `wiki/` 还缺哪些支撑页。

## 转交条件

- 新论文还没吸收到 `wiki/`：转 `wiki-ingest`
- thread 里的稳定结论该写回 `wiki/`：转 `wiki-reflect`
- 主要问题是断链、漏链、控制文件失配：转 `wiki-lint`
- 已经变成多主题重构：转周期维护

## 禁止事项

- 不把 `threads/` 当事实来源。
- 不把 `extracts/` 当最终依据。
- 不把正文写成证据清单。
- 不把多个不同问题硬塞进同一个 thread。
- 不把 agent 推理伪装成论文原话。

## 验收

- 新建还是更新，判断说得清
- `Current Answer` 可读
- 关键结论能回到 `wiki`，必要时能回到 `raw`
- `Open Uncertainties` 写清楚
- `Update Log` 已更新
