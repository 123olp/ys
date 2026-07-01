# Health Insurance Enrollment Renewal Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/health-insurance-enrollment-renewal-continuity` |
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


## 定位

本域研究健康保险参保、续保、特殊参保期、资格通知、保费支付、Medicaid/CHIP 转换和覆盖生效如何影响主体能否持续进入医疗支付系统。

它不是保险选择、投保建议、补贴资格判断或 Marketplace 申诉代写入口。

## 先验问题

```text
医疗风险转移何以成立？
  -> 主体必须持续拥有有效覆盖
  -> 参保、续保、资格更新和保费支付必须不中断
  -> life event、收入变化、地址变化和 Medicaid/Marketplace 转换必须可处理
  -> 否则医疗服务会在支付入口前断裂
```

## 研究对象

- Marketplace open enrollment、special enrollment period、renewal、plan change 和 coverage effective date。
- Medicaid/CHIP redetermination、loss of coverage、transfer to Marketplace 和 household 信息更新。
- Premium payment、grace period、termination、reinstatement、eligibility notice 和 appeals interface。

## 关键变量

- 覆盖连续天数、失保窗口、续保完成率、保费支付失败率。
- 资格通知理解度、文件验证负担、life event 处理时长。
- Medicaid/Marketplace 转换成功率、coverage gap 和重新参保摩擦。

## 证据入口

- HealthCare.gov enrollment、renewal、special enrollment period 和 Marketplace appeal 资料。
- CMS Marketplace、Medicaid/CHIP eligibility and enrollment materials。
- State Medicaid renewal 和 unwinding 公开资料。

## 非目标

- 不提供保险计划选择、补贴资格、收入计算、税务、移民、法律或个案参保建议。
- 不代写 Marketplace、Medicaid、雇主保险或保险公司申诉材料。
- 不收集 SSN、移民身份、收入、家庭成员、保费、保险卡或账户凭证。

## 上下游

- 上游：`insurance-risk-transfer/`、`legal-identity-civil-registration/`、`household-composition-dependent-eligibility-continuity/`。
- 下游：`insurance-eligibility-benefits-verification-continuity/`、`healthcare-access-continuity/`、`financial-resilience-access/`。
