# Prenatal Care Access Risk Screening Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/prenatal-care-access-risk-screening-continuity` |
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


产前照护接入与风险筛查连续性，关注怀孕确认、产前照护入口、风险筛查、实验室检查、影像检查、转诊、交通、保险、语言和随访闭环如何影响孕产主体与胎儿/新生儿的持续性。

## 对象

- Prenatal care access and appointment continuity
- Pregnancy confirmation and entry timing
- Risk screening and referral handoff
- Laboratory / ultrasound follow-up
- Transportation, language, insurance and scheduling barriers
- High-risk pregnancy referral boundary
- Documentation and privacy boundary

## Human Infra 价值

产前照护不是单次医疗行为，而是把风险发现、信息解释、转诊、准备、营养、感染预防、慢病控制和分娩计划接入连续系统。该域把“怀孕期间能否持续被看见、被筛查、被转接”建模为主体持续性和下一代主体形成的前置条件。

## 边界

- 不提供怀孕确认、产前检查频率、筛查结果解释、药物、营养、影像、分娩方式、医院选择或个体医疗建议。
- 不判断个人妊娠风险、胎儿风险、是否高危、是否需要转诊、是否需要急诊或某项检查是否必要。
- 不替代 OB/GYN、midwife、primary care、MFM、公共卫生机构、保险、交通、语言服务或紧急服务。

## 上游与下游

- 上游：`reproductive-fertility-continuity/`、`health-insurance-enrollment-renewal-continuity/`、`healthcare-access-continuity/`。
- 下游：`obstetric-emergency-hemorrhage-hypertension-continuity/`、`postpartum-care-recovery-follow-up-continuity/`、`maternal-newborn-child-development/`。

## 初始资料线索

- CDC maternal health and pregnancy materials.
- HRSA maternal health and prenatal service access materials.
- ACOG prenatal care and perinatal care guidance.
