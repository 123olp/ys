# School Workplace Outbreak Operations Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/school-workplace-outbreak-operations-continuity` |
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

`school-workplace-outbreak-operations-continuity/` 研究学校、工作场所和公共服务组织在暴发期间如何通过运营规则、病假、替代路径和风险层级维持任务连续性。

> 核心问题：暴发会同时攻击健康、学习、收入、照护和组织运转；运营连续性决定控制措施是否能被真实执行。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体能力形成和资源获得依赖学校、工作场所和公共服务
  -> 暴发使这些组织在传播风险与开放需求之间摇摆
  -> 组织运营连续性把检测、隔离、通风、口罩和疫苗等措施编排成可执行制度
```

## 关注对象

- 学校运营、工作场所运营、病假、远程替代、分层措施、沟通、缺勤、照护接口、闭环反馈和公平影响。
- 与 `education-access-lifelong-learning/` 和 `occupational-work-design/` 的关系：本域只聚焦暴发状态下的组织运营连续性。

## Human Infra 模型链路

```text
学校与工作场所暴发运营
  -> 编排检测、隔离、通风、口罩、疫苗、病假和远程替代
  -> 改变传播风险、缺勤、学习损失、收入中断和照护压力
  -> 降低过度停摆、盲目开放和组织信任崩塌
  -> 增强学习连续、收入稳定、有效时间和主体持续性
```

## 非目标

- 不提供个案返校返工、HR 法律、学校纪律、劳动争议、医疗 clearance 或场所开放建议。
- 不提供规避病假、瞒报、证明伪造、检测规避、组织监控或惩罚机制。
- 不替代学校、雇主、本地卫生部门或法律专业判断。

## Source Signals

- CDC respiratory viruses guidance: https://www.cdc.gov/respiratory-viruses/guidance/
- CDC schools and childcare resources: https://www.cdc.gov/respiratory-viruses/guidance/schools-childcare.html
- OSHA COVID-19 and workplace safety resources: https://www.osha.gov/coronavirus
- U.S. Department of Education: https://www.ed.gov/

## 下一步

- 建立变量表：病假、缺勤、远程替代、学习损失、运营层级、风险沟通、工种差异、照护压力和公平影响。
- 与 `isolation-quarantine-work-school-continuity/`、`indoor-ventilation-filtration-outbreak-control-continuity/` 和 `mask-respirator-source-control-fit-access-continuity/` 建立接口。
