# inference-efficiency-routes

## Question
- 推理期高效 VLA 如何从局部 token/cache 复用，演化到 pruning、caching、speculative / parallel decoding、async / streaming control 这些更广的 compute-allocation 路线？

## Shared Ground
- 本页是 [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]] 之下的子主题页；它承接总纲页已经固定好的效率定义，不单独重写“效率”总概念。
- 当前主题的固定比较轴是：
  - 冗余来源：`token / cache / action chunk / language layer / diffusion timestep / block schedule`
  - 控制面：`semantic saliency / action-aware / interaction-aware / gated execution / streaming trigger`
  - 代价口径：`latency / speedup / FLOPs / frequency / skip ratio`
  - 适用边界：`training-free` vs `requires adaptation`，以及 `single-family validation` vs `broader validated scope`
- `VLA-Cache`、`FlashVLA`、`EfficientVLA`、`SpecPrune-VLA`、`VLA-Pruner`、`VLA-IAP`、`AsyncVLA`、`StreamVLA`、`Fast-dVLA` 共同表明，推理效率的核心是 inference-time compute allocation，而不是训练阶段成本。
- 这些工作都不是单纯追求“更高 speedup”，而是在不同冗余来源和不同控制面上重新分配计算预算。
- 共享 evidence 页已经稳定支持两个共识：
  - runtime headline 必须和 task 或 operating point 口径一起阅读；
  - retention / pruning ratio 只有在与性能保持条件绑定时才有解释力。

## Theme Structure
- 结构角色：inference 路线子主题页。
- 总纲页：[[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]
- 相邻但不等价的子主题：
  - [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
  - [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
- 本页只处理 inference-time compute allocation 路线，不承担训练成本、总定义或部署总纲。

## Route Split
- `cache-and-reuse`
  - 代表：[[wiki/papers/2502_02175_VLA-Cache.md|VLA-Cache]]
  - 依据：通过 temporal 或 latent reuse 回收已有计算，而不是直接丢弃 token。
- `pruning-and-selection`
  - 代表：[[wiki/papers/2509_05614_SpecPrune-VLA.md|SpecPrune-VLA]]、[[wiki/papers/2511_16449_VLA-Pruner.md|VLA-Pruner]]、[[wiki/papers/2603_22991_VLA-IAP.md|VLA-IAP]]
  - 依据：通过 semantic / action / interaction-aware 规则选择性保留 token 或路径。
- `speculative-or-parallel-decoding`
  - 代表：[[wiki/papers/2603_25661_Fast-dVLA.md|Fast-dVLA]]
  - 依据：通过 block-wise diffusion、KV reuse、parallel decoding 改写解码调度。
- `async-or-streaming-control`
  - 代表：[[wiki/papers/2511_14148_AsyncVLA.md|AsyncVLA]]、[[wiki/papers/2602_01100_StreamVLA.md|StreamVLA]]
  - 依据：通过 asynchronous regeneration、completion-state gating 或 streaming trigger 让 compute allocation 服从控制节奏。

## Boundary Conditions
- `training-free` 只能在 evidence 页列出的具体方法与验证范围内成立；需要 adaptation 的方法不能被混入同一 headline。
- `speedup / latency reduction` 只有在明确对应冗余来源与控制面时才可比较；单纯列 speedup 数值不足以建立路线关系。
- `retention ratio` 或 `skip ratio` 必须和性能保持条件一起阅读；否则 pruning/selection 路线之间不可直接比较。
- `frequency` 或 `real-time` 结果只有在明确系统 placement、执行循环与 control setting 时才可与 async/streaming 路线比较。

## Not Directly Comparable
- 训练侧效率工作如 [[wiki/papers/2501_09747_FAST.md|FAST]]、[[wiki/papers/2511_16233_FT-NCFM.md|FT-NCFM]] 不能进入本主题主比较。
- 纯部署分析如 [[wiki/papers/2602_18397_VLA-Perf.md|VLA-Perf]] 只能提供边界说明，不能直接与 inference-time compute-allocation 路线比较。
- 只给单一 speedup、未说明 redundancy source 或控制面的 headline，只能算边缘例子，不能参与 route-level 比较。

## Evidence Links
- [[wiki/evidence/metrics/runtime-vs-task-metrics.md|runtime-vs-task-metrics]]
- [[wiki/evidence/metrics/retention-ratio-vs-speed-performance.md|retention-ratio-vs-speed-performance]]
- [[wiki/evidence/wording/training-free-vs-no-retraining.md|training-free-vs-no-retraining]]
- [[wiki/papers/2501_09747_FAST.md|FAST]]
- [[wiki/papers/2502_02175_VLA-Cache.md|VLA-Cache]]
- [[wiki/papers/2505_21200_FlashVLA.md|FlashVLA]]
- [[wiki/papers/2506_10100_EfficientVLA.md|EfficientVLA]]
- [[wiki/papers/2509_05614_SpecPrune-VLA.md|SpecPrune-VLA]]
- [[wiki/papers/2511_16233_FT-NCFM.md|FT-NCFM]]
- [[wiki/papers/2511_16449_VLA-Pruner.md|VLA-Pruner]]
- [[wiki/papers/2511_14148_AsyncVLA.md|AsyncVLA]]
- [[wiki/papers/2602_01100_StreamVLA.md|StreamVLA]]
- [[wiki/papers/2602_18397_VLA-Perf.md|VLA-Perf]]
- [[wiki/papers/2603_25661_Fast-dVLA.md|Fast-dVLA]]
- [[wiki/papers/2603_22991_VLA-IAP.md|VLA-IAP]]

## Open Questions
- 目前 `cache-and-reuse` 与 `speculative-or-parallel-decoding` 在共享 benchmark 上的直接并比仍然不足，后续建模时需要更谨慎处理“更优路线”这种表述。
- 一些 routing/gating 路线仍把系统频率收益与任务成功率混写，后续 closeout 时还需要持续防止回退。

## Gate Check
- `required_sections_complete: yes`
- `evidence_links_present: yes`
- `unscoped_comparative_claims: 0`
- `boundary_conditions_present: yes`
