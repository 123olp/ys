# Home Oxygen Respiratory Equipment Supply Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/home-oxygen-respiratory-equipment-supply-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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


## 定位

本域研究居家氧疗、氧气浓缩机、便携氧、氧气瓶、CPAP/BiPAP、呼吸耗材、电力依赖、供应商补给和灾害备用路径如何影响呼吸脆弱主体的持续行动和安全。

它不是氧疗处方、设备设置、急救或维修操作入口。

## 先验问题

```text
呼吸支持何以离开医院后仍然连续？
  -> 氧气和呼吸设备必须在家中、路上和停电时可用
  -> 供应商、能源、耗材、维护和临床随访必须协同
  -> 否则主体持续性会被电力、配送或设备故障截断
```

## 研究对象

- Home oxygen、oxygen concentrator、portable oxygen、cylinders、tubing 和 consumables。
- CPAP/BiPAP、sleep apnea equipment、滤芯、面罩和维护支持。
- 电力依赖、停电登记、备用电源、灾害配送和出行限制。
- Medicare oxygen equipment coverage、supplier responsibility 和用户训练。

## 关键变量

- 氧气配送中断、设备停机时间、备用电源可用性和供应商响应。
- 耗材补给间隔、维护延迟、出行可携性和停电暴露。
- 呼吸支持依赖程度、环境暴露、热/烟雾灾害和能源脆弱性。

## 证据入口

- Medicare oxygen equipment 与 DME 资料。
- FDA / CDC / HHS emergency preparedness for electricity-dependent medical equipment 资料。
- 呼吸治疗、睡眠医学、灾害准备和居家医疗研究。

## 非目标

- 不提供氧流量、设备设置、急救、插管、CPAP 参数、维修或电力改装建议。
- 不判断某个氧疗、睡眠呼吸、设备、停电风险或供应商个案。
- 不收集处方、诊断、设备序列号、氧流量、住址、电力账户或医疗资料。

## 上下游

- 上游：`respiratory-oxygenation/`、`durable-medical-equipment-supplier-repair-continuity/`、`energy-access-resilience/`。
- 下游：`household-emergency-preparedness-resilience/`、`electric-grid-reliability-resilience-continuity/`、`home-health-hospice-palliative-care-continuity/`。
