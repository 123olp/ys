# HAZWOPER Responder PPE Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/hazwoper-responder-ppe-safety-continuity` |
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

`hazwoper-responder-ppe-safety-continuity/` 研究危险物质响应人员的培训、PPE、呼吸防护、热压力、污染转移、轮换和心理/组织支持如何决定事故响应是否可持续。

> 核心问题：如果响应者不能安全持续工作，公众保护、医疗转运、去污、环境监测和恢复都会失去执行主体。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 社区事故响应依赖一线响应者持续可行动
  -> 危险材料响应把毒性、缺氧、热压力、装备负担和组织压力集中到响应者身上
  -> HAZWOPER 与 PPE 安全把响应者保护转化为公共服务连续性条件
```

## 关注对象

- HAZWOPER、PPE、呼吸防护、训练、医疗监测、热压力、污染转移、轮班疲劳和机构责任。
- 与 `occupational-exposure-industrial-hygiene/` 的关系：工业卫生域关注长期工作暴露；本域关注应急响应者在危险材料事故中的保护和持续行动能力。

## Human Infra 模型链路

```text
响应者 PPE 与 HAZWOPER 安全
  -> 改变响应者伤害、疲劳、热压力、交叉污染和任务持续能力
  -> 改变事故控制、公众保护、医疗转运和恢复速度
  -> 支撑社区主体持续性和应急系统可信度
```

## 非目标

- 不提供 PPE 选择、穿脱、呼吸器适配、现场等级判断、训练替代或职业合规建议。
- 不提供进入危险区域、采样、去污、泄漏控制、消防或救援操作步骤。
- 不输出规避 HAZWOPER、规避 PPE、规避监管或降低安全标准的信息。

## Source Signals

- OSHA HAZWOPER: https://www.osha.gov/hazwoper
- OSHA respiratory protection: https://www.osha.gov/respiratory-protection
- NIOSH emergency response resources: https://www.cdc.gov/niosh/emres/
- NIOSH personal protective equipment: https://www.cdc.gov/niosh/ppe/

## 下一步

- 建立 Responder Safety Card：training, PPE, respiratory protection, heat/fatigue, contamination control, medical monitoring, staffing rotation。
- 与 `occupational-exposure-industrial-hygiene/`、`mask-respirator-source-control-fit-access-continuity/` 和 `health-workforce-capacity/` 建立接口。
