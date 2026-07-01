# Newborn Screening Result Followup Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/newborn-screening-result-followup-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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

- 界定生命载体变量：细胞、组织、器官、脑、免疫、代谢、急性风险或衰老损伤。
- 说明影响机制：修复、替换、再生、控制、筛查、预防、维持或风险降低。
- 列出可观察状态：功能指标、生物标志物、疾病终点、失能时间、恢复能力或死亡风险。
- 记录副作用、过度干预、癌变、免疫、长期安全性和尾部风险。
- 区分机制合理性、体外证据、动物证据、人体早期数据、临床终点和长期安全性。

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

新生儿筛查结果与随访连续性，关注出生后早期筛查、样本采集、实验室报告、异常结果通知、诊断确认、专科转介、家庭沟通和州级项目接口如何影响可逆风险窗口。

## 对象

- Newborn screening program interface
- Specimen collection and result routing
- Abnormal result notification and follow-up
- Confirmatory testing referral boundary
- Family communication and language access
- State program, pediatric care and specialty handoff
- Privacy and genetic information boundary

## Human Infra 价值

新生儿筛查不是单次检测，而是把出生后短暂、可逆、可能高后果的代谢、内分泌、血液、免疫或其他风险接入可通知、可确认、可转诊和可随访的公共卫生系统。该域把“早期信号是否能转成及时行动”建模为下一代主体持续性的早期基础设施。

## 边界

- 不提供筛查项目选择、筛查结果解释、遗传风险解释、诊断、治疗、喂养、药物、急诊或个体儿科建议。
- 不判断某个婴儿是否异常、是否需要复查、是否需要治疗、是否遗传风险增加或家庭成员是否需要检测。
- 不替代儿科、新生儿科、遗传咨询、州 newborn screening program、公共卫生机构、实验室、保险、语言服务或紧急服务。

## 上游与下游

- 上游：`maternal-newborn-child-development/`、`postpartum-care-recovery-follow-up-continuity/`、`healthcare-access-continuity/`。
- 下游：`well-child-visit-preventive-care-continuity/`、`children-youth-special-health-care-needs-care-coordination-continuity/`、`patient-data-interoperability/`。

## 初始资料线索

- CDC newborn screening materials.
- HRSA newborn screening and follow-up resources.
- State newborn screening program public materials.
