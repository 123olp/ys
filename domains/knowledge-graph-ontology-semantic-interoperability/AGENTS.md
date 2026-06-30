# Knowledge Graph Ontology Semantic Interoperability 目录说明

## 目录结构

```text
knowledge-graph-ontology-semantic-interoperability/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义知识图谱、本体、语义互操作和 FAIR 知识结构在 Human Infra 中的职责边界。
- `AGENTS.md`：说明本目录的职责边界和维护规则。

## 边界

本目录只承载概念建模、语义关系、知识结构和互操作边界。它不承载临床编码服务、保险账单编码、诊断映射、许可受限术语转储或自动事实证明。

## 维护规则

- 新增概念必须说明上位类、关系、来源和禁止推论。
- 不允许把语义映射写成临床等价或监管等价。
- 任何使用外部术语体系的内容必须保留许可、访问和引用边界。
- 图谱推理只能作为检索和审查辅助，不能替代证据审查。
