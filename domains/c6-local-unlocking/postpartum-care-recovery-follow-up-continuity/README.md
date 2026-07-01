# Postpartum Care Recovery Follow Up Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/postpartum-care-recovery-follow-up-continuity` |
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


产后照护、恢复与随访连续性，关注分娩后身体恢复、产后随访、慢病和妊娠并发症延续管理、警示信号教育、医保覆盖、家庭支持、工作/照护压力和转诊闭环。

## 对象

- Postpartum visit and ongoing care
- Recovery after birth and cesarean boundary
- Blood pressure, diabetes, infection and pain follow-up
- Warning signs and urgent referral interface
- Insurance coverage and appointment continuity
- Family, work and caregiving load
- Transition back to primary care

## Human Infra 价值

产后阶段会把身体恢复、睡眠、照护负担、医疗随访、心理状态、收入和家庭支持集中到一个高负荷窗口。该域把“分娩之后是否仍有连续照护”建模为避免可预防死亡、失能、心理崩溃和长期健康轨迹恶化的基础设施。

## 边界

- 不提供产后症状判断、用药、伤口处理、哺乳、避孕、运动恢复、复工、急诊判断、心理危机或个体医疗建议。
- 不判断个人是否恢复正常、是否需要复诊、是否有并发症、是否适合工作或某项活动。
- 不替代 OB/GYN、midwife、primary care、mental health professional、lactation consultant、保险、雇主或紧急服务。

## 上游与下游

- 上游：`prenatal-care-access-risk-screening-continuity/`、`obstetric-emergency-hemorrhage-hypertension-continuity/`、`pregnancy-parental-work-continuity/`。
- 下游：`perinatal-mental-health-screening-referral-continuity/`、`lactation-breastfeeding-support-continuity/`、`maternal-newborn-child-development/`。

## 初始资料线索

- ACOG Optimizing Postpartum Care.
- CDC Hear Her / maternal warning signs and maternal mortality materials.
- HRSA maternal health and postpartum coverage materials.
