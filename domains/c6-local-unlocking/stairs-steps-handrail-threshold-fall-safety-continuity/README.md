# Stairs Steps Handrail Threshold Fall Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/stairs-steps-handrail-threshold-fall-safety-continuity` |
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


`stairs-steps-handrail-threshold-fall-safety-continuity/` 研究楼梯、台阶、门槛、坡道、扶手、地面高度变化和路径连续性如何影响家庭内外移动、跌倒风险和独立出入。

> 核心问题：一个台阶或门槛足以把住所从保护层变成行动边界，尤其对老年、残障、术后和携物行动主体。

## 先验位置

```text
主体要持续出入住所和移动
  -> 必须跨越楼梯、台阶、门槛、坡道和高差
  -> 高差需要视觉、平衡、肌力、扶手和路径设计共同支撑
  -> 因而楼梯/门槛是行动连续性的结构性关口
```

## 关注对象

- 楼梯、台阶、门槛、坡道、扶手、栏杆、防滑、边缘对比、照明、楼梯间维护和室外入口。
- 携物、夜间、恶劣天气、轮椅/助行器、儿童、老年人和恢复期主体。

## Human Infra 模型链路

```text
楼梯台阶与扶手环境 T
  -> 改变高差、抓握、照明、对比、防滑和路径连续性 X
  -> 改变出入、上下楼、转运和家庭行动状态 S
  -> 改变跌倒、骨折、外出回避、照护依赖和住宅不可达风险 λ(t)
  -> 改变行动半径、独立生活和未来选择权
```

## 非目标

- 不提供建筑改造、扶手安装、坡道设计、施工、产品、个人跌倒评分、康复动作、住房合规、保险或法律建议。
- 不收集家庭照片、地址、户型、楼梯尺寸、残障状态、跌倒史或定位资料。

## Source Signals

- CDC / STEADI fall prevention materials.
- NIA home safety and falls materials.
- ADA / accessibility public materials as boundary references.
