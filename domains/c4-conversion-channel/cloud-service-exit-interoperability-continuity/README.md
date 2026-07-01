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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

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
