# Disaster Temporary Housing Displacement Recovery Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/disaster-temporary-housing-displacement-recovery-continuity` |
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

`disaster-temporary-housing-displacement-recovery-continuity/` 研究灾后临时住房、过渡安置、租金援助、住房修复、可负担住房缺口和长期迁移如何影响主体恢复行动能力。

> 核心问题：灾害摧毁的不只是房屋，而是睡眠、储物、用药、儿童照护、工作通勤、通信和身份稳定；临时住房失败会把灾害转化为长期主体持续性损耗。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续性需要稳定睡眠、卫生、药物保存、照护和工作学习场所
  -> 灾害导致住房损坏、撤离、分散安置和长期流离
  -> 临时住房和修复路径决定主体能否从避险状态回到行动状态
  -> 因此灾后住房恢复是主体恢复连续性的核心域
```

## 关注对象

- FEMA temporary housing assistance、rental assistance、direct housing、HUD 灾后住房恢复、CDBG-DR 和地方安置系统。
- 住房损坏评估、临时租赁、无障碍住宿、家庭不分离、宠物/医疗需求、学校工作通勤和长期重建。
- 与 `evacuation-route-transportation-shelter-plan-continuity/` 的边界：该域关注灾前撤离与避难计划；本域关注灾后居住稳定。

## Human Infra 模型链路

```text
灾后临时住房与修复支持 T
  -> 改变住所可用性、安置稳定、卫生、通勤、药物保存和家庭照护变量 X
  -> 改变主体灾后生活基础状态 S
  -> 改变失眠、失学失业、治疗中断、家庭分离和迁移风险 λ(t)
  -> 影响有效时间、恢复能力和长期选择权
```

## 非目标

- 不提供房源推荐、资格判断、租约法律建议、保险理赔建议、占用规避或个案安置指导。
- 不收集地址、住房损失、家庭成员、移民身份、收入或医疗需求等敏感资料。
- 不替代 FEMA、HUD、地方住房机构、保险机构、房东租客法律援助或灾后个案管理。

## Source Signals

- FEMA Individual Assistance Housing: https://www.fema.gov/assistance/individual/housing
- FEMA Direct Housing: https://www.fema.gov/assistance/individual/direct-housing
- HUD Disaster Resources: https://www.hud.gov/program_offices/comm_planning/cdbg-dr
- DisasterAssistance.gov: https://www.disasterassistance.gov/
