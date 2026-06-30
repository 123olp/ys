# health-insurance-enrollment-renewal-continuity

## 职责

本目录承载健康保险参保、续保、特殊参保期、资格通知、保费支付、Medicaid/Marketplace 转换和覆盖连续性资料。

## 边界

- 只做制度、变量、证据和失败模式研究。
- 不提供保险选择、参保、补贴、税务、法律、移民或申诉建议。
- 不保存 SSN、保险账号、收入、家庭成员、保费支付或账户凭证资料。

## 结构

```text
health-insurance-enrollment-renewal-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分 Marketplace、Medicaid/CHIP、Medicare、雇主保险和商业个人保险场景。
- 涉及个体 eligibility、premium、appeal 或 coverage termination 的内容必须转回官方渠道和专业人员。
