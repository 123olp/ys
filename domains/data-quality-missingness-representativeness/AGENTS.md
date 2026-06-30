# Data Quality Missingness Representativeness 目录说明

## 目录结构

```text
data-quality-missingness-representativeness/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义数据质量、缺失机制、代表性、测量误差和数据入口门禁。
- `AGENTS.md`：说明本目录的职责边界和维护规则。

## 边界

本目录只承载数据入口审查、偏差识别和代表性治理。它不承载个人数据处理、数据再识别、隐私规避、数据爬取、数据买卖、伪造清洗或统计操控。

## 维护规则

- 所有数据源必须声明来源、覆盖对象、采集机制、缺失机制、测量误差和适用边界。
- 不允许用代表性不足的数据推导普遍化结论。
- 不允许把 imputation 后的数据写成真实观测。
- 涉及隐私、同意、授权或数据权利时必须转向 `health-data-privacy-governance/`。
