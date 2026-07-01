# medical-countermeasure-stockpile-distribution-continuity 目录说明

`domains/c6-local-unlocking/medical-countermeasure-stockpile-distribution-continuity/` 是 Human Infra 的医疗对策储备与分发连续性域，负责把暴发关键物资从库存转化为可达、合规、公平的风险控制输入。

## 目录结构

```text
medical-countermeasure-stockpile-distribution-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义战略储备、POD、医疗对策、PPE、冷链、物流、分配和公平可达的对象、链路、非目标和来源信号。
- 本域只整理公开医疗对策和供应分发资料。
- 药品选择、剂量、处方、囤货、库存位置、配送路径、资源抢占和监管规避不属于本域。

## 上下游关系

- 上游：`pharmaceutical-quality-supply-integrity/`、`public-procurement-contracting-capacity/`、`freight-logistics-port-cold-chain-continuity/` 和 `supply-chain-continuity/`。
- 下游：`healthcare-surge-triage-capacity-continuity/`、`vaccination-campaign-booster-delivery-continuity/`、`medicine-access-treatment-continuity/` 和 `mask-respirator-source-control-fit-access-continuity/`。

## 维护规则

- 新增资料必须说明它支持储备、POD、分发、冷链、分配公平、质量安全还是供应瓶颈分析。
- 不能输出处方治疗、个人囤货、库存位置、配送路径、设施安全弱点或规避分配内容。
