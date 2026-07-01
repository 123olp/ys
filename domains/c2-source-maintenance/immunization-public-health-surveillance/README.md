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
