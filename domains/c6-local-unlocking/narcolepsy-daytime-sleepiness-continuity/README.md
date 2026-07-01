# Narcolepsy Daytime Sleepiness Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/narcolepsy-daytime-sleepiness-continuity` |
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


`narcolepsy-daytime-sleepiness-continuity/` 研究发作性睡病、白天过度嗜睡、猝倒、睡眠瘫痪、入睡幻觉、诊断延迟和学习/驾驶/工作安全如何影响主体持续性。

> 核心问题：发作性睡病不是“困一点”，而是觉醒维持系统失稳，可能把清醒时间、任务可靠性、学习轮次、交通安全和社会参与持续压缩。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要可预测的清醒窗口维持学习、行动、驾驶、工作和关系参与
  -> 发作性睡病会造成日间睡意、睡眠发作、猝倒和睡眠-觉醒边界混乱
  -> 结果取决于识别、睡眠医学评估、教育/工作支持、安全边界和长期管理可及性
  -> 因此发作性睡病是觉醒维持与有效时间可靠性的关键研究域
```

## 关注对象

- Narcolepsy、excessive daytime sleepiness、cataplexy、sleep paralysis、hypnagogic hallucinations、diagnostic delay、school / work accommodations、driving and safety context。
- 与 `sleep-circadian-recovery/` 的边界：该域关注睡眠恢复总机制；本域关注发作性睡病这种觉醒维持障碍。
- 与 `fatigue-risk-alertness-continuity/` 的关系：疲劳风险域关注排班、长工时和恢复缺口；本域关注睡眠-觉醒神经调控障碍。

## Human Infra 模型链路

```text
发作性睡病识别与支持系统 T
  -> 改变日间嗜睡、猝倒风险、睡眠发作、诊断延迟、安全暴露和学校/工作支持变量 X
  -> 改变清醒窗口可靠性、任务中断、交通暴露、学习参与和关系负担 S
  -> 改变事故风险、教育/就业损耗、心理压力和有效时间损失 λ(t)
  -> 影响主体行动质量、长期能力形成和未来选择权
```

## 非目标

- 不提供个人发作性睡病诊断、睡眠检查解释、药物选择、剂量、驾驶限制、学校/工作便利申请或治疗建议。
- 不生成个人嗜睡评分、睡眠日记解释、药物方案、兴奋剂建议、请假/残障/保险材料或安全许可判断。
- 不收集个案睡眠记录、驾驶记录、学校/工作记录、用药、病史、心理健康或可识别医疗资料。

## Source Signals

- NHLBI narcolepsy: https://www.nhlbi.nih.gov/health/narcolepsy
- MedlinePlus sleep disorders: https://medlineplus.gov/ency/article/000800.htm

## 下一步

- 建立 Narcolepsy Continuity Card：sleepiness, cataplexy, sleep attacks, diagnostic access, support access, safety exposure, follow-up。
- 与 `sleep-circadian-recovery/`、`fatigue-risk-alertness-continuity/` 和 `attention-executive-control/` 建立接口。
