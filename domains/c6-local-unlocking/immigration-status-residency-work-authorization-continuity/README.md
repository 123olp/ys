# Immigration Status Residency Work Authorization Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/immigration-status-residency-work-authorization-continuity` |
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

本域研究移民身份、居留资格、工作授权、身份变更、身份续期和身份失效风险如何影响主体在一个制度内持续生活、工作、学习、医疗和连接家庭。

> 核心问题：主体能否继续行动，不只取决于是否在某地，还取决于是否有被承认的居留与工作资格；身份过期、文件延迟或授权断裂会把时间、收入、医疗、教育和家庭关系同时推入不稳定。

## 关注对象

- 签证、居留、永久居民、工作授权、身份变更、延期、续期、身份证明和雇佣资格核验。
- 身份过期、等待期间、文件丢失、地址变更、雇主依赖、家庭成员派生资格和服务资格断点。
- 移民身份与就业、教育、医疗、银行、住房、驾照、税务、公共福利和家庭团聚的接口。
- 与 `migration-displacement-humanitarian-continuity/` 的边界：迁移域关注移动和流离失所后的服务连续性；本域关注制度内居留和工作授权连续性。

## Human Infra 链路

```text
移民身份 / 居留 / 工作授权连续
  -> 主体在所在地拥有可证明、可续期、可核验的制度资格
  -> 工作、学习、医疗、住房、金融和家庭关系可以持续运行
  -> 过期、延误、雇主锁定、资格断裂和服务拒绝风险下降
  -> 主体获得跨时间的制度稳定和行动窗口
```

## 非目标

- 不提供签证、绿卡、居留、工作许可、身份变更、延期、加急、申诉、雇佣、税务或法律建议。
- 不判断个人是否有移民资格、工作资格、福利资格、入境资格或身份风险。
- 不协助伪造文件、规避 E-Verify/I-9、隐藏身份、绕过边境/执法、滥用签证或组织危险迁移。

## Source Signals

- USCIS Green Card: https://www.uscis.gov/green-card
- USCIS Employment Authorization: https://www.uscis.gov/green-card/green-card-processes-and-procedures/employment-authorization-document
- USCIS Change My Nonimmigrant Status: https://www.uscis.gov/visit-the-united-states/change-my-nonimmigrant-status
- USCIS I-9 Central: https://www.uscis.gov/i-9-central

## 下一步

- 建立移民状态连续性变量表：身份类别、有效期、续期窗口、工作授权、派生资格、等待状态、文件恢复和服务资格接口。
- 整理 USCIS、DHS、State Department visa、I-9/E-Verify 和 OECD / IOM migration governance Source Cards。
- 与 `passport-travel-document-mobility-continuity/` 明确分工：护照域研究跨境移动证件，本域研究在地居留和工作授权。
