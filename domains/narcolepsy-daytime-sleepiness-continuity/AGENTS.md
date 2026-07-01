# narcolepsy-daytime-sleepiness-continuity 目录说明

本目录维护发作性睡病、白天过度嗜睡、猝倒和清醒窗口可靠性资料。它关注睡眠-觉醒边界失稳如何影响学习、驾驶、工作、关系和有效时间。

## 目录结构

```text
narcolepsy-daytime-sleepiness-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义发作性睡病如何通过日间嗜睡、猝倒、诊断延迟和支持可及性影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案睡眠报告、用药、驾驶、学校、工作或医疗资料。
- 资料进入本域时必须保留对象、诊断语境、支持接口、安全暴露和禁止用途。

## 上下游关系

- 上游来自 NHLBI、MedlinePlus 和睡眠医学资料。
- 下游服务 `sleep-circadian-recovery/`、`fatigue-risk-alertness-continuity/`、`attention-executive-control/` 和交通/工作安全模型。
- 不替代睡眠医学、神经科、药学、学校/雇主、驾驶安全、保险、残障服务或个体医疗建议。

## 维护规则

- 不写个人诊断、睡眠检查解释、药物、剂量、驾驶许可、便利申请、保险或残障建议。
- 不把嗜睡症状资料写成筛查或治疗建议。
- 新增资料必须区分日间嗜睡、猝倒、睡眠发作、诊断、支持和安全暴露阶段。
