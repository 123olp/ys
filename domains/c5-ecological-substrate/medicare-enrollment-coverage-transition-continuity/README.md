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
