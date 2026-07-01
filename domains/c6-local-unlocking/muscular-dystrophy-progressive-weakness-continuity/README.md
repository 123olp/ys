# Muscular Dystrophy Progressive Weakness Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/muscular-dystrophy-progressive-weakness-continuity` |
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


`muscular-dystrophy-progressive-weakness-continuity/` 研究肌营养不良、进行性肌无力、心肺并发风险、移动支持、学校/工作参与和家庭照护如何影响主体持续性。

## Core Question

当肌肉结构和力量逐步退化时，主体如何继续把身体作为行动接口，维持移动、呼吸、心脏安全、学习/工作和社会参与？

## 先验位置

- 与 `musculoskeletal-integrity/` 的关系：肌营养不良不是普通肌骨负荷问题，而是遗传/结构性肌肉退行。
- 与 `respiratory-oxygenation/` 和 `cardiovascular-resilience/` 的关系：呼吸肌和心肌风险决定长期安全边界。
- 与 `assistive-technology-access/` 的关系：设备、无障碍和服务可及决定功能能否被补偿。

## 关注对象

- 肌无力、运动发育、心肺风险、脊柱/关节并发、移动设备、学校/工作参与、照护者负担和长期监测。
- 遗传检测、治疗进展、可及性、公平、家庭资源和失能权益。

## Human Infra 模型链路

```text
进行性肌肉结构/功能退化
-> 肌力、移动、呼吸和心脏安全边界变化
-> 学习、工作、外出、照护和环境适配需求增加
-> 有效时间与未来选择权下降
```

## 非目标

- 不提供肌营养不良诊断、基因解释、药物、激素、基因治疗、康复动作、设备、心肺监测或学校/工作建议。
- 不输出个体预后、治疗资格、保险、福利或功能许可判断。

## Source Signals

- NINDS muscular dystrophy: https://www.ninds.nih.gov/health-information/disorders/muscular-dystrophy

## 下一步

- 建立 progressive weakness card：把肌力、心肺风险、设备可及和参与限制纳入同一变量框架。
