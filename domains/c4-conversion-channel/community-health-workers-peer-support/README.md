# Community Health Workers Peer Support

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/community-health-workers-peer-support` |
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

`community-health-workers-peer-support/` 研究社区健康工作者、同伴支持者、导航员和可信社区中介如何把医疗、公共卫生、社会服务和恢复支持连接到主体日常生活。

> 核心问题：服务存在不等于主体会信任、理解和持续使用；社区健康工作者与同伴支持把专业系统翻译为关系、陪伴、导航、反馈和低门槛支持。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须把医疗和社会服务嵌入日常生活
  -> 单靠机构入口、网页和临床建议不足以解决信任、语言、交通、文化、创伤和坚持问题
  -> 社区中介和同伴支持能降低服务导航成本并增强恢复关系
  -> 因此社区健康工作者与同伴支持是服务转化为实际行动的关系接口域
```

## 关注对象

- 社区健康工作者、peer support、patient navigator、promotoras、community link workers 和社会处方接口。
- 信任、文化/语言适配、健康教育、转介、随访、慢病支持、行为健康恢复和服务闭环。
- 培训、监督、边界、报酬、角色清晰度、数据隐私和非专业替代风险。
- 与 `community-resource-navigation/` 的边界：本域关注人际中介角色；资源导航域关注目录、筛查、转介和闭环系统。
- 与 `health-workforce-capacity/` 的边界：本域关注社区和同伴角色；健康劳动力容量域关注整体卫生人力系统。

## Human Infra 模型链路

```text
社区健康工作者与同伴支持 T
  -> 改变信任、语言适配、服务导航、持续陪伴、转介闭环和恢复支持变量 X
  -> 改变主体理解、进入、坚持和反馈医疗/社会服务的状态 S
  -> 改变服务脱落、慢病管理失败、复发、孤立、误解和恢复中断风险 λ(t)
  -> 影响健康寿命、行动能力、社会连接和未来选择权
```

## 非目标

- 不把社区健康工作者或同伴支持者写成医生、心理治疗师、急救人员、法律顾问或危机干预替代。
- 不提供诊断、治疗、用药、心理咨询、危机处理、个案转介或资格建议。
- 不支持无偿化、低薪化、过度任务转移、隐私越权或用社区关系替代制度责任。

## Source Signals

- WHO Community Health Workers guideline: https://www.who.int/publications/i/item/9789241550369
- CDC Community Health Workers: https://www.cdc.gov/community-health-workers/
- HRSA Community Health Worker Training Program: https://www.hrsa.gov/grants/find-funding/HRSA-22-124
- SAMHSA Peer Support Workers: https://www.samhsa.gov/brss-tacs/recovery-support-tools/peers
- CDC Health Equity: https://www.cdc.gov/health-equity/

## 下一步

- 建立社区中介变量表：信任、语言、文化适配、导航、随访、闭环、监督、培训、报酬和边界。
- 与 `healthcare-access-continuity/`、`community-resource-navigation/`、`mental-health-affective-stability/` 和 `social-connection-relational-infra/` 建立接口。
