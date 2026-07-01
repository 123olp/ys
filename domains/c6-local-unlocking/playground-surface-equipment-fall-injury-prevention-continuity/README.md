# Playground Surface Equipment Fall Injury Prevention Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/playground-surface-equipment-fall-injury-prevention-continuity` |
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


`playground-surface-equipment-fall-injury-prevention-continuity/` 研究游乐场设备、跌落高度、缓冲地面、维护、可达性和儿童游戏参与如何影响伤害预防与发展机会。

> 核心问题：游乐场既是儿童学习、社交和身体发展的基础设施，也是跌落、夹伤和设备失效风险的环境系统。

## 先验位置

```text
儿童主体要成长
  -> 需要可达、可探索、可社交的游戏空间
  -> 游戏空间存在跌落高度、表面缓冲和设备维护风险
  -> 因而游乐场安全是发展机会和伤害预防之间的基础设施边界
```

## 关注对象

- 公共游乐场、学校/社区设备、缓冲地面、跌落高度、维护检查、年龄适配、无障碍和伤害监测。

## Human Infra 模型链路

```text
游乐场设备与表面 T
  -> 改变跌落高度、冲击吸收、夹陷点、维护、年龄适配和可达性变量 X
  -> 改变儿童游戏、探索、运动和事故后状态 S
  -> 改变骨折、头部伤害、活动回避和发展机会损失风险 λ(t)
  -> 改变儿童成长、公共空间信任和未来行动能力
```

## 非目标

- 不提供游乐场设计、施工、检查清单、维修、设备采购、年龄许可、儿童监控、法律合规或个体安全建议。
- 不收集儿童影像、学校/社区位置、设备缺陷照片、事故记录或责任材料。

## Source Signals

- CPSC Public Playground Safety Handbook: https://www.cpsc.gov/safety-education/safety-guides/playgrounds/public-playground-safety-handbook
- CDC child injury prevention materials: https://www.cdc.gov/child-safety/
