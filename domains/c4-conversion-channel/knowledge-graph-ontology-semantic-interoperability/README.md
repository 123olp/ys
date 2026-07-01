# Knowledge Graph Ontology Semantic Interoperability

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/knowledge-graph-ontology-semantic-interoperability` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 主要把科学、医疗、数据、制度或技术从潜在能力转成真实可用路径。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

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
