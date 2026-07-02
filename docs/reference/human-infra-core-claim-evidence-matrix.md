# Human Infra Core Claim-Evidence Matrix

本文档把 Human Infra 的核心价值主张、研究框架主张和定量模型主张绑定到外部方法锚点。它不是宣传稿，也不是文献综述；它的用途是防止 README、论文页、Web 页面和模型文档在讲同一件事时使用不同边界。

## 使用边界

- 本文件只证明 Human Infra 的主张语言可以被哲学、公共卫生、复杂干预、预测模型和健康经济建模传统约束。
- 本文件不证明任何具体长寿技术、医学干预、AI 工具、时间差分路径或社会政策已经能实现有效永生。
- 本文件不提供个体医疗、法律、投资、生活方式、药物、训练、设备或风险规避建议。
- 本文件的来源多数是方法锚点和定义锚点；方法锚点只能约束如何建模、报告和审查，不能替代实证证据。

## Source Anchor Cards

| ID | 来源 | Human Infra 使用位置 | 能支持什么 | 不能支持什么 |
| --- | --- | --- | --- | --- |
| `SA1` | Stanford Encyclopedia of Philosophy / Internet Encyclopedia of Philosophy: Capability Approach | 把 Human Infra 的价值对象从“资源占有”转向“真实可行动、可选择、可实现的生活路径” | 用 capabilities / functionings 语言描述真实机会集合、行动能力和选择空间 | 不证明永生是伦理必然；不证明任何技术会自动扩大能力集合 |
| `SA2` | WHO Constitution | 把健康从“无病”扩展为身体、心理和社会福祉，并连接公共责任与社会条件 | 支持 Human Infra 把身体、心理、社会支持、环境和服务纳入主体持续性对象 | 不支持把健康定义直接外推为长寿干预效果或个人健康建议 |
| `SA3` | MRC / NIHR complex interventions framework | 把 Human Infra 技术、医疗、AI、服务、环境和资源路径视为复杂干预和语境化系统 | 支持“不能只问单点变量好不好，要看机制、语境、实施、适用性和系统后果” | 不证明某个复杂干预有效；不替代 RCT、队列研究、实施研究或伦理审查 |
| `SA4` | TRIPOD+AI | 约束预测模型报告：目标人群、预测目标、数据、建模、验证、更新、透明度 | 支持区分 toy model、screening model、calibrated predictive model 和 deployed decision model | 不证明当前 Human Infra toy model 达到临床预测标准 |
| `SA5` | PROBAST / PROBAST+AI | 约束预测模型偏倚和适用性审查 | 支持把 risk of bias、applicability、数据来源、样本、预测因子和分析问题放入 gate | 不证明模型低偏倚；不证明 AI 模型适合实际使用 |
| `SA6` | ISPOR-SMDM Modeling Good Research Practices | 约束模型透明度、验证、结构、参数、报告和决策语境 | 支持模型必须可解释结构、来源、参数、验证和用途边界 | 不证明模型可用于医保、资源分配、临床或政策决策 |
| `SA7` | OHDSI Patient-Level Prediction | 提供观察性医疗数据中患者级预测模型的标准化工程参考 | 支持未来把真实队列、OMOP/CDM、外部验证和网络研究作为升级方向 | 不证明 Human Infra 当前拥有医疗数据、可泛化模型或个体预测许可 |
| `SA8` | DYNAMO-HIA | 提供群体风险因素、疾病、死亡和情景比较的动态健康影响建模参考 | 支持 Human Infra 用情景级风险状态、参考场景和干预场景表达群体路径 | 不证明当前模型参数真实；不支持个人死亡日期、个体寿命或临床疗效推断 |

## Core Claim Register

| Claim ID | 核心主张 | 主张类型 | 当前状态 | 反证或降级条件 |
| --- | --- | --- | --- | --- |
| `HI-CL1` | 一切目标、价值和创造都预设一个仍能感知、判断、行动、学习和修正的主体。 | 先验 / 规范 / 定义 | `working-core` | 如果项目无法把“主体”操作化为状态、能力、风险和边界变量，该主张必须降级为哲学口号。 |
| `HI-CL2` | Human Infra 的对象不是单点延寿，而是维护和扩展主体持续性的基础条件集合。 | 框架 / 范围 | `working-core` | 如果研究域无法说明其对持续存在、行动、恢复、学习、选择或进入未来的贡献，应移出核心范围或降级为边缘域。 |
| `HI-CL3` | 主体持续性的价值不只体现在寿命长度，也体现在健康寿命、有效时间、主观时间、相对时间、行动能力和未来选择权。 | 测量 / 价值 | `working-core` | 如果模型只剩单一寿命指标，不能表示健康质量、行动能力和选项空间，Human Infra 价值语言必须收缩。 |
| `HI-CL4` | 技术或干预不能被当成“加寿命变量”，必须被放入变量、状态、风险函数、生存曲线和有效时间链路中审查。 | 模型 / 方法 | `working-core` | 如果无法定义变量、机制、风险、结果、证据等级和不确定性，该技术只能进入候选域，不能进入定量模型。 |
| `HI-CL5` | Human Infra 的多数路径是复杂干预：医学、AI、工具、服务、环境、资金、社会支持和治理共同作用。 | 系统 / 实施 | `working-core` | 如果某条路线只能通过单一叙事成立、不能拆解语境和实施路径，应禁止写成稳定结论。 |
| `HI-CL6` | 当前模型只能是 toy / screening / research infrastructure，不能输出个体死亡日期、个体医学建议或真实校准结论。 | 治理 / 禁止用途 | `enforced-locally` | 若页面、数据或脚本输出个体死亡日期、个人寿命排名、个体医疗建议或未验证校准声明，必须阻塞。 |
| `HI-CL7` | 走向严肃研究框架需要主张级证据闭环：Source Cards、Claim-Evidence Matrix、变量表、反证条件和模型位置。 | 研究治理 | `working-core` | 如果强主张无法回到来源、证据等级和禁止外推边界，应从 README、论文页和 Web 页面降级或删除。 |

## Claim-Evidence Matrix

| Claim | 支撑来源 | 来源角色 | 证据强度 | 支持范围 | 禁止外推 |
| --- | --- | --- | --- | --- | --- |
| `HI-CL1` | `SA1` Capability Approach；Human Infra 先验追问文档 | 规范评价空间 / 项目第一性定义 | `conceptual-medium` | 支持把主体真实可行动能力和选择空间作为价值语言，而不只看资源或产出 | 不证明生物永生可行；不证明任何增强技术自动有价值 |
| `HI-CL2` | `SA2` WHO Constitution；`SA3` MRC complex interventions | 健康多维定义 / 复杂系统边界 | `method-medium` | 支持把身体、心理、社会、服务、环境和实施语境纳入基础设施对象 | 不证明所有社会问题都应进入 Human Infra；不证明某域已具备证据闭环 |
| `HI-CL3` | `SA1` Capability Approach；`SA2` WHO Constitution；`SA8` DYNAMO-HIA | 能力集合 / 健康质量 / 群体情景模型 | `method-medium` | 支持用有效时间、健康质量、行动能力和选项空间补充寿命指标 | 不支持把 option value 直接量化为真实福利；不支持个人级结论 |
| `HI-CL4` | `SA4` TRIPOD+AI；`SA5` PROBAST+AI；`SA6` ISPOR-SMDM；`SA7` OHDSI PLP | 预测模型报告、偏倚、验证和工程参考 | `method-high` | 支持要求目标人群、time zero、outcome、estimand、predictors、validation、calibration 和 prohibited use | 不证明当前 toy model 已校准；不证明变量链路具有因果效应 |
| `HI-CL5` | `SA3` MRC complex interventions；`SA6` ISPOR-SMDM | 复杂干预和模型透明度 | `method-medium` | 支持把多组件、多语境、多反馈、多风险的路线拆成概率门和实施路径 | 不支持把复杂性当成无法验证的借口；不支持跳过单项证据 |
| `HI-CL6` | `SA4` TRIPOD+AI；`SA5` PROBAST+AI；`SA6` ISPOR-SMDM；本地 `life-path-toy-model-audit` | 报告透明度、偏倚审查、验证边界和本地 gate | `local-enforced-medium` | 支持当前禁止个体死亡日期、个体预测、医学建议和未验证校准声明 | 不证明模型永远安全；不替代外部审查、伦理审查或真实数据治理 |
| `HI-CL7` | `SA4` TRIPOD+AI；`SA5` PROBAST+AI；`docs/reference/evidence-policy.md`；`docs/reference/source-card-system.md` | 报告、偏倚、证据治理和 source card 制度 | `process-medium` | 支持把强主张拆成来源、主张类型、证据等级、适用范围和反证条件 | 不证明现有全部 990 个域都已完成主张级证据闭环 |

## Method Translation Contract

Human Infra 对外部方法传统的使用必须遵守以下转换规则：

```text
Capability Approach
  -> 只转译为真实能力、功能、选择空间和可能性集合语言
  -> 不转译为永生伦理证明

WHO health framing
  -> 只转译为身体、心理、社会和公共条件的对象边界
  -> 不转译为具体疗效证据

MRC complex interventions
  -> 只转译为复杂系统、语境、机制、实施和适用性 gate
  -> 不转译为某干预有效

TRIPOD+AI / PROBAST+AI
  -> 只转译为预测模型报告、偏倚、适用性和校准/验证要求
  -> 不转译为当前模型已经可预测

ISPOR-SMDM / OHDSI / DYNAMO-HIA
  -> 只转译为模型透明度、验证、群体情景和数据工程参考
  -> 不转译为个人预测许可或真实决策模型
```

## Project-Level Evidence Gates

进入 README、论文页或 Web 模型页的主张，至少要通过下列 gate：

| Gate | 要求 | 未通过时处理 |
| --- | --- | --- |
| `claim-type` | 标明是定义、规范、机制、预测、因果、治理还是传播主张 | 降级为 source note 或删除 |
| `source-role` | 标明来源是定义锚点、方法锚点、实证证据、数据源、工具还是内部模型 | 不允许作为稳定结论 |
| `scope-boundary` | 写明适用对象、时间尺度、数据条件和不可支持结论 | 不允许进入 README 主叙事 |
| `model-position` | 指明主张进入 screening、toy、calibrated prediction 还是 decision model | 禁止写成定量结论 |
| `falsifier` | 至少写出一个会让主张降级的条件 | 只能作为假设 |
| `prohibited-use` | 医疗、法律、投资、个人预测、工程操作等高风险边界必须写清 | 必须阻塞发布 |

## Current Project Status

| 维度 | 当前状态 | 下一步 |
| --- | --- | --- |
| 价值主张 | 已有第一性语言和多视角价值解析 | 把 `HI-CL1` 到 `HI-CL3` 压入 README、论文页和 Web 首页的同一表述 |
| 研究框架 | 已有 C1-C6 域地图、evidence policy、source-card system 和本矩阵 | 给 C1/C2 核心域补主张级矩阵，而不是只补域骨架 |
| 定量模型 | 已有 toy model、合成敏感性分析和本地审计 | 进入真实队列前补 acquisition-ready Data Card、字段字典、权重、endpoint 和输出抑制 |
| 治理边界 | 已有禁止个体死亡日期、医学建议和未校准外推边界 | 把所有强叙事页面纳入同一 claim gate |

## Local Audit

本矩阵进入本地质量门禁：

```bash
python3 tools/audit_core_claim_evidence_matrix.py
make claim-matrix-audit
```

审计范围只覆盖结构契约：Source Anchor、Claim ID、gate、禁止用途、方法锚点 URL 和入口索引。它不验证外部文献真实性，也不把方法锚点升级为实证证据。

## Source Traceability

- Capability Approach, Stanford Encyclopedia of Philosophy: https://plato.stanford.edu/entries/capability-approach/
- Capability Approach, Internet Encyclopedia of Philosophy: https://iep.utm.edu/sen-cap/
- WHO Constitution: https://www.who.int/about/governance/constitution
- MRC / NIHR complex interventions framework, BMJ 2021: https://www.bmj.com/content/374/bmj.n2061
- TRIPOD+AI official statement hub: https://www.tripod-statement.org/
- TRIPOD+AI BMJ 2024: https://www.bmj.com/content/385/bmj-2023-078378
- PROBAST official site: https://www.probast.org/
- PROBAST+AI PubMed entry: https://pubmed.ncbi.nlm.nih.gov/40127903/
- ISPOR-SMDM model transparency and validation: https://www.valueinhealthjournal.com/article/S1098-3015(12)01656-7/fulltext
- OHDSI PatientLevelPrediction GitHub: https://github.com/OHDSI/PatientLevelPrediction
- OHDSI Patient-Level Prediction workgroup: https://www.ohdsi.org/web/wiki/doku.php?id=projects:workgroups:patient-level_prediction
- DYNAMO-HIA PLOS ONE 2012: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0033317

Last reviewed: 2026-07-02.
