# Intensive Care Organ Support Delirium Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/intensive-care-organ-support-delirium-continuity` |
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

`intensive-care-organ-support-delirium-continuity/` 研究 ICU 多器官支持、镇静、谵妄、早期活动、家属参与、感染控制和 ICU 后综合征如何影响危重病后的主体连续性。

> 核心问题：ICU 不只是“活下来”的机器房。危重病后的认知、肌力、精神状态和家庭功能决定存活是否能转回有效时间。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体可能进入多器官失效或生命支持状态
  -> ICU 可延长生存窗口，但也可能带来谵妄、虚弱、感染和长期认知功能损伤
  -> 存活收益必须扣除 ICU 后综合征、恢复成本和主体能力损失
  -> 因此 ICU 器官支持与谵妄治理是“活下来能否继续行动”的关键域
```

## 关注对象

- ICU capacity、organ support、ABCDE/ABCDEF bundle、pain/agitation/delirium、sedation、mobilization、family engagement、post-intensive care syndrome。
- 与 `sepsis-shock-early-recognition-resuscitation-continuity/` 的关系：脓毒症常进入 ICU 多器官支持。
- 与 `delirium-acute-cognitive-failure-prevention/` 的边界：谵妄域关注认知失败机制；本域关注 ICU 场景下的多系统支持和恢复。

## Human Infra 模型链路

```text
ICU 器官支持与谵妄治理 T
  -> 改变器官支持、镇静、活动、感染控制、家属参与和恢复变量 X
  -> 改变危重病存活、认知、肌力、心理和家庭支持状态 S
  -> 改变 ICU 死亡、长期虚弱、谵妄后认知损害和再入院风险 λ(t)
  -> 影响主体有效时间、恢复能力和长期行动资格
```

## 非目标

- 不提供 ICU 治疗、镇静、呼吸机、营养、感染、转院、撤机、预后或家属决策建议。
- 不生成 ICU checklist、医嘱、床位策略、个案病情解释或替代临床团队的判断。
- 不收集 ICU 病历、生命体征、用药、设备参数、家属资料或敏感医疗数据。

## Source Signals

- SCCM ICU Liberation: https://www.sccm.org/clinical-resources/iculiberation-home
- SCCM PADIS Guidelines: https://www.sccm.org/clinical-resources/guidelines/guidelines/padis-guidelines
- NIH post-intensive care syndrome overview: https://www.nhlbi.nih.gov/health/respiratory-failure/after

## 下一步

- 建立 ICU Continuity Card：organ support, delirium, sedation, mobilization, family engagement, infection risk, PICS outcome。
- 与 `mechanical-ventilation-respiratory-failure-continuity/`、`ecmo-extracorporeal-life-support-continuity/` 和 `delirium-acute-cognitive-failure-prevention/` 建立接口。
