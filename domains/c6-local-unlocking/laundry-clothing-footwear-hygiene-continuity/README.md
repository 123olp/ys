# Laundry Clothing Footwear Hygiene Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/laundry-clothing-footwear-hygiene-continuity` |
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

`laundry-clothing-footwear-hygiene-continuity` 研究衣物、鞋履、洗衣、干燥、个人卫生、工作/学校着装和天气防护如何影响主体尊严、感染控制、出行、工作和恢复连续性。

> 核心问题：衣物和鞋履不是生活细节；干净、合身、适温、防护和可维护的穿着系统，是外出、工作、学习、照护、睡眠和社会参与的低层条件。

## 关注对象

- 洗衣、干燥、换洗、衣物储存、鞋履、天气防护、制服、工作服、学校着装和个人卫生用品。
- 清洁衣物可及、洗衣设施、能源/水依赖、污染衣物处理、潮湿霉变、寄生虫/感染暴露和尊严边界。
- 极端热/冷、雨雪、户外工作、无家可归、灾后恢复、照护场景和残障穿脱可达性。
- 与 WASH、住房、能源、职业安全、学校、公共福利、家庭应急和无障碍设计的接口。

## Human Infra 链路

```text
衣物鞋履卫生连续
  -> 主体能保持清洁、适温、防护、尊严和外出可达
  -> 洗衣、水电、衣物损耗、天气暴露和穿着排除造成的任务摩擦下降
  -> 学习、工作、照护、社交和恢复不被低层物品短缺反复中断
  -> 有效时间、社会参与、健康风险控制和未来选择权增强
```

## 非目标

- 不提供个体穿搭、购买推荐、医疗诊断、职业 PPE 配置、感染处理或清洗处置操作建议。
- 不替代 OSHA/NIOSH、CDC、学校、雇主、本地福利或公共卫生指导。
- 不把衣着、卫生或外观作为道德评价、资格筛选、阶层污名或监控依据。

## Source Signals

- CDC Hygiene: https://www.cdc.gov/hygiene/
- CDC Cleaning and Disinfecting: https://www.cdc.gov/hygiene/cleaning/
- Ready.gov Emergency Kit: https://www.ready.gov/kit
- NIOSH Workplace Safety and Health Topics: https://www.cdc.gov/niosh/topics/

## 下一步

- 建立 `clothing item -> task context -> hygiene/protection function -> maintenance dependency -> participation impact` 变量表。
- 区分日常换洗、学校/工作要求、极端天气、灾后、无家可归和照护/残障穿脱场景。
- 与 `water-sanitation-hygiene-continuity`、`occupational-exposure-industrial-hygiene`、`housing-built-environment-stability` 和 `household-cleaning-disinfection-pest-control-continuity` 建立边界。
