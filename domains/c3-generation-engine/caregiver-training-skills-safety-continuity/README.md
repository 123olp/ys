# Caregiver Training Skills Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/caregiver-training-skills-safety-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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


`caregiver-training-skills-safety-continuity/` 研究家庭照护者培训、技能理解、转移安全、感染预防、用药理解、设备使用、沟通和边界意识如何影响照护质量、照护者损伤和被照护者持续性。

> 核心问题：家庭照护常把复杂任务交给非专业人员。若没有培训、演示、可理解资料和边界说明，照护会从支持系统变成损伤、错误和耗竭来源。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 家庭照护者经常承担移动、卫生、餐食、观察、沟通和设备相关任务
  -> 这些任务需要最低技能、风险识别和知道何时求助
  -> 照护者训练决定家庭照护能否安全、可持续、不过度医疗化
```

## 关注对象

- 照护者教育、技能训练、teach-back、书面/视频材料、语言可及和健康素养。
- 转移协助、跌倒风险、感染预防、用药理解、设备基础、营养/吞咽提示边界和紧急升级。
- 照护者肌骨损伤、错误任务执行、信息过载、培训缺口和专业支持转介。
- 与 `health-literacy-navigation/`、`care-transitions-discharge-continuity/`、`feeding-assistance-mealtime-dignity-continuity/` 的接口。

## Human Infra 模型链路

```text
照护者训练与技能支持
  -> 改变任务理解、风险识别、沟通、求助阈值和安全执行能力
  -> 改变家庭照护质量、照护者损伤和被照护者日常支持状态
  -> 降低跌倒、感染、用药误解、照护者肌骨损伤和再入院风险
  -> 增强居家持续性、尊严和恢复能力
```

## 非目标

- 不提供护理技术、转移动作、感染控制操作、用药、设备操作或急救步骤。
- 不替代护士、治疗师、医生、社工、药师或培训机构。
- 不判断个人照护者能力、家庭安全、照护质量或是否可独立照护。
- 不收集家庭照片、护理视频、设备型号、病历、照护计划或健康资料。

## Source Signals

- NIA Caregiving: https://www.nia.nih.gov/health/caregiving
- AHRQ Care Transitions: https://www.ahrq.gov/patient-safety/settings/hospital/red/toolkit/index.html
- ACL National Family Caregiver Support Program: https://acl.gov/programs/support-caregivers/national-family-caregiver-support-program
- CDC Caregiving and health materials: https://www.cdc.gov/aging/

## 下一步

- 建立照护者训练变量表：任务类型、材料可理解性、演示/回教、语言可及、专业支持、过载和边界升级。
- 整理 discharge teaching、caregiver education、health literacy 和 safety training Source Cards。
