# insurance-eligibility-benefits-verification-continuity

## 职责

本目录承载保险资格、benefits verification、coverage active 状态、费用分担、网络状态和覆盖限制资料。

## 边界

- 只研究权益核验机制、变量和失败模式。
- 不提供个人保险权益解释、费用预测、provider 选择、理赔、申诉或法律建议。
- 不保存保险卡、member ID、诊断、claim、账单或个人财务资料。

## 结构

```text
insurance-eligibility-benefits-verification-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分 coverage status、benefit design、network status 和 patient responsibility。
- 涉及个体权益核验、账单或 claim 的内容必须回到 payer、provider、官方渠道和专业人员。
