# Pregnancy Loss Stillbirth Bereavement Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pregnancy-loss-stillbirth-bereavement-continuity` |
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


妊娠丧失、死产与悲伤支持连续性，关注 miscarriage、stillbirth、pregnancy loss、医疗交接、死亡/生命事件记录、心理支持、工作学校调整、家庭沟通和后续妊娠风险咨询边界如何影响主体恢复和家庭连续性。

## 对象

- Miscarriage and stillbirth support boundary
- Pregnancy loss follow-up and referral
- Bereavement and peer support
- Work / school adjustment after loss
- Death or vital-record interface where applicable
- Family communication and cultural ritual boundary
- Subsequent pregnancy counseling boundary

## Human Infra 价值

妊娠丧失会同时打击身体恢复、未来生育计划、家庭关系、工作学校参与、心理稳定和意义结构。该域把“失去尚未进入社会系统的新生命后，主体和家庭如何恢复行动能力”建模为医疗、记录、假期、悲伤支持和文化承认的连续性问题。

## 边界

- 不提供流产/死产症状判断、原因解释、治疗、用药、急诊判断、尸检/检测、再次怀孕、法律、工作请假、宗教仪式或心理危机建议。
- 不判断个人损失类型、责任、医学原因、是否需急诊、是否可再次怀孕、是否有法律或福利资格。
- 不替代 OB/GYN、MFM、genetic counselor、mental health professional、employer/school、vital records office、宗教/文化顾问、律师或紧急服务。

## 上游与下游

- 上游：`prenatal-care-access-risk-screening-continuity/`、`reproductive-fertility-continuity/`、`maternal-newborn-child-development/`。
- 下游：`perinatal-mental-health-screening-referral-continuity/`、`bereavement-leave-grief-support-continuity/`、`vital-records-life-event-continuity/`。

## 初始资料线索

- CDC stillbirth and pregnancy loss materials.
- March of Dimes pregnancy loss and stillbirth resources.
- ACOG early pregnancy loss and stillbirth guidance boundaries.
