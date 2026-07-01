# 家庭组成、受扶养人与资格关系连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/household-composition-dependent-eligibility-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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


本域研究 household、受扶养人、共同居住、照护关系、亲属关系和申报单位如何影响税务、健康保险、福利、学校、住房、托育和社会服务资格。它关注家庭事实如何被制度建模，不提供个人报税、福利、保险或家庭法建议。

## 研究对象

- household composition、tax dependents、coverage household、benefit household 和服务资格单位。
- 共同居住、主要照护者、受扶养人、监护安排、共享费用和家庭收入计算。
- IRS、HealthCare.gov、Medicaid/SNAP/TANF、学校、住房、保险和托育系统中的 household 定义差异。
- 家庭变化、分居、离婚、再婚、监护变化、寄养、大学生、老年照护和多代同堂场景。

## 价值链路

```text
资源资格不是只由个人决定
  -> 许多制度先把人放进 household、受扶养人或照护关系模型
  -> 家庭组成决定收入计算、责任归属、保险覆盖、福利资格和服务入口
  -> 家庭事实变化或系统定义不一致会导致错误拒绝、错误支付、覆盖断裂或追缴风险
  -> 家庭组成连续性把关系事实转化为可审查的资源资格底座
```

## 关键问题

- 不同制度如何定义 household、dependent、coverage family 和 benefit unit？
- 家庭组成变化如何影响医疗覆盖、税务抵免、公共福利、学校和住房资格？
- household 变量如何连接资源分配、责任归属、照护角色和行政负担？
- 如何避免把家庭关系建模简化为个体失败、福利欺诈假设或家庭监控？

## 上游与下游

- 上游：`vital-records-life-event-continuity/`、`family-law-custody-child-support-continuity/`、`kinship-foster-adoption-care-continuity/`、`childcare-family-continuity/`。
- 下游：`tax-administration-filing-record-continuity/`、`social-protection-benefits-delivery/`、`healthcare-access-continuity/`、`insurance-risk-transfer/`、`public-benefits-eligibility-automated-decision-continuity/`。

## 非目标

- 不提供个人税务申报、dependent claim、健康保险 household、Medicaid/SNAP/TANF、住房、学校或托育资格判断。
- 不判断谁能申报谁、谁应计入 household、谁有监护权、谁应支付费用或谁应取得福利。
- 不协助福利欺诈、虚假申报、规避追缴、隐瞒家庭成员、逃避抚养责任或操纵资格规则。

## 初始资料入口

- IRS: Dependents
- HealthCare.gov: Household size and income
- Medicaid, SNAP, TANF, school and housing program official rules
- State/local benefits eligibility official resources
