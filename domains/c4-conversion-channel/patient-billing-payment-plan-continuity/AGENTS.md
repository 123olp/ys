# patient-billing-payment-plan-continuity

## 职责

本目录承载患者账单、statement、payment plan、billing inquiry、collections handoff 和账单可理解性资料。

## 边界

- 只研究账单流程、变量、公开制度和失败模式。
- 不提供账单谈判、付款计划、信用修复、催收应对、法律或个案财务建议。
- 不保存账单、EOB、信用、银行、收入、地址或催收资料。

## 结构

```text
patient-billing-payment-plan-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分 provider bill、payer EOB、self-pay estimate、collections 和 financial assistance。
- 涉及个体账单、催收或信用报告的内容必须转回官方渠道和专业人员。
