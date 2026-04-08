# Pass 3 准备说明

## 目标
1. `Pass 3 | Evidence Mining` 不再按整篇论文平均深挖，而是按 `evidence task` 推进。
2. 这一轮的核心不是“写更多摘要”，而是把高价值 claim、表格、图和关键 wording 钉到可复用证据上。
3. `wiki/evidence/` 只有在证据具有复用价值时才增长。
4. `Pass 3` 不是默认一轮完成，而是由 `chief-editor` 主导、可持续多轮推进的 evidence mining 阶段。
5. `Pass 3` 既要保证全库覆盖，也要允许重点深挖；不能只围绕少数核心论文反复打磨。

## 默认工作模式
1. `chief-editor` 串行写入正式 `wiki/`。
2. `sidecar` 如使用，只做只读取证，不直接写正式页面。
3. `Pass 3` 的正式推进顺序是：
   - `paper-local hardening`
   - `single-paper evidence extraction`
   - `cross-paper reusable evidence`
4. 正式推进不再额外做独立 pilot；改为正式轮次推进，并在每轮结束后由 `chief-editor` 复盘。

## 两条主线
1. `coverage track`
   - 目标：保证整库每篇论文都至少完成一次真正的 evidence deepening。
   - 最低要求：每篇论文至少有一个被打透的 evidence unit，而不是只有 page-level pointer。
2. `priority track`
   - 目标：优先深挖高频被引用论文、共享 metric / benchmark 口径、关键表格、关键图和关键 wording。
   - 约束：不能吞没 `coverage track`，否则 `Pass 3` 会退化成只服务少数论文的局部精修。

## 三类任务
1. `paper-local`
   - 只补强单篇 `papers/*.md`
   - 不新建 `wiki/evidence/*`
2. `single-paper evidence`
   - 从单篇页抽出可复用证据页
   - 典型对象：headline split、table operating point split、figure/caption anchor
3. `cross-paper reusable evidence`
   - 只写共享证据与“不可混写项”
   - 不做主题级 synthesis

## 轮次建议
1. 第 1 轮：以 `coverage track` 为主铺设全库 evidence 骨架，并把 `papers/*.md` 推进到稳定的 single-paper evidence 落点；若页面已经具备清楚的 headline split 与不可混写项，可在同一轮直接达到 `P3-Minimum`。
2. 第 2 轮：继续沿 `coverage track` 查漏补缺，同时在 `priority track` 上推进高价值表格、指标与 operating point。
3. 第 3 轮：在继续覆盖的同时，深挖 figure / caption / wording。
4. 第 4 轮：收口，判断哪些缺口仍属于 `Pass 3`，哪些应转交新的 `Pass 4` 历史整合与主题建模阶段。

## 当前阶段
1. 当前已进入 `Pass 3` 正式展开前的就绪态。
2. 正式早期轮次默认采用：
   - `chief-editor` 单人串行写入
   - `sidecar` 默认关闭
   - 每轮 `4` 个 task 左右
   - 每轮最多 `1` 个 `cross-paper reusable evidence` task
   - 推荐配比：`3` 个 `coverage track` task + `1` 个 `priority track` task
