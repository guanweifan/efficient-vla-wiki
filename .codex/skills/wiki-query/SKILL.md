---
name: wiki-query
description: 用于以具体问题为入口，在 wiki/ 中分层检索相关信息，并把答案沉淀到 threads/ 中持续维护。在需要判断一个问题是已有 thread 的追问还是全新问题、基于 wiki/ 汇总结构化答案、并明确哪些问题应转交给 ingest、reflect 或 lint 时使用。
---

# Wiki Query

## 核心目标

- `wiki-query` 只处理 question-driven retrieval and answer writing：把用户问题压成一个稳定的 `canonical question`，并把当前答案沉淀到 `threads/`。
- 它的主产物是：一个新增或更新后的 thread，以及一版基于当前 `wiki/` 的结构化回答。
- 它不是新论文吸收、thread 回流到 `wiki/`、或维护态缺陷修复的 skill。

## 何时使用

- 用户提出一个面向知识内容的具体问题，希望基于当前 `wiki/` 得到结构化回答。
- 用户围绕一个已有问题继续追问，希望在原有回答基础上继续补充，而不是重新开新文件。
- 用户希望把问答结果沉淀进 `threads/`，形成可持续更新的问题记录。

## 何时不使用

- 不用它代替 `wiki-ingest` 处理新增论文。
- 不用它代替 `wiki-reflect` 把稳定 thread 结果回流到 `wiki/`。
- 不用它在 `wiki/` 还明显缺页或结构未建立时硬做大规模问答沉淀。
- 不用它把 `threads/` 直接当成事实层或主知识库。

## 先读什么

- 仓库根下的 `AGENTS.md`
- 仓库根下的 `WIKI_SCHEMA.md`
- `wiki/index.md`
- 与问题可能相关的 `wiki/synthesis/`、`wiki/evidence/`、`wiki/papers/`
- 如命中已有问答，再读对应 `threads/` 文件

## 输入

- 一个用户问题
- 可选的范围约束，例如：
  - 时间范围
  - 论文范围
  - 主题范围
  - 比较维度
  - 是否要求更严格回到 `raw/` 核证

## 核心职责

1. 把用户问题解析成一个稳定的 `canonical question`。
2. 在 `wiki/` 中分层检索与问题相关的信息。
3. 判断这是一个已有问题的追问，还是一个新的问题。
4. 产出一个可持续维护的 thread 回答文件，并在后续追问中继续更新它。

## 核心原则

- `wiki/` 是检索入口，`raw/` 是唯一事实兜底来源，`threads/` 是问题沉淀层。
- `threads/` 中的事实性表述不得脱离 `raw/` 支撑。
- 回答正文应尽量干净、清晰，不在正文堆叠过多证据细节。
- 默认优先复用现有 thread；只有当新问题已经脱离原有 `canonical question` 时才开新文件。
- 证据优先以下沉方式呈现：
  - 优先在正文中用 Obsidian 双链指向相关 `wiki/papers/*`、`wiki/evidence/*`、`wiki/synthesis/*`
  - 需要更细的证据说明时，统一放在正文下方的 `附录 / Evidence Notes`
- 先回答问题，再补证据；但没有证据支撑的结论不得写入正式答案。
- 如果 `wiki/` 无法支撑关键结论，应明确说明缺口，必要时回到 `raw/` 局部核证。
- 若问题本质上已变成“应先修 wiki 再回答”，应明确转交，而不是在 query 中硬撑。

## 问题分类

### A. 追问

属于追问的常见情况：

- 用户只是缩小范围或增加限定条件
- 用户要求对已有答案做补证、分层、细化或反例说明
- 用户继续围绕同一个核心主题、同一组比较轴或同一个 canonical question 发问

示例：

- 原问题：`近一年最常用的 VLA baseline 有哪些？`
- 追问：`那在 manipulation 里最常见的是哪些？`

### B. 新问题

属于新问题的常见情况：

- 核心对象已经变化
- 主比较轴已经变化
- 原线程的答案结构已不适合承载这个问题

示例：

- 原问题：`token prune 的 trick 具体有哪些？`
- 新问题：`近一年最常用的 VLA baseline 有哪些？`

## 追问判断规则

按下面顺序判断：

1. 是否仍然能压缩到同一个 `canonical question`
2. 是否仍然依赖同一组核心 `wiki` 页面
3. 是否仍然沿用同一组比较轴或子问题骨架
4. 若把新问题写进旧 thread，不会让旧 thread 变成杂糅 bucket

若以上 1-3 大致成立，且第 4 条不被破坏，则视为追问。
否则，开新 thread。

## 推荐检索顺序

1. 先查 `wiki/synthesis/`
   - 拿整体框架、已有聚类、边界条件、不可直接比较项
2. 再查 `wiki/evidence/`
   - 拿关键支撑点、共享 metric、共享 wording、单篇 claim split
3. 最后查 `wiki/papers/`
   - 补单篇定位、细节、局部上下文与原始落点
4. 若关键结论仍不稳，再回 `raw/`

不要把 `extracts/` 当成默认信息来源；它只可作为定位辅助。

## 信息组织方式

- 不按文件顺序堆摘录。
- 先拆出用户真正的问题结构，再按子问题组织答案。
- 优先输出：
  - 直接答案
  - 比较维度
  - 代表性对象
  - 边界与例外
  - 尚不确定之处

## threads 文件组织

推荐目录：

- `threads/query/`

推荐命名：

- `threads/query/q0001-vla-baselines-recent.md`
- `threads/query/q0002-token-pruning-tricks.md`

命名原则：

- 使用稳定编号 + 简短 slug
- slug 依据 `canonical question`，不直接照抄用户原话

## thread 文件推荐结构

每个问答文件建议使用以下结构：

```md
# Q0001 | 近一年最常用的 VLA baseline

## Canonical Question

一句稳定的问题表述。

## Scope

- 本问题包含什么
- 不包含什么
- 时间范围 / 论文范围 / 任务范围

## Current Answer

这里写面向用户的主答案。正文应保持干净，不堆叠过多证据细节。

## Short Answer

可选。适合先给一个压缩版结论。

## Structured Notes

- 子问题 1
- 子问题 2
- 子问题 3

## Related Wiki Pages

- [[wiki/synthesis/...]]
- [[wiki/evidence/...]]
- [[wiki/papers/...]]

## Evidence Notes

这里写证据附录，优先使用 Obsidian 双链组织。

## Open Uncertainties

- 哪些地方仍待核
- 哪些结论只在特定边界内成立

## Update Log

- 日期 + 本次追问补了什么
```

## 正文与证据的写法

- `Current Answer` 保持流畅、清楚、面向问题。
- 不在正文里堆很多页码、表格编号和细证据。
- 正文里若需要提示依据，优先写成轻量双链：
  - `这类方法主要集中在 [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]。`
- 更细的证据支撑统一放到 `Evidence Notes`：
  - 双链到 `wiki/evidence/*`
  - 必要时补一句该页面解决了什么口径问题

## 推荐流程

1. 解析问题，抽出：
   - 主题对象
   - 时间范围
   - 比较维度
   - 期望答案形态
2. 判断是否命中已有 thread。
3. 按 `synthesis -> evidence -> papers` 检索相关页面。
4. 把找到的信息按子问题聚类，而不是按文件罗列。
5. 若关键结论仍不稳，回 `raw/` 做局部核证。
6. 更新或新建 `threads/query/*.md`。
7. 在 `Update Log` 记录本次补充。
8. 向用户返回当前答案，并说明：
   - 这是更新已有 thread 还是新建 thread
   - 本次主要依据了哪些 `wiki` 页面
   - 哪些地方仍然待核

## 新建 vs 更新

- 命中已有 thread：更新原文件，不新建。
- 属于新问题：新建 thread 文件。
- 若旧 thread 已经被追问拉得过宽：
  - 可以拆出新 thread
  - 但要在旧文件中保留交叉引用

## 输出

主要输出是：

- 一个新增或更新后的 `threads/query/*.md`
- 一段面向用户的当前答案

可选输出：

- 一个简短的“wiki 缺口提醒”，说明哪些问题之所以答不深，是因为 `wiki` 当前缺相应支撑页

## 转交条件

- 新论文尚未进入 `wiki/`，或缺基础 paper/evidence 页面，导致问题无法稳定回答：转 `wiki-ingest`。
- 某个 thread 已形成稳定、可复用、且能回到 `raw` 的命题，值得沉淀到 `wiki/`：转 `wiki-reflect`。
- 主要问题不是知识缺口，而是断链、Evidence Links 漏挂、`index/log/status` 不同步：转 `wiki-lint`。
- 问题已经演变成跨多个主题页的大范围重构：转 `Periodic Maintenance`。

## 禁止事项

- 不把 `threads/` 当事实来源。
- 不把 `extracts/` 当最终依据。
- 不把正文写成证据清单。
- 不在没有必要时把每次追问都开成新文件。
- 不把多个不同问题粗暴塞进同一个 thread。
- 不把 agent 的推理伪装成论文原话。

## 验收标准

完成前至少自查：

- 这是在更新旧 thread，还是新建 thread；判断是否合理
- `Current Answer` 是否足够干净、可读
- 证据是否以下沉方式组织，而不是挤进正文
- 关键结论是否都能回到 `wiki`，必要时回到 `raw`
- `Open Uncertainties` 是否写清楚
- `Update Log` 是否记录了这次追问补充了什么
