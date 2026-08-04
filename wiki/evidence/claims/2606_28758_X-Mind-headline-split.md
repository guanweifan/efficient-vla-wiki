# 2606_28758_X-Mind-headline-split

## 用途
- 服务于 [[wiki/papers/2606_28758_X-Mind.md|X-Mind]]，拆分 reasoning substrate、visual bandwidth 与 action planning。

## Evidence
- 方法证据命题：X-Mind 以 abstract sketch 取代 dense future rollout，并通过 recurrent block diffusion 把 iterative refinement 折入 backbone layers。来源：[[raw/2606_28758_X-Mind.pdf]]，Abstract、Sec. 1。
- 分类证据命题：被压缩的是 action planning 前的 visual reasoning，主路线为 reasoning efficiency；sketch token compression 为次级感知相关。
- 待核证据命题：96 tokens、单次 forward 与低延迟 deployment 需要分别回到 method 和 evaluation setting。

## Table / Metric Anchors
- **Abstract / Method**：abstract sketch、DC-AE、recurrent block diffusion。
- **Evaluation**：driving metrics、latency 与 resource setting 待核。

## Table / Metric Split
- visual token count、reasoning generation passes 与最终 action latency 需要分层。
- autonomous-driving metric 不与 manipulation benchmark 直接并表。

## 不可混写项
- 不把中间 visual CoT 的 diffusion refinement 写成 trajectory denoising-step reduction。
- 不把 compact sketch 自动等同于完整系统部署收益。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/reasoning-efficiency-routes.md|reasoning-efficiency-routes]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 本页保留 driving visual reasoning 与 manipulation action decoding 的边界。
