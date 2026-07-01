# asthma-copd-maintenance-control-continuity 目录说明

本目录维护哮喘、COPD、长期气道控制、吸入药可及、触发因素、肺康复和急性加重预防资料。它关注慢性气道疾病如何持续压缩行动能力。

## 目录结构

```text
asthma-copd-maintenance-control-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义哮喘/COPD 长期控制如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案肺功能、用药、氧饱和度、急诊、吸烟、职业暴露或设备资料。
- 资料进入本域时必须保留疾病类型、控制状态、药物可及、触发因素、急性加重边界和禁止用途。

## 上下游关系

- 上游来自 NHLBI、CDC、呼吸医学、环境健康和康复资料。
- 下游服务 `respiratory-oxygenation/`、`asthma-copd-exacerbation-airway-continuity/` 和空气质量暴露模型。
- 不替代呼吸科、急诊、药学、氧疗、康复、职业医学、保险或个体医疗建议。

## 维护规则

- 不写个人诊断、肺功能判读、吸入药、剂量、氧疗、急性发作处理、康复动作或设备建议。
- 不把长期控制证据写成个人行动计划或药物调整流程。
- 新增资料必须区分哮喘、COPD、控制状态、触发暴露、急性加重和活动结果。
