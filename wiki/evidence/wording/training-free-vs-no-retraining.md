# training-free-vs-no-retraining

## 用途
- 当前页收敛 `training-free`、`no retraining`、`decoding-process-only` 这组最容易被混写的加速措辞。
- 当前页只记录 source-grounded wording 边界，不承担主题级 synthesis。

## Evidence
- [[wiki/papers/2503_02310_PD-VLA.md|2503_02310_PD-VLA]]：`training-free acceleration without redesign and modification of models` 的更精确含义是 **只在 inference-time 改写 decoding process**，不重训 backbone，也不重写基础 VLA 架构。来源：[[raw/2503_02310_PD-VLA.pdf]]，第 2 页 Introduction。
- [[wiki/papers/2509_05614_SpecPrune-VLA.md|2509_05614_SpecPrune-VLA]]：`training-free` 对应 **two-level pruning + action-aware controller at inference time**；它不需要重新训练 backbone，但仍包含显式 heuristic controller。来源：[[raw/2509_05614_SpecPrune-VLA.pdf]]，第 1-2 页 Abstract / Introduction。
- [[wiki/papers/2511_16449_VLA-Pruner.md|2511_16449_VLA-Pruner]]：`training-free` 和 `plug-and-play` 的直接证据来自方法介绍与主实验，但已验证范围主要是 `OpenVLA`、`OpenVLA-OFT` 和 `π0`。来源：[[raw/2511_16449_VLA-Pruner.pdf]]，第 2-3 页 Introduction；第 7 页 Table 1；第 16 页 Table 4。
- [[wiki/papers/2511_20720_DeeAD.md|2511_20720_DeeAD]]：`training-free` 指 **不重训 ORION backbone**，而是在 inference time 根据 action-space deviation 与 lightweight planning prior 决定 early exit。来源：[[raw/2511_20720_DeeAD.pdf]]，第 1-2 页 Abstract / Introduction。

## 不可混写项
- `training-free` 不等于 `model-agnostic`；一个方法可以不重训 backbone，但仍然只在少数架构上验证。
- `training-free` 也不等于“没有额外控制逻辑 / 阈值 / heuristic”；很多方法仍然依赖 inference-time controller、threshold 或 routing rule。
- 若论文强调 `decoding-process-only` 或 `inference-time`，应保留这层精确含义，不要直接压扁成宽泛的 “无需训练”。

## 影响页面
- [[wiki/papers/2503_02310_PD-VLA.md|2503_02310_PD-VLA]]
- [[wiki/papers/2509_05614_SpecPrune-VLA.md|2509_05614_SpecPrune-VLA]]
- [[wiki/papers/2511_16449_VLA-Pruner.md|2511_16449_VLA-Pruner]]
- [[wiki/papers/2511_20720_DeeAD.md|2511_20720_DeeAD]]

## 边界
- 当前页只记录 `training-free / no retraining` 的 wording boundary。
- 若如需比较这些方法在效率路线上各自扮演什么角色，应留到 `Pass 3.5 / Pass 4`。
