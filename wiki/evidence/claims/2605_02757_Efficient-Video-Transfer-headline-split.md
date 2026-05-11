# 2605_02757_Efficient-Video-Transfer-headline-split

## 用途
- 当前页服务于 [[wiki/papers/2605_02757_Efficient-Video-Transfer.md|2605_02757_Efficient-Video-Transfer]] 的单篇证据落点，用来拆分 sim-to-real video augmentation、velocity caching、coreset sampling 与 downstream VLA benchmark headline。
- 本页聚焦的 headline bundle：`efficient video transfer`、`over 60% generation-time reduction`、`coreset sampling`、`Robotwin / LIBERO-Plus gains` 需要分层阅读。

## Evidence
- 核心证据命题：论文将 simulated VLA videos 转成 realistic training videos，并通过 captions、rewritten contexts、structural/depth conditions 和 conditional video diffusion 保持 task semantics 与 action trajectories。来源：[[raw/2605_02757_Efficient-Video-Transfer.pdf]]，Abstract、Figure 1、Section 3.2。
- 加速证据命题：velocity caching 复用 video diffusion denoising 中相邻 timesteps 的 velocity predictions，并在 Figure 8 / appendix 中报告平均超过 60% 的 generation-time reduction。来源：[[raw/2605_02757_Efficient-Video-Transfer.pdf]]，Figure 3、Algorithm 1、Figure 8。
- 数据选择证据命题：trajectory-level coreset sampling 结合 policy difficulty 与 visual diversity，选择 compact high-value trajectories for augmentation。来源：[[raw/2605_02757_Efficient-Video-Transfer.pdf]]，Figure 4、Figure 6、Figure 7。

## Table / Metric Anchors
- **Figure 1**：overall framework。
- **Figure 3 / Algorithm 1**：velocity caching。
- **Figure 4 / Figure 6 / Figure 7**：coreset sampling。
- **Table 1-3**：Robotwin / LIBERO-Plus simulation results。
- **Table 4**：real-world results。
- **Table 5 / Figure 8**：velocity cache acceleration and impact。

## Table / Metric Split
- generation-time reduction 属于 data augmentation pipeline，不是 VLA policy inference speedup。
- Robotwin、LIBERO、LIBERO-Plus 和 real-world results 是不同 evaluation settings。
- coreset percentage、mixture/replacement strategy 和 policy backbone 会影响结果解释。

## 不可混写项
- 不应把 video diffusion velocity cache 写成 temporal KV cache。
- 不应把 data augmentation gain 写成模型结构本身更高效。
- 不应把 sim-to-real robustness 结果合并成单一通用 VLA improvement。

## 影响页面
- [[wiki/papers/2605_02757_Efficient-Video-Transfer.md|2605_02757_Efficient-Video-Transfer]]
- [[wiki/synthesis/training-efficiency-routes.md|training-efficiency-routes]]
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]

## 边界
- 本页只承担单篇证据落点，不承担跨论文 synthesis。
