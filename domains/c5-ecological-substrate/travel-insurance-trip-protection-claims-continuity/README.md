# 旅行保险、行程保障与理赔连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/travel-insurance-trip-protection-claims-continuity` |
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


本域研究 travel insurance、trip cancellation、trip interruption、travel medical、evacuation、baggage coverage、delay coverage、pre-existing condition waiver、claim 和 documentation 如何影响主体离家后的时间、现金、医疗和行李恢复。它关注旅行风险转移执行层，而不是保险购买、行程退款、医疗转运或法律建议。

## 研究对象

- 旅行取消、旅行中断、旅行延误、行李延误/丢失、旅行医疗、紧急撤离和 rental car coverage。
- covered reasons、cancel for any reason、pre-existing condition waiver、exclusions、documentation、receipts 和 claim deadlines。
- 航空/酒店退款、信用卡旅行权益、旅行保险 claim、第三方援助服务和投诉入口。
- 与旅行预订、航空旅客权利、行李物品、旅行健康准备和领事协助的边界。

## 价值链路

```text
主体离家后暴露于行程中断、医疗和财物风险
  -> 旅行保险把延误、取消、医疗和行李损失转移到保单理赔链
  -> 明确 covered reasons、材料记录和援助入口降低离家状态的现金与时间损失
  -> 除外责任、资料缺失、重复覆盖或理赔延迟会让旅行中断扩大为长期负担
  -> 旅行保险连续性把临时移动风险纳入可恢复的风险转移系统
```

## 关键问题

- 旅行保险与航空退款权、酒店取消规则、信用卡权益如何分界？
- covered reasons、pre-existing condition waiver 和 exclusions 如何影响真实保障？
- 医疗、撤离、行李和延误 claim 需要哪些不同记录链？
- 旅行保险如何与旅行健康准备、领事协助和临时住宿连接？

## 上游与下游

- 上游：`long-distance-travel-booking-itinerary-continuity/`、`travel-health-preparedness-continuity/`、`baggage-personal-property-travel-continuity/`。
- 下游：`air-passenger-rights-disruption-refund-continuity/`、`lodging-temporary-accommodation-access-continuity/`、`travel-advisory-consular-assistance-continuity/`、`consumer-return-refund-dispute-resolution-continuity/`。

## 非目标

- 不提供旅行保险购买、保额选择、claim 填写、退款、医疗转运、撤离、签证、旅行安全、诉讼或法律建议。
- 不判断某个行程中断、医疗事件、行李损失、保险产品或赔付金额是否应覆盖。
- 不协助伪造行程、虚假医疗证明、虚假行李损失、重复索赔、夸大损失、保险欺诈、退款套利或骚扰服务人员。

## 初始资料入口

- NAIC: Travel insurance consumer materials
- U.S. DOT aviation consumer protection materials
- State insurance department travel insurance complaint materials
- State Department / CDC travel risk context materials
