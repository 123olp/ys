# toxic-plume-air-monitoring-risk-communication-continuity 目录说明

`domains/toxic-plume-air-monitoring-risk-communication-continuity/` 是 Human Infra 的有毒羽流空气监测与风险沟通连续性域，负责把动态空气暴露信号建模为公众行动和信任接口。

## 目录结构

```text
toxic-plume-air-monitoring-risk-communication-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义空气监测、羽流模型、气象接口、阈值沟通和不确定性表达。
- 本域只整理公开工具边界、变量模型和沟通风险。
- 实时预测、传感器部署、阈值判断、撤离命令、攻击模拟和检测规避不属于本域。

## 上下游关系

- 上游：`weather-climate-observation-forecasting/`、`chemical-safety-poison-control-toxicology/`、`air-quality-ventilation-exposure-control/`。
- 下游：`chemical-release-shelter-evacuation-continuity/`、`emergency-alerts-communications/`、`healthcare-access-continuity/`。

## 维护规则

- 新增资料必须说明它支持监测、模型、气象、不确定性、公众沟通还是信任治理。
- 不得写入实时行动建议、设施攻击、扩散优化、恐慌传播或个体健康解释。
