# docs 目录说明

`docs/` 是 Human Infra 的总理论和治理边界层，只保存跨子域稳定材料，不承载某个子域的业务数据或采集脚本。

## 目录结构

```text
docs/
├── AGENTS.md
├── README.md
├── decisions/
│   ├── 0001-adopt-docs-as-code-knowledge-base-structure.md
│   ├── 0002-adopt-local-quality-gates.md
│   └── README.md
├── explanations/
│   ├── README.md
│   └── human-runtime-infrastructure.md
├── how-to/
│   ├── README.md
│   ├── add-domain.md
│   ├── add-source-note.md
│   ├── contribute-docs.md
│   └── run-quality-checks.md
├── reference/
│   ├── README.md
│   ├── document-lifecycle.md
│   ├── domain-map.md
│   ├── evidence-policy.md
│   ├── ethics-and-safety-boundaries.md
│   ├── glossary.md
│   ├── repository-standards.md
│   ├── review-checklists.md
│   ├── source-management.md
│   └── writing-style-guide.md
├── source-notes/
│   ├── README.md
│   ├── disembodied-cns-and-memory-editing-brief.md
│   ├── disembodied-cns-interface-architecture.md
│   ├── human-runtime-infrastructure-learning-note.md
│   └── human-runtime-infrastructure-longform.md
├── templates/
│   ├── README.md
│   ├── decision-record.md
│   ├── domain-readme.md
│   ├── reference-doc.md
│   └── source-note.md
└── tutorials/
```

## 文件职责

- `explanations/human-runtime-infrastructure.md`：定义 Human Infra 的核心模型、七层结构、诊断框架和 Human SRE 类比。
- `reference/domain-map.md`：定义根项目与子域的边界、迁移切片、主动不做和验证点。
- `reference/ethics-and-safety-boundaries.md`：定义医疗、组织、去具身中枢、记忆编辑和数据证据边界。
- `reference/evidence-policy.md`：定义证据、解释、主张、推测和决策的分层规则。
- `reference/source-management.md`：定义 source notes、外部数据和稳定文档之间的流转规则。
- `reference/document-lifecycle.md`：定义文档从 source 到 stable、superseded、archived 的生命周期。
- `reference/repository-standards.md`：记录本仓库采用的标准结构、根文件和调研来源。
- `reference/review-checklists.md`：提供文档、证据、安全、域边界和数据脚本审查清单。
- `how-to/add-domain.md`：说明新增子域的步骤和停止条件。
- `how-to/add-source-note.md`：说明新增 source note 的步骤和规则。
- `how-to/run-quality-checks.md`：说明如何运行本地质量检查。
- `source-notes/`：保存最新资料原文或轻整理版本，供后续提炼，不直接作为产品说明入口。
- `source-notes/README.md`：说明原始资料归档的文件职责和使用规则。
- `templates/`：保存决策记录、子域 README、source note 和 reference 文档模板。

## 依赖关系

- `README.md` 和根 `AGENTS.md` 依赖本目录的稳定文档描述总项目。
- `domains/*/README.md` 可引用本目录的上位原则，但不能把自身职责推回 `docs/`。
- `source-notes/` 只向稳定文档提供资料来源，不反向决定架构。

## 维护规则

- 新的跨域原则、伦理边界、域地图变更写入本目录。
- 单一子域的产品、数据源、脚本说明写入对应 `domains/*/`。
- 原始资料进入 `source-notes/` 前必须改成语义化文件名。
- 稳定结论应从 `source-notes/` 提炼出来，避免长期以临时资料名作为知识入口。
- 新增重复类型文档时优先使用 `templates/`，避免每次重新发明结构。
