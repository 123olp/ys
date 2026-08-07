# 历史年表数据来源获取计划

本文档回答“继续深度补齐年表，数据从哪里获取”。它只做来源分析与采集优先级设计，
不替代来源卡、本地复核和独立审阅。

## 1. 获取目标

年表需要四类数据：

1. **事件本体**：何时、何地、谁、做了什么、结果如何。
2. **来源证据**：论文、档案、机构公告、新闻、临床试验注册号。
3. **时期与实体关系**：人物、组织、地点、时期、技术路线之间的关系。
4. **失败与边界**：监管警告、撤销、复现失败、伦理争议和无效宣称。

因此数据来源不是只找论文，而是按“学术、临床监管、产业组织、历史档案、社区雷达”
五个层获取，再统一进入年表来源卡。

## 2. 分层来源矩阵

| 层 | 用途 | 首选来源 | 获取方式 | 对年表的价值 |
| --- | --- | --- | --- | --- |
| 学术文献 | 论文、综述、预印本、方法标准 | PubMed/E-utilities、Europe PMC REST、OpenAlex、Crossref、Semantic Scholar、arXiv、NBER、SSRN | API + DOI/PMID 核验 | 技术事件、科学思想、失败复现、证据边界 |
| 临床与监管 | 人体试验、审批、警告、撤市 | ClinicalTrials.gov API v2、WHO ICTRP、FDA、EMA、NIH RePORTER、ARPA-H | 官方 API/公告 | 人体阶段、监管节点、政策与失败教训 |
| 组织与产业 | 实验室、公司、基金会、竞赛、产业资金 | LEV、XPRIZE Healthspan、AFAR/TAME、SENS、Hevolution、Altos、Retro、NewLimit、Turn Bio、Life Biosciences、Loyal、Blueprint | 官网、新闻稿、RSS、GitHub | 全球主流路线、产业节点、资本与组织事件 |
| 历史与档案 | 神话、文本、手稿、时期、文化脉络 | Internet Archive、Project Gutenberg、Perseus、Chinese Text Project、BHL、HathiTrust、PeriodO、Wikidata SPARQL、Zotero/Tropy | 开放档案、OCR、SPARQL、书目 | 古代事件、思想史、原始文献、时期映射 |
| 社区与雷达 | 持续新事件、人物动态、快讯、交叉验证 | Reddit r/longevity、Hacker News、X 列表、Telegram 频道、RSSHub、专业媒体 RSS | 现有 `human_infra_radar` 采集器 | 新发现、早期信号、产业动态、反证线索 |

## 3. 按下一轮补录队列映射

### 全球主流长寿路线

- LEV Foundation Robust Mouse Rejuvenation：官网研究更新页。
- XPRIZE Healthspan：XPRIZE 官网与竞赛规则。
- TAME 试验：AFAR 官方试验页、ClinicalTrials.gov。
- Life Biosciences ER-100：FDA IND、公司新闻稿、ClinicalTrials.gov。
- OpenAI/Retro 因子设计：OpenAI/Retro 官方发布、arXiv/期刊。
- DunedinPACE 等时钟：PubMed、期刊补充材料。
- Loyal 犬类临床捷径：FDA 兽医产品路径、公司公告。
- Hevolution/ARPA-H PROSPR：机构官网、NIH RePORTER、新闻稿。

### 数字与认知路径

- Nectome/脑保存：BPF、公司官网、期刊。
- 连接组与神经形态：OpenAlex/PubMed、会议论文。
- 数字孪生：JMIR、Frontiers、综述引用网络。
- griefbots/数字复活：媒体专题、伦理期刊、公司公告。
- BCI 伦理与身份：PubMed、ClinicalTrials.gov、SEP/IEP。

### 暂停与重建

- 玻璃化冷冻：Cryobiology、器官保存期刊、组织官网。
- 器官灌注：PubMed、欧洲 PMC。
- BrainEx 后续：Nature 系列、期刊引用追踪。
- 生物打印：期刊综述、公司新闻稿。
- 最小充分身体：项目内部研究域、工程期刊、FDA/EMA 监管。

### 思想与治理

- 长寿逃逸速度谱系：SENS、Ending Aging、原始书籍与访谈档案。
- 有效永生飞轮：项目内部论文、引用图谱。
- AI 安全与长寿治理：arXiv、NIST AI RMF、OECD、WHO。
- 健康老龄化政策：WHO、UN DESA、国家老龄化政策数据库。

## 4. 获取链路

```text
来源发现（雷达/RSS/API/人工）
  -> 元数据采集（标题、作者、日期、URL、DOI/PMID）
  -> 来源可达性核验（官方页面、DOI、PMC、Internet Archive）
  -> 事件事实抽取（时间、主体、结果、边界）
  -> 来源卡写入 sources.json
  -> 事件写入 timeline.json
  -> make history-timeline-preview
  -> make history-timeline-gate
  -> 本地复核 -> 独立审阅 -> published
```

## 5. 优先复用现有能力

- `tools/fetch_effective_immortality_kb.py`：已覆盖 PubMed、Europe PMC 的批量检索。
- `human_infra_radar`：已实现 RSS、HTML、PubMed、ClinicalTrials、Reddit、Telegram、
  X、GitHub、Hacker News 等采集器，可作为持续新事件入口。
- `TOOLS.md`：已推荐 Zotero、Tropy、OpenRefine、PeriodO、Wikidata、TimelineJS。

不要在 Human Infra 重复造雷达；雷达负责持续采集，年表负责结构化证据治理。

## 6. 隐私与治理边界

- 真实社交来源清单只存在于私有 `human_infra_radar/private/`，不得写入公开仓库。
- 年表只登记可公开核验的来源；私有社群动态不得直接进入来源卡。
- 来自公司新闻稿、媒体和预印本的内容必须标注证据等级与“尚未独立复核”。
- 对神话、文学和思想事件，使用 `M/I`，不写成史实。
- 对动物实验和细胞实验，使用 `T`，不写成人体有效结论。

## 7. 首批执行顺序

1. 用 PubMed/Europe PMC 补齐 12 个“下一轮补录队列”中已有论文锚点的来源卡。
2. 用 ClinicalTrials.gov API 补齐人体试验事件：TAME、ER-100、Neuralink 后续、异种移植。
3. 用机构官网和新闻稿补齐产业事件：LEV、XPRIZE、Hevolution、ARPA-H、NewLimit、Loyal。
4. 用 Internet Archive/原始文本补齐思想史与失败教训的原始文献。
5. 每一批完成后只做 draft 事件，不自动进入 public 正文。
