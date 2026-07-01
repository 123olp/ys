# chronic-viral-hepatitis-screening-liver-protection-continuity 目录说明

本目录维护慢性乙肝、丙肝筛查、确认、治疗连接、肝脏保护和肝癌风险监测资料。它是感染控制、肝脏清除和癌症预防之间的执行域。

## 目录结构

```text
chronic-viral-hepatitis-screening-liver-protection-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义病毒性肝炎筛查和肝脏风险控制如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案化验、病毒载量、影像、药物、暴露或身份资料。
- 资料进入本域时必须保留感染类型、筛查对象、确认路径、治疗连接、监测边界和禁止用途。

## 上下游关系

- 上游来自 CDC、USPSTF、肝病和公共卫生资料。
- 下游服务 `renal-hepatic-clearance/`、`chronic-infectious-disease-care-continuity/` 和肝癌风险建模。
- 不替代肝病专科、感染科、公共卫生、疫苗服务、药师或个体医疗建议。

## 维护规则

- 不写个人检测判读、抗病毒药物、剂量、疫苗建议、肝癌监测安排、家庭传播处理或治疗建议。
- 不收集或推断敏感感染、性行为、注射暴露、身份或保险资料。
- 新增资料必须区分筛查、确认、分期、治疗连接、随访、监测和预防接口。
