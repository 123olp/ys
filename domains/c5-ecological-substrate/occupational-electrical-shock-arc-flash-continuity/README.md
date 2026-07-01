# Occupational Electrical Shock Arc Flash Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/occupational-electrical-shock-arc-flash-continuity` |
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

`occupational-electrical-shock-arc-flash-continuity/` 研究职业电气暴露、电击、电弧闪爆、电弧爆炸、临时用电、架空线路和带电系统任务如何影响工作者主体持续性。

核心问题：

> 当工作任务接近电能系统时，主体能否不把维修、施工、检测和操作窗口转换成电击、烧伤、心律失常、爆炸创伤或死亡。

## 先验位置

```text
有效永生 / 主体持续性
  -> 主体需要在施工、维修、制造和公共服务中接触电能系统
  -> 电能把任务置于电击、触电死亡、电弧闪爆、烧伤和爆炸窗口
  -> 电气事故会快速造成心脏骤停、热损伤、创伤和长期功能损失
  -> 因此职业电气安全是技术工作持续性的基础执行条件
```

## 关注对象

- Occupational electrical exposure、electric shock、electrocution、arc flash/blast、temporary power、overhead lines、energized-system boundary、task authorization。
- 风险链：电气任务 -> 接近或接触带电系统 -> 电击/闪爆/爆炸 -> 死亡、烧伤、神经/心脏损伤和长期恢复。
- 制度链：hazard identification、authorization boundary、de-energization interface、training evidence、incident reporting。

## Human Infra 模型位置

```text
职业电气任务 T
  -> 改变电击/闪爆暴露 X
  -> 改变心脏、电神经、皮肤和创伤状态 S
  -> 改变急性死亡/烧伤/失能风险 lambda(t)
  -> 改变有效工作年限、技术技能资本和未来选择权
```

## 非目标

- 不提供电气施工、布线、带电作业、故障排查、电弧闪爆计算、PPE 类别、锁定挂牌、维修、设备操作、合规或现场安全方案。
- 不替代 `residential-electrical-wiring-outlet-safety-continuity/` 的家庭用电边界，也不替代 `hazardous-energy-lockout-tagout-continuity/` 的能量隔离边界。
- 不判断个人工伤、责任、赔偿、复工、事故调查、OSHA 违规或法律策略。

## Source Signals

- OSHA Electrical: https://www.osha.gov/electrical
- OSHA Workers: https://www.osha.gov/workers

## 下一步

- 建立 Electrical Continuity Card：energized exposure、shock path、arc-flash boundary、temporary/overhead power interface、authorization evidence、EMS latency、incident reporting。
- 与 `hazardous-energy-lockout-tagout-continuity/`、`burn-injury-critical-care-rehabilitation-continuity/` 和 `cardiac-arrest-cpr-defibrillation-continuity/` 建立接口。
