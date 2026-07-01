# Parasomnia Sleepwalking Behavior Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/parasomnia-sleepwalking-behavior-safety-continuity` |
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


`parasomnia-sleepwalking-behavior-safety-continuity/` 研究异态睡眠、梦游、睡中行为、夜惊/异常觉醒、伤害风险、家庭安全和隐私污名如何影响主体持续性。

> 核心问题：异态睡眠会让主体在意识不完整状态下发生行为，安全风险、家庭负担和羞耻污名都可能反过来破坏恢复系统。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要睡眠阶段保持恢复和基本安全
  -> 异态睡眠可在睡眠中产生行走、行为、惊恐或危险互动
  -> 结果取决于识别、睡眠医学语境、家庭环境、安全防护和隐私/污名治理
  -> 因此异态睡眠是恢复系统、安全边界和家庭支持之间的关键研究域
```

## 关注对象

- Parasomnia、sleepwalking、night terrors / arousal events、abnormal sleep behaviors、injury risk、household safety context、stigma and privacy。
- 与 `sleep-circadian-recovery/` 的边界：该域关注恢复总机制；本域关注睡眠中异常行为和安全边界。
- 与 `home-safety-emergency-preparedness/` 的关系：家庭安全域关注住所风险；本域关注睡眠状态下的行为风险。

## Human Infra 模型链路

```text
异态睡眠识别与安全支持系统 T
  -> 改变睡中行为频率、伤害暴露、家庭安全环境、睡眠碎片、隐私污名和转诊可及变量 X
  -> 改变夜间安全、家庭照护负担、恢复质量、情绪压力和生活自主 S
  -> 改变伤害风险、关系压力、睡眠恐惧和有效时间损失 λ(t)
  -> 影响主体恢复、家庭支持和长期行动能力
```

## 非目标

- 不提供个人异态睡眠诊断、睡眠检查解释、药物建议、安全处置步骤、儿童/成人个案判断、家庭改造或治疗建议。
- 不生成个人风险评分、卧室安全清单、伴侣/儿童处理脚本、药物方案、法律/保险材料或监控方案。
- 不收集个案睡眠视频、家庭布局、儿童资料、伴侣资料、心理健康、用药、伤害记录或可识别医疗/家庭资料。

## Source Signals

- MedlinePlus sleepwalking: https://medlineplus.gov/ency/article/000808.htm
- MedlinePlus sleep disorders: https://medlineplus.gov/ency/article/000800.htm

## 下一步

- 建立 Parasomnia Safety Card：behavior type, injury exposure, household context, sleep fragmentation, privacy/stigma, referral context, support burden。
- 与 `sleep-circadian-recovery/`、`home-safety-emergency-preparedness/` 和 `family-caregiving-continuity/` 建立接口。
