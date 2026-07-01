# idiopathic-hypersomnia-excessive-sleepiness-continuity 目录说明

本目录维护特发性嗜睡、白天过度嗜睡、睡眠惯性和清醒启动困难资料。它关注“睡了仍无法清醒”如何压缩有效行动窗口。

## 目录结构

```text
idiopathic-hypersomnia-excessive-sleepiness-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义特发性嗜睡如何通过日间嗜睡、醒后困难、诊断不确定性和污名影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案睡眠、用药、驾驶、学校、工作或医疗资料。
- 资料进入本域时必须保留对象、排除诊断语境、功能损耗、支持接口和禁止用途。

## 上下游关系

- 上游来自 MedlinePlus 和睡眠医学资料。
- 下游服务 `sleep-circadian-recovery/`、`narcolepsy-daytime-sleepiness-continuity/` 和注意力/任务启动模型。
- 不替代睡眠医学、神经科、精神科、药学、驾驶安全、学校/雇主、保险、残障服务或个体医疗建议。

## 维护规则

- 不写个人诊断、睡眠检查解释、药物、剂量、作息、驾驶许可、便利申请或残障建议。
- 不把嗜睡体验写成治疗流程或自我诊断。
- 新增资料必须区分持续嗜睡、醒后困难、诊断不确定性、支持和安全暴露。
