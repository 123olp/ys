# healthcare-surge-triage-capacity-continuity 目录说明

`domains/c4-conversion-channel/healthcare-surge-triage-capacity-continuity/` 是 Human Infra 的医疗挤兑、分诊与容量连续性域，负责把暴发期间的医疗系统容量建模为主体恢复能力边界。

## 目录结构

```text
healthcare-surge-triage-capacity-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 surge capacity、床位、人力、分诊、危机标准、转运、延迟照护和伦理治理的对象、链路、非目标和来源信号。
- 本域只整理公开医疗准备和系统容量资料。
- 临床分诊、治疗优先级、床位/医院选择、转院建议、资源抢占和现场指挥不属于本域。

## 上下游关系

- 上游：`healthcare-access-continuity/`、`emergency-medical-services-prehospital-care/`、`medical-countermeasure-stockpile-distribution-continuity/` 和 `health-workforce-capacity/`。
- 下游：`patient-safety-organizational-learning/`、`medicine-access-treatment-continuity/`、`surgical-anesthesia-perioperative-safety/` 和 `care-transitions-discharge-continuity/`。

## 维护规则

- 新增资料必须说明它支持容量、分诊框架、医疗人力、转运、危机标准还是延迟照护评估。
- 不能输出个案医疗、分诊判定、治疗优先级、转院方案、资源抢占或设施安全弱点。
