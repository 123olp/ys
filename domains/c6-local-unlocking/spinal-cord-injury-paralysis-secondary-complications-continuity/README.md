# Spinal Cord Injury Paralysis Secondary Complications Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/spinal-cord-injury-paralysis-secondary-complications-continuity` |
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


`spinal-cord-injury-paralysis-secondary-complications-continuity/` 研究脊髓损伤、瘫痪、感觉运动通道断裂、二级并发症、无障碍和长期参与如何影响主体持续性。

## Core Question

当脊髓损伤改变运动、感觉、自主功能和环境需求时，主体如何通过康复、辅助技术、无障碍、照护和并发症预防维持行动与选择权？

## 先验位置

- 与 `neuro-continuity/` 的关系：SCI 是中枢传导通路损伤，并长期影响身体-环境接口。
- 与 `assistive-technology-access/` 的关系：轮椅、设备、住房/交通无障碍和维修决定行动能否恢复。
- 与 `urogenital-continuity/`、`skin-barrier-wound-healing/` 和 `autonomic-nervous-system-homeostasis/` 的关系：二级并发症是长期持续性的关键。

## 关注对象

- 运动/感觉功能、神经源性膀胱肠道、皮肤压力损伤、疼痛、痉挛、自主神经异常、呼吸、设备、住房、交通和照护。
- 急性到长期转衔、再入院、社区参与、就业教育、照护者负担和权利可达。

## Human Infra 模型链路

```text
脊髓通路损伤
-> 运动、感觉、自主功能和环境依赖改变
-> 二级并发症、设备和无障碍需求增加
-> 行动半径、独立生活和社会参与受限
-> 主体持续性下降
```

## 非目标

- 不提供 SCI 急救、损伤分级、康复训练、设备选择、皮肤/泌尿/肠道处理、性功能、药物、手术或照护建议。
- 不输出个体恢复概率、功能等级、住房/交通改造、福利、保险或法律判断。

## Source Signals

- NINDS spinal cord injury: https://www.ninds.nih.gov/health-information/disorders/spinal-cord-injury

## 下一步

- 建立 SCI secondary-complications card：把二级并发症、无障碍、设备和社会参与作为核心变量。
