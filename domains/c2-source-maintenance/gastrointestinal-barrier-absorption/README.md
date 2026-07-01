# Gastrointestinal Barrier Absorption

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/gastrointestinal-barrier-absorption` |
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


Gastrointestinal Barrier Absorption 负责整理消化、吸收、肠道屏障、胃肠动力和营养进入身体系统的过程如何支撑主体持续性。

核心问题：

> 主体不只是需要食物，还需要把食物转化为可吸收、可耐受、可利用的物质输入；消化吸收失败会把营养、免疫、能量和行动能力同时拉低。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须持续获得可用营养和水分
  -> 食物必须经过消化、吸收、屏障过滤和肠道动力进入系统循环
  -> 吸收不良、慢性炎症、肠屏障破坏或胃肠动力失败会削弱营养、免疫、药物利用和恢复能力
  -> 因此消化屏障与吸收是主体持续性的基础输入域
```

## 关注对象

- 胃肠道消化、吸收、肠道屏障、黏膜免疫、胃肠动力和排泄连续性。
- 吸收不良、炎症性肠病、肠易激、胃肠感染、便秘、腹泻、吞咽和营养进入障碍。
- 药物吸收、营养利用、慢性炎症、脱水、微生物生态和生活质量之间的关系。
- 消化吸收状态如何进入营养代谢、微生物生态、免疫、体液稳态、药物安全和康复模型。

## Human Infra 模型链路

```text
消化吸收相关因素 T
  -> 改变营养吸收、屏障完整性、胃肠动力、炎症和水分电解质损失 X
  -> 改变主体能量、免疫、药物利用、恢复和有效行动状态 S
  -> 改变营养不良、感染、失能、急性脱水和长期疾病风险 λ(t)
  -> 影响健康寿命、有效时间和未来选择权
```

## 非目标

- 不提供胃肠疾病诊断、饮食处方、药物、补剂、益生菌、检查解释或治疗建议。
- 不把肠屏障、菌群或消化症状写成个体寿命判断。
- 不替代 `nutrition-metabolic-health/` 或 `microbiome-ecology/`，而是承载消化、吸收和屏障主接口。

## Source Signals

- NIDDK digestive diseases: https://www.niddk.nih.gov/health-information/digestive-diseases
- NIDDK digestive diseases statistics: https://www.niddk.nih.gov/health-information/health-statistics/digestive-diseases
- Intestinal permeability and aging review: https://pmc.ncbi.nlm.nih.gov/articles/PMC6385119/

## 下一步

1. 建立消化吸收变量表：吸收能力、屏障完整性、胃肠动力、脱水风险、炎症、药物吸收。
2. 与 `nutrition-metabolic-health/`、`microbiome-ecology/`、`immune-maintenance/` 和 `fluid-electrolyte-acid-base-homeostasis/` 建立交叉边界。
