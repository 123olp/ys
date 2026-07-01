# 数据源规划

Longevity Evidence 优先接入公开、可追溯、稳定维护的数据源。第一阶段不追求全量覆盖，先保证每条数据能回到原始来源。

## 核心结论

MVP 必须持续维护 6 类数据：

1. 文献证据：论文、综述、研究类型、样本量、物种和结论。
2. 临床试验：NCT ID、状态、阶段、干预、终点、结果和更新时间。
3. 干预词表：药物、补剂、生活方式、检测、疗法及其同义词。
4. 衰老知识库：衰老基因、长寿关联、动物寿命实验和干预条目。
5. 药品安全：标签、适应症、警告、不良反应、召回和监管状态。
6. 人群基线：流行病学指标、体检指标、营养、生活方式和死亡风险关联。

## 第一优先级：MVP 必接

| 数据源 | 维护对象 | 用途 | 接入方式 | 建议频率 |
| --- | --- | --- | --- | --- |
| PubMed / NCBI E-utilities | PMID、标题、摘要、期刊、年份、研究类型、MeSH | 生物医学文献主索引 | API 查询 | 每周增量 |
| OpenAlex Works | DOI、引用、开放获取、机构、作者、主题、相关论文 | 文献补充索引和引用网络 | API 查询 | 每周增量 |
| ClinicalTrials.gov | NCT ID、状态、阶段、干预、条件、终点、结果、更新时间 | 临床试验事实源 | API 查询 | 每个工作日或每周 |
| HAGR / GenAge / LongevityMap / DrugAge | 衰老基因、长寿关联、动物寿命干预 | 长寿垂直基础库 | 下载快照 | 每月检查 |
| openFDA Drug Label / Drug Event / Drugs@FDA | 标签、适应症、禁忌、不良反应、批准信息 | 药物安全和监管边界 | API / 下载 | 每周 |

## 第二优先级：证据增强

| 数据源 | 维护对象 | 用途 | 接入方式 | 建议频率 |
| --- | --- | --- | --- | --- |
| Open Targets | target、disease、drug、target-disease association | 靶点、疾病和药物关系图谱 | GraphQL / 下载 | 每月 |
| GWAS Catalog | trait、variant、gene、association、study、ancestry | 性状和遗传关联证据 | REST API / 下载 | 每月 |
| NHANES | 体检、实验室、营养、生活方式、问卷、死亡链接数据 | 人群基线和风险指标 | 数据文件 | 每季度或版本更新 |
| PubChem | 化合物、同义词、结构、CID | 药物和补剂实体归一化 | API | 按需 |
| Crossref | DOI、出版物元数据 | DOI 兜底和出版元数据校验 | API | 按需 |

## 第三优先级：后续商业情报

| 数据源 | 维护对象 | 用途 | 接入方式 | 建议频率 |
| --- | --- | --- | --- | --- |
| SEC EDGAR | 公司年报、风险披露、研发项目 | 长寿公司情报 | API / 下载 | 每周 |
| PatentsView / Google Patents | 专利、申请人、主题 | 靶点、药物和公司早期信号 | API / 搜索 | 每月 |
| NIH RePORTER | 资助项目、PI、机构、主题 | 科研资金流向 | API | 每月 |

## Longevity Evidence 自有维护表

外部数据不能直接变成产品结论，必须沉淀为内部维护表：

| 表 | 说明 | 维护方式 |
| --- | --- | --- |
| `interventions` | 干预主表：规范名、类别、别名、外部 ID | 人工审核 + 半自动补全 |
| `claims` | 明确主张：某干预对某人群和结果是否有效 | 人工维护 |
| `evidence_items` | 证据条目：论文、试验、数据库记录 | 自动导入 + 人工标注 |
| `trials` | 临床试验标准化表 | 自动导入 |
| `safety_signals` | 风险、禁忌、不良反应和标签警告 | 自动导入 + 人工摘要 |
| `effect_metrics` | 效果大小：HR、RR、OR、均值差、寿命变化、指标变化 | 人工抽取为主 |
| `source_snapshots` | 原始响应、下载快照、抓取时间和校验 hash | 自动维护 |
| `source_runs` | 每次采集任务的状态、耗时、失败原因和数据量 | 自动维护 |

## 数据更新策略

- 临床试验和药品安全属于高变动源，必须做增量刷新和更新时间比对。
- 文献源每周刷新即可，MVP 阶段不做全量 PubMed 镜像。
- HAGR、GWAS、Open Targets、NHANES 更适合版本化快照，不适合频繁 API 拉取。
- 所有原始响应先进入本子域的 `data/raw/`，清洗结果进入本子域的 `data/processed/`，人工结论进入独立表。
- 每个源必须记录 `source_name`、`source_url`、`source_record_id`、`retrieved_at`、`license_note` 和 `raw_hash`。

## 接入规则

- 每条外部数据必须保存来源 URL、访问日期和原始标识符。
- 论文类数据优先保存 DOI、PMID、标题、年份、研究类型和人群。
- 临床试验类数据优先保存 NCT ID、状态、阶段、干预、终点和结果链接。
- 药品类数据必须保存药品同义词、活性成分、标签更新时间和安全章节来源。
- 人工结论必须和原始数据分离，避免把编辑判断写进原始数据层。
- 对用户展示的结论必须保留证据等级、适用对象和不确定性。

## 官方参考入口

- NCBI APIs: https://www.ncbi.nlm.nih.gov/home/develop/api/
- OpenAlex API: https://docs.openalex.org/how-to-use-the-api/api-overview
- ClinicalTrials.gov API: https://clinicaltrials.gov/data-api/api
- HAGR downloads: https://genomics.senescence.info/download.html
- openFDA Drug APIs: https://open.fda.gov/apis/drug/
- Open Targets GraphQL: https://platform-docs.opentargets.org/data-access/graphql-api
- GWAS Catalog REST API: https://www.ebi.ac.uk/gwas/rest/api/v2/docs
- NHANES: https://www.cdc.gov/nchs/nhanes/about/index.html
