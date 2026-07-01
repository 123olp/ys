# Delirium Acute Cognitive Failure Prevention

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/delirium-acute-cognitive-failure-prevention` |
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


`delirium-acute-cognitive-failure-prevention/` 研究谵妄、急性意识和注意障碍、住院/ICU 认知失败、术后认知风险和可预防诱因，如何影响 Human Infra 的短期主体连续性和长期认知轨迹。

> 核心问题：主体不是只会慢慢衰退，也可能在感染、手术、ICU、药物、睡眠剥夺或环境压力下快速失去注意、定向、判断和沟通能力。谵妄是“急性主体失联”的典型医学形态。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须在疾病、住院、手术和 ICU 中保持可感知、可沟通、可判断
  -> 谵妄会急性破坏注意、意识、定向和决策能力，并增加长期认知和死亡风险
  -> 若诱因识别、睡眠、疼痛、药物、活动、感官辅助和环境支持失败，治疗系统会反向制造认知损害
  -> 因此谵妄预防是医疗系统中的急性认知连续性域
```

## 关注对象

- ICU 谵妄、住院谵妄、术后谵妄、感染/药物/睡眠/疼痛/感官剥夺相关认知失败。
- CAM-ICU、PADIS 指南、ABCDEF bundle、早期活动、镇静策略、睡眠、家属参与和长期认知结果。
- 与 `dementia-cognitive-decline-care-continuity/` 的边界：痴呆域关注慢性认知下降；本域关注急性、波动性、可预防的认知失败。
- 与 `surgical-anesthesia-perioperative-safety/` 的边界：围手术域关注手术麻醉安全；本域关注谵妄作为跨场景急性主体失联。

## Human Infra 模型链路

```text
谵妄预防 T
  -> 改变镇静、疼痛、睡眠、感染、药物负担、活动、感官输入和环境支持变量 X
  -> 改变注意、意识、定向、沟通、决策和长期认知状态 S
  -> 改变住院并发症、长期认知损害、死亡、照护负担和主体失联风险 λ(t)
  -> 影响有效时间、医疗决策能力、恢复速度和主体连续性
```

## 非目标

- 不提供谵妄诊断、用药、镇静调整、ICU 治疗方案或个体照护计划。
- 不替代医生、护士、药师、ICU 团队、麻醉团队或照护机构流程。
- 不把筛查工具、家属观察或单项行为表现写成个人诊断。

## Source Signals

- SCCM PADIS Guidelines: https://www.sccm.org/Clinical-Resources/Guidelines/Guidelines/Pain-Agitation-Delirium-Immobility-and-Sleep-Disruption
- ICU Liberation ABCDEF Bundle: https://www.sccm.org/Clinical-Resources/ICULiberation-Home/ABCDEF-Bundles
- NIA Delirium: https://www.nia.nih.gov/health/what-delirium
- NICE Delirium guideline: https://www.nice.org.uk/guidance/cg103

## 下一步

- 建立谵妄变量表：诱因、镇静、疼痛、睡眠、药物、感染、感官输入、活动、环境、筛查和长期结局。
- 与 `patient-safety-organizational-learning/`、`surgical-anesthesia-perioperative-safety/`、`sleep-circadian-recovery/` 和 `dementia-cognitive-decline-care-continuity/` 建立接口。
