# 真实应用与文献索引

本页把 Human Infra 从概念拉回真实世界：哪些已经存在的项目、制度、研究计划和论文，实际上都在处理“人类运行基础设施”的一部分。

它不是推荐清单，也不是证据等级结论。它的用途是建立一条可追溯的资料主干，帮助后续把宣传叙事、README、美化材料和子域文档都接回真实来源。

## 收录标准

- 优先收录官方项目页、政府/机构资料、论文原文、PubMed、ClinicalTrials.gov 或出版社页面。
- 每个条目必须说明它映射到 Human Infra 的哪一层。
- 高风险健康、神经、生命延续内容必须保留边界：不是医疗建议，不是人体实验指南，不是技术可行性背书。
- 商业个人实验可以作为现象和应用案例收录，但不能当作临床证据。

## 应用地图

| 线路 | 真实应用 | 它提示了什么 | Human Infra 映射 | 首批来源 |
| --- | --- | --- | --- | --- |
| 自我量化与长寿实践 | Bryan Johnson / Blueprint | 个体可以尝试把睡眠、饮食、运动、补剂、检测和生活流程组织成一套可观测运行系统 | 个体级运行系统、反馈闭环、长寿证据边界 | [Blueprint Protocol](https://protocol.bryanjohnson.com/) |
| 可穿戴健康监测 | Apple Heart Study | 消费级传感器可以进入大规模健康筛查和反馈链路，但需要临床验证和风险沟通 | 传感器、反馈、医学边界、数字健康 | [NEJM Apple Heart Study](https://www.nejm.org/doi/full/10.1056/NEJMoa1901183), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31722151/), [Stanford Medicine](https://med.stanford.edu/news/all-news/2019/11/through-apple-heart-study--stanford-medicine-researchers-show-we.html) |
| 职业健康与组织设计 | NIOSH Total Worker Health | 工作不是背景变量，而是影响健康、安全和福祉的系统条件 | 组织基础设施、恢复、风险控制、反压榨边界 | [NIOSH TWH Program](https://www.cdc.gov/niosh/twh/programs/index.html), [TWH overview](https://www.cdc.gov/niosh/twh/index.html) |
| 老年整合照护 | WHO ICOPE | 健康老龄化可以围绕内在能力、功能能力和个性化照护路径组织 | 健康寿命、照护路径、主体能力维护 | [WHO ICOPE handbook](https://www.who.int/publications/i/item/9789240103726), [WHO ICOPE training](https://www.decadeofhealthyageing.org/find-knowledge/support/training-programmes/who-integrated-care-for-older-people-%28icope%29-training-programme-field-testing-version) |
| 极端环境人因 | NASA Human Research Program | 太空飞行把人类健康、表现、风险、训练、任务和环境约束压缩到一个高风险系统里 | 人因工程、生命支持、任务表现、极端环境恢复 | [NASA HRP](https://www.nasa.gov/hrp/), [NASA Human Health and Performance](https://www.nasa.gov/hhp/), [NASA spaceflight risks](https://www.nasa.gov/humans-in-space/hhc-spaceflight-risks/) |
| 军队人类表现优化 | U.S. Army H2F / Total Force Fitness | 高压组织已经把体能、睡眠、营养、心理和恢复合并成战备基础设施 | 高压任务执行、恢复、训练系统、组织支持 | [Army H2F](https://h2f.army.mil/), [Army H2F overview](https://www.goarmy.com/explore-the-army/holistic-health-fitness), [Total Force Fitness review](https://pmc.ncbi.nlm.nih.gov/articles/PMC10666955/) |
| 神经科技基础设施 | NIH BRAIN Initiative / DARPA NESD / Neuralink PRIME | 神经接口、脑功能理解和临床设备试验正在形成高风险神经基础设施 | 记忆编辑、去具身中枢、主体权利、安全审计 | [NIH BRAIN Initiative](https://braininitiative.nih.gov/), [DARPA NESD](https://www.darpa.mil/research/programs/neural-engineering-system-design), [Neuralink PRIME on ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06429735), [FDA IDE overview](https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/investigational-device-exemption-ide) |
| 系统安全与人机组织 | NASA Human Systems Integration / Leveson STAMP | 人的限制、训练、维护、组织决策和安全控制必须在系统设计中前置 | Human SRE、事故预防、任务系统、安全边界 | [NASA HSI lessons](https://www.nasa.gov/humans-in-space/commercial-space/leo-economy/nasa-shares-lessons-human-systems-integration/), [Engineering a Safer World](https://direct.mit.edu/books/oa-monograph/2908/Engineering-a-Safer-WorldSystems-Thinking-Applied) |

## 文献主干

| 主题 | 文献或资料 | 为什么重要 | 应放入的后续子域 |
| --- | --- | --- | --- |
| 衰老机制 | Lopez-Otin 等，The Hallmarks of Aging | 提供长寿证据和干预讨论的机制框架，但不能直接等同于人体疗效 | `domains/longevity-evidence/` |
| 慢性压力与负荷 | McEwen / Stellar 的 allostatic load 线路 | 把压力、恢复和长期疾病风险放进同一套生理成本模型 | `docs/explanations/` 与组织使用边界 |
| 自我追踪文化 | Gary Wolf / Quantified Self | 解释从个人记录、传感器、指标到生活系统的历史线路 | README 叙事与应用案例 |
| 工作与福祉 | NIOSH Total Worker Health 文献与工具 | 把“工作设计”作为健康基础设施，而不是只要求个人自律 | 组织应用与安全边界 |
| 健康老龄化 | WHO ICOPE | 把老年照护从疾病中心转向能力维护和路径设计 | Longevity Evidence 与应用案例 |
| 数字健康验证 | Apple Heart Study | 展示可穿戴传感器进入健康系统时需要大规模验证、确认和边界沟通 | 数据脚本、证据政策、数字健康案例 |
| 极端环境人因 | NASA HRP / HSI | 把人的生理、认知、环境和任务风险当作工程约束 | 去具身中枢、未来等待、任务执行模型 |
| 神经科技治理 | NIH BRAIN、DARPA NESD、ClinicalTrials.gov 神经接口试验 | 提供记忆编辑、神经接口和主体权利讨论的真实研究背景 | `domains/memory-editing/` 与 `domains/disembodied-cns/` |
| 系统安全 | Nancy Leveson, Engineering a Safer World | 把事故理解为控制、组织和系统约束问题，而不只是个体失误 | Human SRE、审查清单、安全边界 |

## 如何用于 README 和宣传

宣传时可以强表达：

```text
Human Infra 不是凭空发明的新词。
Bryan Johnson、NIOSH Total Worker Health、WHO ICOPE、NASA HRP、Apple Heart Study、军队 H2F、NIH BRAIN 和系统安全工程，其实都在研究同一个更大的对象：
支撑人类长期运行、判断、创造、恢复和延续的基础设施。
```

但仓库文档必须弱结论：

- Bryan Johnson / Blueprint 是自我量化和个人运行系统案例，不是临床证据标准。
- Apple Heart Study 是数字健康验证案例，不表示所有可穿戴功能都可用于诊断。
- BRAIN、NESD、Neuralink PRIME 是神经科技研究和试验背景，不表示记忆编辑或去具身中枢已经可执行。
- NASA、军队和职业健康案例能说明 Human Infra 的工程价值，但不能直接迁移到普通生活场景而不考虑伦理和权力关系。

## 下一批资料队列

- 睡眠、运动、营养和心理健康的公共卫生指南。
- 长寿干预数据库、NIA Interventions Testing Program、Geroscience 文献。
- 人机协作、认知负荷、注意力恢复和知识工作研究。
- 神经伦理、BCI 临床安全、记忆干预伦理文献。
- 组织疲劳管理、事故复盘、医疗安全和高可靠组织资料。

## 来源清单

- Bryan Johnson Blueprint Protocol: https://protocol.bryanjohnson.com/
- Apple Heart Study, NEJM: https://www.nejm.org/doi/full/10.1056/NEJMoa1901183
- Apple Heart Study, PubMed: https://pubmed.ncbi.nlm.nih.gov/31722151/
- Stanford Medicine Apple Heart Study release: https://med.stanford.edu/news/all-news/2019/11/through-apple-heart-study--stanford-medicine-researchers-show-we.html
- NIOSH Total Worker Health Program: https://www.cdc.gov/niosh/twh/programs/index.html
- NIOSH Total Worker Health overview: https://www.cdc.gov/niosh/twh/index.html
- WHO ICOPE handbook: https://www.who.int/publications/i/item/9789240103726
- WHO ICOPE training programme: https://www.decadeofhealthyageing.org/find-knowledge/support/training-programmes/who-integrated-care-for-older-people-%28icope%29-training-programme-field-testing-version
- NASA Human Research Program: https://www.nasa.gov/hrp/
- NASA Human Health and Performance: https://www.nasa.gov/hhp/
- NASA Human Health Countermeasures risks: https://www.nasa.gov/humans-in-space/hhc-spaceflight-risks/
- U.S. Army H2F: https://h2f.army.mil/
- U.S. Army H2F overview: https://www.goarmy.com/explore-the-army/holistic-health-fitness
- Total Force Fitness review: https://pmc.ncbi.nlm.nih.gov/articles/PMC10666955/
- NIH BRAIN Initiative: https://braininitiative.nih.gov/
- DARPA NESD: https://www.darpa.mil/research/programs/neural-engineering-system-design
- Neuralink PRIME Study, ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT06429735
- FDA Investigational Device Exemption overview: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/investigational-device-exemption-ide
- NASA Human Systems Integration lessons: https://www.nasa.gov/humans-in-space/commercial-space/leo-economy/nasa-shares-lessons-human-systems-integration/
- Nancy Leveson, Engineering a Safer World: https://direct.mit.edu/books/oa-monograph/2908/Engineering-a-Safer-WorldSystems-Thinking-Applied
- Lopez-Otin et al., The Hallmarks of Aging: https://pmc.ncbi.nlm.nih.gov/articles/PMC3836174/
- Hallmarks of Aging, PubMed: https://pubmed.ncbi.nlm.nih.gov/23746838/
- McEwen and Stellar, allostatic load: https://pubmed.ncbi.nlm.nih.gov/8379800/
- McEwen, stress and allostatic load review: https://pubmed.ncbi.nlm.nih.gov/9629234/
- Gary Wolf / Quantified Self background: https://quantifiedself.com/gary-wolf-bio/
