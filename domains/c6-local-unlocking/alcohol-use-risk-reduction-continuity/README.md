# Alcohol Use Risk Reduction Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/alcohol-use-risk-reduction-continuity` |
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

`alcohol-use-risk-reduction-continuity/` 研究不健康饮酒筛查、简短干预、治疗转介、复发/伤害减少、肝脏/癌症/伤害风险和社会功能影响如何改变主体持续性。

> 核心问题：酒精风险不只影响肝脏，也会改变事故、暴力、癌症、睡眠、认知、工作、家庭和自杀风险。有效永生需要把酒精风险识别和降风险支持建模为主体控制权和有效时间保护系统。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖稳定判断、睡眠、肝脏代谢、关系和行动安全
  -> 不健康饮酒会同时改变身体、认知、事故、家庭和资源风险
  -> 结果取决于筛查、简短干预、转介、治疗可及和复发/伤害减少系统
  -> 因此酒精使用风险降低是主体控制权和多系统风险的上游治理域
```

## 关注对象

- Unhealthy alcohol use screening, brief intervention, referral to treatment, alcohol use disorder care continuity, injury prevention, stigma, family/work impact。
- 与 `substance-exposure-control/` 的边界：该域关注广义物质暴露；本域关注酒精作为合法、高负担、强社会嵌入风险源的识别和降风险执行链。
- 与 `mental-health-affective-stability/`、`renal-hepatic-clearance/` 和 `personal-safety-violence-prevention/` 的关系：酒精风险跨越情绪、肝脏、事故和暴力风险。

## Human Infra 模型链路

```text
酒精风险降低系统 T
  -> 改变筛查、简短干预、转介、治疗可及、污名和复发/伤害减少变量 X
  -> 改变肝脏代谢、睡眠、判断、事故风险、关系稳定和资源状态 S
  -> 改变死亡、癌症、肝病、事故、自杀、失业和有效时间损失 λ(t)
  -> 影响主体控制权、行动质量和未来选择权
```

## 非目标

- 不提供个人饮酒量判断、戒断处理、解酒、药物、排毒、治疗计划、家庭干预、法律、驾驶或个体医疗建议。
- 不生成饮酒技巧、规避检测、危险挑战、酒精购买、未成年人饮酒或自伤相关内容。
- 不收集个案饮酒史、戒断症状、家庭冲突、驾驶、法律或心理危机资料。

## Source Signals

- NIAAA alcohol resources: https://www.niaaa.nih.gov/
- USPSTF unhealthy alcohol use screening: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/unhealthy-alcohol-use-in-adolescents-and-adults-screening-and-behavioral-counseling-interventions
- WHO alcohol: https://www.who.int/health-topics/alcohol

## 下一步

- 建立 Alcohol Risk Reduction Card：screening, brief intervention, referral, treatment continuity, relapse / harm reduction, family/work impact。
- 与 `substance-exposure-control/`、`mental-health-affective-stability/`、`renal-hepatic-clearance/` 和 `personal-safety-violence-prevention/` 建立接口。
