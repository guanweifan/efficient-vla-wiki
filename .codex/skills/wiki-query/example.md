# wiki-query example

## 示例 1：新问题

用户提问：

`近一年最常用的 VLA baseline 有哪些？`

推荐动作：

1. 先把它标准化成一个 `canonical question`
2. 先查 `wiki/synthesis/` 中与 baseline、efficiency、deployment 相关的主题页
3. 再查相关 `wiki/papers/` 与 `wiki/evidence/`
4. 若 `threads/query/` 中不存在同类问题，则按 `canonical question` 新建一个稳定命名的 thread
5. 在正文写清主答案，在 `Evidence Notes` 用双链补证据入口

## 示例 2：对已有问题的追问

已有 thread：某个已存在的 `threads/query/qXXXX-*.md`

用户继续问：

`哪些 token prune 方法是 training-free 的？`

推荐动作：

1. 判断它仍然属于 `token pruning tricks` 的同一 canonical question
2. 更新原文件，不新建新 thread
3. 在 `Current Answer` 中补“training-free 子类”
4. 在 `Evidence Notes` 中补充相关：
   - `[[wiki/evidence/metrics/retention-ratio-vs-speed-performance.md]]`
   - 若有必要，再补对应 `papers` 或 `claims`
5. 在 `Update Log` 追加本次追问
6. 若判断这已经不是 query，而是一个稳定命题应回流到 `wiki/`，则转 `wiki-reflect`
