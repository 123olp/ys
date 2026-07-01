# Disaster Recovery Relief Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/disaster-recovery-relief-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 主要提供主体展开未来所需的基础环境、资源、治理或基础设施。 |
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

`disaster-recovery-relief-continuity/` 研究灾后个人援助、恢复中心、临时安置、灾害贷款、救济服务和家庭恢复路径如何防止一次灾害清零主体长期积累。

> 核心问题：灾害结束不等于主体恢复；住房、现金、食物、文件、通信、医疗、债务和临时安置断裂，会把一次事件变成长期能力损耗。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体会遭遇灾害、事故、火灾、风暴、洪水和其他低频高冲击事件
  -> 事件后必须有恢复资金、临时住所、食物、文件、医疗、贷款和服务入口
  -> 灾后恢复失败会造成长期失能、贫困、迁移、关系断裂和资源损失
  -> 因此灾后恢复与救济连续性是主体持续性的尾部风险恢复域
```

## 关注对象

- 灾后个人援助、恢复中心、临时安置、开放避难所、灾害贷款、账单/食物支持和官方救济入口。
- 恢复时间、申请摩擦、文件丢失、身份连续、住房连续、债务压力和跨机构转介。
- 与 `emergency-preparedness-response/` 的边界：本域关注事件后的恢复与救济；应急准备与响应关注事前准备和事件中响应。

## Human Infra 模型链路

```text
灾后恢复与救济系统 T
  -> 改变资金、住房、食物、文件、医疗、贷款、安置和服务导航变量 X
  -> 改变主体灾后恢复状态 S
  -> 改变无家可归、医疗中断、债务升级、迁移、失业和长期能力损耗风险 λ(t)
  -> 影响主体恢复窗口、资源复原、家庭连续性和未来选择权
```

## 非目标

- 不提供个体灾害申请、资格判断、理赔、贷款、法律、税务、保险或住房建议。
- 不承诺避难所实时可用、资金发放、资格结果、灾害认定或恢复时间。
- 不支持虚假申请、身份冒用、材料伪造、囤积、黑市采购或制度规避。

## Source Signals

- USA.gov Disaster Assistance: https://www.usa.gov/disaster-assistance
- FEMA Disaster Recovery Centers: https://egateway.fema.gov/ESF6/DRCLocator
- SBA Disaster Assistance: https://www.sba.gov/funding-programs/disaster-assistance
- Benefits.gov Disaster Relief: https://www.benefits.gov/categories/Disaster%20Relief
- American Red Cross Open Shelters: https://www.redcross.org/get-help/disaster-relief-and-recovery-services/find-an-open-shelter.html
- Global Shelter Cluster: https://sheltercluster.org/

## 下一步

- 建立变量表：恢复资金、临时住所、文件恢复、食品援助、医疗连续、债务压力、申请摩擦和服务转介。
- 与 `emergency-alerts-communications/`、`social-protection-benefits-delivery/`、`insurance-risk-transfer/` 和 `housing-built-environment-stability/` 建立接口。
