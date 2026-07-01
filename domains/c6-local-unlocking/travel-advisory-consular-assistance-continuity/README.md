# 旅行警示与领事协助连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/travel-advisory-consular-assistance-continuity` |
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


本域研究旅行警示、海外登记、领事协助、紧急护照、海外医疗/逮捕/死亡/危机协助和海外通信如何影响跨境主体的安全与选择权。它关注的是国家边界外的制度求助链，而不是旅行安全建议、撤离路线或法律策略。

## 研究对象

- Travel Advisory、STEP、海外使领馆、紧急协助、紧急护照、危机通信和海外联系。
- 海外医疗、事故、死亡、逮捕、失踪、灾害、冲突和证件丢失时的制度性断点。
- 旅行警示如何影响保险、雇主/学校安排、家庭联络、行程决策和风险边界。
- 领事协助的能力边界、不可承诺事项、隐私同意和家庭通知。

## 价值链路

```text
跨境移动把主体放入不熟悉的法律、医疗和安全环境
  -> 旅行警示和领事登记把外部风险、危机通信和求助入口提前接入主体计划
  -> 海外突发事件中，领事协助、紧急证件和家庭通信决定主体是否仍能被定位、承认和恢复
  -> 若警示失读、登记缺失或求助边界被误解，跨境风险会放大为身份、医疗、自由和家庭断裂
  -> 旅行警示与领事协助连续性把海外风险治理纳入主体持续性基础设施
```

## 关键问题

- 旅行警示、STEP 和领事协助如何影响跨境风险识别与求助链？
- 海外医疗、逮捕、死亡、失踪、灾害和证件丢失如何改变主体连续性？
- 领事协助能做什么、不能做什么，如何避免虚假安全感？
- 如何把官方警示作为风险资料，而不是具体出行、撤离或法律行动建议？

## 上游与下游

- 上游：`passport-travel-document-mobility-continuity/`、`long-distance-travel-booking-itinerary-continuity/`、`travel-health-preparedness-continuity/`。
- 下游：`customs-border-entry-declaration-continuity/`、`disaster-recovery-relief-continuity/`、`armed-conflict-civilian-protection-ihl/`。

## 非目标

- 不提供旅行安全、撤离路线、冲突地区行动、海外法律、签证、移民、逮捕处置、医疗转运、保险理赔或个案领事建议。
- 不判断个人是否应旅行、是否应撤离、是否安全、是否能获得领事协助或是否可入境。
- 不收集护照号、海外位置、行程、家属信息、报警记录、医疗记录或领事案件资料。

## 初始资料入口

- U.S. Department of State: Travel Advisories
- Smart Traveler Enrollment Program (STEP)
- U.S. Department of State: Emergency Assistance for U.S. Citizens Abroad
- U.S. Embassies and Consulates public materials as contextual sources
