# Medicare Enrollment Coverage Transition Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/medicare-enrollment-coverage-transition-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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

- 界定外部承载条件：能源、水、食物、住房、通信、交通、治理、经济或公共基础设施。
- 说明它如何改变主体展开未来所需的稳定性、冗余、可获得性和安全边界。
- 记录基础设施依赖：供应链、地理环境、制度、资金、维护能力和公共服务。
- 识别冲击场景：灾害、战争、断供、污染、气候、系统失灵或社会支持崩溃。
- 建立韧性指标：可用率、恢复时间、冗余、成本、覆盖范围、可负担性和风险暴露。

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

`medicare-enrollment-coverage-transition-continuity` 研究 Medicare 初始参保、特殊参保期、Open Enrollment、Original Medicare、Medicare Advantage、Part D、Medigap 和从雇主保险/Medicaid/Marketplace 过渡时的覆盖连续性、延迟风险和计划切换摩擦。

## 核心问题

老年、残障或 ESRD 主体进入 Medicare 时，真正的风险不是“有没有 Medicare 这个制度”，而是参保窗口、药物覆盖、网络、补充保险、低收入补助和原有覆盖转换是否在正确时间接上。

## 对象

- Medicare eligibility、Initial Enrollment Period、General Enrollment Period、Special Enrollment Period 和 Open Enrollment。
- Original Medicare、Medicare Advantage、Part D、Medigap、Extra Help 和 dual eligibility 的覆盖接口。
- 雇主保险、retiree coverage、COBRA、Marketplace、Medicaid 与 Medicare 之间的交接风险。
- 与 `health-insurance-enrollment-renewal-continuity` 的分工：本域聚焦 Medicare 生命周期转换。

## Human Infra 价值

- 将退休、残障和慢病阶段的医疗支付连续性纳入主体长期生存与恢复模型。
- 解释参保窗口和覆盖转换如何影响药物、专科、DME、住院、账单和现金流。
- 为“有效永生”的晚年制度接口补齐一类高概率、高损失的行政断点。

## 边界

- 不提供 Medicare 计划选择、参保、换计划、Part D 药物比较、Medigap 购买、Extra Help 资格、税务、法律或财务建议。
- 不推荐 plan、broker、药房、医生、MA/Part D 产品或补充保险。
- 不判断个人是否应延迟参保、是否有罚金、是否适合某计划、是否有 SEP 或是否应申诉。
- 不收集 Medicare number、SSN、药物清单、医生名单、收入资产、保单或门户凭证。

## 上游与下游

- 上游：`health-insurance-enrollment-renewal-continuity`、`retirement-pension-savings-plan-continuity`、`social-security-earnings-benefit-record-continuity`。
- 下游：`pharmacy-benefit-formulary-prior-authorization-continuity`、`durable-medical-equipment-supplier-repair-continuity`、`claims-adjudication-eob-denial-continuity`、`long-term-care-insurance-benefit-activation-continuity`。

## 初始资料线索

- Medicare.gov get started: https://www.medicare.gov/basics/get-started-with-medicare
- Medicare.gov coverage options: https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/your-coverage-options
- Medicare.gov joining a plan: https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/joining-a-plan
