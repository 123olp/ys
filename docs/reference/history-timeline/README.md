# Human Infra 历史年表工程包

本目录是《永生史》的严肃历史年表标准包。它把“大历史重要事件一览”从散文年表升级为可复核、可版本化、可发布的结构化时间线工程。

## 定位

这份年表属于跨学科的严肃历史工程：

- 观念史与概念史：追踪“永生、灵魂、长寿、复活、意识延续”等概念的语义变化。
- 死亡与寿命的文化史/医学史：承接 Ariès 以来的死亡史传统。
- 宗教史、历史人口学、科学史与未来学谱系：处理不同文明的永生路径。
- 数字人文/历史信息学：用结构化事件、来源卡和时间标准支持复核与可视化。

它服务于 `docs/publications/history-of-immortality.md`，不替代公共作品正文。

## 文件

| 文件 | 职责 |
| --- | --- |
| `README.md` | 工程包入口与使用说明 |
| `CONTRACT.md` | 年表字段、命名、日期、来源与禁止用途契约 |
| `GOVERNANCE.md` | 证据分级、审阅、生命周期、质量门禁与更新治理 |
| `TOOLS.md` | 成熟开源工具、标准与指导文献 |
| `timeline.schema.json` | 年表 JSON Schema 机器契约 |
| `sources.schema.json` | 来源卡 Schema |
| `periods.schema.json` | 时期定义 Schema |
| `timeline.json` | 正式年表数据：2592 条事件 |
| `sources.json` | 正式来源卡：2602 个来源 |
| `periods.json` | 时期定义与 PeriodO 映射状态：31 个时期 |
| `example-events.json` | 引用式数据示例 |
| `works-subset.schema.json` | 作品子集 Schema |
| `works-subset.v1.json` | 第一版作品子集：400 条事件入选，待逐条复核 |
| `works-review-register.schema.json` | 本地复核登记 Schema |
| `works-review-register.v1.json` | 首批 31 条事件本地复核登记 |
| `publication-manifest.schema.json` | 展示与出版清单 Schema |
| `publication-manifest.v1.json` | 展示与出版机器契约 |
| `PUBLICATION.md` | 展示与出版架构说明 |
| `preview.js` | 时间轴图表与事件阅读交互脚本 |
| `preview-core.js` | 核心纯函数模块，浏览器与 Node 共用，可单测 |
| `echarts.min.js` | 本地化 ECharts 运行时，预览不依赖外部 CDN |
| `timeline-events.psql.txt` | 完整事件明细 psql 表格（由 `make history-timeline-preview` 生成） |
| `timelinejs.json` | 图表发布数据，保留 TimelineJS JSON 兼容结构（由 `make history-timeline-preview` 生成） |
| `timelinejs.light.json` | 图表与筛选用轻量发布数据，不含完整正文与来源链接（由 `make history-timeline-preview` 生成） |
| `preview.html` | 可直接打开的 ECharts 图表模式预览（由 `make history-timeline-preview` 生成） |

事件录入模板位于 `docs/templates/history-event.md`。

## 使用方式

1. 新事件先写为 JSON 事件对象，放入 `timeline.json`。
2. 新来源先写入 `sources.json`，新时期先写入 `periods.json`。
3. 事件通过 `sources` 和 `period_id` 引用来源卡与时期定义，不内嵌重复来源对象。
4. 用 `make history-timeline-gate` 做机器校验。
5. 来源必须可追溯，证据等级必须显式标注。
6. 审阅通过后，才能在 `docs/publications/history-of-immortality.md` 中引用。

作品化入口：

```bash
make history-timeline-works-subset
```

重新生成发布原型：

```bash
make history-timeline-preview
```

核心函数单测：

```bash
make history-timeline-core-test
```

## 当前进度

- 来源卡：2602 个来源已注册，包含重复引用和疑似错源标注。
- 事件：2592 条事件已转为结构化 JSON，覆盖神话、思想、技术、制度、实践和失败教训。
- 日期：使用 EDTF 风格字符串表达约数、区间和长时段。
- 时期：31 个本地时期定义，16 个已匹配 PeriodO URI，15 个标记为 `pending`。
- 复核：全部事件仍为 `unreviewed` / `draft`，尚未进入本地复核或独立审阅。
- 作品子集：`works-subset.v1.json` 已登记 400 条第一版作品事件，覆盖全部时期、8 个路径族、10 类事件类型和 5 类证据等级；当前 `reviewed_event_count=31`。
- 本地复核：首批 31 条事件已登记为 `locally_reviewed`，来源 URL/DOI 可达并完成标题匹配；独立 fresh review 尚未开始。
- 可视化：已生成图表发布数据与可浏览原型，当前预览遵循零美化语义界面规范，psql ASCII 表格承载核心数据，ECharts 图表作为增强视图；支持搜索、筛选、年份缩放、事件阅读器与图表双向联动、事件 ID/序号跳转、动态聚合表，以及“全部资料 / 作品子集 / 本地已复核”三档范围；完整正文自动加载并直接显示，ECharts 本地化运行，预览文件为 `timelinejs.json`、`timelinejs.light.json`、`preview.html`、`preview-core.js` 和 `echarts.min.js`。
- 出版层：`publication-manifest.v1.json` 定义时间轴、永生史正文、健康手册和永生指南四类出版入口及各自 `review_gate`；说明见 `PUBLICATION.md`。

第二轮补录来源：`docs/publications/history-of-immortality.md` 与
`docs/source-notes/effective-immortality-kb-cards/`；新增事件包括古代神话与道家思想、
19-20 世纪寿命科学奠基、CRISPR 与异种移植、脑保存与连接组、DishBrain 与类器官智能、
超人类主义组织、Blueprint，以及苦杏仁苷、激素滥用、干细胞诊所、人头移植和年轻血浆等失败教训。

第三轮补录来源：数据源候选池与官方抓取核验；新增 XPRIZE Healthspan 启动及首批里程碑、
Hevolution、LEV RMR 首轮结果、TAME 试验设计、DunedinPACE、OpenAI/Retro 因子设计、
Life Biosciences ER-100 IND 与首例给药、Loyal LOY-002、ARPA-H PROSPR。

第四轮补录来源：数字与认知路径官方页面和论文元数据；新增醛稳定低温保存、脑保存奖、
OrganEx、果蝇全脑连接组、动态人类数字孪生、Griefbots、脑机接口伦理、异种肾移植 EXPAND。

第五轮补录来源：暂停重建、智能治理与产业节点；新增大鼠肾脏玻璃化移植、常温机器灌注肺保存、
器官玻璃化升尺度、类器官智能伦理、AI 风险分类数据库、NewLimit 4.35 亿美元 C 轮融资。

第六轮补录来源：生物打印、长寿产业资金、健康老龄化政策与 AI 治理；新增 3D 生物打印心脏组织、
OSK 基因疗法小鼠延寿、Longevity Fund、WHO 全球年龄歧视报告、NIST AI RMF、Turn Bio ERA。

第七轮补录来源：身体功效替代、衰老标志物验证、AI 药物发现与 AI 治理；新增 FDA 自动胰岛素泵、
衰老标志物验证标准、生成式 AI 药物 IIa 期试验、长寿生物技术综述、美国 AI 行政令。

第八轮补录来源：历史档案与原始书籍；新增洛克《人类理解论》、休谟《人性论》、
康德《纯粹理性批判》、托尔斯泰《伊凡·伊里奇之死》、博尔赫斯《永生》。

第九轮补录来源：古典生命哲学、中古医学与老年科学机构；新增卢克莱修《物性论》、
《庄子》养生思想、塞涅卡《论生命短暂》、伊本·西那《医典》、Academy of Geroscience
更名、尼采永恒轮回生命观。

第十轮补录来源：古埃及医学文献、晚期古代神学、近代长寿书与 20 世纪永生主义文本；
新增埃伯斯纸草、奥古斯丁《上帝之城》、罗吉尔·培根长寿书英译本、乌纳穆诺
《生命的悲剧意识》、哈林顿《不朽主义者》。

第十一轮补录来源：人口统计基础设施、AI 生物科学与基因编辑制度；
新增人类死亡率数据库、AlphaFold 2、AlphaMissense、2020 年 CRISPR 诺奖、
《追求长寿红利》健康寿命议程。

第十二轮补录来源：克隆里程碑与人类细胞重编程节点；
新增克隆羊多莉、短暂非整合 mRNA 重编程、MPTR 人类成纤维细胞年轻化。

第十三轮补录来源：人体临床与监管边界；
新增 TRIIM 人体试验、FDA 批准首个 CRISPR 基因疗法 Casgevy、
首个体内 CRISPR 临床数据、FDA 干细胞疗法风险警告。

第十四轮补录来源：老年科学研究基础设施；
新增 Buck Institute、SENS Research Foundation、Calico、UK Biobank。

第十五轮补录来源：认知外延、人格同一性与超级智能经典文本；
新增恩格尔巴特智能增强框架、帕菲特《理与人》、克拉克与查默斯《扩展心智》、
查默斯奇点哲学分析、博斯特罗姆《超级智能》。

第十六轮补录来源：死亡意识与永生意义经典文本；
新增《亡灵书》、但丁《神曲》、弗洛伊德《超越快乐原则》、加缪《西西弗神话》、
贝克尔《拒斥死亡》。

第十七轮补录来源：老年科学方法学、人体试验与结构数据库；
新增 NIA ITP 中期报告、Geroscience 假说、首个人体 senolytics 报告、
AlphaFold 蛋白质结构数据库 2.14 亿序列覆盖。

第十八轮补录来源：失败教训与监管反证；
新增 GSK 终止 SRT501、UBX0101 senolytics II 期失败、
FDA 恢复 NMN 膳食补充剂地位。

第十九轮补录来源：生物重建与生殖未来选择权；
新增首例合成基因组细菌细胞、CRISPR-Cas9 可编程编辑、首例手移植、
首例部分面部移植、首位 IVF 婴儿出生。

第二十轮补录来源：跨文明永生思想与普及文本；
新增《得墨忒耳颂歌》、《淮南子》、《薄伽梵歌》、《西藏度亡经》、
库兹韦尔与格罗斯曼《奇妙之旅》。

第二十一轮补录来源：基因编辑伦理与监管；
新增人类基因编辑国际峰会声明、CRISPR 婴儿事件、英国人类受精与胚胎学法、
FDA 批准 Luxturna、EMA 授权 Glybera。

第二十二轮补录来源：脑机接口、神经技术监管与 AI 治理；
新增 BrainGate 人体研究、Argus II 视网膜假体、Neuralink 首例人体植入、
BRAIN Initiative、欧盟人工智能法案。

第二十三轮补录来源：数字迁移与全脑仿真路线；
新增《全脑仿真路线图》、线虫完整连接组、艾伦脑科学研究所、
人类连接组计划、人类脑计划。

第二十四轮补录来源：寿命理论谱系与生物年龄指标；
新增奥洛夫尼科夫端粒边际切除理论、柯克伍德一次性体细胞理论、
PhenoAge、GrimAge、玛土撒拉基金会更名。

第二十五轮补录来源：数字永生与意识上传叙事谱系；
新增《神经漫游者》、《攻壳机动队》、《置换城市》、
《灵魂机器的时代》、《副本》。

第二十六轮补录来源：古代神话与复活谱系；
新增奥尔菲斯金箔、《但以理书》身体复活、第二圣殿犹太教复活教义、
《诗体埃达》诸神黄昏、阿弥陀佛净土思想。

第二十七轮补录来源：现代档案发现与文本保存基础设施；
新增奥克西林库斯纸草、纳格哈马迪文库、死海古卷首批发现、
库姆兰第四洞穴、圣书之龛。

第二十八轮补录来源：纳米技术与分子修复奠基文献；
新增费曼《底部还有大量空间》、德雷克斯勒《创造的引擎》与《纳米系统》、
弗雷塔斯《纳米医学》第一卷、德雷克斯勒《富足激进》。

第二十九轮补录来源：衰老机制关键论文；
新增佩托悖论、炎症衰老、氧化应激与衰老生物学、p16INK4a 衰老标志物、
衰老相关分泌表型 SASP。

第三十轮补录来源：超人类主义与数字主体奠基文本；
新增赛博格概念、哈拉维《赛博格宣言》、博斯特罗姆超人类主义 FAQ、
哈贝马斯《人类本性的未来》、博斯特罗姆后人类价值论。

第三十一轮补录来源：低温保存与脑保存基础设施；
新增阿尔科生命延续基金会、冷冻学会、脑保存基金会、
KrioRus、Nectome。

第三十二轮补录来源：寿命上限与遗传长寿争论；
新增《寻找玛土撒拉》、《打破寿命预期上限》、人口生物学综述、
人类寿命极限证据、FOXO3A 长寿关联。

第三十三轮补录来源：科幻中的身份与再生命题；
新增《弗兰肯斯坦》、《时间机器》、《仿生人会梦见电子羊吗？》、
《两百岁的人》、《雪崩》。

第三十四轮补录来源：产业资金网络与转化试验组织；
新增 Life Extension Foundation、Methuselah Mouse Prize、
Rejuvenate Bio、Cambrian Biopharma 与 Novartis 许可、Juvena B 轮融资。

第三十五轮补录来源：记忆可塑性、神经形态计算与脑启发硬件；
新增 LTP 机制发表、Mead 神经形态电子系统、IBM TrueNorth、
Intel Loihi、SpiNNaker 百万核里程碑。

第三十六轮补录来源：AI 与长寿技术治理；
新增 OECD AI 原则、WHO AI 健康伦理指南、UNESCO AI 伦理建议书、
《布莱切利宣言》、《人工智能框架公约》。

第三十七轮补录来源：化学重编程、表观遗传编辑与记忆重编程；
新增人类体细胞化学重编程、部分化学重编程年轻化、
表观遗传编辑临床转化综述、体内 hit-and-run PCSK9 沉默、
记忆痕迹细胞 OSK 部分重编程。

第三十八轮补录来源：第二代生物年龄时钟与器官特异性衰老标志物；
新增 DunedinPoAm、GrimAge 2、Aging Biomarker Consortium
脑衰老、血管衰老和心脏衰老标志物共识框架。

第三十九轮补录来源：神经权利与脑数据治理；
新增国际脑计划神经伦理问题指南、Neurorights Initiative、
OECD 负责任神经技术创新建议、智利神经权利法案、
神经权利作为重构人权框架。

第四十轮补录来源：数字遗产、数字化身与死亡制度；
新增 Facebook 纪念账户、Google Inactive Account Manager、
UFADAA、数字来世跨学科研究和数字死亡研究议程。

第四十一轮补录来源：人格同一性理论谱系；
新增巴特勒记忆判准批评、里德勇敢军官反例、威廉斯自我与未来、
舒梅克与斯温伯恩人格同一性辩论、谢赫特曼自我构成理论。

第四十二轮补录来源：脑死亡标准与生命延续制度；
新增 coma dépassé 概念、哈佛不可逆昏迷定义、美国《统一死亡判定法》、
美国神经病学学会成人脑死亡指南、World Brain Death Project 国际共识。

第四十三轮补录来源：生命支持与人工器官；
新增铁肺首次临床使用、人工心肺机首例成功开胸手术、闭式胸外心脏按压、
首例人类心脏移植、Jarvik-7 全人工心脏首次植入人体。

第四十四轮补录来源：体外膜氧合、心室辅助装置与人工器官监管；
新增首例临床左心室辅助装置、首例新生儿 ECMO、FDA 首个植入式心室辅助系统批准、
Berlin Heart EXCOR 儿科批准、CARMAT 全人工心脏 CE 标志。

第四十五轮补录来源：体外生命支持组织、随机对照证据与长期随访注册表；
新增 ELSO 成立、REMATCH、CESAR、EOLIA、ELSO 注册表 10 万名幸存者报告。

第四十六轮补录来源：器官保存、机器灌注与体外器官维护；
新增 Belzer 连续低温灌注、UW 溶液、PROCEED II、COPE 常温肝脏保存、
人类肝脏体外保存三天后成功移植。

第四十七轮补录来源：低温保存基础、循环死亡捐献分类与常温区域灌注；
新增甘油低温保存精子复苏、冷冻人类胚胎首次妊娠、Maastricht DCD 分类、
美国 NRP 心脏 DCD、JAMA Surgery NRP 肝脏扩展。

第四十八轮补录来源：人工器官伦理、监管与长期生存数据；
新增 ESRD Medicare、医疗器械修正案、NOTA/OPTN、国家科学院人工心脏政策报告、
INTERMACS 首份年度报告、HeartMate II 目的地治疗批准。

第四十九轮补录来源：机械循环支持长期证据、指南与注册表治理；
新增 MOMENTUM 3 两年结果、STS/INTERMACS 2019/2023/2025 年度报告、
2022 AHA/ACC/HFSA 心衰指南、2023 ISHLT 机械循环支持指南。

第五十轮补录来源：健康老龄化全球治理谱系；
新增马德里老龄问题国际行动计划、WHO 积极老龄化框架、全球老龄与健康战略、
WHA73(12)、联合国健康老龄化十年决议和 WHO 基线报告。

第五十一轮补录来源：再生医学与衰老干预转化；
新增人类胚胎干细胞系、人类 iPS 细胞、Geron 首个人类胚胎干细胞临床试验、
2012 年细胞重编程诺奖、日本首例 iPS 细胞来源 RPE 移植、FDA 批准首个 CAR-T 疗法。

第五十二轮补录来源：细胞治疗产业化与 iPS 细胞库；
新增首个人类基因治疗试验方案、FDA 批准 Provenge、CiRA 临床级 iPS 细胞储备、
首例 iPS 细胞来源心肌细胞片移植、iPS 细胞治疗帕金森病 I/II 期结果、
日本药事委员会对异体 iPS 细胞产品的条件性批准建议。

第五十三轮补录来源：细胞与基因治疗监管及真实世界安全；
新增 Yescarta 首个大 B 细胞淋巴瘤 CAR-T、Zolgensma 首个全身性基因疗法、
Abecma 首个骨髓瘤细胞基因疗法、Yescarta 二线治疗批准、
FDA 对 CAR-T 继发性 T 细胞恶性肿瘤的黑框警告。

第五十四轮补录来源：细胞疗法扩展与下一代基因治疗监管；
新增欧盟授权 Libmeldy、FDA 批准 Breyanzi 并首次授予 RMAT 许可、
Carvykti 第二个 BCMA CAR-T、FDA 批准 Lenmeldy、首个实体瘤工程化细胞疗法 Tecelra。

第五十五轮补录来源：长寿产业资金网络二阶段官方与可靠来源；
新增 Human Longevity 成立、Life Biosciences 成立、Longevity Vision Fund 启动、
Tally Health 种子轮、BioAge Labs IPO。

第五十六轮补录来源：长寿产业资本与近期临床转化三阶段；
新增 Retro Biosciences 早期融资、NewLimit Series B 与 4500 万美元追加融资、
Life Biosciences Series D、BioAge BGE-102 Phase 1 中期数据和 QUELL-CV 首例给药。

第五十七轮补录来源：AI 自动化科学引擎；
新增 GNoME 材料发现、A-Lab 自主实验室、RoboChem 自动化化学合成、
AlphaFold 3 生物分子复合物预测和 Google AI co-scientist。

第五十八轮补录来源：脑机接口人体临床与神经技术监管二阶段；
新增 BrainGate 无线居家 BCI、Synchron COMMAND 首例美国入组、
Neuralink PRIME 第二例、Blindsight 突破性设备认定和 CAN-PRIME 国际试验。

第五十九轮补录来源：脑机接口结果、设备集成与国际试验二阶段；
新增 Synchron COMMAND 12 个月阳性结果、Apple Vision Pro 首用、
Neuralink UAE-PRIME、GB-PRIME 和 VOICE 沟通恢复试验。

第六十轮补录来源：脑机接口平台集成、资本与多国试验三阶段；
新增 Neuralink CONVOY、Synchron Apple BCI HID 协议、2 亿美元 D 轮、
INTENT 早期可行性和 FOCUS-AUS 澳大利亚功能结局研究。

第六十一轮补录来源：神经形态与活性算力、复合组织与异种移植二阶段；
新增 Intel Hala Point、FinalSpark 远程湿件计算平台、Cortical Labs
合成生物智能实验室方法、NYU 全眼与部分面部联合移植，以及六基因编辑猪
全肝与双肾遗体多器官异种移植。

第六十二轮补录来源：生物年龄指标跨人群验证与产业临床推进；
新增 MOMENTUM 3 五年结果、衰老生物标志物干预研究专家共识、
17 种人类组织 DNA 甲基化衰老特征荟萃分析、14 种共识衰老标志物
死亡率预测比较，以及 NewLimit 首个候选药进入临床开发计划。

第六十三轮补录来源：衰老测量转化、学科会议与产业科研；
新增衰老生物标志物转化建议、第 12 届 ARDD 会议报告、
首届全球老年物理学会议共识、Retro Biosciences 精确重编程评述，
以及含 Altos Labs 合作的灵长类骨髓衰老与维生素 C 干预研究。

第六十四轮补录来源：脑机接口言语解码、家庭长期使用与监管推进；
新增 Synchron FOCUS-CAN、锁闭综合征意图言语解码、双手快速打字
神经假体、皮层内 BCI 长期独立家庭使用，以及 FDA 授予 Neuralink
言语恢复项目突破性设备认定。

第六十五轮补录来源：BCI 资本、使用里程碑、数据基础设施与神经数据隐私立法；
新增加州神经数据隐私法、Neuralink 6.5 亿美元 E 轮、Telepathy 独立使用累计数据、
Neuralink datarepo 开源目录，以及 Synchron 经血管 BCI 十年临床转化主题演讲。

第六十六轮补录来源：生物衰老时钟、重编程年轻化、基因治疗衰老与 BCI 数据保护；
新增 Nature Medicine 生物衰老时钟综述、重编程诱导年轻化综述、
内皮细胞瞬时重编程功能年轻化研究、基因治疗干预衰老综述，
以及植入式 BCI 数据保护框架综述。

第六十七轮补录来源：器官机器灌注、再调节与异种移植转化；
新增器官再调节临床与伦理观点、机器灌注经济学范围综述、
美国低温与常温机器灌注肝移植队列、猪源免疫相容器官综述，
以及儿科供肝常温机器灌注单中心病例系列。

第六十八轮补录来源：AI 自动化科研与药物发现；
新增 AI 驱动药物合成综述、TeLLAgent 双代理科研框架、
自驱动扫描探针显微镜综述、自驱动实验室综述，
以及代理式 AI 与 Eroom 定律讨论。

第六十九轮补录来源：低温保存、生物停滞与未来选择权；
新增 AI 视角冷冻保护剂设计、组织与器官制冷剂选择指南、
玻璃化组织电场复温综述、全卵巢低温保存与移植综述，
以及 CryoClean 封闭玻璃化胚胎保存系统。

第七十轮补录来源：健康寿命、衰老测量与长寿医学监管；
新增老年医学试验分层终点与胜率统计、laromestrocel 衰老虚弱
随机 2b 期试验、长寿药理学临床转化综述、数字健康长寿政策议程，
以及欧盟健康老龄化与长寿研究支持计划呼吁。

第七十一轮补录来源：认知增强、记忆编辑与神经权利；
新增 BCI 具身化与持续知情同意、神经技术伦理治理范围综述、
植入式医疗设备伦理分析、老年人经颅电刺激与认知训练随机试验，
以及长期动作视频游戏训练注意力增强 EEG 研究。

第七十二轮补录来源：长寿产业资金、联邦资助与健康寿命转化；
新增 Retro Biosciences 初始融资、RTR242 Phase 1 披露、
ARPA-H PROSPR 首批 7 个研究团队、Cambrian 最高 3080 万美元资助，
以及 Linnaeus 最高 2200 万美元资助。

第七十三轮补录来源：脑机接口言语解码、手势编码与长期电极数据；
新增腹侧前中央回言语模式与响度编码、手势编码、内部言语、
二维多手势拖放解码，以及 BrainGate 14 名参与者微电极阵列长期表现预印本。

第七十四轮补录来源：AI 自动化科研与材料发现；
新增统计 AI 催化剂筛选、AutoLabs 多代理化学实验、
代理式 AI 系统生物学验证、AI 4.0 知识生成式科研，
以及 AI 科学家组学发现基准。

第七十五轮补录来源：细胞与基因疗法、再生医学与临床转化；
新增包裹细胞局部 IL2 首次人体试验、肝细胞扩增与类器官综述、
脐带间充质干细胞异质性范式、AI 驱动 CAR-T 转化，
以及衰老与长寿基因治疗综述。

第七十六轮补录来源：数字孪生、健康智能与主体状态建模；
新增乳腺癌虚拟人孪生、更年期数字孪生、炎症性肠病数字孪生、
检验医学 2050 健康智能网络，以及医疗诊断 AI 数字孪生范围综述。

第七十七轮补录来源：异种移植、器官保存与组织重建；
新增异种灌注综述、改善器官可及性低温保存策略、器官移植现状综述、
异种移植公共媒体叙事分析，以及肾移植等待名单患者意愿研究。

第七十八轮补录来源：健康老龄化与老年权利治理；
新增联合国老年人权利政府间工作组组织会议与首届会议、2026 世界老年人虐待防治日、
2026 亚太区域人口老龄化会议，以及 UNECE 老龄叙事政策简报。

第七十九轮补录来源：脑机接口监管与产业节点；
新增 CorTec FDA 突破性设备认定、Paradromics Connect-One IDE 与首例 Connexus 植入、
Neuralink Telepathy 两年使用更新，以及 Synchron Stentrode 100 例里程碑。

第八十轮补录来源：生物年龄时钟与衰老标志物；
新增跨队列代谢组学时钟、BAGE 贝叶斯转录组年龄、BHARAT 印度人群多组学研究、
PhysAge 多系统分子时钟，以及 DNA 甲基化时钟与衰弱荟萃分析。

第八十一轮补录来源：AI 药物发现与临床转化；
新增生成式 AI 发现 TNIK 抑制剂 IIa 期论文、Rentosertib 吸入临床批件、
AI 发现候选药 III 期启动、精准肿瘤学 AI 转化综述，
以及 AI 设计或塑造药物人体试验管线数量盘点。

第八十二轮补录来源：低温保存、3D 生物打印与再生；
新增冷冻保护生物墨水直接生物打印、3D 生物打印进展综述、
卵巢组织冷冻保存综述、子宫冷冻保存转化综述，
以及公升级物理玻璃化与纳米复温研究。


第八十三轮补录来源：细胞重编程与年轻化；
新增 Gerozyme 靶向综述、部分重编程治疗策略综述、短暂重编程恢复内皮功能研究、
体内化学重编程脂滴毒性失败证据，以及芽殖酵母复制衰老与年轻化综述。

第八十四轮补录来源：细胞衰老、SASP 与 senolytics；
新增成孔毒素 senolytic 策略、个体化 senolytic 试验方法、细胞衰老驱动糖尿病动脉粥样硬化、
线粒体动力学与细胞衰老，以及血浆置换靶向 SASP 综述。

第八十五轮补录来源：长寿医学与健康寿命；
新增长寿医学数字孪生、单细胞多组学精准长寿医学、线虫延寿候选化合物、
COSMOS 多维生素代谢组随机试验结果，以及寿命与健康寿命机制区分综述。

第八十六轮补录来源：异种移植、器官保存与组织重建；
新增器官保存到异种移植路径综述、异种移植与器官贩运影响、HLA-E/HLA-G 免疫调节、
临床猪器官移植经验回顾，以及异种器官与常用药物相互作用综述。

第八十七轮补录来源：AI 生物医学与健康智能；
新增胚胎形态 AI 基础模型、生物医学大模型代理伦理、机器学习药物发现方法综述、
认知衰老 AI 数字孪生架构，以及结构生物学 AI 突破综述。


第八十八轮补录来源：长寿药理学与老年医学试验；
新增 PEARL 雷帕霉素试验、超适应症使用证据审查、二甲双胍心血管衰老综述、
Dasatinib 联合 Quercetin pilot 方案，以及二甲双胍 geroprotector 再评估。

第八十九轮补录来源：干细胞与再生医学；
新增离体器官年轻化、干细胞损伤检测与修复、内源可塑性、
MSC 胞外囊泡标准化和刺激响应水凝胶综述。

第九十轮补录来源：脑机接口与神经增强；
新增 BCI 康复评估专家共识、临床实现距离、BCI 与无创脑刺激组合、
UNESCO 神经技术伦理草案评论，以及神经技术文化叙事研究议程。

第九十一轮补录来源：认知增强、记忆与数字生物标志；
新增认知训练联合运动随机试验、工作记忆训练、海马认知假体哲学分析、
游戏化认知评估和言语数字生物标志。

第九十二轮补录来源：健康老龄化、公平与治理；
新增老龄与长寿研究政策议程、饮食社会决定因素、居住照护环境、
老年人共同设计照护未来，以及痴呆住院患者需求定性研究。


第九十三轮补录来源：饮食限制与代谢健康；
新增 CALERIE 2 炎症表观遗传分析、器官特异性生物衰老随机试验、小 RNA 谱变化、
睡眠限制 DNA 甲基化试验，以及饮食干预表观遗传综述。

第九十四轮补录来源：表观遗传与衰老时钟；
新增椎间盘退变表观遗传时钟重置、内在能力血液时钟、爪蟾时钟、
糖尿病表观遗传加速和社会不平等，以及病毒潜伏与时钟失调研究。

第九十五轮补录来源：蛋白质稳态与自噬；
新增神经元自噬、自噬蛋白酶体串扰、衰老蛋白稳态、选择性自噬心血管作用，
以及 UBE2G1 造血干细胞衰老研究。

第九十六轮补录来源：免疫衰老与炎症；
新增心脏免疫衰老、结核清除受损、疫苗应答、外周免疫衰老与认知下降，
以及慢性炎症驱动肿瘤免疫衰老。

第九十七轮补录来源：心血管与健康寿命框架；
新增心脏代谢健康寿命德尔菲框架、体验性长寿框架、衰老机制冗余层级、
内在能力核心结局，以及 Discover Aging 期刊创建。

第九十八轮补录来源：神经退行与脑健康；
新增神经炎症与细胞衰老、神经韧性掩盖退行、PLCG2 遗传韧性、
星形胶质细胞自噬和脂质代谢研究。

第九十九轮补录来源：生殖健康与生育保存；
新增精卵保存生物技术、子宫内膜异位症、特纳综合征、
肿瘤生殖外泌体，以及年轻肿瘤患者生育结局综述。

第一百轮补录来源：数字健康与可穿戴；
新增 AI 与老年人幸福感、可穿戴认知衰退评估、野外纵向采集、
可穿戴心血管监测和睡眠数字生物标志研究。


第101轮补录来源：寿命建模与预测；新增 衰老作为网络化过程综述发表、峰值生产寿命定义与量化框架发表、裸盖菇素延长细胞寿命并改善老龄小鼠生存研究发表、线粒体 NAD+/NADH 比率遗传操纵延长寿命并改善阿尔茨海默表型研究发表、PLOS Aging and Health 期刊创建。
第102轮补录来源：脑保存与连接组；新增 人脑组织保存方法蛋白质组比较研究发表、大核连接组生成网络用于阿尔茨海默病分析发表、连接组引导胶质瘤切除系统综述发表、特发性正常压力脑积水全脑连接组分析发表、多发性硬化突触连接组与液体生物标志综述发表。
第103轮补录来源：低温保存与生物停滞；新增 绵羊卵巢组织慢冻与玻璃化存活比较研究发表、小鼠主动脉玻璃化保存研究发表、卵巢组织慢速冷冻与玻璃化质量比较荟萃分析发表、载体辅助玻璃化装置推动卵母细胞标准化保存发表、化学限定玻璃化培养基用于牛胚胎冷冻发表。
第104轮补录来源：生物打印与器官工程；新增 3D 生物打印器官移植工程综述发表、无支架光基高细胞密度生物打印研究发表、熔体电写骨修复支架综述发表、支架与无支架 3D 生物打印组织工程综述发表、3D 打印 PLGA/PLA 支架用于骨癌双模式治疗研究发表。
第105轮补录来源：AI 蛋白与药物设计；新增 生成式 AI 药物发现与蛋白设计综述发表、类器官-AI 平台药物发现治理观点发表、制药研发生成式 AI 从大模型到代理与监管综述发表、AI 原生药物设计五年议程发表、AI 重新定义药物递送系统逆向设计综述发表。
第106轮补录来源：数字孪生与个体建模；新增 患者中心数字孪生联邦增量学习框架发表、数字孪生是科学还是工程观点发表、患者流与临床调度 AI 智能数字孪生框架发表、乳腺癌类器官精准建模平台综述发表、香豆素与精准医学药物基因组学综述发表。
第107轮补录来源：照护系统与社会支持；新增 家庭长期照护者负担生物心理社会视角综述发表、辅助设备与长期照护机构照护者留任研究发表、疫情期养老院痴呆照护人格与照护者压力研究发表、长期照护人员营养教育范围综述发表、家庭照护者负担与居家照护质量有效性研究发表。
第108轮补录来源：纳米医学与递送系统；新增 脂质递送系统精准纳米医学用于肺结核综述发表、生物标志驱动 AI 辅助纳米医学乳腺癌综述发表、脂质纳米颗粒作为转化纳米医学平台综述发表、纳米医学穿越血脑屏障治疗阿尔茨海默病综述发表、空间组学引导纳米医学精准递送综述发表。
第109轮补录来源：计算神经科学与脑模拟；新增 认知计算神经科学未来十年综述发表、基于尖峰网络的意识计算神经病学模型发表、贝叶斯大脑理论计算神经科学综述发表、全脑机制是否支撑注意与意识研究发表、帕金森病慢性自适应深脑刺激居家监测研究发表。
第110轮补录来源：治理与伦理；新增 国际 AI 安全报告 2026 政策审计与治理分析发表、老龄与照护中 AI 问责从伦理到治理研究发表、生成式系统确定性治理运行时发表、欧盟 AI 伦理治理混合专业知识研究发表、残障权利视角重新构想神经技术治理研究发表。


第111轮补录来源：抗衰老药物与 geroprotector；新增 运动作为 geroprotector 聚焦表观遗传衰老综述发表、大模型与 AI 生命模型用于中药 geroprotector 配方研究发表、硝唑尼特在线虫与加速衰老小鼠中的抗衰老作用研究发表、基于 AI 与多组学的抗衰老和年龄相关疾病药物发现进展发表、AI 可编程虚拟人用于生理药理学药物发现发表。
第112轮补录来源：细胞重编程与年轻化；新增 细胞重编程作为激进年轻化策略综述发表、直接心脏重编程克服年龄相关代谢障碍研究发表、组学时代直接心脏重编程综述发表、病理过程中造血细胞命运重编程综述发表、食品来源多糖水凝胶重编程微环境用于皮肤年轻化发表。
第113轮补录来源：器官芯片与类器官；新增 患者中心器官芯片模型框架发表、眼部器官芯片系统演化综述发表、器官芯片用于药物发现微生理系统综述发表、器官芯片疾病建模与药物测试应用综述发表、器官芯片驱动药物开发变革综述发表。
第114轮补录来源：蛋白质组与多组学；新增 3D 蛋白质组学用于结构功能与生物标志发现发表、GNPC 神经退行疾病蛋白质组资源发表、尿液蛋白质组识别不稳定颈动脉斑块非侵入性生物标志研究发表、复合肽对敏感皮肤抗衰老作用与机制研究发表、从表观标记检测到表观编辑策略理性设计综述发表。
第115轮补录来源：可解释 AI 与临床决策；新增 可解释机器学习预测抑郁和糖尿病研究发表、儿童阑尾炎和腹膜炎可解释机器学习框架发表、生成式 AI 应如何改变临床决策支持观点发表、AI 临床决策支持工具中的广告问题研究发表、老龄居住社区可持续景观再生 AI 决策支持研究发表。
第116轮补录来源：心理健康与情绪韧性；新增 老年人心理韧性与社会支持、积极性和孤独关联研究发表、开罗老年难民流离失所中的韧性创伤与身份研究发表、年龄污名与晚年情绪隔离中介研究发表、阿尔茨海默风险行为改变情境情绪反应研究发表、身体活动促进可持续健康老龄化的快乐老龄化观点发表。
第117轮补录来源：身体活动与运动干预；新增 老年人身体活动干预评估方法与指标系统综述发表、祖孙共同身体活动代际干预开发研究发表、游戏化数字身体活动干预自主动机随机试验发表、拉丁裔帕金森老年人远程身体活动试验招募研究发表、力量训练与舞蹈训练随机试验勘误发表。
第118轮补录来源：睡眠与昼夜节律；新增 昼夜节律健康定义与指数框架发表、光暴露对睡眠和昼夜节律影响建模研究发表、褪黑素在昼夜节律与脑健康中的神经保护综述发表、Web3 去中心化睡眠昼夜节律健康数据共享系统发表、估算心肺适能与昼夜节律综合征跨队列研究发表。
第119轮补录来源：环境暴露与表观遗传；新增 长期空气污染暴露与表观遗传时钟系统综述发表、环境神经毒物诱发早衰脑表观机制综述发表、出生时砷暴露与社会经济地位对成人表观衰老影响研究发表、宇航员作为人类衰老模型表观年龄响应研究发表、环境暴露表观修饰与不良妊娠结局系统综述发表。
第120轮补录来源：人口统计与全球健康；新增 美国心血管病与癌症并存死亡率趋势研究发表、1999-2023 年美国老年人骨关节炎死亡率趋势发表、积极老龄态度与十年死亡延迟人群研究发表、老年人数字金融包容趋势挑战与策略发表、灾害与老龄化全球研究趋势发表。


第121轮补录来源：神经调控与脑机接口；新增 《Selective tACS modulation of aperiodic EEG components》论文发表、《Understanding the neural pathways of trigeminal nerve stimulation》论文发表、《The modulation of spatiotemporal patterns of neural activity depend on…》论文发表、《EEG-Based Evaluation of Brain Activity Modulation Through Deep Brain S…》论文发表、《Hormonal modulation after deep brain stimulation and spinal cord stimu…》论文发表。
第122轮补录来源：细胞衰老与 SASP；新增 《Senescence-associated secretory phenotype: the pathogenic factor drivi…》论文发表、《Proteostasis decline and endoplasmic reticulum stress in aging》论文发表、《Extracellular Vesicles as Key SASP Carriers Driving Cellular Senescenc…》论文发表、《The multifaceted inducers of cellular senescence》论文发表、《Inflammaging and Senescence-Associated Secretory Phenotype (SASP) in P…》论文发表。
第123轮补录来源：基因编辑与表观编辑；新增 《Investigating the Potential of Gene Editing Technologies in Enhancing …》论文发表、《Editing epigenetic age》论文发表、《Novel gene-editing technologies: applications of CRISPR-Cas9, base edi…》论文发表、《Epigenetic editing to advance CAR T cell therapy》论文发表、《Gene Editing Pioneer Sangamo Files for Chapter 11 Bankruptcy》论文发表。
第124轮补录来源：器官保存与灌注；新增 《Machine Perfusion Improves Organ Preservation for Transplant》论文发表、《The Current State of Organ Perfusion and Preservation: Lessons From th…》论文发表、《Updates on Machine Perfusion for Organ Preservation: Highlights From t…》论文发表、《Characteristics and Outcomes of Combined Lung-Liver Transplant with or…》论文发表、《Response to Machine Perfusion Organ Preservation: Highlights From the …》论文发表。
第125轮补录来源：营养与饮食干预；新增 《Supporting healthy ageing through community-based dietary education》论文发表、《The Relationship Between Receptivity to Questions about Dietary Just-i…》论文发表、《Psychological attributes predict dietary pattern transitions in older …》论文发表、《Associations of dietary patterns with mild cognitive impairment in old…》论文发表、《Low muscle mass as an independent risk factor for 30-day mortality amo…》论文发表。
第126轮补录来源：免疫疗法与疫苗；新增 《Reversing Immune Aging to Improve Immunotherapy Outcomes》论文发表、《Anti-Tumor Immunotherapy of Scutellaria Baicalensis-Derived Vesicles o…》论文发表、《Metabolism of Young and Aged Hematopoietic and Acute Myeloid Leukemia …》论文发表、《Clonal hematopoiesis boosts response to immune checkpoint therapy》论文发表、《Considerations on Heterochronic Plasma Transfer in Aging Research》论文发表。
第127轮补录来源：运动与康复；新增 《Methods and Safety of Exercise Testing in Older Adults: A Narrative Re…》论文发表、《Effects of an Exercise-Assisting Mobile App for Osteoarthritis Rehabil…》论文发表、《The Benefits of a Digital Exercise Intervention for Older Adults: Fitt…》论文发表、《Can Older Adults Become Exercise Junkies? Commentary on Exercise Addic…》论文发表、《Effects of Commercial Exergames vs. Traditional Indoor Exercise on Moo…》论文发表。
第128轮补录来源：认知与心理健康；新增 《Do ecosystem improvements enhance the cognitive function of older adul…》论文发表、《Perceived age discrimination and cognitive function in older Korean ad…》论文发表、《Self-perceptions of aging and cognitive function: mediating role of vo…》论文发表、《The effects of social isolation and loneliness on cognitive function i…》论文发表、《Cognitive function and its change over time: effects on depression tra…》论文发表。
第129轮补录来源：数据治理与隐私；新增 《Balancing privacy and explainability in AI: Differential privacy and g…》论文发表、《Data privacy in the health AI era》论文发表、《AI governance and data privacy in cross-border contexts: comparative a…》论文发表、《From property to power: Why governance, not ownership, will define per…》论文发表、《A Privacy-First Governance Architecture for Compliant Generative AI Da…》论文发表。
第130轮补录来源：全球长寿产业与政策；新增 《Psychedelics and longevity: implications for lifespan, healthspan and …》论文发表、《Psilocybin and human longevity》论文发表、《Brain Aging and the Pursuit of Longevity: Biological Mechanisms and Cl…》论文发表、《Leveraging transcriptome-based biological aging clocks and mRNA signat…》论文发表、《A Unified Longevity-Financial Risk Framework for Evaluating Pension Fu…》论文发表。
第131轮补录来源：衰老生物标志物验证；新增 《Circadian rhythm analysis using wearable-based accelerometry as a digital biomarker of aging and healthspan》论文发表、《Quantification of healthspan in aging mice: introducing FAMY and GRAIL》论文发表、《Hallmarks of aging: middle-aging hypovascularity, tissue perfusion and nitric oxide perspective on healthspan》论文发表、《Inhibition of Ferroptosis Delays Aging and Extends Healthspan Across Multiple Species》论文发表、《Multimodal clocks of human aging》论文发表。
第132轮补录来源：神经调控与记忆增强；新增 《Deep Brain Stimulation: From Antidepressants to Memory Enhancement》论文发表、《Computational memory capacity predicts aging and cognitive decline》论文发表、《Cellular senescence in brain aging and cognitive decline》论文发表、《DeepPLL: Synchronization of non-invasive brain stimulation to deep brain stimulation》论文发表、《Pairing non-invasive brain stimulation with memory reactivation: rapid learning (and unlearning) in the human brain》论文发表。
第133轮补录来源：线粒体与代谢重编程；新增 《Mitochondrial-derived vesicles in metabolism, disease, and aging》论文发表、《Mitochondrial GTP metabolism controls reproductive aging in C. elegans》论文发表、《The mitochondrial integrated stress response: A novel approach to anti-aging and pro-longevity》论文发表、《Unraveling the interplay between sleep, redox metabolism, and aging: implications for brain health and longevity》论文发表、《The mitochondrial unfolded protein response regulates hippocampal neural stem cell aging》论文发表。
第134轮补录来源：免疫衰老与疫苗接种；新增 《Conquering aging-related immunosenescence and tumor immune escape》论文发表、《Immunosenescence in prostate cancer: from aging-related immune dysfunction to therapeutic opportunities》论文发表、《The 3 I’s of immunity and aging: immunosenescence, inflammaging, and immune resilience》论文发表、《CD300f immune receptor contributes to healthy aging by regulating inflammaging, metabolism, and cognitive decline》论文发表、《Immune Resilience: Rewriting the Rules of Healthy Aging》论文发表。
第135轮补录来源：类器官与器官芯片；新增 《A human autoimmune organoid model reveals IL-7 function in coeliac disease》论文发表、《Advances in Biliary Disease Organoid Research: From Model Construction to Clinical Applications》论文发表、《Optimization of Vascularized Intestinal Organoid Model》论文发表、《Vascular organoid model of Hutchinson-Gilford progeria syndrome uncovers repression of the SRF pathway in premature aging》论文发表、《Understanding Immune-Driven Brain Aging by Human Brain Organoid Microphysiological Analysis Platform》论文发表。
第136轮补录来源：干细胞与再生医学；新增 《Stem Cell Aging and Rejuvenation in the Skeletal Muscle System》论文发表、《Brain aging and rejuvenation at single-cell resolution》论文发表、《Hallmarks of stem cell aging》论文发表、《DNA methylation controls hematopoietic stem cell aging》论文发表、《Trained immunity links hematopoietic stem cell aging to aging-associated inflammation》论文发表。
第137轮补录来源：低温保存与玻璃化；新增 《Developing physical protocols for human organ scale vitrification and rewarming》论文发表、《Organ cryopreservation by vitrification and rapid rewarming: new breakthroughs in transplantation》论文发表、《IS OVARIAN TISSUE CRYOPRESERVATION WIDELY ACCESSIBLE?》论文发表、《Clinical dilemmas in ovarian tissue cryopreservation》论文发表、《ASSESSING KNOWLEDGE AMONG OVARIAN TISSUE CRYOPRESERVATION PATIENTS》论文发表。
第138轮补录来源：数字孪生与个体化健康建模；新增 《Towards a multi-organ, multi-omics medical digital twin》论文发表、《Patient-Centric Digital Twin Framework with Hybrid Knowledge Distillation for Federated Class-Incremental Learning in Precision Medicine》论文发表、《Digital twin for personalized medicine development》论文发表、《Digital twin technologies in prostate cancer as a frontier for precision medicine》论文发表、《Integrated Patient Digital and Biomimetic Twins for Precision Medicine: A Perspective》论文发表。
第139轮补录来源：AI 药物发现与临床转化；新增 《Artificial intelligence in drug discovery》论文发表、《Artificial intelligence for natural product drug discovery》论文发表、《Physics-based machine learning for enhanced drug formulation development》论文发表、《Machine learning models for drug-drug interaction prediction from computational discovery to clinical application》论文发表、《Deep learning in image-based phenotypic drug discovery》论文发表。
第140轮补录来源：长寿医学监管与终点设计；新增 《The role of quality of life data as an endpoint for collecting real-world evidence within geroscience clinical trials》论文发表、《NIA Translational Geroscience Network: An infrastructure to facilitate geroscience‐guided clinical trials》论文发表、《Geroscience》论文发表、《Advancing Geroscience Research - A Scoping Review of Regulatory Environments for Gerotherapeutics》论文发表、《Revisiting metformin as a geroprotector》论文发表。
第141轮补录来源：表观遗传时钟跨人群验证；新增 《An epigenetic clock in plants》论文发表、《Epigenetic clock work ticks forward》论文发表、《An evolutionary epigenetic clock in plants》论文发表、《Efficient epigenetic clock measurements with TIME-seq》论文发表、《Epigenetic Clock Analysis of Sex Chromosome Aneuploidies》论文发表。
第142轮补录来源：蛋白质稳态与自噬；新增 《Astrocytic proteostasis in the tale of aging and neurodegeneration》论文发表、《Autophagy, aging, and age-related neurodegeneration》论文发表、《Proteostasis and neurodegeneration: a closer look at autophagy in Alzheimer's disease》论文发表、《Karyopherins in proteostasis and aging》论文发表、《Endolysosomal dysfunction impairs proteostasis and induces neurodegeneration in vivo》论文发表。
第143轮补录来源：细胞衰老清除与 senolytics；新增 《Senolytics target cellular senescence — but can they slow aging?》论文发表、《Aging, Cellular Senescence, and Glaucoma》论文发表、《Increased cellular senescence in doxorubicin-induced murine ovarian injury: effect of senolytics》论文发表、《Sex, senescence, senolytics, and cognition》论文发表、《Cellular senescence in brain aging and neurodegeneration》论文发表。
第144轮补录来源：脑机接口与言语解码；新增 《Unlocking Naturalistic Speech With Brain‐Computer Interface》论文发表、《An EEG-EMG-Based Hybrid Brain–Computer Interface for Decoding Tones in Silent and Audible Speech》论文发表、《Real-time decoding of full-spectrum Chinese using brain-computer interface》论文发表、《Cross-subject decoding of human neural data for speech brain computer interfaces》论文发表、《Decoding cortical responses from visual input using an endovascular brain–computer interface》论文发表。
第145轮补录来源：神经形态计算与活性算力；新增 《Emerging Iontronic Neural Devices for Neuromorphic Sensory Computing》论文发表、《Neuromorphic computing paradigms enhance robustness through spiking neural networks》论文发表、《Oscillatory Neural Network with Tunable Frequency for Brain-Inspired Neuromorphic Computing》论文发表、《Biocomputing with organoid intelligence》论文发表、《Brain organoid reservoir computing for artificial intelligence》论文发表。
第146轮补录来源：纳米医学与药物递送；新增 《Oral delivery of nanomedicine for genetic kidney disease》论文发表、《Music enhances lipid nanoparticle brain delivery and mRNA transfection in brain cells》论文发表、《H-ferritin nanoparticle-mediated antibody delivery across the blood-brain barrier》论文发表、《Ionic Liquid Coating‐Driven Nanoparticle Delivery to the Brain: Applications for NeuroHIV》论文发表、《Intracerebral Nanoparticle Transport Facilitated by Alzheimer Pathology and Age》论文发表。
第147轮补录来源：生物打印与器官重建；新增 《Bioprinted Scaffold Remodels the Neuromodulatory Microenvironment for Enhancing Bone Regeneration》论文发表、《A 3D bioprinted adhesive tissue engineering scaffold to repair ischemic heart injury》论文发表、《3D bioprinting of emulating homeostasis regulation for regenerative medicine applications》论文发表、《Advances in 3D bioprinting for regenerative medicine applications》论文发表、《3D bioprinted organ-on-chips》论文发表。
第148轮补录来源：异种移植与器官可及性；新增 《Milestones on the path to clinical pig organ xenotransplantation》论文发表、《Is Allosensitization Detrimental to Pig Organ Xenotransplantation, and Is Xenosensitization Detrimental to Subsequent Organ Allotransplantation? A Debate Organized by the International Xenotransplantation Association (IXA)》论文发表、《Proteomic Insights Into Organ-Specific and Shared Dynamics in Pig-to-Human Xenotransplantation》论文发表、《Renin‐Angiotensin‐Aldosterone System (RAAS) in Pig‐to‐Baboon Kidney Xenotransplantation—Relevance to Clinical Pig Kidney Xenotransplantation》论文发表、《Gene-Edited Pig Kidney Xenotransplants in Humans: Record Survival and Mechanistic Insights》论文发表。
第149轮补录来源：生殖保存与未来选择权；新增 《FERTILITY BENEFIT SATISFACTION IN THE PHYSICIAN WORKFORCE: THE IMPACT OF EMPLOYER FERTILITY AND OOCYTE CRYOPRESERVATION COVERAGE》论文发表、《OOCYTE CRYOPRESERVATION OUTCOMES IN ONCOFERTILITY PATIENTS COMPARED TO THOSE UNDERGOING PLANNED OOCYTE CRYOPRESERVATION》论文发表、《P-398 Elective Oocyte Cryopreservation – a viable alternative as a means of fertility preservation》论文发表、《Oocyte cryopreservation for fertility preservation in transgender and gender diverse individuals: a SWOT analysis》论文发表、《Is planned oocyte cryopreservation delivering?》论文发表。
第150轮补录来源：脑保存与连接组；新增 《Network statistics of the whole-brain connectome of Drosophila》论文发表、《Whole-brain phenotype mapping between humans and mice》论文发表、《Brain-wide neuronal circuit connectome of human glioblastoma》论文发表、《Proteomic comparison of human brain tissue preservation methods》论文发表、《Optimization of Brain Tissue Preservation for Nucleic Acid Stability》论文发表。
第151轮补录来源：长寿产业资金与转化组织；新增 《Clinical research on extreme longevity: The FACET experience》论文发表、《Mucosal TLR5 activation controls healthspan and longevity》论文发表、《Isoleucine dietary restriction boosts healthspan and longevity in mice》论文发表、《Defining a longevity biotechnology company》论文发表、《The Longevity Med Summit: insights on healthspan from cell to society》论文发表。
第152轮补录来源：长寿转化研究基础设施；新增 《Enabling translational geroscience by broadening the scope of geriatric care》论文发表、《Artificial intelligence across the aging continuum: Mechanistic geroscience, therapeutic innovation, and clinical impact》论文发表、《Translational Geroscience Strategies for Delaying Multimorbidity》论文发表、《Translational Geroscience: Human Models of Healthy Aging and Longevity》论文发表、《Aging Cell and the growing pains of translational geroscience》论文发表。
第153轮补录来源：脑机接口长期随访与居家使用；新增 《Novel AIRTrode-based wearable electrode supports long-term, online brain–computer interface operations》论文发表、《Brain-computer interface commercialization》论文发表、《An Interventional Brain-Computer Interface for Long-Term EEG Collection and Motion Classification of a Quadruped Mammal》论文发表、《Visual tracking brain-computer interface》论文发表、《Intracortical brain-computer interface for navigation in virtual reality in macaque monkeys》论文发表。
第154轮补录来源：AI 自动化科研与材料发现；新增 《Discovery of tunable and soluble organic emitters for solid-state lasers with a self-driving laboratory》论文发表、《Digital twins for self-driving chemistry laboratories》论文发表、《Autonomous experimentation systems for materials development: A community perspective》论文发表、《Self-Driving Laboratory for Polymer Electronics》论文发表、《A review of large language models and autonomous agents in chemistry》论文发表。
第155轮补录来源：生物年龄跨人群校准；新增 《SECOND-GENERATION SPERM EPIGENETIC CLOCK ESTIMATES SPERM BIOLOGICAL AGE AND PREDICTS TIME-TO-PREGNANCY IN A GENERAL POPULATION COHORT》论文发表、《Biological age construction for prediction of mortality in the Chinese population》论文发表、《Difference between Biological Age and Chronological Age Predicts Mortality and Hospitalization in a Longitudinal Adult Cohort》论文发表、《Associations between shift work and biological age acceleration: A population-based study》论文发表、《Biological age acceleration, longitudinal change and mortality risk in the Dutch Lifelines cohort》论文发表。
第156轮补录来源：活性算力与合成智能治理；新增 《Ethics need to keep up with human brain organoid research》论文发表、《Organoid intelligence (OI): the new frontier in biocomputing and intelligence-in-a-dish》论文发表、《The Ethics of Human Brain Organoid Transplantation in Animals》论文发表、《Consciousness and the Ethics of Human Brain Organoid Research》论文发表、《Human Brain Organoid Transplantation: Testing the Foundations of Animal Research Ethics》论文发表。
第157轮补录来源：器官灌注与移植结局；新增 《Hypothermic Machine Perfusion in Liver Transplantation — A Randomized Trial》论文发表、《Normothermic Machine Perfusion Increases Donor Liver Use》论文发表、《Portable hypothermic oxygenated machine perfusion for organ preservation in liver transplantation: A randomized, open-label, clinical trial》论文发表、《Normothermic Machine Perfusion: Transforming "Unacceptable" Liver Transplants into Reality》论文发表、《Automated Hypothermic Machine Perfusion for Donor Kidney Preservation》论文发表。
第158轮补录来源：老年权利与健康老龄化政策；新增 《Structural Ageism and the Health of Older Adults》论文发表、《Experiences of Everyday Ageism and the Health of Older US Adults》论文发表、《The Capability Approach and the WHO healthy ageing framework (for the UN Decade of Healthy Ageing)》论文发表、《The Decade of Healthy Ageing: progress and challenges ahead》论文发表、《Decade of healthy ageing in Asia》论文发表。
第159轮补录来源：生物年龄指标监管接受度；新增 《Is taurine an aging biomarker?》论文发表、《Regulatory Roles of Exosomes in Aging and Aging-Related Diseases》论文发表、《NfL makes regulatory debut as neurodegenerative disease biomarker》论文发表、《The Aging Biomarker Consortium represents a new era for aging research in China》论文发表、《The clinical trial landscape of osteosarcoma: integrating trial data, immunotherapeutic trends, and biomarker insights》论文发表。
第160轮补录来源：AI 药物管线与临床失败教训；新增 《AI-enabled drug discovery reaches clinical milestone》论文发表、《Machine learning in drug delivery》论文发表、《Machine learning in drug discovery》论文发表、《Artificial intelligence in drug development》论文发表、《DrugnomeAI is an ensemble machine-learning framework for predicting druggability of candidate drug targets》论文发表。
第161轮补录来源：细胞重编程与临床转化；新增 《Partial cellular reprogramming: A deep dive into an emerging rejuvenation technology》论文发表、《Cellular plasticity in reprogramming, rejuvenation and tumorigenesis: a pioneer TF perspective》论文发表、《Conserved biological processes in partial cellular reprogramming: Relevance to aging and rejuvenation》论文发表、《Cellular reprogramming beyond pluripotency》论文发表、《Mechanisms, pathways and strategies for rejuvenation through epigenetic reprogramming》论文发表。
第162轮补录来源：人工器官与生命维持；新增 《Clinical Outcomes of Left Ventricular Assist Device Pump Infection》论文发表、《Impact of Frailty on Left Ventricular Assist Device Clinical Outcomes》论文发表、《Mechanical circulatory support in patients with congenital heart disease: a European Registry for Patients with Mechanical Circulatory Support》论文发表、《Clinical outcomes of modified left ventricular assist device driveline management》论文发表、《Sex-based differences in left ventricular assist device clinical outcomes》论文发表。
第163轮补录来源：健康老龄化治理与失能压缩；新增 《Pace of aging matters for healthspan and lifespan in older adults》论文发表、《The Decade of Healthy Ageing: progress and challenges ahead》论文发表、《Power to prolong independence and healthy ageing in older adults》论文发表、《Healthy ageing in older adults with cardiovascular disease》论文发表、《Improving oral health of older adults for healthy ageing》论文发表。
第164轮补录来源：长寿医学临床实践；新增 《Advances in clinical application of lipidomics in healthy ageing and healthy longevity medicine》论文发表、《Beyond the linear genome: how reference bias threatens preventive medicine and geroscience》论文发表、《Healthspan as a Clinical Outcome: Reframing Longevity in Modern Medicine》论文发表、《Science of longevity medicine》论文发表、《Toward responsible longevity medicine: Swiss framework for healthy longevity medicine clinics》论文发表。
第165轮补录来源：再生医学转化与细胞疗法；新增 《Agonal cell resuscitation strategy to promote tissue repair》论文发表、《Stem cell-derived exosome versus stem cell therapy》论文发表、《Challenges in the Clinical Translation of Exosomal Therapy in Regenerative Medicine》论文发表、《Clinical Trial Landscape of Stem Cell Therapy for Peripheral Arterial Disease》论文发表、《Biodegradable polyurethane scaffolds in regenerative medicine: Clinical translation review》论文发表。
第166轮补录来源：数字遗产与数字永生；新增 《Ready or not, the digital afterlife is here》论文发表、《The law of digital afterlife: the Chinese experience of AI "resurrection" and "grief tech"》论文发表、《Digital Access, Digital Literacy, and Afterlife Preparedness: Societal Contexts of Digital Afterlife Traces》论文发表、《Digital afterlife leaders: professionalisation as a social innovation in the digital afterlife industry》论文发表、《Personal digital legacy preservation by libraries》论文发表。
第167轮补录来源：神经技术与脑数据权利；新增 《Applying the IEEE BRAIN neuroethics framework to intra-cortical brain-computer interfaces》论文发表、《Privacy Challenges to the Democratization of Brain Data》论文发表、《Brain Data in Context: Are New Rights the Way to Mental and Brain Privacy?》论文发表、《Neurorights in the Constitution: from neurotechnology to ethics and politics》论文发表、《Neurorights in neurology》论文发表。
第168轮补录来源：认知训练与注意力增强；新增 《Effective engagement in computerized cognitive training for older adults》论文发表、《Mindfulness Training and Exercise and Cognitive Function in Older Adults》论文发表、《Mindfulness Training and Exercise and Cognitive Function in Older Adults—Reply》论文发表、《Digital cognitive training for functionality in mild cognitive impairment: a randomized controlled clinical trial》论文发表、《Primary outcome from the augmenting cognitive training in older adults study (ACT): A tDCS and cognitive training randomized clinical trial》论文发表。
第169轮补录来源：睡眠与昼夜节律；新增 《Sleep health in the older adults: Architecture, circadian changes, and common sleep disorders》论文发表、《A familial natural short sleep mutation in dec2 extends healthspan and lifespan in Drosophila》论文发表、《Global Healthspan Summit 2023: closing the gap between healthspan and lifespan》论文发表、《Sleep health and aging: Recommendations for promoting healthy sleep among older adults: A National Sleep Foundation report》论文发表、《The circadian rhythm: A key variable in aging?》论文发表。
第170轮补录来源：环境暴露与表观衰老；新增 《Epigenetic Aging and Racialized, Economic, and Environmental Injustice》论文发表、《Associations between environmental air pollution, greenspace and apparent biological aging: a cross-sectional study》论文发表、《Impact of air pollution on cardiovascular aging》论文发表、《Air pollution and impulsive choice in aging: evidence from delay discounting》论文发表、《Exposome and unhealthy aging: environmental drivers from air pollution to occupational exposures》论文发表。
第171轮补录来源：生殖医学与生育力维护；新增 《Perspectives on biomarkers of reproductive aging for fertility and beyond》论文发表、《Obesity, Fertility, and Reproductive Health Across the Life Course》论文发表、《Seminal fluid cytokines in reproductive health and fertility of men》论文发表、《Fertility preservation and mental health among cancer patients of reproductive age》论文发表、《Polyamine metabolite spermidine rejuvenates oocyte quality by enhancing mitophagy during female reproductive aging》论文发表。
第172轮补录来源：微生物组与免疫代谢；新增 《Aging Gut Microbiome in Healthy and Unhealthy Aging》论文发表、《Polystyrene nanoplastics promotes inflammation and aging in young mice through the oral-gut microbiome axis》论文发表、《The Gut Microbiome and Aging》论文发表、《Gut Instincts: The Gut Microbiome-Cardiovascular Inflammation Axis》论文发表、《Effect of Gut Microbiota-Mediated Tryptophan Metabolism on Inflammaging in Frailty and Sarcopenia》论文发表。
第173轮补录来源：心血管衰老与循环韧性；新增 《Semaglutide Improves Heart Failure and Cardiovascular Disease》论文发表、《Intravenous iron therapy reduces cardiovascular events in heart failure》论文发表、《Arterial stiffness and vascular aging: mechanisms, prevention, and therapy》论文发表、《Cardiovascular Aging and Exercise: Implications for Heart Failure Prevention and Management》论文发表、《Cardiovascular Aging》论文发表。
第174轮补录来源：骨骼肌肉与身体功能；新增 《Sarcopenia in Older Adults》论文发表、《Blocking myostatin: muscle mass equals muscle strength?》论文发表、《Muscle mass, muscle strength and the renin-angiotensin system》论文发表、《Physical Frailty: A Biological Marker of Aging?》论文发表、《Structured horticultural therapy enhances muscle strength and mass in aging women at risk of sarcopenia》论文发表。
第175轮补录来源：癌症与衰老相关疾病；新增 《NFATC1 dysfunction-triggered MSC senescence induces tooth aging amenable to senolytic therapy》论文发表、《Aging, Cellular Senescence, and Glaucoma》论文发表、《Exosomal dynamics: Bridging the gap between cellular senescence and cancer therapy》论文发表、《Cellular Senescence: Aging, Cancer, and Injury》论文发表、《The aging tumor metabolic microenvironment》论文发表。
第176轮补录来源：神经退行与阿尔茨海默；新增 《Alzheimer Disease Pathology and Neurodegeneration in Midlife Obesity: A Pilot Study》论文发表、《Advanced structural brain aging in preclinical autosomal dominant Alzheimer disease》论文发表、《Resilience and Resistance in Aging and Alzheimer Disease》论文发表、《Role of primary aging hallmarks in Alzheimer's disease》论文发表、《Harnessing Brain Pathology for Dementia Prevention》论文发表。
第177轮补录来源：代谢营养与禁食；新增 《Circadian clocks and periodic anticipated fasting prevent fasting-associated hepatic steatosis in calorie restriction》论文发表、《Neurotrophic effects of intermittent fasting, calorie restriction and exercise: a review and annotated bibliography》论文发表、《Brain responses to intermittent fasting and the healthy living diet in older adults》论文发表、《Dietary and pharmacological energy restriction and exercise for healthspan extension》论文发表、《Dietary restriction of isoleucine increases healthspan and lifespan of genetically heterogeneous mice》论文发表。
第178轮补录来源：心理韧性与社会支持；新增 《Psychological Resilience and Frailty Progression in Older Adults》论文发表、《Effects of social support on cognitive frailty among the older adults in China: mediation of psychological resilience and moderated mediation of education》论文发表、《Social Isolation and Loneliness in Older Adults》论文发表、《Loneliness and Social Isolation Among US Older Adults》论文发表、《RETRACTED: Personality Traits and Social Isolation in Older Adults》论文发表。
第179轮补录来源：照护劳动力与长期照护；新增 《Post–Intensive Care Syndrome and Caregiver Burden》论文发表、《Use of Caregiving Support Services Among Diverse Dementia Caregivers by Geographic Context》论文发表、《Empowering a person-centered long-term care workforce》论文发表、《Providing long-term care: Options for a better workforce》论文发表、《Influence of caregiver burden on well-being of family member caregivers of older adults》论文发表。
第180轮补录来源：住房与社区环境；新增 《LGBTQ older adults deserve safe and affirming housing》论文发表、《Health and Economic Impacts of Stable Housing Provision for Older Adults》论文发表、《Neighborhood environment and older adults' mental wellbeing and cognition: mediating role of activity variety》论文发表、《If You've Seen One Age-Friendly Community, You've Seen One Age-Friendly Community》论文发表、《Urban environment and mental wellbeing in Belgian older adults by neighborhood income level》论文发表。
第181轮补录来源：健康数据互操作；新增 《Patient-Centered Data Home: A Path Towards National Interoperability》论文发表、《Utilization of an Electronic Health Record Embedded Enterprise Health Data Exchange: A Single Institute Experience》论文发表、《Automating Electronic Health Record Data Quality Assessment》论文发表、《Electronic health record data for antimicrobial prescribing》论文发表、《MediTrans—Patient-centric interoperability through blockchain》论文发表。
第182轮补录来源：隐私与神经数据治理；新增 《Synthetic Data and Health Privacy》论文发表、《Toward owner governance in genomic data privacy with Governome》论文发表、《Health data justice: building new norms for health data governance》论文发表、《Data Governance and Distribution of Biobank: A Case from a Chinese Cancer Hospital》论文发表、《Prospective study design and data analysis in UK Biobank》论文发表。
第183轮补录来源：气候灾害韧性；新增 《Climate Change and Mental Health》论文发表、《Addressing the Health Impacts of Climate Change in Older Adults》论文发表、《Climate Change, Extreme Heat, and Health》论文发表、《Factors influencing disaster preparedness behaviors of older adults》论文发表、《Addressing the Health Risks of Climate Change in Older Adults》论文发表。
第184轮补录来源：开放科学可复现；新增 《Reproducibility and robustness of economics and political science research》论文发表、《Balancing ethical data sharing and open science for reproducible research in biomedical data science》论文发表、《Reproducibility Failure in Biomedical Research: Problems and Solutions》论文发表、《Biomedical researchers' perspectives on the reproducibility of research》论文发表、《Recommendations to enhance rigor and reproducibility in biomedical research》论文发表。
第185轮补录来源：功能指标与患者报告结局；新增 《Associations between days spent at home and <scp>patient‐reported</scp> outcomes among frail older adults》论文发表、《Differences in phenotypic and functional aging trajectories among people aging with disability and the US general population》论文发表、《Disability: measurement matters》论文发表、《Handgrip Strength Asymmetry and Weakness Together Are Associated With Functional Disability in Aging Americans》论文发表、《Oral Health-Related Quality Of Life In Older Adults》论文发表。
第186轮补录来源：安宁疗护与死亡质量；新增 《Palliative care use in Taiwanese older adults》论文发表、《Advance Care Planning, End-of-Life Preferences, and Burdensome Care》论文发表、《Palliative care considerations in frail older adults》论文发表、《Palliative care for older adults with cardiovascular disease》论文发表、《Hospice and Palliative Care》论文发表。
第187轮补录来源：生命伦理与身份连续性；新增 《Personal identity is social identity》论文发表、《Self-identity and personal identity》论文发表、《Is personal identity intransitive?》论文发表、《Narrative and Personal Identity》论文发表、《Personal Identity and National Identity: An Analogy》论文发表。
第188轮补录来源：长寿逃逸速度理论；新增 《Implausibility of radical life extension in humans in the twenty-first century》论文发表、《Healthspan versus lifespan: new medicines to close the gap》论文发表、《Healthspan-lifespan gap differs in magnitude and disease contribution across world regions》论文发表、《The Ethics of Radical Life Extension: Catholic, Protestant, Orthodox Christian, and Global Ethic Perspectives》论文发表、《Forever is Always Finite: Reflections on Radical Life Extension》论文发表。
第189轮补录来源：合成生物学生物安全；新增 《Synthetic biology》论文发表、《Quantitative synthetic biology》论文发表、《Decoding the origins of cellular self-organization for engineered biology》论文发表、《Exploring the Application and Prospects of Synthetic Biology in Engineered Living Materials》论文发表、《Building biosecurity for synthetic biology》论文发表。
第190轮补录来源：纳米机器与分子修复；新增 《Technology Roadmap of Micro/Nanorobots》论文发表、《Janus Micro/Nanorobots in Biomedical Applications》论文发表、《AI-enhanced biomedical micro/nanorobots in microfluidics》论文发表、《Microenvironment-responsive nanorobots for biomedical applications》论文发表、《Micro/nanomotors in targeted drug delivery: Advances, challenges, and future directions》论文发表。
第191轮补录来源：脑机接口运动重建；新增 《Decoding motor plans using a closed-loop ultrasonic brain–machine interface》论文发表、《A Novel Brain–Computer Interface Application: Precise Decoding of Urination and Defecation Motor Attempts in Spinal Cord Injury Patients》论文发表、《Feasibility of decoding cerebellar movement-related potentials for brain-computer interface applications》论文发表、《Decoding trajectories of imagined hand movement using electrocorticograms for brain–machine interface》论文发表、《Motor Imagery Hand Movement Direction Decoding Using Brain Computer Interface to Aid Stroke Recovery and Rehabilitation》论文发表。
第192轮补录来源：脑保存与意识伦理；新增 《Cryonics for all?》论文发表、《Cryonics: Traps and transformations》论文发表、《Selective Optimism about Mind-Uploading》论文发表、《Mind Uploading and Embodied Cognition: A Theological Response》论文发表、《The ethics of preservation: Balancing clinical utility and duty in catastrophic brain injury》论文发表。
第193轮补录来源：数字孪生预测医学；新增 《Neurosymbolic Digital Twin for Cardiovascular Disease Prediction and Personalized Modeling》论文发表、《DECIDE-Twin: A Framework for AI-Enabled Digital Twins in Clinical Decision-Making》论文发表、《A digital twin model for evidence-based clinical decision support in multiple myeloma treatment》论文发表、《Hybrid disease prediction approach leveraging digital twin and metaverse technologies for health consumer》论文发表、《Rheumatic Digital Twin: Proposed Machine Learning–Based Multimodal Framework to Inform Clinical Decision-Making》论文发表。
第194轮补录来源：细胞衰老组织特异性；新增 《Tissue Fibrosis Decoded via Cellular Senescence: Mechanisms, Treatments, and Emerging Technologies》论文发表、《Hydrogel-based senomorphic approaches to modulate cellular senescence and promote tissue rejuvenation》论文发表、《Hypertension and cellular senescence》论文发表、《Cellular senescence and glaucoma》论文发表、《Cellular senescence in ischemic stroke: Cell-type specificity, temporal dynamics, and response to therapeutic interventions》论文发表。
第195轮补录来源：线粒体生物能量学；新增 《Differential mitochondrial bioenergetics and cellular resilience in astrocytes, hepatocytes, and fibroblasts from aging baboons》论文发表、《Sex-specific decline in prefrontal cortex mitochondrial bioenergetics in aging baboons correlates with walking speed》论文发表、《Mitochondrial function and phenotype are defined by bioenergetics》论文发表、《Mitochondrial quality control in human ageing and longevity》论文发表、《Mitochondrial respiratory supercomplexes associated with longevity in mammals》论文发表。
第196轮补录来源：免疫代谢疫苗；新增 《Immunometabolism In Brain Aging and Neurodegeneration: Bridging Metabolic Pathways and Immune Responses》论文发表、《Immunometabolism and oxidative stress: roles and therapeutic strategies in cancer and aging》论文发表、《Diet switch pre-vaccination improves immune response and metabolic status in formerly obese mice》论文发表、《Obesity Dysregulates the Immune Response to Influenza Infection and Vaccination Through Metabolic and Inflammatory Mechanisms》论文发表、《Metabolic mediators: How immunometabolism directs the immune response to infection》论文发表。
第197轮补录来源：蛋白质稳态蛋白病；新增 《Glial-derived mitochondrial signals affect neuronal proteostasis and aging》论文发表、《Central role of the ER proteostasis network in healthy aging》论文发表、《Aging-associated modulation of UFMylation impairs proteostasis in C. elegans》论文发表、《Moderately cold temperatures prevent protein aggregation related to aging and disease》论文发表、《The aging factor EPS8 induces disease-related protein aggregation through RAC signaling hyperactivation》论文发表。
第198轮补录来源：干细胞组织修复；新增 《Bioengineered human tissue regeneration and repair using endogenous stem cells》论文发表、《Regenesis: Repair and regeneration reinvented in stem cell therapeutics》论文发表、《Apoptotic dysregulation mediates stem cell competition and tissue regeneration》论文发表、《Stem cell therapy might improve aging frailty》论文发表、《Mitochondrial drivers of stem cell aging and inflammaging》论文发表。
第199轮补录来源：器官芯片疾病模型；新增 《Organ-on-chip models for infectious disease research》论文发表、《An eighteen-organ microphysiological system coupling a vascular network and excretion system for drug discovery》论文发表、《Heart-on-a-chip: a revolutionary organ-on-chip platform for cardiovascular disease modeling》论文发表、《Application of Microphysiological Systems to Enhance Safety Assessment in Drug Discovery》论文发表、《Microfluidic Organ-on-a-Chip Models of Human Intestine》论文发表。
第200轮补录来源：综合证据治理与门禁；新增 《Rethinking research reproducibility》论文发表、《Reproducibility in Plant Research》论文发表、《Research Lifecycle Management: Using Analysis Reproducibility Research Software to Define Contextual Data Governance Policies》论文发表、《Reproducibility in chemistry research》论文发表、《Adaptive data governance for research data management》论文发表。
第201轮补录来源：帕金森细胞疗法；新增 《Gene therapy zeroes in on Parkinson disease brain circuits》论文发表、《New Addition to Parkinson Therapy》论文发表、《Long-term Clinical Outcomes After Fetal Cell Transplantation in Parkinson Disease》论文发表、《Multiplying Messages LRRK beneath Parkinson Disease》论文发表、《Research Yields Clues to Improving Cell Therapy for Parkinson Disease》论文发表。
第202轮补录来源：心脏再生与心肌修复；新增 《Single-cell chromatin accessibility landscape of cardiac non-myocytes identifies tissue repair program during heart regeneration》论文发表、《Epicardial FSTL1 reconstitution regenerates the adult mammalian heart》论文发表、《Transient Regenerative Potential of the Neonatal Mouse Heart》论文发表、《Mending broken hearts: cardiac development as a basis for adult heart regeneration and repair》论文发表、《Cellular Senescence Affects Cardiac Regeneration and Repair in Ischemic Heart Disease》论文发表。
第203轮补录来源：肺再生与慢性肺病；新增 《Versican expression from lung fibroblasts suppresses pulmonary fibrosis》论文发表、《Lung cell transplantation for pulmonary fibrosis》论文发表、《Hippo signaling impairs alveolar epithelial regeneration in pulmonary fibrosis》论文发表、《Ziritaxestat and Lung Function in Idiopathic Pulmonary Fibrosis》论文发表、《Atf3 defines a population of pulmonary endothelial cells essential for lung regeneration》论文发表。
第204轮补录来源：肝脏再生与肝病逆转；新增 《Molecular mechanisms in liver repair and regeneration: from physiology to therapeutics》论文发表、《Hepatic Snai1 and Snai2 promote liver regeneration and suppress liver fibrosis in mice》论文发表、《Human hepatocyte transplantation for liver disease: current status and future perspectives》论文发表、《Liver regeneration: from myth to mechanism》论文发表、《Clinical Implications of Advances in the Basic Science of Liver Repair and Regeneration》论文发表。
第205轮补录来源：肾脏再生与透析替代；新增 《ENPP1 blockade with a humanized monoclonal antibody enhances renal repair after acute kidney injury》论文发表、《3D Bioprinted Renal Constructs Using Kidney‐Specific ECM Bioink System on Kidney Regeneration》论文发表、《Collagen V regulates renal function after kidney injury and can be pharmacologically targeted to enhance kidney repair in mice》论文发表、《Proenkephalin-A secreted by renal proximal tubules functions as a brake in kidney regeneration》论文发表、《Kidney Regeneration: Lessons from Development》论文发表。
第206轮补录来源：胰岛细胞移植与糖尿病逆转；新增 《Islet organoids: a new hope for islet transplantation in diabetes》论文发表、《Revolutionizing islet transplantation with a preconditioning boost for beta cell survival》论文发表、《TRPC3 Regulates Islet Beta‐Cell Insulin Secretion》论文发表、《Islet transplantation: Current status and future directions》论文发表、《Warm ischemia time influences human islet cell isolation yield when assessed as beta cell number but not as islet equivalent number》论文发表。
第207轮补录来源：脊髓损伤修复与神经再生；新增 《NG2 glia reprogramming induces robust axonal regeneration after spinal cord injury》论文发表、《Regulation of axonal regeneration after mammalian spinal cord injury》论文发表、《Chondroitinase ABC promotes functional recovery after spinal cord injury》论文发表、《Summary Statement: Repair of the Injured Spinal Cord》论文发表、《The roles of neural stem cells in myelin regeneration and repair therapy after spinal cord injury》论文发表。
第208轮补录来源：周围神经再生；新增 《3’UTR regulation of axon translation and optic nerve regeneration》论文发表、《GFRα1 Promotes Axon Regeneration after Peripheral Nerve Injury by Functioning as a Ligand》论文发表、《In Vitro Models for Peripheral Nerve Regeneration》论文发表、《Scaffold design considerations for peripheral nerve regeneration》论文发表、《Mature but not developing Schwann cells promote axon regeneration after peripheral nerve injury》论文发表。
第209轮补录来源：软骨与骨再生；新增 《Functional Hydrogel Interfaces for Cartilage and Bone Regeneration》论文发表、《Bone Tissue Engineering: State of the Art and Future Trends》论文发表、《Advances in graphene-based 2D materials for tendon, nerve, bone/cartilage regeneration and biomedicine》论文发表、《Unlike Bone, Cartilage Regeneration Remains Elusive》论文发表、《Gene therapy for repair and regeneration of bone and cartilage》论文发表。
第210轮补录来源：皮肤再生与无瘢痕愈合；新增 《Promoting Treg Polarization‐Mediated Anti‐Scar and Appendage Regeneration in Wound Healing》论文发表、《Sprayable Nanocomposites Hydrogel for Wound Healing and Skin Regeneration》论文发表、《Wound healing in oral mucosa results in reduced scar formation as compared with skin: Evidence from the red Duroc pig model and humans》论文发表、《Regeneration of injured skin and peripheral nerves requires control of wound contraction, not scar formation》论文发表、《Wound Healing--Aiming for Perfect Skin Regeneration》论文发表。
第211轮补录来源：毛囊与感觉器官再生；新增 《Intermittent fasting triggers interorgan communication to suppress hair follicle regeneration》论文发表、《MCL‑1 safeguards activated hair follicle stem cells to enable adult hair regeneration》论文发表、《TLR2 regulates hair follicle cycle and regeneration via BMP signaling》论文发表、《Nanotechnology-based techniques for hair follicle regeneration》论文发表、《Immune modulation of hair follicle regeneration》论文发表。
第212轮补录来源：视网膜再生与视力恢复；新增 《Nanotherapy for Neural Retinal Regeneration》论文发表、《KIF11 UFMylation Maintains Photoreceptor Cilium Integrity and Retinal Homeostasis》论文发表、《Müller glia are a potential source of neural regeneration in the postnatal chicken retina》论文发表、《Retinal Regeneration in Mammals?》论文发表、《Invited Session II: Retinal remodeling and regeneration: Insights into retinal cell replacement: Optimising photoreceptor and RPE transplantation》论文发表。
第213轮补录来源：内耳毛细胞再生与听力恢复；新增 《Hair cell regeneration, reinnervation, and restoration of hearing thresholds in the avian hearing organ》论文发表、《The Notch ligand Jagged1 plays a dual role in cochlear hair cell regeneration》论文发表、《Dopamine-modified Ti3C2Tx MXene promotes supporting cell pluripotency and hair cell regeneration in cochlear organoid culture》论文发表、《Notch Inhibition Induces Cochlear Hair Cell Regeneration and Recovery of Hearing after Acoustic Trauma》论文发表、《Recent advances in cochlear hair cell regeneration—A promising opportunity for the treatment of age-related hearing loss》论文发表。
第214轮补录来源：胸腺再生与免疫重建；新增 《Thymus regeneration therapies: entering a new era》论文发表、《The alarmin IL33 orchestrates type 2 immune-mediated control of thymus regeneration》论文发表、《Immune Reconstitution in the Aging Host: Opportunities for Mechanism-Based Therapy in Allogeneic Hematopoietic Cell Transplantation》论文发表、《Innate Immune Reconstitution in Humanized Bone Marrow-Liver-Thymus (HuBLT) Mice Governs Adaptive Cellular Immune Function and Responses to HIV-1 Infection》论文发表、《Thymus Degeneration and Regeneration》论文发表。
第215轮补录来源：造血干细胞移植与血液重建；新增 《Advances in second hematopoietic stem cell transplantation》论文发表、《Growing and aging of hematopoietic stem cells》论文发表、《Hematopoiesis: An Evolving Paradigm for Stem Cell Biology》论文发表、《Hematopoietic stem cell aging: Mechanism and consequence》论文发表、《Aspartate availability limits hematopoietic stem cell function during hematopoietic regeneration》论文发表。
第216轮补录来源：间充质干细胞治疗；新增 《Advances and clinical challenges of mesenchymal stem cell therapy》论文发表、《Immunomodulatory role of mesenchymal stem cell therapy in liver fibrosis》论文发表、《Mesenchymal Stem Cells-based Cell-free Therapy Targeting Neuroinflammation》论文发表、《Mesenchymal Stem Cells: Mechanisms of Immunomodulation and Homing》论文发表、《Mesenchymal stromal cells: Putative microenvironmental modulators become cell therapy》论文发表。
第217轮补录来源：类器官疾病模型；新增 《Human organoid systems in modeling reproductive tissue development, function, and disease》论文发表、《Human organoids: model systems for human biology and medicine》论文发表、《Organogenesis in a dish: Modeling development and disease using organoid technologies》论文发表、《A scalable organoid model of human autosomal dominant polycystic kidney disease for disease mechanism and drug discovery》论文发表、《NEUBOrg: Artificially Induced Pluripotent Stem Cell-Derived Brain Organoid to Model and Study Genetics of Alzheimer’s Disease Progression》论文发表。
第218轮补录来源：3D生物打印器官；新增 《3D bioprinting of tissues and organs》论文发表、《3D Bioprinting for Organ Regeneration》论文发表、《Progress in 3D bioprinting technology for tissue/organ regenerative engineering》论文发表、《Tissue and Organ 3D Bioprinting》论文发表、《Current Developments in 3D Bioprinting for Tissue and Organ Regeneration–A Review》论文发表。
第219轮补录来源：器官芯片药物评价；新增 《Democratizing Organ‐On‐Chip Technologies With a Modular, Reusable, and Perfusion‐Ready Microphysiological System》论文发表、《Vascular microphysiological system as an organ preservation testbed》论文发表、《Reconstituting Organ-Level Lung Functions on a Chip》论文发表、《Microphysiological (“organ-on-a-chip”) models of pulmonary infections for developing novel anti-infectives》论文发表、《Microfluidic organs-on-chips》论文发表。
第220轮补录来源：异种器官移植临床；新增 《Genetically modified pig liver keeps man alive until human organ transplant》论文发表、《Clinical Kidney Xenotransplantation—Why Do We Not Transplant Both Pig Kidneys Into the Recipient?》论文发表、《Endothelial Injury and Fibrogenesis Drives Post-Transplant Response After Pig-to-Human Heart Xenotransplantation》论文发表、《How Much Will a Pig Organ Transplant Cost? A Preliminary Estimate of the Cost of Xenotransplantation Versus Allotransplantation in the USA》论文发表、《Two US surgical teams transplant functional pig kidneys into humans in xenotransplantation success》论文发表。
第221轮补录来源：器官灌注保存与移植前修复；新增 《Advancing Organ Preservation and Perfusion: Introducing the International Society of Organ Preservation and Perfusion Therapy (ISOPPT)》论文发表、《Crash course: organ perfusion technologies - improving the physiology of transplant preservation and creating opportunities for organ cryopreservation?》论文发表、《Endoplasmic and Vascular Surface Activation During Organ Preservation: Refining Upon the Benefits of Machine Perfusion》论文发表、《14. Hypothermic machine perfusion for organ preservation》论文发表、《Hypothermic perfusion preservation: The future of organ preservation revisited?》论文发表。
第222轮补录来源：深低温保存与玻璃化；新增 《Organ Cryopreservation by Vitrification: Challenges and Opportunities》论文发表、《Vitrification as a prospect for cryopreservation of tissue-engineered constructs》论文发表、《Ovarian tissue cryopreservation using vitrification and/or<i>in vitro</i>activated technology》论文发表、《Cryopreservation of porcine intact tibial plateau using vitrification》论文发表、《Cryopreservation of mesenchymal stromal cells spheroids by vitrification》论文发表。
第223轮补录来源：冷冻复苏与生物停滞；新增 《BIostasis: a transformative capability for human civilization》论文发表、《Cryonics Takes Another Big Step Toward the Mainstream》论文发表、《Brain Preservation and Cryonics Through the Lens of Moral Psychology》论文发表、《Biostasis: A Roadmap for Research in Preservation and Potential Revival of Humans》论文发表、《Frozen Bodies and Future Imaginaries: Assisted Dying, Cryonics, and a Good Death》论文发表。
第224轮补录来源：纳米医学与靶向药物递送；新增 《Nanoparticle therapeutics: an emerging treatment modality for cancer》论文发表、《Drug delivery and nanoparticles: Applications and hazards》论文发表、《Multifunctional nanoparticle–EpCAM aptamer bioconjugates: A paradigm for targeted drug delivery and imaging in cancer therapy》论文发表、《Tumor vascular-targeted co-delivery of anti-angiogenesis and chemotherapeutic agents by mesoporous silica nanoparticle-based drug delivery system for synergetic therapy of tumor》论文发表、《Curcumin-guided nanotherapy: a lipid-based nanomedicine for targeted drug delivery in breast cancer therapy》论文发表。
第225轮补录来源：纳米机器人生物医学；新增 《A Logic-Gated Nanorobot for Targeted Transport of Molecular Payloads》论文发表、《A DNA Nanorobot Uprises against Cancer》论文发表、《Design and Control of the Magnetically Actuated Micro/Nanorobot Swarm toward Biomedical Applications》论文发表、《Synchronous Rotation-Based Knot Tying on Mini-Incisions Using Dual-Arm Nanorobot》论文发表、《Nanorobot-Based Direct Implantation of Flexible Neural Electrode for BCI》论文发表。
第226轮补录来源：分子机器与DNA纳米技术；新增 《DNA origami: a history and current perspective》论文发表、《Folding DNA to create nanoscale shapes and patterns》论文发表、《A DNA-fuelled molecular machine made of DNA》论文发表、《DNA Nanotechnology: From DNA Nanotechnology to Material Systems Engineering (Adv. Mater. 26/2019)》论文发表、《Designed DNA molecules: principles and applications of molecular nanotechnology》论文发表。
第227轮补录来源：合成生物学与细胞编程；新增 《Integrating bioelectronics with cell-based synthetic biology》论文发表、《Programming of synthetic regulatory DNA for cell-type targeting in humans》论文发表、《Synthetic Organisms Simplify Biology》论文发表、《A Synthetic Bacterial Cell-Cell Adhesion Toolbox for Programming Multicellular Morphologies and Patterns》论文发表、《Programming gene and engineered-cell therapies with synthetic biology》论文发表。
第228轮补录来源：基因编辑与表观基因组编辑；新增 《Programmable epigenome editing by transient delivery of CRISPR epigenome editor ribonucleoproteins》论文发表、《CRISPR technologies for genome, epigenome and transcriptome editing》论文发表、《Epigenome editing technologies for discovery and medicine》论文发表、《Promoter editing generates stable setpoints of gene expression》论文发表、《Epigenome editing》论文发表。
第229轮补录来源：线粒体移植与能量医学；新增 《Therapeutic applications of mitochondrial transplantation》论文发表、《Mitochondrial transfer mediates endothelial cell engraftment through mitophagy》论文发表、《Mitochondrial transfer between cell crosstalk – An emerging role in mitochondrial quality control》论文发表、《Mitochondrial transfer in endothelial cells and vascular health》论文发表、《Small-molecule hypoxia therapy in mitochondrial disease》论文发表。
第230轮补录来源：炎症衰老与慢性炎症；新增 《High Torque teno virus viremia predicts long-term mortality and reflects chronic low-grade inflammation (inflammaging) in geriatric inpatients》论文发表、《InflammAging and Human Diversity: Expanding Horizons in Age-Related Chronic Disease》论文发表、《Targeting Macrophage Efferocytosis to Treat Chronic Inflammation in Cancer and Inflammaging》论文发表、《Inflammation and aging-related disease: A transdisciplinary inflammaging framework》论文发表、《New Perspectives on Gastric Inflammaging: Integrating Multi-Omics Mechanisms and Gerotherapeutic Strategies in Chronic Gastritis》论文发表。
第231轮补录来源：巨噬细胞与组织修复；新增 《Role of Macrophages in Wound Healing》论文发表、《Macrophages in Tissue Repair, Regeneration, and Fibrosis》论文发表、《Tissue‐resident macrophages: then and now》论文发表、《Macrophage plasticity and polarization: in vivo veritas》论文发表、《Macrophage polarization and plasticity in health and disease》论文发表。
第232轮补录来源：细胞外囊泡与外泌体治疗；新增 《Developing Therapeutically Enhanced Extracellular Vesicles for Atherosclerosis Therapy》论文发表、《Extracellular vesicles for the delivery of gene therapy》论文发表、《Antibody-displaying extracellular vesicles for targeted cancer therapy》论文发表、《Anticancer Therapy Targeting Cancer-Derived Extracellular Vesicles》论文发表、《Extracellular vesicles for developing targeted hearing loss therapy》论文发表。
第233轮补录来源：生物年龄时钟与干预反馈；新增 《Amino acid-based biological age clock and its implications for human health and aging》论文发表、《Gene clock predicts time to death in humans — and assesses ‘biological’ age》论文发表、《A urinary microRNA aging clock accurately predicts biological age》论文发表、《The immunosenescence clock: A new method for evaluating biological age and predicting mortality risk》论文发表、《Measuring biological age using a functionally interpretable multi‐tissue RNA clock》论文发表。
第234轮补录来源：寿命临床试验设计；新增 《Ameliorating calcium homeostasis improves longevity and healthspan in progeroid and naturally aged mice》论文发表、《Dietary cinnamon promotes longevity and extends healthspan via mTORC1 and autophagy signaling》论文发表、《Plasma proteomics links brain and immune system aging with healthspan and longevity》论文发表、《TARGETING AGING WITH METFORMIN (TAME)》论文发表、《From telomeres and senescence to integrated longevity medicine: redefining the path to extended healthspan》论文发表。
第235轮补录来源：雷帕霉素与长寿药物；新增 《Dietary restriction in aging and longevity》论文发表、《German longevity study reveals novel rare pro-longevity alleles clustering in mTOR signaling pathway》论文发表、《Rapamycin for longevity: the pros, the cons, and future perspectives》论文发表、《The bioavailability and blood levels of low-dose rapamycin for longevity in real-world cohorts of normative aging individuals》论文发表、《Gene expression and regulatory factors of the mechanistic target of rapamycin (mTOR) complex 1 predict mammalian longevity》论文发表。
第236轮补录来源：二甲双胍与TAME试验；新增 《Emerging uncertainty on the anti-aging potential of metformin》论文发表、《Delaying Renal Aging: Metformin Holds Promise as a Potential Treatment》论文发表、《Metformin decelerates aging clock in male monkeys》论文发表、《Metformin slows signs of primate aging》论文发表、《Metformin: decelerates biomarkers of aging clocks》论文发表。
第237轮补录来源：衰老细胞清除；新增 《Immunotherapy for senescent cell clearance: Hallmarks, strategies and translational challenges》论文发表、《Endothelial senescent-cell-specific clearance alleviates metabolic dysfunction in obese mice》论文发表、《SENESCENT CELL CLEARANCE PROTECTS THE OVARIAN RESERVE IN AGING MICE》论文发表、《Senolytic Therapy Enabled by Senescent Cell‐Sensitive Biomimetic Melanin Nano‐Senolytics》论文发表、《Senescent cells, senolytics and tissue repair: the devil may be in the dosing》论文发表。
第238轮补录来源：端粒与染色体稳定性；新增 《NONO, SFPQ, and PSPC1 promote telomerase recruitment to the telomere》论文发表、《Nuclear actin and DNA replication stress regulate telomere maintenance by telomerase》论文发表、《Telomerase reactivation reverses tissue degeneration in aged telomerase-deficient mice》论文发表、《Purification of Human Telomerase Complexes Identifies Factors Involved in Telomerase Biogenesis and Telomere Length Regulation》论文发表、《TPP1 OB-Fold Domain Controls Telomere Maintenance by Recruiting Telomerase to Chromosome Ends》论文发表。
第239轮补录来源：蛋白稳态与自噬；新增 《Loss of DDI2 rewires proteostasis through CCN1-driven compensatory autophagy》论文发表、《The coming of age of chaperone-mediated autophagy》论文发表、《Protein Homeostasis and Aging: Taking Care of Proteins From the Cradle to the Grave》论文发表、《Autophagy in the Pathogenesis of Disease》论文发表、《Spatial quality control bypasses cell-based limitations on proteostasis to promote prion curing》论文发表。
第240轮补录来源：神经退行性疾病干预；新增 《Senescent cell heterogeneity in brain aging and neurodegenerative disease》论文发表、《Shared and disease-specific glial gene expression changes in neurodegenerative diseases》论文发表、《The untapped potential of targeting NRF2 in neurodegenerative disease》论文发表、《Activated or Impaired: An Overview of DNA Repair in Neurodegenerative Diseases》论文发表、《Plasma Neurodegenerative Biomarkers in Cognitively Preserved Nonagenarians》论文发表。
第241轮补录来源：认知增强与工作记忆；新增 《Reduced connection strength leads to enhancement of working memory capacity in cognitive training》论文发表、《The Effects of Working Memory Versus Adaptive Visual Search Control Training on Executive Cognitive Function》论文发表、《Behavioural and ERP Effects of Cognitive and Combined Cognitive and Physical Training on Working Memory and Executive Function in Healthy Older Adults》论文发表、《Strategy training and working memory task performance》论文发表、《The Effects of Cognitive Training on Executive Function and Cognition》论文发表。
第242轮补录来源：睡眠与大脑清洁；新增 《Norepinephrine-mediated slow vasomotion drives glymphatic clearance during sleep》论文发表、《Sleep Drives Metabolite Clearance from the Adult Brain》论文发表、《The Glymphatic System and Waste Clearance with Brain Aging: A Review》论文发表、《Sleep Facilitates Clearance of Metabolites from the Brain: Glymphatic Function in Aging and Neurodegenerative Diseases》论文发表、《Sleep-circadian modulation of autophagy and glymphatic function: failure of coordinated brain clearance in Parkinson’s disease》论文发表。
第243轮补录来源：脑机接口语音解码；新增 《Continuous tracking using deep learning-based decoding for noninvasive brain–computer interface》论文发表、《A high-performance speech neuroprosthesis》论文发表、《Using adversarial networks to extend brain computer interface decoding accuracy over time》论文发表、《Bilingual speech neuroprosthesis》论文发表、《Brain-Computer Interface: Applications to Speech Decoding and Synthesis to Augment Communication》论文发表。
第244轮补录来源：记忆编辑与创伤后应激；新增 《Memory editing from science fiction to clinical practice》论文发表、《Reconsolidation: maintaining memory relevance》论文发表、《Circuit-informed modulation of traumatic memory in PTSD: integrating extinction, suppression, and reconsolidation》论文发表、《Effects of propranolol on the modification of trauma memory reconsolidation in PTSD patients: A systematic review and meta-analysis》论文发表、《A clinician's perspective on memory reconsolidation as the primary basis for psychotherapeutic change in posttraumatic stress disorder (PTSD)》论文发表。
第245轮补录来源：数字孪生与个性化健康；新增 《Digital Twin Technology: New Frontiers for Personalized Healthcare》论文发表、《Causal digital twin modeling of periodontal healing: personalized prediction of low-level laser therapy benefit using a tooth-graph ODE transformer》论文发表、《iDT-diet: Toward Personalized Health Forecasting-An Intelligent Digital Twin Model for Diet-Influenced Biomarker Trajectories (Student Abstract)》论文发表、《Innovative digital twin framework for early risk detection and personalized perinatal healthcare》论文发表、《Digital Twin Model: A Real-Time Emotion Recognition System for Personalized Healthcare》论文发表。
第246轮补录来源：AI药物发现与临床试验；新增 《Accelerating drug discovery, development, and clinical trials by artificial intelligence》论文发表、《Generative artificial intelligence empowers digital twins in drug discovery and clinical trials》论文发表、《Advancement of Artificial Intelligence in Drug Discovery: A Comprehensive Review》论文发表、《Artificial intelligence and machine learning in drug discovery: From lead discovery to clinical validation (2020–2025)》论文发表、《Artificial Intelligence in Drug Development - Revolutionizing Drug Discovery and Clinical Trials》论文发表。
第247轮补录来源：生成式AI与科学自动化；新增 《An autonomous laboratory for the accelerated synthesis of inorganic materials》论文发表、《Autonomous chemical research with large language models》论文发表、《Scaling deep learning for materials discovery》论文发表、《Data-Driven Design and Autonomous Experimentation in Soft and Biological Materials Engineering》论文发表、《Agentic and Generative AI for Autonomous Energy Systems: Reference Architecture, Open Challenges, and Research Agenda》论文发表。
第248轮补录来源：长寿逃逸速度理论与建模；新增 《Healthy dietary patterns, longevity genes, and life expectancy: A prospective cohort study》论文发表、《Modifiable risk factors attenuated longevity genetic predisposition on life expectancy in the oldest old》论文发表、《Longevity Escape Velocity Medicine: A New Medical Specialty for Longevity?》论文发表、《Addressing Longevity, Life Expectancy and Health Life Expectancy》论文发表、《The Effect of Exceptional Parental Longevity on Life Expectancy》论文发表。
第249轮补录来源：主体持续性建模；新增 《CONTENT OF PERSONAL IDENTITY AT DIFFERENT STAGES OF THE LIFE COURSE》论文发表、《Personal network dynamics across the life course: A relationship-related structural approach》论文发表、《Personality Development: Continuity and Change Over the Life Course》论文发表、《Life Course Transitions and Social Identity Change》论文发表、《Bodily continuity, personal identity and life after death》论文发表。
第250轮补录来源：风险治理与全球合作；新增 《Towards the Governance of Global Systemic Risk》论文发表、《Localized Development Gaps in Global Governance: The Case of Disaster Risk Reduction in Oceania》论文发表、《Whose risk counts? Climate risk frames in global green finance governance complex》论文发表、《The Risk of Global Environmental Change to Economic Sustainability and Law: Help from Digital Technology and Governance Regulation》论文发表、《Technology-Enabled Adaptive Knowledge Architecture for Humanitarian Governance (TAKAH) as an Enabler for Disaster Risk Management: An African-Global Comparative Analysis》论文发表。
第251轮补录来源：神经干细胞疗法；新增 《Ultrasound Activated Piezoelectric Dural Patches to Drive Endogenous Neural Stem Cell–Mediated Repair Traumatic Brain Injury》论文发表、《How neural stem cell therapy promotes brain repair after stroke》论文发表、《Neural stem cells of the subventricular zone: A potential stem cell pool for brain repair in Parkinson’s disease》论文发表、《A Coated Sponge: Toward Neonatal Brain Repair》论文发表、《Plug and Play Brain: Understanding Integration of Transplanted Neurons for Brain Repair》论文发表。
第252轮补录来源：少突胶质细胞与髓鞘再生；新增 《Oligodendrocyte-encoded lactate dehydrogenase A couples glycolysis to remyelination via protein lactylation》论文发表、《Circulating platelets modulate oligodendrocyte progenitor cell differentiation during remyelination》论文发表、《Respiratory infection with influenza A virus delays remyelination and alters oligodendrocyte metabolism》论文发表、《Fractalkine enhances oligodendrocyte regeneration and remyelination in a demyelination mouse model》论文发表、《Oligodendrocyte death initiates synchronous remyelination to restore cortical myelin patterns in mice》论文发表。
第253轮补录来源：星形胶质细胞与脑修复；新增 《Astrocyte Enrichment of 3D Cortical Constructs Enhances Brain Repair》论文发表、《Mechanisms of astrocyte aging in reactivity and disease》论文发表、《A molecular switch for neuroprotective astrocyte reactivity》论文发表、《Dysregulation of polarity proteins in astrocyte reactivity》论文发表、《Astrocyte Reactivity in Alzheimer’s Disease: Therapeutic Opportunities to Promote Repair》论文发表。
第254轮补录来源：小胶质细胞与神经免疫；新增 《Neuroimmune dynamics and brain aging: mechanisms and consequences》论文发表、《An in vivo neuroimmune organoid model to study human microglia phenotypes》论文发表、《Microglia modulate neurodevelopment in human neuroimmune organoids》论文发表、《Aging Microglia—Phenotypes, Functions and Implications for Age-Related Neurodegenerative Diseases》论文发表、《The cellular choreography of brain aging: a neuroimmune network perspective》论文发表。
第255轮补录来源：血脑屏障与神经血管单元；新增 《Temporal dynamics of neurovascular unit changes following blood-brain barrier opening in the putamen of non-human primates》论文发表、《Contributions of blood–brain barrier imaging to neurovascular unit pathophysiology of Alzheimer’s disease and related dementias》论文发表、《Engineering Neurovascular Unit and Blood–Brain Barrier for Ischemic Stroke Modeling》论文发表、《Neurovascular unit senescence as a driver of blood–brain barrier dysfunction in Alzheimer’s disease：Mechanisms, consequences, and therapeutic implications》论文发表、《Multiple sclerosis: etiology in the context of neurovascular unit and immune system involvement and advancements with in vitro blood–brain barrier models》论文发表。
第256轮补录来源：神经炎症与认知保护；新增 《Neuronal Necroptosis Drives Neuroinflammation and Cognitive Decline Independent of Neuronal Cell Death》论文发表、《Cognitive frailty: A comprehensive clinical paradigm beyond cognitive decline》论文发表、《P2Y1R silencing in Astrocytes Protected Neuroinflammation and Cognitive Decline in a Mouse Model of Alzheimer's Disease》论文发表、《Periodontitis-induced neuroinflammation triggers IFITM3-Aβ axis to cause alzheimer’s disease-like pathology and cognitive decline》论文发表、《Neuroinflammation and cognitive decline: a TSPO‐PET imaging study.》论文发表。
第257轮补录来源：脑类器官与神经发育；新增 《KCNJ2 inhibition mitigates mechanical injury in a human brain organoid model of traumatic brain injury》论文发表、《Cortical brain organoid as a model to study microgravity exposure》论文发表、《Modest Neurodevelopment Impacts of APOE4 in a Human Brain Organoid Model of Low-Grade SARS-CoV-2 Infection》论文发表、《Brain organoid models of Huntington's disease shift the focus towards neurodevelopment》论文发表、《Novel model of cortical–meningeal organoid co-culture system improves human cortical brain organoid cytoarchitecture》论文发表。
第258轮补录来源：全脑连接组图谱；新增 《Whole-body connectome of a segmented annelid larva》论文发表、《Generative network modeling reveals quantitative definitions of bilateral symmetry exhibited by a whole insect brain connectome》论文发表、《Fly-brain connectome helps to make predictions about neural activity》论文发表、《Sexual coordination in a whole-brain map of prairie vole pair bonding》论文发表、《Comparative Study on Topological Properties of the Whole-Brain Functional Connectome in Idiopathic Rapid Eye Movement Sleep Behavior Disorder and Parkinson’s Disease Without RBD》论文发表。
第259轮补录来源：脑机接口运动解码；新增 《Relevance-based channel selection in motor imagery brain–computer interface》论文发表、《Decoding post-stroke motor function from structural brain images》论文发表、《Decoding motor imagery hand direction in brain computer interface from direction-dependent modulation of parietal connectivity using a new brain functional connectivity measure》论文发表、《Cortical brain signals improve decoding of movement and tremor for clinical brain computer interfaces》论文发表、《Improving direction decoding accuracy during online motor imagery based brain-computer interface using error-related potentials》论文发表。
第260轮补录来源：脑机接口感觉反馈；新增 《Real-time brain-computer interface control of walking exoskeleton with bilateral sensory feedback》论文发表、《A brain–computer interface working definition》论文发表、《Peripheral nerve stimulation enables somatosensory feedback while suppressing phantom limb pain in transradial amputees》论文发表、《Learning from feedback training data at a self-paced brain–computer interface》论文发表、《Convolutional neural network approach for motor imagery and steady-state somatosensory evoked potential-based hybrid brain-computer interface using dry electrodes》论文发表。
第261轮补录来源：神经假体与人工感官；新增 《Neural mechanisms underlying intracortical microstimulation for sensory restoration》论文发表、《Wearable non-invasive neuroprosthesis for targeted sensory restoration in neuropathy》论文发表、《Recapitulating sensory feedback in artificial skin》论文发表、《Targeted Nipple-Areola Complex Reinnervation for Sensory Restoration in Gender-Affirming Mastectomy》论文发表、《Restoration of sensory information via bionic hands》论文发表。
第262轮补录来源：记忆巩固与睡眠依赖；新增 《Sleep—A brain-state serving systems memory consolidation》论文发表、《Smell, Sleep, and Memory Consolidation》论文发表、《Sleep-dependent memory consolidation》论文发表、《Memory Consolidation in Sleep》论文发表、《Reactivation of memory-encoding dentate gyrus neurons during memory consolidation is associated with subregion-specific, learning- and sleep-mediated biosynthetic changes》论文发表。
第263轮补录来源：突触可塑性与学习；新增 《Meta-learning synaptic plasticity and memory addressing for continual familiarity detection》论文发表、《Phase-Amplitude Coupling: A General Mechanism for Memory Processing and Synaptic Plasticity?》论文发表、《Synaptic signatures of perinatal cannabinoids: A systematic review of rodent hippocampal synaptic plasticity, learning, and memory》论文发表、《Neuromodulators and Long-Term Synaptic Plasticity in Learning and Memory: A Steered-Glutamatergic Perspective》论文发表、《Synaptic Plasticity and Learning and Memory: 15 Years of Progress》论文发表。
第264轮补录来源：神经再生药物；新增 《The Role of Hyperbaric Oxygen Therapy in Neuroregeneration and Neuroprotection: A Review》论文发表、《Neuroregeneration and functional recovery after stroke: advancing neural stem cell therapy toward clinical application》论文发表、《The brain-derived neurotrophic factor in neuronal plasticity and neuroregeneration: new pharmacological concepts for old and new drugs》论文发表、《TRPV1 may increase the effectiveness of estrogen therapy on neuroprotection and neuroregeneration》论文发表、《Exosomes derived from human placental mesenchymal stem cells in combination with hyperbaric oxygen therapy enhance neuroregeneration in a rat model of sciatic nerve crush injury》论文发表。
第265轮补录来源：脑衰老与认知储备；新增 《Cognitive Reserve and Related Constructs: A Unified Framework Across Cognitive and Brain Dimensions of Aging》论文发表、《The Influence of Genetic Factors and Cognitive Reserve on Structural and Functional Resting-State Brain Networks in Aging and Alzheimer’s Disease》论文发表、《Lower cognitive reserve in the aging human immunodeficiency virus-infected brain》论文发表、《Brain structure and function related to cognitive reserve variables in normal aging, mild cognitive impairment and Alzheimer's disease》论文发表、《Cognitive reserve and brain maintenance in aging and dementia: An integrative review》论文发表。
第266轮补录来源：心血管衰老与动脉硬化逆转；新增 《Cerebromicrovascular senescence in vascular cognitive impairment: does accelerated microvascular aging accompany atherosclerosis?》论文发表、《Vascular Aging and Atherosclerosis: A Perspective on Aging》论文发表、《The Role and Mechanism of Vascular Aging in Geriatric Vascular Diseases》论文发表、《Cerebral Hemodynamics and Carotid Atherosclerosis in Patients With Subcortical Ischemic Vascular Dementia》论文发表、《MicroRNAs in vascular aging and atherosclerosis》论文发表。
第267轮补录来源：血管新生与组织灌注；新增 《Enhanced angiogenesis through controlled release of basic fibroblast growth factor from peptide amphiphile for tissue regeneration》论文发表、《Hyperbaric oxygen therapy promotes wound repair in ischemic and hyperglycemic conditions, increasing tissue perfusion and collagen deposition》论文发表、《Microvessels derived from hiPSCs are a novel source for angiogenesis and tissue regeneration》论文发表、《Trimetazidine improves angiogenesis and tissue perfusion in ischemic rat skeletal muscle》论文发表、《Novel metal nanomaterials to promote angiogenesis in tissue regeneration》论文发表。
第268轮补录来源：淋巴系统与免疫运输；新增 《Lymphatic-immune interactions in the musculoskeletal system》论文发表、《Immune cells as messengers from the CNS to the periphery: the role of the meningeal lymphatic system in immune cell migration from the CNS》论文发表、《Leucocyte Trafficking via the Lymphatic Vasculature— Mechanisms and Consequences》论文发表、《Regulation of Immune Function by the Lymphatic System in Lymphedema》论文发表、《T Cell Trafficking through Lymphatic Vessels》论文发表。
第269轮补录来源：免疫衰老与疫苗反应；新增 《Immunosenescence and Vaccine Efficacy in Aging: Dynamic Interplay of Gut Microbiota and <scp>mTOR</scp> Signaling Pathways》论文发表、《Immunosenescence and vaccine efficacy revealed by immunometabolic analysis of SARS-CoV-2-specific cells in multiple sclerosis patients》论文发表、《Remodeling of the Immune Response With Aging: Immunosenescence and Its Potential Impact on COVID-19 Immune Response》论文发表、《Targeting Inflammation and Immunosenescence to Improve Vaccine Responses in the Elderly》论文发表、《Immunosenescence: A systems-level overview of immune cell biology and strategies for improving vaccine responses》论文发表。
第270轮补录来源：胸腺再生与T细胞库；新增 《Single Cell and Spatially Resolved Transcriptome and Immune Repertoire of Mouse Thymus During Aging Reveal Immunological Heterogeneity and Direction of Thymic Selection Pressure》论文发表、《Mesenchymal thymic niche cells enable regeneration of the adult thymus and T cell immunity》论文发表、《Aryl hydrocarbon receptor regulates IL-22 receptor expression on thymic epithelial cell and accelerates thymus regeneration》论文发表、《Regeneration circuits in the thymus》论文发表、《Human T cell repertoire: what happens in thymus does not stay in thymus》论文发表。
第271轮补录来源：造血系统衰老；新增 《Aging of hematopoietic stem cells is inconsequential to progenitor cell function》论文发表、《Nanobioreactor detection of space-associated hematopoietic stem and progenitor cell aging》论文发表、《DNA methylation drives hematopoietic stem cell aging phenotypes after proliferative stress》论文发表、《Turning the clock forward: Inflammation accelerates the aging of hematopoietic stem cells》论文发表、《Aging of the Hematopoietic Stem Cell Niche: An Unnerving Matter》论文发表。
第272轮补录来源：干细胞生态位工程；新增 《Biomimetic Fibrinogen Nanofiber Scaffolds for Vascular Hematopoietic Stem Cell Niche Engineering》论文发表、《The emergence of the stem cell niche》论文发表、《The intestinal stem cell niche flexes its muscles》论文发表、《Niche inflammatory signals control oscillating mammary regeneration and protect stem cells from cytotoxic stress》论文发表、《Engineering Nanoscale Stem Cell Niche: Direct Stem Cell Behavior at Cell–Matrix Interface》论文发表。
第273轮补录来源：细胞衰老与组织微环境；新增 《Polyphenol mediated zinc-oxygen synergistic hydrogel remodels senescent microenvironment for periodontal tissue regeneration》论文发表、《The impact of the senescent microenvironment on tumorigenesis: Insights for cancer therapy》论文发表、《Fundamental Cell-Intrinsic Mechanism Underlying Age-Dependent Accumulation of Senescent Cells》论文发表、《Microenvironment-sensitive nanozymes for tissue regeneration》论文发表、《Senescent cells enhance newt limb regeneration by promoting muscle dedifferentiation》论文发表。
第274轮补录来源：细胞外基质重塑；新增 《The senescence-stiffening loop: Extracellular matrix remodeling, hypoperfusion, and mitochondrial dysfunction drive tissue aging》论文发表、《Extracellular matrix remodeling in the tumor immunity》论文发表、《Counteracting immunodepression by extracellular matrix hydrogel to promote brain tissue remodeling and neurological function recovery after traumatic brain injury》论文发表、《Alpha-1 adrenergic signaling drives cardiac regeneration via extracellular matrix remodeling transcriptional program in zebrafish macrophages》论文发表、《Extracellular matrix stiffness cues junctional remodeling for 3D tissue elongation》论文发表。
第275轮补录来源：肌肉再生与肌少症逆转；新增 《Brain senescence drives sarcopenia-like transcriptomic remodeling in skeletal muscle》论文发表、《Macrophage SREBP1 regulates skeletal muscle regeneration》论文发表、《Skeletal Muscle Regeneration: Functional Skeletal Muscle Regeneration with Thermally Drawn Porous Fibers and Reprogrammed Muscle Progenitors for Volumetric Muscle Injury (Adv. Mater. 14/2021)》论文发表、《SRSF1 Is Crucial for Maintaining Satellite Cell Homeostasis During Skeletal Muscle Growth and Regeneration》论文发表、《Old muscle stem cells are rejuvenated by a young environment》论文发表。
第276轮补录来源：骨骼重塑与骨质疏松；新增 《Osteoporosis: interferon-gamma-mediated bone remodeling in osteoimmunology》论文发表、《Bone remodeling: A review of the bone microenvironment perspective for fragility fracture (osteoporosis) of the hip》论文发表、《Modulation of bone remodeling by the gut microbiota: a new therapy for osteoporosis》论文发表、《Epigenetics, Bone Remodeling and Osteoporosis》论文发表、《Clinical use of biochemical markers of bone remodeling in osteoporosis》论文发表。
第277轮补录来源：脂肪组织与代谢健康；新增 《From fat to fate: how aging adipose tissue drives systemic metabolic aging》论文发表、《IgG is an aging factor that drives adipose tissue fibrosis and metabolic decline》论文发表、《Exploring adipose tissue-derived extracellular vesicles in inter-organ crosstalk: Implications for metabolic regulation and adipose tissue function》论文发表、《The interplay of aging, adipose tissue, and COVID-19: a potent alliance with implications for health》论文发表、《It is a branched road to adipose tissue aging》论文发表。
第278轮补录来源：胰岛β细胞再生；新增 《Beta-Cell Dedifferentiation in Type 2 Diabetes: Concise Review》论文发表、《Beta-cell replacement and regeneration: Strategies of cell-based therapy for type 1 diabetes mellitus》论文发表、《Regeneration of pancreatic beta-cell mass for the treatment of diabetes》论文发表、《From pancreatic islet formation to beta-cell regeneration》论文发表、《Sustained beta cell apoptosis in patients with long-standing type 1 diabetes: indirect evidence for islet regeneration?》论文发表。
第279轮补录来源：肝脏脂肪变性逆转；新增 《Metabolic Dysfunction-Associated Steatotic Liver Disease: The Role of Hepatic Steatosis in Insulin Resistance and Metabolic Health》论文发表、《The mediterranean diet, hepatic steatosis and nonalcoholic fatty liver disease》论文发表、《Optimal Cutoffs of Fatty Liver Index and Hepatic Steatosis Index in Diagnosing Pediatric Metabolic Dysfunction-associated Steatotic Liver Disease》论文发表、《Predicting hepatic steatosis degree in metabolic dysfunction-associated steatotic liver disease using obesity and lipid-related indices》论文发表、《An umbrella meta-analysis of microbial therapy on hepatic steatosis, fibrosis, and liver stiffness in metabolic dysfunction-associated steatotic liver disease》论文发表。
第280轮补录来源：肠道屏障与菌群移植；新增 《Effects of cassava polysaccharides on gut microbiome, intestinal barrier and macrophage activation》论文发表、《Gut microbiome alterations precede graft rejection in kidney transplantation patients》论文发表、《Rewiring bugs: Diet, the gut microbiome, and nerve regeneration》论文发表、《Continuous fermentation-derived fecal microbiota transplantation improves intestinal barrier function and reshapes gut microbiota in weaned piglets》论文发表、《Fecal Microbiota Transplantation Induces Sustained Gut Microbiome Changes in Pediatric Ulcerative Colitis: A Combined Randomized and Open-Label Study》论文发表。
第281轮补录来源：肾脏纤维化逆转；新增 《Native T1 mapping-based radiomics diagnosis of kidney function and renal fibrosis in chronic kidney disease》论文发表、《MYCT1 attenuates renal fibrosis and tubular injury in diabetic kidney disease》论文发表、《Anthraquinones from Rheum officinale Ameliorate Renal Fibrosis in Acute Kidney Injury and Chronic Kidney Disease》论文发表、《Macrophages in Renal Injury, Repair, Fibrosis Following Acute Kidney Injury and Targeted Therapy》论文发表、《Senolytic therapy ameliorates renal fibrosis postacute kidney injury by alleviating renal senescence》论文发表。
第282轮补录来源：肺纤维化与肺泡再生；新增 《Atg5 deficiency alters myofibroblast accumulation and alveolar regeneration in lung fibrosis》论文发表、《Designer umbilical cord-stem cells induce alveolar wall regeneration in pulmonary disease models》论文发表、《Pulmonary administration of 1,25-dihydroxyvitamin D3 to the lungs induces alveolar regeneration in a mouse model of chronic obstructive pulmonary disease》论文发表、《Pulmonary administration of phosphoinositide 3-kinase inhibitor is a curative treatment for chronic obstructive pulmonary disease by alveolar regeneration》论文发表、《Extracellular vesicles from alveolar macrophages promotes pulmonary fibrosis through suppression of lung alveolar regeneration》论文发表。
第283轮补录来源：心脏纤维化与心肌功能；新增 《Loss of primary cilia on cardiac fibroblast attenuates fibrosis and preserves cardiac function post myocardial infarction》论文发表、《Selective HDL-Raising Human Apo A-I Gene Therapy Counteracts Cardiac Hypertrophy, Reduces Myocardial Fibrosis, and Improves Cardiac Function in Mice with Chronic Pressure Overload》论文发表、《Ginsenoside Rg2 attenuates myocardial fibrosis and improves cardiac function after myocardial infarction via AKT signaling pathway》论文发表、《Suppression of macrophage enriched miRNA 210-3p improves cardiac fibrosis and cardiac function following myocardial infarction》论文发表、《Rat strain-related differences in myocardial adrenergic tone and the impact on cardiac fibrosis, adrenergic responsiveness and myocardial structure and function》论文发表。
第284轮补录来源：脑小血管病与白质完整；新增 《White matter microstructure fingerprint of cerebral small vessel disease》论文发表、《White matter lesions in cerebral small vessel disease》论文发表、《Quantifying the severity of white matter damage in Cerebral Small Vessel Disease》论文发表、《Pathogenesis of white matter changes in cerebral small vessel diseases: beyond vessel-intrinsic mechanisms》论文发表、《Heterogeneity of White Matter Hyperintensities in Cognitively Impaired Patients With Cerebral Small Vessel Disease》论文发表。
第285轮补录来源：神经退行性蛋白病；新增 《Abnormal Amyloid-β Duration, Tau, and Neurodegeneration in Cranial Images》论文发表、《Plasma brain-derived tau is an amyloid-associated neurodegeneration biomarker in Alzheimer’s disease》论文发表、《Lewy body dementia: exploring biomarkers and pathogenic interactions of amyloid β, tau, and α-synuclein》论文发表、《The spatial distribution of coupling between tau and neurodegeneration in amyloid-β positive mild cognitive impairment》论文发表、《Putting the New Alzheimer Disease Amyloid, Tau, Neurodegeneration (AT[N]) Diagnostic System to the Test》论文发表。
第286轮补录来源：蛋白质聚集体清除；新增 《Physiological brain clearance architecture revealed by neuronal protein tracing》论文发表、《Aspirin inhibits proteasomal degradation and promotes α-synuclein aggregate clearance through K63 ubiquitination》论文发表、《Clearance of protein aggregates during cell division》论文发表、《Antibody-mediated clearance of an ER-resident aggregate that causes glaucoma》论文发表、《Reactivated endogenous retroviruses promote protein aggregate spreading》论文发表。
第287轮补录来源：线粒体自噬与能量稳态；新增 《Mitophagy-Enhanced Nanoparticle-Engineered Mitochondria Restore Homeostasis of Mitochondrial Pool for Alleviating Pulmonary Fibrosis》论文发表、《Mitophagy in cardiovascular homeostasis》论文发表、《Putting energy into mitophagy》论文发表、《Enhanced brain mitophagy slows systemic aging》论文发表、《Mitophagy, Mitochondrial Dynamics, and Homeostasis in Cardiovascular Aging》论文发表。
第288轮补录来源：内质网应激与蛋白稳态；新增 《Phenylhydrazone-based endoplasmic reticulum proteostasis regulator compounds with enhanced biological activity》论文发表、《The endoplasmic reticulum proteostasis network and bone disease》论文发表、《Zinc-redox crosstalk regulates proteostasis in the endoplasmic reticulum》论文发表、《The endoplasmic reticulum membrane complex promotes proteostasis of GABAA receptors》论文发表、《Calcium depletion challenges endoplasmic reticulum proteostasis by destabilising BiP-substrate complexes》论文发表。
第289轮补录来源：溶酶体功能与细胞自净；新增 《Nutrient-regulated control of lysosome function by signaling lipid conversion》论文发表、《Targeted clearance of senescent cells alleviates alcohol-associated liver disease by restoring cellular function and immune balance》论文发表、《Mitochondria-lysosome-related organelles mediate mitochondrial clearance during cellular dedifferentiation》论文发表、《The Lysosome at the Intersection of Cellular Growth and Destruction》论文发表、《Regulation and Function of Mitochondria–Lysosome Membrane Contact Sites in Cellular Homeostasis》论文发表。
第290轮补录来源：细胞膜修复与机械韧性；新增 《Membrane repair following filtroporation-induced cell permeabilization》论文发表、《Time matters: the dynamics of plasma membrane repair》论文发表、《Membrane Tension Regulation is Required for Wound Repair》论文发表、《Hybrid Cell Membrane‐Functionalized Matrixes for Modulating Inflammatory Microenvironment and Improving Bone Defect Repair》论文发表、《ATG9 assists lipid replenishment for lysosome membrane repair》论文发表。
第291轮补录来源：表观遗传重编程；新增 《Epigenetic Modifiers as Game Changers for Healthy Aging》论文发表、《Rejuvenation by Partial Reprogramming of the Epigenome》论文发表、《Rejuvenation of Adult Stem Cells: Is Age-Associated Dysfunction Epigenetic?》论文发表、《Aging, Rejuvenation, and Epigenetic Reprogramming: Resetting the Aging Clock》论文发表、《Cellular reprogramming and epigenetic rejuvenation》论文发表。
第292轮补录来源：化学重编程与小分子疗法；新增 《In vivo brown adipogenic reprogramming induced by a small molecule cocktail》论文发表、《Molecular time machines unleashed: small-molecule-driven reprogramming to reverse the senescence》论文发表、《Improving chemical reprogramming strategies》论文发表、《Robust small molecule-aided cardiac reprogramming systems selective to cardiac fibroblasts》论文发表、《Small-Molecule-Based Lineage Reprogramming Creates Functional Astrocytes》论文发表。
第293轮补录来源：基因疗法与体内编辑；新增 《In vivo base editing gene therapy for heterozygous familial hypercholesterolemia: a phase 1 trial》论文发表、《Personalized, in vivo gene editing for a newborn》论文发表、《In vivo gene editing for inherited vision loss》论文发表、《Therapeutic in vivo genome editing: innovations and challenges in rAAV vector-based CRISPR delivery》论文发表、《CRISPR/Cas-Dependent and Nuclease-Free
第294轮补录来源：RNA疗法与mRNA医学；新增 《Empower the age of smart mRNA medicine: Programmable RNA sensor and molecular tools refine therapeutic payload production》论文发表、《mRNA vaccine quality analysis using RNA sequencing》论文发表、《mRNA therapy for a rare childhood disease》论文发表、《mRNA therapeutics: Transforming medicine through innovation in design, delivery, and disease treatment》论文发表、《mRNA therapy as primary and bridge therapy for inborn errors of metabolism》论文发表。
第295轮补录来源：细胞疗法与免疫重建；新增 《Advances in cell therapy for orthopedic diseases: bridging immune modulation and regeneration》论文发表、《Immune reconstitution following allogeneic hematopoietic cell transplantation and CAR-T therapy: dynamics, determinants, and directions》论文发表、《Kinetics of Immune Reconstitution after CD19 CAR-T Cell Therapy in ALL Patients》论文发表、《In vivo T-cell dynamics during immune reconstitution after hematopoietic stem cell gene therapy in adenosine deaminase severe combined immune deficiency》论文发表、《Adoptive precursor cell therapy to enhance immune reconstitution after hematopoietic stem cell transplantation in mouse and man》论文发表。
第296轮补录来源：器官芯片与药物安全；新增 《Bioethical implications of organ‐on‐a‐chip on modernizing drug development》论文发表、《Adoption of organ-on-chip platforms by the pharmaceutical industry》论文发表、《Integrated human organ-on-a-chip model for predictive studies of anti-tumor drug efficacy and cardiac safety》论文发表、《Human organotypic bioconstructs from organ-on-chip devices for human-predictive biological insights on drug candidates》论文发表、《Organ-on-chip technology to revolutionise drug development》论文发表。
第297轮补录来源：数字孪生与寿命预测；新增 《An insight in the future of healthcare: integrating digital twin for personalized medicine》论文发表、《Human Digital Twin for Personalized Healthcare: Vision, Architecture and Future Directions》论文发表、《Digital twin for healthcare systems》论文发表、《Digital Twin: Generalization, characterization and implementation》论文发表、《Design for a digital twin in clinical patient care》论文发表。
第298轮补录来源：长寿逃逸速度与医学基础设施；新增 《Longevity medicine: upskilling the physicians of tomorrow》论文发表、《No more band-aids: health-care system reform》论文发表、《The Lancet Healthy Longevity: Health For All, For Longer》论文发表、《Human rights for healthy longevity》论文发表、《Digital Transformation in Medicine to Enhance Quality of Life, Longevity, and Health Equity》论文发表。
第299轮补录来源：主体连续性与未来选择权；新增 《Personal recovery and future self-continuity in individuals with schizophrenia》论文发表、《Towards a Human Right to Psychological Continuity? Reflections on the Rights to Personal Identity, Self-Determination, and Personal Integrity》论文发表、《Using Identity-Based Motivation to Enhance Future Self-Continuity》论文发表、《Personal Identity and Cortical Midline Structure (CMS): Do Temporal Features of CMS Neural Activity Transform Into “Self-Continuity”?》论文发表、《Contribution of past and future self-defining event networks to personal identity》论文发表。
第300轮补录来源：文明级风险与长期治理；新增 《Governance of artificial intelligence in Southeast Asia》论文发表、《Artificial intelligence, complexity, and systemic resilience in global governance》论文发表、《Governing the safety of artificial intelligence in healthcare》论文发表、《'Solving for X?' Towards a problem-finding framework to ground long-term governance strategies for artificial intelligence》论文发表、《Comparative Analysis of Long-Term Governance Problems: Risks of Climate Change and Artificial Intelligence》论文发表。
第301轮补录来源：端粒酶激活与染色体端粒维持；新增 《Integrated evaluation of telomerase activation and telomere maintenance across cancer cell lines》论文发表、《Break-induced replication and telomerase-independent telomere maintenance require Pol32》论文发表、《EXO1 Contributes to Telomere Maintenance in Both Telomerase-Proficient and Telomerase-Deficient Saccharomyces cerevisiae》论文发表、《<i>EXO1</i> Contributes to Telomere Maintenance in Both Telomerase-Proficient and Telomerase-Deficient <i>Saccharomyces cerevisiae</i>》论文发表、《Telomerase Regulation at the Telomere》论文发表。
第302轮补录来源：DNA损伤修复与基因组稳定；新增 《Genomic instability and DNA damage responses in progeria arising from defective maturation of prelamin A》论文发表、《Mre11 Nuclease Activity Has Essential Roles in DNA Repair and Genomic Stability Distinct from ATM Activation》论文发表、《Endogenous DNA Damage as a Source of Genomic Instability in Cancer》论文发表、《Interplay of p53 and DNA-repair protein XRCC4 in tumorigenesis, genomic stability and development》论文发表、《DNA strands show symmetry in damage tolerance but asymmetries in repair efficiency》论文发表。
第303轮补录来源：表观遗传时钟与干预；新增 《The epigenetic clock: a molecular crystal ball for human aging?》论文发表、《An epigenetic aging clock for dogs and wolves》论文发表、《An epigenetic clock controls aging》论文发表、《Epigenetic drift underlies epigenetic clock signals, but displays distinct responses to lifespan interventions, development, and cellular dedifferentiation》论文发表、《Various diseases and conditions are strongly associated with the next-generation epigenetic aging clock CheekAge》论文发表。
第304轮补录来源：衰老细胞清除与组织年轻化；新增 《Rejuvenation by Therapeutic Elimination of Senescent Cells》论文发表、《Clearance of senescent glial cells prevents tau-dependent pathology and cognitive decline》论文发表、《Abstract 4344658: Endothelial cell specific senescent cell clearance alleviates metabolic dysfunction in obese mice》论文发表、《Restored clearance of senescent neutrophils by tissue-resident macrophages limits organ aging》论文发表、《Clearance of p16Ink4a-positive senescent cells delays ageing-associated disorders》论文发表。
第305轮补录来源：干细胞耗竭与再生；新增 《Imaging stem-cell-driven regeneration in mammals》论文发表、《Researchers rejuvenate aging mice with stem cell genes》论文发表、《Stem cell factors reverse signs of aging in mice》论文发表、《Cholesterol induces T cell exhaustion》论文发表、《Mitochondrial oxidative phosphorylation is linked to T-cell exhaustion》论文发表。
第306轮补录来源：蛋白稳态与分子伴侣；新增 《Molecular chaperones in protein folding and proteostasis》论文发表、《Proteostasis collapse, a hallmark of aging, hinders the chaperone-Start network and arrests cells in G1》论文发表、《FOXO/4E-BP Signaling in Drosophila Muscles Regulates Organism-wide Proteostasis during Aging》论文发表、《Regulation of Organismal Proteostasis by Transcellular Chaperone Signaling》论文发表、《Molecular Chaperone Machines: Chaperone Activities of the Cyclophilin Cyp-40 and the Steroid Aporeceptor-Associated Protein p23》论文发表。
第307轮补录来源：线粒体功能与能量代谢；新增 《Transcriptomic and metabolomic profiling of long-lived growth hormone releasing hormone knock-out mice: evidence for altered mitochondrial function and amino acid metabolism》论文发表、《Activation of mitochondrial energy metabolism protects against cardiac failure》论文发表、《Comprehensive analysis of mitochondrial energy metabolism–related genes and immune infiltration in intervertebral disk degeneration》论文发表、《Caveolin-1 controls mitochondrial function through regulation of m-AAA mitochondrial protease》论文发表、《MitoNEET in cardiac mitochondria: Linking mitochondrial function and cardiac disease》论文发表。
第308轮补录来源：细胞自噬与溶酶体；新增 《Autophagy as a Regulated Pathway of Cellular Degradation》论文发表、《Biological Functions of Autophagy Genes: A Disease Perspective》论文发表、《Signals from the lysosome: a control centre for cellular clearance and energy metabolism》论文发表、《The origin of the autophagosomal membrane》论文发表、《Autophagy fights disease through cellular self-digestion》论文发表。
第309轮补录来源：炎症衰老与免疫；新增 《Aging without inflammaging: lesson from Spalax》论文发表、《Is RAGE the receptor for inflammaging?》论文发表、《Inflammaging: disturbed interplay between autophagy and inflammasomes》论文发表、《Integrating cardiovascular risk biomarkers in the context of inflammaging》论文发表、《DNA methylation clocks struggle to distinguish inflammaging from healthy aging, but feature rectification improves coherence and enhances detection of inflammaging》论文发表。
第310轮补录来源：微生物组与健康长寿；新增 《Deep learning and generative artificial intelligence in aging research and healthy longevity medicine》论文发表、《Microbiome and Longevity: Gut Microbes Send Signals to Host Mitochondria》论文发表、《Microbiome: That healthy gut feeling》论文发表、《Could social relationships be key to reaching healthy longevity?》论文发表、《Structure, function and diversity of the healthy human microbiome》论文发表。
第311轮补录来源：神经退行性疾病与衰老；新增 《The Amyloid Hypothesis of Alzheimer's Disease: Progress and Problems on the Road to Therapeutics》论文发表、《Alzheimer's Disease Is a Synaptic Failure》论文发表、《Self-propagation of pathogenic protein aggregates in neurodegenerative diseases》论文发表、《Amyloid-β–induced neuronal dysfunction in Alzheimer's disease: from synapses toward neural networks》论文发表、《Neurodegenerative diseases and oxidative stress》论文发表。
第312轮补录来源：心血管衰老与动脉韧性；新增 《Arterial and Cardiac Aging: Major Shareholders in Cardiovascular Disease Enterprises》论文发表、《Accelerated peripheral vascular aging in pseudoxanthoma elasticum – proof of concept for arterial calcification-induced cardiovascular disease》论文发表、《Arterial and Cardiac Aging: Major Shareholders in Cardiovascular Disease Enterprises》论文发表、《Arterial and Cardiac Aging: Major Shareholders in Cardiovascular Disease Enterprises》论文发表、《Voluntary aerobic exercise increases arterial resilience and mitochondrial health with aging in mice》论文发表。
第313轮补录来源：代谢综合征与长寿；新增 《Abdominal obesity and metabolic syndrome》论文发表、《Metabolic Networks of Longevity》论文发表、《Metabolic Control of Longevity》论文发表、《Promoting Health and Longevity through Diet: From Model Organisms to Humans》论文发表、《Sirtuins as potential targets for metabolic syndrome》论文发表。
第314轮补录来源：肌肉骨骼健康与功能；新增 《The Loss of Skeletal Muscle Strength, Mass, and Quality in Older Adults: The Health, Aging and Body Composition Study》论文发表、《Dynapenia and Aging: An Update》论文发表、《Criteria for Clinically Relevant Weakness and Low Lean Mass and Their Longitudinal Association With Incident Mobility Impairment and Mortality: The Foundation for the National Institutes of Health (FNIH) Sarcopenia Project》论文发表、《Lower-Extremity Function in Persons over the Age of 70 Years as a Predictor of Subsequent Disability》论文发表、《Gait Speed and Survival in Older Adults》论文发表。
第315轮补录来源：生殖健康与未来选择权；新增 《Fertility Preservation in Women》论文发表、《Feasibility of ovarian stimulation and oocyte cryopreservation for fertility preservation in female children》论文发表、《Fertility Preservation in Patients With Cancer: ASCO Clinical Practice Guideline Update》论文发表、《Ovary cryopreservation and transplantation for fertility preservation》论文发表、《The efficacy and safety of fertility preservation using ovarian stimulation and oocyte or embryo cryopreservation in female cancer patients》论文发表。
第316轮补录来源：皮肤屏障与组织修复；新增 《Scratching the surface of skin development》论文发表、《Wound repair and regeneration》论文发表、《Wound repair and regeneration: Mechanisms, signaling, and translation》论文发表、《Wound repair: a showcase for cell plasticity and migration》论文发表、《Skin Cell Heterogeneity in Development, Wound Healing, and Cancer》论文发表。
第317轮补录来源：器官衰竭与替代疗法；新增 《Therapy of Severe Heatshock in Combination With Multiple Organ Dysfunction With Continuous Renal Replacement Therapy》论文发表、《Management of pediatric liver failure with therapeutic plasma exchange and continuous renal replacement therapy: A retrospective observational study》论文发表、《Organ failure》论文发表、《Replacement therapy, not recreational tonic》论文发表、《Friendly fire from organ failure》论文发表。
第318轮补录来源：异种移植与器官工程；新增 《What will be the cost of a genetically‐engineered pig organ for clinical xenotransplantation?》论文发表、《Will donor‐derived neoplasia be problematic after clinical pig organ or cell xenotransplantation?》论文发表、《Solid organ xenotransplantation at the interface between research and clinical development: Regulatory aspects》论文发表、《IXA Plenary Session 1: Update on Preclinical Life‐Supporting Organ Xenotransplantation – Current Strategies to Remaining Obstacles》论文发表、《Low anti‐pig antibody levels are key to the success of solid organ xenotransplantation: But is this sufficient?》论文发表。
第319轮补录来源：冷冻保存与生物停滞；新增 《Novel approaches for cryopreservation: Meeting the needs for cellular therapy, tissue, and organ preservation》论文发表、《The Organ Preservation Alliance: Accelerating research to enable breakthroughs in organ cryopreservation》论文发表、《Importance and safety of autologous sperm cryopreservation for fertility preservation in young male patients with cancer》论文发表、《Cryopreservation of immature ovaries for fertility preservation》论文发表、《Cryopreservation of porcine embryos》论文发表。
第320轮补录来源：数字永生与意识上传；新增 《Immortality improves cell reprogramming》论文发表、《FDA and immortality》论文发表、《In pursuit of data immortality》论文发表、《Immortality of a kind》论文发表、《The quest for immortality》论文发表。
第321轮补录来源：认知增强与神经接口；新增 《Cognitive enhancement drug may also cause addiction》论文发表、《Age-related cognitive decline: Can neural stem cells help us?》论文发表、《Much ado about cognitive enhancement》论文发表、《Brain–machine interface reveals the origin of a widely used neural signal》论文发表、《Neural interface translates thoughts into type》论文发表。
第322轮补录来源：脑机接口与运动重建；新增 《High-performance brain-to-text communication via handwriting》论文发表、《Neuronal ensemble control of prosthetic devices by a human with tetraplegia》论文发表、《High-performance neuroprosthetic control by an individual with tetraplegia》论文发表、《Fully Implanted Brain–Computer Interface in a Locked-In Patient with ALS》论文发表、《High performance communication by people with paralysis using an intracortical brain-computer interface》论文发表。
第323轮补录来源：人工智能药物发现；新增 《Highly accurate protein structure prediction with AlphaFold》论文发表、《Deep learning enables rapid identification of potent DDR1 kinase inhibitors》论文发表、《Rethinking drug design in the artificial intelligence era》论文发表、《Drug discovery with explainable artificial intelligence》论文发表、《Dual use of artificial-intelligence-powered drug discovery》论文发表。
第324轮补录来源：AI科学自动化；新增 《Autonomous elemental characterization enabled by a low cost robotic platform built upon a generalized software architecture》论文发表、《ChemCrow: Augmenting Large-Language Models with Chemistry Tools》论文发表、《A mobile robotic chemist》论文发表、《A robotic platform for flow synthesis of organic compounds informed by AI planning》论文发表、《Electronic polymer discovery through adaptive AI-guided autonomous experimentation》论文发表。
第325轮补录来源：纳米医学与分子修复；新增 《Molecular biology: RNA repair》论文发表、《Molecular Mechanism of Transcription-Repair Coupling》论文发表、《From start to finish—a molecular link in wound repair》论文发表、《Molecular Pathologies: <i>DNA Repair and Mutagenesis</i> . Errol C. Friedberg, Graham C. Walker, and Wolfram Siede. ASM Press, Washington, DC, 1995. xviii, 698 pp., iiius., + plates. $79. New edition of <i>DNA Repair</i> .》论文发表、《Draft guidelines for nanomedicine unveiled》论文发表。
第326轮补录来源：合成生物学与细胞编程；新增 《Programming circuitry for synthetic biology》论文发表、《Synthetic biology: How best to build a cell》论文发表、《A Synthetic Biology Framework for Programming Eukaryotic Transcription Functions》论文发表、《Programming self-organizing multicellular structures with synthetic cell-cell signaling》论文发表、《Synthetic Biology Looks Good on Paper》论文发表。
第327轮补录来源：基因编辑与治疗；新增 《Sickle Cell Disease Approvals Include First CRISPR Gene Editing Therapy》论文发表、《HIV overcomes CRISPR gene-editing attack》论文发表、《CRISPR gene editing produces unwanted DNA deletions》论文发表、《CRISPR gene-editing system unleashed on RNA》论文发表、《Powerful enzyme could make CRISPR gene-editing more versatile》论文发表。
第328轮补录来源：表观遗传编辑与状态重写；新增 《Inheritable Silencing of Endogenous Genes by Hit-and-Run Targeted Epigenetic Editing》论文发表、《A Metabolic Throttle Regulates the Epigenetic State of rDNA》论文发表、《Epigenetic editing makes its mark》论文发表、《‘Epigenetic’ editing cuts cholesterol in mice》论文发表、《Rewriting the genetic bond: Gene editing and our understanding of genetic parenthood》论文发表。
第329轮补录来源：脑保存与连接组重建；新增 《LIFE SCIENCE TECHNOLOGIES: This Is Your Brain: Mapping the Connectome》论文发表、《Identify connectome between genotypes and brain network phenotypes via deep self-reconstruction sparse canonical correlation analysis》论文发表、《Transcriptome, connectome and neuromodulation of the primate brain》论文发表、《From Connections to Function: The Mouse Brain Connectome Atlas》论文发表、《Language in the aging brain: The network dynamics of cognitive decline and preservation》论文发表。
第330轮补录来源：记忆编辑与身份连续性；新增 《Moral Bioenhancement Through Memory-editing: A Risk for Identity and Authenticity?》论文发表、《Memory of myself: Autobiographical memory and identity in Alzheimer's disease》论文发表、《Episodic memory reconsolidation: Updating or source confusion?》论文发表、《Opening the reconsolidation window using the mind’s eye: Extinction training during reconsolidation disrupts fear memory expression following mental imagery reactivation》论文发表、《Sleep Loss Immediately After Fear Memory Reactivation Attenuates Fear Memory Reconsolidation》论文发表。
第331轮补录来源：主体连续性建模；新增 《Reasons and Persons》论文发表、《Personal Identity》论文发表、《The Personal Identity Dilemma for Transhumanism》论文发表、《Extended mind, functionalism and personal identity》论文发表、《James Giles on Personal Identity》论文发表。
第332轮补录来源：长寿逃逸速度理论；新增 《Prions' great escape》论文发表、《Longevity genes challenged》论文发表、《Mars rover plans its escape》论文发表、《T Cell Responses and Viral Escape》论文发表、《Escape from UNEP?》论文发表。
第333轮补录来源：未来等待与时间差分；新增 《Gravitational Red-Shift in Nuclear Resonance》论文发表、《Test of Relativistic Gravitation with a Space-Borne Hydrogen Maser》论文发表、《Relativity in the Global Positioning System》论文发表、《Zur Elektrodynamik bewegter Körper》论文发表、《Non-Turing Computations Via Malament–Hogarth Space-Times》论文发表。
第334轮补录来源：技术风险治理；新增 《Existential Risk Prevention as Global Priority》论文发表、《The Malicious Use of Artificial Intelligence: Forecasting, Prevention, and Mitigation》论文发表、《An Overview of Catastrophic AI Risks》论文发表、《The AI Risk Repository: A Comprehensive Meta-Review, Database, and Risk Taxonomy of AI Risks》论文发表、《The Precipice: Existential Risk and the Future of Humanity》论文发表。
第335轮补录来源：健康寿命测量；新增 《DNA methylation age of human tissues and cell types》论文发表、《An epigenetic biomarker of aging for lifespan and healthspan》论文发表、《DNA methylation GrimAge strongly predicts lifespan and healthspan》论文发表、《Quantification of biological aging in young adults》论文发表、《Early prediction of healthy ageing and age-related diseases using blood protein biomarkers》论文发表。
第336轮补录来源：临床转化与监管；新增 《Metformin as a Tool to Target Aging》论文发表、《Cellular Senescence: A Translational Perspective》论文发表、《A framework for selection of blood-based biomarkers for geroscience-guided clinical trials: report from the TAME Biomarkers Workgroup》论文发表、《Geroscience: The Intersection of Basic Aging Biology, Chronic Disease, and Health》论文发表、《Targeting Aging with Metformin (TAME)》论文发表。
第337轮补录来源：长寿产业与资金；新增 《Flu study faces shake-up over industry funding》论文发表、《Funding cuts favour industry links》论文发表、《Industry funding doesn't influence our reports》论文发表、《Industry funding of UK universities static》论文发表、《Scientists split over tobacco industry research funding》论文发表。
第338轮补录来源：全球健康与老龄化政策；新增 《Dementia prevention, intervention, and care》论文发表、《Global burden of 369 diseases and injuries in 204 countries and territories, 1990–2019: a systematic analysis for the Global Burden of Disease Study 2019》论文发表、《The World Report on Ageing and Health》论文发表、《The World report on ageing and health: a policy framework for healthy ageing》论文发表、《Global Strategy and Action Plan on Ageing and Health》论文发表。
第339轮补录来源：教育与社会适应；新增 《Adopt universal standards for study adaptation to boost health, education and social-science research》论文发表、《Cell-intrinsic adaptation of lipid composition to local crowding drives social behaviour》论文发表、《Education: Embed social awareness in science curricula》论文发表、《Derepressing Nuclear Receptors for Metabolic Adaptation》论文发表、《Checkpoint Adaptation》论文发表。
第340轮补录来源：劳动力与AI协作；新增 《Quantum computing: physics–AI collaboration quashes quantum errors》论文发表、《Dual Arms of Adaptive Immunity: Division of Labor and Collaboration between B and T Cells》论文发表、《ChatGPT and science: the AI system was a force in 2023 — for good and bad》论文发表、《Promoter Cleavage: A TopoIIβ and PARP-1 Collaboration》论文发表、《Division of Labor by Dendritic Cells》论文发表。
第341轮补录来源：环境健康与生态韧性；新增 《Environmental Governance for the Anthropocene? Social-Ecological Systems, Resilience, and Collaborative Learning》论文发表、《Tropical forest tells a tale of ecological resilience and human tragedy》论文发表、《Public health in the age of longevity interventions: from prevention to system-wide resilience》论文发表、《COVID-19: boost mental-health resilience》论文发表、《Mitochondrial activity tunes nociceptor resilience to excitotoxicity》论文发表。
第342轮补录来源：能源基础设施与长期文明；新增 《Bidirectional linkage between a long-term energy system and a short-term power market model》论文发表、《Intra-regional renewable energy resource variability in long-term energy system planning》论文发表、《Energy-economic-environmental analysis and multi-objective optimization of district heating and cooling system with long-term and short-term thermal storage》论文发表、《Short-term solar and wind variability in long-term energy system models - A European case study》论文发表、《Long-term renewable energy technology valuation using system dynamics and Monte Carlo simulation: Photovoltaic technology case》论文发表。
第343轮补录来源：食物系统与营养安全；新增 《Seven Food System Metrics of Sustainable Nutrition Security》论文发表、《Risk Challenges and Their Impact on the Sustainable Food Security System: Lessons Learned from the COVID-19 Pandemic》论文发表、《An Integrated Global Food and Energy Security System Dynamics Model for Addressing Systemic Risk》论文发表、《The Coupling Coordination Degree and Constraints of the Water–Energy–Food Security System: A Case Study in Northeast China》论文发表、《Crisis Response and Supervision System for Food Security: A Comparative Analysis between Mainland China and Taiwan》论文发表。
第344轮补录来源：水资源与卫生设施；新增 《Burden of disease from inadequate water, sanitation and hygiene for selected adverse health outcomes: An updated analysis with a focus on low- and middle-income countries》论文发表、《Impact of drinking water, sanitation and handwashing with soap on childhood diarrhoeal disease: updated meta‐analysis and meta‐regression》论文发表、《Effectiveness of a rural sanitation programme on diarrhoea, soil-transmitted helminth infection, and child malnutrition in Odisha, India: a cluster-randomised trial》论文发表、《Interventions to improve water quality for preventing diarrhoea》论文发表、《Effect of washing hands with soap on diarrhoea risk in the community: a systematic review》论文发表。
第345轮补录来源：住房与建成环境；新增 《Housing and Health Inequalities: Review and Prospects for Research》论文发表、《Housing and inequalities in health》论文发表、《Housing and health inequalities: A synthesis of systematic reviews of interventions aimed at different pathways linking housing and health》论文发表、《Housing improvements for health and associated socio-economic outcomes》论文发表、《Housing and Health: Time Again for Public Health Action》论文发表。
第346轮补录来源：交通与移动基础设施；新增 《Astounding bat mobility》论文发表、《Protein Mobility within the Nucleus—What Are the Right Moves?》论文发表、《Protein Mobility within the Nucleus—What Are the Right Moves?》论文发表、《Retrohoming: cDNA-Mediated Mobility of Group II Introns Requires a Catalytic RNA》论文发表、《The Lateral Organization and Mobility of Plasma Membrane Components》论文发表。
第347轮补录来源：数字基础设施与连接；新增 《Internet skills and the digital divide》论文发表、《Second-Level Digital Divide: Differences in People's Online Skills》论文发表、《Any Thing for Anyone? A New Digital Divide in Internet‐of‐Things Skills》论文发表、《Digital Inclusion as Health Care — Supporting Health Care Equity with Digital-Infrastructure Initiatives》论文发表、《Relationship Between Internet Use and Cognitive Function Among Middle-Aged and Older Chinese Adults: 5-Year Longitudinal Study》论文发表。
第348轮补录来源：隐私、数据与主体权利；新增 《Israel split on rights to genetic privacy》论文发表、《China’s souped-up data privacy laws deter researchers》论文发表、《Data sharing threatens privacy》论文发表、《Intellectual property and data privacy: the hidden risks of AI》论文发表、《Protect privacy of mobile data》论文发表。
第349轮补录来源：伦理与人类增强边界；新增 《Ethics guidelines for human enhancement R&amp;D》论文发表、《Ethics and the human genome》论文发表、《Human-subjects research: The ethics squad》论文发表、《Take stock of research ethics in human genome editing》论文发表、《Audio long read: Hybrid brains – the ethics of transplanting human neurons into animals》论文发表。
第350轮补录来源：心理韧性与意义；新增 《Happiness is everything, or is it? Explorations on the meaning of psychological well-being.》论文发表、《The meaning in life questionnaire: Assessing the presence of and search for meaning in life.》论文发表、《Purpose in Life as a Predictor of Mortality Across Adulthood》论文发表、《Purpose in Life Is Associated With Mortality Among Community-Dwelling Older Persons》论文发表、《The Contours of Positive Human Health》论文发表。
第351轮补录来源：社会支持网络与长寿；新增 《Social Networks and Longevity: How Social Ties Influence Healthy Aging》论文发表、《Watch how social inequality impacts everything from health to longevity》论文发表、《Support cells in the brain promote longevity》论文发表、《Death Anxiety in Older Adults: The Role of Perceived Social Support and Psychological Hardiness Mediated by Resilience among Older Adults in Tehran》论文发表、《Black scientist network celebrates successes — but calls for more support》论文发表。
第352轮补录来源：家庭照护与长期护理；新增 《Caregiving as a Risk Factor for Mortality》论文发表、《Caregiver Burden》论文发表、《Differences between caregivers and noncaregivers in psychological health and physical health: A meta-analysis.》论文发表、《Caregiving, Mortality, and Mobility Decline&lt;subtitle&gt;The Health, Aging, and Body Composition (Health ABC) Study&lt;/subtitle&gt;》论文发表、《Family caregiving and emotional strain: associations with quality of life in a large national sample of middle-aged and older adults》论文发表。
第353轮补录来源：精神健康与生命意义；新增 《Subjective wellbeing, health, and ageing》论文发表、《The Lancet Commission on ending stigma and discrimination in mental health》论文发表、《Effect of Purpose in Life on the Relation Between Alzheimer Disease Pathologic Changes on Cognitive Function in Advanced Age》论文发表、《Global, regional, and national burden of 12 mental disorders in 204 countries and territories, 1990–2019: a systematic analysis for the Global Burden of Disease Study 2019》论文发表、《Interpersonal Processes in Depression》论文发表。
第354轮补录来源：认知老化与脑韧性；新增 《The Protective Power of Cognitive Reserve: Examining White Matter Integrity and Cognitive Function in the Aging Brain for Sustainable Cognitive Health》论文发表、《Plasticity of the aging brain: New directions in cognitive neuroscience》论文发表、《Speak, memory: on cognitive reserve and brain resilience》论文发表、《Cognitive resilience and severe Alzheimer’s disease neuropathology》论文发表、《MILD COGNITIVE IMPAIRMENT: AGING TO ALZHEIMER'S DISEASE》论文发表。
第355轮补录来源：注意力与执行功能；新增 《Improving fluid intelligence with training on working memory》论文发表、《Putting brain training to the test》论文发表、《Training and plasticity of working memory》论文发表、《Executive Functions》论文发表、《Do “Brain-Training” Programs Work?》论文发表。
第356轮补录来源：学习科学与技能积累；新增 《Genetic and environmental contributions to the acquisition of a motor skill》论文发表、《The time course of learning a visual skill》论文发表、《Covert skill learning in a cortical-basal ganglia circuit》论文发表、《Functional MRI evidence for adult motor cortex plasticity during motor skill learning》论文发表、《Blended Learning Improves Science Education》论文发表。
第357轮补录来源：创造力与创新系统；新增 《The Creativity Code <b>The Creativity Code: Art and Innovation in the Age of AI</b> <i>Marcus du Sautoy</i> Belknap Press, 2019. 320 pp.》论文发表、《A latent capacity for evolutionary innovation through exaptation in metabolic systems》论文发表、《Mysteries and Miseries of Creativity》论文发表、《How jazz boosts my creativity in physics》论文发表、《The creativity machine》论文发表。
第358轮补录来源：人类增强与超人类主义；新增 《Transhumanism Without Transindividuation in the Age Without Epochality: Stiegler, Vice, and Radical Human Enhancement》论文发表、《Nucleosome disruption and enhancement of activator binding by a human SW1/SNF complex》论文发表、《Mechanism of DNA-binding enhancement by the human T-cell leukaemia virus transactivator Tax》论文发表、《Performance enhancement: Superhuman athletes》论文发表、《Electronics: Silicon enhancement》论文发表。
第359轮补录来源：神经权利与脑数据治理；新增 《Ethical issues with brain-computer interfaces》论文发表、《Towards new human rights in the age of neuroscience and neurotechnology》论文发表、《Four ethical priorities for neurotechnologies and AI》论文发表、《Declaration on the ethics of brain–computer interfaces and augment intelligence》论文发表、《Big Brain Data: On the Responsible Use of Brain Data from Clinical and Consumer-Directed Neurotechnological Devices》论文发表。
第360轮补录来源：人工智能对齐与安全；新增 《Concrete Problems in AI Safety》论文发表、《The Alignment Problem from a Deep Learning Perspective》论文发表、《Safely Interruptible Agents》论文发表、《The Off-Switch Game》论文发表、《Scalable Agent Alignment via Reward Modeling: A Research Direction》论文发表。
第361轮补录来源：超级智能与奇点；新增 《Countering Superintelligence Misinformation》论文发表、《Superintelligence Skepticism as a Political Tool》论文发表、《The singularity graveyard》论文发表、《A press release from just before the singularity》论文发表、《Mr Singularity》论文发表。
第362轮补录来源：技术风险与双刃效应；新增 《Risks and benefits of dual-use research》论文发表、《Australia dials back effort to control ‘dual use’ research》论文发表、《Terror watchdog set up for ‘dual use’ biology》论文发表、《Genetic risk of smoking and alcohol use examined》论文发表、《Dual-use research needs international oversight》论文发表。
第363轮补录来源：文明转型与长期未来；新增 《A field guide to existential risk <b>The Precipice: Existential Risk and the Future of Humanity</b> <i>Toby Ord</i> Hachette, 2020. 480 pp.》论文发表、《Exponential Technology and The Singularity》论文发表、《What We Owe the Future: A Million Year View》论文发表、《What we owe (to) the present: Normative and practical challenges for strong longtermism》论文发表、《The Precipice. Existential Risk and the Future of Humanity, de T. Ord》论文发表。
第364轮补录来源：宇宙智能与扩张；新增 《‘Early dark energy’ fails to solve mystery of cosmic expansion》论文发表、《New results intensify debate over cosmic expansion rate》论文发表、《Ideal Mergers for Measuring Cosmic Expansion》论文发表、《Measuring Cosmic Expansion with a Lensed Supernova》论文发表、《Cosmic Expansion, Poco Adagio》论文发表。
第365轮补录来源：算力基础设施与智能；新增 《Tackling Climate Change with Machine Learning》论文发表、《Language Models are Few-Shot Learners》论文发表、《Training Compute-Optimal Large Language Models》论文发表、《Carbon Emissions and Large Neural Network Training》论文发表、《The Computational Limits of Deep Learning》论文发表。
第366轮补录来源：数据科学与健康；新增 《High-performance medicine: the convergence of human and artificial intelligence》论文发表、《Big Data and Machine Learning in Health Care》论文发表、《Predicting the Future — Big Data, Machine Learning, and Clinical Medicine》论文发表、《Scalable and accurate deep learning with electronic health records》论文发表、《Health intelligence: how artificial intelligence transforms population and personalized health》论文发表。
第367轮补录来源：数字孪生与预测健康；新增 《Building a modular and multi-cellular virtual twin of the synovial joint in Rheumatoid Arthritis》论文发表、《Digital twins in medicine》论文发表、《A Systematic Review of Digital Twin Technology for Home Care》论文发表、《A health digital twin framework for discrete event simulation based optimised critical care workflows》论文发表、《Realizing the Potential of Computer-Assisted Surgery by Embedding Digital Twin Technology》论文发表。
第368轮补录来源：生物年龄干预；新增 《Reversal of epigenetic aging and immunosenescent trends in humans》论文发表、《Alpha-ketoglutarate supplementation and BiologicaL agE in middle-aged adults (ABLE)—intervention study protocol》论文发表、《Measuring biological age using metabolomics》论文发表、《Transient and late-life rapamycin for healthspan extension》论文发表、《Effect of 6-Month Calorie Restriction on Biomarkers of Longevity, Metabolic Adaptation, and Oxidative Stress in Overweight Individuals: A Randomized Controlled Trial—Correction》论文发表。
第369轮补录来源：药物再利用与长寿；新增 《Rapamycin fed late in life extends lifespan in genetically heterogeneous mice》论文发表、《Drug repurposing: progress, challenges and recommendations》论文发表、《Rapamycin and Ageing: When, for How Long, and How Much?》论文发表、《Rapamycin As an Antiaging Therapeutic?: Targeting Mammalian Target of Rapamycin to Treat Hutchinson–Gilford Progeria and Neurodegenerative Diseases》论文发表、《A double whammy for aging? Rapamycin extends lifespan and inhibits cancer in inbred female mice》论文发表。
第370轮补录来源：营养干预与禁食；新增 《Nutrition, longevity and disease: From molecular mechanisms to interventions》论文发表、《Signalling through RHEB-1 mediates intermittent fasting-induced longevity in C. elegans》论文发表、《Investigating fasting for metabolic health and longevity》论文发表、《Feasting and fasting》论文发表、《Nutrigenomics and Personalized Nutrition in the Context of Aging》论文发表。
第371轮补录来源：运动与身体韧性；新增 《Effect of physical inactivity on major non-communicable diseases worldwide: an analysis of burden of disease and life expectancy》论文发表、《Does physical activity attenuate, or even eliminate, the detrimental association of sitting time with mortality? A harmonised meta-analysis of data from more than 1 million men and women》论文发表、《Effect of Structured Physical Activity on Prevention of Major Mobility Disability in Older Adults》论文发表、《Quantity and Quality of Exercise for Developing and Maintaining Cardiorespiratory, Musculoskeletal, and Neuromotor Fitness in Apparently Healthy Adults》论文发表、《Exercise benefits in cardiovascular disease: beyond attenuation of traditional risk factors》论文发表。
第372轮补录来源：睡眠与恢复；新增 《Aging, Subjective Sleep Quality, and Health Status: The Global Picture》论文发表、《1294 What Factors Influence Sleep Health During Recovery After Stroke?》论文发表、《1039 Diffusion Imaging Markers of Glymphatic Function in Veterans with Sleep Dysfunction and Mild Traumatic Brain Injury》论文发表、《0453 Hypoxia Affects Glymphatic Efficiency: Assessing Glymphatic Disruption in Obstructive Sleep Apnea Using Near-Infrared Spectroscopy》论文发表、《Can we monitor and enhance glymphatic clearance during sleep?》论文发表。
第373轮补录来源：压力与应激韧性；新增 《Interacting mediators of allostasis and allostatic load: towards an understanding of resilience in aging》论文发表、《Root of resilience under stress》论文发表、《Stress: The roots of resilience》论文发表、《Brain’s reward region helps to supply resilience in the face of stress》论文发表、《Stress-test the resilience of critical infrastructure》论文发表。
第374轮补录来源：环境毒素与去毒；新增 《Whitefly hijacks a plant detoxification gene that neutralizes plant toxins》论文发表、《Whitefly hijacks a plant detoxification gene that neutralizes plant toxins》论文发表、《The aryl hydrocarbon receptor links TH17-cell-mediated autoimmunity to environmental toxins》论文发表、《World’s first full-body PET scanner could aid drug development, monitor environmental toxins》论文发表、《A Class of Environmental and Endogenous Toxins Induces BRCA2 Haploinsufficiency and Genome Instability》论文发表。
第375轮补录来源：免疫治疗与肿瘤；新增 《Efficacy of zinc carnosine in the treatment of colorectal cancer and its potential in combination with immunotherapy in vivo》论文发表、《Cancer Immunotherapy: A Treatment for the Masses》论文发表、《Cancer immunotherapy: weak beats strong》论文发表、《Cancer Immunotherapy Booster》论文发表、《Challenges in targeting the tryptophan metabolism in cancer immunotherapy》论文发表。
第376轮补录来源：癌症预防与早筛；新增 《Early detection versus prevention in colorectal cancer screening: Methods estimates and public health implications》论文发表、《Huge lung-cancer screening campaign boosts early diagnosis》论文发表、《Early-onset cancer fuels calls for wider screening — but at what cost?》论文发表、《Accelerating discovery of cancer causes for prevention in the era of rising early-onset cancers》论文发表、《Metformin for aging and cancer prevention》论文发表。
第377轮补录来源：癌症治疗与治愈；新增 《The future of precision cancer therapy might be to try everything》论文发表、《Using Genes to Cure Cancer》论文发表、《Rationalizing rules for immunotherapy combination trials: About time for precision immunotherapy》论文发表、《Early results support base‐edited anti‐CD7 CAR T‐cell therapy in T‐cell ALL》论文发表、《High response rates with novel CAR T‐cell therapy for adults with advanced B‐cell ALL》论文发表。
第378轮补录来源：感染与病原体控制；新增 《Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis》论文发表、《COVID-19: towards controlling of a pandemic》论文发表、《The Lancet Commission on lessons for the future from the COVID-19 pandemic》论文发表、《Symposium: Public Health Preparedness》论文发表、《Assessing Public Health Emergency Preparedness: Concepts, Tools, and Challenges》论文发表。
第379轮补录来源：抗生素与抗微生物；新增 《Are non-antibiotic drugs contributing to antimicrobial resistance?》论文发表、《Antibiotic resistance racing downriver》论文发表、《Antibiotic resistance switched off》论文发表、《Diagnostic developers target antibiotic resistance》论文发表、《Antibiotic resistance marching across Europe》论文发表。
第380轮补录来源：疫苗与免疫保护；新增 《A Comparative Study on Immune Protection Efficacy: An HSV-1 Trivalent Antigen Subunit Vaccine Formulated with a Cellular Immunity-Inducing Adjuvant Versus an mRNA Vaccine》论文发表、《Malaria vaccine booster prolongs protection》论文发表、《Fungal sugars boost vaccine protection》论文发表、《Combo COVID-19 and Flu mRNA Vaccine Falls Short of Total Flu Protection》论文发表、《Discerning dengue vaccine protection》论文发表。
第381轮补录来源：器官芯片与药物评价；新增 《Organoids-on-a-chip》论文发表、《Human organs-on-chips for disease modelling, drug development and personalized medicine》论文发表、《Organs-on-chips: into the next decade》论文发表、《Vascularized organoids on a chip: strategies for engineering organoids with functional vasculature》论文发表、《Organs-on-chips at the frontiers of drug discovery》论文发表。
第382轮补录来源：类器官与疾病建模；新增 《The Imperative for Innovative Enteric Nervous System–Intestinal Organoid Co-Culture Models: Transforming GI Disease Modeling and Treatment》论文发表、《Advances in Cerebral Organoid Systems and their Application in Disease Modeling》论文发表、《Human airway organoid engineering as a step toward lung regeneration and disease modeling》论文发表、《Cancer modeling meets human organoid technology》论文发表、《This organoid can menstruate — and shows how tissue can repair itself》论文发表。
第383轮补录来源：3D生物打印与器官制造；新增 《3D extrusion bioprinting》论文发表、《A 3D bioprinting system to produce human-scale tissue constructs with structural integrity》论文发表、《3D bioprinting of collagen to rebuild components of the human heart》论文发表、《Bioprinting scale-up tissue and organ constructs for transplantation》论文发表、《Advances in 3D bioprinting of tissues/organs for regenerative medicine and in-vitro models》论文发表。
第384轮补录来源：细胞治疗与再生医学；新增 《Chimeric Antigen Receptor T Cells for Sustained Remissions in Leukemia》论文发表、《CAR T cell immunotherapy for human cancer》论文发表、《Axicabtagene Ciloleucel CAR T-Cell Therapy in Refractory Large B-Cell Lymphoma》论文发表、《The Principles of Engineering Immune Cells to Treat Cancer》论文发表、《Adoptive cell transfer as personalized immunotherapy for human cancer》论文发表。
第385轮补录来源：基因治疗与体内编辑；新增 《CRISPR-Cas9 In Vivo Gene Editing for Transthyretin Amyloidosis》论文发表、《CRISPR-Cas9 Gene Editing for Sickle Cell Disease and β-Thalassemia》论文发表、《Single-Dose Gene-Replacement Therapy for Spinal Muscular Atrophy》论文发表、《Therapeutic in vivo delivery of gene editing agents》论文发表、《Search-and-replace genome editing without double-strand breaks or donor DNA》论文发表。
第386轮补录来源：蛋白质工程与设计；新增 《De novo protein design—From new structures to programmable functions》论文发表、《Structure and Protein Design of a Human Platelet Function Inhibitor》论文发表、《Structure and Protein Design of a Human Platelet Function Inhibitor》论文发表、《Design and engineering of an O2 transport protein》论文发表、《Role of the Biomolecular Energy Gap in Protein Design, Structure, and Evolution》论文发表。
第387轮补录来源：RNA治疗与mRNA医学；新增 《Tissue- and age-dependent expression of RNA-binding proteins that influence mRNA turnover and translation》论文发表、《Identifying lncRNA–miRNA–mRNA networks to investigate Alzheimer’s disease pathogenesis and therapy strategy》论文发表、《Tumours might be sensitized to immune therapy by COVID mRNA vaccines》论文发表、《mRNA therapy is safe for treating the inherited metabolic condition propionic acidaemia》论文发表、《Targeted mRNA therapy tackles deadly pregnancy condition in mice》论文发表。
第388轮补录来源：精准医疗与个体化；新增 《Personalized medicine: Special treatment》论文发表、《Metagenomics and Personalized Medicine》论文发表、《Personalized ranges for blood-test results enable precision diagnostics》论文发表、《Britain to launch personalized medicine project》论文发表、《Redefining Clinical Trials: The Age of Personalized Medicine》论文发表。
第389轮补录来源：生物标志物与寿命预测；新增 《The role of Hsp70 in oxi-inflamm-aging and its use as a potential biomarker of lifespan》论文发表、《DNA methylation entropy is a biomarker for aging》论文发表、《NODULE DILEMMA: PROTEOMIC BIOMARKER DISCORDANCE WITH PET RESULTS》论文发表、《A novel clinical biomarker-based Physiology Healthy Aging Index and risk of all-cause and cause-specific mortality: A 20-year prospective cohort study》论文发表、《Neuroimaging-derived brain-age: an ageing biomarker?》论文发表。
第390轮补录来源：影像诊断与健康监测；新增 《Dermatologist-level classification of skin cancer with deep neural networks》论文发表、《International evaluation of an AI system for breast cancer screening》论文发表、《End-to-end lung cancer screening with three-dimensional deep learning on low-dose chest computed tomography》论文发表、《A survey on deep learning in medical image analysis》论文发表、《CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning》论文发表。
第391轮补录来源：可穿戴设备与连续监测；新增 《Use of Wearable Monitoring Devices to Change Health Behavior》论文发表、《Silk-based wearable devices for health monitoring and medical treatment》论文发表、《Use of Wearable Monitoring Devices to Change Health Behavior—Reply》论文发表、《Meaningful digital biomarkers derived from wearable sensors to predict daily fatigue in multiple sclerosis patients and healthy controls》论文发表、《A wearable ultrasound patch for continuous heart imaging》论文发表。
第392轮补录来源：远程医疗与数字照护；新增 《Virtually Perfect? Telemedicine for Covid-19》论文发表、《Telehealth transformation: COVID-19 and the rise of virtual care》论文发表、《Virtual Care, Telemedicine Visits, and Real Connection in the Era of COVID-19》论文发表、《On-Demand, Virtual Health Care During COVID-19: Clinician Redeployment and Telemedicine Utilization in a Children's Health System》论文发表、《Digital health equity for older populations》论文发表。
第393轮补录来源：健康数据互操作；新增 《Data standards urged》论文发表、《Minimum standards set out for gene-expression data》论文发表、《UK's food standards agency will report to health minister》论文发表、《Progress being made on standards for use in data sharing》论文发表、《Data sharing: standards are on the rise》论文发表。
第394轮补录来源：健康经济学与价值；新增 《Updating Cost-Effectiveness — The Curious Resilience of the $50,000-per-QALY Threshold》论文发表、《Recommendations for Conduct, Methodological Practices, and Reporting of Cost-effectiveness Analyses》论文发表、《The value of value in health economic modelling》论文发表、《History of the international societies in health technology assessment: International Society for Technology Assessment in Health Care and Health Technology Assessment International》论文发表、《RS2 Cost-Effectiveness of End-of-Life, Life-Extending Interventions: NICE's Cost-Effectiveness Threshold Explored》论文发表。
第395轮补录来源：老龄化社会与制度；新增 《APOCALYPSE NO: Population Aging and The Future of Health Care Systems》论文发表、《Navigating the long road to long‐term care funding reform》论文发表、《World Health Organisation, Ageing and Work Capacity, WHO Technical Report Series 835, World Health Organisation, Geneva, 1993, 49 pp., pbk Sw.F. 10, price in developing countries Sw.F. 7, ISBN 9 241 20835 X.》论文发表、《The World Health Organization perspective on gender, ageing and health》论文发表、《World Health Report 2000: Challenging a World View》论文发表。
第396轮补录来源：长期护理与照护体系；新增 《Different voltage-dependent thresholds for inducing long-term depression and long-term potentiation in slices of rat visual cortex》论文发表、《Short-term tests validate long-term estimates of climate change》论文发表、《Long-distance long-term depression》论文发表、《Long-term memory gets wiped》论文发表、《Aplysia CREB2 represses long-term facilitation: Relief of repression converts transient facilitation into long-term functional and structural change》论文发表。
第397轮补录来源：临终关怀与死亡文化；新增 《The Lancet Commission on Palliative Care and Pain Relief—findings, recommendations, and future directions》论文发表、《Prioritising palliative care》论文发表、《Closing the divide: the Harvard Global Equity Initiative–Lancet Commission on global access to pain control and palliative care》论文发表、《Paediatric palliative care》论文发表、《Report of the Lancet Commission on the Value of Death: bringing death back into life》论文发表。
第398轮补录来源：永生哲学与意义；新增 《Immortality and Meaning: Reflections on the Makropulos Debate》论文发表、《Death, Immortality, and Meaning in Life》论文发表、《Reflections on Meaning and Immortality》论文发表、《IMMORTALITY WITHOUT BOREDOM》论文发表、《IMMORTALITY, HUMAN NATURE, THE VALUE OF LIFE AND THE VALUE OF LIFE EXTENSION》论文发表。
第399轮补录来源：未来文明愿景；新增 《Vision of the future》论文发表、《Future vision》论文发表、《A vision of our transport future》论文发表、《Vision of a personal genomics future》论文发表、《Ancient civilization goes online》论文发表。
第400轮补录来源：人类基础设施总体评估；新增 《Social determinants of health inequalities》论文发表、《Global burden of 87 risk factors in 204 countries and territories, 1990–2019: a systematic analysis for the Global Burden of Disease Study 2019》论文发表、《Global, regional, and national age-sex-specific mortality for 282 causes of death in 195 countries and territories, 1980–2017: a systematic analysis for the Global Burden of Disease Study 2017》论文发表、《Universal Health Coverage: realistic and achievable?》论文发表、《Toward a theory-led meta-framework for implementing health system resilience analysis studies: a systematic review and critical interpretive synthesis》论文发表。
第401轮补录来源：胶质淋巴系统与脑废弃物清除；新增 《Waste clearance shapes aging brain health》论文发表、《Neuronal activity drives glymphatic waste clearance》论文发表、《Impaired glymphatic clearance as a mechanistic link between brain aging and neurodegenerative disease pathogenesis》论文发表、《Imaging of brain clearance pathways via MRI assessment of the glymphatic system》论文发表、《Brain glymphatic clearance is impaired in a rat model of cirrhosis》论文发表。
第402轮补录来源：脑膜淋巴系统与脑免疫边界；新增 《Compartmentalized ocular lymphatic system mediates eye–brain immunity》论文发表、《Role of meningeal lymphatic vessels in brain homeostasis》论文发表、《Meningeal lymphatic dysfunction exacerbates traumatic brain injury pathogenesis》论文发表、《Disrupted drainage in the aging brain: Meningeal lymphatic decline as a convergent axis of vulnerability》论文发表、《Meningeal lymphatic flow slows after mild traumatic brain injury》论文发表。
第403轮补录来源：血脑屏障衰老与转运维持；新增 《Aging and the blood-brain barrier》论文发表、《Healthy aging and the blood–brain barrier》论文发表、《Copper transport to the brain by the blood-brain barrier and blood-CSF barrier》论文发表、《Peptide transport across the blood-brain barrier》论文发表、《Development, maintenance and disruption of the blood-brain barrier》论文发表。
第404轮补录来源：脑脊液动力学与神经稳态；新增 《Cerebrospinal fluid dynamics and brain function regulation: from homeostasis to neurological disorders》论文发表、《Pulsatile Cerebrospinal Fluid Dynamics in the Human Brain》论文发表、《Neuronal dynamics direct cerebrospinal fluid perfusion and brain clearance》论文发表、《AQP1 and AQP4 Contribution to Cerebrospinal Fluid Homeostasis》论文发表、《The Potential Roles of Blood–Brain Barrier and Blood–Cerebrospinal Fluid Barrier in Maintaining Brain Manganese Homeostasis》论文发表。
第405轮补录来源：昼夜节律与生物钟老化；新增 《AGING AND CIRCADIAN CLOCK》论文发表、《0680 Body Clock and Aging: Relationships of Circadian Rhythm with Sleep Quality, Mental Health and Geriatric Conditions》论文发表、《Aging attenuates the ovarian circadian rhythm》论文发表、《Crosstalk Between Aging, Circadian Rhythm, and Melatonin》论文发表、《CLOCK Acetylates ASS1 to Drive Circadian Rhythm of Ureagenesis》论文发表。
第406轮补录来源：睡眠结构与恢复性睡眠；新增 《Subjective sleep quality and sleep architecture in aging》论文发表、《Association between restorative sleep and sleep fragmentation in obstructive sleep apnea》论文发表、《Severe sleep disordered breathing disrupts sleep architecture》论文发表、《Resilience and Readiness through Restorative Sleep》论文发表、《Effects of oxybate on sleep, sleep architecture, and disrupted nighttime sleep》论文发表。
第407轮补录来源：深睡眠与记忆巩固；新增 《How Aging Affects Sleep-Dependent Memory Consolidation?》论文发表、《Sleep-dependent prospective memory consolidation is impaired with aging》论文发表、《046 Sleep-dependent prospective memory consolidation is impaired with aging》论文发表、《Sleep and Social Memory Consolidation》论文发表、《Sleep enhances memory consolidation in children》论文发表。
第408轮补录来源：成年神经发生与脑修复；新增 《Adult neurogenesis in brain repair: cellular plasticity vs. cellular replacement》论文发表、《Adult neurogenesis 20 years later: physiological function vs. brain repair》论文发表、《Adult neurogenesis and its promise as a hope for brain repair》论文发表、《Parkinson's disease, aging and adult neurogenesis: Wnt/β‐catenin signalling as the key to unlock the mystery of endogenous brain repair》论文发表、《Adult Hippocampal Neurogenesis in Aging and Alzheimer's Disease》论文发表。
第409轮补录来源：突触可塑性与长期记忆；新增 《Translational Control by MAPK Signaling in Long-Term Synaptic Plasticity and Memory》论文发表、《Long-term synaptic plasticity in hippocampal interneurons》论文发表、《Visual recognition memory, manifested as long-term habituation, requires synaptic plasticity in V1》论文发表、《Methamphetamine Inhibits Long-Term Memory Acquisition and Synaptic Plasticity by Evoking Endoplasmic Reticulum Stress》论文发表、《Sleep and the Price of Plasticity: From Synaptic and Cellular Homeostasis to Memory Consolidation and Integration》论文发表。
第410轮补录来源：髓鞘修复与再髓鞘化；新增 《Induction of myelin-associated glycoprotein mRNA in experimental remyelination》论文发表、《Remyelination alters the pattern of myelin in the cerebral cortex》论文发表、《Targeting the Subventricular Zone to Promote Myelin Repair in the Aging Brain》论文发表、《Role of Multifocal Visually Evoked Potential as a Biomarker of Demyelination, Spontaneous Remyelination, and Myelin Repair in Multiple Sclerosis》论文发表、《Microglia promote remyelination independent of their role in clearing myelin debris》论文发表。
第411轮补录来源：轴突再生与外周神经修复；新增 《Spinal Cord Repair: Strategies to Promote Axon Regeneration》论文发表、《Neuronal maturation and axon regeneration: unfixing circuitry to enable repair》论文发表、《Nerve regeneration and nerve repair》论文发表、《Local delivery of FK506 to injured peripheral nerve enhances axon regeneration after surgical nerve repair in rats》论文发表、《PTEN inhibition and axon regeneration and neural repair》论文发表。
第412轮补录来源：脊髓损伤恢复与神经重建；新增 《Neurorehabilitation of Spinal Cord Injury》论文发表、《Spinal cord injury and bladder recovery》论文发表、《The physiological basis of neurorehabilitation - locomotor training after spinal cord injury》论文发表、《Disuse plasticity limits spinal cord injury recovery》论文发表、《Neurologic recovery after traumatic spinal cord injury: data from the model spinal cord injury systems》论文发表。
第413轮补录来源：外周神经病变与感觉保留；新增 《Macrophages protect against sensory axon loss in peripheral neuropathy》论文发表、《Cardiovascular autonomic and peripheral sensory neuropathy in women with obesity》论文发表、《Peripheral Sensory Neuropathy Associates With Micro- or Macroangiopathy》论文发表、《Integrins protect sensory neurons in models of paclitaxel-induced peripheral sensory neuropathy》论文发表、《Neurotrophin-3 reverses experimental cisplatin-induced peripheral sensory neuropathy》论文发表。
第414轮补录来源：前庭平衡与空间定向；新增 《Vestibular Deficits in Neurodegenerative Disorders: Balance, Dizziness, and Spatial Disorientation》论文发表、《Impairment of human spatial orientation in the horizontal, but not the vertical plane, due to aging, cognitive decline, or chronic peripheral vestibular loss》论文发表、《Perspectives on Aging Vestibular Function》论文发表、《Aging with Cerebral Small Vessel Disease and Dizziness: The Importance of Undiagnosed Peripheral Vestibular Disorders》论文发表、《Vestibular and Balance Rehabilitation Therapy》论文发表。
第415轮补录来源：听力保存与耳蜗健康；新增 《Molecular marker of cochlear aging and hearing loss in primates》论文发表、《Hearing preservation in cochlear implantation》论文发表、《Hearing Preservation in Elderly Cochlear Implant Recipients》论文发表、《Residual Hearing Preservation After Pediatric Cochlear Implantation》论文发表、《Hearing Preservation in Pediatric Cochlear Implantation》论文发表。
第416轮补录来源：人工耳蜗与听觉康复；新增 《Cochlear Implant Artifacts Removal in EEG-Based Objective Auditory Rehabilitation Assessment》论文发表、《Adult cochlear implant rehabilitation》论文发表、《Auditory Rehabilitation Following Cochlear Implantation》论文发表、《Objective electroencephalography-based assessment for auditory rehabilitation of pediatric cochlear implant users》论文发表、《Auditory rehabilitation with a cochlear implant improves cognitive performance》论文发表。
第417轮补录来源：视觉修复与视网膜重建；新增 《Low vision: Rescue, regeneration, restoration and rehabilitation》论文发表、《Synaptic repair and vision restoration in advanced degenerating eyes by transplantation of retinal progenitor cells》论文发表、《Focal electrical stimulation of human retinal ganglion cells for vision restoration》论文发表、《Chemical reprogramming of fibroblasts into retinal pigment epithelium cells for vision restoration》论文发表、《In vivo Regeneration of Ganglion Cells for Vision Restoration in Mammalian Retinas》论文发表。
第418轮补录来源：视网膜细胞治疗与视觉；新增 《Recent Progress in Photoreceptor Cell-Based Therapy for Degenerative Retinal Disease》论文发表、《Photoreceptor cell rescue in retinal degeneration (rd) mice by in vivo gene therapy》论文发表、《Retinal repair by transplantation of photoreceptor precursors》论文发表、《Mesenchymal stem cell therapy for retinal ganglion cell neuroprotection and axon regeneration》论文发表、《Retinal regeneration and stem cell therapy in retinitis pigmentosa》论文发表。
第419轮补录来源：晶状体再生与白内障修复；新增 《Lens regeneration in children》论文发表、《An attempt at natural lens regeneration in congenital cataract surgery》论文发表、《Lens and Cataract》论文发表、《Lens and Cataract》论文发表、《Cataract surgery and lens implantation》论文发表。
第420轮补录来源：干眼与眼表稳态维持；新增 《Dry Eye Management: Targeting the Ocular Surface Microenvironment》论文发表、《Dry eye and ocular surface disease》论文发表、《Lacrimal Gland, Ocular Surface, and Dry Eye》论文发表、《Ocular Surface Ion Transport and Dry Eye Disease》论文发表、《Ocular surface immune cell diversity in dry eye disease》论文发表。
第421轮补录来源：嗅觉味觉与化学感觉保存；新增 《SMELL AND TASTE COMPLAINTS》论文发表、《Aging inhibits olfactory recovery from traumatic olfactory system injury》论文发表、《Olfactory dysfunction in aging and neurodegenerative diseases》论文发表、《Taste, olfactory and trigeminal neophobia in rats with forebrain lesions》论文发表、《Aging and Olfactory Training: A Scoping Review》论文发表。
第422轮补录来源：吞咽安全与气道保护；新增 《Swallow Screen Associated With Airway Protection and Dysphagia After Acute Stroke》论文发表、《Training in Swallowing Prevents Aspiration Pneumonia in Stroke Patients with Dysphagia》论文发表、《Aspiration and dysphagia screening in acute stroke – the Gugging Swallowing Screen revisited》论文发表、《Dysphagia and Aspiration》论文发表、《Prevalence and Severity of Dysphagia Using Videofluoroscopic Swallowing Study in Patients with Aspiration Pneumonia》论文发表。
第423轮补录来源：言语与沟通康复；新增 《Combining Aerobic Exercise and Speech Language Treatment for Aphasia Rehabilitation: A Case Study》论文发表、《Event-related potentials indicate bi-hemispherical changes in speech sound processing during aphasia rehabilitation》论文发表、《Applying the Rehabilitation Treatment Specification System to Functional Communication Treatment Approaches for Aphasia》论文发表、《Computerised speech and language therapy in post-stroke aphasia》论文发表、《Plastic Changes Following Imitation-Based Speech and Language Therapy for Aphasia》论文发表。
第424轮补录来源：失语症与语言功能恢复；新增 《Structural networks, language deficits, and aphasia recovery》论文发表、《Predicting Language Recovery Outcomes in Individuals with Aphasia》论文发表、《Functional networks, language impairment and recovery after treatment in aphasia》论文发表、《Neuroplasticity and Functional Recovery after Intensive Language Therapy in Chronic Post Stroke Aphasia: Which Factors Are Relevant?》论文发表、《Intensity of Aphasia Therapy, Impact on Recovery》论文发表。
第425轮补录来源：运动康复与神经重塑；新增 《Neuroplasticity and Motor Rehabilitation in Multiple Sclerosis》论文发表、《Neuroplasticity in the context of motor rehabilitation after stroke》论文发表、《Macrostructural Cerebellar Neuroplasticity Correlates With Motor Recovery After Stroke》论文发表、《Virtual reality modulating dynamics of neuroplasticity: Innovations in neuro-motor rehabilitation》论文发表、《Rehabilitation drives post-stroke motor recovery》论文发表。
第426轮补录来源：平衡与跌倒预防；新增 《Falls Prevention for Older Adults》论文发表、《Prevention of Falls in Older Adults》论文发表、《Prevention of Falls in Community-Dwelling Older Adults》论文发表、《PERCEIVED BALANCE PREDICTS FALLS IN COMMUNITY-DWELLING OLDER ADULTS》论文发表、《Older Adults’ Perceptions of Falls and Falls Prevention: An Interview-Based Study》论文发表。
第427轮补录来源：衰弱与多重慢病；新增 《A Novel Longitudinal Proteomic Aging Index Predicts Mortality, Multimorbidity, and Frailty in Older Adults》论文发表、《ASSOCIATION OF FRAILTY WITH FIFTEEN-YEAR MORTALITY IN OLDER ADULTS WITHOUT MULTIMORBIDITY》论文发表、《Beyond Unidirectional Decline: Identifying Nonlinear Frailty and Multimorbidity Trajectories in Older Adults》论文发表、《MULTIMORBIDITY PATTERNS PROVIDE ADDED PROGNOSTIC INFORMATION BEYOND FRAILTY STATUS IN OLDER ADULTS》论文发表、《Frailty in Older Adults》论文发表。
第428轮补录来源：肌少症与肌肉功能；新增 《Dietary Patterns, Skeletal Muscle Health, and Sarcopenia in Older Adults》论文发表、《THE ROLE OF SKELETAL MUSCLE MYOSTATIN IN SARCOPENIA IN OLDER ADULTS》论文发表、《Association of skeletal muscle oxidative capacity with muscle function, sarcopenia-related exercise performance, and intramuscular adipose tissue in older adults》论文发表、《Sarcopenia and Cognitive Decline in Older Adults: Targeting the Muscle–Brain Axis》论文发表、《Traditional Chinese exercises on muscle strength, muscle mass, and physical function in older adults with sarcopenia: a systematic review and meta-analysis》论文发表。
第429轮补录来源：骨质疏松与骨骼韧性；新增 《Osteoporosis, fragility fracture, and periodontal disease》论文发表、《Osteoporosis survey: GP management post fragility fracture》论文发表、《Beyond bone density: toward an integrated bone– muscle–function framework for fragility fracture prevention》论文发表、《OFELIA: Prevalence of Osteoporosis in Fragility Fracture Patients》论文发表、《Osteoporosis Therapy: Bone Modeling during Growth and Aging》论文发表。
第430轮补录来源：软骨与关节保存；新增 《Aging, articular cartilage chondrocyte senescence and osteoarthritis》论文发表、《Specific premature epigenetic aging of cartilage in osteoarthritis》论文发表、《Transthyretin and amyloid in cartilage aging and osteoarthritis》论文发表、《Targeting cartilage aging as osteoarthritis therapeutics by drug repurposing》论文发表、《Fibulin-3 in joint aging and osteoarthritis pathogenesis》论文发表。
第431轮补录来源：肌腱韧带修复；新增 《Role of Biomaterials and Controlled Architecture on Tendon/Ligament Repair and Regeneration》论文发表、《Tendon and Ligament Healing and Current Approaches to Tendon and Ligament Regeneration》论文发表、《Tendon Healing: Repair and Regeneration》论文发表、《Fibrous Systems as Potential Solutions for Tendon and Ligament Repair, Healing, and Regeneration》论文发表、《Xenografts for tendon and ligament repair》论文发表。
第432轮补录来源：牙髓与牙齿再生；新增 《Tooth Repair and Regeneration: Potential of Dental Stem Cells》论文发表、《The Regenerative Potential of bFGF in Dental Pulp Repair and Regeneration》论文发表、《Stem cells and the dental pulp: potential roles in dentine regeneration and repair》论文发表、《A comparison between adipose tissue and dental pulp as sources of MSCs for tooth regeneration》论文发表、《Injectable Xenogeneic Dental Pulp Decellularized Extracellular Matrix Hydrogel Promotes Functional Dental Pulp Regeneration》论文发表。
第433轮补录来源：口腔健康与长寿；新增 《Aging, longevity and health》论文发表、《Oral Health in Healthy Aging》论文发表、《Oral Microbiome, Oral Health and Systemic Health: A Multidirectional Link》论文发表、《Aging envisage imbalance of the periodontium: A keystone in oral disease and systemic health》论文发表、《Aging and Longevity》论文发表。
第434轮补录来源：肠脑轴与认知健康；新增 《Brain Aging and Gut–Brain Axis》论文发表、《Is aging preprogrammed? Observations from the brain/gut axis》论文发表、《The Impact of Microbiota-Gut-Brain Axis on Diabetic Cognition Impairment》论文发表、《Aging Microbiota-Gut-Brain Axis in Stroke Risk and Outcome》论文发表、《The brain-gut-muscle axis: a mechanism for exercise-mediated protection in brain aging》论文发表。
第435轮补录来源：肠道屏障与通透性；新增 《Intestinal barrier permeability: the influence of gut microbiota, nutrition, and exercise》论文发表、《Intestinal Barrier and Permeability in Health, Obesity and NAFLD》论文发表、《The Intestinal Barrier and Current Techniques for the Assessment of Gut Permeability》论文发表、《Intestinal Barrier Permeability in Allergic Diseases》论文发表、《Gut Microbiota and Intestinal Trans-Epithelial Permeability》论文发表。
第436轮补录来源：肠道微生物代谢与衰老；新增 《THE GUT MICROBIOME AND AGING》论文发表、《Gut microbiome and health: mechanistic insights》论文发表、《Gut Microbiome and Microbiome-Derived Metabolites in Patients with End-Stage Kidney Disease》论文发表、《The Gut Microbiome, Aging, and Longevity: A Systematic Review》论文发表、《STRESS, STEM CELLS, AND THE GUT MICROBIOME—IMPLICATIONS FOR AGING》论文发表。
第437轮补录来源：短链脂肪酸与健康寿命；新增 《Short-chain fatty acids in fetal development and metabolism》论文发表、《Short-chain fatty acids》论文发表、《Short-Chain Fatty Acids, Maternal Microbiota and Metabolism in Pregnancy》论文发表、《Modulation of Adipocyte Metabolism by Microbial Short-Chain Fatty Acids》论文发表、《Effect of lactulose on the metabolism of short-chain fatty acids》论文发表。
第438轮补录来源：NAD+代谢与去乙酰化酶；新增 《SnapShot: Sirtuins, NAD, and Aging》论文发表、《NAD+ and sirtuins in aging and disease》论文发表、《The Many Faces of Sirtuins: Coupling of NAD metabolism, sirtuins and lifespan》论文发表、《NAD metabolism: Implications in aging and longevity》论文发表、《Regulation of NAD+ metabolism in aging and disease》论文发表。
第439轮补录来源：AMPK与代谢韧性；新增 《Metabolic pathways and therapeutics to promote resilience, rehabilitation and delayed aging》论文发表、《228-LB: Metformin Alleviates Aging-Associated Metabolic Disorders through Intestinal AMPK-Mediated Gut Microbiome Alteration》论文发表、《Phosphodiesterase 4 inhibitor activates AMPK-SIRT6 pathway to prevent aging-related adipose deposition induced by metabolic disorder》论文发表、《SDHAF1 confers metabolic resilience to aging hematopoietic stem cells by promoting mitochondrial ATP production》论文发表、《AMPK at the Nexus of Energetics and Aging》论文发表。
第440轮补录来源：mTOR通路与寿命调控；新增 《mTOR as Regulator of Lifespan, Aging, and Cellular Senescence: A Mini-Review》论文发表、《The Crucial Roles of Phospholipids in Aging and Lifespan Regulation》论文发表、《BMAL1-dependent regulation of the mTOR signaling pathway delays aging》论文发表、《mTOR links nutrients, inflammaging and lifespan》论文发表、《The role of lipid metabolism in aging, lifespan regulation, and age‐related disease》论文发表。
第441轮补录来源：衰老细胞清除与衰老抑制药物；新增 《Senolytics combat COVID-19 in aging》论文发表、《Senolytics rejuvenate aging cardiomyopathy in human cardiac organoids》论文发表、《Senolytics under scrutiny in the quest to slow aging》论文发表、《Senolytics: A Translational Bridge Between Cellular Senescence and Organismal Aging》论文发表、《Nutritional senolytics and senomorphics: Implications to immune cells metabolism and aging – from theory to practice》论文发表。
第442轮补录来源：衰老相关分泌表型调控；新增 《Endothelial senescence-associated secretory phenotype (SASP) is regulated by Makorin-1 ubiquitin E3 ligase》论文发表、《A Senescence Associated Secretory Phenotype (SASP) in Indolent Systemic Mastocytosis Compared to Healthy Controls》论文发表、《Abstract 11559: Prognostic Significance of Senescence-Associated Secretory Phenotype (SASP) Biomarkers in Heart Failure (HF)》论文发表、《Single-cell transcriptomics identifies senescence-associated secretory phenotype (SASP) features of testicular aging in human》论文发表、《The microRNA-34a-Induced Senescence-Associated Secretory Phenotype (SASP) Favors Vascular Smooth Muscle Cells Calcification》论文发表。
第443轮补录来源：蛋白稳态网络与应激响应；新增 《Mitochondrial Stress Restores the Heat Shock Response and Prevents Proteostasis Collapse during Aging》论文发表、《Proteostasis and aging》论文发表、《Mastering organismal aging through the endoplasmic reticulum proteostasis network》论文发表、《Hsf1 promotes hematopoietic stem cell fitness and proteostasis in response to ex vivo culture stress and aging》论文发表、《Exploiting inter-tissue stress signaling mechanisms to preserve organismal proteostasis during aging》论文发表。
第444轮补录来源：自噬与溶酶体清除；新增 《Dnase2a Deficiency Uncovers Lysosomal Clearance of Damaged Nuclear DNA via Autophagy》论文发表、《Aging: Central role for autophagy and the lysosomal degradative system》论文发表、《Asparagine prevents intestinal stem cell aging via the autophagy‐lysosomal pathway》论文发表、《Staphylococcus aureus Avoids Autophagy Clearance of Bovine Mammary Epithelial Cells by Impairing Lysosomal Function》论文发表、《“LRRK2: Autophagy and Lysosomal Activity”》论文发表。
第445轮补录来源：线粒体自噬与质量控制；新增 《Mitophagy: At the heart of mitochondrial quality control in cardiac aging and frailty》论文发表、《Renal aging and mitochondrial quality control》论文发表、《The role of mitochondrial quality surveillance in skin aging: Focus on mitochondrial dynamics, biogenesis and mitophagy》论文发表、《Inflammation and mitophagy are mitochondrial checkpoints to aging》论文发表、《SIRT4 interacts with OPA1 and regulates mitochondrial quality control and mitophagy》论文发表。
第446轮补录来源：线粒体动力学与融合分裂；新增 《Mitochondrial Dynamics — Mitochondrial Fission and Fusion in Human Diseases》论文发表、《Mitochondrial fusion/fission dynamics in neurodegeneration and neuronal plasticity》论文发表、《Mitochondrial Fission, Fusion, and Stress》论文发表、《Aging shifts mitochondrial dynamics toward fission to promote germline stem cell loss》论文发表、《Mitochondrial Dynamics: Fission and Fusion in Fate Determination of Mesenchymal Stem Cells》论文发表。
第447轮补录来源：氧化应激与氧化还原信号；新增 《Extracellular Redox State: Refining the Definition of Oxidative Stress in Aging》论文发表、《Oxidative stress and aberrant signaling in aging and cognitive decline》论文发表、《Reactive Oxygen Species, Vascular Oxidative Stress, and Redox Signaling in Hypertension》论文发表、《Oxidative stress and aging》论文发表、《Ca2+ signaling, mitochondria and sensitivity to oxidative stress in aging astrocytes》论文发表。
第448轮补录来源：脂质代谢与膜稳态；新增 《Lipid Metabolism at Membrane Contacts: Dynamics and Functions Beyond Lipid Homeostasis》论文发表、《Membrane lipid homeostasis in bacteria》论文发表、《Lipid metabolism in homeostasis and disease》论文发表、《Lipid-anchored proteasomes control membrane protein homeostasis》论文发表、《Lipid landscapes and pipelines in membrane homeostasis》论文发表。
第449轮补录来源：胆固醇与心血管老化；新增 《Aging-Associated miR-217 Aggravates Atherosclerosis and Promotes Cardiovascular Dysfunction》论文发表、《Remnant Cholesterol and Triglyceride-Rich Lipoproteins in Atherosclerosis Progression and Cardiovascular Disease》论文发表、《CARDIOVASCULAR HEALTH AND SUCCESSFUL AGING: THE MULTI-ETHNIC STUDY OF ATHEROSCLEROSIS》论文发表、《Subclinical Cardiovascular Disease and Atherosclerosis Are Not Inevitable Consequences of Aging》论文发表、《P3456Total cholesterol, low-density lipoprotein cholesterol, non-high-density lipoprotein cholesterol in atherosclerosis cardiovascular disease and cancer in Chinese male》论文发表。
第450轮补录来源：血压控制与血管老化；新增 《NETosis Drives Blood Pressure Elevation and Vascular Dysfunction in Hypertension》论文发表、《Spironolactone and Hydrochlorothiazide Decrease Vascular Stiffness and Blood Pressure in Geriatric Hypertension》论文发表、《Dietary Approaches to Stop Hypertension Dietary Intervention Improves Blood Pressure and Vascular Health in Youth With Elevated Blood Pressure》论文发表、《Phospholemman Phosphorylation Regulates Vascular Tone, Blood Pressure, and Hypertension in Mice and Humans》论文发表、《Hypertension and Ambulatory Blood Pressure》论文发表。
第451轮补录来源：动脉硬化与脉搏波速；新增 《Arterial Stiffness and Pulse Wave Velocity: Problems with Terminology》论文发表、《Chest Pulse-Wave Velocity: A Novel Approach to Assess Arterial Stiffness》论文发表、《Heart-Ankle Pulse Wave Velocity Is Superior to Brachial-Ankle Pulse Wave Velocity in Detecting Aldosterone-Induced Arterial Stiffness》论文发表、《HEART-FEMORAL PULSE WAVE VELOCITY IS A STRONGER MARKER OF ARTERIAL AGING THAN CAROTID-FEMORAL PULSE WAVE VELOCITY》论文发表、《SP304NON INVASIVE ASSESSMENT OF ARTERIAL STIFFNESS USING PULSE WAVE VELOCITY IN NEPHROLOGY OUTPATIENTS》论文发表。
第452轮补录来源：内皮功能与一氧化氮；新增 《Endothelial S100A1 Modulates Vascular Function via Nitric Oxide》论文发表、《ZFYVE21 promotes endothelial nitric oxide signaling and vascular barrier function in the kidney during aging》论文发表、《Endothelial Nitric Oxide Synthase in Vascular Disease》论文发表、《Vascular Endothelial Growth Factor Signaling to Endothelial Nitric Oxide Synthase》论文发表、《ZFYVE21 Sustains Akt-Endothelial Nitric Oxide Synthase (ENOS) Signaling to Promote Vascular Barrier Function in the Kidneys during Aging》论文发表。
第453轮补录来源：心脏再生与心肌细胞更新；新增 《Cardiomyocyte Regeneration》论文发表、《Pkm2 Regulates Cardiomyocyte Cell Cycle and Promotes Cardiac Regeneration》论文发表、《Abstract 131: Cardiomyocyte Renewal and Cardiac Outcomes Following Injury in Young Swine》论文发表、《Regulation of cardiomyocyte fate plasticity: a key strategy for cardiac regeneration》论文发表、《Metabolic Changes Associated With Cardiomyocyte Dedifferentiation Enable Adult Mammalian Cardiac Regeneration》论文发表。
第454轮补录来源：心脏纤维化与心肌重塑；新增 《Sacubitril/Valsartan, Cardiac Fibrosis, and Remodeling in Heart Failure》论文发表、《PUFA Supplementation and Heart Failure: Effects on Fibrosis and Cardiac Remodeling》论文发表、《Exercise‐Induced Cardiac Lymphatic Remodeling Mitigates Inflammation in the Aging Heart》论文发表、《P1093Influence of glycogen content in mouse heart on post-MI fibrosis and cardiac remodeling》论文发表、《Cardiac Fibrosis: Key Role of Integrins in Cardiac Homeostasis and Remodeling》论文发表。
第455轮补录来源：肺老化与肺再生；新增 《Angiogenesis in Lung Regeneration and Aging》论文发表、《Lung Repair and Regeneration in ARDS》论文发表、《Comparative biology of tissue repair, regeneration and aging》论文发表、《Endothelial FoxM1 reactivates aging-impaired endothelial regeneration for vascular repair and resolution of inflammatory lung injury》论文发表、《Regeneration of the Aging Lung: A Mini-Review》论文发表。
第456轮补录来源：呼吸肌与通气能力；新增 《Respiratory muscle fatigue and ventilatory failure》论文发表、《Respiratory muscle weakness and normal ventilatory drive in dilative cardiomyopathy》论文发表、《Respiratory muscle strength and ventilatory failure in amyotrophic lateral sclerosis》论文发表、《Pulmonary rehabilitation in chronic respiratory insufficiency. 3. Ventilatory muscle training.》论文发表、《Respiratory muscle training improves aerobic capacity and respiratory muscle strength in youth wrestlers》论文发表。
第457轮补录来源：肾脏老化与肾单位韧性；新增 《Lineage-Tracing of p16INK4a-Positive Cells Reveals Nephron-by-Nephron Heterogeneity in Kidney Aging》论文发表、《Lineage-Tracing Experiments of Senescent Cell Marker p16INK4a-Positive Cells Show that Kidney Aging Proceeds on a Nephron-by-Nephron Basis》论文发表、《Nephron Protection in Diabetic Kidney Disease》论文发表、《Larger nephron size, low nephron number, and nephrosclerosis on biopsy as predictors of kidney function after donating a kidney》论文发表、《Low birth weight, nephron number, and kidney disease》论文发表。
第458轮补录来源：肝脏再生与代谢韧性；新增 《Metabolic Remodeling during Liver Regeneration》论文发表、《Metabolic inflexibility promotes mitochondrial health during liver regeneration》论文发表、《Effect of Hepatic Pathology on Liver Regeneration: The Main Metabolic Mechanisms Causing Impaired Hepatic Regeneration》论文发表、《Decoding the metabolic dialogue between hepatocytes and macrophages driving liver regeneration》论文发表、《Liver regeneration》论文发表。
第459轮补录来源：胰岛β细胞保存；新增 《251-LB: Tracking Beta-Cell Regeneration in Human Pancreatic Slices using Adenovirus Transduction》论文发表、《Beta cell regeneration meets autoimmunity: PAX4 variants in type 1 diabetes》论文发表、《Insights into beta cell regeneration for diabetes via integration of molecular landscapes in human insulinomas》论文发表、《2142-LB: GPR75 Signaling Mediates Beta-Cell Regeneration》论文发表、《Pancreatic alpha cell glucagon–liver FGF21 axis regulates beta cell regeneration in a mouse model of type 2 diabetes》论文发表。
第460轮补录来源：甲状腺与内分泌老化；新增 《Thyroid Function in Aging: A Discerning Approach》论文发表、《Thyroid autoimmunity, thyroid function, and endometriosis: reproductive immune-endocrine crosstalk and causal uncertainty》论文发表、《Thyroid Function and Morphology in Gaucher Disease: Exploring the Endocrine Implications》论文发表、《Thyroid Response to Peripheral Endocrine Factors: Neuropeptide Y Influences Thyroid Function in the Reptile Podarcis siculus》论文发表、《Circadian rhythm of the Leydig cells endocrine function is attenuated during aging》论文发表。
第461轮补录来源：肾上腺与应激激素韧性；新增 《Adrenal Aging and Its Implications on Stress Responsiveness in Humans》论文发表、《Aging induces region-specific dysregulation of hormone synthesis in the primate adrenal gland》论文发表、《Aging and the adrenal cortex》论文发表、《Aging and Adrenal Aldosterone Production》论文发表、《Harnessing the power of nutritional antioxidants against adrenal hormone imbalance-associated oxidative stress》论文发表。
第462轮补录来源：性激素下降与健康寿命；新增 《SEX DIFFERENCES IN AGING-RELATED DISEASE AND HEALTHSPAN》论文发表、《Abstract 10441: Sex-Specific Decline in Coronary Flow Reserve with Aging》论文发表、《Steroid hormone levels vary with sex, aging, lifestyle, and genetics》论文发表、《Reproductive aging is associated with a decline in per follicle antimullerian hormone》论文发表、《NUTRITIONAL INTERVENTIONS IN AGING: HEALTHSPAN AND DISEASE VULNERABILITY》论文发表。
第463轮补录来源：骨髓老化与造血维持；新增 《Bone Marrow Fat and Hematopoiesis》论文发表、《Inflamm-Aging of Hematopoiesis, Hematopoietic Stem Cells, and the Bone Marrow Microenvironment》论文发表、《Bone marrow hematopoiesis drives multiple sclerosis progression》论文发表、《Cell-Extrinsic Stressors from the Aging Bone Marrow (BM) Microenvironment Promote Dnmt3a-Mutant Clonal Hematopoiesis》论文发表、《Clonal hematopoiesis in the inherited bone marrow failure syndromes》论文发表。
第464轮补录来源：胸腺退化与T细胞生产；新增 《Human Thymic Involution and Aging in Humanized Mice》论文发表、《Ultrastructural study of thymic microenvironment involution in aging mice》论文发表、《Aging augments obesity-induced thymic involution and peripheral T cell exhaustion altering the “obesity paradox”》论文发表、《Altered aging-related thymic involution in T cell receptor transgenic, MHC-deficient, and CD4-deficient mice》论文发表、《IL-33 induces thymic involution-associated naive T cell aging and impairs host control of severe infection》论文发表。
第465轮补录来源：免疫组库多样性与老化；新增 《Diversity of the Immune Repertoire and Immunoregulation》论文发表、《Quantifiable blood TCR repertoire components associate with immune aging》论文发表、《Shattuck Lecture — Diversity of the Immune Repertoire and Immunoregulation》论文发表、《An Aging Clock Based on Immune Repertoire Features: <scp>COVID</scp> ‐19 Accelerates Aging》论文发表、《Immune remodeling: lessons from repertoire alterations during chronological aging and in immune-mediated disease》论文发表。
第466轮补录来源：NK细胞功能与免疫监视；新增 《Stress, NK Receptors, and Immune Surveillance》论文发表、《Evasion of NK cell immune surveillance via the vimentin-mediated cytoskeleton remodeling》论文发表、《RANKL Expressed by Acute Myeloid Leukemia Cells Impairs NK Cell-Mediated Immune Surveillance》论文发表、《NK Cell-Based Immune Checkpoint Inhibition》论文发表、《Natural Killer Cells in Myeloid Malignancies: Immune Surveillance, NK Cell Dysfunction, and Pharmacological Opportunities to Bolster the Endogenous NK Cells》论文发表。
第467轮补录来源：树突状细胞与抗原呈递；新增 《Hypoxia directly enhances dendritic cell antigen presentation》论文发表、《Myeloid apolipoprotein E controls dendritic cell antigen presentation and T cell activation》论文发表、《Involvement of LOX-1 in Dendritic Cell-Mediated Antigen Cross-Presentation》论文发表、《AML Bone Marrow Microenvironment Impairs Dendritic Cell Maturation and Antigen Presentation》论文发表、《Acquisition and presentation of follicular dendritic cell–bound antigen by lymph node–resident dendritic cells》论文发表。
第468轮补录来源：B细胞与抗体组库老化；新增 《Antibody Repertoire Revealed》论文发表、《Antibody Repertoire: Embracing Diversity》论文发表、《Aberrant B cell repertoire selection associated with HIV neutralizing antibody breadth》论文发表、《Profiling celiac disease antibody repertoire》论文发表、《A public anti-COVID antibody repertoire》论文发表。
第469轮补录来源：疫苗应答与免疫衰老；新增 《Immunosenescence, aging and successful aging》论文发表、《Immunosenescence: Role and measurement in influenza vaccine response among the elderly》论文发表、《Immune Senescence, Immunosenescence and Aging》论文发表、《Immunosenescence in Aging-Related Vascular Dysfunction》论文发表、《Analyzing Immune Responses to the Seasonal Influenza Vaccine to Understand Immunosenescence》论文发表。
第470轮补录来源：训练免疫与先天记忆；新增 《Innate immune memory, trained immunity and nomenclature clarification》论文发表、《Trained Immunity and Local Innate Immune Memory in the Lung》论文发表、《Resident memory macrophages and trained innate immunity at barrier tissues》论文发表、《Trained Innate Immunity Not Always Amicable》论文发表、《Trained immunity-inducing vaccines: Harnessing innate memory for vaccine design and delivery》论文发表。
第471轮补录来源：慢性炎症与炎性衰老；新增 《Inflammaging and Brain Aging》论文发表、《Chronic Inflammation and Aging in Rheumatic Diseases》论文发表、《Chronic inflammation and the hallmarks of aging》论文发表、《Chronic inflammation – inflammaging – in the ageing cochlea: A novel target for future presbycusis therapy》论文发表、《The Potential Roles of Probiotics, Resistant Starch, and Resistant Proteins in Ameliorating Inflammation during Aging (Inflammaging)》论文发表。
第472轮补录来源：纤维化消退与器官修复；新增 《RNF41 orchestrates macrophage-driven fibrosis resolution and hepatic regeneration》论文发表、《Comprehensive Review of the Vascular Niche in Regulating Organ Regeneration and Fibrosis》论文发表、《Vascular Endothelial Growth Factor Promotes Fibrosis Resolution and Repair in Mice》论文发表、《Liver fibrosis and repair: immune regulation of wound healing in a solid organ》论文发表、《Chaperone-mediated autophagy supports organ regeneration and fibroblast quiescence in mouse models of fibrosis》论文发表。
第473轮补录来源：脂肪组织老化与代谢健康；新增 《Adipose tissue browning and metabolic health》论文发表、《Aging epicardial adipose tissue: a metabolic-endocrine network driving vascular calcification》论文发表、《Intermuscular adipose tissue in healthy human aging—effects of exercise training and implications to metabolic health》论文发表、《Adipose tissue ageing: implications for metabolic health and lifespan》论文发表、《Thermogenic adipose tissue in energy regulation and metabolic health》论文发表。
第474轮补录来源：棕色脂肪与产热；新增 《SnapShot: Brown and Beige Adipose Thermogenesis》论文发表、《Brown adipose tissue thermogenesis in humans》论文发表、《Central Control of Brown Adipose Tissue Thermogenesis》论文发表、《Electrical Neurostimulation Promotes Brown Adipose Tissue Thermogenesis》论文发表、《Brown adipose tissue derived ANGPTL4 controls glucose and lipid metabolism and regulates thermogenesis》论文发表。
第475轮补录来源：糖代谢与胰岛素敏感性；新增 《Neuronal control of peripheral insulin sensitivity and glucose metabolism》论文发表、《Insulin Sensitivity, Glucose Metabolism, and Membrane Fluidity in Hypertensive Subjects》论文发表、《ATORVASTATIN WORSENS GLUCOSE METABOLISM AND INSULIN SENSITIVITY IN HYPERCHOLESTEROLEMIC PATIENTS》论文发表、《Liver-specific deletion of Ppp2cα enhances glucose metabolism and insulin sensitivity》论文发表、《Sex and Depot Differences in Adipocyte Insulin Sensitivity and Glucose Metabolism》论文发表。
第476轮补录来源：热量限制与寿命；新增 《Calorie restriction and longevity: fast and loose?》论文发表、《Calorie restriction, SIRT1 and metabolism: understanding longevity》论文发表、《Bile acids extend longevity beyond calorie restriction》论文发表、《Why calorie restriction would work for human longevity》论文发表、《How Can Dietary Calorie Restriction Lead to Longevity?》论文发表。
第477轮补录来源：间歇性禁食与代谢健康；新增 《Intermittent Fasting and Metabolic Health》论文发表、《Intermittent and periodic fasting, longevity and disease》论文发表、《Intermittent Fasting and Metabolic Health: From Religious Fast to Time‐Restricted Feeding》论文发表、《The cyclic metabolic switching theory of intermittent fasting》论文发表、《Intermittent fasting and longevity: From animal models to implication for humans》论文发表。
第478轮补录来源：植物性饮食与健康寿命；新增 《Diet-based strategies, informed by genetics, to improve healthspan》论文发表、《HEALTHSPAN MEASURES IN A WESTERN DIET CONDITIONED, IRRADIATED RODENT MODEL OF ACCELERATED AGING》论文发表、《Healthy Plant-Based Diet》论文发表、《Diet and Botanical Supplementation: Combination Therapy for Healthspan Improvement?》论文发表、《A Ketogenic Diet Extends Longevity and Healthspan in Adult Mice》论文发表。
第479轮补录来源：地中海饮食与认知老化；新增 《Perceived Control and Cognitive Aging: The Mediating Role of Mediterranean Diet Adherence》论文发表、《Mediterranean Diet and Cognitive Decline》论文发表、《Components of a Mediterranean diet and their impact on cognitive functions in aging》论文发表、《Mediterranean Diet and Cognitive Decline—Reply》论文发表、《Mediterranean Diet and Age-Related Cognitive Decline》论文发表。
第480轮补录来源：欧米伽3与炎症平衡；新增 《Depressive Symptoms, omega-6:omega-3 Fatty Acids, and Inflammation in Older Adults》论文发表、《Omega-3 Fatty Acids and Heart Health》论文发表、《Do Omega-3 Fatty Acids Benefit Health?》论文发表、《Omega-3 fatty acids and inflammation》论文发表、《Omega-3 polyunsaturated fatty acids and brain aging》论文发表。
第481轮补录来源：多酚与年龄相关疾病；新增 《Sirtuins in Aging and Age-Related Disease》论文发表、《Targeting Wnt signaling pathway by polyphenols: implication for aging and age-related diseases》论文发表、《Age-related neurodegenerative disease research needs aging models》论文发表、《Metabolic regulation of aging and age-related disease》论文发表、《Translational strategies in aging and age-related disease》论文发表。
第482轮补录来源：微量营养素与免疫韧性；新增 《IMMUNOGENOMIC RESPONSES TO VACCINATION IN AGING: INSIGHTS INTO IMMUNE RESILIENCE》论文发表、《IMMUNE AGING》论文发表、《Human immune aging》论文发表、《The 15‐Year Survival Advantage: Immune Resilience as a Salutogenic Force in Healthy Aging》论文发表、《Effective Immune Functions of Micronutrients against SARS-CoV-2》论文发表。
第483轮补录来源：蛋白质摄入与肌肉维持；新增 《Estimating protein intake in maintenance hemodialysis patients》论文发表、《Aging, exercise, and muscle protein metabolism》论文发表、《NAD+ deficit, protein acetylation and muscle aging》论文发表、《Maintenance of NAD+ Homeostasis in Skeletal Muscle during Aging and Exercise》论文发表、《Skeletal Muscle GLUT4 Protein Concentration and Aging in Humans》论文发表。
第484轮补录来源：水合作用与细胞稳态；新增 《Effect of cellular aging on memory T-cell homeostasis》论文发表、《Cellular and Mitochondrial Quality Control Mechanisms in Maintaining Homeostasis in Aging》论文发表、《Selective autophagy in the maintenance of cellular homeostasis in aging organisms》论文发表、《ATF6 safeguards organelle homeostasis and cellular aging in human mesenchymal stem cells》论文发表、《Mitochondria-lysosome contacts in aging: A mechanistic interface linking organelle homeostasis and cellular decline》论文发表。
第485轮补录来源：运动处方与健康寿命；新增 《Molecular Mechanisms of Exercise and Healthspan》论文发表、《Abstract 4141191: Early-life Exercise Extends Healthspan and Attenuates Cardiovascular Aging in Aged Mice》论文发表、《Exercise Prescription》论文发表、《AGING INTERVENTIONS GET HUMAN: CAN WE EXTEND HEALTHSPAN?》论文发表、《Exercise Prescription for Older Adults》论文发表。
第486轮补录来源：抗阻训练与骨肌维持；新增 《Optimizing Skeletal Muscle Anabolic Response to Resistance Training in Aging》论文发表、《Time-efficient, high-resistance inspiratory muscle strength training for cardiovascular aging》论文发表、《Influence of Exercise Training on Skeletal Muscle Insulin Resistance in Aging: Spotlight on Muscle Ceramides》论文发表、《Aging, obese-insulin resistance, and bone remodeling》论文发表、《Simulated resistance training during hindlimb unloading abolishes disuse bone loss and maintains muscle strength》论文发表。
第487轮补录来源：有氧适能与心血管韧性；新增 《Aging, cardiorespiratory fitness and sympathetic transduction》论文发表、《Cardiorespiratory Fitness and Attentional Control in the Aging Brain》论文发表、《Does clinical rehabilitation impose sufficient cardiorespiratory strain to improve aerobic fitness?》论文发表、《Accelerated Decline of Aerobic Fitness With Healthy Aging》论文发表、《The Association of Aging and Aerobic Fitness With Memory》论文发表。
第488轮补录来源：睡眠卫生与昼夜对齐；新增 《0196 Retinal responsivity is associated with circadian phase and circadian alignment but not sleep timing》论文发表、《0655 Circadian Sleep Preferences, Sleep Quality, Daytime Sleepiness and Sleep Hygiene amongst Undergraduate students of a Nigerian University》论文发表、《0302 Household Chaos in Diverse Families: Does It Influence Family Sleep or Circadian Alignment?》论文发表、《Circadian Rhythm Sleep Disorders》论文发表、《Sleep and circadian rhythms》论文发表。
第489轮补录来源：压力缓解与长寿心理；新增 《Strain, stress, neurodegeneration and longevity》论文发表、《THE ROLE OF EDUCATION AND RESILIENCE IN MENTAL HEALTH TRAJECTORIES OF AGING VETERANS》论文发表、《Psychological and biological resilience modulates the effects of stress on epigenetic aging》论文发表、《Psychological stress and aging: role of glucocorticoids (GCs)》论文发表、《Molecular consequences of psychological stress in human aging》论文发表。
第490轮补录来源：社会连接与健康老化；新增 《Yeast longevity and aging—the mitochondrial connection》论文发表、《Lipidomics in longevity and healthy aging》论文发表、《Integrative Multi-Omic Signatures of Longevity and Healthy Aging》论文发表、《Ergothioneine promotes longevity and healthy aging in male mice》论文发表、《Complementary and Integrated Studies of Longevity and Healthy Aging》论文发表。
第491轮补录来源：生活目标感与长寿；新增 《Early Life Interventions: Impact on Aging and Longevity》论文发表、《Longevity Assurance Genes: How Do They Influence Aging and Life Span?》论文发表、《PURPOSE IN LIFE, STRESS REACTIVITY, AND COGNITIVE AGING: A LONGITUDINAL INVESTIGATION》论文发表、《Cardiovascular Aging and Longevity》论文发表、《Longevity, Genes, and Aging》论文发表。
第492轮补录来源：财务健康与寿命公平；新增 《Can financial incentives improve health equity?》论文发表、《Acarbose improves health and lifespan in aging HET3 mice》论文发表、《Reframing Aging and Diabetes: Centering Transgender Health Equity》论文发表、《Physiological Dysregulation and Aging: Implications for Health Equity》论文发表、《Measuring Structural Racism to Advance Health Equity in Aging》论文发表。
第493轮补录来源：健康素养与自我管理；新增 《Health Literacy Influences Self-Management Behavior in Asthma》论文发表、《Health Literacy Influences Self-Management Behavior in Asthma: Response》论文发表、《Tailored Education May Reduce Health Literacy Disparities in Asthma Self-Management》论文发表、《EXPLORING DIGITAL LITERACY, HEALTH LITERACY, AND SELF-MANAGEMENT IN YOUNGER AND OLDER LIVER TRANSPLANT RECIPIENTS》论文发表、《Aging immigrant family caregivers health, social engagement, and health literacy》论文发表。
第494轮补录来源：数字生物标志物与连续感知；新增 《Digital biomarkers: Convergence of digital health technologies and biomarkers》论文发表、《Digital biomarkers for brain health: passive and continuous assessment from wearable sensors》论文发表、《Direct digital sensing of protein biomarkers in solution》论文发表、《Continuous sleep depth index annotation with deep learning yields novel digital biomarkers for sleep health》论文发表、《Advancing digital sensing in mental health research》论文发表。
第495轮补录来源：纵向队列与老化研究；新增 《Cohort Profile: The Longitudinal Aging Study Amsterdam》论文发表、《Cohort Profile: The Canadian Longitudinal Study on Aging (CLSA)》论文发表、《AI AND AGING: IDENTIFYING IMPORTANT LIVING ACTIVITIES FOR HEALTHY AGING IN SINGAPORE LONGITUDINAL AGING COHORT》论文发表、《Cohort Profile: The Healthy Aging Longitudinal Study in Taiwan (HALST)》论文发表、《Blood-Based Biomarkers of Aging and Neurodegeneration in Longitudinal Cohort Studies of Brain Aging》论文发表。
第496轮补录来源：因果推断与长寿干预；新增 《Causal Inference is Necessary but Insufficient for Causal Inference.》论文发表、《Assimilative causal inference》论文发表、《Improving causal inference》论文发表、《Concepts of Causal Inference.》论文发表、《Causal Inference in Public Health》论文发表。
第497轮补录来源：老龄化临床试验设计；新增 《Epigenetic aging biomarkers in dietary geroscience: feasibility, participant perceptions, and trial design considerations》论文发表、《GEROSCIENCE-DRIVEN THERAPIES TO TARGET HEALTHSPAN WITH AGING: CLINICAL IMPLICATIONS》论文发表、《CLINICAL TRIALS IN GEROSCIENCE》论文发表、《Bringing Geroscience to the Bedside: Leveraging Biomarkers of Aging in Clinical Research》论文发表、《BARRIERS TO GEROSCIENCE IN CLINICAL COMMUNITY》论文发表。
第498轮补录来源：老年保护药物监管科学；新增 《Potential dietary geroprotectors and their impact on key mechanisms of aging》论文发表、《Crowdsourced Drug Discovery Approach Identifies BET Inhibitors As Novel Geroprotectors Promoting Healthy Aging》论文发表、《Advancing Regulatory Science》论文发表、《Regulatory issues in aging pharmacology》论文发表、《Regulatory Science in Neonates》论文发表。
第499轮补录来源：健康寿命经济学与价值评估；新增 《Energetic interventions for healthspan and resiliency with aging》论文发表、《Biomarker Insights Into Brain Health, Aging, and Healthspan》论文发表、《ECONOMICS OF AGING》论文发表、《DELETION OF THROMBOSPONDIN-1 PRESERVES HEMATOPOIETIC STEM CELL HEALTHSPAN DURING AGING》论文发表、《The circadian clock gene period extends healthspan in aging Drosophila melanogaster》论文发表。
第500轮补录来源：未来人类基础设施与有效永生；新增 《Inducible immortality in hTERT‐human mesenchymal stem cells》论文发表、《Aging, longevity, and immortality in vitro》论文发表、《The Future of Human Longevity》论文发表、《Nuclear autophagy promotes longevity and germline immortality》论文发表、《The Future of Human Longevity: A Demographer's Perspective》论文发表。
                    <i>In Vivo</i>
                    Therapeutic Gene Editing》论文发表。

## 下一轮补录队列

- 产业资金网络四阶段：Retro 临床推进、NewLimit IND、BioAge DME 试验、
  长寿公开市场与基金回报数据、Altos Labs 科研成果。
- PROSPR 资助后续：7 个团队里程碑、健康寿命终点与监管接受度、
  Cambrian TORnado 临床数据、Linnaeus LNS8801 转化和 Retro RTR242 独立试验注册。
- 脑机接口后续：Synchron COMMAND 阳性结果与长期随访、Neuralink GB-PRIME/UAE-PRIME/VOICE、
  Synchron Apple HID 协议与 CONVOY/INTENT、FDA 完整 IDE 与器械批准、
  Synchron FOCUS-CAN、关键试验与商业化启动、BCI 居家使用、言语解码、神经权利治理、
  Synchron 长期随访、UNESCO 神经技术伦理和更多州/联合国神经权利立法。
- AI 自动化科学后续：AI co-scientist 临床转化、自主实验室扩展、材料数据库治理、
  药物发现可复现性、AI 假设生成与科研诚信边界、TeLLAgent 类代理框架独立评测、
  自驱动实验室跨实验室泛化和代理式 AI 临床研发案例。
- 理论谱系：Peto's paradox、生物年龄指标跨人群校准、GrimAge/PhenoAge 临床验证、
  衰老测量标准与监管接受度；已有共识与跨组织图谱，继续补跨人群复现、
  FDA/EMA 监管讨论和长寿干预终点设计。
- 数字与认知路径：Nectome/脑保存、神经形态硬件、数字孪生、griefbots、
  BCI 伦理与身份、类器官智能伦理。
- 认知增强后续：BCI 持续同意机制、神经技术伦理指南执行、
  植入设备数据治理、经颅电刺激随机试验复现和可训练注意力跨人群证据。
- 神经形态与活性算力后续：Loihi/Hala Point 后续系统与能效数据、
  FinalSpark/Cortical Labs 湿件平台标准化、合成生物智能伦理、
  活性算力的可扩展性与治理边界。
- 暂停与重建：玻璃化冷冻、器官灌注、BrainEx 后续研究、生物打印、最小充分身体、
  异种移植临床监管节点、全眼移植长期随访、人遗体多器官异种移植后续、
  儿科常温机器灌注、低温/常温灌注全国队列、器官再调节伦理和猪源器官基因编辑监管、
  AI 冷冻保护剂设计、器官体积复温、全卵巢保存和封闭玻璃化系统。
- 老年权利治理后续：IGWG 第二、三届会议、公约草案框架、区域实施战略审查、
  年龄友好城市与社区国家行动、长期照护融资、失能压缩测量和健康寿命指标标准化。
- BCI 监管后续：Paradromics 可行性研究随访、CorTec 器械临床路径、
  Neuralink Blindsight 与 VOICE 临床节点、Synchron 关键试验登记和神经权利治理。
- 生物年龄指标后续：跨队列复现、临床终点对齐、监管接受度、
  不同组学时钟比较和个体不确定性传播。
- AI 药物发现后续：Rentosertib III 期独立数据、AI 候选药获批边界、
  临床失败教训、管线统计口径标准化和监管框架。
- 低温保存与生物打印后续：公升级器官灌注复温、卵巢/子宫保存临床转化、
  生物墨水血管化、移植结局和伦理治理。
- 历史与文献：古代铭文档案、死海古卷、道教外丹文本、数字永生叙事文本。
- 思想与治理：长寿逃逸速度谱系、有效永生飞轮、AI 安全与长寿技术治理、
  健康老龄化政策。
- 人工器官与生命维持后续：INTERMACS/STS 后续年度报告、VAD 患者选择与撤除伦理、
  器官分配公平、长期随访治理和医疗不公；MOMENTUM 3 五年结果、
  LVAD 撤除与临终伦理、患者决策辅助和支付可及性。
- 健康老龄化治理后续：各国十年执行报告、长期照护融资、年龄友好城市、
  老年权利公约、失能压缩测量和健康寿命指标标准化。
- 长寿医学监管后续：老年医学试验终点验证、胜率统计监管接受度、
  干细胞抗衰随机试验独立复核、长寿药物临床信号和欧盟/全球研究资助协调。
- 再生医学转化后续：hESC/iPSC 临床监管、细胞与基因疗法长期随访、CAR-T 可及性、
  iPS 细胞库与免疫匹配、组织工程与器官重建、干细胞产业证据治理。

## 当前原料

- 详细年表底稿：`docs/source-notes/2026-08-06-human-immortality-research-major-events-timeline.md`
- 公共正文：`docs/publications/history-of-immortality.md`
- 数据来源获取计划：`DATA_SOURCES.md`

## 最小落地顺序

1. 完成本地来源语境复核，重点纠偏 SRC-028、SRC-038 两处疑似错配。
2. 对 16 个已匹配 PeriodO 的时期做 fresh review，并继续映射 5 个 `pending` 时期。
3. 对每个事件完成本地复核，再进入 fresh review。
4. 对第二轮补录的 30 条事件继续做来源语境复核，再进入 fresh review。
5. 稳定结论回写公共永生史。

## 门禁

- 本地门禁：`make history-timeline-gate`
- 机器契约：`governance/control-plane/history-timeline-contract.v1.yaml`
- CI 门禁：`.github/workflows/check.yml`

## 技术决策

- 技术栈调研与最终推荐：`TOOLS.md`
- 架构决策：`governance/decisions/adr/ADR-0001-历史年表采用可复核数据管线与成熟发布工具组合.md`
