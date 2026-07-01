# Medical ID Allergy Critical Alert Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/medical-id-allergy-critical-alert-continuity` |
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

Medical ID Allergy Critical Alert Continuity 研究 medical ID、过敏/不良反应、关键诊断、癫痫/糖尿病/抗凝等急救提示和可穿戴/手机急救信息如何在主体无法表达时被发现、理解和正确使用。

> 核心问题：很多急救风险不需要完整病历，先需要一个醒目、可信、不过度暴露隐私的关键警报。

## 研究对象

- Medical ID、medical alert bracelet/card、手机 emergency info、可穿戴急救信息和钱包卡。
- 药物过敏、食物过敏、严重不良反应、植入设备、抗凝、糖尿病、癫痫、肾上腺危机等关键提示。
- 发现概率、可信度、更新机制、语言可读性、隐私暴露和误标风险。

## 先验链路

```text
急救现场时间有限且主体可能无法沟通
  -> 完整病历通常不可立即访问
  -> 关键过敏、设备、病情和禁忌需要被快速发现
  -> Medical ID 和 critical alert 可把少量高价值信息暴露给急救链
  -> 信息若缺失、错误、过期或不可见，会增加误治、延误和伤害风险
  -> 因而医疗 ID 与关键警报是主体无法表达时的最低健康信号层
```

## 关键变量

- 警报类型、可见性、准确性、更新频率、验证来源和读取场景。
- 隐私最小化、语言/符号、照护者联系方式、设备依赖和紧急访问方式。
- 误报、漏报、过敏混淆、过度暴露身份和平台锁定风险。

## 证据入口

- MedlinePlus personal health records and emergency information materials.
- CDC chronic condition emergency preparedness materials.
- NLM/FDA device and health information materials.
- Emergency medical services and patient safety materials.

## 非目标

- 本域不判断某人是否需要 medical ID、写什么内容、是否过敏、是否停药或急救如何处置。
- 不提供医疗、急救、设备、药物、可穿戴、手机设置、产品推荐或法律建议。
- 不收集过敏史、诊断、药物、设备序列号、联系方式、定位或 PHI。

## 上下游

- 上游：`personal-health-record-emergency-summary-continuity/`、`allergy-adverse-reaction` 相关资料、`wearables-continuous-sensing-personal-informatics/`。
- 下游：`emergency-medical-services-prehospital-care/`、`medication-list-implant-device-emergency-continuity/`、`patient-safety-organizational-learning/`。
