# 2511_01718_UNIFIED-DIFFUSION-VLA-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2511_01718_UNIFIED-DIFFUSION-VLA.md|2511_01718_UNIFIED-DIFFUSION-VLA]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`4× faster inference` 是 abstract headline，而正文更具体的 decoding analysis 给出的是 `JD3P` 相对 AR 约 `4.3×`；引用时需统一 headline vs table value，并避免把 decoding speed 误写成跨 benchmark 的统一 wall-clock latency。

## Evidence
- 核心证据命题：这篇论文要解决的是：统一型 VLA 既要理解视觉和语言，又要生成未来图像并输出动作，但现有 unified VLA 往往依赖外部 expert 做模态拼接，或者虽然把输入输出 token 化了，却仍把图像生成和动作预测拆成独立过程，导致两者协同不足、推理延迟较高。 来源：[[raw/2511_01718_UNIFIED-DIFFUSION-VLA.pdf]]，`PDF p.1-2` Abstract + Introduction：
- 补充证据命题：作者提出 `Unified Diffusion VLA (UD-VLA)`，核心机制是 `Joint Discrete Denoising Diffusion Process (JD3P)`：未来图像 token 与动作 token 在同一条离散 diffusion 轨迹中同步去噪，在每个 denoising step 里动作持续接受未来图像的信息，从而让 understanding、generation、acting 形成更紧的耦合。 来源：[[raw/2511_01718_UNIFIED-DIFFUSION-VLA.pdf]]，unified VLA 的问题定义、为何“joint denoising”优于分离式 image/action decoding，以及 `4× faster inference` 的 headline 在这里。
- 主证据锚点 1：来源：[[raw/2511_01718_UNIFIED-DIFFUSION-VLA.pdf]]，`PDF p.1-2` Abstract + Introduction：
- 主证据锚点 2：来源：[[raw/2511_01718_UNIFIED-DIFFUSION-VLA.pdf]]，unified VLA 的问题定义、为何“joint denoising”优于分离式 image/action decoding，以及 `4× faster inference` 的 headline 在这里。
- 主证据锚点 3：来源：[[raw/2511_01718_UNIFIED-DIFFUSION-VLA.pdf]]，`PDF p.2-3` Table 1：

## Table / Metric Anchors
- `PDF p.2-3` Table 1：
  - unified VLA 各路线的组件对比在这里，用于锚定“UD-VLA 与 extrinsic experts / separate decoding 的结构差异”。
- `PDF p.7` Table 2：
  - CALVIN 主结果在这里；`UD-VLA` 的 average success length `4.64` 来自该表。
- `PDF p.8` Table 3：
  - LIBERO 主结果在这里；`92.7%` average、`95.7%` Object、`89.6%` Long 等核心数据在这里。
- `PDF p.8-9` Table 4：
  - SimplerEnv-WidowX 的 `59.4%` overall success rate 在这里。
- `PDF p.9-10` Table 7：
  - AR、Jacobi、independent diffusion、JD3P 的 decoding mechanism 对比在这里；`4.3× faster decoding speed` 与 `4.64` average length 的效率-性能对比应回到这张表，而不是只引用 abstract 里的 `4×` headline。

## Table / Metric Split
- ``PDF p.2-3` Table 1` 这一层支撑 ``PDF p.2-3` Table 1` 对应的 benchmark / metric / operating point。 - unified VLA 各路线的组件对比在这里，当前对应“UD-VLA 与 extrinsic experts / separate decoding 的结构差异”。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2511_01718_UNIFIED-DIFFUSION-VLA.pdf]]，``PDF p.2-3` Table 1`。
- ``PDF p.7` Table 2` 这一层支撑 ``PDF p.7` Table 2` 对应的 benchmark / metric / operating point。 - CALVIN 主结果在这里；`UD-VLA` 的 average success length `4.64` 来自该表。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2511_01718_UNIFIED-DIFFUSION-VLA.pdf]]，``PDF p.7` Table 2`。
- ``PDF p.8` Table 3` 这一层支撑 ``PDF p.8` Table 3` 对应的 benchmark / metric / operating point。 - LIBERO 主结果在这里；`92.7%` average、`95.7%` Object、`89.6%` Long 等核心数据在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2511_01718_UNIFIED-DIFFUSION-VLA.pdf]]，``PDF p.8` Table 3`。
- ``PDF p.8-9` Table 4` 这一层支撑 ``PDF p.8-9` Table 4` 对应的 benchmark / metric / operating point。 - SimplerEnv-WidowX 的 `59.4%` overall success rate 在这里。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2511_01718_UNIFIED-DIFFUSION-VLA.pdf]]，``PDF p.8-9` Table 4`。
- ``PDF p.9-10` Table 7` 这一层支撑 ``PDF p.9-10` Table 7` 对应的 benchmark / metric / operating point。 - AR、Jacobi、independent diffusion、JD3P 的 decoding mechanism 对比在这里；`4.3× faster decoding speed` 与 `4.64` average length 的效率-性能对比应回到这张表，而不是只引用 abstract 里的 `4×` headline。引用时必须限定在这一层对应的表格、图或 setting 内，不把它与同页其他结果、其他 benchmark、部署口径或训练成本 headline 混写。来源：[[raw/2511_01718_UNIFIED-DIFFUSION-VLA.pdf]]，``PDF p.9-10` Table 7`。

## 不可混写项
- `4× faster inference` 是 abstract headline，而正文更具体的 decoding analysis 给出的是 `JD3P` 相对 AR 约 `4.3×`；引用时需统一 headline vs table value，并避免把 decoding speed 误写成跨 benchmark 的统一 wall-clock latency。
- `SOTA` 分别落在 CALVIN、LIBERO、SimplerEnv 上，但比较基线并不完全一致；若写成统一“全 benchmark 全面领先”，需要保留 benchmark-specific caveat。
- 论文把多种 test-time efficiency 技巧一起用于推理（KV-cache、prefilled special tokens、candidate remapping、confidence-based decoding）；若单独归因于 JD3P，需要避免把所有收益都压到一个机制上。

## 影响页面
- [[wiki/papers/2511_01718_UNIFIED-DIFFUSION-VLA.md|2511_01718_UNIFIED-DIFFUSION-VLA]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
