# Disaster Recovery Relief Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/disaster-recovery-relief-continuity` |
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


`disaster-recovery-relief-continuity/` 研究灾后个人援助、恢复中心、临时安置、灾害贷款、救济服务和家庭恢复路径如何防止一次灾害清零主体长期积累。

> 核心问题：灾害结束不等于主体恢复；住房、现金、食物、文件、通信、医疗、债务和临时安置断裂，会把一次事件变成长期能力损耗。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体会遭遇灾害、事故、火灾、风暴、洪水和其他低频高冲击事件
  -> 事件后必须有恢复资金、临时住所、食物、文件、医疗、贷款和服务入口
  -> 灾后恢复失败会造成长期失能、贫困、迁移、关系断裂和资源损失
  -> 因此灾后恢复与救济连续性是主体持续性的尾部风险恢复域
```

## 关注对象

- 灾后个人援助、恢复中心、临时安置、开放避难所、灾害贷款、账单/食物支持和官方救济入口。
- 恢复时间、申请摩擦、文件丢失、身份连续、住房连续、债务压力和跨机构转介。
- 与 `emergency-preparedness-response/` 的边界：本域关注事件后的恢复与救济；应急准备与响应关注事前准备和事件中响应。

## Human Infra 模型链路

```text
灾后恢复与救济系统 T
  -> 改变资金、住房、食物、文件、医疗、贷款、安置和服务导航变量 X
  -> 改变主体灾后恢复状态 S
  -> 改变无家可归、医疗中断、债务升级、迁移、失业和长期能力损耗风险 λ(t)
  -> 影响主体恢复窗口、资源复原、家庭连续性和未来选择权
```

## 非目标

- 不提供个体灾害申请、资格判断、理赔、贷款、法律、税务、保险或住房建议。
- 不承诺避难所实时可用、资金发放、资格结果、灾害认定或恢复时间。
- 不支持虚假申请、身份冒用、材料伪造、囤积、黑市采购或制度规避。

## Source Signals

- USA.gov Disaster Assistance: https://www.usa.gov/disaster-assistance
- FEMA Disaster Recovery Centers: https://egateway.fema.gov/ESF6/DRCLocator
- SBA Disaster Assistance: https://www.sba.gov/funding-programs/disaster-assistance
- Benefits.gov Disaster Relief: https://www.benefits.gov/categories/Disaster%20Relief
- American Red Cross Open Shelters: https://www.redcross.org/get-help/disaster-relief-and-recovery-services/find-an-open-shelter.html
- Global Shelter Cluster: https://sheltercluster.org/

## 下一步

- 建立变量表：恢复资金、临时住所、文件恢复、食品援助、医疗连续、债务压力、申请摩擦和服务转介。
- 与 `emergency-alerts-communications/`、`social-protection-benefits-delivery/`、`insurance-risk-transfer/` 和 `housing-built-environment-stability/` 建立接口。
