# cardiac-arrest-cpr-defibrillation-continuity 目录说明

本目录维护心脏骤停、CPR、AED/除颤和复苏系统资料。它是主体从分钟级死亡边界返回的急性救援域。

## 目录结构

```text
cardiac-arrest-cpr-defibrillation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义心脏骤停救援链如何影响主体持续性、脑灌注和未来选择权。
- 本目录只维护研究框架、变量和证据边界，不保存个案急救记录、心电图、定位、视频或身份资料。
- 资料进入本域时必须保留来源、对象、系统层级、可逆时间窗、结局指标和禁止用途。

## 上下游关系

- 上游来自 AHA、CDC CARES、EMS 系统、复苏科学和公共 AED 资料。
- 下游服务 `emergency-medical-services-prehospital-care/`、`cerebrovascular-stroke-brain-perfusion-resilience/` 和急性死亡风险建模。
- 不替代官方急救培训、EMS、医生、医院、公共安全机构或个人医疗建议。

## 维护规则

- 不写 CPR/AED 操作教程或个案急救判断。
- 不把“公共知识整理”写成实时急救指令。
- 若新增系统绩效字段，必须同步更新索引和安全边界。
