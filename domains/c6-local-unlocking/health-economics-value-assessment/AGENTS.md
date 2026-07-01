# health-economics-value-assessment 目录说明

`domains/c6-local-unlocking/health-economics-value-assessment/` 是 Human Infra 的健康经济与价值评估域，负责把疾病负担、成本效果、HTA、预算影响和公共价值边界建模为稀缺资源转化问题。

## 目录结构

```text
health-economics-value-assessment/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义疾病负担、成本效果、卫生技术评估、资源分配和公共价值的对象、链路、非目标和来源信号。
- 本域只做系统级价值语言、证据边界、变量模型和资源配置问题整理。
- 投资、报销、保险、个体治疗选择、福利申请和把人还原为经济指标不属于本域。

## 上下游关系

- 上游：`functioning-quality-of-life-outcomes/`、`measurement-feedback/` 和 `healthcare-access-continuity/`。
- 下游：`insurance-risk-transfer/`、`social-protection-benefits-delivery/`、`medicine-access-treatment-continuity/` 和 `governance-rights/`。

## 维护规则

- 新增资料必须说明它支持的是疾病负担、成本效果、预算影响、HTA、价值框架、支付激励还是公平边界。
- 不能把价值评估资料写成个体治疗、覆盖、投资或政策执行建议。
