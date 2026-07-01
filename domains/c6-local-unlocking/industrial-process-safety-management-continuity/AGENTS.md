# industrial-process-safety-management-continuity 目录说明

`domains/c6-local-unlocking/industrial-process-safety-management-continuity/` 是 Human Infra 的工业过程安全管理连续性域，负责把重大事故预防、维护、变更管理和组织学习建模为工人社区持续性基础设施。

## 目录结构

```text
industrial-process-safety-management-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 PSM、RMP、机械完整性、变更管理、事故学习和社区接口。
- 本域只整理公开制度、组织变量、事故预防框架和禁止用途。
- 工艺参数、设备操作、联锁绕过、企业合规、事故责任和监管规避不属于本域。

## 上下游关系

- 上游：`manufacturing-repair-capacity/`、`occupational-exposure-industrial-hygiene/`、`chemical-safety-poison-control-toxicology/`。
- 下游：`chemical-release-shelter-evacuation-continuity/`、`community-right-to-know-chemical-risk-disclosure-continuity/`、`risk-engineering/`。

## 维护规则

- 新增资料必须说明它支持预防、维护、变更、组织学习、工人安全还是社区风险边界。
- 不得写入危险工艺操作、事故制造、规避监管、法律结论或企业具体合规建议。
