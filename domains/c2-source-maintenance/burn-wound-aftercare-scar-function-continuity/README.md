# Burn Wound Aftercare, Scar and Function Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/burn-wound-aftercare-scar-function-continuity` |
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


`burn-wound-aftercare-scar-function-continuity/` 研究烧伤急性期之后的创面闭合、感染风险、瘢痕、挛缩、疼痛、温度调节、心理负担和功能恢复如何影响主体长期行动能力。

> 核心问题：烧伤不是急性抢救结束就完成；创面、瘢痕和功能恢复决定主体能否重新进入行动系统。

## 先验位置

```text
有效永生
  -> 主体必须从热损伤和皮肤边界破坏中恢复
  -> 烧伤后创面、瘢痕、挛缩、疼痛和感染会限制行动与生活执行
  -> 长期功能恢复决定急性生存能否转化为有效时间
  -> 因此烧伤后护理是急性创伤之后的皮肤-功能连续性域
```

## 关注对象

- Burn wound, aftercare, scar, contracture, infection, pain, thermoregulation, rehabilitation and psychosocial burden。
- 与 `burn-injury-critical-care-rehabilitation-continuity/` 的关系：后者关注烧伤急救和重症康复总域，本域聚焦创面后续、瘢痕和功能连续性。

## Human Infra 模型链路

```text
烧伤后创面和功能连续性 T
  -> 改变创面闭合、感染入口、瘢痕、挛缩、疼痛和康复执行 X
  -> 改变行动能力、皮肤屏障、热调节和心理负担 S
  -> 改变感染、失能、慢性疼痛和长期照护风险 lambda(t)
  -> 改变有效时间、社会参与和恢复质量
```

## 非目标

- 不提供烧伤急救、创面处理、敷料、感染判断、瘢痕治疗、康复动作或个体治疗建议。
- 不根据烧伤面积、照片或症状输出严重程度判断。

## Source Signals

- MedlinePlus burns materials.
- WHO burns fact materials.
- Burn rehabilitation and scar management literature as contextual sources.
