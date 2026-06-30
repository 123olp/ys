# labor-rights-workplace-protection 目录说明

`domains/labor-rights-workplace-protection/` 是 Human Infra 的劳动权利与工作场所保护域，负责把工资工时、安全权利、反歧视、反报复、申诉和劳动组织治理建模为工作连续性的制度条件。

## 目录结构

```text
labor-rights-workplace-protection/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义劳动标准、工资工时、安全权利、反歧视、申诉入口和组织治理的对象、链路、非目标和来源信号。
- 本域只做公开资料整理、变量建模、证据边界和权利执行断点分析。
- 个案法律意见、工资计算、雇佣分类、投诉策略、劳动组织策略、谈判策略和胜诉承诺不属于本域。

## 上下游关系

- 上游：`governance-rights/`、`language-access-plain-communication/` 和 `access-to-justice-legal-aid/`。
- 下游：`occupational-work-design/`、`financial-resilience-access/`、`mental-health-affective-stability/` 和 `time-allocation-effective-time/`。

## 维护规则

- 新增资料必须说明它支持的是劳动标准、工资工时、安全权利、反歧视、反报复、申诉执行还是组织治理变量。
- 不能把劳动资料写成个案法律判断、劳动争议策略或规避程序建议。
