# cardiac-arrhythmia-syncope-decompensation-continuity 目录说明

本目录维护心律失常、晕厥、传导异常和节律稳定资料。它是主体从正常行动突然进入脑灌注不足、跌倒、卒中或骤停风险的研究域。

## 目录结构

```text
cardiac-arrhythmia-syncope-decompensation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义心律和晕厥如何改变突发失能、跌倒、卒中、心衰、骤停和未来选择权。
- 本目录只维护系统级变量、来源和边界，不保存个案心电图、设备、症状、用药或位置数据。
- 资料进入本域时必须区分监测、风险识别、转诊、设备路径、栓塞风险和骤停前状态。

## 上下游关系

- 上游来自 AHA/ACC/HRS、NHLBI 和心律失常/晕厥 guideline materials。
- 下游服务 `cardiovascular-resilience/`、`cerebrovascular-stroke-brain-perfusion-resilience/` 和 `cardiac-arrest-cpr-defibrillation-continuity/`。
- 不替代医生、急诊、心内科、电生理、神经科或个体医疗建议。

## 维护规则

- 不写心电图判读、抗凝、用药、起搏器、ICD、消融、驾驶、运动或晕厥处理建议。
- 不把系统级节律连续性研究写成个人风险计算或治疗工具。
- 新增变量必须区分节律、传导、晕厥、栓塞、跌倒和骤停上游风险。
