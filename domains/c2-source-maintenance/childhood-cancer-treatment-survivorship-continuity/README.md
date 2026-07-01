# Childhood Cancer Treatment Survivorship Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/childhood-cancer-treatment-survivorship-continuity` |
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


`childhood-cancer-treatment-survivorship-continuity/` 研究儿童癌症治疗强度、家庭照护、教育中断、发育影响、心理社会支持、长期幸存者晚期效应和过渡照护如何影响主体持续性。

> 核心问题：儿童癌症不仅是儿童期生存问题；治疗会穿过发育、学习、家庭经济、父母劳动、长期器官功能和成年后的幸存者照护。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续性从儿童期就受到重大疾病和治疗毒性的塑形
  -> 儿童癌症治疗、教育中断、家庭照护和晚期效应改变整个人生路径
  -> 发育、学习、心理、器官功能和成人过渡照护决定长期有效时间和能力系统
  -> 因此儿童癌症是癌症连续性中的生命早期路径塑形域
```

## 关注对象

- Childhood cancers, treatment burden, family caregiving, school disruption, developmental effects, psychosocial support, late effects, transition to adult survivorship care。
- 与 `child-development-family-infrastructure/` 和 `education-learning-infrastructure/` 的关系：儿童癌症会改变发育、学习、家庭和学校连续性。
- 与 `cancer-survivorship-late-effects-continuity/` 的关系：儿童期治疗晚期效应常持续到成人期。

## Human Infra 模型链路

```text
儿童癌症连续性系统 T
  -> 改变治疗强度、家庭照护、教育中断、发育支持、心理支持和长期随访变量 X
  -> 改变生存、器官功能、学习路径、家庭资源、心理状态和成人过渡状态 S
  -> 改变死亡、发育损失、长期失能、有效时间损失和家庭资源消耗 λ(t)
  -> 影响主体健康寿命、能力形成、家庭系统和未来选择权
```

## 非目标

- 不提供儿童癌症诊断、分期、治疗方案、临床试验选择、药物剂量、学校服务申请、家庭个案处理、预后判断或个体建议。
- 不生成儿童癌症风险计算器、治疗排序、晚期效应预测器、教育安置建议或商业检测推广。
- 不收集个案儿童诊断、病理、治疗、学校、发育、家庭、心理或随访资料。

## Source Signals

- NCI childhood cancers: https://www.cancer.gov/types/childhood-cancers
- NCI childhood cancer survivorship: https://www.cancer.gov/types/childhood-cancers/survivorship
- CDC childhood cancer: https://www.cdc.gov/cancer/dcpc/research/articles/childhood_cancer.htm

## 下一步

- 建立 Childhood Cancer Continuity Card：treatment burden, family caregiving, school continuity, development, psychosocial support, late effects, transition care。
- 与 `child-development-family-infrastructure/`、`education-learning-infrastructure/` 和 `cancer-survivorship-late-effects-continuity/` 建立接口。
