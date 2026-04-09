# Pass 5 Stage 1 Doc Inventory

## 判定口径
1. `keep`：内容仍正确、清楚、非冗余，且对当前仓库的知识、控制或维护仍有直接价值。
2. `trim`：内容仍有价值，但存在历史噪声、过时段落、冗余块或描述不够规范，需要精炼。
3. `merge`：单独保留价值不足，应并入其他文档。
4. `delete`：属于运行态残留、过时过程文件或低保留价值噪声，不值得继续保留。

## Keep
1. `wiki/papers/*.md`
   - 理由：单篇知识层核心页面，仍是 `wiki` 原子层。
2. `wiki/evidence/claims/*.md`
   - 理由：单篇证据层核心页面，是 `papers -> evidence -> synthesis` 链路的中间层。
3. `wiki/evidence/metrics/*.md`
   - 理由：共享口径页，已被 `synthesis` 复用，保留价值高。
4. `wiki/evidence/wording/*.md`
   - 理由：共享措辞边界页，已被 `synthesis` 复用，保留价值高。
5. `wiki/synthesis/*.md`
   - 理由：主题建模层核心页面。
6. `subagents/pass1/README.md`
   - 理由：保留 `Pass 1` 的正式并行配置说明，仍有流程复盘价值。
7. `subagents/pass1/paper_l1_template.md`
   - 理由：`Pass 1` 单篇页模板，仍可作为后续维护参照。
8. `subagents/pass1/worker_prompt.md`
   - 理由：记录 `Pass 1` 的执行约束与口径。
9. `subagents/pass2/README.md`
   - 理由：保留 `Pass 2` 的正式 reverse calibration 工作模式。
10. `subagents/pass2/worker_prompt.md`
    - 理由：保留 `Pass 2` 的执行约束与收口边界。
11. `subagents/pass3/backlog.md`
    - 理由：记录 `Pass 3` 的覆盖优先、多轮 deepening 设计，仍有维护参考价值。
12. `subagents/pass3/task_template.md`
    - 理由：定义 evidence task 的最小工作单元，仍可复用。
13. `subagents/pass3/evidence_page_template.md`
    - 理由：evidence 页结构模板，仍有长期价值。
14. `subagents/pass3/sidecar_prompt.md`
    - 理由：只读取证 sidecar 的边界说明，仍可复用。
15. `subagents/pass4/README.md`
    - 理由：保留 `Pass 4` 的主题准入与阶段 gate 说明。
16. `subagents/pass4/backlog.md`
    - 理由：保留 `Pass 4` 主题集与阶段结果，仍有结构复盘价值。
17. `subagents/pass4/history_chain_template.md`
    - 理由：历史链模板，仍可复用。
18. `subagents/pass4/synthesis_page_template.md`
    - 理由：主题页模板，仍可复用。
19. `subagents/pass4/sidecar_prompt.md`
    - 理由：`Pass 4` 只读 sidecar 边界说明，仍可复用。
20. `subagents/pass5/README.md`
    - 理由：当前 `Pass 5` 的执行说明。
21. `subagents/pass5/backlog.md`
    - 理由：当前 `Pass 5` 的阶段记录与审计范围说明。
22. `subagents/pass5/audit_checklist.md`
    - 理由：`Pass 5` 的硬 gate 清单。
23. `subagents/pass5/sidecar_prompt.md`
    - 理由：`Pass 5` 只读核查模式边界说明。
24. `subagents/pass5/doc_inventory.md`
    - 理由：Stage 1 的正式审计产物。
25. `skills/wiki-ingest/SKILL.md`
    - 理由：冷启动后增量维护仍可能使用。
26. `skills/wiki-ingest/example.md`
    - 理由：给增量维护提供可执行示例，内容未过时。
27. `skills/wiki-lint/SKILL.md`
    - 理由：后续维护期仍需要健康检查技能说明。
28. `skills/wiki-lint/example.md`
    - 理由：给维护性 lint 提供示例，内容仍可复用。
29. `skills/wiki-reflect/SKILL.md`
    - 理由：虽不在当前阶段执行，但其定位与 `threads` 用户主导并不冲突，仍有后续维护价值。
30. `skills/wiki-reflect/example.md`
    - 理由：反映 thread-to-wiki 维护流程的示例，仍可保留。
31. `extracts/pass0_status.json`
    - 理由：本地 parse 参考层状态文件，保留本地诊断价值。
32. `extracts/pass0_index.jsonl`
    - 理由：本地 parse 索引文件，保留本地诊断价值。

## Trim
1. `wiki/index.md`
   - 问题类型：历史噪声过多、控制价值偏低、导航性不足。
   - 动作：改成当前状态、层级入口、主题结构和 `Pass 5` 审计范围的简明索引。
2. `wiki/log.md`
   - 问题类型：wave 级流水账过长、过时“下一步”过多、低价值重复块明显。
   - 动作：压缩为里程碑日志，只保留阶段完成节点与关键收口信息。
3. `wiki/status.json`
   - 问题类型：运行时历史细节过多、包含大量已无控制价值的数组和过程字段。
   - 动作：改成简明的阶段控制文件，只保留当前仍需维护的 gate、计数和摘要。
4. `WIKI_SCHEMA.md`
   - 问题类型：`Pass 5` 范围描述未覆盖 `subagents/pass5/` 与 `skills/*`，与当前实际审计范围不完全一致。
   - 动作：收紧 `Pass 5` 范围与阶段描述。
5. `subagents/pass3/README.md`
   - 问题类型：保留了过时的“当前阶段”表述。
   - 动作：改成归档性的“正式基线”说明。
6. `subagents/pass4/backlog.md`
   - 问题类型：残留过时的阶段推进提示。
   - 动作：删去已过时的过渡性语句。
7. `subagents/pass5/README.md`
   - 问题类型：范围描述不完整，未覆盖 `subagents/pass5/` 与 `skills/*`。
   - 动作：补齐范围。
8. `subagents/pass5/backlog.md`
   - 问题类型：范围描述不完整，且未记录 Stage 1 审计结果。
   - 动作：补齐范围并写入 Stage 1 结果。

## Merge
1. 当前无必须合并的文档。

## Delete
1. `subagents/pass2/queue.md`
   - 问题类型：运行态队列、阶段已完成、长期保留价值低。
   - 动作：删除。
