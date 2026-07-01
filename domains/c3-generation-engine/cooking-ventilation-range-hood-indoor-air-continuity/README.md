# Cooking Ventilation Range Hood Indoor Air Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/cooking-ventilation-range-hood-indoor-air-continuity` |
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


`cooking-ventilation-range-hood-indoor-air-continuity` 研究烹饪排风、抽油烟机、燃气/电烹饪排放、颗粒物、氮氧化物、气味、厨房空气和餐食任务如何影响居住恢复与家庭执行连续性。

> 核心问题：做饭是高频基础任务，但烹饪同时会释放颗粒物、气味和燃烧/加热副产物；如果排风与源控制失败，餐食生产会反向消耗睡眠、呼吸、注意力和居住舒适。

## 关注对象

- 抽油烟机、排风扇、厨房通风、燃气灶、电炉、煎炒油烟、烤箱、厨房颗粒物、NO2、气味和湿热。
- 家庭餐食准备、儿童/老人照护、开放式厨房、租房、多户住宅、低通风住房和高频烹饪家庭。
- 与食品安全、厨房火灾、CO 报警、燃气泄漏、VOC/气味源控制和室内空气总域的接口。
- 烹饪空气负荷如何影响睡眠、呼吸舒适、清洁负担、学习办公和家庭成员共同使用空间。

## Human Infra 链路

```text
烹饪排风连续
  -> 烹饪产生的颗粒物、燃烧副产物、气味和湿热更可控
  -> 餐食准备不再把厨房和居住空间转成慢性空气负担
  -> 家庭营养、照护、学习、工作、睡眠和恢复任务稳定
  -> 主体日常执行密度和居住可持续性提高
```

## 非目标

- 不提供燃气设备维修、抽油烟机安装、电气改造、管道设计、火灾处置、CO 急救、烹饪教程、产品购买或个案室内空气安全认证。
- 不替代 EPA、CDC、USFA、地方建筑/消防/住房部门、燃气公司、物业、设备专业人员或医生。
- 不把排风资料写成替代食品安全、火灾预防、燃气泄漏处置、CO 报警或医学管理的单一方案。

## Source Signals

- EPA Indoor Particulate Matter: https://www.epa.gov/indoor-air-quality-iaq/indoor-particulate-matter
- EPA Combustion Pollutants in Your Home: https://www.epa.gov/indoor-air-quality-iaq/combustion-pollutants-your-home
- EPA Indoor Air Quality: https://www.epa.gov/indoor-air-quality-iaq

## 下一步

- 建立 `cooking source -> ventilation/capture state -> indoor air burden -> meal task -> continuity outcome` 变量表。
- 区分燃气烹饪、电烹饪、高温煎炒、长时烹饪、开放式厨房和低通风住房。
- 与 `cooking-meal-preparation-kitchen-safety-continuity`、`carbon-monoxide-alarm-combustion-appliance-safety-continuity` 和 `natural-gas-propane-leak-shutoff-continuity` 建立边界。
