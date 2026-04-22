---
name: wiki-lint
description: 用于检查 wiki 的断链、证据缺口、控制文件失配和页面职责漂移，并做小范围修复。
---

# Wiki Lint

## 用途

这个技能用来检查 `wiki/` 有没有断链、证据缺口、控制文件失配和页面职责漂移。

它适合在这些时候使用：

- ingest 之后做一轮收口
- reflect 之后检查有没有带来结构漂移
- 怀疑某个主题页已经写乱了
- 定期检查 `wiki/index.md`、`wiki/log.md`、`wiki/status.json`

## 不适合的情况

- 吸收新论文
- 把 thread 里的稳定结论写回 `wiki/`
- 围绕一个问题写报告
- 做大范围主题重写

## 先读什么

- `AGENTS.md`
- `WIKI_SCHEMA.md`
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

## 重点看什么

- `raw` 锚点是否缺失
- 单篇页是否漏挂证据页
- 主题页的证据链能不能落回下层页面
- `papers / evidence / synthesis` 三层是否串位
- `index / log / status` 是否和当前内容一致

## 建议流程

1. 先定范围：整库、某个目录、某个主题，或者只看控制文件。
2. 再定重点：断链、证据链、控制文件、页面职责。
3. 先记录问题，再决定哪些可以直接修。
4. 只修边界清楚、风险低的问题。
5. 一旦发现问题已经超出局部修复范围，就转交。

## 输出

至少要有这些内容：

- 检查范围
- 检查重点
- 发现的问题
- 已修复项
- 转交项

如果动了控制文件，要同步更新 `wiki/log.md`，必要时再更新 `wiki/status.json`。

## 可直接修的常见问题

- 单篇页缺少已有证据页的链接
- 证据页缺少 `raw` 锚点
- 主题页正文用了某个证据页，但 `Evidence Links` 没收口
- `wiki/index.md`、`wiki/log.md`、`wiki/status.json` 的计数或状态不同步
- 局部链接失效

## 转交条件

- 新论文还没吸收进来：转 `wiki-ingest`
- thread 里的稳定结论该写回 `wiki/`：转 `wiki-reflect`
- 用户要的是一份问题报告：转 `wiki-query`
- 某个主题需要大改：转周期维护

## 禁止事项

- 不把 lint 扩成一次全面重写。
- 不在没回原文时改关键事实。
- 不为了统一语气删掉原本有用的差异表述。
- 不把“页面存在”当成“问题已经解决”。

## 验收

- 每个问题都落到了具体页面
- 严重度和处理方式清楚
- 已修内容范围小、可回溯
- 如果没发现问题，也写清检查范围
