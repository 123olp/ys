# Platform Account Suspension Appeals Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/platform-account-suspension-appeals-continuity` |
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

`platform-account-suspension-appeals-continuity` 研究平台账号停权、内容移除、申诉、透明度报告、身份验证、创作者/商家收入和服务依赖如何影响主体在平台化社会中的行动连续。

> 核心问题：平台账号可能承载收入、客户、学习、社交、作品、身份和社区入口；停权和申诉失败会把私人规则变成主体行动边界。

## 关注对象

- Account suspension、content removal、strike systems、appeals、notice、reason statements、transparency reports 和 human review。
- Creator income、merchant account、marketplace access、app store access、education platform access、community moderation 和 identity verification。
- 错误停权、重复处罚、申诉无门、平台迁移成本、数据导出失败、收入冻结、声誉损害和群体歧视。
- 与言论权利、消费者保护、劳动收入、创作资产、商业连续和数字身份的关系。

## Human Infra 链路

```text
平台账号停权与申诉连续
  -> 平台准入、通知、理由、申诉、数据导出和替代路径可审查
  -> 错误停权、收入冻结、社交断裂和作品消失导致的行动损失下降
  -> 创作、商业、学习、社交和社区参与保持可恢复
  -> 主体平台依赖风险下降，未来选择权增强
```

## 非目标

- 不提供个人账号申诉文案、规避封禁、批量开号、平台规则绕过、虚假身份、内容操纵、刷量、骚扰或法律策略建议。
- 不替代平台支持、监管机构、消费者保护机构、律师、工会/创作者组织、商家服务或官方申诉渠道。
- 不收集或处理账号 ID、封禁通知、申诉材料、收入数据、身份文件、聊天记录、内容证据、客户资料或平台后台截图。

## Source Signals

- EU Digital Services Act platform notice, action and appeal framework: https://digital-strategy.ec.europa.eu/
- FTC consumer protection and online platform guidance: https://www.ftc.gov/
- OECD digital platform governance and transparency materials: https://www.oecd.org/
- Major platform public transparency, appeals and data export documentation as implementation examples.

## 下一步

- 建立 `platform account -> moderation action -> appeal/review -> export/exit -> continuity` 变量表。
- 区分内容账号、创作者账号、商家账号、学习账号、开发者账号和社区管理员账号。
- 与 `online-safety-digital-harm-prevention`、`contract-subscription-billing-consent-continuity`、`employment-algorithmic-hiring-screening-continuity` 和 `messaging-contact-graph-portability-continuity` 建立边界。
