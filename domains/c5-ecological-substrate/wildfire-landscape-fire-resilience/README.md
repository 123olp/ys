# Wildfire Landscape Fire Resilience

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/wildfire-landscape-fire-resilience` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 主要提供主体展开未来所需的基础环境、资源、治理或基础设施。 |
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


`wildfire-landscape-fire-resilience/` 研究野火、景观燃料、荒野-城市交界、烟雾、疏散、火灾天气和社区防火如何影响主体持续性。

> 核心问题：野火不是单一灾害事件，而是气候、土地管理、建筑、空气、交通、通信、保险、公共卫生和社区恢复共同作用的复合风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要安全居住、清洁空气、可撤离路径、通信和恢复能力
  -> 野火会同时破坏住房、空气质量、电力、通信、交通、医疗和保险可得性
  -> 景观燃料、建筑防护、早期预警、疏散和恢复决定火灾风险函数
  -> 野火韧性失败会把长期积累转化为一次性损失和长期健康负担
```

## 关注对象

- 野火风险、火灾天气、景观燃料、WUI、社区防火、疏散、烟雾暴露和恢复。
- 与 `weather-climate-observation-forecasting/` 的边界：天气域关注火灾天气预测；本域关注火灾风险治理和社区韧性。
- 与 `air-quality-ventilation-exposure-control/` 的边界：空气域关注暴露控制；本域关注野火作为复合风险源。
- 与 `building-fire-life-safety-codes/` 的边界：建筑消防域关注建筑和室内生命安全；本域关注景观、社区和区域火灾风险。

## Human Infra 模型链路

```text
野火景观和社区韧性
  -> 火灾发生、蔓延、暴露、疏散和恢复条件改善
  -> 住房损失、烟雾暴露、医疗中断、通信断线和经济冲击下降
  -> 家庭、社区、基础设施和公共卫生恢复时间缩短
  -> 主体持续性免于被复合灾害一次性击穿
```

## 非目标

- 不提供实时火场行动、灭火战术、疏散路线、纵火、规避指挥、设备操作或保险索赔建议。
- 不替代官方火灾警报、应急管理、消防机构和公共卫生指引。
- 不提供可被用于制造火灾、扩大火势或干扰救援的信息。

## Source Signals

- UNDRR Wildfire Risk: https://www.undrr.org/
- US Fire Administration Wildland Urban Interface: https://www.usfa.fema.gov/wui/
- National Interagency Fire Center: https://www.nifc.gov/

## 下一步

- 建立野火变量表：燃料、WUI 暴露、火灾天气、疏散、烟雾、建筑防护、通信、电力和恢复时间。
- 整理 UNDRR、USFA、NIFC、WHO wildfire smoke 和地方 firewise 资料卡片。
- 与天气、空气质量、建筑、应急预警、能源、通信、保险和住房域建立链路。
