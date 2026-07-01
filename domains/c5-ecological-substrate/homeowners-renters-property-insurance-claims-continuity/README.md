# 房主租客财产保险与理赔连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/homeowners-renters-property-insurance-claims-continuity` |
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

本域研究 homeowners insurance、renters insurance、condo insurance、personal property coverage、loss of use、deductible、exclusions、claims、inventory、proof of loss 和保单取消如何影响主体住房恢复、个人物品恢复和灾后临时生活。它关注家庭财产风险转移，而不是投保建议、理赔谈判或法律建议。

## 研究对象

- 房主险、租客险、condo insurance、个人财产、liability、loss of use、additional living expenses 和特殊限额。
- 保费、免赔额、replacement cost、actual cash value、exclusions、endorsements、保单续保、取消和非续保。
- 财产清单、照片记录、proof of loss、adjuster、维修估价、临时住宿、claim dispute 和州监管投诉。
- 与租住稳定、房贷、灾害恢复、家庭物品、家庭维修和责任保险的边界。

## 价值链路

```text
主体依赖住房和家庭物品维持日常运行
  -> 房主/租客保险把火灾、盗窃、风暴和责任风险转移到保单执行链
  -> 财产记录、清晰 coverage 和 loss-of-use 支付支持临时生活恢复
  -> 除外责任、低估、延迟、非续保或资料断裂会把灾害转成长期资源损失
  -> 家庭财产保险连续性把住所和物品恢复纳入可审查的风险转移系统
```

## 关键问题

- 房主险、租客险和 condo insurance 在主体恢复上有什么不同角色？
- replacement cost、actual cash value 和 deductible 如何改变恢复质量？
- 财产清单、proof of loss 和 adjuster 互动如何影响 claim 结果？
- loss of use 和临时住宿如何连接灾害住房恢复域？

## 上游与下游

- 上游：`housing-shelter-stability/`、`real-property-title-deed-record-continuity/`、`home-access-lock-key-entry-continuity/`。
- 下游：`disaster-housing-recovery-rebuilding-continuity/`、`household-maintenance-repair-contractor-continuity/`、`lodging-temporary-accommodation-access-continuity/`、`personal-liability-umbrella-insurance-defense-continuity/`。

## 非目标

- 不提供房主险、租客险、condo insurance、保额选择、财产清单估值、理赔、临时住宿、诉讼或法律建议。
- 不判断某个损失、保单、保险公司、adjuster、维修估价或赔付是否合理。
- 不协助虚假索赔、夸大损失、伪造收据、隐瞒风险、纵火、保险欺诈、骚扰房东/租客/理赔人员或规避保单条款。

## 初始资料入口

- NAIC: Homeowners and renters insurance consumer materials
- State insurance department homeowners / renters complaint materials
- FEMA and Ready.gov household disaster documentation materials
- FTC home repair scam consumer materials
