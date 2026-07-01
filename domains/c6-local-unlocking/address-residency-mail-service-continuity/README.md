# 地址、居住地与邮件服务连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/address-residency-mail-service-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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


本域研究地址、居住地证明和邮件转递如何成为服务通知、资格判断、学校、医疗、税务、投票、福利、保险、法院和灾害救援的路由基础设施。它关注地址连续性和地址断点，不提供个人迁址、居住证明或邮政操作建议。

## 研究对象

- 通信地址、居住地址、服务地址、邮寄地址和无固定住址场景的替代联系机制。
- 邮件转递、地址变更通知、政府账户地址更新和关键通知送达。
- 地址与辖区、学校、投票、税务、福利、医疗网络、保险费率、应急服务和灾后救援的关系。
- 住房不稳定、无家可归、迁移、灾害、家庭暴力安全地址和数字服务通知断点。

## 价值链路

```text
服务系统必须知道主体在哪里以及如何联系主体
  -> 地址和邮件服务把主体连接到通知、资格、辖区、学校、医疗、税务和救援系统
  -> 迁居、无固定住址、邮件丢失或地址未同步会造成通知失效、资格中断和服务错位
  -> 地址连续性把空间位置和制度通信转化为可恢复的服务路由层
```

## 关键问题

- 地址在哪些系统中同时扮演位置、通信、辖区和资格变量？
- 地址变化如何影响医疗、福利、税务、学校、投票、保险、法院和灾害救援？
- 邮件服务中断如何把名义权利转化为实际缺席、逾期、丢失和默认失败？
- 对无固定住址、流离失所和安全地址需求主体，如何理解地址基础设施的包容性边界？

## 上游与下游

- 上游：`housing-built-environment-stability/`、`homelessness-unsheltered-health-continuity/`、`migration-displacement-humanitarian-continuity/`、`geospatial-navigation-location-infrastructure/`。
- 下游：`public-service-design-accessibility/`、`social-protection-benefits-delivery/`、`civic-participation-election-access/`、`tax-administration-filing-record-continuity/`、`disaster-recovery-relief-continuity/`。

## 非目标

- 不提供个人 USPS、IRS、SSA、DMV、学校、法院、投票、福利或保险地址变更建议。
- 不判断个人居住地、税务居民身份、投票资格、学区资格、福利资格或保险费率。
- 不协助隐藏地址、规避法律通知、逃避债务、规避抚养义务、规避执法或欺骗服务系统。

## 初始资料入口

- USPS Change of Address
- USA.gov: Change your address
- IRS: Address changes
- SSA and state benefits account address update official pages
