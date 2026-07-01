# Home Humidity Dehumidifier Moisture Control Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-humidity-dehumidifier-moisture-control-continuity` |
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


`home-humidity-dehumidifier-moisture-control-continuity` 研究家庭湿度、除湿机、加湿器、冷凝、地下室潮湿、舒适区间、设备维护和水分控制如何影响睡眠、呼吸、霉菌风险、材料损耗和恢复空间。

> 核心问题：湿度不是舒适度小问题，而是把空气、建筑材料、霉菌、睡眠、呼吸和设备维护连接起来的家庭控制变量；湿度失控会让居住空间变成长期恢复负担。

## 关注对象

- 相对湿度、冷凝、除湿机、加湿器、排水、滤网/水箱维护、地下室潮湿、季节变化、空调除湿和通风。
- 高湿导致的霉菌/尘螨风险、低湿导致的舒适/刺激问题、睡眠质量、儿童/老人照护和呼吸敏感人群。
- 与水损霉菌、地下室进水、天气化围护结构、HVAC 滤网和家庭清洁的接口。
- 湿度控制如何影响床上用品、衣物、食品储存、学习办公、慢病恢复和居住稳定。

## Human Infra 链路

```text
家庭湿度控制连续
  -> 潮湿、冷凝、霉菌条件、尘螨负荷和干燥刺激更可控
  -> 睡眠、呼吸舒适、材料保存、清洁负担和恢复空间更稳定
  -> 家庭照护、工作学习、慢病管理和灾后恢复不被湿度失控切断
  -> 主体居住基础设施和有效时间提高
```

## 非目标

- 不提供霉菌清理、除湿设备选型、加湿器处方、建筑维修、防水施工、空调维修、水损评估、医疗建议、租房纠纷或保险建议。
- 不替代 EPA、CDC、WHO、地方住房部门、建筑/水损专业人员、物业、医生或公共卫生机构。
- 不判断某个房间的湿度数值是否安全、是否需要检测、是否存在霉菌或是否需要施工。

## Source Signals

- EPA Mold Resources: https://www.epa.gov/mold
- EPA Indoor Air Quality: https://www.epa.gov/indoor-air-quality-iaq
- CDC Mold: https://www.cdc.gov/mold-health/

## 下一步

- 建立 `humidity/moisture state -> biological/material burden -> room function -> continuity outcome` 变量表。
- 区分高湿、低湿、冷凝、地下室潮湿、灾后潮湿、除湿机维护和加湿器卫生。
- 与 `mold-dampness-indoor-biological-exposure`、`basement-flooding-sump-pump-moisture-recovery-continuity` 和 `weatherization-insulation-air-sealing-thermal-envelope-continuity` 建立边界。
