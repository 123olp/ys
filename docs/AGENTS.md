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
│   ├── 0003-add-future-waiting-domain.md
│   ├── 0004-add-cellular-reprogramming-domain.md
│   ├── 0005-establish-research-domain-atlas.md
│   ├── 0006-add-second-wave-research-domains.md
│   ├── 0007-add-third-wave-research-domains.md
│   ├── 0008-add-fourth-wave-molecular-maintenance-domains.md
│   ├── 0009-add-fifth-wave-external-technology-risk-domains.md
│   ├── 0010-add-sixth-wave-physiological-structural-maintenance-domains.md
│   ├── 0011-add-seventh-wave-homeostasis-choice-domains.md
│   └── README.md
├── explanations/
│   ├── README.md
│   ├── effective-immortality-acceleration-flywheel.md
│   ├── human-runtime-infrastructure.md
│   ├── life-path-prediction-model.md
│   ├── noah-ark-genealogy.md
│   └── value-lenses.md
├── how-to/
│   ├── README.md
│   ├── add-domain.md
│   ├── add-source-note.md
│   ├── contribute-docs.md
│   ├── run-quality-checks.md
│   └── share-human-infra.md
├── reference/
│   ├── README.md
│   ├── applications-and-literature.md
│   ├── document-lifecycle.md
│   ├── domain-map.md
│   ├── evidence-policy.md
│   ├── ethics-and-safety-boundaries.md
│   ├── glossary.md
│   ├── life-path-prediction-model-contract.md
│   ├── life-path-prediction-model-governance.md
│   ├── project-boundary-v0.1.md
│   ├── repository-standards.md
│   ├── research-domain-atlas.md
│   ├── research-domain-radar.md
│   ├── research-model-visualization-toolkit.md
│   ├── review-checklists.md
│   ├── source-card-system.md
│   ├── source-management.md
│   └── writing-style-guide.md
├── source-notes/
│   ├── README.md
│   ├── core-literature/
│   │   ├── AGENTS.md
│   │   ├── README.md
│   │   ├── reading-reports/
│   │   ├── 2026-06-28-human-infra-core-12-source-card-pack.md
│   │   └── 2026-06-28-human-infra-genealogy-download-manifest.md
│   ├── disembodied-cns-and-memory-editing-brief.md
│   ├── 2026-06-29-metric-redshift-recursive-waiting-revision-notes.md
│   ├── 2026-06-28-effective-immortality-flywheel-automated-research-run.md
│   ├── 2026-06-28-effective-immortality-flywheel-derivation-package.md
│   ├── 2026-06-28-effective-immortality-flywheel-evidence-matrix.md
│   ├── 2026-06-28-effective-immortality-flywheel-source-cards.md
│   ├── disembodied-cns-interface-architecture.md
│   ├── human-runtime-infrastructure-learning-note.md
│   └── human-runtime-infrastructure-longform.md
├── templates/
│   ├── README.md
│   ├── decision-record.md
│   ├── domain-readme.md
│   ├── research-card.md
│   ├── reference-doc.md
│   └── source-note.md
└── tutorials/
```

## 文件职责

- `explanations/human-runtime-infrastructure.md`：定义 Human Infra 的核心模型、七层结构、诊断框架和 Human SRE 类比。
- `explanations/effective-immortality-acceleration-flywheel.md`：新建有效永生飞轮 working paper，定义主体持续时间、有效时间、学习轮次、积累资本、技术采用、行动质量和可能性空间之间的研究链路。
- `explanations/life-path-prediction-model.md`：解释定量生命路径预测层的概念、时间类型、模型族和边界。
- `explanations/noah-ark-genealogy.md`：定义“诺亚方舟”作为 Human Infra 主隐喻的叙事谱系、理论谱系、映射、使用场景和传播边界。
- `explanations/value-lenses.md`：定义 Human Infra 的多视角价值理解，补充“寿命延长和逃逸路径带来的通用资源预算增量”视角但不替代主体持续性主线。
- `reference/applications-and-literature.md`：整理 Human Infra 的真实应用案例和首批文献主干。
- `reference/life-path-prediction-model-contract.md`：定义干预、状态转移、风险函数、生存曲线、有效时间、主观时间、相对时间和未来选择权的预测模型契约。
- `reference/life-path-prediction-model-governance.md`：定义定量预测模型的证据准入、偏差审查、验证、报告和禁止用途门禁。
- `reference/project-boundary-v0.1.md`：定义当前公开版本边界、纳入范围、排除范围、材料落点和后续版本方向。
- `reference/research-domain-atlas.md`：定义从有效永生先验条件生成研究域的规则、当前域地图和域判定契约。
- `reference/research-domain-radar.md`：记录尚未晋升为正式子域的潜在研究域、来源信号和晋升触发条件。
- `reference/research-model-visualization-toolkit.md`：沉淀科研论文阅读、文献脊梁、模型工具、可视化标准和 Human Infra 定量页面实现路线。
- `reference/source-card-system.md`：定义论文、书籍、工具、案例、标准和数据集进入项目之前的资料卡片制度。
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
- `how-to/share-human-infra.md`：说明如何对外介绍 Human Infra、复用短推文模板并保持传播边界。
- `source-notes/`：保存最新资料原文或轻整理版本，供后续提炼，不直接作为产品说明入口。
- `source-notes/README.md`：说明原始资料归档的文件职责和使用规则。
- `source-notes/core-literature/`：保存 Human Infra 谱系论文集的下载清单、核心 Source Card 草案、论文解读报告和缓存边界说明；原文缓存留在 `.research/literature/`。
- `source-notes/2026-06-28-effective-immortality-flywheel-automated-research-run.md`：记录有效永生飞轮第一轮自动化科研流程、文献脊梁、发现和下一步任务。
- `source-notes/2026-06-28-effective-immortality-flywheel-derivation-package.md`：保存有效永生飞轮公式推导包，冻结不变量、假设、符号、推导图、主公式、边界和开放风险。
- `source-notes/2026-06-28-effective-immortality-flywheel-evidence-matrix.md`：保存有效永生飞轮证据矩阵，把主链路拆成可检验边，并记录候选来源、证据角色、断裂条件和下一步模型任务。
- `source-notes/2026-06-28-effective-immortality-flywheel-source-cards.md`：保存有效永生飞轮第一批来源卡片，服务后续论文扩写、模型变量和 Web 可视化。
- `source-notes/2026-06-29-metric-redshift-recursive-waiting-revision-notes.md`：保存度规红移递归等待假设论文页 v0.2 优化依据、来源分层和下一步科研任务。
- `source-notes/2026-06-29-controllable-metric-waiting-room-hypothesis-revision-notes.md`：保存可控度规等待室假设论文页收口记录，包括研究对象、toy NCG 推导、场景比较、引用语境、预提交审查和覆盖审计。
- `templates/`：保存决策记录、子域 README、research card、source note 和 reference 文档模板。

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
