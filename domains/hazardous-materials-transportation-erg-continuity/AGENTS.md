# hazardous-materials-transportation-erg-continuity 目录说明

`domains/hazardous-materials-transportation-erg-continuity/` 是 Human Infra 的危险材料运输与 ERG 连续性域，负责把移动危险品事故建模为交通、供应链、社区暴露和应急沟通接口。

## 目录结构

```text
hazardous-materials-transportation-erg-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义危险品运输、ERG、标识、交通中断、物流断点和社区沟通。
- 本域只整理公开运输安全资料、变量模型和禁止用途。
- 包装装卸、路线建议、隔离距离、危险品操作、企业合规和规避检查不属于本域。

## 上下游关系

- 上游：`transportation-access-mobility/`、`freight-logistics-port-cold-chain-continuity/`、`chemical-safety-poison-control-toxicology/`。
- 下游：`chemical-release-shelter-evacuation-continuity/`、`hazmat-incident-command-emergency-response-continuity/`、`supply-chain-continuity/`。

## 维护规则

- 新增资料必须说明它支持运输模式、识别接口、交通中断、供应链影响、社区沟通还是恢复边界。
- 不得写入危险品运输操作、包装路线、规避检查、实时事故行动或违法用途。
