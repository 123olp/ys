# Disaster Recovery Center Service Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/disaster-recovery-center-service-access-continuity` |
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


`disaster-recovery-center-service-access-continuity/` 研究灾后恢复中心、现场服务点、多机构协同窗口、移动 DRC 和线上恢复入口如何影响主体获取援助、信息和转介。

> 核心问题：灾后主体常同时面对住房、医疗、保险、文件、收入和法律问题；恢复中心把碎片化制度压缩成一个可进入、可理解、可转介的服务界面。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 灾害后主体需要跨机构完成信息、申请、补正、转介和服务接续
  -> 单一入口缺失会放大认知负担、交通成本和错过窗口风险
  -> 恢复中心将多机构服务变成可访问的恢复接口
  -> 因此灾后恢复中心是主体恢复资源可达性的基础设施域
```

## 关注对象

- FEMA Disaster Recovery Centers、移动恢复中心、州/地方服务点、非营利协同窗口和线上恢复入口。
- 开放时段、交通可达、语言服务、无障碍、隐私、服务转介、文件补正、数字辅助和服务退出。
- 与 `disaster-individual-assistance-benefits-navigation-continuity/` 的边界：该域关注援助申请链；本域关注多机构线下/混合服务入口。

## Human Infra 模型链路

```text
灾后恢复中心 T
  -> 改变服务入口、信息解释、材料补正、跨机构转介和无障碍变量 X
  -> 改变主体灾后制度接入状态 S
  -> 改变错过申请、重复奔波、恢复延迟和服务断裂风险 λ(t)
  -> 影响恢复速度、认知负担和未来选择权
```

## 非目标

- 不提供实时 DRC 位置、排队状态、个案资格、文件审核、现场指挥或服务承诺。
- 不收集个人身份、灾损、保险、收入、移民身份、医疗或家庭成员信息。
- 不替代 FEMA、州/地方应急管理、社区组织或正式恢复中心服务。

## Source Signals

- FEMA Disaster Recovery Centers: https://www.fema.gov/about/news-multimedia/mobile-products#drc
- FEMA Individual Assistance: https://www.fema.gov/assistance/individual
- DisasterAssistance.gov: https://www.disasterassistance.gov/
