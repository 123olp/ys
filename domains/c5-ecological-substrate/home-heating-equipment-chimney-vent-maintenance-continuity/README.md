# Home Heating Equipment Chimney Vent Maintenance Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-heating-equipment-chimney-vent-maintenance-continuity` |
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


`home-heating-equipment-chimney-vent-maintenance-continuity` 研究住宅供暖设备、烟囱、通风排气、燃料燃烧、维护记录和季节性启停如何影响冬季居住、安全睡眠、照护和恢复。

> 核心问题：供暖不是单纯温度，而是燃烧、排气、维护、通风和火灾/CO 风险共同构成的家庭生命支持接口。

## 关注对象

- furnace、boiler、fireplace、wood stove、chimney、venting、portable heater、燃料供应和季节性维护。
- 火灾、CO、通风不良、设备老化、清洁维护延迟、燃料中断和极端寒冷叠加。
- 老年人、儿童、慢病患者、低收入能源负担家庭、租房家庭和冬季停电场景。
- 与 CO 报警、烟雾报警、能源服务、冬季风暴、燃料可得和住房维修的接口。

## Human Infra 链路

```text
家庭供暖设备与排气维护连续
  -> 寒冷环境下室内温度、燃烧和排气边界更可靠
  -> 火灾、CO、冻伤、睡眠破坏和照护中断风险下降
  -> 居住、恢复、照护和慢病管理任务保持可执行
  -> 主体寒冷暴露风险下降并保持冬季行动窗口
```

## 非目标

- 不提供供暖设备维修、烟囱清理、燃气/油炉调试、空间加热器使用教程、排气判断或现场安全许可。
- 不替代 HVAC 专业人员、chimney professional、消防部门、能源公司、房东维修义务或应急服务。
- 不把高温供暖能力当成唯一目标；本域关注安全、可维护、可负担、可通风的供暖连续性。

## Source Signals

- USFA Home Heating Fire Safety: https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/heating/
- CDC Carbon Monoxide Poisoning Basics: https://www.cdc.gov/carbon-monoxide/about/index.html
- Ready.gov Winter Weather: https://www.ready.gov/winter-weather

## 下一步

- 建立 `heating equipment -> venting/maintenance state -> indoor thermal state -> household task -> continuity outcome` 变量表。
- 区分燃烧设备、电供暖、空间加热器、烟囱壁炉、租房维护和能源负担。
- 与 `carbon-monoxide-alarm-combustion-appliance-safety-continuity`、`winter-storm-cold-exposure-power-continuity` 和 `fuel-thermal-energy-service-continuity` 建立边界。
