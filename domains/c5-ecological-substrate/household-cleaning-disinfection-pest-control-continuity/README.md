# Household Cleaning Disinfection Pest Control Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/household-cleaning-disinfection-pest-control-continuity` |
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


`household-cleaning-disinfection-pest-control-continuity` 研究家庭清洁、消毒、垃圾处理、害虫控制、化学品安全和室内卫生如何影响感染、过敏、毒性暴露、睡眠和家庭恢复环境连续性。

> 核心问题：家庭不是天然安全环境；清洁不足会制造感染和害虫风险，清洁过度或错误混合又会制造化学暴露，真正需要研究的是家庭卫生作为可治理的风险边界。

## 关注对象

- 表面清洁、消毒、洗手点、卫生间/厨房清洁、垃圾、霉味/潮湿信号、害虫迹象和家庭卫生例程。
- 消毒剂、清洁剂、农药、标签、储存、儿童/宠物暴露、误混合、通风和中毒风险。
- 老年、儿童、免疫低下、照护、租住、灾后水损、公共住房和多户住宅环境。
- 与 WASH、化学安全、毒物控制、室内空气、霉菌潮湿、病媒控制和产品安全的接口。

## Human Infra 链路

```text
家庭卫生治理连续
  -> 清洁、消毒、害虫控制和化学品使用保持可理解、可追踪、可恢复
  -> 感染、过敏、毒性暴露、害虫和卫生摩擦风险下降
  -> 家庭空间成为可恢复、可睡眠、可照护和可工作的环境
  -> 健康寿命、有效时间、照护安全和居住稳定性增强
```

## 非目标

- 不提供具体消毒配比、化学混合、杀虫剂使用、毒物处理、霉菌清除或医疗处置步骤。
- 不替代 CDC、EPA、毒物中心、公共卫生、房屋维修、害虫治理或医疗服务。
- 不鼓励危险化学品使用、标签规避、非法灭害、房东/租客对抗策略或恐慌性清洁。

## Source Signals

- CDC Cleaning and Disinfecting: https://www.cdc.gov/hygiene/cleaning/
- EPA Pesticide Labels: https://www.epa.gov/pesticide-labels
- National Pesticide Information Center: https://npic.orst.edu/
- Poison Help: https://www.poisonhelp.org/

## 下一步

- 建立 `surface/environment -> contamination/pest signal -> cleaning/disinfection control -> chemical exposure boundary -> recovery cost` 变量表。
- 区分日常清洁、感染暴发、灾后水损、害虫控制、儿童/宠物暴露和照护卫生场景。
- 与 `sterilization-disinfection-infection-control`、`chemical-safety-poison-control-toxicology`、`mold-dampness-indoor-biological-exposure` 和 `vector-borne-disease-environmental-control` 建立边界。
