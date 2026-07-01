# unemployment-insurance-wage-record-continuity

本目录承载失业保险工资记录、资格判定和给付连续性资料。它研究劳动收入中断时，过去工资和雇佣记录如何转化为短期稳定和再就业窗口。

## 目录结构

```text
unemployment-insurance-wage-record-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明本域对象、Human Infra 价值、边界、上下游和初始资料线索。
- 后续资料应区分工资记录、covered employment、base period、claims、eligibility、appeals、fraud controls、overpayments 和再就业服务。
- 本域不保存个人失业、工资、雇佣或身份资料，不提供 UI 申请、资格、申诉、税务、法律、移民或个人福利建议。

## 维护规则

- 引用资料优先来自 DOL ETA、州级 UI 官方资料、官方审计报告和失业保险研究。
- 必须保留州差异、个人建议边界、身份防护、申诉权、系统错误、overpayment 和反欺诈边界。
- 不把 UI 记录连续性写成保证给付，也不输出任何虚假申领或规避验证路径。
