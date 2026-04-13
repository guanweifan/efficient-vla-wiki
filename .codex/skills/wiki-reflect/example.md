# wiki-reflect example

## 示例 1

把一个 thread 的稳定命题回写到现有页面：

```text
使用 wiki-reflect，检查某个 thread 里关于 token pruning 的讨论。
先把 thread 里的稳定判断拆成命题，再判断哪些值得写回 `wiki/evidence/` 或 `wiki/synthesis/`。
不要转存整段 thread，只回写已能回到 raw 或 source-grounded page 的部分。
```

## 示例 2

根据反复出现的问题补共享 evidence：

```text
使用 wiki-reflect。
最近多个 thread 都在追问 `training-free` 和 `no retraining` 能不能混写。
如果这已经形成稳定命题，就补一个共享 wording evidence，并更新受影响的 synthesis 页面。
如果只是局部断链或控制文件不同步，不要在 reflect 中顺手修，改为转交 `wiki-lint`。
```

## 示例 3

用 reflect 判断哪些内容不该进 wiki：

```text
使用 wiki-reflect。
如果 thread 里有研究建议、idea 发散或 speculative roadmap，请明确保留在 `threads/`，不要写进 `wiki/`。
如果发现某些基础页面本来就缺失，应转交 `wiki-ingest`，不要在 reflect 中硬补。
```
