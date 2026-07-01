# Price Transparency Good Faith Estimate Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/price-transparency-good-faith-estimate-continuity` |
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


## 定位

本域研究 hospital price transparency、payer transparency、shoppable services、machine-readable files、good faith estimate 和 patient-provider dispute resolution 如何影响主体能否预先理解医疗成本。

它不是价格比较、机构选择、谈价策略或账单争议工具。

## 先验问题

```text
医疗成本可预期何以成立？
  -> 服务价格和预期费用必须在服务前可发现
  -> 价格资料必须可读、可比、可解释并与实际账单有关系
  -> 估算与最终账单差异必须有争议处理边界
  -> 否则主体无法把医疗决策纳入资源规划
```

## 研究对象

- Hospital Price Transparency、Transparency in Coverage、machine-readable files 和 shoppable services。
- Good Faith Estimate、uninsured/self-pay estimate、item/service charges 和 facility/provider fees。
- Patient-provider dispute resolution、estimate-to-bill mismatch 和 estimator tools。

## 关键变量

- 价格资料完整性、可读性、可发现性、标准化程度和更新频率。
- Estimate accuracy、bill-estimate variance、dispute eligibility 和 response time。
- 主体预期成本、延迟治疗、放弃服务和财务计划能力。

## 证据入口

- CMS Hospital Price Transparency 和 Medical Bill Rights / Good Faith Estimate 资料。
- Transparency in Coverage rule 和 payer price transparency resources。
- CMS enforcement updates、health economics 和价格透明度研究。

## 非目标

- 不提供机构价格排名、provider 选择、检查/手术选择、账单争议、谈价或医疗建议。
- 不抓取、规避或滥用价格文件，不构建个体价格套利或机构规避工具。
- 不收集 estimate、bill、insurance、diagnosis、CPT/ICD 或个人财务资料。

## 上下游

- 上游：`health-economics-value-assessment/`、`insurance-eligibility-benefits-verification-continuity/`。
- 下游：`patient-billing-payment-plan-continuity/`、`surprise-billing-balance-bill-protection-continuity/`。
