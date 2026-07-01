# Vaccination Campaign Booster Delivery Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/vaccination-campaign-booster-delivery-continuity` |
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


`vaccination-campaign-booster-delivery-continuity/` 研究疫苗行动、加强针递送、预约、冷链、提醒、可达公平和高风险人群覆盖如何支撑暴发响应。

> 核心问题：疫苗价值不只在研发和批准；只有被安全、公平、及时递送到可受益人群，才会改变生命路径风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 暴发期间免疫屏障决定感染、重症和医疗挤兑风险
  -> 免疫屏障依赖疫苗行动、加强针递送、冷链、预约和信任
  -> 疫苗递送连续性决定技术收益能否转化为群体风险下降
```

## 关注对象

- 疫苗行动、加强针递送、冷链、预约系统、提醒召回、流动接种、社区伙伴、可达公平和风险沟通。
- 与 `immunization-public-health-surveillance/` 的关系：上位域关注免疫计划与监测；本域关注 outbreak/campaign 执行层。

## Human Infra 模型链路

```text
疫苗行动与加强针递送
  -> 改变覆盖率、及时性、高风险人群保护和医疗系统压力
  -> 改变感染后重症、失能、死亡和服务中断风险
  -> 提高组织开放、安全学习工作和照护连续性的可行性
  -> 增强健康寿命、有效时间和主体持续性
```

## 非目标

- 不提供个体接种建议、禁忌判断、加强针时间表、旅行疫苗、医学风险解释或接种预约代办。
- 不提供疫苗证明伪造、优先级规避、冷链操作、医疗操作或宣传操纵策略。
- 不把疫苗行动资料写成个体医疗处方。

## Source Signals

- CDC vaccines: https://www.cdc.gov/vaccines/
- CDC immunization schedules: https://www.cdc.gov/vaccines/schedules/
- WHO vaccines and immunization: https://www.who.int/health-topics/vaccines-and-immunization
- Immunization Agenda 2030: https://www.who.int/teams/immunization-vaccines-and-biologicals/strategies/ia2030

## 下一步

- 建立变量表：覆盖率、及时性、预约摩擦、冷链稳定、提醒召回、高风险覆盖、信任和不良事件反馈接口。
- 与 `immunization-record-proof-continuity/`、`pharmacovigilance-drug-safety-monitoring/` 和 `community-health-workers-peer-support/` 建立接口。
