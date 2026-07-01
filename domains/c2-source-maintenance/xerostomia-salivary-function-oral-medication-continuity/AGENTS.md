# xerostomia-salivary-function-oral-medication-continuity 目录说明

`domains/c2-source-maintenance/xerostomia-salivary-function-oral-medication-continuity/` 保存口干、唾液功能和药物相关口腔风险连续性研究域。

## 目录结构

```text
xerostomia-salivary-function-oral-medication-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责口干、唾液功能、药物负担、放疗后口腔风险、吞咽言语和口腔感染风险的资料整理。
- 本域可以描述口腔副作用如何影响进食、睡眠、沟通和生活质量。
- 本域不提供药物更改、剂量、产品、治疗、Sjögren 诊断或个体护理建议。

## 上下游关系

- 上游：`oral-health-continuity/`、`medication-access-continuity/`、`geriatric-long-term-care-oral-health-continuity/`。
- 下游：`dental-caries-prevention-restoration-continuity/`、`swallowing-dysphagia-aspiration-nutrition/`、`speech-language-communication-continuity/`。

## 维护规则

- 口干资料必须区分症状、唾液功能、药物相关风险、疾病相关风险和治疗后风险。
- 不允许把资料写成停药、换药、产品推荐或自我诊断流程。
- 新增文件或子目录时，同步更新本文件。
