# Psoriasis, Inflammatory Skin and Systemic Burden Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/psoriasis-inflammatory-skin-systemic-burden-continuity` |
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


`psoriasis-inflammatory-skin-systemic-burden-continuity/` 研究银屑病、慢性皮肤炎症、关节/心代谢共病、疼痛瘙痒、污名、治疗可及和长期免疫治理如何影响主体持续性。

> 核心问题：银屑病不是只有皮肤斑块；它可能连接系统性炎症、关节功能、心理负担和长期治疗连续性。

## 先验位置

```text
有效永生
  -> 主体需要长期降低系统性炎症和功能税
  -> 银屑病可把皮肤炎症、共病风险、疼痛瘙痒和污名压力连接起来
  -> 慢性炎症负担会降低行动质量、社交参与和恢复能力
  -> 因此银屑病是皮肤炎症进入系统性持续性模型的执行域
```

## 关注对象

- Psoriasis, psoriatic disease, systemic inflammation, itch, pain, stigma, comorbidities, treatment continuity and access。
- 与 `autoimmune-rheumatic-disease-inflammatory-burden-continuity/` 的关系：后者关注自身免疫/风湿炎症总负担，本域关注皮肤表现和银屑病特异连续性。

## Human Infra 模型链路

```text
银屑病炎症治理连续性 T
  -> 改变皮肤炎症、疼痛瘙痒、关节/心代谢共病、污名和治疗可及 X
  -> 改变行动能力、心理负担、社会参与和系统炎症状态 S
  -> 改变失能、共病、治疗中断和生活质量下降风险 lambda(t)
  -> 改变有效时间、协作能力和未来选择权
```

## 非目标

- 不提供诊断、严重度评分、药物/生物制剂建议、关节症状判断、照片判断或个体治疗建议。
- 不输出个人共病风险、用药选择、保险策略或机构选择。

## Source Signals

- NIAMS psoriasis materials.
- MedlinePlus psoriasis materials.
- Dermatology and rheumatology guideline literature as contextual sources.
