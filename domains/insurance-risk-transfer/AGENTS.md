# insurance-risk-transfer 目录说明

`insurance-risk-transfer/` 是 Human Infra 的保险与风险转移域，负责研究高成本风险如何通过保险、赔付、担保和风险池被制度性分摊。

## 目录结构

```text
insurance-risk-transfer/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义保险与风险转移域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做覆盖、保费、自付、理赔、拒赔、风险池、保障缺口和制度性风险分摊资料整理。
- 个体投保、理赔、税务、法律、投资、福利、财务规划和保险规避不属于本域。

## 上下游关系

- 上游：`financial-resilience-access/`、`occupational-work-design/`、`legal-identity-civil-registration/`。
- 下游：`healthcare-access-continuity/`、`emergency-preparedness-response/`、`social-protection-benefits-delivery/` 和 `housing-built-environment-stability/`。

## 维护规则

- 新增资料必须说明它影响覆盖、保费、自付、免赔额、理赔、拒赔、等待期、风险池还是保障缺口。
- 禁止输出个体保险选择、理赔策略、规避或欺诈方法。
