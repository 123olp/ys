# Income Payroll Employment Record Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/income-payroll-employment-record-continuity` |
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

Income Payroll Employment Record Continuity 关注工资、工时、雇佣记录、收入证明、薪资单、工资报表和雇佣核验如何让主体把劳动时间持续转化为收入、信用、租房、福利、贷款、税务和社会保险权益。

## 对象

- 工资、薪资单、工时记录、雇佣证明、工资报表、工资支付频率、扣缴记录、工资错误、记录保存和更正机制。
- 雇主、雇员、独立承包、工资系统、payroll providers、employment verification services 和政府工资工时监管机构。
- 收入证明在住房、信贷、福利、税务、医疗补助、失业保险、退休权益和身份核验中的跨系统使用。

## Human Infra 价值

```text
主体通过劳动换取收入和未来权益
-> 工资、工时和雇佣记录是劳动被制度承认的证据
-> 记录缺失、错误或不可携带会削弱收入证明、福利资格、税务记录、信用和退休权益
-> 可访问、可纠错、可核验的工资与雇佣记录降低跨系统证明成本
-> 主体更容易把过去劳动转化为当前资源、未来保障和长期行动能力
```

## 边界

- 本域不提供工资索赔、劳动仲裁、税务申报、雇佣分类、薪资系统部署、背景调查、贷款、租房、福利申请或法律建议。
- 不帮助制造、修改、伪造、隐瞒或规避工资、工时、收入、雇佣或扣缴记录。
- 不判断某个人的雇佣状态、工资合法性、申诉胜率、税务责任或福利资格。
- 只整理公开规则、记录机制、证明链路、纠错入口、数据可携带性、隐私风险和制度边界。

## 上游与下游

- 上游：`labor-rights-workplace-protection/`、`workforce-employment-services/`、`financial-inclusion-payment-systems/`、`digital-identity-security/`。
- 下游：`tax-administration-filing-record-continuity/`、`social-security-earnings-benefit-record-continuity/`、`unemployment-insurance-wage-record-continuity/`、`retirement-pension-savings-plan-continuity/`、`tenant-screening-rental-access-continuity/`。

## 初始资料线索

- U.S. Department of Labor Wage and Hour Division wage, hour and worker protection resources.
- IRS wage and income transcript and tax record access resources.
- SSA earnings record and Social Security Statement resources.
- Payroll recordkeeping, employment verification, wage theft, worker classification and income-proof literature.
