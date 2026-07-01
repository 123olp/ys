# child-care-availability-affordability-continuity 目录说明

`child-care-availability-affordability-continuity/` 是 Human Infra 的托育供给与费用可承受性执行域，负责研究名额、费用、时段、距离和年龄覆盖如何影响家庭运行与照护者有效时间。

## 目录结构

```text
child-care-availability-affordability-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义托育供给、费用和可达性执行域的对象、链路、非目标和来源信号。
- 本域只整理公开资料、指标和结构性变量，不做个体机构推荐、价格判断、排队策略或家庭安排。
- 儿童身份、家庭收入、住址、排班、托育记录和候补名单资料不得进入本域。

## 上下游关系

- 上游：`childcare-family-continuity/`、`social-protection-benefits-delivery/`、`workforce-employment-services/`。
- 下游：`time-allocation-effective-time/`、`financial-resilience-access/`、`child-care-subsidy-ccdf-payment-continuity/`。

## 维护规则

- 新增资料必须说明它影响名额、费用、时段、距离、年龄覆盖、等待时间还是照护稳定性。
- 禁止输出托育机构选择、补贴申请、儿童适配、费用建议或家庭纠纷建议。
