# Battery Thermal Runaway Fire Hazard Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/battery-thermal-runaway-fire-hazard-continuity` |
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

`battery-thermal-runaway-fire-hazard-continuity/` 研究锂离子电池、储能系统、微出行设备、充电环境、热失控、火灾烟气、召回和消防/住房/能源接口如何影响主体持续性。

> 核心问题：电池让移动、通信、医疗设备和能源备份更强，但热失控会把便利工具转化为居住、交通、消防和空气暴露风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体越来越依赖电池化工具、移动设备、储能和备用电
  -> 电池失效可同时制造火灾、烟气、疏散、停电和住房断裂
  -> 电池热失控风险治理把能源工具收益纳入可持续、可居住、可恢复的边界
```

## 关注对象

- 锂离子电池、热失控、微出行、储能系统、充电场景、召回、消防风险、烟气暴露和多户住房风险。
- 与 `grid-scale-storage-flexibility-continuity/` 的关系：储能域关注电网灵活性；本域关注电池失效事故对家庭、建筑、消防和公共安全的影响。

## Human Infra 模型链路

```text
电池热失控火灾风险治理
  -> 改变火灾、烟气、疏散、设备可用性、召回和住房中断风险
  -> 改变有效时间、居住稳定、通信能源冗余和恢复成本
  -> 让电池化基础设施成为主体增强而不是反向风险
```

## 非目标

- 不提供电池改装、维修、拆解、充电方案、灭火操作、储能设计、产品推荐或现场处置。
- 不提供绕过 BMS、规避召回、危险运输、保险、法律、采购或企业合规建议。
- 不输出可帮助制造热失控、隐藏缺陷或降低安全边界的信息。

## Source Signals

- NFPA lithium-ion battery safety resources: https://www.nfpa.org/
- CPSC lithium-ion battery safety and recalls: https://www.cpsc.gov/
- UL Research Institutes battery safety: https://ul.org/
- OSHA fire safety and workplace context: https://www.osha.gov/fire-safety

## 下一步

- 建立 Battery Hazard Continuity Card：device class, charging context, recall signal, fire/smoke risk, housing interface, emergency power trade-off。
- 与 `backup-power-generator-safety-continuity/`、`building-fire-life-safety-codes/`、`product-safety-recall-systems/` 和 `grid-scale-storage-flexibility-continuity/` 建立接口。
