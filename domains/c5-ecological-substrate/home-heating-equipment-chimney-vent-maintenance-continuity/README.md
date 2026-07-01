# Home Heating Equipment Chimney Vent Maintenance Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-heating-equipment-chimney-vent-maintenance-continuity` |
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

`home-heating-equipment-chimney-vent-maintenance-continuity` 研究住宅供暖设备、烟囱、通风排气、燃料燃烧、维护记录和季节性启停如何影响冬季居住、安全睡眠、照护和恢复。

> 核心问题：供暖不是单纯温度，而是燃烧、排气、维护、通风和火灾/CO 风险共同构成的家庭生命支持接口。

## 关注对象

- furnace、boiler、fireplace、wood stove、chimney、venting、portable heater、燃料供应和季节性维护。
- 火灾、CO、通风不良、设备老化、清洁维护延迟、燃料中断和极端寒冷叠加。
- 老年人、儿童、慢病患者、低收入能源负担家庭、租房家庭和冬季停电场景。
- 与 CO 报警、烟雾报警、能源服务、冬季风暴、燃料可得和住房维修的接口。

## Human Infra 链路

```text
家庭供暖设备与排气维护连续
  -> 寒冷环境下室内温度、燃烧和排气边界更可靠
  -> 火灾、CO、冻伤、睡眠破坏和照护中断风险下降
  -> 居住、恢复、照护和慢病管理任务保持可执行
  -> 主体寒冷暴露风险下降并保持冬季行动窗口
```

## 非目标

- 不提供供暖设备维修、烟囱清理、燃气/油炉调试、空间加热器使用教程、排气判断或现场安全许可。
- 不替代 HVAC 专业人员、chimney professional、消防部门、能源公司、房东维修义务或应急服务。
- 不把高温供暖能力当成唯一目标；本域关注安全、可维护、可负担、可通风的供暖连续性。

## Source Signals

- USFA Home Heating Fire Safety: https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/heating/
- CDC Carbon Monoxide Poisoning Basics: https://www.cdc.gov/carbon-monoxide/about/index.html
- Ready.gov Winter Weather: https://www.ready.gov/winter-weather

## 下一步

- 建立 `heating equipment -> venting/maintenance state -> indoor thermal state -> household task -> continuity outcome` 变量表。
- 区分燃烧设备、电供暖、空间加热器、烟囱壁炉、租房维护和能源负担。
- 与 `carbon-monoxide-alarm-combustion-appliance-safety-continuity`、`winter-storm-cold-exposure-power-continuity` 和 `fuel-thermal-energy-service-continuity` 建立边界。
