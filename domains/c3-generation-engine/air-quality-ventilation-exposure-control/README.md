# Air Quality Ventilation Exposure Control

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/air-quality-ventilation-exposure-control` |
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


空气质量、通风与暴露控制域研究：当主体持续性依赖可呼吸、可恢复、可集中注意力的环境时，室内外空气污染、通风、过滤、烟雾和气溶胶暴露如何成为基础条件。

## 对象

- 室外空气污染、颗粒物、臭氧、氮氧化物、野火烟雾和交通/工业暴露。
- 室内空气质量、通风、过滤、空气交换、二氧化碳、燃烧源、霉菌和建筑材料释放。
- 感染性气溶胶、工作/学校/照护场所空气暴露和公共空间通风治理。
- 空气质量监测、风险沟通、预警、标准、建筑运行和低成本暴露降低能力。
- 空气暴露对呼吸、心血管、认知、睡眠、学习、工作和长期健康风险的影响。

## Human Infra 价值

主体不是只在身体内部维持生命，也持续暴露在可吸入环境中。空气质量与通风域把“环境是否允许持续呼吸、学习、工作、照护和恢复”纳入主体持续性模型，避免把呼吸风险只缩小成肺部疾病问题。

```text
空气暴露被监测与控制
  -> 呼吸、心血管、感染和认知负担下降
  -> 学校、工作、照护和公共空间更可持续
  -> 有效时间、恢复能力和未来选择权提高
```

## 边界

本域只整理空气质量、通风、过滤、监测、标准和公共风险治理资料。

不提供：

- 个体医疗诊断、治疗、用药、氧疗、过敏/哮喘管理或急救建议。
- HVAC 设计、施工、电气改造、过滤设备采购、现场检测或验收建议。
- 危险环境进入、烟雾事故处置、化学泄漏处理、灾害撤离或实时安全指挥。
- 规避监管、篡改监测、虚假合规、污染源隐藏或危险清理操作。

## 上游与下游

- 上游：`planetary-health-environment/`、`weather-climate-observation-forecasting/`、`building-fire-life-safety-codes/`、`housing-built-environment-stability/`。
- 下游：`respiratory-oxygenation/`、`cardiovascular-resilience/`、`attention-executive-control/`、`occupational-exposure-industrial-hygiene/`。

## 初始资料线索

- WHO air pollution resources。
- EPA indoor air quality and AirNow resources。
- CDC/NIOSH ventilation resources。
- ASHRAE ventilation and infectious aerosol standards。
