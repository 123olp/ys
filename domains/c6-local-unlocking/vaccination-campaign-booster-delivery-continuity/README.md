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
