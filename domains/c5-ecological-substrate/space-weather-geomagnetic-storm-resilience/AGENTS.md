# AGENTS.md

## 职责

本目录维护空间天气、地磁暴和太阳活动对 Human Infra 的影响。重点是电网、卫星、通信、导航、时间同步和关键服务韧性。

## 文件

```text
space-weather-geomagnetic-storm-resilience/
├── AGENTS.md
└── README.md
```

## 上游

- `domains/c5-ecological-substrate/electric-grid-reliability-resilience-continuity/`
- `domains/c5-ecological-substrate/telecommunications-network-resilience-continuity/`
- `domains/c4-conversion-channel/geospatial-navigation-location-infrastructure/`
- `domains/c5-ecological-substrate/critical-infrastructure-lifeline-interdependency-resilience/`

## 下游

- 主体有效时间、求助能力、数据可用性和工具系统连续性。

## 边界

- 不提供实时空间天气操作建议。
- 不输出电网、卫星、航空、金融或导航系统的具体风险处置指令。
- 所有高风险结论必须回到 NOAA、NASA 或同等级权威来源。
