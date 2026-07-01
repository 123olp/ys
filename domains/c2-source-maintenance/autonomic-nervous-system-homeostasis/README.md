# Autonomic Nervous System Homeostasis

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/autonomic-nervous-system-homeostasis` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 直接维护身体、脑、器官、衰老、损伤或生命系统这些可能性源体。 |
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


`autonomic-nervous-system-homeostasis/` 研究自主神经系统、交感/副交感平衡、心率变异性、体位性耐受、消化排尿调控、出汗和压力恢复，如何影响 Human Infra 的内环境稳定和有效时间。

> 核心问题：主体能否持续行动，不只取决于意识和肌肉，还取决于血压、心率、温度、消化、排尿、出汗和压力恢复这些自动调节是否稳定。自主神经失衡会把站立、进食、睡眠、工作和恢复都变成成本。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体行动依赖身体自动调节血压、心率、体温、消化、排尿、出汗和压力反应
  -> 自主神经失衡会造成晕厥、疲劳、脑雾、胃肠问题、热不耐受和恢复失败
  -> 若这些隐性调节失败被忽略，主体会在“没有明显器官衰竭”的情况下失去有效时间
  -> 因此自主神经稳态是连接神经、循环、内分泌、睡眠和恢复的调节域
```

## 关注对象

- 自主神经系统、交感/副交感调节、心率变异性、体位性低血压、POTS、晕厥、汗液调节和压力恢复。
- 长 COVID、糖尿病自主神经病变、神经退行、睡眠、体温、胃肠、泌尿和慢性疲劳相关调节问题。
- 与 `endocrine-hormonal-regulation/` 的边界：内分泌域关注激素反馈；本域关注神经性自动调节。
- 与 `cardiovascular-resilience/` 的边界：心血管域关注心血管结构和疾病；本域关注神经调控下的动态适应。

## Human Infra 模型链路

```text
自主神经稳态 T
  -> 改变心率、血压调节、体位耐受、温度调节、胃肠/泌尿功能、压力恢复和睡眠变量 X
  -> 改变站立、工作、学习、运动、恢复和日常活动耐受状态 S
  -> 改变晕厥、疲劳、脑雾、跌倒、失能、焦虑误判和有效时间损耗风险 λ(t)
  -> 影响行动密度、恢复能力、长期照护需求和主体持续性
```

## 非目标

- 不提供 POTS、晕厥、自主神经病变、HRV、补液、用盐、药物或运动处方建议。
- 不替代神经科、心脏科、内分泌科、康复医学或临床自主神经测试。
- 不把可穿戴 HRV、心率或血压读数写成个人诊断。

## Source Signals

- NINDS Dysautonomia: https://www.ninds.nih.gov/health-information/disorders/dysautonomia
- MedlinePlus Autonomic Disorders: https://medlineplus.gov/autonomicnervoussystemdisorders.html
- NIH POTS resources: https://www.nhlbi.nih.gov/health/postural-orthostatic-tachycardia-syndrome
- Heart Rhythm Society consensus on POTS and syncope: https://www.hrsonline.org/guidance/clinical-resources/2015-heart-rhythm-society-expert-consensus-statement-diagnosis-and-treatment-postural-tachycardia

## 下一步

- 建立自主神经变量表：心率、血压、体位耐受、HRV、出汗、胃肠、泌尿、睡眠、压力恢复、跌倒和有效时间。
- 与 `cardiovascular-resilience/`、`endocrine-hormonal-regulation/`、`sleep-circadian-recovery/`、`gastrointestinal-barrier-absorption/` 和 `thermal-homeostasis-resilience/` 建立接口。
