# Weatherization Insulation Air Sealing Thermal Envelope Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/weatherization-insulation-air-sealing-thermal-envelope-continuity` |
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


`weatherization-insulation-air-sealing-thermal-envelope-continuity` 研究住宅围护结构、保温、气密、门窗、渗漏、通风平衡和天气化如何影响冷热暴露、能源负担、湿度、空气质量和居住稳定。

> 核心问题：供暖制冷设备只是主动系统，围护结构决定热量、湿气和空气如何流失；差的热边界会把能源、健康和住房风险长期放大。

## 关注对象

- insulation、air sealing、duct sealing、weatherstripping、windows/doors、thermal envelope、ventilation balance 和 energy audit。
- 冷热暴露、能源负担、潮湿霉菌、室内污染物积累、施工质量、租房维修和灾后住房恢复。
- 老旧住房、低收入家庭、儿童老人、慢病患者、极端天气和住房不稳定家庭。
- 与供暖、制冷、室内空气、霉菌潮湿、能源援助和住房维修的接口。

## Human Infra 链路

```text
天气化保温气密与围护结构连续
  -> 房屋热边界、湿气边界和空气交换更可控
  -> 供暖制冷负担、冷热暴露、潮湿和空气质量风险下降
  -> 睡眠、照护、学习、工作和恢复空间更稳定
  -> 主体长期居住韧性和资源可用性提高
```

## 非目标

- 不提供施工教程、材料选择、能效审计、保温改造方案、霉菌清理、通风设计、补贴申请或房屋交易建议。
- 不替代 Weatherization Assistance Program、持证承包商、能源审计师、建筑规范、房东维修义务或公共卫生建议。
- 不把气密性越高视为单向目标；本域关注保温、气密、通风、湿度和室内空气之间的平衡。

## Source Signals

- Energy Saver Weatherize: https://www.energy.gov/energysaver/weatherize
- Energy Saver Insulation: https://www.energy.gov/energysaver/insulation
- DOE Weatherization Assistance Program: https://www.energy.gov/scep/wap/weatherization-assistance-program

## 下一步

- 建立 `thermal envelope -> air/moisture flow -> energy burden/exposure -> household task -> continuity outcome` 变量表。
- 区分老旧住房、低收入天气化、租房维修、灾后恢复、潮湿霉菌和通风不足风险。
- 与 `mold-dampness-indoor-biological-exposure`、`energy-access-resilience` 和 `home-cooling-heat-pump-air-conditioning-maintenance-continuity` 建立边界。
