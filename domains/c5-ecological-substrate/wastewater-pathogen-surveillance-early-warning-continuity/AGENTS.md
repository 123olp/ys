# wastewater-pathogen-surveillance-early-warning-continuity 目录说明

`domains/c5-ecological-substrate/wastewater-pathogen-surveillance-early-warning-continuity/` 是 Human Infra 的污水病原体监测与早期预警连续性域，负责把社区级污水信号建模为暴发预警基础设施。

## 目录结构

```text
wastewater-pathogen-surveillance-early-warning-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义污水病原体监测、趋势信号、早期预警、社区聚合、隐私边界和风险沟通的对象、链路、非目标和来源信号。
- 本域只整理公开公共卫生监测资料、变量模型和边界。
- 采样教程、设施定位、个体结果解释、社区点名、污名化、恐慌传播和水务设施操作不属于本域。

## 上下游关系

- 上游：`immunization-public-health-surveillance/`、`public-health-laboratory-diagnostic-capacity/` 和 `water-wastewater-utility-service-continuity/`。
- 下游：`community-testing-screening-access-continuity/`、`school-workplace-outbreak-operations-continuity/`、`healthcare-surge-triage-capacity-continuity/` 和 `risk-engineering/`。

## 维护规则

- 新增资料必须说明它支持采样覆盖、趋势信号、早期预警、聚合隐私、公共卫生触发器还是风险沟通。
- 不能输出采样操作、设施定位、个体诊断、社区污名化、恐慌传播或规避监测内容。
