# 2604_20834_PokeVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2604_20834_PokeVLA.md|2604_20834_PokeVLA]] 的单篇证据落点，用来拆分 compact backbone、world-knowledge pretraining、spatial representation learning 与 benchmark / real-world claims。
- 本页聚焦的 headline bundle：`pocket-sized VLA`、`2.4M samples`、`SOTA on LIBERO-Plus`、`real-world deployment` 和 `open-source` 需要分层阅读。

## Evidence
- 核心证据命题：PokeVLA 先预训练 compact PokeVLM，再通过 multi-view goal-aware semantics learning、geometry alignment 和 action expert 将 manipulation-relevant representations 注入 action space。来源：[[raw/2604_20834_PokeVLA.pdf]]，Abstract、Introduction、Figure 3。
- 数据证据命题：论文报告预训练数据约 `2.4M` samples，覆盖 general-purpose VQA、spatial grounding、affordance 与 embodied reasoning 等类别。来源：[[raw/2604_20834_PokeVLA.pdf]]，Introduction、dataset section、Table I。
- 结果证据命题：Table IV 报告标准 LIBERO 上 PokeVLA `1.22B` backbone 与 `98.2%` total success；Table V 报告 LIBERO-Plus fine-tuned 与 transfer setting；Table IX / X 报告 real-world task 与 perturbation setting。来源：[[raw/2604_20834_PokeVLA.pdf]]，Table IV、Table V、Table IX、Table X。

## Table / Metric Anchors
- **Table I**：PokeVLM pretraining data composition。
- **Figure 3**：PokeVLA architecture。
- **Table IV**：LIBERO benchmark，包含 parameter scale 与 task-suite success。
- **Table V**：LIBERO-Plus benchmark，包含 direct fine-tuning 与 transfer setting。
- **Table IX**：real-world eight-task success rates。
- **Table X**：real-world perturbation results。

## Table / Metric Split
- `1.22B` 是模型规模口径，不等同于端侧部署验证。
- `98.2%` total success 属于标准 LIBERO benchmark；LIBERO-Plus 与 real-world results 需要分开读。
- `2.4M samples` 是预训练数据规模，不直接代表训练效率；它是 compact backbone 获得 embodied knowledge 的条件之一。
- `open-source` 在论文中是作者承诺；当前 evidence 不把它当作已核验事实。

## 不可混写项
- 不应把 compact model scale 写成已经证明 on-device / edge deployment。
- 不应把 pretraining data scale 写成低训练成本；PokeVLA 更像 model-and-representation efficiency，而不是 training-cost reduction。
- 不应把 LIBERO、LIBERO-Plus、real-world xArm7 结果合并成单一 superiority claim。

## 影响页面
- [[wiki/papers/2604_20834_PokeVLA.md|2604_20834_PokeVLA]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
