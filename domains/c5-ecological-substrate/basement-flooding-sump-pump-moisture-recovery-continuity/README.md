# Basement Flooding Sump Pump Moisture Recovery Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/basement-flooding-sump-pump-moisture-recovery-continuity` |
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


`basement-flooding-sump-pump-moisture-recovery-continuity` 研究地下室进水、sump pump、排水、潮湿、断电、霉菌风险和洪水后恢复如何影响住房可居住性、储物、设备、空气质量和恢复时间。

> 核心问题：家庭底层空间常承载设备、文件、药品、储物和避难功能；进水与潮湿恢复失败会把一次性水害转成长期空气、财产和居住稳定性损耗。

## 关注对象

- 地下室进水、sump pump、排水、地表径流、断电、备电、潮湿材料、清理恢复和霉菌风险。
- 电气设备、HVAC、热水器、文件、药品、食物储备、可访问通道和家庭恢复空间。
- 洪水后室内空气、干燥时间、维修协调、保险/援助、租赁责任、老年/残障家庭和低收入恢复负担。
- 与家庭维修、灾后恢复、室内空气、公共卫生和住房稳定的接口。

## Human Infra 链路

```text
地下室进水与潮湿恢复连续
  -> 家庭底层空间水害更早发现并可恢复
  -> 设备、文件、储物、空气质量和通行功能更可靠
  -> 霉菌、财产损失、维修延误和居住中断风险下降
  -> 家庭恢复空间、有效时间和资源稳定性增强
```

## 非目标

- 不提供电气进入、抽水操作、霉菌清理步骤、施工防水、保险索赔、承包商谈判或灾害现场判断。
- 不替代 EPA、CDC、FEMA、地方应急管理、持证维修商、电工、保险、房东/物业或公共卫生。
- 不把地下室进水问题写成 DIY 灾害恢复教程；本域只处理风险链、恢复断点和主体持续性后果。

## Source Signals

- EPA Flood Cleanup to Protect Indoor Air and Health: https://www.epa.gov/emergencies-iaq/flood-cleanup-protect-indoor-air-and-your-health
- EPA Septic maintenance context for sewage/flood interfaces: https://www.epa.gov/septic/why-maintain-your-septic-system

## 下一步

- 建立 `water intrusion -> pump/power/drainage state -> drying/repair delay -> housing task -> continuity outcome` 变量表。
- 区分普通渗水、暴雨、河流洪水、污水回流、断电、租房、多代同住和医疗设备家庭场景。
- 与 `disaster-recovery-relief-continuity`、`mold-dampness-indoor-biological-exposure` 和 `household-maintenance-repair-contractor-continuity` 建立边界。
