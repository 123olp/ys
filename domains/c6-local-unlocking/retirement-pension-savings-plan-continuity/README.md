# Retirement Pension Savings Plan Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/retirement-pension-savings-plan-continuity` |
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

Retirement Pension Savings Plan Continuity 关注雇主退休计划、养老金、401(k)、IRA、rollover、受益人、计划披露、缴费记录、vesting、丢失账户、计划终止和养老金保障如何支撑主体在劳动退出后的长期资源连续性。

## 对象

- Defined benefit pensions、defined contribution plans、401(k)、IRA、rollovers、vesting、plan statements、beneficiaries、fees、plan termination、lost accounts 和 pension guarantees。
- 雇主、计划管理人、recordkeepers、custodians、监管机构、PBGC、税务机构和个人账户访问机制。
- 退休资产、账户转移、计划文件、受益人信息、缴费历史和老年收入风险之间的关系。

## Human Infra 价值

```text
主体会逐步离开劳动收入窗口
-> 退休计划和养老金记录把工作期资源沉淀为未来生活资金
-> 账户遗失、计划终止、受益人错误、费用不透明或转移失败会削弱老年行动能力
-> 可追踪、可携带、可纠错、可保护的退休记录降低劳动退出后的资源断裂
-> 主体在衰老、失能、照护和长寿风险中保留更长的可持续选择窗口
```

## 边界

- 本域不提供投资、资产配置、rollover、税务、退休时间、受益人、理财、ERISA、养老金申诉或法律建议。
- 不判断任何账户、计划、投资、费用、退休策略、领取方式或受益安排是否适合个人。
- 不帮助规避税务、隐藏资产、伪造计划文件、冒领养老金、绕过身份核验或操纵账户。
- 只整理公开计划类型、记录机制、监管边界、可携带性、丢失账户、计划终止、保障机制和风险。

## 上游与下游

- 上游：`income-payroll-employment-record-continuity/`、`social-security-earnings-benefit-record-continuity/`、`tax-administration-filing-record-continuity/`、`financial-fiduciary-power-of-attorney-continuity/`。
- 下游：`caregiving-long-term-care/`、`home-health-hospice-palliative-care-continuity/`、`trust-estate-affairs-succession-continuity/`、`financial-resilience-access/`。

## 初始资料线索

- U.S. Department of Labor Employee Benefits Security Administration worker and family retirement resources.
- PBGC pension plan and unclaimed benefits resources.
- IRS retirement plan resources.
- Retirement security, pension administration, rollover, lost account and pension guarantee literature.
