# Confined Space Entry Atmospheric Hazard Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/confined-space-entry-atmospheric-hazard-continuity` |
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


`confined-space-entry-atmospheric-hazard-continuity/` 研究受限空间、缺氧、有毒/易燃气体、入口许可、监护、救援延迟和承包商交接如何影响主体持续性。

核心问题：

> 有些空间不是因为狭小危险，而是因为进入后空气、逃生、沟通和救援同时变成限制条件；一次进入失败可能造成多名人员连续伤亡。

## 先验位置

```text
有效永生 / 主体持续性
  -> 主体需要进入罐体、井道、管廊、坑洞等空间维护基础设施
  -> 这些空间可能包含缺氧、有毒、易燃或物理困陷风险
  -> 进入后退出和救援条件受限，旁人救援也可能成为二次伤亡
  -> 因此受限空间治理是基础设施维护与劳动安全的边界条件
```

## 关注对象

- Confined spaces、permit-required confined spaces、oxygen deficiency、toxic/flammable atmosphere、attendant、entry supervisor、rescue planning。
- 风险链：空间进入 -> 大气/物理危险 -> 监测/许可/通信失败 -> 倒地/困陷 -> 救援延迟/二次伤亡。
- 制度链：classification、permit system、atmospheric testing boundary、communication、rescue readiness、contractor coordination。

## Human Infra 模型位置

```text
受限空间任务 T
  -> 改变缺氧/毒性/困陷暴露 X
  -> 改变生命支持和退出状态 S
  -> 改变急性死亡/群体伤亡风险 lambda(t)
  -> 改变基础设施维护能力、工作年限和家庭恢复成本
```

## 非目标

- 不提供进入许可、气体检测、通风、救援、监护、PPE、分类、设备选择、现场程序或合规建议。
- 不判断个人事故、现场是否安全、救援行动、工伤、责任、OSHA 违规或法律策略。
- 不帮助冒险进入、规避 permit、隐藏事故、压缩救援准备或绕开专业人员。

## Source Signals

- OSHA Confined Spaces: https://www.osha.gov/confined-spaces
- OSHA Workers: https://www.osha.gov/workers

## 下一步

- 建立 Confined Space Continuity Card：space type、atmospheric hazard、entry control、communication、rescue latency、contractor boundary。
- 与 `chemical-safety-poison-control-toxicology/`、`industrial-process-safety-management-continuity/` 和 `emergency-medical-services-prehospital-care/` 建立接口。
