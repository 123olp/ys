# indoor-ventilation-filtration-outbreak-control-continuity 目录说明

`domains/indoor-ventilation-filtration-outbreak-control-continuity/` 是 Human Infra 的室内通风过滤与暴发控制连续性域，负责把建筑空气运行建模为传染病传播风险控制基础设施。

## 目录结构

```text
indoor-ventilation-filtration-outbreak-control-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义通风、过滤、空气净化、CO2 代理指标、建筑运营和空间开放风险的对象、链路、非目标和来源信号。
- 本域只整理公开室内空气控制资料、变量模型和治理边界。
- HVAC 设计施工、设备采购、场所认证、实时开放判断和个体风险计算不属于本域。

## 上下游关系

- 上游：`air-quality-ventilation-exposure-control/`、`building-fire-life-safety-codes/` 和 `immunization-public-health-surveillance/`。
- 下游：`school-workplace-outbreak-operations-continuity/`、`healthcare-surge-triage-capacity-continuity/` 和 `caregiving-long-term-care/`。

## 维护规则

- 新增资料必须说明它支持通风、过滤、建筑运行、空间开放风险还是公平治理。
- 不能输出 HVAC 操作、安装维修、采购建议、实时场所安全判断或法律责任判断。
