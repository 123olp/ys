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
