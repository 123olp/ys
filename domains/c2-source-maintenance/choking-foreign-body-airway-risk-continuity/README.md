# Choking Foreign Body Airway Risk Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/choking-foreign-body-airway-risk-continuity` |
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


Choking foreign body airway risk continuity studies acute airway obstruction from food or foreign material as a time-sensitive boundary between ordinary eating, emergency response, disability risk, and death.

核心问题：

> 窒息把进食从日常任务瞬间变成气道中断事件；它的价值不是提供急救教学，而是把高后果入口风险纳入系统设计。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能安全进食、饮水和参与公共餐食
  -> 食物或异物堵塞气道会快速切断氧合
  -> 时间敏感的气道失败会造成死亡、脑损伤和长期恐惧
  -> 因而窒息风险是吞咽入口和急性救援之间的高后果边界
```

## 关注对象

- 食物和异物气道阻塞、儿童/老年/残障风险、公共餐食环境、照护监督、食品形态和事件记录。
- 与 `mechanical-ventilation-respiratory-failure-continuity/` 的关系：通气域关注呼吸支持；本域关注入口异物导致的急性阻塞风险。
- 与 `emergency-preparedness-response/` 的关系：应急域关注响应系统；本域关注吞咽入口风险建模。

## Human Infra 模型链路

```text
风险识别 / 餐食设计 / 监督流程 / 应急可达 T
  -> 改变异物暴露、食品形态、照护监督和响应时间变量 X
  -> 改变气道安全、公共进食信心和照护负担状态 S
  -> 改变窒息、缺氧、脑损伤、死亡和长期回避风险 λ(t)
  -> 影响主体安全进食、有效时间和未来选择权
```

## 非目标

- 不提供海姆立克、儿童急救、气道清除、食物切割、吞咽训练、个案风险判断或现场处置。
- 不根据年龄、食物、症状或环境判断具体窒息风险和责任。
- 不替代急救培训、儿科、老年照护、言语语言治疗、营养、学校或餐饮安全服务。

## Source Signals

- MedlinePlus choking public-health materials。
- CDC child injury and older-adult safety materials as risk context。
- Food and long-term-care safety literature as research context。
