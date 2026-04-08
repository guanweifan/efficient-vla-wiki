# 2601_05248_LaST0-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2601_05248_LaST0.md|2601_05248_LaST0]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`8%`、`13% / 14% / 14%`、`14× speedup`、`15.4 Hz` 等数字来自不同评测层面；仍需拆清对应的 baseline、任务集合与比较口径。

## Evidence
- 这篇论文提出 **LaST0**，目标是在机器人操作中实现更高效的 **reason-before-act**，但不再显式生成冗长的语言 CoT 或未来图像，而是把推理压到一个 **Latent Spatio-Temporal CoT** 空间里。作者的核心判断是：显式 CoT 会带来显著推理延迟，而且语言空间本身不足以充分表达机器人操作中的细粒度物理与几何动态。来源：[[raw/2601_05248_LaST0.pdf]]，第 1-2 页 Abstract、Introduction、Fig. 1。
- 方法上的主张由两部分组成：一是一个 **token-efficient latent CoT space**，用于建模未来 2D 图像、3D 结构和机器人本体感知状态，从而形成时序一致的隐式推理轨迹；二是一个通过 **Mixture-of-Transformers (MoT)** 实现的 **dual-system architecture**，其中 `slow reasoning expert` 低频更新 latent CoT，`fast acting expert` 高频生成动作。来源：[[raw/2601_05248_LaST0.pdf]]，第 1-3 页 Abstract、Introduction；第 4-6 页 Fig. 2、Sec. 3。
- 主证据锚点 1：来源：[[raw/2601_05248_LaST0.pdf]]，**Abstract**：第 1 页。可直接承载 `latent CoT + dual-system + 13/14/14% + 14×` 的 headline。
- 主证据锚点 2：来源：[[raw/2601_05248_LaST0.pdf]]，**Figure 1 + Introduction**：第 1-2 页。用于锚定 explicit CoT vs latent CoT、reasoning latency 与 “difficult to verbalize” 的方法动机。
- 主证据锚点 3：来源：[[raw/2601_05248_LaST0.pdf]]，**Figure 2 + Sec. 3**：第 4-6 页。用于锚定 latent CoT space、MoT 双专家、fast/slow 交互和 heterogeneous frequency 训练机制。

## Table / Metric Anchors
- **Table 1 + Fig. 4**：第 6-8 页。用于锚定 RLBench / simulation 结果，以及 `15.4 Hz` 与显式 CoT 方法 / π0.5 的推理频率比较。
- **Table 2**：第 8 页后。用于锚定真实世界 single-arm / dual-arm / mobile manipulation 的 success-rate 对比。

## Table / Metric Split
- `**Table 1 + Fig. 4**` 这一层应单独承载 `**Table 1 + Fig. 4**` 相关的 benchmark / metric / operating point。 这里收口为：**Table 1 + Fig. 4**：第 6-8 页。当前对应 RLBench / simulation 结果，以及 `15.4 Hz` 与显式 CoT 方法 / π0.5 的推理频率比较。；`8%`、`13% / 14% / 14%`、`14× speedup`、`15.4 Hz` 等数字来自不同评测层面；这里需要拆清对应的 baseline、任务集合与比较口径。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2601_05248_LaST0.pdf]]，`**Table 1 + Fig. 4**`。
- `**Table 2**` 这一层应单独承载 `**Table 2**` 相关的 benchmark / metric / operating point。 这一层对应真实世界 single-arm / dual-arm / mobile manipulation 的 success-rate 对比。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2601_05248_LaST0.pdf]]，`**Table 2**`。

## 不可混写项
- `8%`、`13% / 14% / 14%`、`14× speedup`、`15.4 Hz` 等数字来自不同评测层面；仍需拆清对应的 baseline、任务集合与比较口径。
- 论文同时用 `LaST0`、`latent CoT`、`dual-system MoT` 三套 framing 讲方法；后续 taxonomy 需要统一它的主定位。
- `14× speedup over previous explicit CoT VLA approaches` 目前仍偏 headline 表述；仍应明确具体比较对象以及 speedup 是如何测得。

## 影响页面
- [[wiki/papers/2601_05248_LaST0.md|2601_05248_LaST0]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
