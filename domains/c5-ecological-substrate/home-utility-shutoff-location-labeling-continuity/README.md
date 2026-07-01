# Home Utility Shutoff Location Labeling Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-utility-shutoff-location-labeling-continuity` |
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


`home-utility-shutoff-location-labeling-continuity` 研究家庭水、电、燃气等关键公用设施的关断位置、责任边界、标签、地图和交接资料如何影响事故响应、灾害恢复、维修协作和照护连续性。

> 核心问题：家庭基础设施在正常状态下经常“隐形”；一旦漏水、燃气风险、停电、维修或灾后返家发生，家庭成员、照护者、房东、维修人员和应急人员是否能知道关键位置在哪里，会直接改变损失扩大、响应延误和恢复失败风险。

## 关注对象

- 水、电、燃气、供暖、网络和其他家庭关键服务的入口位置、标识、访问状态、权限边界和资料备份。
- 租房、合租、老年照护、残障支持、短租、房屋托管、灾害返家、维修交接和临时照护场景。
- 标签、家庭地图、照片索引、责任说明、联系人和更新周期如何降低家庭系统不可读性。
- 与燃气泄漏边界、电气安全、水管维护、物业责任、应急文件和家庭通信计划的接口。

## Human Infra 链路

```text
家庭关键服务位置可读
  -> 关键信息不再只存在于单个家庭成员记忆中
  -> 照护者、维修人员、房东或应急响应者能更快理解家庭系统边界
  -> 漏水、燃气风险、停电、维修延误和灾后返家摩擦下降
  -> 居住、照护、卫生、通信和恢复任务连续性提高
```

## 非目标

- 不提供关断操作教程、电气面板操作、燃气阀门操作、管线维修、现场判断、灾后返家许可、房屋改造或个案安全建议。
- 不替代公用事业公司、消防部门、持证电工、持证 plumber/HVAC、房东/物业、本地规范或应急服务。
- 不收集住址、设施照片、阀门位置、面板位置、门禁、账户、住户身份或其他可被滥用的家庭基础设施细节。

## Source Signals

- Ready.gov Make a Plan: https://www.ready.gov/plan
- Ready.gov Document and Insure Your Property: https://www.ready.gov/sites/default/files/2020-03/ready_document-and-insure-your-property.pdf
- USFA Appliance and Electrical Fire Safety: https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/appliance-and-electrical/

## 下一步

- 建立 `utility location knowledge -> label/map state -> emergency/repair handoff -> continuity outcome` 变量表。
- 区分业主、租客、照护者、短期访客、物业和专业维修人员的权限边界。
- 与 `natural-gas-propane-leak-shutoff-continuity`、`residential-electrical-wiring-outlet-safety-continuity` 和 `premise-plumbing-backflow-cross-connection-continuity` 建立边界。
