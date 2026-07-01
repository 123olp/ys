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
