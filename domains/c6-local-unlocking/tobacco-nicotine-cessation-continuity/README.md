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
