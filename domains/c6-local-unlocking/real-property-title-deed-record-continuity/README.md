# 不动产权属、地契与土地记录连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/real-property-title-deed-record-continuity` |
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

本域研究不动产权属、地契、土地记录、抵押、税费和产权链如何支撑主体对居住、资产、继承和迁移选择的长期控制。它关注的是产权记录作为资源稳定性的基础设施，而不是个人买房、卖房、产权、税务或法律建议。

## 研究对象

- 地契、土地登记、产权链、所有权记录、抵押记录、留置和产权负担。
- 房产税、地块信息、地址地理编码、评估记录和地方记录机关。
- title search、title insurance、closing documents 和产权错误纠正。
- 不动产记录与住房稳定、遗产继承、抵押融资、灾害恢复、地址证明和公共服务的关系。

## 价值链路

```text
主体需要稳定控制居住空间和长期资产
  -> 不动产权属和土地记录把空间、住所和资产绑定到可承认的制度事实
  -> 地契、产权链、税费、抵押和留置记录决定资产能否使用、转让、继承或融资
  -> 记录错误、产权争议、地址错配、税费断点或灾害损毁会破坏住房与资产连续性
  -> 不动产记录连续性把居住和资产从事实占有转化为可被制度保护的长期资源
```

## 关键问题

- 不动产记录如何连接住房稳定、地址证明、金融抵押、继承和灾害恢复？
- 产权链断裂、地契错误、留置、税费欠缴或地址错误会影响哪些下游能力？
- 地方记录系统、纸质档案、数字地籍和灾害备份如何影响长期可追溯性？
- 产权保险、closing documents 和消费者披露如何降低交易中的信息不对称？

## 上游与下游

- 上游：`address-residency-mail-service-continuity/`、`housing-built-environment-stability/`、`geospatial-navigation-location-infrastructure/`、`trust-estate-affairs-succession-continuity/`。
- 下游：`financial-resilience-access/`、`tenant-screening-rental-access-continuity/`、`disaster-recovery-relief-continuity/`、`trust-estate-affairs-succession-continuity/`、`legal-identity-civil-registration/`。

## 非目标

- 不提供买房、卖房、房产税、产权调查、地契更正、产权保险、抵押、租赁、继承、拆迁、诉讼或法律建议。
- 不判断个人产权归属、税费责任、抵押有效性、地役权、边界、房产价值或交易风险。
- 不协助伪造、篡改、隐藏、转移或规避地契、产权、税费、抵押、留置或法院记录。

## 初始资料入口

- Local county recorder / register of deeds official offices
- CFPB: Mortgage closing and title insurance materials
- HUD: Housing counseling and fair housing materials
- FEMA: Disaster recovery property documentation materials
- State and local land records, tax assessor and cadastral data portals
