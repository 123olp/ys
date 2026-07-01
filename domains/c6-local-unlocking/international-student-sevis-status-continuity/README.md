# International Student SEVIS Status Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/international-student-sevis-status-continuity` |
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

`international-student-sevis-status-continuity` 研究 F/M 国际学生身份、SEVIS 记录、I-20、DSO、full course of study、CPT/OPT、travel signature、status maintenance 和学校报告义务如何影响跨境学习、工作授权、居留连续和未来选择权。

> 核心问题：国际学生的学习不是单一校园问题，而是学籍、移民身份、工作授权、旅行、资金和学校报告系统的耦合；任一断裂都可能把学习路径转化为身份风险。

## 关注对象

- SEVIS record、Form I-20、DSO reporting、full course of study、program extension、transfer、change of level 和 reinstatement。
- CPT、OPT、STEM OPT、on-campus employment、work authorization limits、travel signature 和 entry/exit risks。
- Status maintenance、school withdrawal、reduced course load、leave、medical leave、remote study policy 和 grace periods。
- 数据准确性、通知、期限、身份失效、工作中断、学业中断、家庭资源和法律/移民服务边界。

## Human Infra 链路

```text
国际学生 SEVIS 身份连续
  -> 学籍、身份记录、报告义务和工作/旅行权限保持同步
  -> 因记录错误、期限错过、课程负荷或授权误解导致的身份风险下降
  -> 跨境学习、实习、工作入口和居留路径保持可恢复
  -> 主体长期能力资本、全球移动性和未来选择权增强
```

## 非目标

- 不提供签证、移民身份、SEVIS、CPT/OPT、工作授权、旅行、转学、reinstatement、报税或法律建议。
- 不替代 DSO、SEVP、USCIS、CBP、Department of State、雇主合规、税务专业人士或移民律师。
- 不收集或处理护照、签证、I-20、SEVIS ID、I-94、学校记录、雇佣资料、财务资料或移民个案信息。

## Source Signals

- ICE Student and Exchange Visitor Program and SEVIS resources: https://www.ice.gov/sevis
- Study in the States official student status guidance: https://studyinthestates.dhs.gov/
- USCIS employment authorization and OPT/STEM OPT materials: https://www.uscis.gov/
- Department of State visa and travel resources: https://travel.state.gov/

## 下一步

- 建立 `SEVIS record -> enrollment status -> authorization -> travel/work -> status continuity` 变量表。
- 区分 F-1、M-1、J-1 相邻但不同的制度边界；本域先以 F/M 和 SEVP/SEVIS 为主。
- 与 `immigration-status-residency-work-authorization-continuity`、`passport-travel-document-mobility-continuity`、`postsecondary-admissions-transfer-articulation-continuity` 和本轮高教域建立边界。
