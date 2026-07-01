# Community Resource Navigation

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/community-resource-navigation` |
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


`community-resource-navigation/` 研究 211、社区资源目录、社会需求筛查、转介、闭环回访和本地服务导航。

> 核心问题：资源存在不等于主体能够找到、理解、申请、抵达和持续使用；社区资源导航是把分散服务转化为实际支持的接口。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 资源、服务和支持必须能被发现、匹配、转介和确认到达
  -> 本地服务网络必须降低搜索成本、行政摩擦和断点
  -> 社区资源才能从名义存在转化为主体恢复与持续行动能力
```

## 关注对象

- 211、本地资源目录、Open Referral HSDS、社会需求筛查、闭环转介和服务导航。
- 食物、住房、交通、医疗、心理健康、照护、法律援助和危机服务入口的连接逻辑。
- 资源目录新鲜度、服务资格不确定、转介失败、回访缺失、人工帮助和跨机构协作。
- 与 `social-protection-benefits-delivery/`、`healthcare-access-continuity/`、`health-literacy-navigation/` 和 `resource-social-infra/` 的接口。

## Human Infra 模型链路

```text
社区资源导航基础设施
  -> 改变资源发现、匹配、转介、回访和人工协助能力
  -> 改变主体获得食物、住房、医疗、交通、照护和危机支持的状态
  -> 降低服务碎片化、申请放弃、资源错配和恢复路径中断风险
  -> 增强抗冲击能力、有效时间和未来选择权
```

## 非目标

- 不判断个人资格、申请策略、福利结果、机构质量或资源实时可用性。
- 不替代 911、988、危机热线、社工、法律援助、医疗或福利机构。
- 不收集、交换或公开敏感个人需求数据。

## Source Signals

- 211: https://www.211.org/
- Open Referral: https://openreferral.org/
- Human Services Data Specification: https://docs.openreferral.org/en/latest/hsds/
- The Gravity Project: https://thegravityproject.net/
- CMS Accountable Health Communities Model: https://www.cms.gov/priorities/innovation/innovation-models/ahcm

## 下一步

- 建立社区资源导航变量表：资源发现、目录更新、资格不确定、转介完成、闭环回访、人工协助和隐私边界。
- 与 `social-protection-benefits-delivery/` 拆分福利制度递送边界，与 `resource-social-infra/` 拆分资源供给边界。
- 整理 211、Open Referral、Gravity Project 和 AHC 的 Source Cards。
