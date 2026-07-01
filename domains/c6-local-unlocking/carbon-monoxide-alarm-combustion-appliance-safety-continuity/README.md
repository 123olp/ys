# Carbon Monoxide Alarm Combustion Appliance Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/carbon-monoxide-alarm-combustion-appliance-safety-continuity` |
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


`carbon-monoxide-alarm-combustion-appliance-safety-continuity/` 研究一氧化碳报警、燃烧设备、取暖、炉具、热水器、发电机、通风和停电备用如何影响不可见中毒风险。

> 核心问题：一氧化碳风险的危险在于不可见、不可闻、常发生在取暖或停电应急中，并会快速削弱判断和行动能力。

## 先验位置

```text
主体需要取暖、烹饪和备用能源
  -> 燃烧设备可能产生不可见一氧化碳
  -> 不可见暴露会先破坏认知、睡眠和行动能力
  -> 因而 CO 报警与燃烧设备边界是家庭能源安全执行层
```

## 关注对象

- CO 报警器、燃气炉具、热水器、取暖设备、壁炉、车库、便携发电机、通风、停电应急和多户住房。
- 儿童、老人、孕产者、睡眠中主体、语言障碍和灾害停电场景。

## Human Infra 模型链路

```text
CO 报警与燃烧设备安全 T
  -> 改变不可见暴露、通风、报警、备用能源和维护变量 X
  -> 改变睡眠、判断、撤离、求助和家庭能源状态 S
  -> 改变中毒、认知损伤、死亡和灾害次生风险 λ(t)
  -> 改变家庭能源韧性、生命安全和未来选择权
```

## 非目标

- 不提供燃气/炉具/热水器维修、发电机使用、报警器安装、通风设计、现场处置、中毒诊断、急救、保险或法律建议。
- 不收集家庭地址、设备型号、燃气系统照片、报警记录、家庭成员健康资料或实时位置。

## Source Signals

- CDC carbon monoxide poisoning materials.
- CPSC carbon monoxide and generator safety materials.
- U.S. Fire Administration home safety materials.
