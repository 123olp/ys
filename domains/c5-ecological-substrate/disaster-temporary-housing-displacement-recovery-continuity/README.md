# Disaster Temporary Housing Displacement Recovery Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/disaster-temporary-housing-displacement-recovery-continuity` |
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


`disaster-temporary-housing-displacement-recovery-continuity/` 研究灾后临时住房、过渡安置、租金援助、住房修复、可负担住房缺口和长期迁移如何影响主体恢复行动能力。

> 核心问题：灾害摧毁的不只是房屋，而是睡眠、储物、用药、儿童照护、工作通勤、通信和身份稳定；临时住房失败会把灾害转化为长期主体持续性损耗。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续性需要稳定睡眠、卫生、药物保存、照护和工作学习场所
  -> 灾害导致住房损坏、撤离、分散安置和长期流离
  -> 临时住房和修复路径决定主体能否从避险状态回到行动状态
  -> 因此灾后住房恢复是主体恢复连续性的核心域
```

## 关注对象

- FEMA temporary housing assistance、rental assistance、direct housing、HUD 灾后住房恢复、CDBG-DR 和地方安置系统。
- 住房损坏评估、临时租赁、无障碍住宿、家庭不分离、宠物/医疗需求、学校工作通勤和长期重建。
- 与 `evacuation-route-transportation-shelter-plan-continuity/` 的边界：该域关注灾前撤离与避难计划；本域关注灾后居住稳定。

## Human Infra 模型链路

```text
灾后临时住房与修复支持 T
  -> 改变住所可用性、安置稳定、卫生、通勤、药物保存和家庭照护变量 X
  -> 改变主体灾后生活基础状态 S
  -> 改变失眠、失学失业、治疗中断、家庭分离和迁移风险 λ(t)
  -> 影响有效时间、恢复能力和长期选择权
```

## 非目标

- 不提供房源推荐、资格判断、租约法律建议、保险理赔建议、占用规避或个案安置指导。
- 不收集地址、住房损失、家庭成员、移民身份、收入或医疗需求等敏感资料。
- 不替代 FEMA、HUD、地方住房机构、保险机构、房东租客法律援助或灾后个案管理。

## Source Signals

- FEMA Individual Assistance Housing: https://www.fema.gov/assistance/individual/housing
- FEMA Direct Housing: https://www.fema.gov/assistance/individual/direct-housing
- HUD Disaster Resources: https://www.hud.gov/program_offices/comm_planning/cdbg-dr
- DisasterAssistance.gov: https://www.disasterassistance.gov/
