# Veterans Health Benefits Navigation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/veterans-health-benefits-navigation-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

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

退伍军人健康、福利与导航连续性域研究：当主体从军队系统转入民用系统后，健康照护、福利资格、创伤支持、就业、住房、家庭和身份记录如何持续衔接。

## 对象

- VA health care、veterans benefits、service records、claims navigation、appeals boundary 和服务入口。
- 军转民、退役身份、健康记录、创伤暴露、残障补偿、就业培训、教育福利、住房支持和家庭照护。
- PTSD、TBI、慢性疼痛、肢体损伤、听力损失、物质使用、心理危机和长期照护连续性。
- 退伍军人服务组织、州/地方服务、社区照护、远程医疗、交通和数字账户访问。
- 身份证明、记录缺口、福利延迟、医疗转介、照护者负担和社会连接断点。

## Human Infra 价值

军队服务把主体放入高风险任务系统，退役又把主体推回复杂民用服务网络。退伍军人健康与福利导航域关注这种制度转换是否会切断医疗、收入、住房、记录、身份和家庭支持。

```text
军转民服务导航被结构化治理
  -> 医疗、福利、记录、住房、就业和家庭支持更连续
  -> 服役风险不被转嫁为退役后的孤立失能
  -> 主体恢复能力、行动能力和未来选择权提高
```

## 边界

本域只整理公开退伍军人健康、福利导航、服务衔接、记录、社区照护和家庭支持资料。

不提供：

- 个体福利申请、claims、appeals、医疗、心理危机、住房、就业或法律建议。
- 军事记录纠错、伤残等级、资格判断、补偿计算、诉讼或代理策略。
- 替代 VA、VSO、临床医生、危机热线、法律援助或政府服务的个案指导。
- 对退伍军人群体的创伤污名化、风险画像、招聘套利或商业获客方案。

## 上游与下游

- 上游：`healthcare-access-continuity/`、`mental-health-affective-stability/`、`housing-stability-affordability/`、`workforce-employment-services/`、`legal-identity-civil-registration/`。
- 下游：`suicide-crisis-response-continuity/`、`substance-use-treatment-recovery-continuity/`、`family-caregiver-respite-work-continuity/`、`disability-income-work-capacity-benefit-continuity/`、`education-access-lifelong-learning/`。

## 初始资料线索

- VA health care and benefits public resources。
- Veterans Crisis Line public materials, used only as service-system context。
- Department of Labor veterans employment resources and community veteran service organization materials。
