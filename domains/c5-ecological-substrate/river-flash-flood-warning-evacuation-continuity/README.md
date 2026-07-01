# River and Flash Flood Warning Evacuation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/river-flash-flood-warning-evacuation-continuity` |
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


`river-flash-flood-warning-evacuation-continuity/` 研究河流洪水、山洪、城市积水、道路淹没、预警理解、撤离和避难如何影响主体持续性。

> 核心问题：洪水把天气预报、水文观测、道路可达、住房安全和家庭撤离能力压缩成短窗口行动链；主体能否继续存在，取决于警报能否转化为及时避险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须穿越低频高冲击自然灾害
  -> 洪水会同时攻击住房、道路、饮水、医疗可达和通信
  -> 若预警理解、撤离、绕行和避难失败，短时水风险会转化为死亡、伤害和长期流离
  -> 因而河流/山洪预警与撤离是主体灾害执行连续性域
```

## 关注对象

- 河流洪水、山洪、城市内涝、道路积水、低洼区、夜间洪水和重复淹没社区。
- 洪水 watch/warning、紧急警报、交通中断、撤离命令、避难所入口、特殊人群转移和灾后返回。
- 与 `water-resources-hydrology-flood-drought-management/` 的边界：该域关注流域和水资源管理；本域关注洪水发生时人的预警-避险-撤离执行链。

## Human Infra 模型链路

```text
洪水预警与撤离系统 T
  -> 改变警报理解、道路选择、撤离时间、避难入口、饮水卫生和家庭团聚变量 X
  -> 改变主体在洪水窗口中的暴露与可达状态 S
  -> 改变溺水、创伤、低体温、感染、流离和服务中断风险 λ(t)
  -> 影响有效寿命、恢复时间、资源消耗和未来选择权
```

## 非目标

- 不提供实时洪水预警、行车路线、涉水判断、撤离点选择、房屋返回判断或保险/理赔建议。
- 不替代 NWS/NOAA、FEMA、地方应急管理、水文部门、交通部门或公共安全机构。
- 不鼓励涉水驾驶、围观洪水、规避撤离命令或传播未核实灾情。

## Source Signals

- NWS Flood Safety: https://www.weather.gov/safety/flood
- Ready.gov Floods: https://www.ready.gov/floods
- FEMA Flood Maps and NFIP context: https://www.fema.gov/flood-maps

## 下一步

- 建立洪水预警术语、道路涉水、家庭撤离、避难所、灾后返回和长期恢复的 source card。
- 与 `post-flood-mold-moisture-indoor-recovery-continuity/`、`flood-insurance-nfip-claims-continuity/` 和 `disaster-temporary-housing-displacement-recovery-continuity/` 建立上下游边界。
