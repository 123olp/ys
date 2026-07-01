# Gait Balance Assessment Fall Screening Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/gait-balance-assessment-fall-screening-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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


Gait, balance assessment, and fall screening continuity studies screening instruments, mobility observation, balance confidence, referral, and follow-up as interfaces between vestibular instability and preventable fall-related loss of independence.

核心问题：

> 跌倒不是只在摔倒那一刻发生；它之前通常有步态、平衡、药物、视力、前庭、环境和信心变化。若这些信号没有进入筛查和转介，主体会在风险升高后才被系统看见。

## 先验位置

```text
主体持续性最大化
  -> 主体必须在跌倒和骨折前被识别为行动风险上升
  -> 步态、平衡、前庭、视觉、药物和环境共同决定跌倒暴露
  -> 筛查和转介把隐性风险转成可处理任务
  -> 因而步态平衡筛查是空间行动连续性的预警接口
```

## 关注对象

- 步态、平衡、移动信心、跌倒史、筛查工具、转介、家庭安全和服务衔接。
- 与 `fall-risk-prevention-home-safety-continuity/` 的关系：后者关注家庭防跌倒干预；本域关注平衡/步态信号如何进入筛查。
- 与 `musculoskeletal-integrity/` 的关系：肌骨域关注骨骼、肌肉和骨折后果；本域关注移动稳定信号。
- 与 `vestibular-rehabilitation-balance-compensation-continuity/` 的关系：康复域关注恢复；本域关注识别和转介。

## Human Infra 模型链路

```text
筛查 / 步态观察 / 转介 / 跟踪 T
  -> 改变风险识别、平衡信心、活动计划和服务衔接 X
  -> 改变跌倒暴露、外出频率、家庭活动和照护需求状态 S
  -> 改变跌倒、骨折、失能、恐惧回避和机构化风险 λ(t)
  -> 影响独立生活、行动半径和未来选择权
```

## 非目标

- 不提供个人跌倒评分、步态诊断、助行器选择、家庭改造建议、训练计划或活动许可。
- 不根据传感器、视频、病史或自测结果判断个人风险等级。
- 不替代临床评估、物理治疗、老年医学、职业治疗或家庭安全评估。

## Source Signals

- CDC STEADI fall prevention resources。
- WHO falls and healthy ageing materials。
- NIDCD balance disorders resources。
