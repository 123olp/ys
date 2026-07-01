# longitudinal-cohort-retention-followup-infrastructure 目录说明

本目录维护纵向队列、长期随访、参与者留存和生命历程数据基础设施。它是寿命、健康寿命和有效时间模型的长期观测层。

## 目录结构

```text
longitudinal-cohort-retention-followup-infrastructure/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义队列留存、随访、失访、事件确认和数据链接如何支撑 Human Infra 定量模型。
- 本目录不保存参与者数据、队列微数据、联系信息或可识别记录。
- 所有队列材料必须保留样本范围、随访时间、结局定义、失访情况和人群适用边界。

## 上下游关系

- 上游来自参与者同意、数据治理、队列方法和公共队列资料。
- 下游服务生存分析、因果推断、数字孪生、健康寿命预测和真实世界证据。
- 不替代 `data-quality-missingness-representativeness/`；本目录关注队列运行和随访基础设施。

## 维护规则

- 不提供重新识别、越权链接、诱导留存或规避同意策略。
- 不把队列相关性写成干预因果结论。
- 若新增队列证据，必须记录样本、随访、结局、失访、偏差和适用边界。
