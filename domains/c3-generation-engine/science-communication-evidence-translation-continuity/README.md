# Science Communication Evidence Translation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/science-communication-evidence-translation-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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

- 界定被放大的通用能力资源：智力、注意力、记忆、学习、判断、执行、反馈或工具使用。
- 说明任务链路：能力变化如何改变问题求解、行动质量、创造密度或学习轮次。
- 识别复利结构：能力增强、工具采用、协作网络、经验积累和自我升级如何互相强化。
- 记录依赖条件：AI、数据、界面、训练、外部工具、社会支持或反馈系统。
- 列出误用、过载、依赖、幻觉、注意力破坏、人格边界和安全风险。

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

`science-communication-evidence-translation-continuity/` 研究科学传播、风险沟通、公众理解、媒体转译和证据翻译如何影响 Human Infra 的社会理解与技术采用。

> 核心问题：证据最终会进入公众语言、社群传播、政策叙事和个人行动；如果传播把假说写成事实，把不确定性写成承诺，主体持续性会被错误叙事牵引。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要把复杂证据转化为可理解、可审查、可行动的公共语言
  -> 科学传播会改变公众信任、技术采用、风险感知和资源配置
  -> 夸大、恐慌、过度简化和确定性错配会扭曲行动
  -> 因此科学传播与证据转译连续性是 Human Infra 的公共理解门槛
```

## 关注对象

- Science communication、risk communication、knowledge translation、public understanding、press release、media framing、uncertainty communication 和 health/science literacy。
- 从论文到新闻稿、社交平台、政策简报、社区材料、README、Web 页面和推文的转译链。
- 与 `media-information-literacy-public-library/` 的边界：媒体素养域关注受众能力和公共学习基础设施；本域关注科学证据如何被转译和传播。
- 与 `trustworthy-scientific-communication-peer-review/` 的边界：可信科研传播域关注科研出版状态；本域关注面向公众和跨界行动者的表达。

## Human Infra 模型链路

```text
科学传播与证据转译 T
  -> 改变 uncertainty_framing、risk_communication、claim_scope、public_understanding 变量 X
  -> 改变公众信任、技术采用、政策叙事和项目传播状态 S
  -> 改变炒作、恐慌、误解、过度承诺和错误行动风险 λ(t)
  -> 影响 Human Infra 的社会合法性、传播效率和主体持续性路径选择
```

## 非目标

- 不提供宣传操控、恐慌传播、微定向说服、伪科学包装、疗效承诺、投资宣传或政策游说。
- 不把复杂证据压缩成确定性口号。
- 不输出个体医疗、法律、投资、保险或政策行动建议。

## Source Signals

- National Academies, Communicating Science Effectively: https://nap.nationalacademies.org/catalog/23674/communicating-science-effectively-a-research-agenda
- WHO risk communication resources: https://www.who.int/teams/risk-communication
- NIH Clear Communication: https://www.nih.gov/institutes-nih/nih-office-director/office-communications-public-liaison/clear-communication
- CDC Clear Communication Index: https://www.cdc.gov/ccindex/
- National Academies, Science Literacy: https://nap.nationalacademies.org/catalog/23595/science-literacy-concepts-contexts-and-consequences

## 下一步

- 给传播材料增加 `claim_scope`、`uncertainty_statement`、`audience_level`、`action_boundary` 和 `hype_risk` 字段。
- 与 README、Web 论文页、推文模板和 Source Card 建立同一传播边界。
