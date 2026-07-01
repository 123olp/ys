# Uterine Fibroids Bleeding Anemia Fertility Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/uterine-fibroids-bleeding-anemia-fertility-continuity` |
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


`uterine-fibroids-bleeding-anemia-fertility-continuity/` 研究子宫肌瘤、重度出血、贫血、疼痛、压迫症状、生育/妊娠影响、治疗路径和医疗可及如何影响主体持续性。

> 核心问题：肌瘤的主体持续性影响不只在“肿块存在”，而在出血、贫血、疲劳、疼痛、工作学习缺席、生育计划和治疗负担共同消耗有效时间。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要稳定能量、行动能力、血液携氧、身体自主和未来选择权
  -> 子宫肌瘤可能通过重度月经出血、贫血、疼痛、压迫和妊娠/生育影响破坏这些条件
  -> 若诊断、贫血处理、治疗选择和随访断裂，主体会损失有效时间、工作参与和生殖规划窗口
  -> 因此肌瘤是出血-贫血-生育-功能连续性的研究域
```

## 关注对象

- Uterine fibroids、heavy menstrual bleeding、anemia、fatigue、pelvic pressure、pain、fertility and pregnancy concerns、procedure burden、shared decision-making。
- 与 `menstrual-health-cycle-literacy-continuity/` 的边界：月经域关注周期性信号和参与；本域关注肌瘤导致的结构性出血、贫血和生育/治疗路径。
- 与 `blood-oxygen-hemostasis/` 的关系：重度出血和贫血会进入携氧能力、疲劳和恢复模型。
- 与 `reproductive-fertility-continuity/` 的关系：肌瘤可能影响未来生育选择权，但不等于个人生育结论。

## Human Infra 模型链路

```text
肌瘤识别与连续照护系统 T
  -> 改变出血量、贫血、疲劳、疼痛、压迫、生育规划、治疗选择和随访变量 X
  -> 改变主体能量、有效时间、行动半径、工作学习参与、身体自主和未来选择权状态 S
  -> 改变贫血、失能、治疗负担、妊娠/生育受限、诊断延迟和资源消耗 lambda(t)
  -> 影响主体健康寿命、有效时间和长期计划能力
```

## 非目标

- 不提供肌瘤诊断、影像解释、贫血治疗、激素/药物、手术/介入、妊娠建议、生育治疗、急诊判断或个体医疗建议。
- 不把出血、贫血、疼痛、腹胀、压迫、影像或肌瘤大小写成个人风险判断。
- 不收集个人月经、贫血、影像、妊娠、生育、用药、手术或保险资料。

## Source Signals

- MedlinePlus uterine fibroids: https://medlineplus.gov/uterinefibroids.html
- NICHD uterine fibroids: https://www.nichd.nih.gov/health/topics/uterine
- HHS OWH uterine fibroids: https://www.womenshealth.gov/a-z-topics/uterine-fibroids

## 下一步

- 建立 Fibroids Continuity Card：bleeding burden, anemia signal, pain/pressure, fertility planning, treatment burden, follow-up access。
- 与 `blood-oxygen-hemostasis/`、`menstrual-health-cycle-literacy-continuity/`、`reproductive-fertility-continuity/` 和 `healthcare-access-continuity/` 建立接口。
