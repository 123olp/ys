# AGENTS.md

## 职责

本目录维护冬季风暴、极寒、冰雪、停电、取暖、道路中断和寒冷暴露对主体持续性的影响。

## 文件

```text
winter-storm-cold-exposure-power-continuity/
├── AGENTS.md
└── README.md
```

## 上游

- `domains/c5-ecological-substrate/weather-climate-observation-forecasting/`
- `domains/c5-ecological-substrate/emergency-alerts-communications/`
- `domains/c5-ecological-substrate/energy-access-resilience/`
- `domains/c5-ecological-substrate/fuel-thermal-energy-service-continuity/`

## 下游

- `domains/c2-source-maintenance/thermal-homeostasis-resilience/`
- `domains/c6-local-unlocking/backup-power-battery-generator-safety-continuity/`
- `domains/c6-local-unlocking/carbon-monoxide-alarm-combustion-appliance-safety-continuity/`

## 边界

- 不输出实时道路、设备操作、发电机使用、低体温急救、药物处理、车辆救援或医疗建议。
- 不替代 NWS、地方应急管理、公用事业、消防、医疗或公共安全机构。
- 内容只做研究域建模、资料索引、证据边界和禁止用途维护。
