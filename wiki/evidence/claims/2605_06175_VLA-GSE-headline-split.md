# 2605_06175_VLA-GSE-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_06175_VLA-GSE.md|2605_06175_VLA-GSE]] 的单篇证据落点，用来拆分 PEFT、SVD-based generalized/specialized experts、trainable-parameter ratio 与 benchmark headline。
- 本页聚焦的 headline bundle：`2.51% trainable parameters`、`81.2% LIBERO-Plus`、`knowledge preservation`、`real-world distribution shifts` 需要分层阅读。

## Evidence
- 核心证据命题：VLA-GSE 对 frozen backbone weight 做 SVD，把 leading components 分配给 generalized expert，把 residual components 分配给 routed specialized experts；GSE 只作用于 VLM backbone。来源：[[raw/2605_06175_VLA-GSE.pdf]]，Abstract、Figure 1、Section 3.1。
- 优化机制命题：expert-wise gradient scale balancing 和 expectation-based backbone weight adjustment 分别处理 specialized experts 的优化不均衡和初始化时 equivalent weight drift。来源：[[raw/2605_06175_VLA-GSE.pdf]]，Section 3.2、Section 3.3、Algorithm 1。
- 结果证据命题：论文报告在 comparable trainable-parameter budget 下，VLA-GSE 更新 `2.51%` full model parameters，并在 LIBERO-Plus、multimodal benchmarks 和 real-world distribution shifts 上给出不同口径的结果。来源：[[raw/2605_06175_VLA-GSE.pdf]]，Abstract、Table 1、Table 2、Table 3、Table 5。

## Table / Metric Anchors
- **Figure 1**：VLA-GSE framework。
- **Table 1 / Table 2**：LIBERO-Plus benchmark and method comparison。
- **Table 3**：multimodal understanding evaluation。
- **Table 4**：component ablation。
- **Figure 3 / Table 5**：real-world generalization。
- **Figure 5**：inference latency comparison。
- **Table 9**：hyperparameters and trainable parameters。

## Table / Metric Split
- `2.51%` 是 trainable-parameter budget，不是 inference-time active-parameter ratio。
- LIBERO-Plus success、VLM benchmark preservation、real-world success 和 latency 是不同层。
- routed specialized experts 服务 adaptation capacity，不等同于 dynamic computation acceleration。

## 不可混写项
- 不应把 VLA-GSE 归为 backbone runtime routing。
- 不应把 PEFT 参数效率写成训练 wall-clock 已减少，除非回到具体 training cost 表。
- 不应把 preserving VLM capability 写成 robotic task success 本身。

## 影响页面
- [[wiki/papers/2605_06175_VLA-GSE.md|2605_06175_VLA-GSE]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
