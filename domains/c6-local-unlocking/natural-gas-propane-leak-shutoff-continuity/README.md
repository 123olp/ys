# Natural Gas Propane Leak Shutoff Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/natural-gas-propane-leak-shutoff-continuity` |
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

`natural-gas-propane-leak-shutoff-continuity` 研究天然气、丙烷、燃料管线、泄漏识别、报警、撤离、关断责任和恢复检查如何影响家庭安全、供暖、烹饪和居住连续性。

> 核心问题：燃气是高能量家庭基础设施；它能支撑供暖和烹饪，也会在泄漏、误操作或恢复失败时迅速转化为爆炸、火灾和中毒风险。

## 关注对象

- 天然气、丙烷、燃气表、阀门、软管、炉具、供暖设备、泄漏气味、报警、撤离和恢复检查。
- 施工破坏、设备老化、灾后返家、租房责任、燃料中断、燃气恢复和公共通知。
- 与供暖、烹饪、CO 风险、消防、应急通信、管线安全和维修专业人员的接口。

## Human Infra 链路

```text
燃气与丙烷泄漏关断连续
  -> 高能量燃料使用保持可识别、可撤离、可专业恢复
  -> 泄漏、爆炸、火灾、CO 和灾后返家风险下降
  -> 供暖、烹饪和居住任务不被不可见燃料风险切断
  -> 主体家庭安全边界和恢复能力提高
```

## 非目标

- 不提供关阀操作教程、泄漏判断、设备维修、燃气恢复、管线施工、燃气表操作或现场安全许可。
- 不替代燃气公司、丙烷供应商、消防部门、911、持证 plumber/HVAC、管线安全机构或房东维修义务。
- 不把燃气可用性和安全性混为一谈；本域只研究燃料接口的识别、响应、专业恢复和任务连续性。

## Source Signals

- PHMSA Pipeline Leak Recognition and What to Do: https://www.phmsa.dot.gov/safety-awareness/pipeline/pipeline-leak-recognition-and-what-do
- USFA Home Heating Fire Safety: https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/heating/
- CDC Carbon Monoxide Poisoning Basics: https://www.cdc.gov/carbon-monoxide/about/index.html

## 下一步

- 建立 `fuel gas interface -> leak signal -> response boundary -> restoration state -> continuity outcome` 变量表。
- 区分天然气、丙烷、供暖、烹饪、灾后返家、施工破坏、租房责任和燃气恢复。
- 与 `carbon-monoxide-alarm-combustion-appliance-safety-continuity`、`fuel-thermal-energy-service-continuity` 和 `home-heating-equipment-chimney-vent-maintenance-continuity` 建立边界。
