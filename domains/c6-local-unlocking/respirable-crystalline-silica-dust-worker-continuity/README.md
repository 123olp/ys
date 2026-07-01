# Respirable Crystalline Silica Dust Worker Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/respirable-crystalline-silica-dust-worker-continuity` |
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

`respirable-crystalline-silica-dust-worker-continuity/` 研究可吸入结晶硅尘、切割/打磨/钻孔/破碎作业、建筑粉尘、暴露监测和长期肺部负担如何影响工作者主体持续性。

核心问题：

> 当主体通过施工、石材、混凝土、采掘和制造任务获得收入时，能否不把粉尘暴露转换成硅肺、COPD、肺癌、肾病和长期有效时间损失。

## 先验位置

```text
有效永生 / 主体持续性
  -> 主体需要通过材料加工、施工和维护工作获取资源
  -> 含硅材料作业会产生可吸入结晶硅尘
  -> 长期或高强度暴露会增加不可逆肺部负担和死亡风险
  -> 因此硅尘暴露治理是劳动寿命和健康寿命的基础执行条件
```

## 关注对象

- Respirable crystalline silica、construction dust、cutting、grinding、drilling、abrasive blasting、engineered stone、silicosis、COPD、lung cancer、kidney disease、exposure monitoring evidence boundary。
- 风险链：含硅材料任务 -> 可吸入粉尘暴露 -> 肺部/肾脏长期损害 -> 工作能力、收入和未来选择权下降。
- 制度链：hazard identification、exposure assessment、control evidence、medical-surveillance boundary、incident/illness reporting。

## Human Infra 模型位置

```text
硅尘相关工作 T
  -> 改变可吸入结晶硅尘暴露 X
  -> 改变肺部炎症、纤维化和慢性病状态 S
  -> 改变职业病、失能和死亡风险 lambda(t)
  -> 改变有效工作年限、健康寿命和未来选择权
```

## 非目标

- 不提供暴露监测方案、工程控制、湿法/通风/除尘设计、呼吸器选择、医学监测解释、职业病诊断、合规或现场安全方案。
- 不替代 `occupational-exposure-industrial-hygiene/` 的广义工业卫生边界，也不替代 `radon-asbestos-indoor-hazard-continuity/` 的室内危险材料边界。
- 不判断个人职业病、工伤、责任、赔偿、复工、OSHA 违规或法律策略。

## Source Signals

- OSHA Silica, Crystalline: https://www.osha.gov/silica-crystalline
- OSHA Workers: https://www.osha.gov/workers

## 下一步

- 建立 Silica Continuity Card：task material、dust-generation process、exposure-evidence boundary、control evidence、latency window、medical-surveillance boundary、illness reporting。
- 与 `occupational-exposure-industrial-hygiene/`、`asthma-copd-maintenance-control-continuity/` 和 `lung-cancer-screening-treatment-continuity/` 建立接口。
