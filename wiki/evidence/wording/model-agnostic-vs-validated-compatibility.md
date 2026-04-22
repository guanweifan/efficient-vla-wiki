# model-agnostic-vs-validated-compatibility

## 用途
- 当前页收敛 `model-agnostic`、`backbone-agnostic`、`universal`、`without modifying downstream control logic` 这组最容易被夸大的兼容性措辞。
- 当前页只记录 source-grounded wording 边界，不承担主题级 synthesis。

## Evidence
- [[wiki/papers/2509_21354_KV-Efficient-VLA.md|2509_21354_KV-Efficient-VLA]]：`model-agnostic memory compression` 的直接 wording 来自摘要，同时说明方法能集成到近期 VLA stack 且**不修改 downstream control logic**；当前实验主要覆盖 `OpenVLA / CogACT / HybridVLA`。来源：[[raw/2509_21354_KV-Efficient-VLA.pdf]]，第 1 页 Abstract；第 7 页 Table 1。
- [[wiki/papers/2506_13725_CEED-VLA.md|2506_13725_CEED-VLA]]：`universal acceleration method` 的直接 wording 来自 contributions，但当前直接实验层主要是 `OpenVLA`、`LLaVA-VLA`、simulation 和 real robotic arm deployment。来源：[[raw/2506_13725_CEED-VLA.pdf]]，第 2-3 页 Contributions；实验章节。
- [[wiki/papers/2602_15397_ActionCodec.md|2602_15397_ActionCodec]]：`ActionCodec is backbone-agnostic` 的直接证据来自 `VLM Compatibility` 段，后面明确列出了 `SmolVLM2-2.2B`、`Qwen2.5VL-3B`、`InternVL3.5-2B` 三种 backbone。来源：[[raw/2602_15397_ActionCodec.pdf]]，第 8 页 `VLM Compatibility` 与 Table 4。
- [[wiki/papers/2603_05147_ActThinkAbstain.md|2603_05147_ActThinkAbstain]]：论文明确写 `although our framework is model-agnostic, our experiments are limited to SmolVLA`，并把 `π0 / OpenVLA` 列为未来扩展对象；这是最直接的 compatiblity caveat。来源：[[raw/2603_05147_ActThinkAbstain.pdf]]，第 7-8 页 Discussion / Conclusion。

## 不可混写项
- `model-agnostic` / `backbone-agnostic` / `universal` 不能自动理解成“所有 VLA 都已验证”；必须保留已验证 backbone 范围。
- `可无缝集成` 与 `已在多种真实系统充分验证` 不是一回事；前者是接口层兼容性，后者是经验外推范围。
- 当论文自己同时写了强兼容性词和实验范围 caveat 时，应优先保留 caveat。

## 影响页面
- [[wiki/papers/2509_21354_KV-Efficient-VLA.md|2509_21354_KV-Efficient-VLA]]
- [[wiki/papers/2506_13725_CEED-VLA.md|2506_13725_CEED-VLA]]
- [[wiki/papers/2602_15397_ActionCodec.md|2602_15397_ActionCodec]]
- [[wiki/papers/2603_05147_ActThinkAbstain.md|2603_05147_ActThinkAbstain]]

## 边界
- 当前页只记录兼容性相关 wording boundary。
- 若如需比较这些方法在跨 backbone 部署中的真正泛化能力，应留到主题建模阶段。
