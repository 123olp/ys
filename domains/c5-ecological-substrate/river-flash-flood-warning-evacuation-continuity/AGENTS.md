# AGENTS.md

## 职责

本目录维护河流洪水、山洪、道路淹没、洪水预警、撤离避难和灾后返回对主体持续性的影响。重点是从官方警报到人类行动的执行链，不做实时路线或水文调度。

## 文件

```text
river-flash-flood-warning-evacuation-continuity/
├── AGENTS.md
└── README.md
```

## 上游

- `domains/c5-ecological-substrate/weather-climate-observation-forecasting/`
- `domains/c5-ecological-substrate/emergency-alerts-communications/`
- `domains/c5-ecological-substrate/water-resources-hydrology-flood-drought-management/`
- `domains/c5-ecological-substrate/household-emergency-preparedness-resilience/`

## 下游

- `domains/c5-ecological-substrate/disaster-recovery-relief-continuity/`
- `domains/c5-ecological-substrate/post-flood-mold-moisture-indoor-recovery-continuity/`
- `domains/c5-ecological-substrate/flood-insurance-nfip-claims-continuity/`

## 边界

- 不输出实时预警、行车路线、涉水判断、撤离点选择或房屋返回建议。
- 不替代 NWS/NOAA、FEMA、地方应急管理、水文、交通或公共安全机构。
- 内容只做研究域建模、资料索引、证据边界和禁止用途维护。
