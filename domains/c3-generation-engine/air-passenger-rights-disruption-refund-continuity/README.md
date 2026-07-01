# 航空旅客权利、中断与退款连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/air-passenger-rights-disruption-refund-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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


本域研究航班延误、取消、退款、拒载、行李责任、无障碍航空旅行和消费者投诉如何影响主体在远距离移动中的时间、资源和任务连续性。它关注的是航空服务中断的公共规则与恢复机制，而不是个人维权、赔偿或航空公司选择建议。

## 研究对象

- 航班延误、取消、退款、拒载、停机坪延误、航班信息披露和航空消费者投诉。
- 航空公司承运合同、DOT 航空消费者保护资料、服务承诺和公开 dashboard。
- 残障旅客、辅助设备、服务动物、儿童、老年旅客和照护者在航空中断中的特殊断点。
- 航空中断如何影响住宿、医疗预约、工作学习、照护交接、签证/入境窗口和回程能力。

## 价值链路

```text
远距离行动依赖航空服务按时、可解释、可恢复
  -> 航班中断会消耗时间、现金、药物余量、住宿窗口和跨境安排
  -> 退款、重新安排、投诉和无障碍义务决定主体能否从中断中恢复
  -> 若规则不透明、通知失败或辅助需求被忽视，移动失败会扩散为工作、医疗、家庭和身份风险
  -> 航空旅客权利连续性把航空中断从单次不便建模为主体行动链的恢复问题
```

## 关键问题

- 航空中断如何改变主体有效时间、现金缓冲、治疗连续性和任务窗口？
- 退款、改签、拒载和投诉规则如何作为公共制度变量进入 Human Infra？
- 残障、辅助设备、服务动物和照护需求如何改变中断风险和恢复成本？
- 如何避免把公共消费者保护资料误写成个案法律、赔偿或投诉策略？

## 上游与下游

- 上游：`long-distance-travel-booking-itinerary-continuity/`、`passport-travel-document-mobility-continuity/`、`disability-services-independent-living/`。
- 下游：`baggage-personal-property-travel-continuity/`、`lodging-temporary-accommodation-access-continuity/`、`travel-advisory-consular-assistance-continuity/`。

## 非目标

- 不提供个人退款、赔偿、投诉、诉讼、航空公司选择、票价购买、改签或航班中断应对策略。
- 不判断某个航班、航空公司、路线、机场、保险或服务是否适合个人。
- 不收集机票、PNR、登机牌、身份文件、残障证明、行李标签或实时航班数据。

## 初始资料入口

- U.S. Department of Transportation: Aviation Consumer Protection
- U.S. DOT: Fly Rights and Airline Customer Service Dashboard
- U.S. DOT: Passengers with Disabilities and Air Travel
- Airline contracts of carriage as contextual materials
