# Aspiration Pneumonia Airway Protection Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/aspiration-pneumonia-airway-protection-continuity` |
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


Aspiration pneumonia airway protection continuity studies how impaired swallowing, oral health, reflux, frailty, and care processes can allow material to enter the airway and become a lung-risk pathway.

核心问题：

> 误吸不是单个吞咽动作失败，而是入口、口腔、气道反射、肺部防御和照护流程同时失配后形成的呼吸风险链。

## 先验位置

```text
主体持续性最大化
  -> 主体必须同时维持营养进入和呼吸安全
  -> 误吸把入口材料带入气道和肺部
  -> 肺部感染、低氧、住院和衰弱会削弱恢复与行动
  -> 因而误吸肺炎是吞咽连续性和呼吸连续性之间的交叉失效模式
```

## 关注对象

- 误吸、口腔负荷、咳嗽防御、肺部脆弱性、口腔护理、卧床/衰弱、照护流程和住院风险。
- 与 `respiratory-oxygenation/` 的关系：呼吸域关注氧合；本域关注误吸进入肺部的上游风险链。
- 与 `oral-health-continuity/` 的关系：口腔域关注口腔健康；本域关注口腔负荷如何参与误吸肺部后果。

## Human Infra 模型链路

```text
吞咽识别 / 口腔护理 / 照护流程 / 营养路径 T
  -> 改变误吸暴露、口腔负荷、咳嗽防御和肺部脆弱性变量 X
  -> 改变呼吸安全、住院风险、恢复能力和照护负担状态 S
  -> 改变吸入性肺炎、低氧、败血症、失能和死亡风险 λ(t)
  -> 影响主体有效寿命、恢复窗口和未来选择权
```

## 非目标

- 不提供肺炎诊断、抗生素、氧疗、急救、吞咽动作、口腔护理处方或风险评级。
- 不根据症状、体温、咳嗽、影像、血氧或吞咽表现判断是否误吸或肺炎。
- 不替代急诊、呼吸、感染、言语语言治疗、牙科、护理或营养服务。

## Source Signals

- NIDCD dysphagia resources。
- ASHA dysphagia practice materials。
- CDC/NIH pneumonia and older-adult risk materials as public-health context。
