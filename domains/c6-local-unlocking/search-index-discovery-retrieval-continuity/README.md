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
