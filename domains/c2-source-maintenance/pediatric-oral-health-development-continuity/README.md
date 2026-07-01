# Pediatric Oral Health Development Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pediatric-oral-health-development-continuity` |
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


`pediatric-oral-health-development-continuity/` 负责整理儿童口腔健康、早期龋病、学校参与和发育连续性。

核心问题：

> 儿童口腔疾病会把一个可预防问题放大为疼痛、缺课、家庭照护、营养和发育参与的长期摩擦。

## 先验位置

```text
主体持续性最大化
  -> 主体能力从儿童期开始形成，学习、营养和家庭稳定是早期基础
  -> 早期龋病、牙痛和服务缺口会中断睡眠、上学、饮食和照护安排
  -> 儿童口腔问题会把家庭资源消耗转化为发展机会损失
  -> 因此儿童口腔健康是生命历程持续性和能力形成的前置条件
```

## 关注对象

- 早期儿童龋、换牙发育、牙痛、学校缺勤、营养、家庭照护和费用摩擦。
- 窝沟封闭、氟化物、学校牙科项目、家长健康素养和社区预防。
- 低收入、农村、残障儿童、语言可及性和保险覆盖差异。
- 与 `early-childhood-development-family-support-continuity/` 的关系：本域聚焦口腔入口；发育域负责上位儿童能力形成。

## Human Infra 模型链路

```text
儿童口腔预防 / 服务 T
  -> 改变早期龋病、牙痛、缺课、营养、家长时间和服务可及性变量 X
  -> 改变儿童发育和家庭资源状态 S
  -> 改变学习中断、睡眠不足、营养下降和家庭任务冲突风险
  -> 增加儿童能力形成、家庭稳定和长期主体持续性
```

## 非目标

- 不提供儿童牙科诊断、氟化物剂量、产品、镇静、矫治、治疗或急救建议。
- 不解释个体儿童牙齿发育是否正常。
- 不替代儿牙、学校卫生、儿科或公共卫生专业服务。

## Source Signals

- CDC Children's Oral Health: https://www.cdc.gov/oral-health/prevention/oral-health-children.html
- NIDCR Tooth Decay: https://www.nidcr.nih.gov/health-info/tooth-decay
- WHO Oral Health: https://www.who.int/news-room/fact-sheets/detail/oral-health

## 下一步

- 建立儿童口腔 Source Card，覆盖早期龋病、学校缺勤、预防项目和家庭资源压力。
- 对接儿童发育、学校服务、保险可及性和牙科急性事件域。
