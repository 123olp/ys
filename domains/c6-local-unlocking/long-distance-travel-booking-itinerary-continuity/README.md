# 长距离旅行预订与行程连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/long-distance-travel-booking-itinerary-continuity` |
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


本域研究长距离出行中的订票、行程记录、改签、取消、通知和跨服务衔接如何保护主体行动窗口。它关注的是离开本地生活圈后的临时操作系统，而不是路线推荐、票价建议或个案旅行安排。

## 研究对象

- 航班、铁路、长途客运、轮渡等长距离出行的订票、确认号、行程单、改签、取消和服务通知。
- 行程资料如何影响住宿入住、工作学习安排、照护交接、医疗预约、紧急联系人和延误恢复。
- 平台锁定、动态定价、退款争议、错订、身份不匹配、通知失败和支付失败造成的执行风险。
- 无智能手机、语言障碍、残障、儿童、老年、低收入和照护责任旅客的额外断点。

## 价值链路

```text
主体持续性需要跨地点任务可执行
  -> 长距离旅行把主体从熟悉住所和服务网络中临时移出
  -> 订票、行程、支付、通知和改签记录成为临时行动脚本
  -> 若行程记录错误、断线或不可更改，工作、照护、医疗、住宿和回程会连锁失败
  -> 长距离旅行预订与行程连续性把远距离移动从愿望转化为可恢复的执行链
```

## 关键问题

- 行程记录如何连接交通、住宿、医疗、工作、家庭和紧急联络？
- 延误、取消、错订、支付失败和服务通知失败如何改变主体有效时间和未来选择权？
- 哪些资料应作为公共研究变量，而不能变成个人实时行程数据收集？
- 官方消费者保护、服务条款和投诉入口如何成为证据边界，而不是个案争议策略？

## 上游与下游

- 上游：`transportation-access-mobility/`、`calendar-scheduling-appointment-continuity/`、`passport-travel-document-mobility-continuity/`。
- 下游：`air-passenger-rights-disruption-refund-continuity/`、`lodging-temporary-accommodation-access-continuity/`、`travel-advisory-consular-assistance-continuity/`。

## 非目标

- 不提供票价套利、刷票、抢票、路线推荐、旅行商业建议、逃票、规避身份检查或退款争议策略。
- 不判断某个服务商、航班、酒店、车次、保险或交通方式是否适合个人。
- 不收集票号、护照号、确认号、位置、支付凭证、实时行程状态或个人旅行计划。

## 初始资料入口

- U.S. Department of Transportation: Aviation Consumer Protection
- USA.gov: Travel and consumer complaints
- FTC: Travel and vacation-rental consumer materials
- Public carrier contracts of carriage and terms as contextual materials
