# Demolition Structural Collapse Debris Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/demolition-structural-collapse-debris-continuity` |
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


`demolition-structural-collapse-debris-continuity/` 研究拆除作业、结构失稳、坍塌、坠落碎片、隐藏设施、相邻结构、粉尘和废弃物如何影响工作者与周边主体持续性。

核心问题：

> 当主体通过拆除和更新建成环境释放空间与材料时，能否不把建筑转换过程变成结构坍塌、碎片击打、暴露、火灾或长期恢复债务。

## 先验位置

```text
有效永生 / 主体持续性
  -> 主体需要通过拆除、改造和再开发更新建成环境
  -> 拆除作业把主体置于结构失稳、坠落碎片、隐藏设施和危险材料窗口
  -> 失控拆除会造成死亡、创伤、粉尘暴露、火灾和社区服务中断
  -> 因此拆除安全是建成环境更新过程中的主体持续性边界
```

## 关注对象

- Demolition、deconstruction、structural instability、collapse、falling debris、hidden utilities、adjacent structures、dust/debris、hazardous-material interface、sequencing evidence boundary。
- 风险链：拆除任务 -> 结构/碎片/设施/材料暴露 -> 坍塌、击打、污染、火灾 -> 工作者与周边主体持续性损伤。
- 制度链：pre-demolition survey evidence、engineering interface、contractor coordination、public protection boundary、incident reporting。

## Human Infra 模型位置

```text
拆除/改造任务 T
  -> 改变结构失稳和碎片暴露 X
  -> 改变身体完整性、环境暴露和服务连续状态 S
  -> 改变急性死亡/创伤/暴露风险 lambda(t)
  -> 改变工作年限、社区安全和未来选择权
```

## 非目标

- 不提供拆除计划、工程顺序、结构评估、支撑、爆破、废弃物清理、危险材料处理、许可、施工、合规或现场安全方案。
- 不判断个人工伤、责任、赔偿、复工、事故调查、OSHA 违规、建筑违规、保险或法律策略。
- 不帮助规避安全规则、隐藏事故、绕开培训、替代雇主安全计划、结构工程师或现场专业人员。

## Source Signals

- OSHA Demolition: https://www.osha.gov/demolition
- OSHA Workers: https://www.osha.gov/workers

## 下一步

- 建立 Demolition Continuity Card：structural-instability exposure、falling-debris boundary、utility/hazmat interface、adjacent-structure risk、public-protection evidence、incident reporting。
- 与 `building-fire-life-safety-codes/`、`occupational-exposure-industrial-hygiene/`、`waste-management-hazardous-materials-continuity/` 和 `trauma-system-hemorrhage-control-continuity/` 建立接口。
