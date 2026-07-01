# Cloud Service Exit Interoperability Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/cloud-service-exit-interoperability-continuity` |
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


`cloud-service-exit-interoperability-continuity` 研究云服务、SaaS、对象存储、协作文档、数据库、身份服务和托管平台的导出、迁移、互操作、退出、合同终止和供应商锁定如何影响主体资料、工作流和组织行动能否继续。

> 核心问题：云服务让主体获得强工具，也把资料、流程和身份绑定到供应商；不能退出的服务会把未来选择权变成许可条件。

## 关注对象

- SaaS、云存储、数据库、协作文档、身份目录、邮件托管、项目管理、低代码平台和托管开发环境。
- 数据导出、格式、API、迁移工具、互操作、合同终止、服务降级、价格变化、区域限制和供应商停止服务。
- 云退出计划、备份、恢复演练、多云/本地替代、访问控制迁移和审计日志保留。
- 供应商锁定、不可导出元数据、工作流断裂、账号停权、服务下线和监管跨境限制。

## Human Infra 链路

```text
云服务退出与互操作连续
  -> 数据、身份、工作流和审计证据可导出可迁移
  -> 供应商停服、涨价、封禁、锁定和格式孤岛造成的行动中断下降
  -> 主体和组织保留迁移、恢复和重新组合工具的能力
  -> 未来选择权和长期数字资产控制力增强
```

## 非目标

- 不提供绕过服务条款、批量抓取、规避封禁、破解 DRM、逃避计费、云入侵或迁移私有数据的操作步骤。
- 不替代云架构、法律、采购、合规、隐私影响评估或数据迁移专业服务。
- 不收集账号、API token、账单、私有数据、合同条款、审计日志或受监管数据。

## Source Signals

- EU Data Act cloud switching and data portability provisions: https://digital-strategy.ec.europa.eu/
- Data Transfer Initiative and Data Transfer Project resources: https://dtinit.org/
- NIST cloud computing and portability/interoperability references: https://www.nist.gov/
- Major cloud provider public export and exit guidance as implementation examples.

## 下一步

- 建立 `cloud service -> export -> interoperability -> exit -> continuity` 变量表。
- 区分个人云资料、组织 SaaS、关键数据库、身份服务和开发平台的退出风险。
- 与 `cloud-backup-file-sync-data-portability-continuity`、`contract-subscription-billing-consent-continuity`、`platform-account-suspension-appeals-continuity` 和 `api-platform-dependency-runtime-continuity` 建立边界。
