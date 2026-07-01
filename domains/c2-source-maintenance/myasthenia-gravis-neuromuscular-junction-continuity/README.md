# Myasthenia Gravis Neuromuscular Junction Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/myasthenia-gravis-neuromuscular-junction-continuity` |
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


`myasthenia-gravis-neuromuscular-junction-continuity/` 研究重症肌无力、神经肌肉接头传递、波动性肌无力、眼咽呼吸风险、感染/药物触发和行动连续性如何影响主体持续性。

## Core Question

当神经肌肉接头传递不稳定导致力量和呼吸/吞咽能力波动时，主体如何维持安全行动、表达、工作节律、急性风险治理和服务承接？

## 先验位置

- 与 `neuro-continuity/` 的关系：MG 是神经肌肉接头传递失败，不是中枢神经病灶。
- 与 `immune-maintenance/` 的关系：自身免疫机制和免疫治疗风险需要独立边界。
- 与 `respiratory-oxygenation/` 的关系：肌无力危象可直接进入呼吸安全边界。

## 关注对象

- 波动性肌无力、眼肌/咽喉/呼吸受累、疲劳、触发因素、感染、免疫治疗、急性危象边界和工作/照护适配。
- 诊断延迟、专科可及、药物相互作用风险、急性服务识别和生活参与。

## Human Infra 模型链路

```text
神经肌肉接头传递不稳定
-> 肌力、吞咽、呼吸和日内功能波动
-> 行动安全、工作节律和急性风险治理需求增加
-> 有效时间与主体控制权下降
```

## 非目标

- 不提供 MG 诊断、抗体/肌电判读、药物、免疫治疗、胸腺手术、危象处理、用药禁忌或活动建议。
- 不输出个体急诊判断、驾驶/工作许可、药物清单审查或治疗资格结论。

## Source Signals

- NINDS myasthenia gravis: https://www.ninds.nih.gov/health-information/disorders/myasthenia-gravis

## 下一步

- 建立 neuromuscular-junction card：区分波动性、触发因素、呼吸/吞咽和急性服务边界。
