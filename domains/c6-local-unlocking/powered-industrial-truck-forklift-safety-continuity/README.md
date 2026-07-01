# Powered Industrial Truck Forklift Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/powered-industrial-truck-forklift-safety-continuity` |
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

`powered-industrial-truck-forklift-safety-continuity/` 研究叉车和 powered industrial trucks 的驾驶、载荷、行人隔离、视线盲区、翻倒、撞击、培训和仓储节奏如何影响主体持续性。

核心问题：

> 物流和仓储把物资流动变成社会运行能力，但叉车把重载、速度、盲区和行人混行压缩到同一空间，安全失效会直接切断身体和供应链。

## 先验位置

```text
有效永生 / 主体持续性
  -> 主体依赖仓储、物流和制造场景获取物资与收入
  -> 叉车等工业车辆在共享空间移动重载
  -> 翻倒、撞击、夹挤和行人混行会造成急性死亡和长期失能
  -> 因此叉车安全是供应链执行与劳动持续性的共同条件
```

## 关注对象

- Powered industrial trucks、forklifts、operator training、pedestrian separation、load stability、tip-over、blind spots、warehouse traffic。
- 风险链：车辆/行人共享空间 -> 视线/载荷/速度失配 -> 撞击/翻倒/夹挤 -> 创伤/死亡 -> 供应和收入中断。
- 制度链：training、authorization、traffic management、maintenance、incident reporting、production pressure。

## Human Infra 模型位置

```text
仓储/物流任务 T
  -> 改变工业车辆与行人暴露 X
  -> 改变身体安全和供应执行状态 S
  -> 改变急性创伤/死亡风险 lambda(t)
  -> 改变物资连续性、工作年限和未来选择权
```

## 非目标

- 不提供叉车驾驶、载荷计算、培训、路线设计、仓库交通控制、检查表、维修、认证、合规或事故处理建议。
- 不判断个人驾驶资格、复工、责任、工伤、赔偿、OSHA 违规或法律策略。
- 不帮助绕过培训、降低安全间隔、提升产能压过安全或规避监管。

## Source Signals

- OSHA Powered Industrial Trucks - Forklifts: https://www.osha.gov/powered-industrial-trucks
- OSHA Workers: https://www.osha.gov/workers

## 下一步

- 建立 Forklift Safety Continuity Card：vehicle type、pedestrian interface、load/visibility risk、training boundary、traffic pattern、incident pathway。
- 与 `freight-logistics-port-cold-chain-continuity/`、`occupational-exposure-industrial-hygiene/` 和 `workers-compensation-occupational-injury-benefit-continuity/` 建立接口。
