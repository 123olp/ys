# Immunization Public Health Surveillance

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/immunization-public-health-surveillance` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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

- 界定生命载体变量：细胞、组织、器官、脑、免疫、代谢、急性风险或衰老损伤。
- 说明影响机制：修复、替换、再生、控制、筛查、预防、维持或风险降低。
- 列出可观察状态：功能指标、生物标志物、疾病终点、失能时间、恢复能力或死亡风险。
- 记录副作用、过度干预、癌变、免疫、长期安全性和尾部风险。
- 区分机制合理性、体外证据、动物证据、人体早期数据、临床终点和长期安全性。

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

`immunization-public-health-surveillance/` 研究免疫计划、传染病监测、公共卫生应急、感染防控、医疗相关感染监测、AMR、One Health 和废水监测。

> 核心问题：主体不是孤立生物体；长期持续性依赖群体免疫、早期发现、传播阻断、医疗环境安全和跨物种风险治理。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 个体免疫和医疗能力会被群体感染环境约束
  -> 疫苗、监测、感染防控和应急系统决定风险能否在大规模传播前被发现
  -> 公共卫生基础设施决定主体是否被感染浪潮、耐药、医疗相关感染和跨物种风险截断
```

## 关注对象

- 免疫计划、疫苗覆盖、传染病报告、NNDSS、GISRS、IHR、公共卫生应急、IPC、NHSN、GLASS、One Health、NWSS。
- 传染病早期信号、医疗相关感染、废水监测、抗微生物耐药、跨物种传播和风险沟通边界。
- 与 `immune-maintenance/` 的关系：免疫维护域关注个体免疫系统；本域关注群体免疫、监测和公共卫生系统。
- 与 `antimicrobial-resilience/`、`emergency-preparedness-response/`、`healthcare-access-continuity/` 和 `planetary-health-environment/` 的接口。

## Human Infra 模型链路

```text
免疫与公共卫生监测基础设施
  -> 改变疫苗覆盖、病例发现、传播监测、感染防控和应急响应能力
  -> 改变个体所处感染风险环境和医疗系统安全状态
  -> 降低暴发、医疗相关感染、耐药扩散、跨物种风险和公共卫生失灵风险
  -> 增强群体保护、医疗可用性、健康寿命和主体持续性
```

## 非目标

- 不提供疫苗医学建议、禁忌判断、个人免疫状态解释、诊断、治疗、隔离或出行建议。
- 不提供疫情预测保证、监测规避、公共卫生措施规避、病原体操作或传播策略。
- 不把群体数据写成个体风险结论或政治化动员工具。

## Source Signals

- WHO vaccines and immunization: https://www.who.int/health-topics/vaccines-and-immunization
- Immunization Agenda 2030: https://www.who.int/teams/immunization-vaccines-and-biologicals/strategies/ia2030
- CDC vaccines: https://www.cdc.gov/vaccines/
- CDC NNDSS: https://www.cdc.gov/nndss/
- WHO GISRS: https://www.who.int/initiatives/global-influenza-surveillance-and-response-system
- WHO International Health Regulations: https://www.who.int/health-topics/international-health-regulations
- WHO IPC: https://www.who.int/teams/integrated-health-services/infection-prevention-control
- CDC NHSN: https://www.cdc.gov/nhsn/
- WHO GLASS: https://www.who.int/initiatives/glass
- CDC NWSS: https://www.cdc.gov/nwss/

## 下一步

- 建立公共卫生监测变量表：免疫覆盖、病例报告、实验室网络、废水信号、IPC、HAI、AMR、One Health、应急响应和风险沟通。
- 与 `immune-maintenance/` 拆分个体免疫和群体公共卫生边界。
- 整理 WHO immunization、IA2030、CDC NNDSS、WHO GISRS、IHR、IPC、NHSN、GLASS 和 NWSS 的 Source Cards。
