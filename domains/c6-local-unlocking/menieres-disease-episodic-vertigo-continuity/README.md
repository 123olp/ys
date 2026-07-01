# Meniere's Disease Episodic Vertigo Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/menieres-disease-episodic-vertigo-continuity` |
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


Meniere's disease episodic vertigo continuity studies recurrent vertigo, fluctuating hearing symptoms, tinnitus, ear fullness, and unpredictable episodes as a combined auditory-vestibular disruption to work, movement, planning, and social participation.

核心问题：

> 主体需要的不只是平均状态稳定，还需要未来数小时和数天的行动计划可预测；发作性眩晕会把时间表、出行、会议和照护安排变成不可靠承诺。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能预测近期身体状态以安排任务
  -> 前庭和听觉系统必须维持足够稳定的输入
  -> 梅尼埃病相关发作会造成眩晕、听觉波动、耳鸣和不确定性
  -> 因而它是空间行动和时间规划中的发作型连续性风险
```

## 关注对象

- 发作性眩晕、听力波动、耳鸣、耳闷、恶心、行动中断和预期不确定性。
- 工作排班、驾驶/交通、公共空间停留、独处风险、社交参与和应急计划。
- 与 `hearing-auditory-communication-continuity/` 的关系：听觉域关注沟通通道；本域关注听觉与前庭共同波动。
- 与 `tinnitus-sound-tolerance-sleep-continuity/` 的关系：耳鸣域关注内源声音负担；本域关注发作型眩晕和听觉波动组合。

## Human Infra 模型链路

```text
教育 / 转诊 / 症状记录 / 工作与出行适配 T
  -> 改变发作识别、行动计划、风险预案和沟通支持 X
  -> 改变工作连续性、移动半径、社交参与和应急暴露状态 S
  -> 改变跌倒、事故、孤立、失业和有效时间损失风险 λ(t)
  -> 影响主体行动稳定性、长期角色维持和未来选择权
```

## 非目标

- 不提供梅尼埃病诊断、饮食/药物/手术建议、听力图解释、发作分型或驾驶判断。
- 不根据个人症状判断发作原因、治疗优先级、工作限制或急诊必要性。
- 不替代耳鼻喉、听力学、神经、前庭康复或职业医学专业服务。

## Source Signals

- NIDCD Meniere's disease resources。
- NIDCD balance disorders resources。
- NIDCD tinnitus and hearing resources as adjacent context。
