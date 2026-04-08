# 2504_19854_NORA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2504_19854_NORA.md|2504_19854_NORA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：论文 abstract 说 NORA “outperforms existing large-scale VLA models”，但主文真实任务表中只直接对比了 `RT-1`、`OpenVLA`、`SpatialVLA`；若写更宽泛结论，需要明确比较范围。

## Evidence
- 核心证据命题：这篇论文要解决的是：现有 VLA 往往接近或超过 `7B` 参数，推理和微调成本高，难以在消费级 GPU 上做高效适配；同时视觉编码不足会在抓取等任务上造成失败。 来源：[[raw/2504_19854_NORA.pdf]]，`PDF p.1` Abstract：
- 补充证据命题：作者提出 `NORA`，一个基于 `Qwen-2.5-VL-3B` 的 `3B` 参数 VLA，目标是在更小模型规模下保留较强的视觉语义理解和任务执行能力。 来源：[[raw/2504_19854_NORA.pdf]]，NORA 的问题设定、`3B`、`Qwen-2.5-VL-3B`、`970k demonstrations`、`FAST+ tokenizer`、以及“超过大模型 baseline”的 headline 都在这里。
- 主证据锚点 1：来源：[[raw/2504_19854_NORA.pdf]]，`PDF p.1` Abstract：
- 主证据锚点 2：来源：[[raw/2504_19854_NORA.pdf]]，NORA 的问题设定、`3B`、`Qwen-2.5-VL-3B`、`970k demonstrations`、`FAST+ tokenizer`、以及“超过大模型 baseline”的 headline 都在这里。
- 主证据锚点 3：来源：[[raw/2504_19854_NORA.pdf]]，`PDF p.4-5` Sec. 3 + Fig. 1：

## Table / Metric Anchors
- `PDF p.6-8` Fig. 3 + Table 1 + Fig. 4：
  - WidowX 真实任务主结果；`Average 56.7`、各类任务（multiple objects / OOD object / spatial）的拆分结果都在这里。
- `PDF p.8-9` Table 2：
  - LIBERO 模拟环境结果，尤其是 `NORA-Long-fine-tuned = 87.9 average` 和 `LIBERO-Long = 74.6` 的核心证据在这里。

## Table / Metric Split
- ``PDF p.6-8` Fig. 3 + Table 1 + Fig. 4` 这一层支撑 ``PDF p.6-8` Fig. 3 + Table 1 + Fig. 4` 对应的 benchmark / metric / operating point。 - WidowX 真实任务主结果；`Average 56.7`、各类任务（multiple objects / OOD object / spatial）的拆分结果都在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2504_19854_NORA.pdf]]，``PDF p.6-8` Fig. 3 + Table 1 + Fig. 4`。
- ``PDF p.8-9` Table 2` 这一层支撑 ``PDF p.8-9` Table 2` 对应的 benchmark / metric / operating point。 - LIBERO 模拟环境结果，尤其是 `NORA-Long-fine-tuned = 87.9 average` 和 `LIBERO-Long = 74.6` 的核心证据在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2504_19854_NORA.pdf]]，``PDF p.8-9` Table 2`。

## 不可混写项
- 论文 abstract 说 NORA “outperforms existing large-scale VLA models”，但主文真实任务表中只直接对比了 `RT-1`、`OpenVLA`、`SpatialVLA`；若写更宽泛结论，需要明确比较范围。
- `NORA-Long` 是文中最佳 LIBERO 结果，但不等于 `NORA` 主模型在所有场景都更强；真实 WidowX 上作者明确写了 `NORA-Long` 更不稳，不能把两者混为一体。
- 真实场景里 NORA 在 multi-object tasks 上虽然最好，但成功率仍多在 `30-40%` 区间，如写“robust real-world performance”，需要保留这个 caveat。

## 影响页面
- [[wiki/papers/2504_19854_NORA.md|2504_19854_NORA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
