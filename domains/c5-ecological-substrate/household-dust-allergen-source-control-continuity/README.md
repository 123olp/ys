# Household Dust Allergen Source Control Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/household-dust-allergen-source-control-continuity` |
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


`household-dust-allergen-source-control-continuity` 研究家庭灰尘、尘螨、宠物皮屑、织物、床品、地毯、清洁频率、HEPA 吸尘和源控制如何影响过敏负荷、睡眠、注意力和家庭恢复。

> 核心问题：灰尘和室内过敏原不是单次清洁问题，而是跨床、织物、宠物、湿度和空气流动的持续负荷；当源控制失败，主体会用更多注意力、睡眠和有效时间支付环境摩擦。

## 关注对象

- 室内灰尘、尘螨、宠物皮屑、蟑螂/害虫残留、花粉带入、床品、地毯、软装、吸尘、湿擦、HEPA 过滤和清洁任务负担。
- 哮喘、过敏、鼻炎、儿童、老人、宠物家庭、租房、多户住宅和资源受限家庭。
- 与家庭清洁、湿度控制、霉菌潮湿、虫害控制、空气过滤和呼吸慢病维护的接口。
- 灰尘过敏原负荷如何影响睡眠、学习、工作、儿童照护、药物依从和社交/家务执行。

## Human Infra 链路

```text
家庭灰尘过敏原源控制连续
  -> 尘螨、宠物皮屑、害虫残留和室内灰尘负荷更可控
  -> 睡眠、呼吸舒适、注意力和家庭恢复摩擦下降
  -> 清洁、照护、学习、工作和慢病维护任务不被环境负荷反复打断
  -> 主体有效时间、恢复能力和家庭行动半径提高
```

## 非目标

- 不提供过敏诊断、哮喘治疗、药物建议、宠物处置建议、杀虫操作、清洁产品推荐、深度清洁教程、房屋检测或租房/法律建议。
- 不替代 EPA、CDC、NIH、医疗人员、害虫控制、物业、公共卫生或住房部门。
- 不判断某个家庭是否存在特定过敏原、应如何治疗、是否需要搬家或是否需要专业清理。

## Source Signals

- EPA Asthma Triggers: https://www.epa.gov/asthma/asthma-triggers-gain-control
- EPA Indoor Air Quality: https://www.epa.gov/indoor-air-quality-iaq
- CDC Asthma Triggers: https://www.cdc.gov/asthma/triggers.html

## 下一步

- 建立 `dust/allergen source -> cleaning/source-control state -> symptom/task burden -> continuity outcome` 变量表。
- 区分尘螨、宠物皮屑、蟑螂/害虫残留、花粉带入、织物/地毯蓄积和资源受限清洁负担。
- 与 `household-cleaning-disinfection-pest-control-continuity`、`allergic-atopic-disease-continuity` 和 `asthma-copd-maintenance-control-continuity` 建立边界。
