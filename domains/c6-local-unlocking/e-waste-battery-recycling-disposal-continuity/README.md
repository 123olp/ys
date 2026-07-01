# E Waste Battery Recycling Disposal Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/e-waste-battery-recycling-disposal-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

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

`e-waste-battery-recycling-disposal-continuity` 研究家庭电子废弃物、锂离子电池、纽扣电池、可充电电池、设备报废、数据残留、回收点和电池火灾如何影响安全、隐私、材料循环和居住空间。

> 核心问题：现代主体依赖大量带电设备；当电池和电子废弃物没有安全回收与数据退役路径时，家庭空间会同时积累火灾、毒性、隐私和资源浪费风险。

## 关注对象

- 手机、电脑、平板、路由器、小家电、线缆、充电器、锂离子电池、纽扣电池、铅酸电池和可充电电池。
- 设备退役、数据清除边界、回收点、take-back、mail-back、零售回收、膨胀电池、损坏电池和热失控风险。
- 家庭办公、学习设备、医疗/辅助设备、儿童玩具、轮椅/代步车电池和灾后受损电子设备。
- 与个人设备生命周期、软件数据备份、电池热失控、辅助设备电池和家庭固废收运的接口。

## Human Infra 链路

```text
电子废弃物与电池回收处置连续
  -> 退役设备和电池能进入安全、合规、可追踪的回收或处置路径
  -> 火灾、毒性暴露、数据残留、儿童误吞和资源浪费风险下降
  -> 家庭设备更新、维修、替换和恢复任务不被旧设备堆积拖累
  -> 主体数字工具连续性、居住安全和材料循环能力提高
```

## 非目标

- 不提供电池拆解、刺穿、放电、改装、维修、数据恢复、数据擦除保证、回收套利、危险运输或损坏电池处理步骤。
- 不替代 EPA、地方回收项目、制造商/零售商 take-back、消防部门、CPSC、数据安全专业人员或危险废物渠道。
- 不判断某个膨胀电池、受损设备、旧硬盘、医疗设备电池或轮椅电池应如何个案处置。

## Source Signals

- EPA Used Household Batteries: https://www.epa.gov/recycle/used-household-batteries
- EPA Used Lithium-Ion Batteries: https://www.epa.gov/recycle/used-lithium-ion-batteries
- EPA Electronics Donation and Recycling: https://www.epa.gov/recycle/electronics-donation-and-recycling

## 下一步

- 建立 `device/battery retirement -> safety/privacy state -> recovery pathway -> household task -> continuity outcome` 变量表。
- 区分锂电、纽扣电池、铅酸电池、儿童玩具、个人计算设备、辅助设备电池和灾后受损电子设备。
- 与 `battery-thermal-runaway-fire-hazard-continuity`、`personal-computing-device-lifecycle-repair-continuity`、`wheelchair-scooter-battery-repair-access-continuity` 建立边界。
