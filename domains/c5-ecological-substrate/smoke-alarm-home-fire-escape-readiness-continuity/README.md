# Smoke Alarm Home Fire Escape Readiness Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/smoke-alarm-home-fire-escape-readiness-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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


`smoke-alarm-home-fire-escape-readiness-continuity/` 研究住宅烟雾报警、火灾逃生计划、门窗出口、听觉/视觉警报、演练、儿童/老年/残障可达和停电情境如何影响家庭火灾中的主体连续性。

> 核心问题：家庭火灾的关键不是“知道火危险”，而是烟雾出现时能否被及时唤醒、理解、移动并离开。

## 先验位置

```text
主体需要住所保护
  -> 住所必须在火灾中提供早期警报、出口和逃生冗余
  -> 烟雾、睡眠、残障、儿童照护和时间压力会压缩行动窗口
  -> 因而烟雾报警与逃生准备是家庭生命安全执行层
```

## 关注对象

- 烟雾报警器、警报可听/可视/可振动、逃生路线、门窗出口、集合点、演练、睡眠中警报、儿童/老人/残障支持。
- 租赁住房、独居、多人家庭、宿舍、临时住所和灾害停电场景。

## Human Infra 模型链路

```text
烟雾报警与逃生准备 T
  -> 改变早期警报、出口、演练、可达警报和家庭协同 X
  -> 改变睡眠中唤醒、判断、移动、撤离和求助状态 S
  -> 改变烟雾吸入、烧伤、死亡、财产损失和长期流离风险 λ(t)
  -> 改变住所保护、恢复窗口和未来选择权
```

## 非目标

- 不提供消防工程、布线、报警器安装、逃生路线定制、现场指挥、危险环境进入、纵火规避、保险索赔或个体安全建议。
- 不收集家庭平面图、地址、安防细节、儿童位置、残障资料或实时占用信息。

## Source Signals

- U.S. Fire Administration smoke alarm and home escape materials.
- NFPA public fire safety materials.
- CPSC smoke alarm / fire safety public materials.
