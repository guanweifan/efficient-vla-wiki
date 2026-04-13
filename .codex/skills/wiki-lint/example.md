# wiki-lint example

## 示例 1

ingest 之后做轻量收口：

```text
使用 wiki-lint。
范围只看本轮新增的 paper/evidence、受影响的 synthesis，以及 `wiki/index.md`、`wiki/log.md`、`wiki/status.json`。
模式用 `small-fix`。
优先检查 paper->evidence 漏链、evidence raw anchor、Evidence Links 漏挂和控制文件同步问题。
```

## 示例 2

局部 lint：

```text
使用 wiki-lint，只检查 `token pruning` 相关页面。
范围包括相关 `wiki/papers/`、对应 `wiki/evidence/` 和 `wiki/synthesis/inference-efficiency-routes.md`。
重点看 `role-boundary` 和 `evidence-chain`，按高、中、低严重度给出结果。
```

## 示例 3

用 lint 判断应不应该转交：

```text
使用 wiki-lint。
如果发现问题只是断链、漏链、计数失配，可以直接修。
如果发现问题本质上是新论文尚未吸收、thread 结论尚未回流，明确标注应转 `wiki-ingest` 或 `wiki-reflect`，不要在 lint 中扩写。
```
