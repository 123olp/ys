# chemical-release-shelter-evacuation-continuity 目录说明

`domains/chemical-release-shelter-evacuation-continuity/` 是 Human Infra 的化学释放就地避险与撤离连续性域，负责把危险信号、保护行动、转移和恢复入口建模为事故期间主体持续性的执行基础设施。

## 目录结构

```text
chemical-release-shelter-evacuation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义化学释放避险、撤离、警报理解、交通转移和恢复入口的对象、链路、非目标和来源信号。
- 本域只整理公开应急资料、变量模型、风险边界和禁止用途。
- 现场处置、路线建议、去污步骤、防护操作、中毒处理和事故指挥不属于本域。

## 上下游关系

- 上游：`chemical-safety-poison-control-toxicology/`、`emergency-alerts-communications/`、`weather-climate-observation-forecasting/`。
- 下游：`disaster-recovery-relief-continuity/`、`transportation-access-mobility/`、`housing-built-environment-stability/`、`healthcare-access-continuity/`。

## 维护规则

- 新增资料必须说明它支持警报、避险、撤离、转介、恢复还是特殊人群连续性。
- 不得写入可执行事故处置、化学品操作、规避监管、恐慌传播或个体医疗建议。
