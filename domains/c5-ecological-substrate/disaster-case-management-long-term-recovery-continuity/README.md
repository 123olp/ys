# Disaster Case Management Long Term Recovery Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/disaster-case-management-long-term-recovery-continuity` |
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


`disaster-case-management-long-term-recovery-continuity/` 研究灾后个案管理、长期恢复组织、未满足需求识别、服务转介和恢复计划如何把一次性救助转化为长期主体恢复。

> 核心问题：灾后恢复不是一次申请结束，而是住房、健康、收入、文件、交通、照护和心理支持的长链条；个案管理失败会让多个小断点叠加成长期功能下降。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 灾害破坏多个生活系统，并且恢复时间远长于新闻周期
  -> 主体需要持续识别未满足需求、转介资源、复盘进度和调整计划
  -> 个案管理把碎片化援助转成长期恢复路线
  -> 因此灾后个案管理是主体长期恢复连续性的协调域
```

## 关注对象

- FEMA Disaster Case Management、Long-Term Recovery Groups、VOAD、社区组织、社会服务转介和未满足需求评估。
- 需求评估、恢复计划、跨机构转介、跟踪、隐私、家庭照护、无障碍、退出条件和长期恢复指标。
- 与 `community-resource-navigation/` 的边界：该域关注日常资源导航；本域关注灾害后多系统恢复。

## Human Infra 模型链路

```text
灾后个案管理 T
  -> 改变未满足需求识别、计划、转介、跟踪和协同变量 X
  -> 改变主体长期恢复状态 S
  -> 改变长期住房不稳、医疗中断、收入断裂、照护崩溃和心理负担风险 λ(t)
  -> 影响主体恢复轨迹、有效时间和长期选择权
```

## 非目标

- 不提供个案管理服务、资源承诺、资格判断、社工替代、法律/医疗/福利建议或实时救助。
- 不收集灾民身份、地址、家庭结构、医疗、收入、创伤经历或未成年人信息。
- 不替代 FEMA、VOAD、地方长期恢复组织、社会服务机构或持证专业人员。

## Source Signals

- FEMA Disaster Case Management: https://www.fema.gov/assistance/individual/disaster-case-management
- National VOAD: https://www.nvoad.org/
- FEMA Individual Assistance: https://www.fema.gov/assistance/individual
