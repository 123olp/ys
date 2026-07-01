# Idiopathic Hypersomnia Excessive Sleepiness Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/idiopathic-hypersomnia-excessive-sleepiness-continuity` |
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


`idiopathic-hypersomnia-excessive-sleepiness-continuity/` 研究特发性嗜睡、白天过度嗜睡、醒后困难、睡眠惯性、诊断不确定性和长期功能损耗如何影响主体持续性。

> 核心问题：特发性嗜睡会让主体拥有足够睡眠时间却仍难以稳定清醒，直接压缩可用行动窗口、任务启动能力和社会解释空间。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要可启动、可维持、可解释的清醒状态执行任务
  -> 特发性嗜睡可造成长睡眠、醒后困难和持续日间嗜睡
  -> 结果取决于诊断排除、睡眠医学可及、学校/工作支持和污名治理
  -> 因此特发性嗜睡是有效时间可用性与清醒启动能力的关键研究域
```

## 关注对象

- Idiopathic hypersomnia、excessive daytime sleepiness、sleep inertia、difficulty awakening、long sleep time、diagnostic uncertainty、school / work participation、stigma。
- 与 `narcolepsy-daytime-sleepiness-continuity/` 的边界：该域关注发作性睡病、猝倒和睡眠发作；本域关注非发作性睡病的持续嗜睡和醒后困难。
- 与 `chronic-insomnia-cbti-access-continuity/` 的关系：失眠域关注睡不着和恢复失败；本域关注睡了仍无法清醒。

## Human Infra 模型链路

```text
特发性嗜睡识别与支持系统 T
  -> 改变日间嗜睡、睡眠惯性、任务启动困难、诊断延迟、解释成本和支持可及变量 X
  -> 改变有效清醒时间、学习/工作启动、社交参与、交通暴露和心理负担 S
  -> 改变失误、旷课/缺勤、就业损耗、污名和有效时间损失 λ(t)
  -> 影响主体行动密度、身份稳定和未来选择权
```

## 非目标

- 不提供个人嗜睡诊断、睡眠检查解释、药物选择、兴奋剂建议、剂量、驾驶限制、学校/工作便利或治疗建议。
- 不生成个人睡眠评分、请假证明、保险/残障材料、用药方案、作息方案或安全许可判断。
- 不收集个案睡眠日志、可穿戴数据、用药、病史、驾驶、学校、工作、心理健康或可识别医疗资料。

## Source Signals

- MedlinePlus idiopathic hypersomnia: https://medlineplus.gov/ency/article/000803.htm
- MedlinePlus sleep disorders: https://medlineplus.gov/ency/article/000800.htm

## 下一步

- 建立 Hypersomnia Continuity Card：sleepiness, awakening difficulty, sleep inertia, diagnostic uncertainty, support access, stigma, safety exposure。
- 与 `sleep-circadian-recovery/`、`narcolepsy-daytime-sleepiness-continuity/` 和 `attention-executive-control/` 建立接口。
