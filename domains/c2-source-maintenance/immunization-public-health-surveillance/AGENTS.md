# immunization-public-health-surveillance 目录说明

`domains/c2-source-maintenance/immunization-public-health-surveillance/` 是 Human Infra 的免疫与公共卫生监测域，负责把疫苗、传染病监测、感染防控、AMR、One Health 和废水监测建模为群体风险屏障。

## 目录结构

```text
immunization-public-health-surveillance/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义免疫计划、传染病监测、公共卫生应急、感染防控和废水监测的对象、链路、非目标和来源信号。
- 本域只做公开公共卫生资料、变量模型、系统边界和禁止用途整理。
- 疫苗个体建议、诊断治疗、疫情预测保证、公共卫生规避、病原体操作和传播策略不属于本域。

## 上下游关系

- 上游：`immune-maintenance/`、`antimicrobial-resilience/` 和 `planetary-health-environment/`。
- 下游：`healthcare-access-continuity/`、`emergency-preparedness-response/`、`risk-engineering/` 和 `medicine-access-treatment-continuity/`。

## 维护规则

- 新增资料必须说明它支持的是免疫计划、病例监测、实验室网络、IHR、IPC、HAI、AMR、One Health、废水监测还是风险沟通。
- 不能把公共卫生资料写成个体医疗建议、规避策略或疫情确定性预测。
