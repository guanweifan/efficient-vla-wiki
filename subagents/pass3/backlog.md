# Pass 3 Backlog

## 状态
1. 本文件记录正式 `Pass 3` 的任务储备与轮次重点，不是完成账本。
2. `Pass 3` 由 `chief-editor` 主导，多轮推进；不默认一轮做完全部 evidence mining。

## 任务分类
1. `paper-local`
   - 目标：把单篇页中的 bundled headline、混合口径和模糊 data pointer 收紧到可补证状态。
   - 典型对象：benchmark / metric / operating point 混写。
2. `single-paper evidence`
   - 目标：从单篇页抽出可复用证据页。
   - 典型对象：headline split、table split、figure / caption anchor、关键 wording。
3. `cross-paper reusable evidence`
   - 目标：沉淀共享 metric、共享 benchmark 口径或共享 wording 约束。
   - 约束：只写 source-grounded evidence 与“不可混写项”，不提前滑向 synthesis。

## 轮次重点
1. 第 1 轮：优先铺设 evidence 骨架，让高价值 `papers/*.md` 有稳定 evidence 落点。
2. 第 2 轮：优先深挖高价值表格、指标与 operating point。
3. 第 3 轮：优先深挖 figure / caption / wording。
4. 第 4 轮：收口，判断剩余缺口属于继续补证，还是转交 `Pass 3.5 / Pass 4`。

## 早期高优先级任务簇
1. runtime / compute / latency / frequency 口径拆分。
2. retention ratio / pruning ratio / token budget 与性能 headline 的拆分。
3. training cost / performance / benchmark layer headline 的拆分。
4. 高频论文的 table-centric claim 补证。
5. 高频论文的 figure / caption / wording 边界补证。

## 正式早期轮次建议
1. 每轮约 `4` 个 task。
2. 每轮最多 `1` 个 `cross-paper reusable evidence` task。
3. `chief-editor` 串行写正式 `wiki/`。
4. `sidecar` 默认关闭；只有在任务退化为纯锚点采集时才按需引入。
