# Crane Derrick Hoist Rigging Suspended Load Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/crane-derrick-hoist-rigging-suspended-load-continuity` |
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

`crane-derrick-hoist-rigging-suspended-load-continuity/` 研究起重机、桅杆起重机、葫芦、吊装索具、悬吊载荷、指挥通信和坠落/碰撞/压伤如何影响工作者主体持续性。

核心问题：

> 当建设、制造和物流任务依赖重物提升时，主体能否不被悬吊载荷、失控吊装和沟通失败转化为压伤、创伤、死亡和长期劳动能力损失。

## 先验位置

```text
有效永生 / 主体持续性
  -> 主体需要通过施工、制造、维修和物料搬运获取资源
  -> 起重吊装把主体置于悬吊载荷、坠落物、碰撞、压伤和通信失效窗口
  -> 吊装失败会快速造成死亡、截肢、TBI、骨折和大出血
  -> 因此起重吊装安全是工业任务持续性的基础执行条件
```

## 关注对象

- Cranes、derricks、hoists、rigging、suspended loads、struck-by/crushed-by hazards、signal person、lift planning evidence boundary、exclusion zone。
- 风险链：提升任务 -> 载荷/索具/通信/区域控制失效 -> 坠落或摆动 -> 击打/压伤 -> 创伤、失能和停工。
- 制度链：qualified-person interface、inspection evidence、communication protocol、contractor coordination、incident reporting。

## Human Infra 模型位置

```text
起重吊装任务 T
  -> 改变悬吊载荷暴露 X
  -> 改变身体完整性和现场逃逸状态 S
  -> 改变急性死亡/压伤/击打风险 lambda(t)
  -> 改变有效工作年限、技能资本和未来选择权
```

## 非目标

- 不提供吊装方案、索具计算、载荷图使用、手势信号、设备操作、检查、认证、维修、施工、合规或现场安全方案。
- 不判断个人工伤、责任、赔偿、复工、事故调查、OSHA 违规或法律策略。
- 不帮助规避安全规则、绕开培训、隐藏事故、替代雇主安全计划或现场专业人员。

## Source Signals

- OSHA Crane, Derrick and Hoist Safety: https://www.osha.gov/cranes-derricks
- OSHA Workers: https://www.osha.gov/workers

## 下一步

- 建立 Suspended Load Continuity Card：load exposure、rigging evidence、communication boundary、exclusion zone、inspection evidence、rescue/EMS latency、incident reporting。
- 与 `occupational-exposure-industrial-hygiene/`、`human-factors-ergonomics-task-system-continuity/` 和 `trauma-system-hemorrhage-control-continuity/` 建立接口。
