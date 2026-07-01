# Autoimmune Rheumatic Disease Inflammatory Burden Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/autoimmune-rheumatic-disease-inflammatory-burden-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

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

`autoimmune-rheumatic-disease-inflammatory-burden-continuity/` 研究类风湿关节炎、狼疮等自身免疫/风湿病、慢性炎症、免疫抑制、器官损害和照护连续性如何影响主体持续性。

> 核心问题：自身免疫风湿病不是单一关节问题，而是长期炎症、疲劳、疼痛、器官风险、免疫抑制和医疗监测共同塑造的主体能力损耗系统。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要免疫系统既能防御又不持续攻击自身组织
  -> 自身免疫风湿病会造成炎症、疼痛、疲劳、器官损害和治疗风险
  -> 结果取决于早诊、疾病活动控制、药物监测、感染预防和多专科协作
  -> 因此自身免疫风湿病是免疫稳态和长期功能连续性的关键维护域
```

## 关注对象

- Rheumatoid arthritis、systemic lupus erythematosus、autoimmune rheumatic disease、disease activity、fatigue、immunosuppression, organ involvement, flare prevention, care continuity。
- 与 `immune-maintenance/` 的边界：该域关注免疫维护总机制；本域聚焦自身免疫风湿病的炎症负担和照护连续性。
- 与 `chronic-infectious-disease-care-continuity/` 的关系：免疫抑制会改变感染风险、疫苗策略和长期监测需求。

## Human Infra 模型链路

```text
自身免疫风湿病照护连续系统 T
  -> 改变疾病活动、炎症、疼痛、疲劳、药物监测、感染风险和器官保护变量 X
  -> 改变移动能力、认知疲劳、工作参与、急性 flare 和医疗负担状态 S
  -> 改变失能风险、器官衰竭风险、感染风险和有效时间损耗 λ(t)
  -> 影响主体长期行动能力、恢复能力和未来选择权
```

## 非目标

- 不提供个人自身免疫诊断、化验判读、药物、免疫抑制、疫苗、妊娠、感染处理、器官监测或 flare 处理建议。
- 不生成治疗计划、用药调整、补充剂、饮食、检查周期、残障或保险判断。
- 不收集个案化验、影像、药物、生育、感染、工作或保险资料。

## Source Signals

- NIAMS rheumatoid arthritis: https://www.niams.nih.gov/health-topics/rheumatoid-arthritis
- NIAMS lupus: https://www.niams.nih.gov/health-topics/lupus
- CDC arthritis information: https://www.cdc.gov/arthritis/

## 下一步

- 建立 Autoimmune Inflammatory Burden Card：disease activity, fatigue, organ involvement, immunosuppression, infection risk, care continuity。
- 与 `immune-maintenance/`、`pharmacovigilance-drug-safety-monitoring/` 和 `multimorbidity-polypharmacy-care-coordination/` 建立接口。
