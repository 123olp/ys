# Child Care Availability Affordability Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/child-care-availability-affordability-continuity` |
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

`child-care-availability-affordability-continuity/` 研究儿童照护名额、费用、时段、距离和年龄覆盖是否让家庭真正接上稳定照护，而不是只在名义上存在托育市场。

> 核心问题：托育服务存在不等于家庭可用；如果名额不足、费用过高、时段不匹配或地理距离过远，照护者的工作、学习、恢复和收入连续性会被直接切断。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 儿童需要稳定安全的日常照护
  -> 照护者需要可预测的时间、收入和恢复窗口
  -> 托育名额、费用、时段、距离和年龄覆盖必须可承受
  -> 家庭才不会被照护缺口压缩有效时间和未来选择权
```

## 关注对象

- 托育名额供给、等待名单、年龄段覆盖、营业时段、通勤距离和可负担性。
- 家庭费用负担、市场供需、照护安排稳定性、非正式照护和备用照护缺口。
- 与 `childcare-family-continuity/`、`child-care-subsidy-ccdf-payment-continuity/`、`social-protection-benefits-delivery/`、`workforce-employment-services/` 和 `time-allocation-effective-time/` 的接口。

## Human Infra 模型链路

```text
儿童照护需求
  -> 可用名额、可承受费用、时段覆盖和地理可达性
  -> 照护者工作学习恢复时间得到保留
  -> 家庭压力、收入中断和儿童照护不稳定下降
  -> 两代主体的有效时间和未来选择权增加
```

## 非目标

- 不推荐具体托育机构、价格、地点、排队策略或家庭照护安排。
- 不判断个体资格、费用承受能力、补贴申请、机构质量或儿童适配性。
- 不收集儿童身份、家庭收入、工作排班、住址、托育记录或候补名单资料。

## Source Signals

- ACF Office of Child Care: https://www.acf.hhs.gov/occ
- ChildCare.gov: https://childcare.gov/
- National Survey of Early Care and Education: https://www.acf.hhs.gov/opre/project/national-survey-early-care-and-education-2019-2017-2022
- Census Child Care: https://www.census.gov/topics/families/child-care.html

## 下一步

- 建立变量表：名额、费用、时段、距离、年龄覆盖、等待时间、备用照护和照护稳定性。
- 整理 ACF OCC、ChildCare.gov、NSECE 和 Census child care 的 Source Cards。
- 与 `childcare-family-continuity/` 区分：本域只处理供给可得性和费用可承受性执行层。
