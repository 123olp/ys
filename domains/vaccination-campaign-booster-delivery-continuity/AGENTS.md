# vaccination-campaign-booster-delivery-continuity 目录说明

`domains/vaccination-campaign-booster-delivery-continuity/` 是 Human Infra 的疫苗行动与加强针递送连续性域，负责把免疫技术转化为暴发期间可达、及时、公平的群体保护。

## 目录结构

```text
vaccination-campaign-booster-delivery-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义疫苗行动、加强针递送、冷链、预约、提醒、高风险覆盖和可达公平的对象、链路、非目标和来源信号。
- 本域只整理公共卫生行动资料、执行变量和边界。
- 个体接种建议、禁忌判断、医学风险解释、预约代办、证明伪造和冷链操作不属于本域。

## 上下游关系

- 上游：`immunization-public-health-surveillance/`、`pharmaceutical-quality-supply-integrity/` 和 `pharmacovigilance-drug-safety-monitoring/`。
- 下游：`school-workplace-outbreak-operations-continuity/`、`immunization-record-proof-continuity/` 和 `healthcare-surge-triage-capacity-continuity/`。

## 维护规则

- 新增资料必须说明它支持递送、覆盖、冷链、预约、提醒、信任还是公平。
- 不能输出接种医学建议、优先级规避、证明伪造、冷链操作或个体风险判断。
