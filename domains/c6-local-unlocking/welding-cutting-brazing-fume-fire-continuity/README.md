# Welding Cutting Brazing Fume Fire Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/welding-cutting-brazing-fume-fire-continuity` |
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


`welding-cutting-brazing-fume-fire-continuity/` 研究焊接、切割、钎焊、烟尘、热作业、火灾、爆炸、气瓶和受限空间接口如何影响工作者主体持续性。

核心问题：

> 当主体使用热、火花、金属烟尘和压缩气体完成制造维修任务时，能否不把生产能力转换成吸入损伤、烧伤、爆炸、火灾或长期肺部负担。

## 先验位置

```text
有效永生 / 主体持续性
  -> 主体需要通过焊接、切割和钎焊完成制造、维修和基础设施维护
  -> 热作业把主体置于烟尘、气体、火花、火灾、爆炸和密闭空间窗口
  -> 控制失败会造成急性烧伤、窒息、吸入损伤和长期肺部损害
  -> 因此焊接切割风险控制是技能工作持续性的基础执行条件
```

## 关注对象

- Welding、cutting、brazing、metal fumes、hot work、fire/explosion, gas cylinders、ventilation evidence boundary、confined-space fume/fire interface。
- 风险链：热作业任务 -> 烟尘/火花/气体/密闭空间暴露 -> 急性或慢性损伤 -> 呼吸功能、工作能力和未来选择权下降。
- 制度链：hazard identification、hot-work interface、ventilation evidence、fire watch boundary、incident reporting。

## Human Infra 模型位置

```text
焊接/切割/钎焊任务 T
  -> 改变烟尘、火灾和爆炸暴露 X
  -> 改变呼吸、皮肤、眼部和创伤状态 S
  -> 改变急性死亡/烧伤/慢性肺部负担风险 lambda(t)
  -> 改变技能工作年限、恢复成本和未来选择权
```

## 非目标

- 不提供焊接、切割、钎焊操作教程、热作业许可、通风设计、呼吸器选择、PPE、气瓶处理、消防监护、受限空间进入、合规或现场安全方案。
- 不判断个人职业病、工伤、责任、赔偿、复工、事故调查、OSHA 违规或法律策略。
- 不帮助规避安全规则、绕开培训、隐藏事故、替代雇主安全计划或现场专业人员。

## Source Signals

- OSHA Welding, Cutting, and Brazing: https://www.osha.gov/welding-cutting-brazing
- OSHA Workers: https://www.osha.gov/workers

## 下一步

- 建立 Hot Work Continuity Card：fume exposure、fire/explosion interface、gas cylinder boundary、confined-space interface、ventilation evidence、burn/respiratory outcome、incident reporting。
- 与 `occupational-exposure-industrial-hygiene/`、`burn-injury-critical-care-rehabilitation-continuity/` 和 `confined-space-entry-atmospheric-hazard-continuity/` 建立接口。
