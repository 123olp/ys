# Dental Caries Prevention Restoration Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/dental-caries-prevention-restoration-continuity` |
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


`dental-caries-prevention-restoration-continuity/` 负责整理龋病、预防、修复可及性和牙体功能连续性。

核心问题：

> 龋病不是单颗牙的小问题；它通过疼痛、感染、缺课缺勤、咀嚼下降和修复成本，把主体的有效时间转化为可预防的摩擦。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能稳定进食、睡眠、学习、工作和参与社会
  -> 龋病会破坏牙体结构并触发疼痛、感染和修复需求
  -> 疼痛、感染和治疗成本会压缩注意力、时间、资源和任务执行能力
  -> 因此龋病预防与修复连续性是口腔功能和行动连续性的基础条件
```

## 关注对象

- 龋病、牙体结构损伤、牙痛、感染、修复需求和复发风险。
- 氟化物、窝沟封闭、饮食糖暴露、口腔卫生、学校和社区预防项目。
- 修复服务可及性、费用、预约等待、缺课缺勤和家庭照护负担。
- 与 `oral-health-continuity/` 的关系：本域聚焦龋病机制；总口腔域负责上位整合。

## Human Infra 模型链路

```text
龋病预防 / 修复服务 T
  -> 改变牙体完整性、疼痛、感染、咀嚼、费用和服务可及性变量 X
  -> 改变主体口腔功能和资源状态 S
  -> 改变睡眠中断、缺课缺勤、营养下降和急性牙科事件风险
  -> 增加有效时间、学习工作连续性和未来选择权
```

## 非目标

- 不提供龋齿诊断、X 光片判读、充填/根管/拔牙选择或个体治疗建议。
- 不推荐具体牙膏、药物、氟化物剂量、止痛方案或牙科产品。
- 不替代牙医、儿牙、公共卫生或学校牙科项目的专业评估。

## Source Signals

- WHO Oral Health: https://www.who.int/news-room/fact-sheets/detail/oral-health
- CDC Oral Health: https://www.cdc.gov/oral-health/
- NIDCR Tooth Decay: https://www.nidcr.nih.gov/health-info/tooth-decay

## 下一步

- 建立龋病 Source Card，区分预防证据、修复可及性和主体持续性终点。
- 对接儿童口腔、老年口腔、牙科可及性和急性牙痛域。
