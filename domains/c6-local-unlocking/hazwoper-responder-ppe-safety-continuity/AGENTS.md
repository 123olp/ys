# hazwoper-responder-ppe-safety-continuity 目录说明

`domains/c6-local-unlocking/hazwoper-responder-ppe-safety-continuity/` 是 Human Infra 的 HAZWOPER 响应者 PPE 与安全连续性域，负责把响应者保护建模为危险材料事故公共服务连续性基础设施。

## 目录结构

```text
hazwoper-responder-ppe-safety-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 HAZWOPER、PPE、呼吸防护、热压力、污染转移、疲劳和组织支持边界。
- 本域只整理公开培训制度、组织变量和风险边界。
- PPE 操作、呼吸器适配、现场等级判断、救援动作和职业合规建议不属于本域。

## 上下游关系

- 上游：`occupational-exposure-industrial-hygiene/`、`health-workforce-capacity/`、`chemical-safety-poison-control-toxicology/`。
- 下游：`hazmat-incident-command-emergency-response-continuity/`、`decontamination-exposure-triage-continuity/`、`healthcare-surge-triage-capacity-continuity/`。

## 维护规则

- 新增资料必须说明它支持响应者训练、PPE、呼吸防护、疲劳热压力、污染控制还是组织容量。
- 不得写入穿脱操作、进入危险区域、现场处置、规避监管或降低安全标准的信息。
