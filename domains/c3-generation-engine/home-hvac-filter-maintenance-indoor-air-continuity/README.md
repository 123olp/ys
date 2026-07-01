# Home HVAC Filter Maintenance Indoor Air Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/home-hvac-filter-maintenance-indoor-air-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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


`home-hvac-filter-maintenance-indoor-air-continuity` 研究住宅 HVAC 滤网、滤网匹配、维护周期、气流阻力、住户提醒和设备可达性如何影响室内空气、睡眠、认知、呼吸恢复和家庭任务连续性。

> 核心问题：家庭通风和制冷供暖系统不是只提供温度，也持续决定空气中颗粒物、过敏原和污染物能否被过滤；滤网维护失败会把可呼吸环境变成隐形损耗条件。

## 关注对象

- HVAC 滤网、回风口、滤网尺寸、MERV 语义、滤网更换周期、脏堵、气流下降、噪声、能耗和维护提醒。
- 租房、多户住宅、低收入家庭、老人照护、儿童、哮喘/COPD、宠物家庭和高尘暴露家庭的滤网可达性。
- 与制冷维护、供暖排气、空气质量总域、湿度控制和过敏原源控制的接口。
- 滤网状态如何改变睡眠、学习、居家办公、照护、慢病管理和恢复窗口。

## Human Infra 链路

```text
HVAC 滤网维护连续
  -> 室内颗粒物、过敏原和循环空气负荷更可控
  -> 睡眠、呼吸舒适、认知负荷和恢复质量更稳定
  -> 家庭学习、工作、照护、慢病管理和高温/寒冷恢复任务不被空气负担切断
  -> 主体有效时间和居住执行连续性提高
```

## 非目标

- 不提供 HVAC 设计、维修、拆装、电气操作、风管改造、滤网产品推荐、MERV 处方、能效审计或现场验收建议。
- 不替代 EPA、DOE、ASHRAE、房东/物业、HVAC 专业人员、医生、公共卫生或本地住房部门。
- 不判断某个家庭应使用何种滤网、多久更换、是否适配设备或是否会损坏系统。

## Source Signals

- EPA Air Cleaners and Air Filters in the Home: https://www.epa.gov/indoor-air-quality-iaq/air-cleaners-and-air-filters-home
- EPA Indoor Air Quality: https://www.epa.gov/indoor-air-quality-iaq
- DOE Maintaining Your Air Conditioner: https://www.energy.gov/energysaver/maintaining-your-air-conditioner

## 下一步

- 建立 `filter state -> airflow/particle burden -> occupant task -> continuity outcome` 变量表。
- 区分滤网缺失、尺寸不合、过期、脏堵、过高阻力、维护不可达和租房责任不清。
- 与 `home-cooling-heat-pump-air-conditioning-maintenance-continuity`、`air-quality-ventilation-exposure-control` 和 `household-dust-allergen-source-control-continuity` 建立边界。
