# ATV Off Highway Vehicle Injury Prevention Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/atv-off-highway-vehicle-injury-prevention-continuity` |
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


`atv-off-highway-vehicle-injury-prevention-continuity/` 研究 ATV、越野车、青少年驾驶、翻覆、头部伤害、道路/地形暴露和产品安全如何影响主体持续性。

> 核心问题：越野车辆把娱乐、交通替代、速度、地形和儿童/青少年判断力连接成高能机械伤害窗口。

## 先验位置

```text
主体要通过娱乐和移动扩展可能性
  -> 必须避免速度、地形和车辆翻覆带来的高能冲击
  -> ATV/OHV 活动常发生在道路系统和常规救援之外
  -> 因而越野车辆安全是边缘移动场景中的伤害预防域
```

## 关注对象

- ATV、OHV、翻覆、头部伤害、儿童/青少年使用、乘客、地形、道路交叉、产品警示和事故监测。

## Human Infra 模型链路

```text
ATV/OHV 安全治理 T
  -> 改变车辆匹配、速度、地形、乘员、头部保护、监督和救援可达变量 X
  -> 改变越野移动中的翻覆、碰撞和伤后响应状态 S
  -> 改变死亡、TBI、脊髓损伤、骨折和长期残障风险 λ(t)
  -> 改变行动自由、家庭负担、有效时间和未来选择权
```

## 非目标

- 不提供驾驶教学、路线选择、车辆选择、年龄许可、维修改装、头盔/装备购买、事故处理、法律或个体安全建议。
- 不收集车辆型号、路线轨迹、儿童驾驶资料、事故照片、伤情记录或家庭活动计划。

## Source Signals

- CPSC ATV Safety Information Center: https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/ATV-Safety-Information-Center
- CPSC off-highway vehicle safety materials: https://www.cpsc.gov/Safety-Education/Safety-Guides/Sports-Fitness-and-Recreation/ATVs
