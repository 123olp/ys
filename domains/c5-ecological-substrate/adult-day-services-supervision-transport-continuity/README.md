# Adult Day Services Supervision Transport Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/adult-day-services-supervision-transport-continuity` |
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

`adult-day-services-supervision-transport-continuity/` 研究 adult day services、日间照护、监督、活动、健康观察、餐食和往返交通如何影响失能、认知衰退、孤立或照护者过载场景中的主体持续性。

> 核心问题：长期照护不只发生在家庭或机构。日间服务可以把白天监督、活动、餐食、社交、照护者喘息和交通组织成中间层，防止主体被困在“独自在家”和“机构化”之间。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体可能在部分失能、认知衰退或孤立状态中仍能参与社区
  -> 白天监督、活动、营养、交通和照护者喘息必须可连续
  -> adult day services 成为居家生活与机构照护之间的执行缓冲层
```

## 关注对象

- Adult day services、adult day health care、社会活动、监督、安全观察和日间结构。
- 往返交通、接送时间、活动参与、餐食、药物提醒边界和照护者工作时间。
- 痴呆、残障、老年脆弱、社交孤立和家庭照护过载场景。
- 与 `caregiving-long-term-care/`、`family-caregiver-respite-work-continuity/`、`home-delivered-meals-congregate-nutrition-services-continuity/` 的接口。

## Human Infra 模型链路

```text
成人日间服务基础设施
  -> 改变监督、活动、餐食、交通和照护者喘息变量
  -> 改变主体白天安全、社交参与和家庭照护负担状态
  -> 降低孤立、跌倒未发现、照护者退出和过早机构化风险
  -> 增加有效时间、关系参与和居家持续性
```

## 非目标

- 不推荐具体 adult day center、交通服务、项目质量或个人照护安排。
- 不判断资格、保险覆盖、Medicaid/HCBS、长期照护保险或费用责任。
- 不制定个人日间照护计划、活动计划、交通路线、药物提醒或安全监督方案。
- 不收集个人健康、认知、行为、照护者、住址、交通或支付资料。

## Source Signals

- Eldercare Locator: https://eldercare.acl.gov/
- ACL National Family Caregiver Support Program: https://acl.gov/programs/support-caregivers/national-family-caregiver-support-program
- Medicaid Home & Community Based Services: https://www.medicaid.gov/medicaid/home-community-based-services/index.html
- NIA Caregiving: https://www.nia.nih.gov/health/caregiving

## 下一步

- 建立 adult day services 变量表：监督时间、交通接续、活动参与、餐食、照护者喘息、服务中断和过早机构化风险。
- 整理 adult day、HCBS、respite 和 caregiver support 的 Source Cards。
