# 2608_00391_Actuation-Slack-Refresh

## Source
- Raw: [[raw/2608_00391_Actuation-Slack-Refresh.pdf]]
- Extracts manifest: [[extracts/parses/2608_00391_Actuation-Slack-Refresh/manifest.json]]
- Primary text fallback: [[extracts/parses/2608_00391_Actuation-Slack-Refresh/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **Actuation-Slack Refresh** 相关的增量论文；当前 L1 记录 closed-loop token-skipping gate reliability。
- 核心机制：在当前 action chunk 执行期间离开 critical path 运行 unconditional dense refresh，为下一轮 sparse serve 提供 clean gate 与 fresh KV base。来源：[[raw/2608_00391_Actuation-Slack-Refresh.pdf]]，Abstract、Sec. 1。
- 维护分类：主路线为 `4.2 Inference Efficiency Techniques`。

## Methodology Index
- actuation-slack refresh
- token skipping
- clean gate provenance
- off-critical-path dense refresh

## Data Pointer
- **Abstract / Sec. 1**：回读 self-harvested gate failure 与 clean-gate hypothesis。
- **Method / Controlled study**：回读 reuse/deletion 与 gate provenance factorial design。
- **Sec. 5.6 / 5.8**：回读 serve latency、total FLOPs、energy 与 limitations。

## Evidence Links
- [[wiki/evidence/claims/2608_00391_Actuation-Slack-Refresh-headline-split.md|2608_00391_Actuation-Slack-Refresh-headline-split]]

## 待核点
- 该方法降低 critical-path serve latency，但论文 limitation 报告总 computation 约为 dense FLOPs 的 1.6 倍且 energy 每 chunk 增加约 18%。
- reliability result 与 latency result 覆盖的 policy、benchmark 和 physical platform 不完全相同。
