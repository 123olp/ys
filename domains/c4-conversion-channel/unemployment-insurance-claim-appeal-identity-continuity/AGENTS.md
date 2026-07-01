# unemployment-insurance-claim-appeal-identity-continuity 目录说明

本目录维护失业保险申领、身份核验、申诉和支付连续性域。它是 Human Infra 的失业收入冲击恢复执行层，不是 UI claim、appeal 或身份核验操作入口。

## 目录结构

```text
unemployment-insurance-claim-appeal-identity-continuity/
├── AGENTS.md
└── README.md
```

## 职责

- 记录 UI claims、continued certification、determinations、ID proofing、appeals、overpayment 和 payment delay。
- 区分工资记录底座、申领执行、法律争议、欺诈控制和个案福利策略。
- 维护 DOL/ETA/OUI 与州级 UI 系统资料的边界。

## 维护规则

- 新增资料必须说明州级差异、联邦来源、执行链路和禁止用途。
- 不保存 SSN、州 UI account、工资记录、雇主信息、身份证件、银行账户或门户凭证。
- 不输出 UI 资格判断、weekly certification、appeal、overpayment 或身份核验个案建议。
