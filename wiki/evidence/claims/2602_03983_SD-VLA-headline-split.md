# 2602_03983_SD-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2602_03983_SD-VLA.md|2602_03983_SD-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`39.8% absolute improvement` 来自作者新建的 memory-dependent benchmark，而不是 SimplerEnv / LIBERO；引用时要明确 benchmark 范围。

## Evidence
- 核心证据命题：这篇论文要解决的是：VLA 处理多帧历史时会遇到两类问题，一是多帧拼接导致 context 迅速膨胀，二是每一步都重算全部视觉 token 的 KV cache 会造成很高的推理开销；因此现有 VLA 很难既保留长时记忆，又保持推理效率。 来源：[[raw/2602_03983_SD-VLA.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 补充证据命题：作者提出 `SD-VLA`，核心是 `static-dynamic disentanglement`：把视觉 token 拆成具有不同时间持久性的 static tokens 与 dynamic tokens。static tokens 跨多个 timestep 只保留一份，dynamic tokens 才随时间拼接；同时通过 trainable `recache gate` 决定 static tokens 何时复用、何时刷新，从而把长时记忆建模与 KV-cache 复用统一起来。 来源：[[raw/2602_03983_SD-VLA.pdf]]，long-horizon context 与 inference efficiency 的双重问题、static-dynamic disentanglement 的核心直觉、以及 `39.8%` / `2.26×` / `1.70×` 的 headline 都在这里。
- 主证据锚点 1：来源：[[raw/2602_03983_SD-VLA.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 主证据锚点 2：来源：[[raw/2602_03983_SD-VLA.pdf]]，long-horizon context 与 inference efficiency 的双重问题、static-dynamic disentanglement 的核心直觉、以及 `39.8%` / `2.26×` / `1.70×` 的 headline 都在这里。
- 主证据锚点 3：来源：[[raw/2602_03983_SD-VLA.pdf]]，`PDF p.3-5` Sec. 3 + Fig. 3：

## Table / Metric Anchors
- `PDF p.5-6` Table 1：
  - 作者提出的 memory-dependent benchmark 主结果在这里；`On Stove`、`Position Reset`、`Doneness` 三个指标都在这里。
- `PDF p.6-7` Table 2：
  - SimplerEnv 上与 base CogACT、FlashVLA、TTF、VLA-Cache 的比较在这里；`2.26×` speedup 与 `92.4` / `38.9` 等主结果应回这张表。

## Table / Metric Split
- ``PDF p.5-6` Table 1` 这一层支撑 ``PDF p.5-6` Table 1` 对应的 benchmark / metric / operating point。 - 作者提出的 memory-dependent benchmark 主结果在这里；`On Stove`、`Position Reset`、`Doneness` 三个指标都在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2602_03983_SD-VLA.pdf]]，``PDF p.5-6` Table 1`。
- ``PDF p.6-7` Table 2` 这一层支撑 ``PDF p.6-7` Table 2` 对应的 benchmark / metric / operating point。 - SimplerEnv 上与 base CogACT、FlashVLA、TTF、VLA-Cache 的比较在这里；`2.26×` speedup 与 `92.4` / `38.9` 等主结果应回这张表。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2602_03983_SD-VLA.pdf]]，``PDF p.6-7` Table 2`。

## 不可混写项
- `39.8% absolute improvement` 来自作者新建的 memory-dependent benchmark，而不是 SimplerEnv / LIBERO；引用时要明确 benchmark 范围。
- `2.26×` 与 `1.70×` 分别对应 SimplerEnv 与 LIBERO，不应混成一个统一 speedup 数值。
- 当前主文里最容易直接抓到的是 SimplerEnv 与 memory benchmark 的表格结果；LIBERO 的更细指标若仍需精确数值，可能还要继续回表格或附录核定。

## 影响页面
- [[wiki/papers/2602_03983_SD-VLA.md|2602_03983_SD-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
