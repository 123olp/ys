# Home Cooling Heat Pump Air Conditioning Maintenance Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/home-cooling-heat-pump-air-conditioning-maintenance-continuity` |
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


`home-cooling-heat-pump-air-conditioning-maintenance-continuity` 研究住宅空调、热泵、过滤、制冷能力、维护延迟和高温负荷如何影响睡眠、慢病管理、药品保存、学习和家庭恢复。

> 核心问题：制冷不是舒适装饰，而是在热浪、慢病、睡眠和室内空气条件下维持主体可行动状态的家庭运行系统。

## 关注对象

- 中央空调、window AC、portable AC、heat pump、过滤器、室外机、冷媒系统、维护计划和能源成本。
- 高温、湿度、设备故障、滤网堵塞、租房维护、低收入能源负担和停电叠加。
- 睡眠质量、慢病症状、药品/设备保存、儿童老人照护、远程工作学习和灾后恢复。
- 与极端高温、公共降温中心、能源可负担性、室内空气过滤和备电的接口。

## Human Infra 链路

```text
家庭制冷与热泵维护连续
  -> 热浪和高湿条件下室内热负荷更可控
  -> 睡眠、慢病管理、照护、药品保存和学习工作受热中断下降
  -> 主体恢复能力、注意力和居住稳定性提高
  -> 高温风险不再直接压缩有效行动时间
```

## 非目标

- 不提供空调维修、冷媒操作、热泵安装、设备选型、温度处方、能耗审计或个案医疗建议。
- 不替代 HVAC 专业人员、能源援助、房东维修义务、公共卫生热警报、医疗建议或应急服务。
- 不把持续低温当作目标；本域关注热风险下的安全、可负担、可维护制冷能力。

## Source Signals

- Energy Saver Maintaining Your Air Conditioner: https://www.energy.gov/energysaver/maintaining-your-air-conditioner
- Energy Saver Heat Pump Systems: https://www.energy.gov/energysaver/heat-pump-systems
- CDC Heat and Health: https://www.cdc.gov/heat-health/about/index.html

## 下一步

- 建立 `cooling equipment -> maintenance/filter state -> indoor heat exposure -> task loss -> continuity outcome` 变量表。
- 区分热泵、中央空调、窗机、便携空调、租房维护、能源负担和停电场景。
- 与 `extreme-heat-cooling-public-health-continuity`、`energy-access-resilience` 和 `indoor-ventilation-filtration-outbreak-control-continuity` 建立边界。
