# Search Index Discovery Retrieval Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/search-index-discovery-retrieval-continuity` |
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

`search-index-discovery-retrieval-continuity` 研究搜索、索引、目录、元数据、站内检索、公共发现、个人检索和链接可达性如何影响主体是否能在需要时找到知识、记录、服务和历史上下文。

> 核心问题：资料存在不等于资料可用；找不到、搜不准、链接坏掉或索引不可迁移，都会让记忆、权利和协作变成沉没成本。

## 关注对象

- 搜索引擎、站内搜索、全文索引、元数据、schema、sitemap、目录、标签、收藏、书签和知识库检索。
- 个人文件检索、组织知识库、公共服务目录、研究资料、网页可发现性和断链修复。
- 查询质量、排序偏差、重复结果、链接腐烂、索引延迟、权限错配和检索隐私。
- 语义搜索、向量检索、知识图谱、RAG、可解释来源和检索结果审计。

## Human Infra 链路

```text
搜索、索引与发现连续
  -> 资料、服务、记录和知识上下文可被描述、索引、查询和验证来源
  -> 找不到、搜不准、链接腐烂、权限错配和来源不明下降
  -> 主体更能恢复上下文、完成任务、纠错和复用历史经验
  -> 外部记忆、学习效率和组织协作连续性增强
```

## 非目标

- 不提供搜索排名操纵、垃圾 SEO、爬虫规避、隐私绕过、数据抓取滥用或模型提示注入方案。
- 不替代版权、隐私、数据治理、公共记录、档案或平台内容政策。
- 不收集私人搜索记录、浏览历史、账号资料、内部索引、敏感文档或未授权内容。

## Source Signals

- Sitemaps protocol: https://www.sitemaps.org/
- Schema.org vocabulary: https://schema.org/
- W3C Data on the Web Best Practices: https://www.w3.org/TR/dwbp/
- Library of Congress digital preservation references: https://www.loc.gov/preservation/

## 下一步

- 建立 `resource -> metadata -> index -> query -> ranked result -> source verification -> reuse` 变量表。
- 区分个人检索、组织知识库、公共服务发现、科研资料检索、网页发现和 AI/RAG 检索。
- 与 `personal-knowledge-management-cognitive-offloading`、`media-information-literacy-public-libraries`、`knowledge-graphs-semantic-interoperability` 和 `document-capture-ocr-pdf-record-workflow-continuity` 建立边界。
