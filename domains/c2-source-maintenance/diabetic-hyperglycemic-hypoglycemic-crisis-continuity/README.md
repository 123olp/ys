# Diabetic Hyperglycemic Hypoglycemic Crisis Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/diabetic-hyperglycemic-hypoglycemic-crisis-continuity` |
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


`diabetic-hyperglycemic-hypoglycemic-crisis-continuity/` 研究 DKA、HHS、严重低血糖、监测断裂、胰岛素/液体/电解质风险、急诊接入和恢复交接如何影响主体持续性。

> 核心问题：糖尿病急性危象不是普通慢病管理失败，而是葡萄糖、胰岛素、水、电解质和意识状态同时失控。它需要被建模为代谢连续性急性失效域。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖葡萄糖、胰岛素、水和电解质维持脑与器官功能
  -> 高血糖危象或严重低血糖可迅速改变意识、循环、肾功能和死亡风险
  -> 结果取决于监测、供应、早识别、急诊接入和恢复教育交接
  -> 因此糖尿病急性危象是代谢连续性的时间关键失效域
```

## 关注对象

- Diabetic ketoacidosis、hyperosmolar hyperglycemic state、severe hypoglycemia、insulin access, CGM / meter continuity, sick-day risk, emergency care, recurrence prevention。
- 与 `diabetes-insulin-glucose-monitoring-supplies-continuity/` 的边界：该域关注日常供应与监测；本域关注急性高低血糖危象和恢复交接。
- 与 `endocrine-hormonal-regulation/` 的关系：本域是内分泌调节进入急性代谢失效的下游。

## Human Infra 模型链路

```text
糖尿病危象治理系统 T
  -> 改变监测、胰岛素连续性、液体/电解质风险、识别和急诊接入变量 X
  -> 改变意识状态、酸碱/渗透压、肾功能、住院和复发状态 S
  -> 改变急性死亡、脑损伤、再入院和有效时间损失 λ(t)
  -> 影响主体行动能力、恢复能力和未来选择权
```

## 非目标

- 不提供血糖读数判断、胰岛素剂量、饮食、运动、补液、电解质、急诊分诊、泵/CGM 设置或个体治疗建议。
- 不生成 DKA/HHS/低血糖路径、危象评分、家庭处理、sick-day rules 或急救替代工具。
- 不收集个案血糖、酮体、电解质、用药、设备数据、饮食、位置或病历资料。

## Source Signals

- ADA Standards of Care and hyperglycemic crises consensus materials: https://diabetesjournals.org/
- NIDDK diabetes materials: https://www.niddk.nih.gov/health-information/diabetes
- CDC diabetes materials: https://www.cdc.gov/diabetes/

## 下一步

- 建立 Diabetes Crisis Card：monitoring break, insulin access, DKA/HHS, severe hypoglycemia, emergency access, recurrence prevention。
- 与 `diabetes-insulin-glucose-monitoring-supplies-continuity/`、`endocrine-hormonal-regulation/` 和 `acute-kidney-injury-renal-replacement-continuity/` 建立接口。
