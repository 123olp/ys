# Tobacco Nicotine Cessation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/tobacco-nicotine-cessation-continuity` |
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


`tobacco-nicotine-cessation-continuity/` 研究烟草、尼古丁依赖、戒烟支持、政策环境、复吸预防、青少年保护和多疾病风险下降如何影响主体持续性。

> 核心问题：烟草和尼古丁依赖会同时改变癌症、心血管、肺部、妊娠、伤口愈合和经济资源路径。有效永生需要把戒烟支持建模为长期死亡风险分布向右移动的高杠杆公共健康基础设施。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖可呼吸环境、血管功能、肺功能和行为自主性
  -> 烟草/尼古丁暴露会长期提高多系统风险并削弱自主控制
  -> 结果取决于筛查、咨询、药物可及、quitline、政策环境和复吸预防
  -> 因此烟草尼古丁戒断支持是多疾病上游风险控制域
```

## 关注对象

- Tobacco use screening, cessation counseling, quitlines, nicotine dependence, smoke-free policy, youth vaping, relapse prevention, equity in cessation access。
- 与 `substance-exposure-control/` 的边界：该域关注广义物质暴露；本域关注烟草/尼古丁作为独立高负担风险因子的戒断支持系统。
- 与 `cancer-control/`、`respiratory-oxygenation/` 和 `cardiovascular-resilience/` 的关系：烟草是这些域共同上游变量。

## Human Infra 模型链路

```text
烟草尼古丁戒断支持 T
  -> 改变筛查、咨询、药物/quitline 可及、无烟环境和复吸预防变量 X
  -> 改变尼古丁依赖、肺功能、血管炎症、癌症风险和资源状态 S
  -> 改变癌症、COPD、CVD、妊娠风险和有效时间损失 λ(t)
  -> 影响主体健康寿命、呼吸能力和未来选择权
```

## 非目标

- 不提供个人戒烟药物、剂量、替代品、电子烟策略、戒断处理、孕期建议、青少年个案或医疗建议。
- 不生成烟草/电子烟使用技巧、规避年龄限制、购买渠道、商业推广或违法规避内容。
- 不收集个案使用史、依赖程度、戒断症状、药物、年龄、学校或家庭资料。

## Source Signals

- CDC tobacco: https://www.cdc.gov/tobacco/
- USPSTF tobacco cessation: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/tobacco-use-in-adults-and-pregnant-women-counseling-and-interventions
- WHO tobacco: https://www.who.int/health-topics/tobacco

## 下一步

- 建立 Tobacco Cessation Card：screening, quitline, medication access, policy, relapse prevention, youth protection, disease risk。
- 与 `substance-exposure-control/`、`cancer-control/`、`respiratory-oxygenation/` 和 `cardiovascular-resilience/` 建立接口。
