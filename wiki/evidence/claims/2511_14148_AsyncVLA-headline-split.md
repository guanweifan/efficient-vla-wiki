# 2511_14148_AsyncVLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2511_14148_AsyncVLA.md|2511_14148_AsyncVLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：这篇没有一个统一的单一 headline 数字，而是跨 `LIBERO`、`WidowX`、`Google Robot` 三类评测；后续不能把不同 benchmark 的 success rate 直接压成一个泛化能力结论。

## Evidence
- 核心证据命题：这篇论文要解决的是：基于 flow matching 的 VLA 往往采用 rigid、uniform 的同步生成时间表（synchronous FM），缺乏对动作上下文和生成置信度的利用，因而在长时程或高精度任务中容易因为一次错误动作而级联失败。 来源：[[raw/2511_14148_AsyncVLA.pdf]]，摘要与核心命题：[[raw/2511_14148_AsyncVLA.pdf]] 第 1-2 页摘要、引言与 Fig. 1。这里定义 `SFM -> AFM` 的异步自纠正思路，并给出论文的总体 benchmark claim。
- 补充证据命题：核心主张是：把 action generation 改写成“先同步初生成、再异步自纠正”的两阶段过程，并让第二阶段只重生成低置信度 action token，就能在 continuous action generation 场景下引入 self-correction；再通过 unified training 让同一个模型同时支持 `SFM` 与 `AFM`，并在 AFM 推理阶段复用 VL KV-cache。 来源：[[raw/2511_14148_AsyncVLA.pdf]]，框架与方法：[[raw/2511_14148_AsyncVLA.pdf]] 第 3-5 页 Fig. 2 与方法章节。这里说明 `SFM`、`confidence rater`、`AFM` 如何串联，以及 unified training 为什么能支持 KV-cache 复用。
- 主证据锚点 1：来源：[[raw/2511_14148_AsyncVLA.pdf]]，摘要与核心命题：[[raw/2511_14148_AsyncVLA.pdf]] 第 1-2 页摘要、引言与 Fig. 1。这里定义 `SFM -> AFM` 的异步自纠正思路，并给出论文的总体 benchmark claim。
- 主证据锚点 2：来源：[[raw/2511_14148_AsyncVLA.pdf]]，框架与方法：[[raw/2511_14148_AsyncVLA.pdf]] 第 3-5 页 Fig. 2 与方法章节。这里说明 `SFM`、`confidence rater`、`AFM` 如何串联，以及 unified training 为什么能支持 KV-cache 复用。
- 主证据锚点 3：来源：[[raw/2511_14148_AsyncVLA.pdf]]，LIBERO 主结果与自纠正示例：[[raw/2511_14148_AsyncVLA.pdf]] 第 6 页 Table 1 与 Fig. 3。这里给出 `97.4%` LIBERO average success rate，以及在 `LIBERO-Long` 上 low-confidence action 被纠正的可视化例子。

## Table / Metric Anchors
- LIBERO 主结果与自纠正示例：[[raw/2511_14148_AsyncVLA.pdf]] 第 6 页 Table 1 与 Fig. 3。这里给出 `97.4%` LIBERO average success rate，以及在 `LIBERO-Long` 上 low-confidence action 被纠正的可视化例子。
- SimplerEnv 主结果：[[raw/2511_14148_AsyncVLA.pdf]] 第 6-7 页 Tables 2-3。这里分别对应 `WidowX` benchmark 的平均 `70.8%`，以及 `Google Robot` benchmark 在 visual matching / variant aggregation 两种 protocol 下的平均值。
- 组件消融与数据效率：[[raw/2511_14148_AsyncVLA.pdf]] 第 7-8 页 Table 4、Fig. 4、Fig. 5。这里说明 unified training、AFM inference、confidence rater 各自贡献，以及在数据受限设置下相对 vanilla SFM 的训练效率提升。
- 推理开销分解：[[raw/2511_14148_AsyncVLA.pdf]] 补充材料 Table 6。这里才是 “SFM 占 86.8% 推理时间、AFM 通过 KV-cache reuse 更高效” 的直接出处，适合支撑更窄的 inference-efficiency 表述。

## Table / Metric Split
- `LIBERO 主结果与自纠正示例` 这一层应单独承载 `LIBERO 主结果与自纠正示例` 相关的 benchmark / metric / operating point。 这里收口为：LIBERO 主结果与自纠正示例：[[raw/2511_14148_AsyncVLA.pdf]] 第 6 页 Table 1 与 Fig. 3。这里给出 `97.4%` LIBERO average success rate，以及在 `LIBERO-Long` 上 low-confidence action 被纠正的可视化例子。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2511_14148_AsyncVLA.pdf]]，`LIBERO 主结果与自纠正示例`。
- `SimplerEnv 主结果` 这一层应单独承载 `SimplerEnv 主结果` 相关的 benchmark / metric / operating point。 这里收口为：SimplerEnv 主结果：[[raw/2511_14148_AsyncVLA.pdf]] 第 6-7 页 Tables 2-3。这里分别对应 `WidowX` benchmark 的平均 `70.8%`，以及 `Google Robot` benchmark 在 visual matching / variant aggregation 两种 protocol 下的平均值。；这篇没有一个统一的单一 headline 数字，而是跨 `LIBERO`、`WidowX`、`Google Robot` 三类评测；后续不能把不同 benchmark 的 success rate 直接压成一个泛化能力结论。。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2511_14148_AsyncVLA.pdf]]，`SimplerEnv 主结果`。
- `组件消融与数据效率` 这一层应单独承载 `组件消融与数据效率` 相关的 benchmark / metric / operating point。 当前这一层说明 unified training、AFM inference、confidence rater 各自贡献，以及在数据受限设置下相对 vanilla SFM 的训练效率提升。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2511_14148_AsyncVLA.pdf]]，`组件消融与数据效率`。
- `推理开销分解` 这一层应单独承载 `推理开销分解` 相关的 benchmark / metric / operating point。 当前这一层才是 “SFM 占 86.8% 推理时间、AFM 通过 KV-cache reuse 更高效” 的直接出处，适合支撑更窄的 inference-efficiency 表述。引用时只在这一层对应的表格、指标和 setting 内对齐，不把它与同页其他结果、其他 benchmark 或部署口径混写。来源：[[raw/2511_14148_AsyncVLA.pdf]]，`推理开销分解`。

## 不可混写项
- 这篇没有一个统一的单一 headline 数字，而是跨 `LIBERO`、`WidowX`、`Google Robot` 三类评测；后续不能把不同 benchmark 的 success rate 直接压成一个泛化能力结论。
- `AsyncVLA` 的效率主张更多体现在 “better data efficiency / unified training / KV-cache utilization / AFM 比 SFM 更快”，而不是像纯加速论文那样给出统一 latency headline；若写“efficient”需要明确是训练利用效率与生成机制效率，不是单一 wall-clock headline。
- `Google Robot` 上 `π0` 在某些单项任务上略高于 AsyncVLA，`WidowX` 上也不是所有子任务都绝对领先；因此整体应写成“整体平均最好 / generally strongest”，而不是“每项都 SOTA”。

## 影响页面
- [[wiki/papers/2511_14148_AsyncVLA.md|2511_14148_AsyncVLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
