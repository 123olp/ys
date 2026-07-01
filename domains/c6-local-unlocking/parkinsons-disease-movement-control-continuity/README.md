# Parkinson's Disease Movement Control Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/parkinsons-disease-movement-control-continuity` |
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


`parkinsons-disease-movement-control-continuity/` 研究帕金森病、运动控制、震颤、僵硬、步态、非运动症状、照护负担和长期功能参与如何影响主体持续性。

## Core Question

当多巴胺能运动控制和非运动功能逐步受损时，主体如何继续维持移动、表达、工作、照护协作、环境适配和长期项目推进能力？

## 先验位置

- 与 `neuro-continuity/` 的关系：帕金森病是慢性神经退行性病程，不是一般神经完整性条目。
- 与 `physical-activity-mobility/` 的关系：步态、平衡和运动迟缓会直接改变行动半径。
- 与 `caregiving-long-term-care/` 的关系：进展期功能变化会放大照护、住房和服务协调需求。

## 关注对象

- 运动症状、非运动症状、药物时效波动、跌倒风险、吞咽/言语、睡眠、认知、情绪和照护连续性。
- 诊断延迟、专科可及、康复/运动支持、辅助技术、照护者负担和长期参与限制。

## Human Infra 模型链路

```text
帕金森病病程
-> 运动控制、非运动症状和认知/情绪负担变化
-> 移动、表达、睡眠、工作和照护协作能力下降
-> 有效时间、社会参与和未来选择权受限
-> 主体持续性下降
```

## 非目标

- 不提供帕金森病诊断、药物、剂量、手术、深脑刺激、康复动作、设备或照护方案建议。
- 不根据症状、视频、步态、可穿戴数据或量表输出个体病程、风险、驾驶/工作许可或治疗判断。

## Source Signals

- NINDS Parkinson's disease: https://www.ninds.nih.gov/health-information/disorders/parkinsons-disease

## 下一步

- 建立 movement control card：把运动症状、非运动症状、跌倒、照护和参与限制拆成可审查变量。
