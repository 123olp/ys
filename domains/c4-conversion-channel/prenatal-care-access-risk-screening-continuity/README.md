# Prenatal Care Access Risk Screening Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/prenatal-care-access-risk-screening-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
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

产前照护接入与风险筛查连续性，关注怀孕确认、产前照护入口、风险筛查、实验室检查、影像检查、转诊、交通、保险、语言和随访闭环如何影响孕产主体与胎儿/新生儿的持续性。

## 对象

- Prenatal care access and appointment continuity
- Pregnancy confirmation and entry timing
- Risk screening and referral handoff
- Laboratory / ultrasound follow-up
- Transportation, language, insurance and scheduling barriers
- High-risk pregnancy referral boundary
- Documentation and privacy boundary

## Human Infra 价值

产前照护不是单次医疗行为，而是把风险发现、信息解释、转诊、准备、营养、感染预防、慢病控制和分娩计划接入连续系统。该域把“怀孕期间能否持续被看见、被筛查、被转接”建模为主体持续性和下一代主体形成的前置条件。

## 边界

- 不提供怀孕确认、产前检查频率、筛查结果解释、药物、营养、影像、分娩方式、医院选择或个体医疗建议。
- 不判断个人妊娠风险、胎儿风险、是否高危、是否需要转诊、是否需要急诊或某项检查是否必要。
- 不替代 OB/GYN、midwife、primary care、MFM、公共卫生机构、保险、交通、语言服务或紧急服务。

## 上游与下游

- 上游：`reproductive-fertility-continuity/`、`health-insurance-enrollment-renewal-continuity/`、`healthcare-access-continuity/`。
- 下游：`obstetric-emergency-hemorrhage-hypertension-continuity/`、`postpartum-care-recovery-follow-up-continuity/`、`maternal-newborn-child-development/`。

## 初始资料线索

- CDC maternal health and pregnancy materials.
- HRSA maternal health and prenatal service access materials.
- ACOG prenatal care and perinatal care guidance.
