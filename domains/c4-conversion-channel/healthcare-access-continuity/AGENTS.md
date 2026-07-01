# healthcare-access-continuity 目录说明

`healthcare-access-continuity/` 是 Human Infra 的医疗服务连续性域，负责把医疗可及、连续照护、服务质量、转诊、随访和费用摩擦建模为主体持续性的外部条件。

## 目录结构

```text
healthcare-access-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义医疗服务连续性域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做公开资料整理、变量建模、证据边界和服务断点分析。
- 个体诊断、治疗、医生选择、医院选择、保险选择、支付建议和急救替代服务不属于本域。

## 上下游关系

- 上游：`health-literacy-navigation/`、`financial-resilience-access/`、`digital-identity-security/` 和 `supply-chain-continuity/`。
- 下游：`rehabilitation-functioning/`、`caregiving-long-term-care/`、`measurement-feedback/` 和所有具体健康维护域。

## 维护规则

- 新增资料必须说明它支持的是服务可及、连续性、质量、成本、等待、转诊还是随访变量。
- 不能把公共健康或服务系统指标写成个体医疗建议。
