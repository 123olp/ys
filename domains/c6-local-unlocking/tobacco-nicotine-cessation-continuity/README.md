# Tobacco Nicotine Cessation Continuity

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
