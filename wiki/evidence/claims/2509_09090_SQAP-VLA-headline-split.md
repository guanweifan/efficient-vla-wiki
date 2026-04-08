# 2509_09090_SQAP-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2509_09090_SQAP-VLA.md|2509_09090_SQAP-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`1.93× speedup`、`4.5% average success rate enhancement`、`36% improvement over EfficientVLA` 来自不同段落和不同比较对象；仍需把 baseline、场景和指标拆清，避免把它们误写成同一个统一 claim。

## Evidence
- 这篇论文提出 **SQAP-VLA**，试图解决一个明确的系统问题：在 VLA 上，低比特量化和 visual token pruning 并不是天然可叠加的，两者直接拼接会因为 attention / feature distribution 扭曲而导致明显性能下降。作者把自己的主要贡献定义为：第一次给出一个**结构化、training-free** 的联合框架，让量化与剪枝可以协同工作，而不是彼此破坏。来源：[[raw/2509_09090_SQAP-VLA.pdf]]，第 1 页 Abstract；第 2-3 页 Introduction。
- 核心方法主张是“co-design”而不是单点技巧：在 pruning 侧，SQAP-VLA 引入 **quantization-insensitive preservation**、**robot-aware protection**、**spatially-aware sampling**；在 quantization 侧，则通过 **Hadamard transformation** 与 **tensor-wise quantization** 提高 pruning criteria 的稳定性。来源：[[raw/2509_09090_SQAP-VLA.pdf]]，第 2-5 页 Fig. 1、Sec. 3。
- 主证据锚点 1：来源：[[raw/2509_09090_SQAP-VLA.pdf]]，**Abstract**：第 1 页。可直接承载“first structured training-free framework + 1.93× + 4.5%”的 headline claim。
- 主证据锚点 2：来源：[[raw/2509_09090_SQAP-VLA.pdf]]，**Figure 1 + Introduction**：第 2-3 页。用于锚定 incompatibility framing 与 co-design 总体结构。
- 主证据锚点 3：来源：[[raw/2509_09090_SQAP-VLA.pdf]]，**Sec. 3 / Figure 2 / Figure 3**：第 3-5 页。用于锚定三种 pruning 策略，以及 Hadamard + tensor-wise quantization 的方法细节。

## Table / Metric Anchors
- **Table 1 / Table 2**：第 6-7 页。用于锚定 visual matching / variant aggregation 场景下相对 CogACT、EfficientVLA、VLA-Cache 等方法的 success-rate 对比。
- **Figure 4 + Table 3 / Table 4**：第 7-8 页。用于锚定 `1.93×` speedup、LLM backbone `2.56×`、memory `14.3 GB -> 7.6 GB`、以及 pruning ratio / compression strategy 的 ablation。

## Table / Metric Split
- `**Table 1 / Table 2**` 这一层应单独承载 `**Table 1 / Table 2**` 相关的 benchmark / metric / operating point。 这一层对应 visual matching / variant aggregation 场景下相对 CogACT、EfficientVLA、VLA-Cache 等方法的 success-rate 对比。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2509_09090_SQAP-VLA.pdf]]，`**Table 1 / Table 2**`。
- `**Figure 4 + Table 3 / Table 4**` 这一层应单独承载 `**Figure 4 + Table 3 / Table 4**` 相关的 benchmark / metric / operating point。 这里收口为：**Figure 4 + Table 3 / Table 4**：第 7-8 页。当前对应 `1.93×` speedup、LLM backbone `2.56×`、memory `14.3 GB -> 7.6 GB`、以及 pruning ratio / compression strategy 的 ablation。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2509_09090_SQAP-VLA.pdf]]，`**Figure 4 + Table 3 / Table 4**`。

## 不可混写项
- `1.93× speedup`、`4.5% average success rate enhancement`、`36% improvement over EfficientVLA` 来自不同段落和不同比较对象；仍需把 baseline、场景和指标拆清，避免把它们误写成同一个统一 claim。
- 当前实验主体围绕 **CogACT** 和仿真任务展开，且 visual matching / variant aggregation 两类场景的表现不完全一致；仍需决定在单篇页里如何呈现这种 benchmark dependence。
- 论文同时强调 training-free、W4A4、edge deployment、co-design；后续 taxonomy 需要决定是把它优先归入 `quantization+pruning co-design`，还是更泛的 `VLA inference acceleration`。

## 影响页面
- [[wiki/papers/2509_09090_SQAP-VLA.md|2509_09090_SQAP-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
