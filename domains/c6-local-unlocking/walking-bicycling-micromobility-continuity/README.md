# Walking Bicycling Micromobility Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/walking-bicycling-micromobility-continuity` |
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


`walking-bicycling-micromobility-continuity` 研究步行、自行车、电助力自行车、滑板车、轮椅/助行工具接口、道路设计、照明、速度、停放和微移动可达性如何影响主体短距离行动。

> 核心问题：移动不是只有汽车和公交；如果步行骑行和微移动环境不安全或不可达，很多低成本、低碳、健康导向的日常任务会被迫转成高成本路径或直接失败。

## 关注对象

- 人行道、过街、路口、自行车道、低速街道、照明、停放、共享单车/滑板车、头盔和可见性。
- 儿童、老年人、残障者、低收入群体、无车家庭、校园、通勤、最后一公里和夜间出行。
- 与道路安全、公共交通、建成环境无障碍、健康活动和城市规划的接口。

## Human Infra 链路

```text
主动出行连续
  -> 短距离任务可由步行、骑行和微移动完成
  -> 交通成本、久坐、孤立和服务不可达风险下降
  -> 身体活动与移动任务合并成日常恢复机制
  -> 主体有效时间、健康输入和社区参与增强
```

## 非目标

- 不提供危险骑行、交通违法、绕过车辆限制、破解共享设备、规避停放规则或事故个案策略。
- 不替代交通工程、城市规划、道路安全、医疗、保险、律师或本地执法。
- 不收集出行轨迹、共享设备账号、事故照片、儿童路线或个人位置数据。

## Source Signals

- FHWA Bicycle and Pedestrian Program: https://www.fhwa.dot.gov/environment/bicycle_pedestrian/
- NHTSA Pedestrian and Bicycle Safety: https://www.nhtsa.gov/road-safety/pedestrian-safety
- CDC Physical Activity and Built Environment resources: https://www.cdc.gov/physical-activity/
- MUTCD: https://mutcd.fhwa.dot.gov/

## 下一步

- 建立 `trip distance -> walking/bicycling/micromobility option -> safety exposure -> access barrier -> task completion` 变量表。
- 区分基础设施、行为风险、设备可得性、停放规则、无障碍和天气暴露。
- 与 `road-traffic-injury-prevention-safe-mobility`、`physical-activity-mobility`、`built-environment-accessibility-universal-design` 和 `public-transit-service-operations-continuity` 建立边界。
