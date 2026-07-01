# Care Transitions Discharge Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/care-transitions-discharge-continuity` |
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

照护转移与出院连续性域研究：当主体在医院、急诊、康复、长期照护、家庭、社区和门诊之间移动时，信息、责任、药物、随访和恢复计划如何不断线。

## 对象

- 出院计划、照护转移、交接、复诊、转诊、再入院风险和闭环随访。
- 用药重整、出院说明、护理摘要、检查结果追踪、警示症状和家庭准备。
- 急诊到门诊、医院到康复、医院到居家、医院到长期照护和社区服务衔接。
- 医患沟通、照护者培训、患者门户、交通、语言、费用和行政负担。
- 照护转移失败对恢复窗口、有效时间、功能状态、死亡风险和未来选择权的影响。

## Human Infra 价值

主体从一个照护场景离开时，风险不会自动结束。照护转移是恢复路径中最容易丢失信息、责任和行动能力的断点。

```text
跨机构照护交接可追踪
  -> 出院后失联、用药错误、复诊失败和再入院风险下降
  -> 可修复状态进入持续恢复路径
  -> 主体恢复窗口和有效时间提高
```

## 边界

本域只整理公开出院计划、照护转移、交接、再入院、患者安全和服务衔接资料。

不提供：

- 个体出院判断、住院/转院/急诊决策、术后护理、警示症状判断或复诊安排。
- 个体用药、伤口、康复、护理、居家安全或医疗设备操作建议。
- 医疗纠纷、责任归属、保险索赔、机构选择或投诉策略。
- 把再入院风险模型写成确定个人预后或医院质量排名。

## 上游与下游

- 上游：`healthcare-access-continuity/`、`patient-data-interoperability/`、`medicine-access-treatment-continuity/`、`patient-safety-organizational-learning/`。
- 下游：`home-health-hospice-palliative-care-continuity/`、`caregiving-long-term-care/`、`rehabilitation-functioning/`、`community-resource-navigation/`。

## 初始资料线索

- AHRQ Care Coordination: https://www.ahrq.gov/ncepcr/care/coordination.html
- AHRQ care transitions and discharge planning public materials。
- CMS discharge planning and quality reporting public materials。
- Public materials on medication reconciliation, readmissions and warm handoffs。

## 下一步

- 建立照护转移变量表：出院资料完整性、药物重整、随访完成、交通可达、照护者可用性和再入院风险。
- 整理 AHRQ、CMS 和患者安全照护转移 Source Cards。
- 明确与长期照护、居家医疗、社区资源导航和患者数据互操作的边界。
