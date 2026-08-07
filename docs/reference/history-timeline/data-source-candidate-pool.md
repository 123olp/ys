# 数据源候选池

本文档是“从哪里抓数据”的候选池，只登记候选入口与抓取可行性，不替代来源卡。
所有候选进入 `sources.json` 前，必须完成可达性、条款、证据等级和用途边界复核。

## 使用方式

按类别挑选候选，优先抓取 `P0` 项；抓取后先进入候选队列，再做来源卡。

| 状态 | 含义 |
| --- | --- |
| ready | 链接或 API 已知，可进入采集实验 |
| verify | 需要先验证 URL、API 版本或开放程度 |
| gate_review | 内容可用但需要许可、版权或证据等级审查 |
| privacy_review | 涉及社交、私人社区或敏感信息，必须走私有雷达 |

## 一、学术与文献

| 候选源 | 访问入口 | 内容类型 | 优先级 | 状态 |
| --- | --- | --- | --- | --- |
| PubMed | https://pubmed.ncbi.nlm.nih.gov/ | 文献元数据、摘要、PMID | P0 | ready |
| PubMed E-utilities | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/ | 检索、摘要、全文链接 | P0 | ready |
| PubMed Central | https://pmc.ncbi.nlm.nih.gov/ | 开放全文 | P0 | ready |
| Europe PMC REST | https://www.ebi.ac.uk/europepmc/webservices/rest | 元数据、开放全文、PMCID | P0 | ready |
| OpenAlex | https://api.openalex.org/ | 文献、作者、机构、引用网络 | P0 | ready |
| Crossref REST | https://api.crossref.org/works | DOI、期刊、出版日期 | P0 | ready |
| Semantic Scholar | https://api.semanticscholar.org/graph/v1/paper/search | 引用、摘要、开放 PDF | P1 | verify |
| arXiv | http://export.arxiv.org/api/query | 预印本元数据与 PDF | P1 | ready |
| bioRxiv | https://www.biorxiv.org/ | 生物预印本 | P1 | ready |
| medRxiv | https://www.medrxiv.org/ | 医学预印本 | P1 | ready |
| SSRN | https://www.ssrn.com/ | 工作论文元数据 | P2 | gate_review |
| NBER | https://www.nber.org/papers | 经济学工作论文 | P2 | gate_review |
| DOAJ | https://doaj.org/ | 开放获取期刊目录 | P2 | ready |
| CORE | https://core.ac.uk/ | 聚合开放全文 | P2 | verify |
| Zotero | https://www.zotero.org/ | 书目、引用、网页快照 | P0 | ready |
| Nature Aging | https://www.nature.com/nataging/ | 综述、研究、政策 | P0 | gate_review |
| Nature Medicine | https://www.nature.com/nm/ | 临床前沿 | P1 | gate_review |
| The Lancet Healthy Longevity | https://www.thelancet.com/journals/lanhlo | 健康寿命研究 | P1 | gate_review |
| Aging Cell | https://onlinelibrary.wiley.com/journal/14749726 | 衰老机制 | P1 | gate_review |
| GeroScience | https://link.springer.com/journal/11357 | 老年科学与干预 | P1 | gate_review |
| eLife | https://elifesciences.org/ | 开放研究、评审记录 | P1 | ready |
| Rejuvenation Research | https://www.liebertpub.com/loi/rej | 修复与重建 | P2 | gate_review |
| Frontiers in Aging | https://www.frontiersin.org/journals/aging | 开放获取 | P2 | ready |
| Aging Cell 等 Wiley 开放页 | https://onlinelibrary.wiley.com/ | 元数据与开放全文 | P2 | gate_review |
| Cochrane Library | https://www.cochranelibrary.com/ | 系统综述 | P1 | gate_review |
| Campbell Collaboration | https://www.campbellcollaboration.org/ | 社科系统综述 | P2 | verify |
| PMC Open Access Subset | https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/ | 开放全文批量下载 | P1 | ready |
| CORDIS | https://cordis.europa.eu/ | 欧盟项目与成果 | P2 | ready |
| NIH RePORTER | https://reporter.nih.gov/ | 美国 NIH 资助项目 | P1 | ready |
| NSF Award Search | https://www.nsf.gov/awardsearch/ | 美国科学基金项目 | P2 | ready |

## 二、临床与监管

| 候选源 | 访问入口 | 内容类型 | 优先级 | 状态 |
| --- | --- | --- | --- | --- |
| ClinicalTrials.gov API v2 | https://clinicaltrials.gov/api/v2/studies | 临床试验注册、状态、结果 | P0 | ready |
| WHO ICTRP | https://trialsearch.who.int/ | 全球试验注册聚合 | P1 | verify |
| EU Clinical Trials Register | https://www.clinicaltrialsregister.eu/ | 欧盟试验 | P1 | ready |
| ISRCTN | https://www.isrctn.com/ | 国际试验注册 | P2 | ready |
| Chinese Clinical Trial Registry | https://www.chictr.org.cn/ | 中国临床试验 | P1 | verify |
| UMIN Clinical Trials Registry | https://www.umin.ac.jp/ctr/ | 日本试验注册 | P2 | verify |
| jRCT | https://jrct.niph.go.jp/ | 日本正式试验注册 | P2 | verify |
| FDA Drug Approvals | https://www.fda.gov/drugs/development-approval-process-drugs/drug-approvals-and-databases | 批准、标签、警告 | P0 | ready |
| openFDA | https://open.fda.gov/ | 药物、设备、不良事件 API | P1 | ready |
| FDA Warning Letters | https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/compliance-actions-and-activities/warning-letters | 监管警告 | P1 | verify |
| FDA Consumer Updates | https://www.fda.gov/consumers/consumer-updates | 消费者风险公告 | P1 | ready |
| EMA Medicines | https://www.ema.europa.eu/en/medicines | 欧洲药品审批 | P1 | ready |
| MHRA | https://www.gov.uk/government/organisations/medicines-and-healthcare-products-regulatory-agency | 英国药品监管 | P2 | verify |
| PMDA | https://www.pmda.go.jp/english/ | 日本药品监管 | P2 | verify |
| ARPA-H | https://arpa-h.gov/ | 高风险健康项目 | P1 | ready |
| NIH Clinical Center | https://clinicalcenter.nih.gov/ | 临床试验信息 | P2 | ready |
| WHO | https://www.who.int/ | 健康老龄化、证据与政策 | P1 | ready |
| US Preventive Services Task Force | https://www.uspreventiveservicestaskforce.org/ | 预防建议 | P2 | ready |
| EQUATOR Network | https://www.equator-network.org/ | 报告规范 | P1 | ready |
| TRIPOD+AI | https://www.tripod-statement.org/ | AI 预测报告标准 | P1 | ready |

## 三、人口、统计与健康数据

| 候选源 | 访问入口 | 内容类型 | 优先级 | 状态 |
| --- | --- | --- | --- | --- |
| Human Mortality Database | https://www.mortality.org/ | 生命表、死亡率 | P0 | gate_review |
| Human Life-Table Database | https://www.lifetable.de/ | 生命表数据 | P1 | gate_review |
| GBD | https://www.healthdata.org/research-analysis/gbd | 疾病负担、寿命损失 | P1 | verify |
| IHME | https://vizhub.healthdata.org/gbd-results/ | 健康指标可视化与下载 | P1 | verify |
| UN World Population Prospects | https://population.un.org/wpp/ | 人口预测 | P1 | ready |
| Our World in Data | https://ourworldindata.org/ | 寿命、死亡、健康指标 CSV | P0 | ready |
| WHO Global Health Observatory | https://www.who.int/data/gho | 健康统计数据 | P1 | ready |
| CDC WONDER | https://wonder.cdc.gov/ | 美国死亡与疾病数据 | P1 | gate_review |
| NCHS | https://www.cdc.gov/nchs/ | 美国生命统计 | P2 | gate_review |
| Eurostat | https://ec.europa.eu/eurostat | 欧洲人口与健康数据 | P2 | ready |
| World Bank Open Data | https://data.worldbank.org/ | 发展指标 | P2 | ready |
| OECD Data | https://data.oecd.org/ | 健康与老龄化指标 | P2 | ready |
| National Vital Statistics System | https://www.cdc.gov/nchs/nvss/index.htm | 美国生命记录 | P2 | gate_review |
| Longevity Project 数据集 | 各期刊补充材料 | 长寿队列 | P1 | verify |
| NHANES | https://www.cdc.gov/nchs/nhanes/ | 美国营养健康调查 | P1 | gate_review |
| UK Biobank | https://www.ukbiobank.ac.uk/ | 生物样本与健康队列 | P2 | gate_review |

## 四、组织、产业与资金

| 候选源 | 访问入口 | 内容类型 | 优先级 | 状态 |
| --- | --- | --- | --- | --- |
| LEV Foundation | https://www.levf.org/ | Robust Mouse Rejuvenation 项目 | P0 | ready |
| XPRIZE Healthspan | https://www.xprize.org/competitions/healthspan | 竞赛规则、团队、里程碑 | P0 | ready |
| AFAR | https://www.afar.org/ | TAME、衰老研究基金 | P1 | ready |
| SENS Research Foundation | https://sens.org/ | 修复衰老、长寿逃逸速度 | P1 | ready |
| Hevolution Foundation | https://www.hevolution.com/ | 资金、路线、产业报告 | P1 | ready |
| Academy for Health and Lifespan Research | https://www.healthylongevity.academy/ | 学者、路线、奖项 | P2 | verify |
| National Institute on Aging | https://www.nia.nih.gov/ | 衰老研究、政策、资金 | P1 | ready |
| Buck Institute | https://www.buckinstitute.org/ | 衰老研究 | P2 | ready |
| Max Planck Institute for Biology of Ageing | https://www.age.mpg.de/ | 衰老机制研究 | P2 | ready |
| Jackson Laboratory | https://www.jax.org/ | 小鼠遗传与衰老模型 | P2 | ready |
| Mayo Clinic Aging Center | https://www.mayo.edu/research/centers-programs/robert-and-arlene-kogod-center-aging | 老年科学、senolytics | P2 | verify |
| Altos Labs | https://www.altoslabs.com/ | 细胞重编程 | P1 | ready |
| Calico | https://www.calicolabs.com/ | 衰老生物学 | P2 | verify |
| NewLimit | https://www.newlimit.com/ | 表观遗传重编程 | P1 | ready |
| Retro Biosciences | https://www.retrobio.com/ | 山中因子、AI 设计 | P1 | ready |
| Turn Bio | https://www.turn.bio/ | mRNA 重编程 | P1 | ready |
| Life Biosciences | https://www.lifebiosciences.com/ | OSK、ER-100 | P0 | ready |
| Loyal | https://www.loyal.com/ | 犬类长寿药物 | P1 | ready |
| Rejuvenate Bio | https://rejuvenatebio.com/ | 基因疗法抗衰 | P2 | ready |
| Cambrian Bio | https://cambrianbio.com/ | 抗衰药物组合 | P2 | verify |
| Fountain Life | https://fountainlife.com/ | 长寿诊断与医疗 | P2 | verify |
| TruDiagnostic | https://www.trudiagnostic.com/ | 表观遗传时钟 | P2 | verify |
| Elysium Health | https://www.elysiumhealth.com/ | NAD、补剂研究 | P2 | verify |
| Unity Biotechnology | https://www.unitybiotechnology.com/ | senolytics | P2 | verify |
| BioAge Labs | https://www.bioage.com/ | 衰老生物标志物 | P2 | verify |
| Gero | https://gero.ai/ | 衰老动力学 | P2 | ready |
| Deep Longevity | https://www.deeplongevity.com/ | AI 衰老时钟 | P2 | verify |
| Insilico Medicine | https://insilico.com/ | AI 药物发现 | P2 | ready |
| Longevity Fund / Longevity Vision Fund | https://longevity.vc/ | 产业投资 | P2 | ready |
| Longevity Science Foundation | https://longevity.foundation/ | 资助与信息 | P2 | verify |
| Project Blueprint | https://blueprint.bryanjohnson.com/ | 个人量化长寿 | P1 | ready |

## 五、媒体、新闻与社区

| 候选源 | 访问入口 | 内容类型 | 优先级 | 状态 |
| --- | --- | --- | --- | --- |
| Nature News | https://www.nature.com/news | 科研新闻 | P1 | gate_review |
| Science News | https://www.sciencenews.org/ | 科学新闻 | P2 | ready |
| MIT Technology Review | https://www.technologyreview.com/ | 技术与长寿报道 | P2 | gate_review |
| STAT News | https://www.statnews.com/ | 生物医药、监管 | P2 | gate_review |
| Endpoints News | https://endpts.com/ | 生物技术产业新闻 | P2 | gate_review |
| Longevity.Technology | https://longevity.technology/ | 长寿产业与科技 | P1 | verify |
| Fight Aging! | https://www.fightaging.org/ | 长寿研究新闻 | P1 | ready |
| Lifespan.io | https://www.lifespan.io/ | 长寿新闻、访谈、资助 | P1 | ready |
| LEAF | https://www.leafscience.org/ | 长寿研究媒体 | P2 | verify |
| H+ Magazine | https://hplusmagazine.com/ | 超人类主义 | P2 | verify |
| Future Timeline | https://www.futuretimeline.net/ | 未来预测时间线 | P2 | verify |
| Scientific American | https://www.scientificamerican.com/ | 衰老与永生报道 | P2 | gate_review |
| New Scientist | https://www.newscientist.com/ | 长寿科技报道 | P2 | gate_review |
| Wired | https://www.wired.com/ | 脑机接口、冷冻、永生 | P2 | gate_review |
| The Economist | https://www.economist.com/ | 老龄化、长寿经济 | P2 | gate_review |
| Reuters Health | https://www.reuters.com/health/ | 医疗新闻 | P2 | gate_review |
| Axios Future | https://www.axios.com/newsletters/axios-future | 未来趋势 | P2 | gate_review |
| Reddit r/longevity | https://www.reddit.com/r/longevity/ | 社区讨论、论文发现 | P1 | privacy_review |
| Reddit r/singularity | https://www.reddit.com/r/singularity/ | 奇点与 AI 讨论 | P2 | privacy_review |
| Hacker News | https://news.ycombinator.com/ | 科技与 AI 新闻 | P1 | ready |
| X 列表 | 私有雷达 | 关键人物动态 | P1 | privacy_review |
| Telegram 频道 | 私有雷达 | 长寿社群快讯 | P1 | privacy_review |
| RSSHub | https://docs.rsshub.app/ | 把无 RSS 网页转成 RSS | P1 | verify |
| YouTube 频道 | https://www.youtube.com/ | SENS、Lifespan.io、LifeXtenShow 访谈 | P2 | verify |
| Podcast RSS | Lifespan.io、Longevity Podcast 等 | 访谈转写线索 | P2 | verify |

## 六、历史档案、书籍与原始文献

| 候选源 | 访问入口 | 内容类型 | 优先级 | 状态 |
| --- | --- | --- | --- | --- |
| Internet Archive | https://archive.org/ | 书籍、网页快照、原始文本 | P0 | ready |
| Project Gutenberg | https://www.gutenberg.org/ | 公版书全文 | P0 | ready |
| HathiTrust | https://www.hathitrust.org/ | 数字图书馆、全文检索 | P1 | gate_review |
| Biodiversity Heritage Library | https://www.biodiversitylibrary.org/ | 自然科学历史文献 | P1 | ready |
| Gallica | https://gallica.bnf.fr/ | 法国国家图书馆 | P2 | verify |
| Europeana | https://www.europeana.eu/ | 欧洲文化遗产 | P2 | ready |
| Library of Congress | https://www.loc.gov/ | 美国历史档案 | P2 | ready |
| British Library | https://www.bl.uk/ | 英国历史文献 | P2 | gate_review |
| Wellcome Collection | https://wellcomecollection.org/ | 医学史与健康史 | P2 | ready |
| National Library of Medicine | https://www.nlm.nih.gov/ | 医学史、原始文献 | P1 | ready |
| Perseus Digital Library | https://www.perseus.tufts.edu/ | 希腊罗马原始文本 | P1 | ready |
| Chinese Text Project | https://ctext.org/ | 中国古典文本 | P0 | ready |
| Wikisource | https://zh.wikisource.org/ | 多语言原始文本 | P1 | ready |
| Wikiquote | https://zh.wikiquote.org/ | 引文与出处 | P2 | ready |
| Wikimedia Commons | https://commons.wikimedia.org/ | 图片、扫描、文件 | P2 | ready |
| Wikidata SPARQL | https://query.wikidata.org/sparql | 实体、人物、作品、时期 | P1 | ready |
| PeriodO | https://perio.do/ | 历史时期 gazetteer | P1 | ready |
| Recogito/Pelagios | https://recogito.pelagios.org/ | 地理与历史实体标注 | P2 | verify |
| 金字塔文译本 | Internet Archive/HathiTrust | 古埃及宗教文本 | P1 | gate_review |
| 吉尔伽美什史诗译本 | Internet Archive/Gutenberg | 两河文学 | P1 | ready |
| 荷马颂歌 | Perseus | 希腊神话母题 | P1 | ready |
| 奥义书译本 | Internet Archive/Gutenberg | 印度思想 | P1 | ready |
| 道德经 | Chinese Text Project | 道家原始文本 | P1 | ready |
| 庄子 | Chinese Text Project | 道家思想 | P1 | ready |
| 淮南子 | Chinese Text Project | 汉代神话与思想 | P1 | ready |
| 抱朴子 | Chinese Text Project | 炼丹与神仙思想 | P1 | ready |
| 史记 | Chinese Text Project | 徐福求药等史事 | P1 | ready |
| 柏拉图《斐多篇》 | Perseus/Gutenberg | 灵魂不朽 | P1 | ready |
| 亚里士多德《论灵魂》 | Perseus/Gutenberg | 灵魂与生命 | P1 | ready |
| 培根《生命与死亡史》 | 早期英文书库 | 近代延寿 | P1 | verify |
| 洛克《人类理解论》 | Project Gutenberg | 记忆同一性 | P1 | ready |
| 休谟《人性论》 | Project Gutenberg | 自我与知觉 | P1 | ready |
| 康德《纯粹理性批判》 | Project Gutenberg/Archive | 时间与自我 | P1 | ready |
| 斯威夫特《格列佛游记》 | Project Gutenberg | Struldbrugs | P1 | ready |
| 玛丽·雪莱《凡人不死者》 | Project Gutenberg/Archive | 永生反例文学 | P1 | verify |
| 王尔德《道林·格雷》 | Project Gutenberg | 青春与人格 | P1 | ready |
| 托尔斯泰《伊凡·伊里奇之死》 | Project Gutenberg | 死亡意识 | P2 | verify |
| 博尔赫斯《永生》 | 图书馆/出版社 | 记忆与永生反例 | P1 | gate_review |
| 恰佩克《马克洛普洛斯秘方》 | 图书馆/档案 | 长寿与意义 | P1 | verify |
| 埃廷格《永生的前景》 | Cryonics Archive | 冷冻运动 | P1 | ready |
| 莫拉维克《心智儿童》 | Internet Archive | 意识上传 | P1 | ready |
| 库兹韦尔《奇点临近》 | Internet Archive/出版社 | 奇点叙事 | P1 | gate_review |
| 德格雷《终结衰老》 | Internet Archive/出版社 | 修复衰老 | P1 | gate_review |
| 博斯特罗姆《超级智能》 | 出版社/图书馆 | AI 风险 | P2 | gate_review |
| 帕菲特《理与人》 | 出版社/图书馆 | 人格同一性 | P1 | gate_review |
| 克拉克与查默斯《延展心智》 | 期刊/开放 PDF | 认知外延 | P1 | ready |

## 七、标准、本体与基础设施

| 候选源 | 访问入口 | 内容类型 | 优先级 | 状态 |
| --- | --- | --- | --- | --- |
| PeriodO API | https://perio.do/api/ | 时期定义 | P1 | verify |
| Wikidata API/SPARQL | https://www.wikidata.org/wiki/Special:EntityData | 实体与关系 | P1 | ready |
| OpenAlex API | https://api.openalex.org/ | 文献与机构 | P0 | ready |
| ORCID | https://orcid.org/ | 作者身份 | P2 | ready |
| ROR | https://ror.org/ | 机构标识 | P2 | ready |
| DataCite | https://datacite.org/ | 数据集 DOI | P2 | ready |
| Zenodo | https://zenodo.org/ | 研究数据与软件 | P1 | ready |
| Figshare | https://figshare.com/ | 研究数据 | P2 | ready |
| Dryad | https://datadryad.org/ | 数据期刊仓库 | P2 | ready |
| OSF | https://osf.io/ | 预注册与数据 | P1 | ready |
| GitHub | https://github.com/ | 代码、数据、工具 | P1 | ready |
| arXiv API | https://info.arxiv.org/help/api/index.html | 预印本 | P1 | ready |
| Crossref REST | https://api.crossref.org/ | DOI 元数据 | P0 | ready |
| sitemap.xml | 各官网 `/sitemap.xml` | 页面清单 | P0 | ready |
| RSS/Atom | 各官网 `/feed` | 更新流 | P1 | ready |
| EDTF | https://www.loc.gov/standards/datetime/ | 日期标准 | P0 | ready |
| CIDOC-CRM | https://www.cidoc-crm.org/ | 事件本体 | P1 | ready |
| TEI | https://tei-c.org/ | 文本标注 | P2 | ready |

## 八、第一批抓取建议

先从不需要登录、条款明确、机器可读的入口开始：

1. PubMed/Europe PMC：补齐论文型事件。
2. ClinicalTrials.gov API v2：补齐试验型事件。
3. 机构官网与 RSS：补齐产业、竞赛和政策事件。
4. Internet Archive/Project Gutenberg/Chinese Text Project：补齐书籍与原始文献。
5. Wikidata/PeriodO：补齐实体与时期关系。
6. Reddit/X/Telegram：只走私有雷达，不进入公开候选池。

抓取后统一登记 `candidate_pool_id`、来源类别、抓取方式、可达性、许可边界、优先级与映射事件队列。
