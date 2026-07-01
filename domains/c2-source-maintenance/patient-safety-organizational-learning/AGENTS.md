# patient-safety-organizational-learning 目录说明

`domains/c2-source-maintenance/patient-safety-organizational-learning/` 是 Human Infra 的患者安全与组织学习域，负责把医疗照护系统中的错误报告、团队沟通、根因分析和流程改进建模为可避免伤害降低机制。

## 目录结构

```text
patient-safety-organizational-learning/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义患者安全、组织学习、事件报告、团队沟通、CUSP、TeamSTEPPS、RCA2 和安全文化的对象、链路、非目标和来源信号。
- 本域只做公开患者安全资料、变量模型、事件学习边界和禁止用途整理。
- 医疗事故法律意见、索赔策略、个案责任判断、机构排名、临床处置和惩罚性监控不属于本域。

## 上下游关系

- 上游：`risk-engineering/`、`healthcare-access-continuity/` 和 `occupational-work-design/`。
- 下游：`medicine-access-treatment-continuity/`、`patient-data-interoperability/`、`measurement-feedback/` 和 `functioning-quality-of-life-outcomes/`。

## 维护规则

- 新增资料必须说明它支持的是患者安全、事件报告、团队沟通、根因分析、CUSP、TeamSTEPPS、HRO 还是安全文化变量。
- 不能把患者安全资料写成法律责任判断、机构背书、惩罚员工、压制报告或临床操作建议。
