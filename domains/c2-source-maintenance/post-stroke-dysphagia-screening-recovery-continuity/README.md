# Post Stroke Dysphagia Screening Recovery Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/post-stroke-dysphagia-screening-recovery-continuity` |
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


Post stroke dysphagia screening recovery continuity studies swallowing risk after stroke as a time-sensitive recovery and nutrition gateway connecting acute stroke care, aspiration prevention, nutrition planning, and rehabilitation.

核心问题：

> 卒中后的吞咽不是附属症状；它决定急性恢复期中营养、水分、药物、肺部风险和康复节奏能否接上。

## 先验位置

```text
主体持续性最大化
  -> 卒中后主体必须尽快恢复安全摄食、药物进入和康复参与
  -> 神经损伤可能扰动口咽吞咽和气道保护
  -> 筛查、转介和恢复链断裂会增加误吸、肺炎、脱水和住院负担
  -> 因而卒中后吞咽筛查恢复是急性脑连续性和营养入口之间的桥
```

## 关注对象

- 卒中后吞咽筛查、口咽吞咽风险、误吸、肺炎、营养水分、康复转介、恢复轨迹和照护沟通。
- 与 `cerebrovascular-stroke-brain-perfusion-resilience/` 的关系：卒中域关注脑灌注；本域关注卒中后的吞咽执行。
- 与 `aspiration-pneumonia-airway-protection-continuity/` 的关系：误吸肺炎域关注肺部后果；本域关注卒中特定入口路径。

## Human Infra 模型链路

```text
卒中吞咽筛查 / 转介 / 营养路径 / 康复协作 T
  -> 改变吞咽风险识别、口服安全、营养水分和肺部暴露变量 X
  -> 改变急性恢复、住院时长、康复参与和照护负担状态 S
  -> 改变误吸、肺炎、脱水、营养不足和再入院风险 λ(t)
  -> 影响恢复窗口、有效时间和未来选择权
```

## 非目标

- 不提供卒中急救、吞咽筛查操作、训练、饮食调整、转诊判断、影像/量表解释或个人预后。
- 不根据个人卒中症状、吞咽表现或病历判断风险和服务优先级。
- 不替代急诊、神经、言语语言治疗、康复、营养、护理或卒中团队。

## Source Signals

- AHA/ASA stroke care and dysphagia screening guideline signals。
- ASHA adult dysphagia materials。
- Stroke rehabilitation and aspiration prevention literature as research context。
