# energy-access-resilience 目录说明

`energy-access-resilience/` 是 Human Infra 的能源可及与韧性域，负责研究电力、清洁烹饪、温控、通信供能和医疗设备供电如何支撑主体持续性。

## 目录结构

```text
energy-access-resilience/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义能源可及与韧性域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做能源可及、可靠性、清洁烹饪、能源负担、停电和能源韧性资料整理。
- 个体电气施工、发电设备、燃料储存、账单申请、投资和危险接线不属于本域。

## 上下游关系

- 上游：`supply-chain-continuity/`、`planetary-health-environment/`、`financial-resilience-access/`。
- 下游：`housing-built-environment-stability/`、`thermal-homeostasis-resilience/`、`healthcare-access-continuity/` 和 `emergency-preparedness-response/`。

## 维护规则

- 新增资料必须说明它影响电力可及、可靠性、清洁烹饪、能源负担、停电、医疗供电还是通信供电。
- 禁止输出危险电气、燃料、采购、补贴申请或应急供电操作建议。
