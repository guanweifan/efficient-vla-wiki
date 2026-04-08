# 2410_08001_RoboDual-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2410_08001_RoboDual.md|2410_08001_RoboDual]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：abstract 里的 `26.7% improvement in real-world setting` 需要后续明确它对应的是哪一个聚合指标、哪组 baseline、哪张表或哪张图；当前只能把它保留为作者 headline claim；若需精确比较，仍应回到对应表格、图或 caption 单元。

## Evidence
- 核心证据命题：这篇论文要解决的是：VLA/generalist 有泛化和高层语义理解，但训练与推理成本高、控制慢、额外模态接入困难；specialist 高效、精确，但泛化差。作者认为不该只继续“加大 generalist”，而应让两类系统协同。 来源：[[raw/2410_08001_RoboDual.pdf]]，`PDF p.1` Abstract + Fig. 1：
- 补充证据命题：作者提出 `RoboDual`，把 generalist 与 specialist 组成一个协同 dual-system：generalist 基于 OpenVLA，提供高层 task understanding、latent representation 和 discretized actions；specialist 是一个 diffusion transformer policy，在这些 generalist 输出和额外感知输入条件下做快速、精细的动作 rollout。 来源：[[raw/2410_08001_RoboDual.pdf]]，RoboDual 的问题设定、dual-system 总体框架、`26.7%` / `12%` / `5% demos` / `3.8x control frequency` 这些 headline claim 都在这里。
- 主证据锚点 1：来源：[[raw/2410_08001_RoboDual.pdf]]，`PDF p.1` Abstract + Fig. 1：
- 主证据锚点 2：来源：[[raw/2410_08001_RoboDual.pdf]]，RoboDual 的问题设定、dual-system 总体框架、`26.7%` / `12%` / `5% demos` / `3.8x control frequency` 这些 headline claim 都在这里。
- 主证据锚点 3：来源：[[raw/2410_08001_RoboDual.pdf]]，`PDF p.4-6` Sec. 3.1-3.3 + Fig. 2：

## Table / Metric Anchors
- `PDF p.7` Table 1 + Table 2：
  - CALVIN 主结果和 free-form instruction robustness；用于锚定 generalist-level 泛化与 instruction-following 证据。
- `PDF p.8` Fig. 3 + Table 3：
  - 真实世界多任务与 generalizability evaluation；是 `+20%` aggregate real-world improvement 与泛化表现的主证据位置。
- `PDF p.9` Fig. 5 + Table 4：
  - training efficiency、data efficiency、few-shot adaptation 的核心证据，尤其是 `5% demos` 和 real-world few-shot 表现。

## Table / Metric Split
- ``PDF p.7` Table 1 + Table 2` 这一层支撑 ``PDF p.7` Table 1 + Table 2` 对应的 benchmark / metric / operating point。 - CALVIN 主结果和 free-form instruction robustness；当前对应 generalist-level 泛化与 instruction-following 证据。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2410_08001_RoboDual.pdf]]，``PDF p.7` Table 1 + Table 2`。
- ``PDF p.8` Fig. 3 + Table 3` 这一层支撑 ``PDF p.8` Fig. 3 + Table 3` 对应的 benchmark / metric / operating point。 - 真实世界多任务与 generalizability evaluation；是 `+20%` aggregate real-world improvement 与泛化表现的主证据位置。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2410_08001_RoboDual.pdf]]，``PDF p.8` Fig. 3 + Table 3`。
- ``PDF p.9` Fig. 5 + Table 4` 这一层支撑 ``PDF p.9` Fig. 5 + Table 4` 对应的 benchmark / metric / operating point。 - training efficiency、data efficiency、few-shot adaptation 的核心证据，尤其是 `5% demos` 和 real-world few-shot 表现。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2410_08001_RoboDual.pdf]]，``PDF p.9` Fig. 5 + Table 4`。

## 不可混写项
- abstract 里的 `26.7% improvement in real-world setting` 需要后续明确它对应的是哪一个聚合指标、哪组 baseline、哪张表或哪张图；当前只能把它保留为作者 headline claim；若需精确比较，仍应回到对应表格、图或 caption 单元。
- `12% gain on CALVIN` 与正文 `3.27 -> 3.66` / `3.52` / `3.44` 这些数字出现在不同效率分析语境中；若要写成稳定比较，需要区分 “fully-trained generalist baseline” 和 “under-trained generalist + one-hour adaptation”。
- `5% demonstrations` 同时出现在 CALVIN 和 real-world few-shot 讨论中；若做横向比较，需要拆开模拟环境与真实环境的 data-efficiency 证据，也不要和 `20M specialist parameters`、`15 Hz` 这些系统级 headline 混写。

## 影响页面
- [[wiki/papers/2410_08001_RoboDual.md|2410_08001_RoboDual]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
