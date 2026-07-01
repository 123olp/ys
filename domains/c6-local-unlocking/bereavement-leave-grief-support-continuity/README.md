# Bereavement Leave Grief Support Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/bereavement-leave-grief-support-continuity` |
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

Bereavement Leave Grief Support Continuity 研究丧亲假、悲伤支持、创伤知情服务、工作/学校调整和社区陪伴如何帮助幸存者在死亡事件后恢复最低行动能力。

> 核心问题：死亡不仅终止一个主体，也会冲击周围主体的时间、注意力、情绪、收入和照护能力；若悲伤恢复缺少缓冲，幸存者自己的主体持续性会被连带削弱。

## 研究对象

- Bereavement leave、grief support、employee assistance、school/work adjustment、peer support 和 counseling referral。
- 家庭死亡、儿童丧亲、灾害死亡、暴力死亡、自杀遗属、照护后悲伤和复杂性悲伤风险。
- 假期覆盖、工资替代、任务交接、隐私、文化哀悼实践和长期支持入口。

## 先验链路

```text
死亡事件会重击幸存者的情绪、时间、注意力、收入和照护责任
  -> 幸存者需要暂时停止或降低工作/学习任务并获得悲伤支持
  -> 若丧亲假、调整和支持缺失，行政任务、工作要求和照护责任会压过恢复能力
  -> 幸存者可能出现失业、学业中断、健康恶化、孤立和长期功能下降
  -> 家庭与协作网络的主体持续性被连带削弱
  -> 因而丧亲假与悲伤支持是死亡事件外溢风险的恢复层
```

## 关键变量

- 丧亲假覆盖、带薪程度、关系定义、时间长度、灵活性、保密性和反报复边界。
- 悲伤支持可达性、文化适配、同伴支持、危机转介、儿童/青少年支持和长期随访。
- 自杀、暴力、灾害、儿童死亡、照护后悲伤、复杂性悲伤和职场/学校污名风险。

## 证据入口

- U.S. DOL leave and workplace rights materials。
- CDC grief, mental health, suicide bereavement and trauma-informed public materials。
- School, employer, EAP and community grief-support public materials。

## 非目标

- 本域不提供心理治疗、危机干预、诊断、请假策略、法律意见或雇主沟通代写。
- 不判断某人是否符合假期、残障便利、工资替代或心理健康服务资格。
- 不收集死亡细节、创伤经历、工作信息、学校记录、诊断或家庭关系。

## 上下游

- 上游：`funeral-cremation-burial-disposition-continuity/`、`survivor-benefits-death-notification-continuity/`。
- 下游：`mental-health-affective-stability/`、`family-medical-leave-job-protection-continuity/`、`paid-sick-family-leave-wage-replacement-continuity/`、`school-mental-health-counseling-support-continuity/`。
