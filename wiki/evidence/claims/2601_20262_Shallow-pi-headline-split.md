# 2601_20262_Shallow-pi-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2601_20262_Shallow-pi.md|2601_20262_Shallow-pi]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`over 2× faster inference` 与 `<1% absolute drop` 主要锚定在 simulation benchmark 与 `L6` student 的 teacher 对比，不应直接泛化成所有部署场景下的统一结论。

## Evidence
- `Jetson Orin` 上接近 `10 Hz` 是特定 real-world deployment 口径，并带有 action chunk size 与 control-loop 条件。来源：[[raw/2601_20262_Shallow-pi.pdf]]，第 1 页摘要；第 6-7 页 Table 2；第 7-8 页 Table 3。
- 补充证据命题：核心主张是：对 `π`-like flow-based VLA 同时压缩 `VLM backbone` 与 `action head` 的 transformer 深度，并用针对该架构定制的知识蒸馏目标去保留层间条件传递，可以比 test-time layer skipping 更稳定地做深层裁剪，同时保持接近 teacher 的操控性能。 来源：[[raw/2601_20262_Shallow-pi.pdf]]，延迟动机与层裁剪理由：[[raw/2601_20262_Shallow-pi.pdf]] 第 3-4 页 Fig. 2、Fig. 3 与 Section 3-4。这里说明为什么在 flow-based VLA 上 layer reduction 比 token reduction 更直接影响 wall-clock latency，以及 test-time layer skipping 为什么不够稳。
- 主证据锚点 1：来源：[[raw/2601_20262_Shallow-pi.pdf]]，摘要与总体命题：[[raw/2601_20262_Shallow-pi.pdf]] 第 1 页摘要与 Fig. 1。这里给出 `18 → 6 layers`、`2× faster`、`<1% absolute drop` 与“jointly compress backbone + action head”的主命题。
- 主证据锚点 2：来源：[[raw/2601_20262_Shallow-pi.pdf]]，延迟动机与层裁剪理由：[[raw/2601_20262_Shallow-pi.pdf]] 第 3-4 页 Fig. 2、Fig. 3 与 Section 3-4。这里说明为什么在 flow-based VLA 上 layer reduction 比 token reduction 更直接影响 wall-clock latency，以及 test-time layer skipping 为什么不够稳。
- 主证据锚点 3：来源：[[raw/2601_20262_Shallow-pi.pdf]]，蒸馏框架：[[raw/2601_20262_Shallow-pi.pdf]] 第 5 页 Fig. 5 与相邻正文。这里定义 `ground-truth supervision`、`teacher trajectory imitation`、`intermediate attention transfer` 三类 distillation objective。

## Table / Metric Anchors
- 模拟主结果：[[raw/2601_20262_Shallow-pi.pdf]] 第 6-7 页 Table 2。这里可回查 `π0/π0.5` teacher、`L9/L6` shallow student、`SmolVLA` 与 token compression 方法的 `Avg / FLOPs / CUDA Time` 对比。
- 真实机器人与部署结果：[[raw/2601_20262_Shallow-pi.pdf]] 第 7-8 页 Table 3、Fig. 6、Fig. 10-11。这里对应 `Jetson Orin / Thor` 上的端到端 latency、动态任务表现、未见环境泛化，以及 “almost 10 Hz” 的部署 claim。

## Table / Metric Split
- `模拟主结果` 这一层应单独承载 `模拟主结果` 相关的 benchmark / metric / operating point。 这里收口为：模拟主结果：[[raw/2601_20262_Shallow-pi.pdf]] 第 6-7 页 Table 2。这里可回查 `π0/π0.5` teacher、`L9/L6` shallow student、`SmolVLA` 与 token compression 方法的 `Avg / FLOPs / CUDA Time` 对比。；真实机器人对比主要是 teacher 与 `SmolVLA`，并非大规模横向比较所有高效 VLA；因此“real-world strongest”需要比 simulation headline 更保守。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2601_20262_Shallow-pi.pdf]]，`模拟主结果`。
- `真实机器人与部署结果` 这一层应单独承载 `真实机器人与部署结果` 相关的 benchmark / metric / operating point。 这里收口为：真实机器人与部署结果：[[raw/2601_20262_Shallow-pi.pdf]] 第 7-8 页 Table 3、Fig. 6、Fig. 10-11。这里对应 `Jetson Orin / Thor` 上的端到端 latency、动态任务表现、未见环境泛化，以及 “almost 10 Hz” 的部署 claim。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2601_20262_Shallow-pi.pdf]]，`真实机器人与部署结果`。

## 不可混写项
- `over 2× faster inference` 与 `<1% absolute drop` 主要锚定在 simulation benchmark 与 `L6` student 的 teacher 对比，不应直接泛化成所有部署场景下的统一结论。
- `almost 10 Hz on Jetson Orin` 依赖特定 real-robot deployment 设置，包括 `action chunk size = 50`、`30 Hz control loop`、每次执行 `7` 个 action 后再请求新 inference；若写实时部署能力，需要保留这些条件。
- 真实机器人对比主要是 teacher 与 `SmolVLA`，并非大规模横向比较所有高效 VLA；因此“real-world strongest”需要比 simulation headline 更保守。

## 影响页面
- [[wiki/papers/2601_20262_Shallow-pi.md|2601_20262_Shallow-pi]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
