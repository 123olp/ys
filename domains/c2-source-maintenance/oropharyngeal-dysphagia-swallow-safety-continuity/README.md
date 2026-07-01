# Oropharyngeal Dysphagia Swallow Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/oropharyngeal-dysphagia-swallow-safety-continuity` |
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


Oropharyngeal dysphagia swallow safety continuity studies the oral-pharyngeal phase where food, liquid, saliva, medication, and airway protection must be coordinated before material reaches the esophagus.

核心问题：

> 入口资源只有安全越过口咽关口才算进入身体；口咽吞咽失效会把进食、饮水和服药变成误吸、窒息、疲劳和照护依赖。

## 先验位置

```text
主体持续性最大化
  -> 主体必须持续获得水分、能量、药物和进食参与
  -> 口咽阶段负责把入口材料送向食管并保护气道
  -> 口咽吞咽失效会增加残留、误吸、进食疲劳和沟通照护成本
  -> 因而口咽吞咽安全是营养入口与呼吸保护之间的执行层
```

## 关注对象

- 口腔准备、舌控制、咽期触发、喉保护、残留、咳嗽反应、湿嗓音和进食效率。
- 卒中、TBI、神经退行、头颈疾病、老年衰弱、重症后和药物相关吞咽风险。
- 与 `swallowing-dysphagia-aspiration-nutrition/` 的关系：父域关注吞咽总体；本域关注口咽阶段吞咽安全。
- 与 `aspiration-pneumonia-airway-protection-continuity/` 的关系：误吸肺炎域关注肺部后果；本域关注入口阶段机制。

## Human Infra 模型链路

```text
识别 / 评估 / 照护流程 / 环境调整 T
  -> 改变口咽控制、气道保护、进食效率和疲劳变量 X
  -> 改变营养水分进入、药物进入、肺部暴露和照护依赖状态 S
  -> 改变误吸、窒息、脱水、营养不良和住院风险 λ(t)
  -> 影响恢复窗口、有效时间、尊严和未来选择权
```

## 非目标

- 不提供吞咽诊断、吞咽造影/内镜解释、代偿动作、饮食调整、训练、急救或护理处置。
- 不根据个人症状、咳嗽、嗓音、影像或传感器数据判断风险等级。
- 不替代言语语言治疗、康复、营养、耳鼻喉、呼吸、神经或急诊服务。

## Source Signals

- NIDCD dysphagia resources。
- ASHA adult dysphagia practice materials。
- MedlinePlus swallowing disorders as public medical context。
