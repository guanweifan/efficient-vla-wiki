# Pass 3 Backlog

## 状态
1. 本文件记录正式 `Pass 3` 的任务储备与轮次重点，不是完成账本。
2. `Pass 3` 由 `chief-editor` 主导，多轮推进；不默认一轮做完全部 evidence mining。
3. `Pass 3` 既要保证全库覆盖，也要允许重点深挖；两者必须同时被调度。

## 覆盖目标
1. `P3-Minimum`
   - 每篇论文至少完成一次真正的 evidence deepening。
   - “真正的 evidence deepening” 不等于只增加一个页码指针；至少要把一个 headline、表格、图注、wording 或 operating point 拆到更细层级。
2. `P3-Core`
   - 高频被比较论文、共享 metric 相关论文、后续建模关键论文，需要完成更高粒度的 table / metric / setting / figure / wording 深挖。
3. `P3-Shared`
   - 高优先级共享 metric / benchmark / wording 口径应沉淀为可复用 evidence 页面。

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

## 两类调度主线
1. `coverage track`
   - 默认优先队列。
   - 每轮优先选择那些尚未完成实质 evidence deepening 的论文。
2. `priority track`
   - 选择高频被引用论文、共享 metric、共享 benchmark、关键图表和关键 wording。
   - 只能与 `coverage track` 并行存在，不能替代它。

## 轮次重点
1. 第 1 轮：以 `coverage track` 为主铺设全库 evidence 骨架，并把 `papers/*.md` 推进到稳定的 single-paper evidence 落点；若页面已经具备清楚的 headline split 与不可混写项，可在同一轮直接达到 `P3-Minimum`。
2. 第 2 轮：继续沿 `coverage track` 查漏补缺，同时深挖高价值表格、指标与 operating point。
3. 第 3 轮：继续推进 `P3-Minimum`，并把重点转向 figure / caption / wording。
4. 第 4 轮：收口，判断剩余缺口属于继续补证，还是转交新的 `Pass 4` 历史整合与主题建模阶段。

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
5. 推荐配比：
   - `3` 个 `coverage track` task
   - `1` 个 `priority track` task
6. 如果当轮包含 `cross-paper reusable evidence`，它优先占用 `priority track` 名额。
