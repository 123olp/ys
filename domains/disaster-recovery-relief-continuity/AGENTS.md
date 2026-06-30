# disaster-recovery-relief-continuity 目录说明

本目录承载灾后恢复、个人援助、临时安置、救济入口和恢复连续性如何进入 Human Infra 模型。

## 结构

```text
disaster-recovery-relief-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 是本域的边界、模型链路、非目标和来源入口。
- 本域只处理灾后恢复系统和非个体化变量，不处理个体资格、申请、贷款、保险、法律或住房选择。
- 后续资料必须标注地区、灾害类型、服务阶段和来源时效。

## 上下游关系

- 上游：`emergency-preparedness-response/`、`emergency-alerts-communications/`、`risk-engineering/`。
- 下游：`housing-built-environment-stability/`、`financial-inclusion-payment-systems/`、`social-protection-benefits-delivery/`。
- 相邻域：`insurance-risk-transfer/`、`community-resource-navigation/`、`legal-identity-civil-registration/`。

## 维护规则

- 不提供个体灾害申请、资格、贷款、保险、税务、法律或住房建议。
- 不承诺官方资源实时可用或救济结果。
- 若新增恢复流程或案例，必须保留官方来源和适用边界。
