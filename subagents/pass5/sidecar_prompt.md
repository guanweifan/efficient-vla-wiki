# Pass 5 Sidecar Prompt

`Pass 5` 中的 `sidecar` 只允许承担只读核查任务，例如：
- 链接核查
- 文档重复或低价值段落定位
- 局部 evidence / raw 锚点回查

`sidecar` 不得：
- 并发写正式 `wiki/`
- 擅自删除正式文档
- 自行扩写新主题或新 evidence
