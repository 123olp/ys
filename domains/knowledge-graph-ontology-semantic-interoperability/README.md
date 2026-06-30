# Knowledge Graph Ontology Semantic Interoperability

## 定位

本域研究知识图谱、本体、语义互操作、受控词表、关系建模和 FAIR 数据原则，如何把 Human Infra 的多研究域组织成机器可读、可追踪、可组合和可审查的知识结构。

Human Infra 的研究对象跨越细胞、器官、主体、工具、社会服务、基础设施、制度和未来技术。如果只靠散文式文档，域之间的概念关系、变量边界和证据来源会逐渐失控。本域负责把“知识仓库”升级为“可计算知识系统”的语义层。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要整合大量研究域、变量、证据、技术和风险
  -> 这些对象必须能被统一命名、链接、追踪和机器读取
  -> 需要本体、知识图谱和语义互操作把碎片知识变成结构化系统
  -> knowledge-graph-ontology-semantic-interoperability
```

## 关注对象

- 概念、变量、干预、风险、终点、证据、来源和禁止用途的语义建模。
- RDF、OWL、SKOS、JSON-LD、schema.org 等知识表达方式。
- FAIR 原则、元数据、标识符、可查找性、可访问性、互操作性和可复用性。
- 生物医学和公共服务术语体系的映射边界，例如 UMLS、LOINC、SNOMED CT、OBO Foundry 相关生态。
- Human Infra 域地图、Source Card、Model Card、Scenario Card 和论文页面之间的关系结构。

## Human Infra 模型链路

```text
多域资料和变量
  -> 受控词表、本体和关系定义
  -> 形成可查询、可链接、可版本化的知识图谱
  -> 支撑模型变量契约、证据追踪、Web 可视化和自动审计
  -> 降低概念混淆、重复域、证据错配和跨域推理错误
```

## 非目标

- 不自称临床术语标准制定机构。
- 不提供医疗编码、保险编码、账单编码或临床语义映射服务。
- 不绕过 UMLS、SNOMED CT、LOINC 等术语系统的授权和许可边界。
- 不把知识图谱推理结果写成事实证明或临床结论。

## Source Signals

- FAIR Principles: https://www.go-fair.org/fair-principles/
- OBO Foundry Principles: https://obofoundry.org/principles/fp-000-summary.html
- W3C RDF: https://www.w3.org/RDF/
- W3C OWL 2 Overview: https://www.w3.org/TR/owl2-overview/
- UMLS: https://www.nlm.nih.gov/research/umls/index.html
- LOINC: https://loinc.org/

## 下一步

- 建立 Human Infra ontology seed：Domain、Variable、Intervention、Outcome、Risk、Evidence、Boundary、Source。
- 为 `docs/reference/research-domain-atlas.md` 设计可机器读取的域关系表。
- 与 `model-cards-ai-audit-documentation/` 对接，把模型卡、数据卡和来源卡纳入同一知识图谱。
