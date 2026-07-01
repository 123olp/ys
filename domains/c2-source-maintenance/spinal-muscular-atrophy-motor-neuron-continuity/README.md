# Spinal Muscular Atrophy Motor Neuron Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/spinal-muscular-atrophy-motor-neuron-continuity` |
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


`spinal-muscular-atrophy-motor-neuron-continuity/` 研究脊髓性肌萎缩症、遗传性运动神经元功能、呼吸/吞咽/移动支持、儿童发展和长期照护连续性如何影响主体持续性。

## Core Question

当遗传性运动神经元疾病从儿童或成人阶段改变肌力、呼吸、吞咽和移动能力时，主体如何保留发育、学习、参与、沟通和照护承接能力？

## 先验位置

- 与 `neuro-continuity/` 的关系：SMA 是遗传性运动神经元病程，不是一般肌力下降。
- 与 `maternal-newborn-child-development/` 的关系：早发类型会直接影响儿童发展和家庭照护系统。
- 与 `respiratory-oxygenation/` 的关系：呼吸支持和感染风险是持续性关键边界。

## 关注对象

- 肌无力、发育里程碑、呼吸、吞咽、营养、移动辅助、基因治疗/药物可及、照护负担和学校参与。
- 新生儿筛查、早期治疗窗口、长期随访、安全监测和家庭资源。

## Human Infra 模型链路

```text
遗传性运动神经元功能受损
-> 肌力、呼吸、吞咽、移动和发育支持需求改变
-> 学习、家庭照护、学校参与和长期独立性受影响
-> 未来选择权与主体持续性被压缩
```

## 非目标

- 不提供 SMA 诊断、基因检测解释、治疗选择、基因疗法、药物、呼吸/营养设备、学校服务或照护建议。
- 不输出儿童发育判断、预后、治疗窗口、保险或临床试验建议。

## Source Signals

- NINDS spinal muscular atrophy: https://www.ninds.nih.gov/health-information/disorders/spinal-muscular-atrophy

## 下一步

- 建立 SMA continuity card：区分筛查、早期治疗信号、呼吸/吞咽、移动和儿童发展边界。
