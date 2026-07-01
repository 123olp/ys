# Tenant Screening Rental Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/tenant-screening-rental-access-continuity` |
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


Tenant Screening Rental Access Continuity 关注租房筛查、租客背景报告、驱逐记录、租金债务、犯罪记录、收入验证和算法化租赁准入如何影响住房连续性。

## 对象

- Tenant screening reports、eviction records、rental history、criminal background checks、income verification 和租赁平台筛查。
- 错误记录、身份混淆、旧记录、歧视性影响、申诉/更正、房东决策和住房不稳定。
- 租房申请、住房补贴、临时安置、低收入住房和灾后住房入口中的筛查层。

## Human Infra 价值

```text
主体持续性需要住房入口不被不透明筛查错误排除
-> 租房筛查把消费者报告、法院记录和平台评分转成居住资格
-> 错误或不透明筛查会造成拒租、押金负担、无家可归和服务断点
-> 可访问、可解释、可争议和可监督的筛查资料降低错误排除
-> 住房稳定更可能作为睡眠、照护、工作和恢复的基础继续存在
```

## 边界

- 本域不提供租房申请、驱逐记录处理、法律、房东谈判、住房补贴、背景报告争议或个案歧视投诉建议。
- 不判断某筛查报告、房东行为、拒租决定或驱逐记录是否合法。
- 不替代 HUD、FTC、CFPB、法院、住房机构、律师、房东、租客组织或公平住房机构。
- 只整理公开资料、报告机制、准入变量、错误风险、监督边界和禁止用途。

## 上游与下游

- 上游：`housing-built-environment-stability/`、`credit-consumer-reporting-access-continuity/`、`access-to-justice-legal-aid/`、`homelessness-unsheltered-health-continuity/`。
- 下游：`social-determinants-community-vulnerability/`、`public-service-design-accessibility/`、`administrative-burden-procedural-friction/`。

## 初始资料线索

- FTC tenant background check and tenant screening materials.
- CFPB tenant background check / rental screening resources.
- HUD fair housing and tenant screening guidance.
