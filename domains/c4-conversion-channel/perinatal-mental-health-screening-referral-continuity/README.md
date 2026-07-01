# Perinatal Mental Health Screening Referral Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/perinatal-mental-health-screening-referral-continuity` |
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


围产期心理健康筛查与转介连续性，关注怀孕至产后期间的抑郁、焦虑、创伤、强迫症状、物质使用、亲密伴侣暴力、危机入口、筛查工具、转介闭环、保险和同伴支持边界。

## 对象

- Perinatal depression and anxiety screening
- Referral and treatment access pathway
- Crisis and emergency boundary
- Trauma, substance use and IPV screening interface
- Insurance, language and culturally safe care
- Peer support and community programs
- Follow-up closure and warm handoff

## Human Infra 价值

围产期心理健康会影响睡眠、判断、照护、亲子关系、工作学习、身体恢复和危机风险。该域把“心理风险是否被发现、转接并持续跟进”建模为主体和下一代持续性的关键恢复系统。

## 边界

- 不提供诊断、量表解释、治疗、药物、自伤/他伤判断、危机干预、家庭暴力处置、物质使用治疗、亲子风险判断或个体心理建议。
- 不判断个人是否有产后抑郁、焦虑、精神病、创伤、成瘾、家庭暴力风险或儿童安全风险。
- 不替代心理健康专业人员、OB/GYN、pediatrics、crisis hotline、IPV advocate、substance-use treatment、儿童保护、律师或紧急服务。

## 上游与下游

- 上游：`prenatal-care-access-risk-screening-continuity/`、`postpartum-care-recovery-follow-up-continuity/`、`pregnancy-loss-stillbirth-bereavement-continuity/`。
- 下游：`maternal-newborn-child-development/`、`suicide-crisis-response-continuity/`、`family-caregiver-respite-work-continuity/`。

## 初始资料线索

- ACOG perinatal mental health screening guidance.
- HRSA maternal mental health resources.
- SAMHSA and National Maternal Mental Health Hotline resources.
