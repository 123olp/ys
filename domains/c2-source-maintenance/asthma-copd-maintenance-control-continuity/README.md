# Asthma COPD Maintenance Control Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/asthma-copd-maintenance-control-continuity` |
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


`asthma-copd-maintenance-control-continuity/` 研究哮喘、COPD、长期气道控制、吸入药可及、触发因素、肺功能、急性加重预防和日常活动如何影响主体持续性。

> 核心问题：慢性气道疾病不只在急性发作时危险；长期控制失败会通过气短、睡眠破坏、运动受限、工作缺勤和急性加重风险持续压缩主体行动能力。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要稳定呼吸、运动耐受、睡眠和活动半径
  -> 哮喘/COPD 长期控制失败会造成症状负担、活动受限和急性加重
  -> 结果取决于诊断连接、吸入药可及、触发因素控制、行动计划和随访连续
  -> 因此慢性气道控制是呼吸持续性和有效时间保护的关键维护域
```

## 关注对象

- Asthma control、COPD maintenance、inhaler access, trigger control, spirometry access, pulmonary rehabilitation, exacerbation prevention, home oxygen interface, activity limitation。
- 与 `asthma-copd-exacerbation-airway-continuity/` 的边界：该域关注急性加重；本域关注日常长期控制和复发预防。
- 与 `respiratory-oxygenation/` 的关系：慢性气道病会把氧合、运动耐受和睡眠恢复连接起来。

## Human Infra 模型链路

```text
慢性气道长期控制系统 T
  -> 改变症状控制、肺功能、吸入药可及、触发暴露、康复和急性加重预防变量 X
  -> 改变睡眠、运动耐受、工作参与、急诊利用和行动半径状态 S
  -> 改变急性加重、住院、死亡风险、有效时间损耗和失能风险 λ(t)
  -> 影响主体呼吸储备、行动质量和未来选择权
```

## 非目标

- 不提供个人哮喘/COPD 诊断、肺功能判读、吸入药、剂量、氧疗、行动计划、急性发作处理、康复或设备建议。
- 不生成个人触发因素清单、药物调整、吸入器技术指导、旅行/工作限制或保险建议。
- 不收集个案肺功能、用药、氧饱和度、急诊、吸烟、职业暴露或设备资料。

## Source Signals

- NHLBI asthma: https://www.nhlbi.nih.gov/health/asthma
- NHLBI COPD: https://www.nhlbi.nih.gov/health/copd
- CDC asthma: https://www.cdc.gov/asthma/

## 下一步

- 建立 Airway Control Card：diagnosis access, symptom control, inhaler access, trigger exposure, rehabilitation, exacerbation prevention。
- 与 `respiratory-oxygenation/`、`asthma-copd-exacerbation-airway-continuity/` 和 `air-quality-ventilation-exposure-control/` 建立接口。
