# Caregiver Health Burnout Screening Support Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/caregiver-health-burnout-screening-support-continuity` |
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


`caregiver-health-burnout-screening-support-continuity/` 研究照护者健康、负担、睡眠、抑郁焦虑、肌骨损伤、社会隔离、筛查、支持服务和恢复资源如何影响家庭照护系统是否可持续。

> 核心问题：照护者不是背景资源，而是另一个主体。若照护者健康、睡眠、收入和心理稳定被持续消耗，被照护者的持续性也会失去支撑。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 长期照护依赖照护者持续存在、行动、恢复和判断
  -> 照护者自身也会受到睡眠损耗、压力、孤立、损伤和收入冲击
  -> 因此照护者健康和 burnout 支持是双主体持续性条件
```

## 关注对象

- Caregiver burden、burnout、sleep loss、depression/anxiety、musculoskeletal strain、financial strain 和 social isolation。
- 负担筛查、同伴支持、咨询转介、respite 连接、工作支持和社区资源导航。
- 痴呆照护、严重疾病、儿童复杂照护、残障支持和长期家庭照护。
- 与 `mental-health-affective-stability/`、`social-connection-relational-infra/`、`family-caregiver-respite-work-continuity/` 的接口。

## Human Infra 模型链路

```text
照护者健康支持
  -> 改变睡眠、压力、情绪、身体损伤、社会支持和恢复资源
  -> 改变照护者持续行动状态和家庭照护系统稳定性
  -> 降低 burnout、照护中断、忽视/冲突、收入退出和危机迁移风险
  -> 同时保护照护者与被照护者主体持续性
```

## 非目标

- 不提供心理诊断、治疗、危机处置、用药、家庭关系裁决或法律建议。
- 不筛查或评估具体照护者 burnout、抑郁、焦虑、虐待风险或照护能力。
- 不制定个人休息、睡眠、治疗、雇佣、福利或照护替代方案。
- 不收集心理健康、家庭冲突、照护安排、收入、住址或危机资料。

## Source Signals

- NIA Caregiving: https://www.nia.nih.gov/health/caregiving
- ACL National Family Caregiver Support Program: https://acl.gov/programs/support-caregivers/national-family-caregiver-support-program
- CDC Older Adult and Caregiver materials: https://www.cdc.gov/aging/
- Eldercare Locator: https://eldercare.acl.gov/

## 下一步

- 建立照护者健康变量表：睡眠、压力、情绪、肌骨损伤、孤立、财务压力、支持连接和照护中断。
- 整理 caregiver burden、burnout、respite、peer support 和 mental health referral Source Cards。
