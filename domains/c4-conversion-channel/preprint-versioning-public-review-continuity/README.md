# Preprint Versioning Public Review Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/preprint-versioning-public-review-continuity` |
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

`preprint-versioning-public-review-continuity/` 研究预印本、版本链、公开评论、后续期刊版本和公共审查如何影响早期技术信号进入 Human Infra。

> 核心问题：预印本能加速知识扩散，也能把未审查、后续大改或被撤回的结论提前推入模型与传播材料。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要尽早识别未来技术窗口
  -> 很多前沿信号先以预印本、公开评论和社区审查出现
  -> 预印本状态、版本差异和后续发表状态决定信号可用等级
  -> 因此预印本版本与公开评审连续性是早期证据接入门槛
```

## 关注对象

- Preprint、version history、withdrawal、journal version、public review、commentary、post-publication peer review 和 overlay review。
- medRxiv、bioRxiv、arXiv、OSF Preprints、PubPeer、PREreview、eLife reviewed preprints 等信号类型。
- 与 `technology-foresight-horizon-scanning/` 的边界：技术预见域发现弱信号；本域判断预印本弱信号的审查状态和版本稳定性。
- 与 `trustworthy-scientific-communication-peer-review/` 的边界：可信传播域是总入口；本域聚焦预印本生命周期。

## Human Infra 模型链路

```text
预印本版本与公开评审 T
  -> 改变 review_status、version_delta、public_comment_signal、journal_linkage 变量 X
  -> 改变早期证据在 Source Card、雷达和模型中的等级 S
  -> 改变过早采用、错误传播、错过早期窗口和版本漂移风险 λ(t)
  -> 影响技术预见、研究组合和主体持续性路径选择
```

## 非目标

- 不提供论文代写、预印本刷评、评论操控、同行评审伪造、抢发策略或平台规避。
- 不把预印本写成已验证临床结论，也不因未同行评审而自动排除。
- 不抓取非公开审稿材料或平台后台数据。

## Source Signals

- ASAPbio preprint resources: https://asapbio.org/preprints
- medRxiv policies: https://www.medrxiv.org/content/about-medrxiv
- bioRxiv about: https://www.biorxiv.org/about-biorxiv
- PubPeer: https://pubpeer.com/
- PREreview: https://prereview.org/

## 下一步

- 给 Source Card 增加 `preprint_server`、`version_number`、`public_review_status`、`journal_version_link` 和 `version_delta_note` 字段。
- 在技术雷达中区分 “preprint signal” 与 “peer-reviewed evidence”。
