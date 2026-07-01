# Household Hazardous Waste Chemical Disposal Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/household-hazardous-waste-chemical-disposal-continuity` |
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

`household-hazardous-waste-chemical-disposal-continuity` 研究家庭危险废物、清洁剂、油漆、溶剂、农药、汽车化学品、易燃品和地方 HHW 回收日如何影响中毒、火灾、污染、儿童安全和居住卫生。

> 核心问题：家庭危险废物不是普通垃圾；当有毒、腐蚀、易燃或反应性材料没有安全的识别、暂存和处置入口时，居住空间会积累低频高后果风险。

## 关注对象

- 家庭危险废物、清洁化学品、油漆、溶剂、农药、汽车用品、含汞物品、易燃材料和未知旧容器。
- HHW drop-off、回收日、地方收集点、标签可读性、儿童接触、火灾风险、下水道/土壤/空气污染风险。
- 租房搬家、老人家庭、车库/地下室储存、多语种标签、灾后清理和物业集中处置场景。
- 与毒物控制、家庭清洁、农药标签、危险材料事故、非法倾倒和灾后废弃物清理的接口。

## Human Infra 链路

```text
家庭危险废物与化学处置连续
  -> 有毒、腐蚀、易燃或反应性家庭材料被识别并进入合规处置入口
  -> 中毒、火灾、儿童接触、下水道污染和非法混入风险下降
  -> 储藏、清洁、维修、搬家和灾后恢复任务不被危险材料拖累
  -> 主体居住安全、恢复速度和风险治理能力提高
```

## 非目标

- 不提供化学品混合、处理、稀释、燃烧、倾倒、下水道排放、危险废物运输、现场清理或容器打开教程。
- 不替代地方 HHW 项目、消防部门、毒物控制中心、EPA/RCRA 规则、物业、危险废物承包商、公共卫生或环境执法渠道。
- 不判断某个未知容器、泄漏、气味、暴露、火灾或儿童接触事件应如何个案处置。

## Source Signals

- EPA Household Hazardous Waste: https://www.epa.gov/hw/household-hazardous-waste-hhw
- Poison Help: https://www.poisonhelp.org/
- EPA Recycling Basics and Benefits: https://www.epa.gov/recycle/recycling-basics-and-benefits

## 下一步

- 建立 `chemical waste type -> hazard class -> access pathway -> exposure/fire/pollution risk -> continuity outcome` 变量表。
- 区分油漆、溶剂、农药、汽车用品、含汞物品、未知旧容器、搬家清空和灾后清理场景。
- 与 `chemical-safety-poison-control-toxicology`、`pesticide-label-exposure-poison-control-continuity`、`waste-management-hazardous-materials-continuity` 建立边界。
