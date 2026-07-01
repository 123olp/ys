# Pain And Suffering Control

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pain-suffering-control` |
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


Pain And Suffering Control 负责整理疼痛、痛苦、症状负担、姑息医学、生活质量和可承受持续性。

核心问题：

> 如果存在伴随持续痛苦，延长时间可能不再是价值增益；主体持续性必须同时考虑可感受状态和可承受性。

## 先验位置

```text
主体持续性最大化
  -> 主体不仅经历时间，也经历感受状态
  -> 慢性疼痛、症状负担和不可承受痛苦会摧毁有效时间
  -> 痛苦也会影响心理稳定、睡眠、行动和未来选择权
  -> 因此疼痛与痛苦控制是有效永生的质量边界
```

## 关注对象

- 慢性疼痛、癌痛、神经病理性疼痛、症状控制和姑息照护。
- 生活质量、可承受性、尊严、同意、治疗负担和终末期决策边界。
- 与 `mental-health-affective-stability/` 的关系：痛苦和心理稳定存在双向影响。
- 与 `governance-rights/` 的关系：痛苦控制必须保留同意、退出和尊严边界。

## Human Infra 模型链路

```text
疼痛 / 痛苦控制 T
  -> 改变痛苦强度、症状负担、睡眠、行动和心理状态 X
  -> 改变主体可承受状态 S
  -> 降低失能、自伤、治疗放弃和生活质量崩塌风险
  -> 增加有效时间和主体持续性的价值密度
```

## 非目标

- 不提供止痛药物、剂量、处方或个体医疗建议。
- 不把痛苦控制写成压制主体表达或延长不可承受状态的工具。
- 不替代紧急医疗、心理危机或姑息照护服务。

## Source Signals

- CDC Chronic Pain: https://www.cdc.gov/chronic-pain/
- WHO Palliative Care: https://www.who.int/news-room/fact-sheets/detail/palliative-care
