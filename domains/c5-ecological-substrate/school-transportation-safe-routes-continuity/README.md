# School Transportation Safe Routes Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/school-transportation-safe-routes-continuity` |
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


`school-transportation-safe-routes-continuity` 研究校车、步行骑行安全路线、无障碍交通、交通资格、到校距离和道路安全如何影响出勤、学习时间、安全风险和家庭时间成本。

> 核心问题：儿童不能安全、可靠、可负担地到达学校，教育权就会退化为纸面资格。

## 关注对象

- 校车安全、路线规划、交通资格、接送点、迟到缺勤、天气灾害和服务中断。
- Safe Routes to School、步行、骑行、道路设计、速度风险、可见性和交叉口安全。
- 残障学生交通、临时住所/寄养/迁居交通、农村距离、家庭工作时间和照护负担。
- 通学交通与出勤、纪律、特殊教育、环境暴露、交通伤害和公共交通运营的交叉。

## Human Infra 链路

```text
通学交通与安全路线连续
  -> 学生到校路径更可靠、可达、安全和低摩擦
  -> 缺勤、迟到、交通伤害、家庭时间成本和安全焦虑下降
  -> 学习时间、恢复时间、家庭工作连续性和社区可达性增强
  -> 儿童能力积累和长期未来选择权更稳定
```

## 非目标

- 不提供个人路线、驾驶、校车申诉、交通资格、道路工程、事故责任、残障交通、法律或安全实时建议。
- 不替代学校交通部门、DOT、NHTSA、FHWA、地方交通机构、警务、急救或法律服务。
- 不收集学生住址、路线、家庭安排、残障资料或定位数据。

## Source Signals

- Federal Highway Administration Safe Routes to School resources.
- National Highway Traffic Safety Administration school bus safety resources.
- State and local school transportation and road safety guidance.
- Local education agency transportation policies and accessibility requirements.

## 下一步

- 建立 `route reliability -> arrival continuity -> exposure/risk -> learning time` 变量表。
- 区分学校交通、公共交通、道路安全、家庭接送、残障交通和灾害交通。
- 与 `transportation-access-mobility`、`road-traffic-injury-prevention-safe-mobility`、`school-enrollment-attendance-continuity` 和 `special-education-iep-504-accommodation-continuity` 建立边界。
