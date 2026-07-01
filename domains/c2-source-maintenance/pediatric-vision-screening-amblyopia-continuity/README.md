# Pediatric Vision Screening Amblyopia Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pediatric-vision-screening-amblyopia-continuity` |
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


`pediatric-vision-screening-amblyopia-continuity/` 负责整理儿童视力筛查、弱视、斜视/屈光风险、学校参与、家庭随访和视觉发育连续性。

核心问题：

> 儿童视觉不是成人视觉的缩小版；发育窗口内的弱视和未矫正视力问题，会把可处理的输入缺陷转化为学习、运动、自信和长期功能损失。

## 先验位置

```text
主体持续性最大化
  -> 主体能力从儿童阶段的感知、学习和运动反馈中逐步形成
  -> 视觉发育问题若错过筛查和随访窗口，会影响长期输入质量
  -> 弱视、斜视或未矫正屈光问题会压缩阅读、课堂参与、运动和发展机会
  -> 因此儿童视觉筛查与弱视连续性是生命历程早期能力形成基础设施
```

## 关注对象

- 儿童视力筛查、弱视、斜视、未矫正屈光问题、转诊和家庭随访。
- 学校、儿科、眼科、验光、保险/费用、家长理解和依从摩擦。
- 阅读、课堂参与、运动、发展、社交、自信和长期视觉功能。
- 与 `refractive-error-glasses-contact-lens-continuity/` 的关系：本域聚焦儿童发育窗口和弱视风险。

## Human Infra 模型链路

```text
儿童视力筛查 / 转诊 / 弱视管理衔接 T
  -> 改变早期发现、屈光矫正、家庭执行、随访和视觉发育变量 X
  -> 改变儿童阅读、课堂、运动、社交和能力形成状态 S
  -> 改变学习损失、发展机会丢失、长期视功能不足和家庭照护负担风险
  -> 增加早期能力形成、教育参与和未来选择权
```

## 非目标

- 不提供儿童视力诊断、弱视治疗方案、遮盖训练、眼镜度数、斜视手术建议或家长个体决策。
- 不根据筛查结果判断学校安排、运动资格、发育诊断或家庭责任。
- 不替代儿科、眼科、验光、学校筛查或特殊教育评估。

## Source Signals

- National Eye Institute Amblyopia: https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/amblyopia-lazy-eye
- CDC Vision Health: https://www.cdc.gov/vision-health/
- USPSTF Vision Screening in Children: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/vision-screening-in-children-ages-6-months-to-5-years

## 下一步

- 建立儿童视觉 Source Card，区分筛查、转诊、家庭执行、学校参与和长期能力终点。
- 对接儿童发展、教育记录、屈光矫正和家庭照护域。
