# Messaging Contact Graph Portability Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/messaging-contact-graph-portability-continuity` |
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


`messaging-contact-graph-portability-continuity` 研究即时通信账号、联系人图谱、群组、聊天历史、通讯录、端到端加密、导出迁移和平台互操作如何影响主体关系、协作和求助连续。

> 核心问题：联系人图谱是社会支持、工作协作、家庭照护和危机求助的实际基础设施；它一旦被锁定、封禁或丢失，主体会失去大量可行动关系。

## 关注对象

- Messaging account、contact list、address book、groups、channels、chat history、media archive 和 notification routing。
- End-to-end encryption、device linking、backup keys、data export、interoperability、identity handles 和 cross-platform migration。
- 账号停权、设备丢失、号码更换、联系人丢失、群组断裂、加密备份失败、骚扰封锁和跨平台迁移。
- 社会支持、照护 coordination、工作协作、社区动员、危机求助和数字安全边界。

## Human Infra 链路

```text
消息与联系人图谱可携带连续
  -> 联系人、群组、聊天历史和通知通道保持可恢复可迁移
  -> 账号停权、设备丢失、平台锁定或号码变化导致的关系断裂下降
  -> 协作、照护、求助、职业网络和社会支持保持可行动
  -> 主体关系资本、恢复能力和未来选择权增强
```

## 非目标

- 不提供个人聊天记录恢复、加密绕过、账号申诉、联系人抓取、骚扰、监控、定位、群组渗透或平台迁移操作建议。
- 不替代消息平台、组织 IT、安全团队、律师、危机服务、执法或官方支持渠道。
- 不收集或处理聊天内容、联系人、群组名单、电话号码、账号 ID、加密密钥、备份文件、定位或社交图谱。

## Source Signals

- Data Transfer Initiative / Data Transfer Project portability materials: https://dtinit.org/
- Digital Markets Act and interoperability materials where relevant: https://digital-markets-act.ec.europa.eu/
- CISA consumer account security resources: https://www.cisa.gov/secure-our-world
- Major messaging platform public export, backup and interoperability documentation as implementation examples.

## 下一步

- 建立 `contact graph -> message channel -> backup/export -> interoperability -> social continuity` 变量表。
- 区分通信内容、联系人图谱、群组治理、通知可达和平台身份这些不同资产。
- 与 `social-connection-relational-infra`、`phone-number-sim-portability-account-security-continuity`、`platform-account-suspension-appeals-continuity` 和 `online-safety-digital-harm-prevention` 建立边界。
