# medicine-access-treatment-continuity 目录说明

`domains/medicine-access-treatment-continuity/` 是 Human Infra 的药品可及与治疗连续性域，负责把关键药物供应、覆盖、标签、理解和用药安全建模为主体持续性的医疗执行条件。

## 目录结构

```text
medicine-access-treatment-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义药品可及、用药安全、短缺、覆盖和治疗连续性的对象、链路、非目标和来源信号。
- 本域只做公开资料整理、变量建模、证据边界和治疗执行断点分析。
- 个人用药建议、替代药物、剂量、停药、处方解释、购药渠道和保险选择不属于本域。

## 上下游关系

- 上游：`healthcare-access-continuity/`、`supply-chain-continuity/`、`financial-resilience-access/` 和 `health-literacy-navigation/`。
- 下游：`cancer-control/`、`cardiovascular-resilience/`、`immune-maintenance/`、`renal-hepatic-clearance/` 和其他依赖持续治疗的健康域。

## 维护规则

- 新增资料必须说明它支持的是可得性、短缺、覆盖、标签、患者理解、用药安全还是供应恢复变量。
- 不能把药品公开资料写成个体治疗、购药、替代或保险建议。
