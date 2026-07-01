# weather-climate-observation-forecasting 目录说明

本目录承载 Human Infra 中“天气气候观测与预报”研究域。

## 结构

```text
weather-climate-observation-forecasting/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义天气气候观测、预报和气候服务如何进入主体持续性模型。
- 本目录只做公开资料、变量、风险链路和来源治理，不放实时预报服务、灾害指挥或个体撤离建议。

## 上下游关系

- 上游：`docs/reference/research-domain-atlas.md`、`planetary-health-environment/`、`risk-engineering/`。
- 下游：`emergency-alerts-communications/`、`household-emergency-preparedness-resilience/`、`disaster-recovery-relief-continuity/`、`energy-access-resilience/`、`transportation-access-mobility/`。

## 维护规则

- 公开结论必须回到官方气象、气候、预警或科研数据来源。
- 不把模型预测写成确定事件，不输出个人安全承诺。
- 涉及实时危险天气时，只指向官方来源和安全边界，不给现场操作指令。
