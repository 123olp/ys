# Restless Legs Periodic Limb Movement Sleep Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/restless-legs-periodic-limb-movement-sleep-continuity` |
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


`restless-legs-periodic-limb-movement-sleep-continuity/` 研究不宁腿综合征、周期性肢体运动、入睡困难、睡眠碎片、铁/药物语境和长期恢复质量如何影响主体持续性。

> 核心问题：RLS 不是小腿不舒服的边缘症状，而是感觉-运动驱动的睡眠破坏，可长期损耗恢复、情绪、注意力和伴侣/家庭睡眠。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖连续睡眠恢复注意力、情绪、免疫和代谢
  -> RLS / 周期性肢体运动可通过不适、冲动和睡眠碎片破坏夜间恢复
  -> 结果取决于识别、共病/药物语境、睡眠医学可及和长期管理边界
  -> 因此 RLS 是睡眠恢复、感觉-运动负担和家庭睡眠连续性的交叉域
```

## 关注对象

- Restless legs syndrome、periodic limb movements、urge to move、sleep fragmentation、daytime impairment、iron context、medication context、partner sleep burden。
- 与 `chronic-insomnia-cbti-access-continuity/` 的边界：失眠域关注行为/认知性入睡维持困难；本域关注感觉-运动症状造成的睡眠中断。
- 与 `peripheral-neuropathy-somatosensory-continuity/` 的关系：周围神经域关注感觉反馈和足部风险；本域关注睡眠阶段的感觉-运动驱动。

## Human Infra 模型链路

```text
RLS 识别与管理可及系统 T
  -> 改变腿部不适、移动冲动、周期性运动、睡眠碎片、共病语境和治疗可及变量 X
  -> 改变恢复质量、日间警觉、情绪稳定、伴侣睡眠和任务持续性 S
  -> 改变有效时间损失、事故暴露、心理负担和家庭关系压力 λ(t)
  -> 影响主体恢复能力、行动质量和长期参与
```

## 非目标

- 不提供个人 RLS 诊断、铁指标解释、药物选择、补铁、剂量、停药、睡眠检查解释、伴侣睡眠或治疗建议。
- 不生成个人症状评分、药物方案、补剂方案、睡眠计划、保险材料或设备推荐。
- 不收集个案睡眠、腿部症状、实验室指标、用药、妊娠、肾病、伴侣或可识别医疗资料。

## Source Signals

- MedlinePlus restless legs: https://medlineplus.gov/restlesslegs.html
- MedlinePlus sleep disorders: https://medlineplus.gov/ency/article/000800.htm

## 下一步

- 建立 RLS Sleep Continuity Card：sensory urge, movement burden, sleep fragmentation, comorbidity context, medication context, daytime impairment, partner burden。
- 与 `sleep-circadian-recovery/`、`peripheral-neuropathy-somatosensory-continuity/` 和 `mental-health-affective-stability/` 建立接口。
