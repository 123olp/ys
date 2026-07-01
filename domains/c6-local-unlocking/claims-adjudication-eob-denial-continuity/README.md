# Claims Adjudication EOB Denial Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/claims-adjudication-eob-denial-continuity` |
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

本域研究医疗 claim 提交、adjudication、EOB、payer denial、coordination of benefits、resubmission、appeal window 和 denial reason 如何影响服务发生后的支付闭环。

它不是理赔申诉、账单争议、编码优化或拒付对抗工具。

## 先验问题

```text
医疗服务完成后如何不变成债务？
  -> claim 必须被正确提交和 adjudicate
  -> EOB 必须把 payer payment、adjustment 和 patient responsibility 讲清楚
  -> denial reason、resubmission 和 appeal window 必须可追踪
  -> 否则服务完成后仍会转化为账单、债务和行政负担
```

## 研究对象

- Claim submission、clearinghouse、payer adjudication、EOB、ERA/EFT 和 claim status。
- Denial reason、coordination of benefits、secondary payer、timely filing 和 appeal deadline。
- Coding mismatch、medical necessity denial、eligibility denial、network denial 和 duplicate claim。

## 关键变量

- Claim acceptance、denial rate、days in adjudication、EOB clarity。
- Appeal / resubmission rate、denial reversal、timely filing failure。
- Patient responsibility mismatch、provider-payer correction workload。

## 证据入口

- CMS claims、Medicare appeals and grievances、HIPAA transaction standards。
- X12 claim / remittance standards、CAQH CORE operating rules。
- KFF、AHRQ、Health Affairs 医疗理赔和拒付研究。

## 非目标

- 不解释个人 EOB、claim、denial、billing code、legal deadline 或 payer decision。
- 不代写 claim appeal、grievance、provider dispute、编码说明或法律信。
- 不提供 upcoding、unbundling、虚假材料、规避审核或欺诈策略。

## 上下游

- 上游：`medical-service-prior-authorization-utilization-management-continuity/`、`insurance-eligibility-benefits-verification-continuity/`。
- 下游：`patient-billing-payment-plan-continuity/`、`charity-care-financial-assistance-medical-debt-continuity/`。
