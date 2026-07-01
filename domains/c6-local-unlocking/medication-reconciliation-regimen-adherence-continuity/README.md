# Medication Reconciliation Regimen Adherence Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/medication-reconciliation-regimen-adherence-continuity` |
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

## 定位

本域研究用药核对、药历一致性、过渡期 medication reconciliation、服药计划、依从性、治疗负担和多药协调如何决定药品是否被主体正确、持续、可承受地使用。

它不是个体用药管理、停药、加药、剂量调整或健康建议入口。

## 先验问题

```text
药物进入家庭后何以继续有效？
  -> 用药清单必须准确
  -> 多个医生、药房和照护者必须共享一致药历
  -> 主体必须能按计划执行并处理漏服、冲突和副作用信号
  -> 否则药物可得性会退化为混乱和风险
```

## 研究对象

- Medication reconciliation、处方变更、出院用药、转诊和长期照护交接。
- 依从性、持药天数、refill gap、pill burden、复杂给药频率。
- 照护者、药师、电子药历、药盒、提醒和用药教育。
- 多病共存、多重用药、治疗负担和 deprescribing 研究边界。

## 关键变量

- 药历一致率、用药差错、PDC/MPR、refill gap、漏服率。
- 过渡期用药冲突、重复治疗、禁忌组合和未说明停药。
- 治疗负担、日常执行成本、照护者参与和理解度。

## 证据入口

- AHRQ medication reconciliation 与 patient safety 资料。
- CDC、FDA、ISMP 和药学组织的 medication safety 公开资料。
- 多病共存、多重用药和依从性研究。

## 非目标

- 不提供具体服药时间、剂量、漏服处理、停药、替换或药物相互作用判断。
- 不生成个人 medication list、药历、处方核对表或照护计划。
- 不收集药名、剂量、诊断、处方、药房、医生、照护者或健康数据。

## 上下游

- 上游：`retail-pharmacy-prescription-dispensing-continuity/`、`care-transitions-discharge-continuity/`、`multimorbidity-polypharmacy-care-coordination/`。
- 下游：`patient-safety-organizational-learning/`、`pharmacovigilance-drug-safety-monitoring/`、`time-allocation-effective-time/`。
