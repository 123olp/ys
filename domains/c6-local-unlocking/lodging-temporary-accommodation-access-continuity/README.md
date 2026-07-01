# 临时住宿与住宿接入连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/lodging-temporary-accommodation-access-continuity` |
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


本域研究酒店、短租、临时住宿、入住资格、取消规则、无障碍客房、灾害临时安置和住宿诈骗如何影响主体离家后的恢复、安全和任务执行。它关注的是住宿作为临时恢复基地，而不是酒店推荐、订房技巧或个案纠纷。

## 研究对象

- 酒店、motel、短租、宿舍式住宿、灾害临时安置、避难所衔接和临时住宿服务。
- 预订、入住、身份核验、押金、付款、取消、无障碍客房、服务动物和住宿安全信息。
- 住宿失败如何影响睡眠、药品冷藏、卫生、工作、儿童照护、医疗预约和危机恢复。
- 住宿诈骗、隐藏费用、平台停权、不可访问房间、灾害安置容量和投诉入口。

## 价值链路

```text
远离住所后，主体需要新的临时恢复基地
  -> 住宿把睡眠、卫生、药物保存、设备充电、工作和家庭协调重新稳定下来
  -> 若预订失败、入住被拒、无障碍房间不可用或遭遇诈骗，主体恢复能力和行动窗口会急剧下降
  -> 公共消费者保护、无障碍规则和灾害安置资料提供风险识别与制度边界
  -> 临时住宿连续性把旅行中的休息点建模为主体恢复和再行动基础设施
```

## 关键问题

- 临时住宿如何支撑睡眠、卫生、药物、设备、家庭和工作任务？
- 入住资格、押金、身份核验、取消规则和平台治理如何制造断点？
- 无障碍住宿、服务动物和灾害临时安置如何进入主体持续性模型？
- 如何避免把公共消费者资料写成酒店选择、退款争议或漏洞利用策略？

## 上游与下游

- 上游：`long-distance-travel-booking-itinerary-continuity/`、`public-accommodation-accessibility-service-continuity/`、`disaster-recovery-relief-continuity/`。
- 下游：`travel-health-preparedness-continuity/`、`baggage-personal-property-travel-continuity/`、`community-resilience-hub-shelter-center-continuity/`。

## 非目标

- 不提供酒店推荐、订房策略、短租经营、退款争议、住宿投诉、法律索赔、规避入住规则、占住、逃费或安全对抗建议。
- 不判断某个住宿是否安全、可达、可退款、可携带动物或适合个人。
- 不收集预订号、证件、支付凭证、住宿位置、入住时间、门禁信息或个人旅行计划。

## 初始资料入口

- ADA.gov: Lodging and reservation accessibility materials
- FTC: Travel scams and vacation-rental scams
- USA.gov: Travel and consumer complaint materials
- FEMA: Transitional Sheltering Assistance materials when disaster context is relevant
