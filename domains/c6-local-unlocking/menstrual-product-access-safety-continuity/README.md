# Menstrual Product Access Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/menstrual-product-access-safety-continuity` |
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

`menstrual-product-access-safety-continuity` 研究月经用品、卫生设施、学校/工作场所可得性、费用、隐私、污名、材料安全和更换条件如何影响主体学习、工作、睡眠、移动和尊严连续性。

> 核心问题：月经用品不是边缘生活用品；它决定一部分主体能否在周期性生理条件下稳定进入学校、工作、交通、照护和公共空间。

## 关注对象

- 卫生巾、棉条、月经杯、经期内裤、处置设施、清洁水、洗手、隐私和更换空间。
- 费用、断供、学校/工作缺勤、应急物资、无家可归、灾害、羁押、旅行和公共厕所可达。
- 产品标签、材料安全、毒性休克风险沟通、皮肤刺激、感染风险和误用边界。
- 与 WASH、公共厕所、学校健康、工作设计、住房、福利和反污名治理的接口。

## Human Infra 链路

```text
月经用品连续
  -> 主体能在周期性出血条件下保持卫生、隐私、尊严和外出能力
  -> 用品费用、设施缺失、处置障碍和污名造成的缺勤与任务中断下降
  -> 学习、工作、照护、睡眠、移动和公共服务进入更稳定
  -> 有效时间、社会参与和未来选择权增强
```

## 非目标

- 不提供月经诊断、异常出血判断、产品品牌推荐、使用参数、感染判断、妇科治疗或避孕建议。
- 不替代临床医生、FDA、OWH、学校/雇主政策、本地福利或公共卫生指导。
- 不把月经追踪、用品发放或设施管理变成监控、羞辱、资格排除或隐私侵犯工具。

## Source Signals

- Office on Women's Health Menstrual Cycle: https://www.womenshealth.gov/menstrual-cycle
- Office on Women's Health Your Menstrual Cycle: https://www.womenshealth.gov/menstrual-cycle/your-menstrual-cycle
- CDC Hygiene: https://www.cdc.gov/hygiene/

## 下一步

- 建立 `product type -> facility dependency -> privacy/dignity condition -> participation impact` 变量表。
- 区分学校、工作、无家可归、灾害、羁押、低收入和残障/照护依赖场景。
- 与 `menstrual-health-cycle-literacy-continuity`、`public-restroom-sanitation-hygiene-access-continuity` 和 `water-sanitation-hygiene-continuity` 建立边界。
