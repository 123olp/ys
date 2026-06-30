# Survival Analysis Healthspan Risk Modeling 目录说明

## 目录结构

```text
survival-analysis-healthspan-risk-modeling/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义生存分析、健康寿命、风险函数、竞争风险和有效时间建模边界。
- `AGENTS.md`：说明本目录的职责边界和维护规则。

## 边界

本目录只承载群体层和方法层的风险建模语言。它不承载个体寿命预测、个体死亡日期、保险评分、医疗诊断、临床用药或现实治疗决策。

## 维护规则

- 所有模型表达必须区分 population-level、subgroup-level 和 individual-level。
- 图表必须说明它展示的是概念、toy model、公开数据还是经验证模型。
- 不允许把 hazard ratio 简化成个体寿命增减。
- 新增公式时必须说明变量、结局、删失、竞争风险和外部验证状态。
