# 洪水保险、NFIP 与理赔连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/flood-insurance-nfip-claims-continuity` |
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


本域研究洪水保险、National Flood Insurance Program、private flood insurance、flood maps、waiting period、coverage limits、proof of loss、claim、appeal 和 mitigation 如何影响主体住房恢复、财产恢复和灾后现金流。它关注洪水风险转移的专门执行层，而不是投保建议、理赔代办或法律建议。

## 研究对象

- NFIP、private flood insurance、flood hazard maps、Special Flood Hazard Area、lender requirement 和 waiting period。
- Building coverage、contents coverage、coverage limits、deductible、exclusions、elevation、mitigation 和 policy renewal。
- Flood claim、adjuster、proof of loss、appeal、ICC coverage、灾后援助和重复损失风险。
- 与房主险、灾害住房恢复、水文洪水控制、房贷和地方土地使用的边界。

## 价值链路

```text
主体住房暴露于洪水风险
  -> 洪水保险把普通房主险之外的水灾损失转移到专门保单和 NFIP 执行链
  -> flood map、coverage 和 proof of loss 决定灾后是否能获得恢复资金
  -> waiting period、限额、除外责任或理赔失败会把洪水事件变成长期住房断裂
  -> 洪水保险连续性把水灾风险纳入可审查的住房恢复和风险分摊系统
```

## 关键问题

- 洪水保险为什么不能被普通房主险自动覆盖？
- flood map、lender requirement 和 waiting period 如何影响保险可用性？
- proof of loss、adjuster 和 appeal 如何决定灾后资金恢复？
- 洪水保险如何与 FEMA 援助、房贷、重建和迁居选择连接？

## 上游与下游

- 上游：`water-resources-hydrology-continuity/`、`dams-levees-flood-control-assets/`、`real-property-title-deed-record-continuity/`。
- 下游：`disaster-housing-recovery-rebuilding-continuity/`、`homeowners-renters-property-insurance-claims-continuity/`、`public-works-asset-management/`、`urban-planning-land-use-zoning-continuity/`。

## 非目标

- 不提供洪水保险购买、保额选择、地图申诉、proof of loss 填写、理赔、appeal、重建、搬迁或法律建议。
- 不判断某处房产是否需要洪水保险、某张 flood map 是否正确、某笔 claim 是否应赔或赔多少。
- 不协助虚假洪水损失、伪造 proof of loss、夸大灾损、隐瞒既有损害、保险欺诈、绕过 lender 要求或骗取灾害援助。

## 初始资料入口

- FEMA FloodSmart / National Flood Insurance Program
- FEMA flood maps and flood insurance claim materials
- State insurance department flood insurance materials
- Ready.gov flood preparedness materials
