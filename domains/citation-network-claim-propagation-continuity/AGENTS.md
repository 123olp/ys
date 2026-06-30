# citation-network-claim-propagation-continuity 目录说明

本目录负责引用网络、引用语境和主张传播连续性。

## 结构

```text
citation-network-claim-propagation-continuity/
├── AGENTS.md
└── README.md
```

## 边界

- 只维护引用语境、主张链、误引风险和知识图谱纠错字段。
- 上游：`domains/persistent-identifier-doi-citation-metadata-continuity/`、`domains/retraction-expression-concern-correction-continuity/`。
- 下游：`domains/knowledge-graph-ontology-semantic-interoperability/`、Source Card、系统综述和研究雷达。
- 不提供刷引用、引用操控、论文 SEO、声誉攻击或访问控制绕过。

## 维护规则

使用 Crossref、OpenAlex、scite 和 Retraction Watch 等来源作为信号锚点。引用次数不是证据强度；必须记录引用语境和主张支持状态。
