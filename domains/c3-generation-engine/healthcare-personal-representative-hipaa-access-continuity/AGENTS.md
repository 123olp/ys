# healthcare-personal-representative-hipaa-access-continuity

本目录承载医疗个人代表、授权照护者和医疗信息访问连续性资料。它研究主体无法独自管理资料时，医疗信息如何在合法授权和隐私边界内跟随照护任务。

## 目录结构

```text
healthcare-personal-representative-hipaa-access-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明本域对象、Human Infra 价值、边界、上下游和初始资料线索。
- 后续资料应区分患者本人访问、personal representative、caregiver proxy access、机构披露和紧急例外。
- 本域不保存 PHI，不解释个案访问权，也不提供隐私投诉、表格填写或诉讼策略。

## 维护规则

- 引用资料优先来自 HHS OCR、ONC、CMS、医疗机构公开资料和隐私/互操作标准。
- 每条资料必须标注它支持的是访问权、隐私边界、代理角色还是机构义务。
- 不把“照护需要”写成越权访问或绕过同意的理由。
