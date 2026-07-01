# 家庭照护者、喘息服务与工作连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/family-caregiver-respite-work-continuity` |
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


本域整理家庭照护者支持、respite care、照护培训、工作灵活性和照护者角色连续性。它关注当家庭成员需要长期照护时，照护者是否会被时间贫困、收入损失、身心耗竭和职业退出击穿。

## 研究对象

- Family caregiver support、respite care、照护者培训、同伴支持和导航服务。
- 老年、残障、儿童复杂照护、痴呆、严重疾病和家庭照护负担。
- 工作灵活性、带薪/无薪照护假、社区服务、成人日间服务和替代照护。
- 照护者健康、收入、职业中断、社会隔离和长期恢复能力。

## 价值链路

```text
家庭成员疾病、衰弱或残障会把照护工作转移给家庭照护者
  -> 若没有喘息和支持，照护责任会吞噬时间、收入、健康和职业角色
  -> 照护者支持、respite 和工作灵活性把不可见照护负担转化为可分担系统
  -> 照护者更可能维持健康、收入、关系和长期工作参与
  -> 被照护者和照护者的主体持续性同时获得保护
```

## 关键问题

- 哪些照护场景会产生最高时间贫困、睡眠损耗、收入损失和心理负担。
- Respite、成人日间服务、居家社区支持、同伴支持和雇主灵活安排如何分担负荷。
- 家庭照护者与长期照护、残障服务、痴呆照护、安宁缓和照护和家庭医疗假的边界。
- 如何把照护者视为主体持续性系统的一部分，而不是免费且无限的资源。

## 上游与下游

- 上游：长期照护、残障服务、痴呆照护、严重疾病、家庭系统和工作制度。
- 下游：照护者健康、被照护者连续性、收入稳定、职业保持和家庭韧性。
- 相关域：`caregiving-long-term-care/`、`dementia-cognitive-decline-care-continuity/`、`disability-services-independent-living/`、`home-health-hospice-palliative-care-continuity/`、`family-medical-leave-job-protection-continuity/`、`paid-sick-family-leave-wage-replacement-continuity/`。

## 非目标

- 不提供个人照护计划、医疗建议、长期照护选择、福利申请、法律或雇佣建议。
- 不判断某个家庭是否有资格获得 respite、HCBS、Medicaid 或其他服务。
- 不生成照护合同、护理方案、雇主请假策略或福利申请材料。
- 不把家庭照护者义务化、道德化，或将照护失败归咎于个人。

## 初始资料入口

- Administration for Community Living: National Family Caregiver Support Program.
- ACL Lifespan Respite Care Program.
- CDC and NIH caregiver health materials.
- Eldercare Locator and Area Agencies on Aging service navigation resources, as public navigation context.
