# Sensitive Location Data Exposure Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/sensitive-location-data-exposure-continuity` |
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


Sensitive Location Data Exposure Continuity 关注位置数据、敏感地点、地理围栏、移动广告 ID、数据经纪、执法/商业访问和位置暴露如何影响主体安全、隐私、住房、医疗、工作和关系连续性。

## 对象

- Precise location data、sensitive location、geofence、mobile ad ID、SDK、location broker 和 movement history。
- 医疗机构、庇护所、宗教场所、学校、法院、工作地、家庭住址和高风险关系中的位置暴露。
- 位置数据进入广告、画像、骚扰、跟踪、执法请求、数据泄露和身份关联的路径。

## Human Infra 价值

```text
主体持续性需要移动轨迹不成为攻击面
-> 位置数据把生活、医疗、工作、关系和安全状态转成可推断轨迹
-> 敏感地点暴露会增加跟踪、歧视、勒索、报复、执法误伤和关系风险
-> 最小化、限制共享、删除、执法审查和数据经纪治理降低位置暴露
-> 主体更能安全移动、就医、求助、工作和恢复
```

## 边界

- 本域不提供跟踪定位、人肉搜索、执法规避、地理围栏广告投放、设备追踪、位置数据购买或去匿名化方法。
- 不判断某执法请求、商业数据访问、app 权限或 location broker 行为是否合法。
- 不收集、推断或公开真实位置、住址、工作地、庇护所、医疗地点、学校或法院出入记录。
- 只整理公开资料、暴露路径、敏感地点边界、治理变量和禁止用途。

## 上下游

- 上游：`digital-identity-security/`、`commercial-surveillance-adtech-profile-continuity/`、`data-broker-registry-opt-out-deletion-continuity/`。
- 下游：`personal-safety-violence-prevention/`、`survivor-safe-housing-emergency-transfer-continuity/`、`travel-advisory-consular-assistance-continuity/`。

## Source Signals

- Federal Trade Commission location data enforcement and data broker materials.
- NIST Privacy Framework.
- CPPA sensitive personal information and opt-out materials.
