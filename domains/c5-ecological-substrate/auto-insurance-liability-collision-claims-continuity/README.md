# 汽车保险、责任碰撞与理赔连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/auto-insurance-liability-collision-claims-continuity` |
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

本域研究汽车责任险、碰撞险、综合险、无保险/保险不足驾驶人、保费、免赔额、claim、adjuster、repair estimate、total loss、subrogation 和保单取消如何影响主体车辆移动、事故恢复和财产风险转移。它关注车辆风险转移执行层，而不是保险购买、事故责任判断、索赔策略或法律建议。

## 研究对象

- 汽车责任险、碰撞险、综合险、UM/UIM、医疗支付、租车报销和州最低责任要求。
- 保费、免赔额、limits、exclusions、proof of insurance、保单续保、取消和非续保。
- 事故报告、claim、adjuster、维修估价、total loss、salvage title、subrogation、投诉和监管入口。
- 与车辆登记、车贷收车、个人车辆维修、道路安全和法律责任的边界。

## 价值链路

```text
主体通过车辆获得日常移动能力
  -> 汽车保险把事故责任、维修费用和财产损失转移到保单执行链
  -> 清晰 coverage、理赔流程和维修估价降低事故后的移动中断
  -> 拒赔、延迟、低估、保单取消或责任争议会放大现金流和通勤风险
  -> 汽车保险连续性把车辆事故从单次事件转化为可恢复的移动风险治理
```

## 关键问题

- 责任险、碰撞险、综合险和 UM/UIM 分别覆盖哪些不同失败模式？
- 免赔额、limits、exclusions 和 total loss 如何影响真实恢复能力？
- 理赔、维修、车贷留置权和车辆登记如何相互作用？
- 保单取消、非续保和保费上升如何影响未来移动选择权？

## 上游与下游

- 上游：`driver-license-vehicle-registration-continuity/`、`personal-vehicle-maintenance-recall-repair-continuity/`、`auto-loan-lease-servicing-repossession-continuity/`。
- 下游：`debt-obligation-collection-relief-continuity/`、`transportation-access-mobility/`、`personal-liability-umbrella-insurance-defense-continuity/`、`road-traffic-injury-prevention-safe-mobility/`。

## 非目标

- 不提供汽车保险购买、保额选择、事故责任判断、claim 填写、维修选择、total loss 谈判、诉讼或法律建议。
- 不判断某个事故、保单、理赔、修理厂、保险公司或赔偿金额是否合理。
- 不协助伪造事故、虚假索赔、夸大损失、隐瞒驾驶人、逃避责任、保险欺诈、规避州保险要求或骚扰理赔人员。

## 初始资料入口

- NAIC: Auto insurance consumer materials
- State insurance department auto insurance and complaint materials
- USA.gov and state DMV proof-of-insurance materials
- FTC and official consumer auto repair / scam materials
