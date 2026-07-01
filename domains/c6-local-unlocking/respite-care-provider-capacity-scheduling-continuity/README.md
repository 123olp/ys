# Respite Care Provider Capacity Scheduling Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/respite-care-provider-capacity-scheduling-continuity` |
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

`respite-care-provider-capacity-scheduling-continuity/` 研究 respite care、临时替代照护、provider capacity、排班、等待、费用和服务中断如何影响家庭照护者恢复、工作连续性和被照护者安全。

> 核心问题：喘息服务不是“可有可无的休息”，而是防止家庭照护者被长期责任耗尽的恢复基础设施。没有可预约、可信任、可负担的替代照护，照护系统会把风险转嫁给单个家庭成员。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 家庭照护者也需要睡眠、工作、就医、恢复和社会参与
  -> 被照护者同时需要替代照护期间的安全、尊严和连续支持
  -> respite capacity 和 scheduling 决定照护负担能否被周期性卸载
```

## 关注对象

- In-home respite、out-of-home respite、overnight respite、emergency respite 和 planned respite。
- 服务容量、等待时间、预约、取消、替代人员、费用、交通和信任边界。
- 照护者睡眠、工作、健康、社交隔离、照护质量和危机迁移。
- 与 `family-caregiver-respite-work-continuity/` 的关系：本域专门承载 respite 供给与排班执行层。

## Human Infra 模型链路

```text
Respite service capacity
  -> 改变替代照护可预约性、时长、可靠性、费用和信任
  -> 改变照护者恢复、工作、就医和被照护者安全状态
  -> 降低照护者耗竭、虐待/忽视风险、急诊迁移和过早机构化风险
  -> 增加家庭照护系统的可持续性
```

## 非目标

- 不推荐 respite provider、机构、时长、场景、路线、费用或个人安排。
- 不判断资格、支付、Medicaid waiver、NFCSP、Lifespan Respite 或保险覆盖。
- 不制定照护交接清单、护理任务、行为支持、药物或安全监督方案。
- 不收集照护者、被照护者、住址、日程、健康、行为或支付资料。

## Source Signals

- ACL Lifespan Respite Care Program: https://acl.gov/programs/support-caregivers/lifespan-respite-care-program
- ACL National Family Caregiver Support Program: https://acl.gov/programs/support-caregivers/national-family-caregiver-support-program
- NIA Caregiving: https://www.nia.nih.gov/health/caregiving
- Eldercare Locator: https://eldercare.acl.gov/

## 下一步

- 建立 respite 变量表：容量、等待、取消、信任、服务时长、费用、替代人员和危机 respite。
- 整理 ACL、NIA、state respite coalitions 和 caregiver support Source Cards。
