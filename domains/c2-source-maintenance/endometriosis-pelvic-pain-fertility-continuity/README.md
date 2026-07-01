# Endometriosis Pelvic Pain Fertility Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/endometriosis-pelvic-pain-fertility-continuity` |
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


`endometriosis-pelvic-pain-fertility-continuity/` 研究子宫内膜异位症、慢性盆腔痛、炎症、诊断延迟、手术/药物路径、生育力、工作学习缺席和生活质量如何影响主体持续性。

> 核心问题：内异症不是“痛经更严重”这么简单，而是会通过疼痛、疲劳、不孕风险、诊断延迟、反复就医和污名长期压缩有效时间与未来选择权。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要可持续行动、可预测身体信号、疼痛可控和未来选择权
  -> 内异症可能造成慢性疼痛、炎症、疲劳、性交痛、生育困难和诊断延迟
  -> 痛苦被正常化或服务路径断裂时，主体会损失学习、工作、关系和生育规划窗口
  -> 因此内异症是疼痛、功能、生殖和医疗导航交叉的连续性域
```

## 关注对象

- Endometriosis、慢性盆腔痛、痛经、性交痛、疲劳、炎症、诊断延迟、影像/手术路径、生育力、工作学习参与和生活质量。
- 与 `menstrual-health-cycle-literacy-continuity/` 的边界：月经域关注周期素养和参与支持；本域关注内异症作为慢性炎症疼痛和生育风险机制。
- 与 `chronic-pain-functional-restoration-continuity/` 的边界：慢性疼痛域关注长期功能恢复总问题；本域关注盆腔、生殖和诊断延迟特异路径。
- 与 `reproductive-fertility-continuity/` 的关系：内异症是影响未来生育选择权的疾病机制之一，但不能简化为不孕结论。

## Human Infra 模型链路

```text
内异症识别与支持系统 T
  -> 改变盆腔痛、炎症、疲劳、诊断延迟、生育规划、工作学习支持和污名变量 X
  -> 改变主体有效时间、行动半径、关系安全、医疗信任、生殖选择权和恢复状态 S
  -> 改变慢性疼痛、缺席、心理负担、手术/用药风险、诊断延迟和未来选择受限 lambda(t)
  -> 影响主体行动质量、健康寿命、关系参与和长期计划
```

## 非目标

- 不提供内异症诊断、影像/腹腔镜解释、止痛药、激素治疗、手术、饮食、补剂、运动、性交痛处理、生育治疗或急诊判断。
- 不把月经疼痛、盆腔痛、性交痛、肠尿症状或不孕写成个人病因推断。
- 不收集个人月经、性生活、疼痛、影像、手术、用药、生育或精神健康资料。

## Source Signals

- MedlinePlus endometriosis: https://medlineplus.gov/endometriosis.html
- NICHD endometriosis: https://www.nichd.nih.gov/health/topics/endometri
- WHO endometriosis: https://www.who.int/news-room/fact-sheets/detail/endometriosis

## 下一步

- 建立 Endometriosis Continuity Card：pain burden, diagnostic delay, fertility planning, work/school participation, treatment burden, stigma。
- 与 `chronic-pain-functional-restoration-continuity/`、`reproductive-fertility-continuity/` 和 `patient-advocacy-shared-decision-making/` 建立接口。
