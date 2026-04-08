# 2512_03044_Video2Act-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2512_03044_Video2Act.md|2512_03044_Video2Act]] 的单篇证据落点，用来把最容易 bundled 的 headline、benchmark、metric、setting 或 operating point 拆开，并为更细的补证提供稳定入口。
- 本页聚焦的 headline bundle：`8.9%` 与 `21.7%` 是相对 prior SOTA 的平均提升幅度，不是论文自己的绝对 success rate；若写 headline，需要避免和绝对 `73.3%` 混口径。

## Evidence
- `73.3%` 则是 real-world 平均成功率的绝对值。来源：[[raw/2512_03044_Video2Act.pdf]]，第 1 页摘要；第 6-7 页 real-world results。
- 补充证据命题：核心主张是：如果把视频扩散模型中的 foreground boundary 与 inter-frame motion variation 显式提炼出来，再异步注入一个更快的 DiT 动作专家，就能把 VDM 的感知优势转化成更强的操作策略，同时避免直接使用高维原始 diffusion token 带来的低效条件化。 来源：[[raw/2512_03044_Video2Act.pdf]]，表征动机与视觉证据：[[raw/2512_03044_Video2Act.pdf]] 第 2-3 页 Fig. 2 与相邻正文。这里说明 VDM latent features 相比通用视觉 encoder 更好地保留了空间与运动一致性，是后续 spatio-motional extraction 的主要动机。
- 主证据锚点 1：来源：[[raw/2512_03044_Video2Act.pdf]]，摘要与总命题：[[raw/2512_03044_Video2Act.pdf]] 第 1 页摘要与 Fig. 1。这里给出 dual-system framing、`8.9% / 21.7%` headline，以及“VDM perceptual system + DiT action system”的总体结构。
- 主证据锚点 2：来源：[[raw/2512_03044_Video2Act.pdf]]，表征动机与视觉证据：[[raw/2512_03044_Video2Act.pdf]] 第 2-3 页 Fig. 2 与相邻正文。这里说明 VDM latent features 相比通用视觉 encoder 更好地保留了空间与运动一致性，是后续 spatio-motional extraction 的主要动机。
- 主证据锚点 3：来源：[[raw/2512_03044_Video2Act.pdf]]，方法总览：[[raw/2512_03044_Video2Act.pdf]] 第 3-5 页 Fig. 3 与 Section 3。这里定义 `Spatial Filtering Operators`、`FFT`、异步 dual-system 更新方式，以及为什么只把结构化 spatio-motional signals 注入 DiT。

## Figure / Caption Anchors
- **Fig. 2 (p.3)**：caption 与正文清楚写出对比对象是 `DINOv2 / SigLIP / VDM` 的 Grad-CAM 可视化；它支撑的是 **VDM latent features 更稳定地关注 foreground object 且具有更强 temporal stability**，不是 task success rate。
- **Fig. 3 (p.5)**：caption 直接定义了 asynchronous dual-system framework：slow perceptual VDM 低频更新，fast DiT action head 高频执行；这才是“real-time action generation frequency” 的机制基础。
- **Fig. 10 / Fig. 11 (appendix)**：分别展示 action distribution 与 real-world Grad-CAM，对“robust to robot motion / viewpoint shifts”的措辞有补充价值，但属于 supporting figure，不替代主结果表。

## Figure / Caption / Wording Split
- `8.9%`、`21.7%`、`73.3%` 已在前面拆开；第三轮需要再收紧的是 `real-time` 与 `robust` 这类强措辞。文中更硬的直接部署数字是 **single 4090 / multi-GPU setup 下 587.9 ms cold-start latency**，因此不能把 `real-time action generation frequency` 直接改写成稳定的低毫秒级控制频率。来源：[[raw/2512_03044_Video2Act.pdf]]，第 6-7 页正文与 latency 描述。
- `Fig. 2` 只支撑 **VDM features preserve stronger spatial structure and motion-aware focus than static image encoders**；它不能直接替代 benchmark 表去证明 `8.9% / 21.7%` 的结果提升。来源：[[raw/2512_03044_Video2Act.pdf]]，第 3 页 Fig. 2 caption 与相邻正文。
- `Fig. 3` 支撑的是 **why asynchronous dual-system can keep System 2 low-frequency and System 1 high-frequency**；若引用时要解释“为什么 Video2Act 是 dual-system 而不是直接把 VDM 当视觉 encoder”，应回到这里。来源：[[raw/2512_03044_Video2Act.pdf]]，第 5 页 Fig. 3 caption 与相邻正文。
- 文中 `robust` 主要指对 robot motion、viewpoint change、illumination variation 和 real-world manipulation disturbance 的适应边界；它不是无条件泛化宣言。来源：[[raw/2512_03044_Video2Act.pdf]]，第 3 页 Fig. 2；第 6-7 页 real-world section；附录 Fig. 11 / Fig. 15。

## 不可混写项
- `8.9%` 与 `21.7%` 是相对 prior SOTA 的平均提升幅度，不是论文自己的绝对 success rate；若写 headline，需要避免和绝对 `73.3%` 混口径。
- 论文同时出现了 `ALOHA dual-arm robot` 与 `Agilex Robot / Cobot Magic` 的表述，平台命名需要后续统一核对，避免把不同 real-world setup 混成同一实验描述。
- 论文强调 `real-time action generation frequency`，但主文里更明确给出了 `587.9 ms` cold-start latency，而非一个统一稳定的控制频率 headline；若写“实时”需要保留这个 caveat。

## 影响页面
- [[wiki/papers/2512_03044_Video2Act.md|2512_03044_Video2Act]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
- 若某个 table / figure / wording 会被多个页面复用，再从此页继续抽成更细的独立 evidence page。
