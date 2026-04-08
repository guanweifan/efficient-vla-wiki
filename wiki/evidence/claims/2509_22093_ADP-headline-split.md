# 2509_22093_ADP-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2509_22093_ADP.md|2509_22093_ADP]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`1.35×` speedup 是在 OpenVLA-OFT / LIBERO 设置下的 headline；real-world 主结果的 headline 更接近 `1.49×` latency speedup，两者不能混成同一指标。

## Evidence
- 核心证据命题：这篇论文要解决的是：VLA manipulation 中视觉 token 的冗余并不是固定不变的，而是会随着 manipulation stage 改变。粗粒度运动阶段冗余更高，细粒度操作阶段则更依赖完整视觉细节；因此静态 pruning 或只看 attention score 的 pruning schedule 不够合适。 来源：[[raw/2509_22093_ADP.pdf]]，`PDF p.1` Abstract + Fig. 1：
- 补充证据命题：作者提出 `Action-aware Dynamic Pruning (ADP)`，把两件事结合起来： 来源：[[raw/2509_22093_ADP.pdf]]，问题设定、action-aware redundancy 的核心观察，以及 `1.35× speedup` / `25.8% improvements with OpenVLA` 的 headline 在这里。
- 主证据锚点 1：来源：[[raw/2509_22093_ADP.pdf]]，`PDF p.1` Abstract + Fig. 1：
- 主证据锚点 2：来源：[[raw/2509_22093_ADP.pdf]]，问题设定、action-aware redundancy 的核心观察，以及 `1.35× speedup` / `25.8% improvements with OpenVLA` 的 headline 在这里。
- 主证据锚点 3：来源：[[raw/2509_22093_ADP.pdf]]，`PDF p.3-5` Method + Fig. 2 / Fig. 3：

## Table / Metric Anchors
- `PDF p.7` Table 1：
  - LIBERO simulation 主结果在这里；不同 keep ratio 下的 success rate、FLOPs 与 speedup，以及与 OpenVLA-OFT、FastV(+OFT) 等 baseline 的比较都在这里。
- `PDF p.8` Table 2 + Fig. 5：
  - real-world 四任务上的 success rate、latency 与 `1.49×` speedup 在这里。
- `PDF p.8-9` Table 3：
  - dynamic controller 的 ablation 在这里，用于锚定“为什么 action-aware gate 比 periodic/static schedule 更合理”的证据；`96.3%` 的平均 SR 更适合回到这里理解，而不是混入主表 headline。

## Table / Metric Split
- ``PDF p.7` Table 1` 这一层支撑 ``PDF p.7` Table 1` 对应的 benchmark / metric / operating point。 - LIBERO simulation 主结果在这里；不同 keep ratio 下的 success rate、FLOPs 与 speedup，以及与 OpenVLA-OFT、FastV(+OFT) 等 baseline 的比较都在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2509_22093_ADP.pdf]]，``PDF p.7` Table 1`。
- ``PDF p.8` Table 2 + Fig. 5` 这一层支撑 ``PDF p.8` Table 2 + Fig. 5` 对应的 benchmark / metric / operating point。 - real-world 四任务上的 success rate、latency 与 `1.49×` speedup 在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2509_22093_ADP.pdf]]，``PDF p.8` Table 2 + Fig. 5`。
- ``PDF p.8-9` Table 3` 这一层支撑 ``PDF p.8-9` Table 3` 对应的 benchmark / metric / operating point。 - dynamic controller 的 ablation 在这里，当前对应“为什么 action-aware gate 比 periodic/static schedule 更合理”的证据；`96.3%` 的平均 SR 更适合回到这里理解，而不是混入主表 headline。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2509_22093_ADP.pdf]]，``PDF p.8-9` Table 3`。

## 不可混写项
- `1.35×` speedup 是在 OpenVLA-OFT / LIBERO 设置下的 headline；real-world 主结果的 headline 更接近 `1.49×` latency speedup，两者不能混成同一指标。
- abstract 里的 “25.8% improvements with OpenVLA” 与正文主实验的比较基线并不完全等同于所有 OFT / baseline 设定；引用时要明确比较对象。
- ADP 的强项依赖 manipulation phase 的 coarse-to-fine 动态结构；若推广到其他 VLA 场景，需要保留 task-dependent caveat。

## 影响页面
- [[wiki/papers/2509_22093_ADP.md|2509_22093_ADP]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
