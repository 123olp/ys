# Child Passenger Safety Car Seat Restraint Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/child-passenger-safety-car-seat-restraint-continuity` |
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


`child-passenger-safety-car-seat-restraint-continuity/` 研究儿童乘员安全、汽车座椅、增高垫、安全带约束、安装理解和车辆碰撞保护如何影响儿童主体持续性。

> 核心问题：儿童乘员安全不是家庭偏好，而是把高速移动风险转化为尺寸、年龄、约束系统和执行理解的问题。

## 先验位置

```text
儿童主体要持续成长
  -> 必须在日常车辆移动中避免高能碰撞伤害
  -> 成人车辆约束默认不匹配儿童身体尺度
  -> 因而儿童约束系统是道路交通安全的执行层
```

## 关注对象

- 儿童安全座椅、增高垫、安全带、后排乘坐、安装理解、检查站、召回、车辆碰撞和照护执行。
- 婴幼儿、儿童、照护者、拼车/校车/家庭车辆场景。

## Human Infra 模型链路

```text
儿童乘员约束系统 T
  -> 改变儿童身体尺度匹配、约束位置、安装理解、召回和照护执行变量 X
  -> 改变车辆移动中的碰撞能量传递状态 S
  -> 改变死亡、头颈胸腹损伤、残障和家庭照护负担风险 λ(t)
  -> 改变儿童成长路径、家庭行动半径和未来选择权
```

## 非目标

- 不提供座椅选择、安装教程、年龄/身高体重适配判断、车辆座位安排、碰撞后处理、法律合规、产品推荐或个体儿童安全建议。
- 不收集儿童身高体重、车辆照片、座椅安装照片、碰撞记录或家庭出行数据。

## Source Signals

- NHTSA child passenger safety: https://www.nhtsa.gov/vehicle-safety/car-seats-and-booster-seats
- Safe Kids Worldwide car seat safety: https://www.safekids.org/car-seat
