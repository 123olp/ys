# Delirium Acute Cognitive Failure Prevention

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/delirium-acute-cognitive-failure-prevention` |
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

`delirium-acute-cognitive-failure-prevention/` 研究谵妄、急性意识和注意障碍、住院/ICU 认知失败、术后认知风险和可预防诱因，如何影响 Human Infra 的短期主体连续性和长期认知轨迹。

> 核心问题：主体不是只会慢慢衰退，也可能在感染、手术、ICU、药物、睡眠剥夺或环境压力下快速失去注意、定向、判断和沟通能力。谵妄是“急性主体失联”的典型医学形态。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须在疾病、住院、手术和 ICU 中保持可感知、可沟通、可判断
  -> 谵妄会急性破坏注意、意识、定向和决策能力，并增加长期认知和死亡风险
  -> 若诱因识别、睡眠、疼痛、药物、活动、感官辅助和环境支持失败，治疗系统会反向制造认知损害
  -> 因此谵妄预防是医疗系统中的急性认知连续性域
```

## 关注对象

- ICU 谵妄、住院谵妄、术后谵妄、感染/药物/睡眠/疼痛/感官剥夺相关认知失败。
- CAM-ICU、PADIS 指南、ABCDEF bundle、早期活动、镇静策略、睡眠、家属参与和长期认知结果。
- 与 `dementia-cognitive-decline-care-continuity/` 的边界：痴呆域关注慢性认知下降；本域关注急性、波动性、可预防的认知失败。
- 与 `surgical-anesthesia-perioperative-safety/` 的边界：围手术域关注手术麻醉安全；本域关注谵妄作为跨场景急性主体失联。

## Human Infra 模型链路

```text
谵妄预防 T
  -> 改变镇静、疼痛、睡眠、感染、药物负担、活动、感官输入和环境支持变量 X
  -> 改变注意、意识、定向、沟通、决策和长期认知状态 S
  -> 改变住院并发症、长期认知损害、死亡、照护负担和主体失联风险 λ(t)
  -> 影响有效时间、医疗决策能力、恢复速度和主体连续性
```

## 非目标

- 不提供谵妄诊断、用药、镇静调整、ICU 治疗方案或个体照护计划。
- 不替代医生、护士、药师、ICU 团队、麻醉团队或照护机构流程。
- 不把筛查工具、家属观察或单项行为表现写成个人诊断。

## Source Signals

- SCCM PADIS Guidelines: https://www.sccm.org/Clinical-Resources/Guidelines/Guidelines/Pain-Agitation-Delirium-Immobility-and-Sleep-Disruption
- ICU Liberation ABCDEF Bundle: https://www.sccm.org/Clinical-Resources/ICULiberation-Home/ABCDEF-Bundles
- NIA Delirium: https://www.nia.nih.gov/health/what-delirium
- NICE Delirium guideline: https://www.nice.org.uk/guidance/cg103

## 下一步

- 建立谵妄变量表：诱因、镇静、疼痛、睡眠、药物、感染、感官输入、活动、环境、筛查和长期结局。
- 与 `patient-safety-organizational-learning/`、`surgical-anesthesia-perioperative-safety/`、`sleep-circadian-recovery/` 和 `dementia-cognitive-decline-care-continuity/` 建立接口。
