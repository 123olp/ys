# Social Prescribing Community Referral Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/social-prescribing-community-referral-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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

- 界定外部承载条件：能源、水、食物、住房、通信、交通、治理、经济或公共基础设施。
- 说明它如何改变主体展开未来所需的稳定性、冗余、可获得性和安全边界。
- 记录基础设施依赖：供应链、地理环境、制度、资金、维护能力和公共服务。
- 识别冲击场景：灾害、战争、断供、污染、气候、系统失灵或社会支持崩溃。
- 建立韧性指标：可用率、恢复时间、冗余、成本、覆盖范围、可负担性和风险暴露。

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

Social Prescribing Community Referral Continuity 研究医疗、社会服务和社区组织如何把孤独、压力、慢病、自我管理和生活需求转介到非临床社区资源，并形成闭环反馈。

> 核心问题：很多主体风险不是单靠药物或一次咨询能解决；如果社区活动、福利、运动、同伴支持和生活服务不能被发现、转介和跟进，非临床支持就不会转化为真实行动。

## 研究对象

- Social prescribing、community referral、link worker、closed-loop referral、community activity 和 non-clinical support。
- 医疗机构、初级照护、社区组织、图书馆、运动项目、艺术文化活动、福利导航和同伴支持。
- 转介质量、资源目录、资格边界、回访、数据共享、同意和服务容量。

## 先验链路

```text
主体的健康和行动障碍常来自社会、情绪、生活和环境需求
  -> 临床系统需要把人连接到社区资源和非临床支持
  -> 资源目录、转介、同意、容量和反馈若断裂，支持无法真正到达
  -> 孤独、慢病管理、压力、经济和生活任务继续积累
  -> 临床系统被重复使用，主体有效时间和恢复能力下降
  -> 因而社会处方与社区转介是关系资源进入行动系统的接口
```

## 关键变量

- 转介完成率、闭环回访、资源可用性、等待时间、资格限制、交通/数字可达和文化适配。
- Link worker、community health worker、公共图书馆、社区中心、福利导航和医疗记录数据边界。
- 隐私、同意、服务目录过期、转介负担、资源不足、过度医疗化和责任转嫁风险。

## 证据入口

- NHS social prescribing and link worker materials。
- CDC / HHS social connectedness and community referral materials。
- Open Referral / 211 / Gravity Project social needs referral materials。

## 非目标

- 本域不推荐具体社区资源、治疗、活动、福利、社群、志愿者或社工。
- 不提供医疗建议、心理治疗、福利申请、转介代办、资格判断或个案导航。
- 不收集健康记录、社会需求、联系方式、转介记录、地址、收入、身份或服务使用数据。

## 上下游

- 上游：`loneliness-social-isolation-risk-continuity/`、`community-resource-navigation/`、`community-health-workers-peer-support/`。
- 下游：`third-place-belonging-social-participation-continuity/`、`volunteering-civic-service-participation-continuity/`、`mutual-aid-neighbor-support-network-continuity/`。
