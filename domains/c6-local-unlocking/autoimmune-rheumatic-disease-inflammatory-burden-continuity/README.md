# Autoimmune Rheumatic Disease Inflammatory Burden Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/autoimmune-rheumatic-disease-inflammatory-burden-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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


`autoimmune-rheumatic-disease-inflammatory-burden-continuity/` 研究类风湿关节炎、狼疮等自身免疫/风湿病、慢性炎症、免疫抑制、器官损害和照护连续性如何影响主体持续性。

> 核心问题：自身免疫风湿病不是单一关节问题，而是长期炎症、疲劳、疼痛、器官风险、免疫抑制和医疗监测共同塑造的主体能力损耗系统。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要免疫系统既能防御又不持续攻击自身组织
  -> 自身免疫风湿病会造成炎症、疼痛、疲劳、器官损害和治疗风险
  -> 结果取决于早诊、疾病活动控制、药物监测、感染预防和多专科协作
  -> 因此自身免疫风湿病是免疫稳态和长期功能连续性的关键维护域
```

## 关注对象

- Rheumatoid arthritis、systemic lupus erythematosus、autoimmune rheumatic disease、disease activity、fatigue、immunosuppression, organ involvement, flare prevention, care continuity。
- 与 `immune-maintenance/` 的边界：该域关注免疫维护总机制；本域聚焦自身免疫风湿病的炎症负担和照护连续性。
- 与 `chronic-infectious-disease-care-continuity/` 的关系：免疫抑制会改变感染风险、疫苗策略和长期监测需求。

## Human Infra 模型链路

```text
自身免疫风湿病照护连续系统 T
  -> 改变疾病活动、炎症、疼痛、疲劳、药物监测、感染风险和器官保护变量 X
  -> 改变移动能力、认知疲劳、工作参与、急性 flare 和医疗负担状态 S
  -> 改变失能风险、器官衰竭风险、感染风险和有效时间损耗 λ(t)
  -> 影响主体长期行动能力、恢复能力和未来选择权
```

## 非目标

- 不提供个人自身免疫诊断、化验判读、药物、免疫抑制、疫苗、妊娠、感染处理、器官监测或 flare 处理建议。
- 不生成治疗计划、用药调整、补充剂、饮食、检查周期、残障或保险判断。
- 不收集个案化验、影像、药物、生育、感染、工作或保险资料。

## Source Signals

- NIAMS rheumatoid arthritis: https://www.niams.nih.gov/health-topics/rheumatoid-arthritis
- NIAMS lupus: https://www.niams.nih.gov/health-topics/lupus
- CDC arthritis information: https://www.cdc.gov/arthritis/

## 下一步

- 建立 Autoimmune Inflammatory Burden Card：disease activity, fatigue, organ involvement, immunosuppression, infection risk, care continuity。
- 与 `immune-maintenance/`、`pharmacovigilance-drug-safety-monitoring/` 和 `multimorbidity-polypharmacy-care-coordination/` 建立接口。
