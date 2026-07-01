# Sidewalk Curb Ramp Maintenance Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/sidewalk-curb-ramp-maintenance-access-continuity` |
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


`sidewalk-curb-ramp-maintenance-access-continuity/` 研究人行道、路缘坡道、裂缝、隆起、积水、无障碍通行和维护请求如何影响步行、轮椅、推车、助行器和低速移动的日常连续性。

## 先验链路

```text
主体离家后需要低成本、可预测的短距离通行
  -> 通行依赖连续人行道、可用路缘坡道、平整表面和可通过宽度
  -> 裂缝、隆起、缺口、阻挡、坡道缺失或维护失败会制造通行断点
  -> 行动速度、跌倒风险、绕行成本、无障碍权益和服务可达同时受损
  -> 医疗、食物、公交、学校、工作和公共服务任务被最后一公里截断
```

## 研究对象

- sidewalk condition、curb ramp、PROWAG、ADA public right-of-way、trip hazard、cross-slope、surface discontinuity、maintenance request、temporary obstruction 和行人设施状态。

## 不能做

- 不提供施工、测量认证、ADA 法律意见、索赔、投诉代写、现场安全判断、路线建议、无障碍诉讼策略或个案处理。
- 不收集、复制或要求住址、残障证明、事故照片、医疗记录、路线轨迹、车牌、投诉记录或法律材料。

## Source Signals

- U.S. Access Board PROWAG: https://www.access-board.gov/prowag/
- FHWA pedestrian facilities accessibility: https://highways.dot.gov/safety/pedestrian-bicyclist
- ADA.gov state and local governments: https://www.ada.gov/resources/title-ii-primer/
- FHWA guide for maintaining pedestrian facilities: https://highways.dot.gov/safety/pedestrian-bicyclist

## 上下游关系

- 上游：`built-environment-accessibility-universal-design/`、`walking-bicycling-micromobility-continuity/`、`public-accommodation-accessibility-service-continuity/`。
- 下游：`paratransit-nemt-access-continuity/`、`fall-risk-prevention-home-safety-continuity/`、`municipal-311-service-request-continuity/`。
