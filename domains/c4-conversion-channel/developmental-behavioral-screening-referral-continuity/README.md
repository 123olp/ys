# Developmental Behavioral Screening Referral Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/developmental-behavioral-screening-referral-continuity` |
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


发育行为筛查与转介连续性，关注 developmental monitoring、behavioral screening、家庭观察、筛查工具接口、转介、早期干预、语言文化可及和随访闭环如何影响儿童学习与执行能力形成。

## 对象

- Developmental monitoring and surveillance
- Behavioral and developmental screening interface
- Caregiver observations and communication
- Referral to early intervention or specialist evaluation
- Language, culture, disability and access barriers
- Follow-up closure and service navigation
- Privacy and child data boundary

## Human Infra 价值

儿童发育行为筛查的价值不在于给儿童贴标签，而在于让语言、运动、认知、社交、行为和家庭压力信号尽早进入可解释、可转接、可支持的系统。该域把“早发现和早转接”建模为未来学习轮次、关系能力和自我维护能力的前置条件。

## 边界

- 不提供发育诊断、量表解释、自闭/ADHD/语言迟缓判断、治疗建议、训练方案、学校安置、福利资格或个体育儿建议。
- 不判断某个儿童是否迟缓、是否需要评估、是否符合早期干预、是否需要特殊教育或是否存在行为障碍。
- 不替代儿科、发育行为儿科、心理/言语/作业/物理治疗、早期干预、学校、社工、保险或紧急服务。

## 上游与下游

- 上游：`well-child-visit-preventive-care-continuity/`、`maternal-newborn-child-development/`、`childcare-family-continuity/`。
- 下游：`early-intervention-idea-part-c-developmental-services-continuity/`、`special-education-iep-504-accommodation-continuity/`、`developmental-language-disorder-child-communication-continuity/`。

## 初始资料线索

- CDC Learn the Signs. Act Early. materials.
- AAP developmental surveillance and screening materials.
- IDEA Part C early intervention public materials.
