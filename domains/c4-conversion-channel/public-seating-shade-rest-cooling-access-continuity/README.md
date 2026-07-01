# Public Seating Shade Rest Cooling Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/public-seating-shade-rest-cooling-access-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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


`public-seating-shade-rest-cooling-access-continuity` 研究公共座椅、遮阴、树冠、候车休息、降温设施、冷却中心导向和可停留空间如何影响主体在城市、交通、排队、照护和高温场景中的有效行动时间。

> 核心问题：公共空间只允许移动而不允许休息，会把老人、儿童、残障者、慢病患者、孕产妇、户外劳动者和低收入人群排除出日常任务系统。

## 关注对象

- 公共座椅、候车亭、遮阳棚、树荫、喷雾/饮水/降温设施、空调公共空间、冷却中心和排队休息点。
- 空间分布、维护状态、无障碍高度、扶手、靠背、照明、安全感、敌意设计、开放时间和极端高温期间的可用性。
- 与热健康、城市树冠、公共交通、老年友好城市、残障可达、公共安全和公园管理的接口。

## Human Infra 链路

```text
公共休息、遮阴和降温接入稳定
  -> 主体在公共空间中可分段恢复体力和热负荷
  -> 中暑、跌倒、疲劳、放弃出行和排队失败风险下降
  -> 医疗、购物、通勤、照护、学校接送和社区参与更可完成
  -> 主体有效行动密度、恢复能力和公共空间选择权增强
```

## 非目标

- 不提供规避公共空间管理、占用设施、破坏敌意设计、露宿策略、跟踪人流、骚扰弱势群体或个案执法建议。
- 不替代城市规划、公共卫生、交通机构、公园部门、设施运营方、社会服务或法律专业人员。
- 不收集个人停留轨迹、脆弱人群实时位置、设施安防细节或敏感庇护/冷却中心拥挤数据。

## Source Signals

- CDC Heat and Health: https://www.cdc.gov/heat-health/
- EPA Heat Island Cooling Strategies: https://www.epa.gov/heatislands/heat-island-cooling-strategies
- EPA Trees and Vegetation: https://www.epa.gov/heatislands/using-trees-and-vegetation-reduce-heat-islands
- Ready.gov Extreme Heat: https://www.ready.gov/heat

## 下一步

- 建立 `rest point -> shade/cooling capacity -> exposure reduction -> recovery interval -> task continuity` 变量表。
- 区分日常座椅、候车休息、树荫降温、冷却中心、排队恢复和灾害期间临时休息设施。
- 与 `heat-health-thermal-safety-continuity`、`green-blue-infrastructure-urban-nature-cooling`、`transportation-access-mobility`、`parks-recreation-green-space-access-continuity` 和 `public-service-design-accessibility` 建立边界。
