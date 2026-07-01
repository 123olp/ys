# 海关、边境入境与申报连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/customs-border-entry-declaration-continuity` |
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


本域研究海关申报、边境检查、I-94/入境记录、受限物品、农业检疫、关税和可信旅客系统如何影响跨境主体的物品、身份和行程连续性。它关注的是入境制度接口如何保护或截断行动链，而不是移民策略、走私规避或个案入境建议。

## 研究对象

- 海关申报、入境检查、I-94、受限/禁止物品、农业与食品检查、现金申报、关税和边境服务。
- Global Entry / Trusted Traveler 等可信旅客项目作为制度接口，而不是个人申请建议。
- 入境记录错误、申报错误、物品扣留、证件/姓名错配、二次检查和语言障碍造成的断点。
- 海关边境规则如何连接护照、旅行健康、药品携带、行李、旅行证件和后续居留/工作/学习安排。

## 价值链路

```text
跨境返回或进入必须通过边境制度接口
  -> 海关申报和入境记录把主体、物品、健康材料和行程事实转化为可入境状态
  -> 若申报、记录、证件或物品边界失败，主体可能失去时间、物资、医疗用品、学习工作窗口和后续身份记录
  -> 官方边境资料和申报规则提供可审查的制度变量与禁止用途边界
  -> 海关与入境申报连续性把边境通过建模为主体跨境行动链的关键门槛
```

## 关键问题

- 海关申报、I-94 和入境记录如何影响后续工作、学习、医疗和跨境行动？
- 药品、食品、动植物、现金、设备和商业物品如何成为边境断点？
- 可信旅客系统、语言可及性和记录更正如何影响摩擦成本？
- 如何避免把公开边境资料写成走私、虚假申报、规避检查或移民策略？

## 上游与下游

- 上游：`passport-travel-document-mobility-continuity/`、`travel-health-preparedness-continuity/`、`baggage-personal-property-travel-continuity/`。
- 下游：`immigration-status-residency-work-authorization-continuity/`、`long-distance-travel-booking-itinerary-continuity/`、`citizenship-nationality-statelessness-continuity/`。

## 非目标

- 不提供签证、移民、入境资格、申报策略、走私、规避检查、违禁品携带、虚假陈述、I-94 个案处理或可信旅客申请建议。
- 不判断个人是否可入境、是否需申报、是否可携带某物、是否应申请某项目或如何处理边境争议。
- 不收集护照号、签证、I-94、海关申报、旅行路线、药品清单、支付信息或边境检查记录。

## 初始资料入口

- U.S. Customs and Border Protection: Travel
- CBP: Know Before You Go
- CBP: I-94 and entry records
- CBP: Prohibited and restricted items / agriculture inspection materials
