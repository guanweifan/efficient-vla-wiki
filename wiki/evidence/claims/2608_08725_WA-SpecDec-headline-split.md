# 2608_08725_WA-SpecDec-headline-split

## 用途
- 服务于 [[wiki/papers/2608_08725_WA-SpecDec.md|WA-SpecDec]]，拆分 world-aware target、draft acceptance、matched-success speedup 与 near-contact failure。

## Evidence
- 方法证据命题：WAB 在不增加 token 数的情况下把 predictive physical-scene bias 注入 visual embeddings；target 和 draft 共享 prefill state，acceptance rule 不变。来源：[[raw/2608_08725_WA-SpecDec.pdf]]，Sec. 3、Algorithm 1。
- operating-point 证据命题：Table 1 在相同 relaxed verifier 下分别报告四个 LIBERO suite 的 success、wall-clock speedup 与 NCF；speedup 已包含 WAB、draft、verification 与 cache updates。来源：[[raw/2608_08725_WA-SpecDec.pdf]]，Table 1、Sec. 4.1。
- training 证据命题：next-frame latent head 只用于训练，部署只用当前 observation；target 训练后还需 distill draft。来源：[[raw/2608_08725_WA-SpecDec.pdf]]，Algorithm 1、Appendix A。

## Table / Metric Anchors
- **Table 1-2**：verifier / target-specific operating points。
- **Table 6**：WAB 与 auxiliary video loss ablation。

## Table / Metric Split
- accepted length、target verification rounds、wall-clock speedup、task success 与 NCF 五项分开。
- world-aware target reliability 与 speculative acceleration 不合并为单一模块收益。

## 不可混写项
- 不把 matched-success 1.5x 写成所有 verifier / suite 的固定 speedup。
- 不把 inference-time no-future-frame 写成 training-free。

## 影响页面
- [[wiki/synthesis/efficient-vla-research-map.md|efficient-vla-research-map]]
- [[wiki/synthesis/inference-efficiency-routes.md|inference-efficiency-routes]]
- [[wiki/synthesis/deployment-oriented-efficiency.md|deployment-oriented-efficiency]]
- [[wiki/synthesis/efficiency-definition-evolution.md|efficiency-definition-evolution]]

## 边界
- 证据来自 LIBERO 与 SIMPLER simulation；NCF 是失败 episode 中的 near-contact failure 比例，不是通用安全率。
