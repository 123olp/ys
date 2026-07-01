# Open Source Maintainer Sustainability Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/open-source-maintainer-sustainability-continuity` |
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

`open-source-maintainer-sustainability-continuity` 研究开源维护者时间、资金、安全支持、治理、交接、项目健康、依赖关键性和社区负载如何影响主体依赖的软件生态能否持续修复、更新和可信演化。

> 核心问题：开源不是免费自然资源；大量关键服务依赖少数维护者的持续劳动和治理能力。

## 关注对象

- Maintainer time、funding、burnout、安全响应、release cadence、bus factor、governance、贡献者入口和交接机制。
- OpenSSF、Alpha-Omega、criticality score、项目健康、依赖图、漏洞响应和安全审计资源。
- 商业使用、公共资金、基金会治理、赞助、责任分配和维护者风险。
- 维护中断、项目废弃、恶意接管、维护者疲劳、治理失效和关键依赖无人负责。

## Human Infra 链路

```text
开源维护者可持续
  -> 关键依赖持续获得修复、审计、发布和治理
  -> 软件工具、公共服务和数字基础设施断裂风险下降
  -> 主体依赖的学习、工作、医疗、金融和协作系统更稳定
  -> 数字行动底座和社会技术系统韧性增强
```

## 非目标

- 不提供项目接管、账号滥用、社工维护者、供应链攻击、漏洞披露滥用或骚扰组织方式。
- 不替代基金会治理、开源项目决策、资助策略、法律建议或安全响应。
- 不收集维护者私人信息、财务细节、未公开安全报告、项目内部冲突或私有仓库资料。

## Source Signals

- OpenSSF resources, Scorecard, Alpha-Omega and Securing Critical Projects: https://openssf.org/
- CISA Open Source Software Security Roadmap: https://www.cisa.gov/
- GitHub / Linux Foundation open source ecosystem reports as ecosystem evidence.
- SLSA and Sigstore as downstream trust tooling references.

## 下一步

- 建立 `maintainer capacity -> project health -> dependency continuity -> subject continuity` 变量表。
- 区分项目健康、安全响应、资金可持续、治理交接和关键依赖集中风险。
- 与 `software-supply-chain-dependency-provenance-continuity`、`research-infrastructure-open-science-translation`、`public-procurement-contracting-capacity` 和 `technology-foresight-horizon-scanning` 建立边界。
