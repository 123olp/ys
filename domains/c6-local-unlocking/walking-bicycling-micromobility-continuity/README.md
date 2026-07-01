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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

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
