# claims-adjudication-eob-denial-continuity

## 职责

本目录承载医疗 claim adjudication、EOB、denial reason、coordination of benefits、resubmission 和 appeal window 连续性资料。

## 边界

- 只研究理赔流程、变量、公开标准和失败模式。
- 不提供 EOB 解读、编码、理赔申诉、账单争议、法律或欺诈规避建议。
- 不保存 claim、EOB、账单、诊断、CPT/ICD、payer decision 或个人账户资料。

## 结构

```text
claims-adjudication-eob-denial-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分 claim status、payer adjudication、EOB communication 和 patient billing。
- 涉及个案拒付、申诉期限或编码的内容必须转回 payer、provider、官方渠道和专业人员。
