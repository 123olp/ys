# Parking Curb Access Towing Impound Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/parking-curb-access-towing-impound-continuity` |
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

`parking-curb-access-towing-impound-continuity` 研究停车、路缘上下客、装卸、残障停车、罚单、拖车、扣押、取回流程和费用如何影响主体能否完成出行并保留车辆移动能力。

> 核心问题：到达目的地不等于完成出行；如果停车、路缘访问、拖车和扣押链失控，移动任务会在最后几十米、罚费和车辆取回流程上失败。

## 关注对象

- 停车位、路缘管理、上下客、装卸、残障停车、停车支付、罚单、拖车、扣押、取回和费用。
- 医疗、照护、学校、工作、配送、搬家、灾害撤离和低收入车辆依赖场景。
- 与城市规划、公共交通、道路安全、消费者保护、法律援助和财务韧性的接口。

## Human Infra 链路

```text
停车与路缘访问连续
  -> 出行的最后一段、上下客和车辆保留可执行
  -> 罚单、拖车、扣押和费用冲击不再轻易切断移动能力
  -> 目的地可达性从地图路径转化为真实任务完成
  -> 主体医疗、工作、照护和公共服务接入增强
```

## 非目标

- 不提供逃避停车执法、规避罚单、隐藏车辆、绕过拖车、伪造残障许可或法律个案策略。
- 不替代本地交通部门、停车机构、DMV、法院、律师、执法、拖车场或消费者保护机构。
- 不收集车牌、停车记录、罚单、扣押单、位置轨迹、残障许可或个人支付信息。

## Source Signals

- U.S. DOT Curb Management resources: https://www.transportation.gov/
- FHWA Curbside Inventory / Curb Management materials: https://ops.fhwa.dot.gov/
- ADA.gov Parking guidance: https://www.ada.gov/
- USA.gov Traffic Tickets: https://www.usa.gov/traffic-tickets

## 下一步

- 建立 `destination -> curb/parking access -> payment/enforcement -> vehicle retention -> task completion` 变量表。
- 区分残障停车、医疗上下客、商业装卸、住宅停车、拖车扣押和罚费负担。
- 与 `urban-planning-land-use-zoning-resilience`、`transportation-access-mobility`、`access-to-justice-legal-aid` 和 `financial-resilience-access` 建立边界。
