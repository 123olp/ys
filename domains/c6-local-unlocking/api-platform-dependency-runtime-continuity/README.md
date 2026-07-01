# API Platform Dependency Runtime Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/api-platform-dependency-runtime-continuity` |
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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

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

`api-platform-dependency-runtime-continuity` 研究第三方 API、平台 SDK、支付/地图/身份/消息/AI 服务、限流、计费、版本废弃、服务等级、变更公告和运行时降级如何影响主体和组织的工具链是否能继续执行任务。

> 核心问题：现代软件常把关键能力外包给平台 API；API 中断、废弃或政策变化会直接变成主体任务中断。

## 关注对象

- 支付、地图、身份、消息、搜索、AI、云函数、存储、数据源、通知、分析和自动化平台 API。
- SLA、速率限制、配额、计费、版本废弃、breaking changes、SDK 生命周期、状态页、降级和替代路径。
- API 依赖图、超时、重试、缓存、幂等、背压、断路器、模拟环境和退出方案。
- 服务中断、价格变化、条款变化、账号封禁、接口废弃、供应商故障和隐性集中化风险。

## Human Infra 链路

```text
API 与平台运行时依赖连续
  -> 外部能力调用、降级和替代路径可审查
  -> 第三方 API 中断、废弃、限流和政策变化造成的任务失败下降
  -> 主体和组织工具链保持可运行、可恢复、可迁移
  -> 数字生产力和长期项目连续性增强
```

## 非目标

- 不提供绕过 API 限制、规避计费、滥用接口、批量抓取、账号规避、破解 SDK 或平台漏洞利用方法。
- 不替代平台工程、SRE、法律、采购、合规或供应商管理。
- 不收集 API key、token、账单、私有流量、客户数据、错误日志或平台合同。

## Source Signals

- NIST cloud and software resilience references: https://www.nist.gov/
- CNCF / SRE public guidance for resilience patterns as implementation references.
- Major platform API status, deprecation and changelog documentation as observable signals.
- EU Data Act and platform interoperability discussions as governance references.

## 下一步

- 建立 `api dependency -> quota -> version -> fallback -> runtime continuity` 变量表。
- 区分个人自动化、创业项目、公共服务、医疗/金融关键工具和 AI 平台依赖。
- 与 `cloud-service-exit-interoperability-continuity`、`software-supply-chain-dependency-provenance-continuity`、`compute-data-center-ai-infrastructure` 和 `model-cards-ai-audit-documentation` 建立边界。
