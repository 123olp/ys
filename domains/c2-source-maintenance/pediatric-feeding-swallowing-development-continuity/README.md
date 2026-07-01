# Pediatric Feeding Swallowing Development Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pediatric-feeding-swallowing-development-continuity` |
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


Pediatric feeding swallowing development continuity studies early feeding, swallowing, oral-motor, sensory, growth, caregiver, and school/daycare participation pathways as conditions for child development.

核心问题：

> 儿童摄食不是小号成人吞咽；它同时牵动发育、增长、家庭压力、感官经验、学校参与和长期能力积累。

## 先验位置

```text
主体持续性最大化
  -> 儿童必须通过稳定摄食获得增长、能量和早期参与经验
  -> 摄食吞咽发展连接口腔运动、感官、照护、营养和关系
  -> 发展窗口中的摄食失败会影响增长、学习、家庭负担和社会参与
  -> 因而儿童摄食吞咽是生命早期主体持续性和能力形成的入口基础设施
```

## 关注对象

- 婴幼儿和儿童摄食、吞咽、口腔运动、挑食/限制、感官负担、增长、照护者压力和学校/日托餐食。
- 与 `developmental-language-disorder-child-communication-continuity/` 的关系：语言域关注沟通；本域关注摄食吞咽。
- 与 `wic-benefit-redemption-infant-maternal-nutrition-continuity/` 的关系：WIC 域关注营养福利兑换；本域关注摄食能力和照护执行。

## Human Infra 模型链路

```text
早期识别 / 家庭支持 / 学校餐食协作 / 专业服务 T
  -> 改变摄食技能、吞咽安全、感官负担、增长和家庭压力变量 X
  -> 改变营养状态、学习参与、家庭恢复和发展窗口状态 S
  -> 改变营养不足、脱水、误吸、增长失败和照护崩溃风险 λ(t)
  -> 影响儿童能力积累、有效学习时间和未来选择权
```

## 非目标

- 不提供儿童诊断、喂养计划、食物引入、质地调整、训练、过敏处理、学校服务资格或责任判断。
- 不根据儿童进食表现、增长、偏好或感官反应判断病因和风险。
- 不替代儿科、言语语言治疗、营养、职业治疗、学校护理或早期干预服务。

## Source Signals

- ASHA pediatric feeding and swallowing practice materials。
- CDC infant and child nutrition materials as context。
- AAP and pediatric feeding literature as research context。
