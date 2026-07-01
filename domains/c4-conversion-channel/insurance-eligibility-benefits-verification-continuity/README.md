# Insurance Eligibility Benefits Verification Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/insurance-eligibility-benefits-verification-continuity` |
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

## 定位

本域研究保险资格、coverage active 状态、benefits verification、cost-sharing、deductible、out-of-pocket maximum、network status 和 coverage limitations 如何在服务发生前被核验。

它不是保险权益解释、个案费用预测、provider 选择或保险争议建议入口。

## 先验问题

```text
医疗服务可支付何以成立？
  -> 覆盖状态必须可核验
  -> 权益、网络、费用分担和限制必须可被服务方与主体理解
  -> 保险信息必须在预约、检查、治疗和账单系统之间一致
  -> 否则服务会在资格核验或费用分担处失败
```

## 研究对象

- Eligibility and benefits verification、coverage active status、subscriber/dependent relationship。
- Deductible、copay、coinsurance、out-of-pocket maximum、benefit limits 和 exclusions。
- In-network / out-of-network status、payer-provider contract、real-time eligibility 和 clearinghouse。

## 关键变量

- 资格核验准确率、信息延迟、网络状态错误率和 coverage mismatch。
- 费用分担可理解度、benefit limit 触发率、eligibility denial。
- 服务发生前后保险信息一致性和人工纠错负担。

## 证据入口

- CMS 和 payer interoperability / eligibility 相关资料。
- CAQH CORE eligibility and benefits standards。
- CMS care compare、plan documents、summary of benefits and coverage 资料。

## 非目标

- 不解释个人 benefits、deductible、network、coverage、claim 或 bill。
- 不推荐 insurance plan、network、provider、facility 或服务路径。
- 不收集保险卡、member ID、病历、诊断、claim、账单或个人财务资料。

## 上下游

- 上游：`health-insurance-enrollment-renewal-continuity/`、`provider-directory-network-adequacy-continuity/`。
- 下游：`medical-service-prior-authorization-utilization-management-continuity/`、`claims-adjudication-eob-denial-continuity/`。
