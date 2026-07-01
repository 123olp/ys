# synthetic-data-generation-validation-continuity 目录说明

本目录维护合成数据生成、验证和边界治理资料。它是把稀缺或敏感数据转化为可审查研究材料前的验证层。

## 目录结构

```text
synthetic-data-generation-validation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义合成数据的隐私、效用、分布保真和下游风险如何影响主体持续性研究。
- 本目录只维护合成数据验证框架，不保存原始敏感数据、生成模型权重或可逆推断材料。
- 资料进入本域时必须保留原始数据边界、生成方法、隐私验证、效用验证和禁止用途。

## 上下游关系

- 上游来自 NIST、ICO、数据治理、隐私工程和合成数据评估资料。
- 下游服务 `ai-data-provenance-contamination-drift-continuity/`、`ai-evaluation-benchmark-validity-continuity/` 和仿真/模型验证页面。
- 不替代 `privacy-preserving-computation/`；该域关注计算机制，本目录关注合成数据产物验证。

## 维护规则

- 不记录重新识别、成员推断、隐私攻击或合成数据洗白方法。
- 不把合成数据写成自动匿名化或自动合规。
- 若新增合成数据字段影响 Source Card 或数据模板，必须同步更新索引。
