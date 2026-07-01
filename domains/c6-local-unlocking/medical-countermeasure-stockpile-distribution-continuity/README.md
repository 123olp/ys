# Medical Countermeasure Stockpile Distribution Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/medical-countermeasure-stockpile-distribution-continuity` |
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

`medical-countermeasure-stockpile-distribution-continuity/` 研究医疗对策、战略储备、POD 分发、抗病毒药、治疗药物、PPE、供应分配和公平可达如何支撑暴发响应。

> 核心问题：药物、疫苗、PPE 和治疗技术只有经过储备、分发、分配和可达接口，才会从库存变成主体持续性的真实输入。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 暴发响应依赖医疗对策和关键物资
  -> 医疗对策从库存到个体之间存在分发、分配、冷链、处方、转介和公平摩擦
  -> 储备与分发连续性决定技术能力能否在时间窗口内转化为风险下降
```

## 关注对象

- Strategic National Stockpile、医疗对策、POD、抗病毒药、治疗药物、PPE、冷链、分配优先级、物流、可及性和公平。
- 与 `pharmaceutical-quality-supply-integrity/` 的关系：药品质量供应域关注常规药品完整性；本域关注暴发医疗对策的储备与分发执行。

## Human Infra 模型链路

```text
医疗对策储备与分发
  -> 改变关键药品、疫苗、PPE、诊断和治疗资源到达速度
  -> 改变暴发中的重症、死亡、医疗挤兑和工作学校中断风险
  -> 降低技术存在但主体无法获得的落差
  -> 增强健康寿命、恢复能力和主体持续性
```

## 非目标

- 不提供药品选择、剂量、处方、个人囤货、购买渠道、治疗建议、PPE 操作或分配优先级规避。
- 不提供库存位置、配送路径、设施安全、抢占资源、假药渠道或监管规避信息。
- 不替代医疗、药事、公共卫生或供应链专业判断。

## Source Signals

- ASPR Strategic National Stockpile: https://aspr.hhs.gov/SNS/
- CDC medical countermeasures and POD resources: https://www.cdc.gov/orr/readiness/mcm.html
- FDA emergency use authorizations: https://www.fda.gov/emergency-preparedness-and-response/mcm-legal-regulatory-and-policy-framework/emergency-use-authorization
- HHS public health emergency resources: https://aspr.hhs.gov/

## 下一步

- 建立变量表：库存、POD、分发时滞、冷链、优先级、公平可达、供应瓶颈、药品质量和不良事件反馈。
- 与 `healthcare-surge-triage-capacity-continuity/`、`vaccination-campaign-booster-delivery-continuity/` 和 `pharmaceutical-quality-supply-integrity/` 建立接口。
