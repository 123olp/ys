# Multimodal Trip Planning Real Time Wayfinding Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/multimodal-trip-planning-real-time-wayfinding-continuity` |
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

`multimodal-trip-planning-real-time-wayfinding-continuity` 研究路线规划、实时到站、GTFS/GTFS-Realtime、无障碍路径、服务中断、导航、站内导向和语言可达如何影响主体能否把出行计划转成真实到达。

> 核心问题：交通选项存在不等于主体能使用；如果路线、时间、换乘、无障碍路径和服务中断信息不可知，主体会在规划、等待、换乘和迷路中消耗有效时间。

## 关注对象

- GTFS、GTFS-Realtime、公交/轨道实时信息、换乘、站点导向、无障碍路径、步行连接、服务中断和多语言信息。
- 医疗预约、工作通勤、学校接送、夜间出行、游客、认知障碍者、低视力/低听力者和低数字技能人群。
- 与地理空间导航、公共交通运营、语言可达、无障碍、通知警报和数字包容的接口。

## Human Infra 链路

```text
出行信息连续
  -> 路线、时间、换乘、无障碍和中断信息可被理解
  -> 等待、迷路、错过换乘和迟到成本下降
  -> 多模式交通从抽象网络转化为可执行路径
  -> 主体有效时间、服务到达率和行动信心增强
```

## 非目标

- 不提供逃票、绕过安检、跟踪他人、抓取私有位置数据、破坏交通数据或规避平台限制方法。
- 不替代交通运营商、地图平台、应急警报、无障碍服务、旅行安全、医疗或本地服务渠道。
- 不收集个人位置轨迹、常用路线、家庭地址、工作地址、医疗预约、儿童路线或账号 token。

## Source Signals

- GTFS Schedule: https://gtfs.org/schedule/
- GTFS Realtime: https://gtfs.org/realtime/
- FTA Transit Data and Mobility resources: https://www.transit.dot.gov/
- ADA.gov Transportation: https://www.ada.gov/topics/transportation/

## 下一步

- 建立 `origin/destination -> route data -> real-time signal -> accessibility path -> arrival outcome` 变量表。
- 区分公共静态数据、实时中断、站内导向、语言可达、无障碍路径和数字排除。
- 与 `geospatial-navigation-location-infrastructure`、`public-transit-service-operations-continuity`、`language-access-plain-communication` 和 `notification-alert-routing-attention-continuity` 建立边界。
