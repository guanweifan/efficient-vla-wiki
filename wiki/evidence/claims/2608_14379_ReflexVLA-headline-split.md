# 2608_14379_ReflexVLA-headline-split

## 用途
- 服务于 [[wiki/papers/2608_14379_ReflexVLA.md|ReflexVLA]]，拆分 predictive model components、runtime optimization、benchmark frequency 与 real-world evidence。

## Evidence
- 方法证据命题：ReflexVLA 用 frozen DINOv3 future targets、vision-backbone causal temporal fusion、batched multi-frame encoding 与 full-pipeline CUDA Graph。来源：[[raw/2608_14379_ReflexVLA.pdf]]，Sec. IV、Fig. 3。
- ablation 证据命题：middle-feature MHA fusion 为 71.7% / 125.107 ms；加入 batched encoding + CUDA Graph 后为 73.8% / 64.991 ms。来源：[[raw/2608_14379_ReflexVLA.pdf]]，Table III。
- deployment 证据命题：ReflexBench 主比较使用单张 RTX 5880 Ada、async、chunk=8、action horizon=2；real-world Table IV 的三项 task metrics 口径不同。来源：[[raw/2608_14379_ReflexVLA.pdf]]，Sec. V-A、Table IV。

## Table / Metric Anchors
- **Fig. 4-5**：frequency、sync/async、chunk/horizon sweep。
- **Table I-III**：dynamic benchmark、static benchmark 与 progressive ablation。

## Table / Metric Split
- injected benchmark frequency、single-inference latency、action horizon 与 task success 分开。
- future prediction、temporal fusion 与 combined runtime optimization 的收益不互相替代。

## 不可混写项
- 不把 30 Hz benchmark setting 写成 ReflexVLA 的实测 model frequency。
- 不把 combined batch/CUDA Graph gain归因于单一系统组件。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- latent prediction / temporal fusion 只在 fine-tuning 阶段加入；未覆盖 large-scale pretraining 与 RTC 等更高级 execution mechanism。
