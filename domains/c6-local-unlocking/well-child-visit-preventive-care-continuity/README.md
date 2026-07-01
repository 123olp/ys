# Well Child Visit Preventive Care Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/well-child-visit-preventive-care-continuity` |
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


儿童健康体检与预防照护连续性，关注 well-child visits、medical home、预防服务、成长发育监测、家庭问题识别、转诊、保险覆盖和随访闭环如何支撑儿童长期能力形成。

## 对象

- Well-child visit and pediatric medical home
- Preventive service schedule interface
- Growth, development and family context monitoring
- Screening, anticipatory guidance and referral handoff
- Insurance, transportation, language and appointment barriers
- Caregiver questions and care-plan comprehension
- Record continuity and follow-up boundary

## Human Infra 价值

Well-child visit 是儿童从“没有明显疾病”进入持续预防、筛查、发育观察、照护者支持和资源转介的制度入口。该域把儿童早期健康服务视为主体能力形成的基础设施，而不是把预防照护压缩成临时看病或家庭个人努力。

## 边界

- 不提供体检频率、筛查结果解释、疫苗建议、药物、营养、发育判断、疾病诊断、转诊策略或个体儿科建议。
- 不判断某个儿童是否正常、是否发育迟缓、是否需要检查、是否应转诊或是否有资格获得服务。
- 不替代儿科、family medicine、public health nursing、保险、学校、早期干预、语言服务或紧急服务。

## 上游与下游

- 上游：`newborn-screening-result-followup-continuity/`、`maternal-newborn-child-development/`、`health-insurance-enrollment-renewal-continuity/`。
- 下游：`childhood-immunization-schedule-record-continuity/`、`developmental-behavioral-screening-referral-continuity/`、`pediatric-lead-screening-environmental-followup-continuity/`。

## 初始资料线索

- AAP Bright Futures and preventive pediatric care materials.
- HRSA Bright Futures periodicity and preventive service materials.
- CMS Medicaid EPSDT child health screening materials.
