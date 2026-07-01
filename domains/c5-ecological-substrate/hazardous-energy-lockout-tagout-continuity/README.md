# Hazardous Energy Lockout Tagout Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/hazardous-energy-lockout-tagout-continuity` |
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


`hazardous-energy-lockout-tagout-continuity/` 研究控制危险能量、lockout/tagout、维修保养、意外启动、储能释放、交接和承包商协调如何影响主体持续性。

核心问题：

> 机器不是只在运行时危险；维护、清洁、调试和排障时，未隔离的能量会把正常任务变成截肢、挤压、电击、烧伤或死亡窗口。

## 先验位置

```text
有效永生 / 主体持续性
  -> 主体依赖机器扩大生产能力
  -> 机器系统储存电、机械、液压、气压、热、化学等能量
  -> 维护或清洁时若能量未被隔离，主体暴露于突发释放
  -> 因此危险能量控制是机器时代工作连续性的基础条件
```

## 关注对象

- Hazardous energy、lockout/tagout、energy isolation、service and maintenance、unexpected energization、stored energy、authorized/affected employees。
- 风险链：维护任务 -> 能量源未识别 -> 锁定失败/交接失败 -> 意外启动/释放 -> 创伤/死亡。
- 制度链：procedure、training、verification、shift handoff、contractor coordination、program audit。

## Human Infra 模型位置

```text
维修/维护任务 T
  -> 改变危险能量暴露 X
  -> 改变身体完整性和任务系统状态 S
  -> 改变急性创伤/死亡风险 lambda(t)
  -> 改变有效工作年限、学习积累和家庭资源
```

## 非目标

- 不提供 lockout/tagout 步骤、设备隔离方案、能量源识别、现场程序、培训材料、合规结论或检查表。
- 不判断个人事故、雇主责任、OSHA 违规、工伤、复工、索赔或法律策略。
- 不帮助绕过安全程序、伪造记录、恢复设备运行、规避停机或隐藏事故。

## Source Signals

- OSHA Control of Hazardous Energy: https://www.osha.gov/control-hazardous-energy
- OSHA Workers: https://www.osha.gov/workers

## 下一步

- 建立 Hazardous Energy Continuity Card：energy type、service context、isolation dependency、handoff risk、verification boundary、incident pathway。
- 与 `machine-guarding-amputation-prevention-continuity/`、`industrial-process-safety-management-continuity/` 和 `workers-compensation-occupational-injury-benefit-continuity/` 建立接口。
