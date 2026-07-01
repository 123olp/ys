# Chronic Insomnia CBTI Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/chronic-insomnia-cbti-access-continuity` |
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


`chronic-insomnia-cbti-access-continuity/` 研究慢性失眠、CBT-I 可及性、睡眠行为治疗、药物依赖风险、日间功能和长期恢复能力如何影响主体持续性。

> 核心问题：慢性失眠会把夜间恢复失败转化为白天注意力、情绪、学习、工作和风险判断的持续损耗；有效永生需要关注可持续恢复能力，而不是只关注睡了多久。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要稳定睡眠恢复以维持注意力、情绪、代谢和学习
  -> 慢性失眠会降低恢复效率并扩大焦虑、抑郁、事故、用药和工作损耗
  -> 结果取决于 CBT-I、睡眠医学、行为支持、药物风险控制和复发预防可及性
  -> 因此慢性失眠是有效时间密度和恢复系统的关键维护域
```

## 关注对象

- Chronic insomnia disorder、CBT-I access、sleep restriction / stimulus control as supervised methods、digital CBT-I、hypnotic medication risk、daytime impairment、relapse prevention。
- 与 `sleep-circadian-recovery/` 的边界：该域关注睡眠恢复总机制；本域关注慢性失眠的行为治疗可及与长期功能损耗。
- 与 `mental-health-affective-stability/` 的关系：失眠既是情绪系统风险因子，也是情绪障碍的放大器。

## Human Infra 模型链路

```text
慢性失眠识别与 CBT-I 可及系统 T
  -> 改变睡眠效率、恢复稳定性、日间警觉、情绪波动、药物暴露和复发预防变量 X
  -> 改变注意力、执行功能、学习速度、事故暴露和工作连续性 S
  -> 改变有效时间损失、精神健康风险、物质风险和长期能力衰退 λ(t)
  -> 影响主体行动质量、创造密度和持续修正能力
```

## 非目标

- 不提供个人失眠诊断、睡眠处方、CBT-I 操作步骤、睡眠限制计划、药物选择、停药建议或危机处理。
- 不生成个人睡眠评分、行为计划、处方替代、设备购买或远程治疗建议。
- 不收集个案睡眠日志、精神健康、药物、工作、驾驶或可穿戴设备数据。

## Source Signals

- NIH / NHLBI sleep deprivation and deficiency: https://www.nhlbi.nih.gov/health/sleep-deprivation
- ACP insomnia guideline summary: https://www.acpjournals.org/doi/10.7326/M15-2175
- AASM behavioral and psychological treatments guideline: https://jcsm.aasm.org/doi/10.5664/jcsm.8986

## 下一步

- 建立 Insomnia Recovery Card：duration, daytime impairment, CBT-I access, medication exposure, relapse prevention, comorbidity。
- 与 `sleep-circadian-recovery/`、`attention-executive-control/` 和 `mental-health-affective-stability/` 建立接口。
