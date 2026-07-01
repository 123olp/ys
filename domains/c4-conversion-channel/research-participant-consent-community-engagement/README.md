# Research Participant Consent Community Engagement

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/research-participant-consent-community-engagement` |
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

`research-participant-consent-community-engagement/` 研究研究参与者同意、退出、再联系、社区参与、患者伙伴关系、信任和研究回馈，如何决定长期人体研究能否持续、合规且被主体认可。

> 核心问题：Human Infra 依赖长期人体数据、队列、样本、真实世界证据和个体反馈。若参与者不能理解、同意、退出、获知风险并参与研究目标塑造，研究基础设施会从主体持续性工具滑向数据抽取系统。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要长期人体研究、纵向数据、样本和真实世界反馈
  -> 这些研究依赖参与者同意、理解、信任、再联系、退出和社区合法性
  -> 同意失效、沟通失真和社区不信任会降低数据质量、研究留存和伦理正当性
  -> 因此研究参与者同意与社区参与是人体研究能持续运行的治理域
```

## 关注对象

- 知情同意、动态同意、撤回、再联系、二次使用、结果回馈和参与者权利。
- 社区参与、患者/公众参与、研究伙伴关系、信任建设、语言文化可达和历史不信任。
- 人体研究、队列研究、样本库、数字健康研究、基因组研究和真实世界数据研究中的参与者治理。
- 与 `governance-rights/` 的边界：治理权利域关注更宽的主体权利；本域关注研究参与者在研究基础设施中的同意、参与和退出。
- 与 `health-data-privacy-governance/` 的边界：隐私域关注敏感数据使用边界；本域关注研究关系、信任、同意和社区合法性。

## Human Infra 模型链路

```text
研究参与者同意与社区参与 T
  -> 改变理解、信任、同意质量、退出能力、再联系和结果回馈变量 X
  -> 改变长期研究、队列、样本库和真实世界数据系统的合法状态 S
  -> 改变失访、拒绝参与、伦理违规、代表性偏差和数据抽取风险 λ(t)
  -> 影响证据质量、参与者权益、长期研究可持续性和主体持续性模型可信度
```

## 非目标

- 不提供规避 IRB、弱化知情同意、诱导参与、隐瞒风险或限制退出的策略。
- 不把社区参与写成宣传包装、数据获取话术或合规表演。
- 不替代机构审查委员会、研究伦理、法律合规或社区治理判断。

## Source Signals

- HHS OHRP 45 CFR 46: https://www.hhs.gov/ohrp/regulations-and-policy/regulations/45-cfr-46/
- OHRP Informed Consent: https://www.hhs.gov/ohrp/regulations-and-policy/guidance/informed-consent/
- PCORI Engagement Rubric: https://www.pcori.org/engagement/engagement-resources/engagement-rubric
- NIH All of Us Research Program: https://www.researchallofus.org/
- NIH Genomic Data Sharing Policy: https://sharing.nih.gov/genomic-data-sharing-policy

## 下一步

- 建立研究参与者治理变量表：同意质量、退出可行性、再联系、结果回馈、社区参与和代表性。
- 与 `longitudinal-cohort-retention-followup-infrastructure/`、`biobanking-biospecimen-quality-chain-of-custody/` 和 `registries-real-world-data-governance/` 建立同意接口。
