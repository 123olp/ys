# ai-data-provenance-contamination-drift-continuity 目录说明

本目录维护 AI 数据谱系、污染和漂移治理资料。它是 AI 模型可信性的数据地基层。

## 目录结构

```text
ai-data-provenance-contamination-drift-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 AI 数据来源、污染、分布漂移和代表性如何影响主体持续性。
- 本目录只维护数据治理框架和边界，不保存私有数据集、受限全文、泄露数据或个人敏感数据。
- 资料进入本域时必须保留数据来源、版本、许可、污染检查、代表性和删除/退出约束。

## 上下游关系

- 上游来自 Datasheets for Datasets、NIST AI RMF、Data Provenance Initiative、OWASP LLM Top 10 和数据治理文献。
- 下游服务 `ai-evaluation-benchmark-validity-continuity/`、`synthetic-data-generation-validation-continuity/` 和模型发布审计。
- 不替代 `data-quality-missingness-representativeness/`；该域关注一般数据质量，本目录关注 AI 数据链路。

## 维护规则

- 不记录受限数据抓取、访问控制绕过、重新识别、数据造假或来源隐匿方法。
- 不把数据清洗写成事实净化。
- 若新增数据字段影响 Source Card 或模型卡契约，必须同步更新对应索引。
