# Household Appliance Maintenance Repair Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/household-appliance-maintenance-repair-continuity` |
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

`household-appliance-maintenance-repair-continuity` 研究家用电器、设备维护、召回、维修、替换、能效和故障恢复如何影响家庭运行、食品保存、清洁、温控和日常任务连续性。

> 核心问题：家电不是消费品背景，而是家庭本地基础设施；冰箱、炉具、洗衣机、热水器、空调、路由器和关键小电器失效，会把食物、卫生、温控、照护和工作流一起拖入恢复成本。

## 关注对象

- 家用电器生命周期、维护、故障模式、维修可及、零件、保修、召回、替换和报废。
- 冰箱、冷冻柜、炉具、烤箱、洗衣机、烘干机、热水器、空调、取暖设备和家庭关键设备。
- 能效标准、能源负担、设备安全、火灾/电气/中毒风险、维修权、备件供应和服务窗口。
- 与能源、电网、产品安全、制造维修、家庭网络、食品安全和清洁卫生的接口。

## Human Infra 链路

```text
家用设备可维护
  -> 食物保存、烹饪、清洁、洗衣、温控和家庭照护工具持续运行
  -> 设备故障、召回、维修延迟、能耗和安全风险被提前识别
  -> 家庭日常任务从一次性劳动变成可恢复的本地服务系统
  -> 有效时间、健康环境、家庭韧性和主体恢复能力增强
```

## 非目标

- 不提供电气施工、燃气维修、拆机、绕过安全联锁、危险改装或具体维修步骤。
- 不替代专业维修、建筑规范、消防检查、产品召回处理或保修/法律判断。
- 不提供品牌推荐、购买建议、能效投资建议、理赔建议或个体维修决策。

## Source Signals

- U.S. CPSC Recalls: https://www.cpsc.gov/Recalls
- DOE Appliance and Equipment Standards Program: https://www.energy.gov/eere/buildings/appliance-and-equipment-standards-program
- ENERGY STAR Appliances: https://www.energystar.gov/products/appliances
- FTC Repair and home services consumer guidance: https://consumer.ftc.gov/

## 下一步

- 建立 `appliance function -> dependent task -> failure mode -> repair/replace path -> downtime cost` 变量表。
- 区分安全召回、能效、维修可及、备件供应、能源依赖和服务合同摩擦。
- 与 `product-safety-recall-systems`、`manufacturing-repair-capacity`、`energy-access-resilience` 和 `household-maintenance-repair-contractor-continuity` 建立边界。
