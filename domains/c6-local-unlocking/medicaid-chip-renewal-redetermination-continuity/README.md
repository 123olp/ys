# Medicaid CHIP Renewal Redetermination Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/medicaid-chip-renewal-redetermination-continuity` |
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

`medicaid-chip-renewal-redetermination-continuity` 研究 Medicaid/CHIP 资格续期、redetermination、ex parte renewal、通知、资料请求、coverage transition 和儿童/家庭覆盖断点如何影响医疗支付入口、治疗连续性、家庭现金流和未来选择权。

## 核心问题

Medicaid/CHIP 的断点常常不是疾病本身，而是资格数据、地址、通知、续期材料、系统匹配和州级流程失败。主体一旦失保，处方、检查、慢病管理、儿童预防照护和家庭预算都会被同步冲击。

## 对象

- Medicaid/CHIP eligibility、annual renewal、redetermination、ex parte renewal 和资料请求。
- 通知送达、语言可及、地址更新、家庭收入变化、儿童/孕产/残障/老年资格类别。
- Medicaid、CHIP、Marketplace、雇主保险和 Medicare 之间的 coverage transition。
- 与 `health-insurance-enrollment-renewal-continuity` 的分工：本域专注 Medicaid/CHIP 公共覆盖续期执行。

## Human Infra 价值

- 把医疗支付入口视为治疗连续性和主体恢复能力的前置条件。
- 揭示行政续期如何决定慢病控制、儿童筛查、药物供应和医疗债务风险。
- 为“主体持续性最大化”补齐公共医保资格维护的高摩擦环节。

## 边界

- 不提供 Medicaid/CHIP 资格判断、申请、续期、申诉、补贴、收入计算、移民、税务或法律建议。
- 不代写表格、证明、appeal、grievance、coverage transition 或州级机构沟通材料。
- 不收集 SSN、Medicaid ID、收入、税表、住址、家庭成员、医疗记录、移民身份或门户凭证。

## 上游与下游

- 上游：`health-insurance-enrollment-renewal-continuity`、`public-benefits-eligibility-automated-decision-continuity`、`administrative-burden-procedural-friction`。
- 下游：`retail-pharmacy-prescription-dispensing-continuity`、`primary-care-panel-appointment-access-continuity`、`claims-adjudication-eob-denial-continuity`、`preventive-care-screening-continuity`。

## 初始资料线索

- Medicaid.gov eligibility: https://www.medicaid.gov/medicaid/eligibility/index.html
- Medicaid.gov renewals: https://www.medicaid.gov/medicaid/eligibility/renewals/index.html
- Medicaid.gov CHIP eligibility: https://www.medicaid.gov/chip/eligibility/index.html
