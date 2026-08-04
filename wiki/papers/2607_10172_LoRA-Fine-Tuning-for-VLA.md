# 2607_10172_LoRA-Fine-Tuning-for-VLA

## Source
- Raw: [[raw/2607_10172_LoRA-Fine-Tuning-for-VLA.pdf]]
- Extracts manifest: [[extracts/parses/2607_10172_LoRA-Fine-Tuning-for-VLA/manifest.json]]
- Primary text fallback: [[extracts/parses/2607_10172_LoRA-Fine-Tuning-for-VLA/pdftotext.txt]]

## Claim
- 页面定位：这是一篇 **LoRA Fine-Tuning for VLA** 相关的增量论文；当前 L1 记录工业 manipulation 中的 PEFT 配置研究。
- 核心机制：系统比较 LoRA rank、VLM/action-expert allocation、VLM freezing 与 vision-encoder adaptation，用于 flow-matching VLA 的参数和静态显存效率。来源：[[raw/2607_10172_LoRA-Fine-Tuning-for-VLA.pdf]]，Abstract、Sec. 1。
- 维护分类：主路线为 `4.1 Training Efficiency Techniques`。

## Methodology Index
- LoRA
- parameter-efficient fine-tuning
- module allocation
- industrial manipulation

## Data Pointer
- **Abstract / Sec. 1**：回读 rank sweep 与 adaptation questions。
- **Experimental design**：回读 FFT/LoRA、module allocation 与 vision encoder ablations。
- **Results**：后续拆分 static VRAM、activation memory、trainable parameters 与 real-robot task result。

## Evidence Links
- [[wiki/evidence/claims/2607_10172_LoRA-Fine-Tuning-for-VLA-headline-split.md|2607_10172_LoRA-Fine-Tuning-for-VLA-headline-split]]

## 待核点
- 论文明确排除 activation memory 的静态显存口径，不能写成完整 training peak memory。
- “无可检测性能损失”需绑定样本量与统计检验设置。
