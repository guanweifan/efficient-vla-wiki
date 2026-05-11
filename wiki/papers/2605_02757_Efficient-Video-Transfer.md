# 2605_02757_Efficient-Video-Transfer

## Source
- Raw: [[raw/2605_02757_Efficient-Video-Transfer.pdf]]
- Extracts manifest: [[extracts/parses/2605_02757_Efficient-Video-Transfer/manifest.json]]
- Primary text fallback: [[extracts/parses/2605_02757_Efficient-Video-Transfer/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **VLA data augmentation efficiency / sim-to-real video transfer** 论文；它的核心效率目标是降低 realistic training video augmentation 的生成成本与数据选择成本。
- 方法把 simulation videos 转成 realistic training videos：先生成/改写 captions 与 structural conditions，再用 conditional video diffusion model 合成视频，同时保持 task semantics 和 action trajectories。来源：[[raw/2605_02757_Efficient-Video-Transfer.pdf]]，Abstract、Figure 1、method section。
- 为了让 augmentation 可规模化，论文提出 segmented velocity caching 来复用 video diffusion denoising 过程中的 velocity predictions，并用 trajectory-level coreset sampling 选择 high-value simulated trajectories。来源：[[raw/2605_02757_Efficient-Video-Transfer.pdf]]，Abstract、Figure 3、Figure 4、Algorithm 1。
- headline 结果需要拆开理解：
  - Robotwin / LIBERO / LIBERO-Plus / real robot 是 downstream policy evaluation；
  - `over 60%` generation-time reduction 是 video transfer acceleration 口径；
  - coreset sampling 是选择要增强的数据子集，不是 VLA policy 推理缓存。
- 更稳的主张是：Efficient Video Transfer 是 data-centric training efficiency 的新增例子，连接 synthetic/sim data、video diffusion generation cost 和 VLA training data construction。

## Methodology Index
- VLA data augmentation
- sim-to-real video transfer
- conditional video diffusion
- caption rewriting
- structured condition extraction
- velocity caching
- segmented caching strategy
- trajectory-level coreset sampling
- policy difficulty
- visual diversity
- Robotwin 2.0 / LIBERO / LIBERO-Plus

## Data Pointer
- **Abstract / Figure 1**：overall video transfer framework。
- **Figure 2**：LIBERO-Plus perturbation examples。
- **Figure 3 / Algorithm 1**：velocity caching mechanism。
- **Figure 4 / Figure 6 / Figure 7**：coreset sampling。
- **Table 1 / Table 2 / Table 3**：Robotwin / LIBERO-Plus simulation results。
- **Table 4**：real-world success counts。
- **Table 5 / Figure 8**：velocity cache acceleration and quality/performance comparison。

## Evidence Links
- [[wiki/evidence/claims/2605_02757_Efficient-Video-Transfer-headline-split.md|2605_02757_Efficient-Video-Transfer-headline-split]]

## 待核点
- 论文 PDF 中 abstract 处只写到 `Code is available at: CODE`，未给出可回到 PDF 的具体代码 URL；wiki 当前只记录原文可证的 code wording，不核验外部代码链接。
- 该论文的缓存作用于 video diffusion augmentation，不应和 VLA inference KV/cache reuse 混写。
- 如后续比较 training data efficiency，需要拆清 augmentation ratio、replacement/mixture strategy 与 benchmark perturbation setting。
