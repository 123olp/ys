# Immigration Status Residency Work Authorization Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/immigration-status-residency-work-authorization-continuity` |
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


本域研究移民身份、居留资格、工作授权、身份变更、身份续期和身份失效风险如何影响主体在一个制度内持续生活、工作、学习、医疗和连接家庭。

> 核心问题：主体能否继续行动，不只取决于是否在某地，还取决于是否有被承认的居留与工作资格；身份过期、文件延迟或授权断裂会把时间、收入、医疗、教育和家庭关系同时推入不稳定。

## 关注对象

- 签证、居留、永久居民、工作授权、身份变更、延期、续期、身份证明和雇佣资格核验。
- 身份过期、等待期间、文件丢失、地址变更、雇主依赖、家庭成员派生资格和服务资格断点。
- 移民身份与就业、教育、医疗、银行、住房、驾照、税务、公共福利和家庭团聚的接口。
- 与 `migration-displacement-humanitarian-continuity/` 的边界：迁移域关注移动和流离失所后的服务连续性；本域关注制度内居留和工作授权连续性。

## Human Infra 链路

```text
移民身份 / 居留 / 工作授权连续
  -> 主体在所在地拥有可证明、可续期、可核验的制度资格
  -> 工作、学习、医疗、住房、金融和家庭关系可以持续运行
  -> 过期、延误、雇主锁定、资格断裂和服务拒绝风险下降
  -> 主体获得跨时间的制度稳定和行动窗口
```

## 非目标

- 不提供签证、绿卡、居留、工作许可、身份变更、延期、加急、申诉、雇佣、税务或法律建议。
- 不判断个人是否有移民资格、工作资格、福利资格、入境资格或身份风险。
- 不协助伪造文件、规避 E-Verify/I-9、隐藏身份、绕过边境/执法、滥用签证或组织危险迁移。

## Source Signals

- USCIS Green Card: https://www.uscis.gov/green-card
- USCIS Employment Authorization: https://www.uscis.gov/green-card/green-card-processes-and-procedures/employment-authorization-document
- USCIS Change My Nonimmigrant Status: https://www.uscis.gov/visit-the-united-states/change-my-nonimmigrant-status
- USCIS I-9 Central: https://www.uscis.gov/i-9-central

## 下一步

- 建立移民状态连续性变量表：身份类别、有效期、续期窗口、工作授权、派生资格、等待状态、文件恢复和服务资格接口。
- 整理 USCIS、DHS、State Department visa、I-9/E-Verify 和 OECD / IOM migration governance Source Cards。
- 与 `passport-travel-document-mobility-continuity/` 明确分工：护照域研究跨境移动证件，本域研究在地居留和工作授权。
