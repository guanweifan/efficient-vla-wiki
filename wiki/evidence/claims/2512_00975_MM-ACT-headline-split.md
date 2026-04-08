# 2512_00975_MM-ACT-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2512_00975_MM-ACT.md|2512_00975_MM-ACT]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`96.3%` / `72.0%` / `52.38%` 分别来自 LIBERO、Franka real-robot、RoboTwin2.0，不应混成一个统一 benchmark headline。

## Evidence
- 核心证据命题：这篇论文要解决的是：统一型 VLA 如果继续沿用 autoregressive text generation，再分别为 image / action 设计 diffusion 或 re-mask 生成，会导致 attention 机制与训练流程复杂；而 fully autoregressive 的统一生成又会让 action inference 过慢。 来源：[[raw/2512_00975_MM-ACT.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 补充证据命题：作者提出 `MM-ACT`，把 text、image、action 统一到共享离散 token space 中，并采用 `parallel decoding` 做三模态生成：text 和 image 采用 re-mask parallel decoding，action 采用 one-step parallel decoding，从而在统一建模的同时兼顾动作推理效率。 来源：[[raw/2512_00975_MM-ACT.pdf]]，unified VLA 三种 generation paradigm 的对比、MM-ACT 的 parallel decoding 路线、以及 `96.3% / 72.0% / 52.38% / +9.25%` 的 headline 都在这里。
- 主证据锚点 1：来源：[[raw/2512_00975_MM-ACT.pdf]]，`PDF p.1-2` Abstract + Fig. 1：
- 主证据锚点 2：来源：[[raw/2512_00975_MM-ACT.pdf]]，unified VLA 三种 generation paradigm 的对比、MM-ACT 的 parallel decoding 路线、以及 `96.3% / 72.0% / 52.38% / +9.25%` 的 headline 都在这里。
- 主证据锚点 3：来源：[[raw/2512_00975_MM-ACT.pdf]]，`PDF p.3-5` Sec. 3 + Fig. 2 / Fig. 3：

## Table / Metric Anchors
- `PDF p.6-8` Table 1：
  - LIBERO 主结果与 multimodal learning 对 long-horizon planning 的增益都在这里；`96.3%` overall 与 Libero-Long 从 `88.0%` 到 `93.0%` 的提升也在这里。
- `PDF p.7-8` Table 2：
  - RoboTwin2.0 八任务主结果在这里；`52.38%` overall 与 `+9.25%` 的 multimodal learning gain 对照可回这里。
- `PDF p.8` Table 3：
  - Franka real-world 三任务的 `72.0%` average 与对 π0 / OpenVLA-OFT 的比较在这里。
- `PDF p.8-9` Table 4：
  - image generation 质量（PSNR / SSIM / LPIPS）与 Stage 1 / Stage 2 的对比在这里，用于锚定“共享训练是否也提升 image prediction”。
- `PDF p.9-10` Table 6 / Table 7：
  - one-step parallel decoding vs re-mask decoding 的 action efficiency / quality tradeoff 在这里；`action chunk size = 8` 时最终选择 one-step parallel decoding、最高 generation frequency 约 `40 Hz (5 Hz per action chunk)` 的依据也在这里。

## Table / Metric Split
- ``PDF p.6-8` Table 1` 这一层支撑 ``PDF p.6-8` Table 1` 对应的 benchmark / metric / operating point。 - LIBERO 主结果与 multimodal learning 对 long-horizon planning 的增益都在这里；`96.3%` overall 与 Libero-Long 从 `88.0%` 到 `93.0%` 的提升也在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2512_00975_MM-ACT.pdf]]，``PDF p.6-8` Table 1`。
- ``PDF p.7-8` Table 2` 这一层支撑 ``PDF p.7-8` Table 2` 对应的 benchmark / metric / operating point。 - RoboTwin2.0 八任务主结果在这里；`52.38%` overall 与 `+9.25%` 的 multimodal learning gain 对照可回这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2512_00975_MM-ACT.pdf]]，``PDF p.7-8` Table 2`。
- ``PDF p.8` Table 3` 这一层支撑 ``PDF p.8` Table 3` 对应的 benchmark / metric / operating point。 - Franka real-world 三任务的 `72.0%` average 与对 π0 / OpenVLA-OFT 的比较在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2512_00975_MM-ACT.pdf]]，``PDF p.8` Table 3`。
- ``PDF p.8-9` Table 4` 这一层支撑 ``PDF p.8-9` Table 4` 对应的 benchmark / metric / operating point。 - image generation 质量（PSNR / SSIM / LPIPS）与 Stage 1 / Stage 2 的对比在这里，当前对应“共享训练是否也提升 image prediction”。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2512_00975_MM-ACT.pdf]]，``PDF p.8-9` Table 4`。
- ``PDF p.9-10` Table 6 / Table 7` 这一层支撑 ``PDF p.9-10` Table 6 / Table 7` 对应的 benchmark / metric / operating point。 - one-step parallel decoding vs re-mask decoding 的 action efficiency / quality tradeoff 在这里；`action chunk size = 8` 时最终选择 one-step parallel decoding、最高 generation frequency 约 `40 Hz (5 Hz per action chunk)` 的依据也在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2512_00975_MM-ACT.pdf]]，``PDF p.9-10` Table 6 / Table 7`。

## 不可混写项
- `96.3%` / `72.0%` / `52.38%` 分别来自 LIBERO、Franka real-robot、RoboTwin2.0，不应混成一个统一 benchmark headline。
- `+9.25%` 是相对于 RoboTwin action-only baseline 的 multimodal co-training gain，不是对所有 benchmark 的统一增益。
- 论文同时使用两种 parallel decoding 策略：text/image 用 re-mask，action 用 one-step；若写成“统一 parallel decoding”，应保留 modality-specific decoding 差异。

## 影响页面
- [[wiki/papers/2512_00975_MM-ACT.md|2512_00975_MM-ACT]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
