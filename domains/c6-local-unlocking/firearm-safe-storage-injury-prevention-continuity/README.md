# Firearm Safe Storage Injury Prevention Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/firearm-safe-storage-injury-prevention-continuity` |
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


`firearm-safe-storage-injury-prevention-continuity/` 研究枪支伤害预防中的安全储存、儿童接触、 suicide risk interface、家庭暴力风险和公共卫生证据边界。

> 核心问题：枪支伤害预防是高后果风险治理问题；Human Infra 只关心公开证据、储存边界和伤害预防系统，不进入武器操作。

## 先验位置

```text
主体要持续存在
  -> 必须降低高致死性工具在危机、儿童探索和冲突中的可及性
  -> 枪支暴露可把瞬时冲动、误触和暴力冲突转化为不可逆死亡
  -> 因而安全储存是伤害预防中的高后果风险边界
```

## 关注对象

- 安全储存、儿童接触、青少年自伤、家庭暴力风险、公共卫生监测、政策评估和证据沟通。

## Human Infra 模型链路

```text
枪支安全储存与伤害预防 T
  -> 改变可及性、储存状态、危机窗口、儿童接触、家庭冲突和风险沟通变量 X
  -> 改变冲动行为、误伤、暴力事件和自伤事件的即时可执行状态 S
  -> 改变死亡、重伤、创伤后家庭破坏和社区安全风险 λ(t)
  -> 改变主体持续性、家庭系统和公共信任
```

## 非目标

- 不提供枪支购买、持有、携带、操作、储存实施步骤、锁具选择、战术、自卫、规避安全装置、法律合规或个体风险判断建议。
- 不收集武器型号、存放位置、家庭成员信息、心理健康个案、暴力事件细节或地址。

## Source Signals

- CDC firearm violence prevention: https://www.cdc.gov/firearm-violence/
- NIH firearm injury prevention research resources: https://www.nichd.nih.gov/research/supported/firearm-injury-prevention
