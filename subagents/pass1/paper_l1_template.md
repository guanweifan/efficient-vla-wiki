# Pass 1 L1 推荐模板

这是 chief-editor 给 worker 的推荐骨架，不是硬模板。  
允许措辞与排版有差异，但最低信息密度应保持一致。

## 推荐结构

```md
# <paper_id>

## Source
- Raw: [[raw/<paper_id>.pdf]]
- Extracts manifest: [[extracts/parses/<paper_id>/manifest.json]]
- Primary text fallback: [[extracts/parses/<paper_id>/pdftotext.txt]]

## Claim
- 这篇论文到底想解决什么问题？
- 作者的核心主张是什么？
- 如果有明确数字级主张，也在这里点出。

## Methodology Index
- 用短语列出核心方法组件、机制和关键词。

## Data Pointer
- 至少给出 2-3 个后续最值得回去补证的位置：
  - Abstract
  - 关键图 / 关键表
  - 方法章节
  - 实验章节

## 待核点
- 写清还不够稳的地方，不要硬补。
```

## 注意
- `Claim` 不是摘要复述，应尽量提炼成可比较的命题。
- `Methodology Index` 不是完整方法说明，只是给后续检索和聚类提供抓手。
- `Data Pointer` 必须尽量具体，至少回到页码、图、表或章节。
- 证据不足时写 `待核`，不要补成确定结论。
