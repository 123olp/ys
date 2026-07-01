# hazmat-incident-command-emergency-response-continuity 目录说明

`domains/c5-ecological-substrate/hazmat-incident-command-emergency-response-continuity/` 是 Human Infra 的危险材料事故指挥与应急响应连续性域，负责把多机构响应建模为事故期间主体服务接续基础设施。

## 目录结构

```text
hazmat-incident-command-emergency-response-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 NIMS/ICS、HazMat 指挥、跨机构协作、公共信息和恢复交接的对象与边界。
- 本域只整理公开制度、响应接口、组织变量和禁止用途。
- 现场指挥、战术动作、隔离距离、消防操作、去污步骤和设施攻防不属于本域。

## 上下游关系

- 上游：`emergency-preparedness-response/`、`emergency-alerts-communications/`、`chemical-safety-poison-control-toxicology/`。
- 下游：`chemical-release-shelter-evacuation-continuity/`、`decontamination-exposure-triage-continuity/`、`healthcare-surge-triage-capacity-continuity/`。

## 维护规则

- 新增资料必须说明它支持指挥接口、机构协作、公众信息、医疗转运、环境监测还是恢复交接。
- 不得写入现场战术、危险材料操作、规避响应、攻击模拟或实时应急建议。
