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
| 长寿证据基础设施 | NIA Interventions Testing Program / Geroscience / HAGR | 长寿不只是个人实验，也需要候选干预筛选、模型验证、机制框架、数据库归档和临床试验登记 | 长寿证据账本、干预分层、证据等级、转化边界 | [NIA ITP](https://www.nia.nih.gov/research/dab/interventions-testing-program-itp), [JAX ITP](https://www.jax.org/research-and-faculty/research-centers/aging-center/research/itp), [NIH GSIG](https://oir.nih.gov/sigs/geroscience-interest-group-gsig), [DrugAge](https://genomics.senescence.info/drugs/) |
| 人口级健康数据基础设施 | All of Us / UK Biobank / NHANES / Framingham / GTEx | 长期健康、基因、表型、环境和生活方式数据正在成为理解人类运行状态的基础设施 | 数据治理、长期随访、多模态表型、代表性、隐私和再识别风险 | [All of Us](https://allofus.nih.gov/), [UK Biobank](https://www.ukbiobank.ac.uk/), [NHANES](https://www.cdc.gov/nchs/nhanes/index.html), [Framingham Heart Study](https://www.nhlbi.nih.gov/science/framingham-heart-study-fhs), [GTEx Portal](https://gtexportal.org/home/) |
| 学习型健康系统与真实世界证据 | ClinicalTrials.gov / FDA RWE / PCORnet / OHDSI OMOP / HL7 FHIR / NICE ESF | 健康数据只有进入登记、互操作、研究网络、证据标准和监管路径，才可能成为可审查的产品和制度 | 证据生成、互操作、监管边界、数字健康评估、真实世界数据治理 | [ClinicalTrials.gov](https://clinicaltrials.gov/), [FDA RWE](https://www.fda.gov/science-research/science-and-research-special-topics/real-world-evidence), [PCORnet](https://pcornet.org/), [OMOP CDM](https://ohdsi.github.io/CommonDataModel/), [HL7 FHIR](https://hl7.org/fhir/), [NICE ESF](https://www.nice.org.uk/what-nice-does/digital-health/evidence-standards-framework-esf-for-digital-health-technologies) |
| 患者健康记录访问、互操作与数据可携带 | ONC Get It, Check It, Use It / USCDI / TEFCA / CMS Patient Access / CMS Blue Button / HL7 FHIR / SMART App Launch | 医疗、照护、保险和研究能否连续，取决于患者和授权照护者能否获取、核对、携带和授权使用健康记录、理赔数据、药物清单和转诊资料 | 患者访问、健康记录、互操作、数据可携带、授权应用、保险数据 API、反数据锁定边界 | [ONC health records](https://www.healthit.gov/how-to-get-your-health-record/), [USCDI](https://www.healthit.gov/isp/united-states-core-data-interoperability-uscdi), [TEFCA](https://www.healthit.gov/topic/interoperability/policy/trusted-exchange-framework-and-common-agreement-tefca), [CMS Patient Access](https://www.cms.gov/priorities/key-initiatives/burden-reduction/interoperability/policies-and-regulations/cms-interoperability-and-patient-access-final-rule-cms-9115-f), [CMS Blue Button](https://bluebutton.cms.gov/), [SMART App Launch](https://hl7.org/fhir/smart-app-launch/) |
| 信任、隐私与数据治理 | HHS HIPAA / Common Rule / NIST Privacy / NIST CSF / NIH GDS / GA4GH / ONC Information Blocking | 人类基础设施收集的是高敏感健康、基因、行为和神经相关数据，必须先有权利、同意、访问控制、安全和用途边界 | 隐私风险管理、受试者保护、网络安全、基因数据治理、健康数据共享边界 | [HHS HIPAA Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/privacy/index.html), [Common Rule](https://www.hhs.gov/ohrp/regulations-and-policy/regulations/common-rule/index.html), [NIST Privacy Framework](https://www.nist.gov/privacy-framework), [NIST CSF](https://www.nist.gov/cyberframework), [GA4GH Framework](https://www.ga4gh.org/product/framework-for-responsible-sharing-of-genomic-and-health-related-data/), [ONC Information Blocking](https://healthit.gov/information-blocking/) |
| 功能、生活质量与患者报告结局 | PROMIS / WHO ICF / EQ-5D / ICHOM / PRO-CTCAE / WHOQOL | Human Infra 的最终问题不是指标更多，而是人是否功能更好、负担更低、生活质量更高、伤害更少 | 功能状态、生活质量、症状负担、患者中心结局、价值导向评估 | [PROMIS](https://www.healthmeasures.net/explore-measurement-systems/promis), [WHO ICF](https://www.who.int/standards/classifications/international-classification-of-functioning-disability-and-health), [EQ-5D](https://euroqol.org/information-and-support/euroqol-instruments/), [ICHOM](https://www.ichom.org/patient-centered-outcome-measures/), [PRO-CTCAE](https://healthcaredelivery.cancer.gov/pro-ctcae/), [WHOQOL](https://www.who.int/tools/whoqol) |
| 康复、辅助技术与可访问性 | WHO Rehabilitation / Rehabilitation 2030 / WHO-UNICEF assistive technology / WHO priority assistive products / WCAG / Section 508 / ADA effective communication | 人类基础设施不能只追求更强的人，也要让受伤、残障、慢病和老化状态下的人继续行动、沟通、学习和工作 | 康复服务、辅助产品、数字无障碍、合理便利、沟通权利、功能连续性 | [WHO rehabilitation](https://www.who.int/news-room/fact-sheets/detail/rehabilitation), [Rehabilitation 2030](https://www.who.int/initiatives/rehabilitation-2030), [Global report on assistive technology](https://www.who.int/publications/i/item/9789240049451), [WHO priority assistive products list](https://www.who.int/publications/i/item/priority-assistive-products-list), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Section 508](https://www.access-board.gov/ict/), [ADA effective communication](https://www.ada.gov/resources/effective-communication/) |
| 价值、成本与疾病负担 | IHME GBD / WHO Global Health Estimates / WHO-CHOICE / NICE HTA / ICER / CMS value-based programs / AHRQ MEPS | Human Infra 必须能说明健康损失、功能损失、成本、资源分配和价值评估，而不是只展示技术指标 | 疾病负担、成本效果、HTA、QALY/DALY 边界、支付与资源配置 | [IHME GBD](https://www.healthdata.org/research-analysis/gbd), [WHO Global Health Estimates](https://www.who.int/data/global-health-estimates), [WHO cost-effectiveness portal](https://www.who.int/universal-health-coverage/compendium/cost-effectiveness-portal), [NICE technology appraisal](https://www.nice.org.uk/what-nice-does/our-guidance/about-technology-appraisal-guidance), [ICER value framework](https://icer.org/assessment/value-assessment-framework-2020/), [AHRQ MEPS](https://meps.ahrq.gov/mepsweb/) |
| 压力、负荷与恢复 | McEwen allostatic load / Perceived Stress Scale / WHO mental health at work / Surgeon General workplace well-being / NIOSH WellBQ | 人类运行失败常常不是单点意志问题，而是长期压力、恢复不足、组织条件和生理负荷共同累积 | 慢性压力、恢复、工作心理健康、福祉测量、疲劳和组织责任边界 | [McEwen allostatic load](https://pubmed.ncbi.nlm.nih.gov/8379800/), [Perceived Stress Scale](https://pubmed.ncbi.nlm.nih.gov/6668417/), [WHO mental health at work](https://www.who.int/publications/i/item/9789240053052), [Surgeon General workplace well-being](https://www.hhs.gov/surgeongeneral/priorities/workplace-well-being/index.html), [NIOSH WellBQ](https://www.cdc.gov/niosh/twh/worker-well-being/wellbq.html) |
| 社会决定因素与生活环境 | WHO SDOH / Healthy People 2030 SDOH / CDC SVI / CDC EJI / CDC PLACES / USDA Food Access / CMS AHC | 个体运行能力受住房、食物、环境、交通、教育、收入、社区和医疗可及性约束，不能只归因于自律或工具 | 社会决定因素、社区脆弱性、环境负担、食物可及性、健康相关社会需求 | [WHO SDOH](https://www.who.int/news-room/fact-sheets/detail/social-determinants-of-health), [Healthy People 2030 SDOH](https://odphp.health.gov/healthypeople/priority-areas/social-determinants-health), [CDC/ATSDR SVI](https://www.atsdr.cdc.gov/place-health/php/svi/index.html), [CDC/ATSDR EJI](https://www.atsdr.cdc.gov/place-health/php/eji/index.html), [CDC PLACES](https://www.cdc.gov/places/index.html), [USDA Food Access Research Atlas](https://www.ers.usda.gov/data-products/food-access-research-atlas), [CMS AHC](https://www.cms.gov/priorities/innovation/innovation-models/ahcm) |
| 住房稳定、无家可归与驱逐风险 | UN-Habitat Housing / HUD AHAR / Census American Housing Survey / Household Pulse Survey / Eviction Lab | 人能否睡眠、学习、就医、照护、工作和保有身份文件，取决于是否有稳定、可负担、安全且不会随时失去的住所 | 住房稳定、住房负担、无家可归、临时居住、驱逐风险、家庭不稳定、反住房污名边界 | [UN-Habitat Housing](https://unhabitat.org/topic/housing), [HUD AHAR](https://www.huduser.gov/portal/datasets/ahar.html), [Census AHS](https://www.census.gov/programs-surveys/ahs.html), [Household Pulse Survey](https://www.census.gov/programs-surveys/household-pulse-survey.html), [Eviction Lab](https://evictionlab.org/), [Eviction Tracking System](https://evictionlab.org/eviction-tracking/) |
| 社会连接、孤独风险与社区归属 | WHO social connection report / WHO social isolation and loneliness / CDC social connectedness / Healthy People Social and Community Context / NASEM social isolation / NHS social prescribing | 人能否长期运行，取决于是否有稳定关系、归属、互助、服务入口和社区支持，而不是只靠个人韧性 | 社会连接、孤独风险、社区归属、社会处方、老年支持、反污名和反监控边界 | [WHO social connection report](https://www.who.int/publications/i/item/978240112360), [WHO social isolation and loneliness](https://www.who.int/teams/social-determinants-of-health/demographic-change-and-healthy-ageing/social-isolation-and-loneliness), [CDC social connectedness](https://www.cdc.gov/social-connectedness/about/index.html), [CDC risk factors](https://www.cdc.gov/social-connectedness/risk-factors/index.html), [Healthy People social context](https://odphp.health.gov/healthypeople/objectives-and-data/browse-objectives/social-and-community-context), [NASEM social isolation](https://www.nationalacademies.org/projects/HMD-HSP-17-25/publication/25663), [NHS social prescribing](https://www.england.nhs.uk/personalisedcare/social-prescribing/) |
| 经济安全、社会保护与时间结构 | ILO Social Protection / ILO Social Protection Floors / World Bank Universal Social Protection / ASPIRE / DOL paid leave / FMLA / UN time use / ILO working time / Fed SHED / CFPB financial well-being / EITC | 人的长期运行受收入稳定、社会保护、带薪休假、工作时间、家庭时间、现金缓冲和金融压力约束 | 社会保护、经济韧性、时间贫困、带薪照护、工作时间、金融福祉、反贫困边界 | [ILO social protection](https://www.ilo.org/topics/social-protection), [ILO social protection floors](https://www.ilo.org/resource/news/ilo-social-protection-floors-recommendation-2012-no-202), [World Bank Universal Social Protection](https://www.worldbank.org/en/topic/socialprotection/brief/universal-social-protection), [World Bank ASPIRE](https://www.worldbank.org/en/data/datatopics/aspire), [DOL paid leave](https://www.dol.gov/agencies/wb/featured-paid-leave), [FMLA](https://www.dol.gov/agencies/whd/fmla), [UN time use](https://unstats.un.org/unsd/gender/timeuse/), [Fed SHED](https://www.federalreserve.gov/consumerscommunities/shed.htm), [CFPB financial well-being](https://www.consumerfinance.gov/consumer-tools/financial-well-being/), [EITC](https://www.irs.gov/credits-deductions/individuals/earned-income-tax-credit-eitc) |
| 公共福利、行政负担与服务导航 | USA.gov Benefit Finder / Performance.gov CX / SNAP / Medicaid.gov / HealthCare.gov Medicaid & CHIP / SSA SSI / LIHEAP / Administrative Burden | 制度存在不等于人能获得支持；资格理解、申请、证明材料、续期、等待、申诉、人工帮助和跨机构体验会决定福利能否转成真实运行能力 | 福利导航、服务递送、行政负担、申请成本、续期流失、公共服务体验、反程序性排除边界 | [USA.gov Benefit Finder](https://www.usa.gov/benefit-finder), [Performance.gov CX](https://www.performance.gov/cx/), [USAGov food assistance](https://www.usa.gov/food-help), [Medicaid eligibility](https://www.medicaid.gov/eligibility), [HealthCare.gov Medicaid & CHIP](https://www.healthcare.gov/medicaid-chip/), [SSA SSI](https://www.ssa.gov/ssi), [ACF LIHEAP](https://www.acf.hhs.gov/ocs/low-income-home-energy-assistance-program-liheap), [Administrative Burden article](https://doi.org/10.1093/jopart/muu009), [Administrative Burden book](https://www.russellsage.org/publications/administrative-burden) |
| 社区资源导航、社会服务转介与资源目录 | 211 / Open Referral HSDS / Gravity Project / CMS Accountable Health Communities / ACL Eldercare Locator | 本地服务存在不等于人能找到并接上；资源目录、热线、筛查、转介、回访和数据标准会决定住房、食物、交通、照护和心理健康支持能否形成闭环 | 社区资源导航、社会服务转介、资源目录标准、健康相关社会需求、闭环转介、反服务碎片化边界 | [211](https://www.211.org/), [Open Referral HSDS](https://docs.openreferral.org/en/latest/hsds/), [Gravity Project](https://thegravityproject.net/), [CMS AHC](https://www.cms.gov/priorities/innovation/innovation-models/ahcm), [ACL Eldercare Locator](https://eldercare.acl.gov/Public/Index.aspx) |
| 金融接入、支付与消费者金融保护 | World Bank Financial Inclusion / Global Findex / Digital Financial Services / Payment Systems / FDIC Household Survey / FDIC Money Smart / CFPB Consumer Complaint Database / Consumer Credit Trends / Federal Reserve Payments Study | 人能否安全收款、存钱、付款、汇款、建立信用、处理债务并避免掠夺性费用，取决于金融账户、支付系统、金融素养和消费者保护 | 金融包容、账户可得性、支付系统、数字金融服务、消费者投诉、信用与债务、反金融排除边界 | [World Bank financial inclusion](https://www.worldbank.org/en/topic/financialinclusion), [Global Findex](https://www.worldbank.org/en/publication/globalfindex), [digital financial services](https://www.worldbank.org/en/topic/financialinclusion/brief/digital-financial-services), [payment systems](https://www.worldbank.org/en/topic/financialinclusion/brief/payment-systems), [FDIC Household Survey](https://www.fdic.gov/household-survey), [FDIC Money Smart](https://www.fdic.gov/resources/consumers/money-smart/), [CFPB complaints](https://www.consumerfinance.gov/data-research/consumer-complaints/), [CFPB credit trends](https://www.consumerfinance.gov/data-research/consumer-credit-trends/), [Federal Reserve Payments Study](https://www.federalreserve.gov/paymentsystems/fr-payments-study.htm) |
| 保险、风险转移与理赔连续性 | NAIC consumer resources / USA.gov health insurance / unemployment benefits / workers' compensation / Benefits.gov Disability Assistance / FDIC deposit insurance / PBGC / World Bank disaster risk finance | 人生病、失业、工伤、残障、遭遇灾害、银行倒闭或养老金计划中断时，是否有风险池、保险覆盖、理赔路径、收入替代和申诉渠道，决定冲击是否会变成长期失稳 | 保险覆盖、理赔连续性、失业保险、工伤补偿、残障援助、存款保险、养老金保障、灾害风险融资、反保险排除边界 | [NAIC consumer](https://content.naic.org/consumer), [USA.gov health insurance](https://www.usa.gov/health-insurance), [USA.gov unemployment benefits](https://www.usa.gov/unemployment-benefits), [USA.gov workers' compensation](https://www.usa.gov/workers-compensation), [Benefits.gov disability assistance](https://www.benefits.gov/categories/Disability%20Assistance), [FDIC deposit insurance](https://www.fdic.gov/resources/deposit-insurance/), [PBGC](https://www.pbgc.gov/), [World Bank disaster risk finance](https://www.worldbank.org/en/topic/disasterriskmanagement/brief/disaster-risk-financing-and-insurance) |
| 食物保障、营养支持与水卫生 | FAO SOFI / FAOSTAT Food Security / WFP HungerMap LIVE / WHO healthy diet / WHO malnutrition / WHO food safety / WHO-UNICEF JMP / WHO drinking-water / WHO sanitation | 人的运行需要稳定获得足够食物、健康饮食、安全食品、清洁饮水和卫生设施；这些不是个人自律问题，而是生存与公共健康基础设施 | 食物保障、营养支持、饥饿监测、食品安全、饮水安全、卫生设施、WASH、灾害响应边界 | [FAO SOFI](https://www.fao.org/publications/fao-flagship-publications/the-state-of-food-security-and-nutrition-in-the-world/en), [FAOSTAT](https://www.fao.org/faostat/en/), [WFP HungerMap](https://hungermap.wfp.org/), [WHO healthy diet](https://www.who.int/news-room/fact-sheets/detail/healthy-diet), [WHO malnutrition](https://www.who.int/news-room/fact-sheets/detail/malnutrition), [WHO food safety](https://www.who.int/news-room/fact-sheets/detail/food-safety), [WHO/UNICEF JMP](https://washdata.org/), [WHO drinking-water](https://www.who.int/news-room/fact-sheets/detail/drinking-water), [WHO sanitation](https://www.who.int/news-room/fact-sheets/detail/sanitation) |
| 能源接入、清洁烹饪与基础公用事业 | World Bank Energy / IEA electricity access / IEA clean cooking / WHO household air pollution / DOE LEAD Tool / DOE Weatherization Assistance Program / EPA IAQ | 人的照明、烹饪、取暖、制冷、通信、医疗设备和室内空气，依赖可靠、可负担、清洁且安全的能源系统 | 电力接入、清洁烹饪、室内空气、能源负担、住宅能效、停电韧性、反能源贫困污名边界 | [World Bank Energy](https://www.worldbank.org/en/topic/energy), [IEA electricity access](https://www.iea.org/reports/sdg7-data-and-projections/access-to-electricity), [IEA clean cooking](https://www.iea.org/reports/sdg7-data-and-projections/access-to-clean-cooking), [WHO household air pollution](https://www.who.int/news-room/fact-sheets/detail/household-air-pollution-and-health), [DOE LEAD Tool](https://www.energy.gov/scep/slsc/lead-tool), [DOE Weatherization](https://www.energy.gov/scep/wap/weatherization-assistance-program), [EPA IAQ](https://www.epa.gov/indoor-air-quality-iaq) |
| 气候风险、早期预警与社区韧性 | IPCC AR6 / WMO Early Warnings for All / U.S. Climate Resilience Toolkit / Climate Mapping for Resilience and Adaptation / NOAA NCEI / CDC Climate and Health / CDC Heat and Health / CDC-ATSDR EJI | 人能否在热浪、洪水、火灾、风暴、空气质量恶化和基础设施中断中继续生活，取决于风险评估、预警、适应、撤离、冷却、恢复和公平资源配置 | 气候风险、早期预警、韧性规划、极端热、灾害损失、环境正义、反气候风险污名边界 | [IPCC AR6 SYR](https://www.ipcc.ch/report/ar6/syr/), [WMO Early Warnings for All](https://wmo.int/activities/early-warnings-all), [Climate Resilience Toolkit](https://toolkit.climate.gov/), [CMRA](https://resilience.climate.gov/), [NOAA billion-dollar disasters](https://www.ncei.noaa.gov/access/billions/), [NOAA climate data records](https://www.ncei.noaa.gov/products/climate-data-records), [CDC Climate and Health](https://www.cdc.gov/climate-health/), [CDC Heat and Health](https://www.cdc.gov/heat-health/), [CDC/ATSDR EJI](https://www.atsdr.cdc.gov/place-health/php/eji/index.html) |
| 家庭应急准备、个人韧性与灾前准备 | Red Cross preparedness / survival kit / make a plan / emergency app / CDC Prepare Your Health / CDC Natural Disasters safety / NOAA Weather-Ready Nation | 灾害前，人能否形成家庭计划、备用通信、物资包、药物和健康文件准备、特殊需求安排、风险认知和本地行动线索，会决定预警能否转成真实行动 | 家庭应急计划、个人韧性、健康准备、应急物资包、备用通信、风险认知、反个人责任转嫁边界 | [Red Cross preparedness](https://www.redcross.org/get-help/how-to-prepare-for-emergencies.html), [Red Cross survival kit](https://www.redcross.org/get-help/how-to-prepare-for-emergencies/survival-kit-supplies.html), [Red Cross make a plan](https://www.redcross.org/get-help/how-to-prepare-for-emergencies/make-a-plan.html), [Red Cross emergency app](https://www.redcross.org/get-help/how-to-prepare-for-emergencies/mobile-apps.html), [CDC Prepare Your Health](https://www.cdc.gov/prepare-your-health/), [CDC disaster safety](https://www.cdc.gov/natural-disasters/safety/), [NOAA Weather-Ready Nation](https://www.weather.gov/wrn/) |
| 公共预警、应急通信与求助入口 | FEMA IPAWS / FCC Wireless Emergency Alerts / FCC Emergency Alert System / NOAA Weather Radio / Ready.gov Alerts / 911.gov / Next Generation 911 / FirstNet | 灾害和危机发生时，人能否收到可信警报、理解风险、联系求助入口，并让响应者持续通信，决定服务连续性是否真的存在 | 公共预警、无线警报、广播警报、天气广播、911/NG911、第一响应者通信、反信息排除边界 | [FEMA IPAWS](https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system), [FCC WEA](https://www.fcc.gov/consumers/guides/wireless-emergency-alerts-wea), [FCC EAS](https://www.fcc.gov/emergency-alert-system), [NOAA Weather Radio](https://www.weather.gov/nwr/), [Ready.gov alerts](https://www.ready.gov/alerts), [911.gov](https://www.911.gov/), [NG911](https://www.911.gov/issues/ng911), [FirstNet](https://www.firstnet.gov/) |
| 灾后恢复、个人援助与临时安置 | USA.gov disaster / disaster assistance / disaster financial help / disaster food help / disaster bills help / FEMA Disaster Recovery Center Locator / SBA Disaster Assistance / Benefits.gov Disaster Relief / Red Cross shelters | 灾害之后，预警和救援只是开始；人能否重新获得住所、食物、现金、账单缓冲、恢复中心、低息贷款、临时避难和服务导航，会决定生活是否能重新接上 | 灾后援助、临时安置、恢复中心、财务帮助、账单帮助、灾害贷款、避难入口、反救助资格误导边界 | [USA.gov disaster](https://www.usa.gov/disaster), [USA.gov disaster assistance](https://www.usa.gov/disaster-assistance), [USA.gov disaster financial help](https://www.usa.gov/disaster-financial-help), [USA.gov disaster food help](https://www.usa.gov/disaster-food-help), [USA.gov disaster bills help](https://www.usa.gov/disaster-help-with-bills), [FEMA DRC Locator](https://egateway.fema.gov/ESF6/DRCLocator), [SBA disaster assistance](https://www.sba.gov/funding-programs/disaster-assistance), [Benefits.gov Disaster Relief](https://www.benefits.gov/categories/Disaster%20Relief), [Red Cross shelter](https://www.redcross.org/get-help/disaster-relief-and-recovery-services/find-an-open-shelter.html) |
| 免疫屏障、感染监测与公共卫生应急 | WHO vaccines and immunization / Immunization Agenda 2030 / CDC vaccines / CDC NNDSS / WHO GISRS / WHO IHR / WHO emergencies / WHO IPC / CDC NHSN / WHO AMR / GLASS / One Health / CDC NWSS | 人的长期运行依赖群体免疫、早期发现、感染防控、医疗相关感染监测、抗微生物耐药治理和跨物种风险治理 | 免疫计划、传染病监测、公共卫生应急、感染防控、AMR、One Health、废水监测边界 | [WHO immunization](https://www.who.int/health-topics/vaccines-and-immunization), [IA2030](https://www.who.int/teams/immunization-vaccines-and-biologicals/strategies/ia2030), [CDC vaccines](https://www.cdc.gov/vaccines/), [CDC NNDSS](https://www.cdc.gov/nndss/), [WHO GISRS](https://www.who.int/initiatives/global-influenza-surveillance-and-response-system), [WHO IHR](https://www.who.int/health-topics/international-health-regulations), [WHO emergencies](https://www.who.int/emergencies/overview), [WHO IPC](https://www.who.int/teams/integrated-health-services/infection-prevention-control), [CDC NHSN](https://www.cdc.gov/nhsn/), [WHO AMR](https://www.who.int/news-room/fact-sheets/detail/antimicrobial-resistance), [WHO GLASS](https://www.who.int/initiatives/glass), [WHO One Health](https://www.who.int/health-topics/one-health), [CDC NWSS](https://www.cdc.gov/nwss/) |
| 母婴健康、儿童发展与早期生命基础设施 | WHO maternal health / maternal mortality / WHO antenatal care / WHO newborn mortality / WHO child health / WHO child growth standards / Nurturing Care Framework / CDC PRAMS / CDC Child Development / DHS Program / World Bank ECD / Healthy People pregnancy and childbirth | 人的长期健康、学习、执行能力和功能连续性从孕产、新生儿、儿童早期照护、营养、生长和安全环境开始被塑造 | 孕产健康、新生儿、儿童健康、早期发展、成长监测、家庭调查、反监控边界 | [WHO maternal health](https://www.who.int/health-topics/maternal-health), [WHO maternal mortality](https://www.who.int/news-room/fact-sheets/detail/maternal-mortality), [WHO antenatal care](https://www.who.int/publications/i/item/9789241549912), [WHO newborn mortality](https://www.who.int/news-room/fact-sheets/detail/newborn-mortality), [WHO child health](https://www.who.int/health-topics/child-health), [WHO child growth standards](https://www.who.int/tools/child-growth-standards), [Nurturing Care Framework](https://www.who.int/publications/i/item/9789241514064), [CDC PRAMS](https://www.cdc.gov/prams/), [CDC Child Development](https://www.cdc.gov/child-development/), [DHS Program](https://dhsprogram.com/), [World Bank ECD](https://www.worldbank.org/en/topic/earlychildhooddevelopment), [Healthy People pregnancy and childbirth](https://odphp.health.gov/healthypeople/objectives-and-data/browse-objectives/pregnancy-and-childbirth) |
| 托育、早期教育与家庭工作连续性 | World Bank Childcare / ILO Care Work / DOL Childcare / ACF Office of Child Care / CCDF / ChildCare.gov / National Survey of Early Care and Education / Census child care / CDC Positive Parenting | 儿童能否获得安全照护和早期学习、照护者能否继续工作学习和恢复，取决于托育可得性、费用、质量、照护劳动条件和服务导航 | 托育可得性、早期教育、照护劳动、父母就业、家庭时间、服务导航、反托育污名边界 | [World Bank childcare](https://www.worldbank.org/en/topic/education/brief/childcare), [ILO care work](https://www.ilo.org/publications/major-publications/care-work-and-care-jobs-future-decent-work), [DOL childcare](https://www.dol.gov/agencies/wb/topics/childcare), [ACF OCC](https://www.acf.hhs.gov/occ), [CCDF](https://www.acf.hhs.gov/occ/programs/ccdf), [ChildCare.gov](https://childcare.gov/), [NSECE](https://www.acf.hhs.gov/opre/project/national-survey-early-care-and-education-2019-2017-2022), [Census child care](https://www.census.gov/topics/families/child-care.html), [CDC positive parenting](https://www.cdc.gov/child-development/positive-parenting-tips/index.html) |
| 法律身份、公民登记与权利入口 | UN Legal Identity Agenda / UN Statistics CRVS / WHO CRVS / World Bank ID4D data / UNICEF birth registration | 人能否进入教育、医疗、福利、金融、迁移、投票、继承、数字身份和公共服务，常常先取决于是否被制度承认为一个可证明的人 | 出生登记、法律身份、民事登记、生命统计、证件可得性、身份排除和反监控边界 | [UN Legal Identity Agenda](https://unstats.un.org/legal-identity-agenda/), [UN Statistics CRVS](https://unstats.un.org/unsd/demographic-social/crvs/), [WHO CRVS](https://www.who.int/data/data-collection-tools/civil-registration-and-vital-statistics-%28crvs%29), [World Bank ID4D data](https://datacatalog.worldbank.org/search/dataset/0040787/identification-for-development-id4d-global-dataset), [UNICEF birth registration](https://www.unicef.org/stories/birth-registration) |
| 司法可及、法律援助与权利救济 | UN SDG 16 / World Justice Project Rule of Law Index / Legal Services Corporation Justice Gap / DOJ Office for Access to Justice / ABA Free Legal Answers | 人被制度承认之后，还必须能理解权利、解决纠纷、获得法律帮助、申诉救济和避免被复杂程序排除 | 司法可及、民事法律需求、法律援助、在线法律帮助、权利救济、反程序性排除边界 | [UN SDG 16](https://sdgs.un.org/goals/goal16), [WJP Rule of Law Index](https://worldjusticeproject.org/rule-of-law-index/), [LSC Justice Gap](https://justicegap.lsc.gov/), [LSC Justice Gap Research](https://www.lsc.gov/initiatives/justice-gap-research), [DOJ Access to Justice](https://www.justice.gov/atj), [ABA Free Legal Answers](https://abafreelegalanswers.org/) |
| 公民参与、投票可达与选举基础设施 | USA.gov voter registration / EAC voters / EAC National Mail Voter Registration Form / EAC VVSG / NIST voting / DOJ Voting Section / ADA voting / International IDEA turnout / ACE Project / OSCE ODIHR elections | 人能否影响制度，不只取决于是否有名义权利；登记、投票地点、设备、无障碍、语言、信息可信度、投票权执行和选举管理会决定参与是否真实可达 | 选民登记、投票可达、无障碍投票、选举系统标准、选举观察、参与数据、反党派操控边界 | [USA.gov voter registration](https://www.usa.gov/register-to-vote), [EAC voters](https://www.eac.gov/voters), [EAC NVRA form](https://www.eac.gov/voters/national-mail-voter-registration-form), [EAC VVSG](https://www.eac.gov/voting-equipment/voluntary-voting-system-guidelines), [NIST voting](https://www.nist.gov/itl/voting), [DOJ Voting Section](https://www.justice.gov/crt/voting-section), [ADA voting](https://www.ada.gov/topics/voting/), [International IDEA turnout](https://www.idea.int/data-tools/data/voter-turnout-database), [ACE Project](https://aceproject.org/), [OSCE ODIHR elections](https://www.osce.org/odihr/elections) |
| 迁移、流离失所与人道服务连续性 | UN Global Compact for Migration / IOM World Migration Report / UNHCR Operational Data Portal / WHO Health and Migration / IDMC GRID / OCHA HDX / INEE Minimum Standards | 当人跨境、内部流离失所或处在人道危机中，身份、庇护、医疗、教育、保护、信息和服务协调必须连续衔接 | 强迫迁移、内部流离失所、人道数据、健康迁移、教育连续性、庇护与保护、反排除边界 | [Global Compact for Migration](https://refugeesmigrants.un.org/migration-compact), [IOM World Migration Report](https://worldmigrationreport.iom.int/), [UNHCR Operational Data Portal](https://data.unhcr.org/en/situations), [WHO Health and Migration](https://www.who.int/teams/health-and-migration-programme), [IDMC GRID 2025](https://www.internal-displacement.org/global-report/grid2025/), [OCHA HDX](https://data.humdata.org/), [INEE Minimum Standards](https://inee.org/minimum-standards) |
| 数字接入、信息可达与公共服务基础设施 | ITU ICT statistics / World Bank Digital Development / NTIA Digital Nation / U.S. Census computer and internet use / NIST digital identity / Login.gov / Digital.gov / U.S. Web Design System / UNESCO MIL / IMLS Public Libraries Survey | 人是否能使用 AI、健康服务、教育、福利、求职和公共信息，取决于网络、设备、数字身份、可用公共服务和信息素养 | 数字包容、宽带/互联网接入、数字身份、公共服务体验、信息素养、公共图书馆、反数字排除边界 | [ITU ICT statistics](https://www.itu.int/itu-d/reports/statistics/), [World Bank Digital Development](https://www.worldbank.org/en/topic/digitaldevelopment), [NTIA Digital Nation](https://www.ntia.gov/data/explorer), [U.S. Census computer and internet use](https://www.census.gov/topics/population/computer-internet.html), [NIST digital identity](https://pages.nist.gov/800-63-4/), [Login.gov](https://www.login.gov/), [Digital.gov](https://digital.gov/), [USWDS](https://designsystem.digital.gov/), [UNESCO MIL](https://www.unesco.org/en/media-information-literacy), [IMLS PLS](https://www.imls.gov/research-evaluation/surveys/public-libraries-survey-pls) |
| 个人数字安全、账号恢复与身份盗用防护 | FTC scams / FTC phishing / IdentityTheft.gov / ReportFraud / FBI IC3 / NIST digital identity / Login.gov | 数字服务存在不等于人能安全保有入口；钓鱼、诈骗、账号接管、身份盗用和恢复失败会切断金融、医疗、福利、教育和公共服务 | 账号安全、钓鱼防护、身份盗用恢复、诈骗举报、账号恢复、反受害者归因边界 | [FTC scams](https://consumer.ftc.gov/scams), [FTC phishing](https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams), [IdentityTheft.gov](https://www.identitytheft.gov/), [ReportFraud](https://reportfraud.ftc.gov/), [FBI IC3](https://www.ic3.gov/), [NIST digital identity](https://pages.nist.gov/800-63-4/), [Login.gov help](https://www.login.gov/help/) |
| 语言可达、清晰沟通与健康素养 | PlainLanguage.gov / Digital.gov plain language / LEP.gov / National CLAS Standards / CDC health literacy / CDC Clear Communication Index / W3C cognitive accessibility | 人能否使用医疗、福利、法律、教育、就业和公共服务，取决于材料是否清晰、可翻译、可解释、认知友好，并能覆盖有限英语能力者和低健康素养场景 | 清晰沟通、语言服务、健康素养、认知可访问性、公共服务理解、反语言排除边界 | [PlainLanguage.gov](https://www.plainlanguage.gov/), [Digital.gov plain language](https://digital.gov/guides/plain-language), [LEP.gov](https://www.lep.gov/), [National CLAS](https://thinkculturalhealth.hhs.gov/clas), [CDC health literacy](https://www.cdc.gov/health-literacy/php/about/index.html), [CDC Clear Communication Index](https://www.cdc.gov/ccindex/index.html), [W3C cognitive accessibility](https://www.w3.org/WAI/cognitive/) |
| 交通可达、公共交通与日常移动 | World Bank Transport / FTA National Transit Database / BTS National Household Travel Survey / USDOT Equitable Transportation Community Explorer RFI / FTA ADA guidance | 人能否到达学校、工作、医疗、福利、照护、食物、社交和避难地点，取决于可靠、可负担、安全、无障碍且可解释的交通系统 | 交通可达、公共交通、日常出行、交通公平、无障碍交通、辅助交通、灾害撤离、反交通贫困污名边界 | [World Bank Transport](https://www.worldbank.org/en/topic/transport), [FTA NTD](https://www.transit.dot.gov/ntd), [NHTS](https://nhts.ornl.gov/), [USDOT ETCE RFI](https://www.federalregister.gov/documents/2023/02/21/2023-03396/request-for-information-on-us-dot-equitable-transportation-community-explorer-etce-tool-and-index), [FTA ADA guidance](https://www.transit.dot.gov/regulations-and-guidance/civil-rights-ada/ada-guidance), [FTA ADA FAQs](https://www.transit.dot.gov/regulations-and-guidance/civil-rights-ada/frequently-asked-questions) |
| 医疗可及性、初级卫生保健与基本服务 | WHO Universal Health Coverage / WHO Primary Health Care / WHO Essential Medicines Lists / WHO Health Workforce / World Bank UHC / CDC access and insurance / AHRQ NHQDR Data Tools | 人生病、受伤、怀孕、慢病管理或需要预防服务时，能否进入可信医疗系统，取决于覆盖、费用、距离、等待时间、医护 workforce、基本药物和服务质量 | 医疗可及性、全民健康覆盖、初级卫生保健、基本药物、医护人员、保险覆盖、质量差异、反医疗排除边界 | [WHO UHC](https://www.who.int/health-topics/universal-health-coverage), [WHO PHC](https://www.who.int/health-topics/primary-health-care), [WHO essential medicines](https://www.who.int/groups/expert-committee-on-selection-and-use-of-essential-medicines/essential-medicines-lists), [WHO health workforce](https://www.who.int/health-topics/health-workforce), [World Bank UHC](https://www.worldbank.org/en/topic/universalhealthcoverage), [CDC access to health care](https://www.cdc.gov/nchs/fastats/access-to-health-care.htm), [CDC health insurance](https://www.cdc.gov/nchs/fastats/health-insurance.htm), [AHRQ Data Tools](https://datatools.ahrq.gov/) |
| 远程医疗、数字照护与居家监测 | Telehealth.HHS.gov / HHS Remote Patient Monitoring / HRSA Telehealth / CMS Telehealth / Medicare telehealth / FDA Digital Health | 医疗服务能否跨越距离、行动受限、慢病随访、农村可及和居家照护断点，取决于远程问诊、远程监测、支付覆盖、设备、隐私和数字能力 | 远程医疗、远程患者监测、虚拟照护、居家连续性、支付覆盖、设备和宽带、反数字医疗排除边界 | [Telehealth.HHS.gov](https://telehealth.hhs.gov/), [HHS remote patient monitoring](https://telehealth.hhs.gov/providers/best-practice-guides/telehealth-and-remote-patient-monitoring), [HRSA telehealth](https://www.hrsa.gov/telehealth), [CMS telehealth](https://www.cms.gov/medicare/coverage/telehealth), [Medicare telehealth](https://www.medicare.gov/coverage/telehealth), [FDA Digital Health](https://www.fda.gov/medical-devices/digital-health-center-excellence) |
| 药品可及、用药安全与供应连续性 | WHO Essential Medicines / WHO Medication Without Harm / FDA Drug Shortages / FDA NDC Directory / DailyMed / MedlinePlus Medicines / Medicare Part D / CDC Medication Safety | 医疗建议能否变成持续治疗，取决于关键药物选择、供应、短缺、价格覆盖、标签说明、患者理解、药房渠道和用药错误防护 | 药品可及、用药安全、药品短缺、标签信息、患者药品信息、处方药覆盖、反自行用药边界 | [WHO essential medicines](https://www.who.int/groups/expert-committee-on-selection-and-use-of-essential-medicines/essential-medicines-lists), [WHO Medication Without Harm](https://www.who.int/initiatives/medication-without-harm), [FDA drug shortages](https://www.fda.gov/drugs/drug-safety-and-availability/drug-shortages), [FDA NDC Directory](https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory), [DailyMed](https://dailymed.nlm.nih.gov/dailymed/), [MedlinePlus medicines](https://medlineplus.gov/medicines.html), [Medicare Part D](https://www.medicare.gov/drug-coverage-part-d), [CDC Medication Safety](https://www.cdc.gov/medication-safety/) |
| 心理健康、成瘾与危机照护 | WHO World Mental Health Report / WHO mhGAP / WHO Mental Health Atlas / FindTreatment.gov / NIMH mental illness / CDC overdose prevention / 988 Lifeline | 人能否持续生活和执行任务，取决于心理健康服务、成瘾治疗、危机响应、社区支持和反污名机制能否及时可达 | 心理健康服务、社区照护、物质使用障碍、成瘾治疗、过量预防、危机连续照护、反污名边界 | [WHO World Mental Health Report](https://www.who.int/publications/i/item/9789240049338), [WHO mhGAP](https://www.who.int/teams/mental-health-and-substance-use/treatment-care/mental-health-gap-action-programme), [WHO Mental Health Atlas](https://www.who.int/publications/i/item/9789240036703), [FindTreatment.gov](https://findtreatment.gov/), [NIMH mental illness](https://www.nimh.nih.gov/health/statistics/mental-illness), [CDC overdose prevention](https://www.cdc.gov/overdose-prevention/), [988 Lifeline](https://988lifeline.org/) |
| 人身安全、伤害预防与应急响应基础设施 | WHO injuries and violence / CDC Injury Center / CDC WISQARS / CDC Violence Prevention / CDC ACEs / CDC Suicide Prevention / 988 Lifeline / WHO Emergency Care / CDC Natural Disasters | 人能否持续生活、学习、工作，取决于能否免于可预防伤害、暴力、创伤和灾害冲击，并在危机后获得及时救援 | 伤害监测、暴力预防、儿童逆境、危机支持、急救系统、灾害准备、反惩罚性风险评分边界 | [WHO injuries and violence](https://www.who.int/news-room/fact-sheets/detail/injuries-and-violence), [CDC Injury Center](https://www.cdc.gov/injury/), [CDC WISQARS](https://www.cdc.gov/injury/wisqars/), [CDC Violence Prevention](https://www.cdc.gov/violence-prevention/), [CDC ACEs](https://www.cdc.gov/aces/about/index.html), [CDC Suicide Prevention](https://www.cdc.gov/suicide/), [988 Lifeline](https://988lifeline.org/), [WHO Emergency Care](https://www.who.int/health-topics/emergency-care), [CDC Natural Disasters](https://www.cdc.gov/natural-disasters/) |
| 建成环境、交通与环境暴露 | WHO Housing and Health / WHO Urban Health / CDC Built Environment Assessment Tool / CDC Active Communities Tool / WHO Air Quality Guidelines / AirNow / CDC Heat and Health Index / WHO Road Safety | 人的睡眠、活动、恢复、社交、通勤、热暴露、空气暴露和伤害风险都受房屋、街道、交通与城市环境约束 | 住房健康、城市健康、可步行性、空气质量、热风险、道路安全、环境暴露边界 | [WHO housing guidelines](https://www.who.int/publications/i/item/9789241550376), [WHO urban health](https://www.who.int/health-topics/urban-health), [CDC BE Tool](https://www.cdc.gov/physical-activity/php/built-environment-assessment/index.html), [CDC Active Communities Tool](https://www.cdc.gov/active-communities-tool/php/about/index.html), [WHO air quality guidelines](https://www.who.int/publications/i/item/9789240034228), [AirNow](https://www.airnow.gov/), [CDC Heat and Health Index](https://www.atsdr.cdc.gov/place-health/php/hhi/index.html), [WHO road safety](https://www.who.int/publications/i/item/9789240086517) |
| 学习、技能形成与能力成长 | National Academies How People Learn II / IES What Works Clearinghouse / UNESCO UIS / UNESCO UIL / O*NET / World Bank Human Capital | 人类长期执行能力依赖学习机制、反馈、教育证据、技能地图、终身学习和能力投资，而不只是意志或工具 | 学习科学、教育证据、技能分类、终身学习、人力资本、训练反馈边界 | [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures), [IES WWC](https://ies.ed.gov/ncee/wwc/), [UNESCO UIS](https://www.uis.unesco.org/en), [UNESCO UIL](https://www.uil.unesco.org/en), [O*NET](https://www.onetcenter.org/overview.html), [World Bank Human Capital](https://www.worldbank.org/en/publication/human-capital) |
| 就业服务、劳动力发展与职业转换 | World Bank Jobs and Development / ILO Employment Promotion / DOL ETA / WIOA / American Job Centers / Apprenticeship.gov / O*NET / My Next Move / JAN | 人能否把能力转成工作和收入，取决于职业信息、公共就业服务、培训、学徒制、转岗支持、无障碍就业和劳动力市场制度 | 就业服务、职业导航、再培训、学徒制、职业转换、就业无障碍、反自动筛选边界 | [World Bank jobs](https://www.worldbank.org/en/topic/jobsanddevelopment), [ILO employment promotion](https://www.ilo.org/topics/employment-promotion), [DOL ETA](https://www.dol.gov/agencies/eta), [WIOA](https://www.dol.gov/agencies/eta/wioa), [American Job Centers](https://www.dol.gov/agencies/eta/american-job-centers), [Apprenticeship.gov](https://www.apprenticeship.gov/), [O*NET Center](https://www.onetcenter.org/overview.html), [O*NET Online](https://www.onetonline.org/), [My Next Move](https://www.mynextmove.org/), [JAN](https://askjan.org/) |
| 可穿戴健康监测 | Apple Heart Study | 消费级传感器可以进入大规模健康筛查和反馈链路，但需要临床验证和风险沟通 | 传感器、反馈、医学边界、数字健康 | [NEJM Apple Heart Study](https://www.nejm.org/doi/full/10.1056/NEJMoa1901183), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31722151/), [Stanford Medicine](https://med.stanford.edu/news/all-news/2019/11/through-apple-heart-study--stanford-medicine-researchers-show-we.html) |
| 职业健康与组织设计 | NIOSH Total Worker Health | 工作不是背景变量，而是影响健康、安全和福祉的系统条件 | 组织基础设施、恢复、风险控制、反压榨边界 | [NIOSH TWH Program](https://www.cdc.gov/niosh/twh/programs/index.html), [TWH overview](https://www.cdc.gov/niosh/twh/index.html) |
| 老年整合照护 | WHO ICOPE | 健康老龄化可以围绕内在能力、功能能力和个性化照护路径组织 | 健康寿命、照护路径、主体能力维护 | [WHO ICOPE handbook](https://www.who.int/publications/i/item/9789240103726), [WHO ICOPE training](https://www.decadeofhealthyageing.org/find-knowledge/support/training-programmes/who-integrated-care-for-older-people-%28icope%29-training-programme-field-testing-version) |
| 照护、家庭照护者与长期服务 | National Strategy to Support Family Caregivers / CDC Caregiving / National Academies Families Caring / Medicaid HCBS / Medicare home health / AHRQ Care Coordination / WHO long-term care | 人的长期运行依赖家庭照护者、居家社区服务、照护协调、喘息支持和长期照护系统，而不只是个人自理能力 | 家庭照护者、长期服务、居家社区支持、照护协调、服务可达性、反责任转嫁边界 | [National Strategy](https://www.federalregister.gov/documents/2022/10/06/2022-21697/2022-national-strategy-to-support-family-caregivers-available-for-public-comments), [CDC Caregiving](https://www.cdc.gov/caregiving/index.html), [Families Caring](https://www.ncbi.nlm.nih.gov/books/NBK396398/), [Medicaid HCBS](https://www.medicaid.gov/medicaid/home-community-based-services/index.html), [Medicare home health](https://www.medicare.gov/coverage/home-health-services), [AHRQ care coordination](https://www.ahrq.gov/ncepcr/care/coordination.html), [WHO long-term care](https://www.who.int/publications/i/item/9789240038844) |
| 极端环境人因 | NASA Human Research Program | 太空飞行把人类健康、表现、风险、训练、任务和环境约束压缩到一个高风险系统里 | 人因工程、生命支持、任务表现、极端环境恢复 | [NASA HRP](https://www.nasa.gov/hrp/), [NASA Human Health and Performance](https://www.nasa.gov/hhp/), [NASA spaceflight risks](https://www.nasa.gov/humans-in-space/hhc-spaceflight-risks/) |
| 军队人类表现优化 | U.S. Army H2F / Total Force Fitness | 高压组织已经把体能、睡眠、营养、心理和恢复合并成战备基础设施 | 高压任务执行、恢复、训练系统、组织支持 | [Army H2F](https://h2f.army.mil/), [Army H2F overview](https://www.goarmy.com/explore-the-army/holistic-health-fitness), [Total Force Fitness review](https://pmc.ncbi.nlm.nih.gov/articles/PMC10666955/) |
| 神经科技基础设施 | NIH BRAIN Initiative / DARPA NESD / Neuralink PRIME | 神经接口、脑功能理解和临床设备试验正在形成高风险神经基础设施 | 记忆编辑、去具身中枢、主体权利、安全审计 | [NIH BRAIN Initiative](https://braininitiative.nih.gov/), [DARPA NESD](https://www.darpa.mil/research/programs/neural-engineering-system-design), [Neuralink PRIME on ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06429735), [FDA IDE overview](https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/investigational-device-exemption-ide) |
| 神经伦理与 BCI 安全治理 | BRAIN Neuroethics / OECD Neurotechnology / UNESCO Neurotechnology Ethics / FDA BCI guidance | 神经科技必须同时处理主体性、隐私、同意、临床安全、设备可靠性和试验监管 | 记忆编辑边界、BCI 临床安全、神经数据治理、退出权 | [BRAIN Neuroethics principles](https://pmc.ncbi.nlm.nih.gov/articles/PMC6297371/), [OECD neurotechnology recommendation](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0457), [UNESCO neurotechnology ethics](https://www.unesco.org/en/ethics-neurotech), [FDA implanted BCI guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/implanted-brain-computer-interface-bci-devices-patients-paralysis-or-amputation-non-clinical-testing) |
| 系统安全与人机组织 | NASA Human Systems Integration / Leveson STAMP | 人的限制、训练、维护、组织决策和安全控制必须在系统设计中前置 | Human SRE、事故预防、任务系统、安全边界 | [NASA HSI lessons](https://www.nasa.gov/humans-in-space/commercial-space/leo-economy/nasa-shares-lessons-human-systems-integration/), [Engineering a Safer World](https://direct.mit.edu/books/oa-monograph/2908/Engineering-a-Safer-WorldSystems-Thinking-Applied) |
| AI 与知识工作基础设施 | NIST AI RMF / NASA-TLX / Human-AI Teaming / Generative AI at Work | AI 工具、工作负荷、交互规则、风险治理和生产率影响必须一起看，不能只看模型能力 | 人机协作、认知负荷、注意力恢复、知识工作系统 | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), [NASA-TLX](https://www.nasa.gov/human-systems-integration-division/nasa-task-load-index-tlx/), [Guidelines for Human-AI Interaction](https://doi.org/10.1145/3290605.3300233), [Generative AI at Work](https://www.nber.org/papers/w31161) |
| 组织安全与事件学习 | WHO Patient Safety / AHRQ TeamSTEPPS / CUSP / HRO / RCA2 | 人的错误、疲劳、交接、沟通和事故复盘必须被设计成组织学习系统，而不是只追责个人 | 医疗安全、疲劳管理、班次设计、复盘机制、组织韧性 | [WHO patient safety action plan](https://www.who.int/publications/i/item/9789240032705), [AHRQ TeamSTEPPS](https://www.ahrq.gov/teamstepps-program/index.html), [AHRQ CUSP](https://www.ahrq.gov/hai/cusp/index.html), [IHI RCA2](https://www.ihi.org/resources/tools/rca2-improving-root-cause-analyses-and-actions-prevent-harm) |

## 公共健康基线

这些资料不是“优化方案”，而是 Human Infra 的底座：睡眠、运动、营养、心理健康和工作福祉。如果没有这些公共健康基线，任何更激进的长寿、自我量化、神经科技或未来等待叙事都会失去现实约束。

| 基线层 | 一手资料 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 身体活动 | WHO Guidelines on physical activity and sedentary behaviour；HHS Physical Activity Guidelines for Americans | 把运动从个人意志问题转成公共健康和生活基础设施问题 | 不能替代个体医疗评估，尤其是慢病、伤病和高风险人群 |
| 睡眠 | AASM / Sleep Research Society 成人睡眠时长共识；CDC Sleep and Sleep Disorders | 把恢复视为运行系统的核心依赖，而不是可牺牲时间 | 不能把睡眠建议泛化为诊断或治疗方案 |
| 营养 | Dietary Guidelines for Americans | 为饮食、代谢和健康寿命讨论提供公共政策基线 | 不能替代医疗营养治疗或个体化饮食处方 |
| 工作心理健康 | WHO Guidelines on mental health at work；U.S. Surgeon General Workplace Mental Health and Well-Being Framework | 把心理健康和工作设计纳入基础设施，而不是只归因于个人韧性 | 不能被用来包装绩效压榨或组织监控 |
| 工作者福祉测量 | NIOSH Worker Well-Being Questionnaire | 提供组织层面观察工作者福祉的结构化工具 | 测量必须服务于保护和改善，不应成为惩罚性监控 |

## 压力、负荷与恢复底座

这一层回答“人为什么会在没有明显疾病时长期失效”：Human Infra 不能只看任务、指标和工具，也必须看压力暴露、恢复不足、主观负荷、睡眠债、工作条件、社会支持和组织责任。压力不是单纯情绪问题，恢复也不是个人偷懒；它们会进入生理负荷、认知负荷、错误率、慢病风险和长期执行能力。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 慢性压力生理学 | McEwen / Stellar allostatic load；McEwen stress and allostatic load review | 把压力反应、适应代价和长期健康风险放进同一套生理负荷语言 | allostatic load 是解释框架和研究线索，不是个人诊断或单一健康评分 |
| 主观压力测量 | Cohen Perceived Stress Scale | 为“压力感”提供可复用的自报测量入口，适合研究压力暴露和体验差异 | 自报量表不能替代临床评估，也不能被组织用于惩罚或排名 |
| 工作心理健康 | WHO Guidelines on mental health at work；U.S. Surgeon General Workplace Mental Health and Well-Being Framework | 把心理健康、工作设计、保护、支持和组织责任连接起来 | 工作心理健康不能被缩减成个人韧性培训或福利包装 |
| 倦怠边界 | WHO burn-out occupational phenomenon | 把 burn-out 放回职业语境，强调它不是任意个人弱点标签 | 倦怠条目不能替代医疗诊断，也不能用来规避组织对工作条件的责任 |
| 工作者福祉测量 | NIOSH Worker Well-Being Questionnaire | 为组织层面观察工作、健康、环境和福祉提供结构化工具 | 测量必须用于改善条件和保护主体，不应变成监控系统 |
| 疲劳与恢复风险 | NIOSH Fatigue at Work；OSHA Worker Fatigue | 把长工时、夜班、恢复不足和事故风险纳入系统设计变量 | 疲劳管理不能要求个人硬扛；排班、 staffing 和资源配置是组织责任 |

## 社会决定因素与生活环境底座

这一层回答“为什么同样的工具和建议在不同人身上效果完全不同”：Human Infra 不能把健康、表现和恢复全都解释成个人选择。出生地、住房、收入、教育、空气、交通、食物可及性、社区安全、医疗可及性和社会支持，都会改变一个人能否长期执行、恢复和延续。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 上位框架 | WHO Social Determinants of Health；Healthy People 2030 Social Determinants of Health | 把健康差异放回生活、成长、工作、老去和社会系统条件中解释 | SDOH 框架不能被用作个人责任减免或群体标签化的粗暴工具 |
| 社区脆弱性 | CDC/ATSDR Social Vulnerability Index | 用社会经济、住房、交通、家庭结构等因素观察社区在灾害和压力下的脆弱性 | SVI 是社区层面规划工具，不是个人风险评分或资源剥夺理由 |
| 环境正义负担 | CDC/ATSDR Environmental Justice Index | 把环境暴露、社会脆弱性和健康脆弱性放到地理尺度上观察 | EJI 适合识别环境不平等线索，不能替代本地调查或个体诊断 |
| 本地健康地图 | CDC PLACES | 提供县、市、普查区等小区域慢病、预防和健康风险估计 | 小区域估计有模型误差，适合公共卫生规划，不适合个人判断 |
| 食物可及性 | USDA Food Access Research Atlas | 把低收入、交通距离和食物零售可达性纳入生活基础设施 | 食物可及性不是个人饮食偏好判断，也不能单独解释营养状态 |
| 健康相关社会需求 | CMS Accountable Health Communities Model | 展示医疗系统如何识别并连接住房、食物、交通、水电安全和人身安全等社会需求 | 临床筛查必须尊重同意、隐私和服务可得性，不能只收集需求却不给支持 |

## 住房稳定、无家可归与驱逐风险底座

这一层回答“人有没有一个能持续生活的地方”：Human Infra 不能把住所当作自然存在的背景。住房负担、租约不稳定、驱逐、无家可归、临时居住、拥挤、家庭迁移和收容系统，都会破坏睡眠、儿童上学、药物保存、慢病管理、证件保管、社交关系和工作连续性。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 全球住房框架 | UN-Habitat Housing | 把住房放入城市发展、居住权和基础服务语境，而不是只看建筑本身 | 全球框架不能替代本地住房法规、租赁关系和服务资格判断 |
| 无家可归统计 | HUD Annual Homeless Assessment Report | 为无家可归人数、趋势、庇护系统和群体差异提供公开数据入口 | AHAR 是统计和政策资料，不是个案服务资格、安置承诺或执法依据 |
| 住房质量与负担 | U.S. Census American Housing Survey | 观察住房成本、质量、设施、负担和家庭条件 | AHS 是调查资料，不能替代本地房屋检查、法律意见或个体风险判断 |
| 住房不安全信号 | U.S. Census Household Pulse Survey | 用高频调查观察支付困难、搬迁风险和家庭压力 | Pulse 数据适合群体趋势观察，不是个人信用、租赁或福利资格判断 |
| 驱逐数据 | Eviction Lab；Eviction Tracking System | 把驱逐从个案纠纷放回住房市场、法院、贫困和家庭稳定系统中观察 | 驱逐数据不是法律意见，也不能用于给租户、房东或社区贴惩罚性标签 |

## 社会连接、孤独风险与社区归属底座

这一层回答“人是否有关系网络和社区支持继续生活”：Human Infra 不能把孤独、断联、缺乏归属和服务不可达解释成个人性格问题。稳定关系、互助网络、社区参与、社会处方、老年人支持和公共服务连接，会影响健康风险、照护可达性、恢复机会、危机发现和长期执行能力。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 全球社会连接框架 | WHO social connection report；WHO social isolation and loneliness | 把孤独和社会隔离视为公共健康和社会系统问题，而不是个体弱点 | 社会连接框架不是个人诊断，也不能把关系质量简化成数量 KPI |
| 社会连接公共健康入口 | CDC Social Connectedness；CDC risk factors | 解释社会连接、孤独风险因素和健康关系，适合进入基础设施地图 | CDC 资料不能替代心理健康评估，也不能用于给个体贴孤独标签 |
| 社会与社区语境 | Healthy People 2030 Social and Community Context | 把家庭、学校、工作、社区和歧视等社会语境纳入健康目标 | 群体目标不能替代本地服务设计，也不能被用于排除高风险社区 |
| 老年社会隔离 | National Academies Social Isolation and Loneliness in Older Adults | 把老年人的社会隔离和孤独接入医疗、照护和社区识别路径 | 报告不是单个老人的风险评分，也不能把照护责任转嫁给家庭 |
| 社会处方路径 | NHS England social prescribing | 展示医疗和社区服务如何把人连接到活动、支持、福利、自然和志愿服务 | 社会处方不是廉价替代医疗、心理治疗或社会保障；必须看服务质量和可及性 |

## 经济安全、社会保护与时间结构底座

这一层回答“人是否有足够资源和时间维持运行”：Human Infra 不能把收入、现金缓冲、工作时间、带薪休假、社会保险、税收抵免和社会救助看成外部背景。经济不安全会压缩睡眠、恢复、学习、照护、就医和长期规划；时间贫困也会让复杂任务无法展开。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 社会保护框架 | ILO social protection；World Social Protection Report | 把医疗、收入安全、儿童、失业、伤残、老年和照护风险放入社会保护体系 | 社会保护框架不是单一政策处方，也不能替代地区制度设计 |
| 社会保护地板 | ILO Social Protection Floors Recommendation No. 202 | 为最低收入安全和基本服务可及性提供国际规范语境 | 国际建议不是自动法律权利，也不能替代本地资格规则 |
| 普遍社会保护 | World Bank Universal Social Protection | 把生命周期风险、贫困冲击和社会保护覆盖纳入发展基础设施 | 世界银行资料不能被简化成单一国家方案或福利承诺 |
| 社会保护数据 | World Bank ASPIRE | 提供社会保护和劳动力项目覆盖、支出和受益分布的数据入口 | 跨国数据适合宏观比较，不能直接判断个体资格或政策充分性 |
| 带薪休假与照护假 | U.S. DOL paid leave；Family and Medical Leave Act | 把生育、疾病、照护和工作中断风险接入劳动制度 | FMLA 和带薪假资料是美国制度语境，不是所有地区都适用 |
| 时间使用与无偿劳动 | UN time-use statistics；ILO working time | 把家务、照护、工作时间和时间贫困变成可观察的基础设施变量 | 时间使用统计不能用于压迫个体效率，也不能抹去无偿劳动价值 |
| 家庭财务韧性 | Federal Reserve SHED；CFPB financial well-being | 把现金缓冲、账单压力、金融能力和主观财务安全纳入运行状态 | 金融福祉不是个人道德评分，也不能替代收入、住房和医疗制度问题 |
| 税收抵免与收入支持 | IRS Earned Income Tax Credit | 展示税收系统如何成为低收入劳动者收入支持工具 | EITC 资格复杂且地区特定，不是税务建议或自动申领承诺 |

## 公共福利、行政负担与服务导航底座

这一层回答“制度存在之后，人能否真的获得支持”：Human Infra 不能把福利、补助、医保、食物援助、住房援助、能源援助和残障收入支持只看成政策名词。资格理解、申请入口、证明材料、等待时间、续期规则、申诉路径、语言、无障碍、身份核验和人工帮助，会决定纸面权利能否变成现实生活能力。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 福利导航入口 | USA.gov Benefit Finder；USAGov food assistance | 把跨项目福利查找、类别筛选和申请理解视为公共服务基础设施 | 导航入口不是资格承诺，也不能替代州、地方和项目规则 |
| 服务递送体验 | Performance.gov Federal Customer Experience | 把案例状态、表单、身份核验、人工帮助、反馈和跨机构体验纳入政府服务质量 | 数字化和 CX 不能成为取消线下渠道、缩减帮助或扩大监控的理由 |
| 医疗保障申请 | Medicaid.gov eligibility；HealthCare.gov Medicaid & CHIP | 展示资格、州机构、申请、续期和覆盖转换如何影响医疗可及性 | Medicaid/CHIP 规则高度依赖州和家庭处境，不能做个体资格承诺 |
| 收入与残障支持 | SSA Supplemental Security Income | 把老年、残障、低收入和资源限制接入收入安全基础设施 | SSI 资料不是法律意见、残障认定或自动获益承诺 |
| 能源账单援助 | ACF LIHEAP | 把取暖、制冷、能源危机和家庭能源负担纳入福利服务递送 | LIHEAP 资金、资格和申请路径地区差异大，不能泛化承诺 |
| 行政负担理论 | Moynihan / Herd / Harvey；Herd / Moynihan | 用学习成本、心理成本和合规成本解释为什么人会被程序排除 | 行政负担框架不能替代具体项目评估，也不能把所有失败归因于个体不会申请 |

## 社区资源导航、社会服务转介与资源目录底座

这一层回答“本地服务存在之后，人如何真正接上它”：Human Infra 不能只列出福利项目、医疗入口和照护服务，还必须处理服务目录是否准确、热线是否可达、需求筛查是否尊重隐私、转介是否闭环、服务是否有容量、数据标准是否可互操作、照护者和个案管理者是否能追踪结果。否则人会在多个机构、表单、电话、资格规则和过期资源之间来回断线。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 社区求助入口 | 211 | 把食物、住房、账单、危机和本地资源查找放入热线与在线导航入口 | 211 不是服务资格承诺，也不保证本地机构有容量或即时响应 |
| 资源目录标准 | Open Referral Human Services Data Specification | 为组织、地点、服务、资格、联系入口和覆盖范围提供可复用数据结构 | 目录标准不能证明资源真实可用，仍需更新、校验和本地治理 |
| 社会需求数据标准 | Gravity Project | 把健康相关社会需求、筛查、目标和转介放入可共享的数据标准语境 | SDOH 数据高度敏感，不能被用于惩罚性画像、保险筛选或未经同意的数据共享 |
| 医疗-社区转介模型 | CMS Accountable Health Communities | 展示医疗系统如何筛查、导航并连接住房、食物、交通、水电和人身安全需求 | 模型资料不是个人服务承诺，也不能用筛查替代真实资源供给 |
| 老年服务定位 | ACL Eldercare Locator | 为老年人和照护者寻找本地服务提供入口 | 服务定位工具有地区差异和更新滞后，不能替代实地核验或专业判断 |

## 金融接入、支付与消费者金融保护底座

这一层回答“人能否进入安全、可负担、可理解的金融系统”：Human Infra 不能默认每个人都有银行账户、稳定支付工具、低成本汇款、合理信贷、债务协商能力和消费者保护。工资、福利、租金、水电、医疗账单、跨境汇款、灾害现金援助和在线服务都依赖账户、支付网络、身份核验、费用透明、金融素养和纠纷处理；没有这一层，经济安全会被高费用、账户排除、欺诈和债务压力持续侵蚀。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 金融包容框架 | World Bank Financial Inclusion；Global Findex | 把账户拥有、数字支付、储蓄、借贷和金融服务可得性放入全球发展基础设施 | 全球指标不能替代本地银行规则、个人资格、信用判断或产品推荐 |
| 数字金融服务 | World Bank Digital Financial Services | 把移动支付、数字账户、代理网络和监管能力纳入基础设施设计 | 数字金融不是取消现金和线下服务的理由，也不能扩大排除、欺诈或监控 |
| 支付系统 | World Bank Payment Systems；Federal Reserve Payments Study | 把零售支付、转账、清算和支付工具使用看成日常生活基础设施 | 支付资料不是金融产品建议，也不能证明某个支付方式适合所有人 |
| 银行账户可得性 | FDIC National Survey of Unbanked and Underbanked Households | 观察未开户、服务不足、费用、信任和替代金融服务使用 | 调查资料不是个人开户资格、信用判断或银行服务背书 |
| 金融教育 | FDIC Money Smart | 为消费者金融能力、预算、储蓄、信用和风险理解提供公共教育入口 | 金融教育不能替代收入、监管和公平服务，也不能把金融排除归咎于个人无知 |
| 消费者投诉与信用趋势 | CFPB Consumer Complaint Database；Consumer Credit Trends | 把金融机构投诉、信用市场变化和消费者问题纳入监督与研究入口 | 投诉和趋势数据不是法律意见、个案裁决、信用建议或机构质量保证 |

## 保险、风险转移与理赔连续性底座

这一层回答“风险发生之后，损失是否会把人永久打断”：Human Infra 不能只看账户、支付和福利，也必须看风险池、保险覆盖、理赔、收入替代、申诉、监管和资金保障。疾病、失业、工伤、残障、灾害、银行倒闭和养老金计划中断，都会把个人生活、住房、医疗、照护和工作连续性推入现金流断裂；没有可理解、可负担、可申诉的风险转移机制，恢复就会变成个人硬扛。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 保险消费者入口 | NAIC consumer resources | 把州保险监管、消费者资料、投诉和保险理解接入公共保护体系 | 资料不是保险产品推荐、法律意见、承保承诺或理赔结果保证 |
| 健康保险入口 | USA.gov health insurance | 把健康保险、公共覆盖和获取入口放入医疗可及性与财务保护链路 | 入口资料不是个体资格承诺、报销建议或计划推荐 |
| 收入中断保护 | USA.gov unemployment benefits；workers' compensation | 把失业、工伤和工作相关收入中断纳入运行连续性 | 项目高度依赖州和雇佣关系，不能替代本地资格、申诉和法律审查 |
| 残障与长期收入风险 | Benefits.gov Disability Assistance | 把残障、疾病和功能受限后的收入与服务支持放入导航入口 | 导航不是残障认定、获益承诺、医疗判断或法律代理 |
| 存款与养老金保障 | FDIC deposit insurance；Pension Benefit Guaranty Corporation | 把银行倒闭和养老金计划中断后的基本资金保护纳入家庭韧性 | 保障范围有上限和条件，不是投资建议、收益保证或所有金融损失兜底 |
| 灾害风险融资 | World Bank disaster risk finance；NAIC flood insurance | 把灾害风险、保险缺口、融资安排和洪水保险边界纳入恢复能力 | 风险融资资料不是个体保险建议、灾害赔付承诺、风险地图或救助资格判断 |

## 食物保障、营养支持与水卫生底座

这一层回答“人是否有稳定的能量、营养和卫生条件维持生命活动”：Human Infra 不能把吃饭、饮水、食品安全、儿童营养和卫生设施简化成个人选择。食物价格、供应链、冲突、气候、学校和社区营养、灾害冲击、饮水安全、厕所和污水系统，都会直接影响发育、免疫、学习、工作、恢复和疾病风险。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 全球食物保障 | FAO / IFAD / UNICEF / WFP / WHO State of Food Security and Nutrition in the World；FAOSTAT food security | 把饥饿、粮食不安全、营养不足和食物系统风险放入全球数据语境 | 宏观指标不能替代本地价格、供应链、文化饮食和家庭处境 |
| 实时饥饿风险 | WFP HungerMap LIVE | 展示冲突、气候、经济冲击和灾害如何快速改变食物可得性 | 风险地图是预警与规划入口，不是个体资格或救助承诺 |
| 健康饮食基线 | WHO healthy diet | 为膳食结构、慢病风险和公共营养讨论提供公共健康语言 | 不是个人营养处方，也不能替代医疗营养治疗 |
| 营养不良边界 | WHO malnutrition | 把消瘦、发育迟缓、低体重、微量营养素不足、超重、肥胖和饮食相关非传染性疾病并列为营养系统问题 | 营养不良判断需要专业评估，不能用单一外观、体重或道德标签化 |
| 食品安全 | WHO food safety | 把食源性疾病、污染、供应链和监管纳入人类运行的风险控制层 | 食品安全资料不是具体食品检测报告，也不能替代本地监管和实验室检测 |
| WASH 数据基础设施 | WHO/UNICEF Joint Monitoring Programme | 把饮水、卫生设施和个人卫生纳入可追踪公共基础设施 | JMP 是群体和服务级统计，不是单户水质检测 |
| 饮水安全 | WHO drinking-water | 把安全饮水视为疾病预防、学校、照护和社区运行依赖 | 饮水资料不是本地水质报告，也不能替代检测和监管 |
| 卫生设施 | WHO sanitation | 把厕所、废弃物、污水和卫生设施视为健康与尊严基础设施 | 卫生设施建设必须结合本地工程、维护、文化和安全条件 |

## 能源接入、清洁烹饪与基础公用事业底座

这一层回答“人是否有稳定、安全、可负担的能源维持日常运行”：Human Infra 不能把电力、照明、烹饪、取暖、制冷、通信、医疗设备供电和室内空气当作背景。能源缺口会影响学习时间、食物保存、数字接入、睡眠温度、慢病设备、灾害恢复和家庭安全；污染性燃料和低效住宅也会把生存成本转成健康负担。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 能源发展与服务 | World Bank Energy | 把电力、现代能源服务、可负担性和发展能力连接到公共基础设施 | 能源发展资料不能替代本地电网、价格、停电和家庭处境评估 |
| 电力接入 | IEA access to electricity | 把照明、通信、学习、冷链、医疗设备和数字服务的前置条件放入全球数据语境 | 接入率不能证明电力稳定、可负担、清洁或足以支撑关键设备 |
| 清洁烹饪 | IEA access to clean cooking；WHO household air pollution | 把烹饪燃料、通风、室内污染和健康风险接到家庭运行基础设施 | 清洁烹饪资料不是单户空气检测，也不能忽视燃料价格、文化和供应链 |
| 室内空气质量 | EPA indoor air quality | 把室内污染、通风和健康风险作为住房与能源系统共同结果 | IAQ 资料不是诊断报告，也不能替代本地检测、工程评估或医疗建议 |
| 能源负担 | DOE Low-Income Energy Affordability Data Tool | 观察家庭能源成本、收入、住房和地区差异如何形成能源负担 | 能源负担数据适合规划，不是个体资格、信用或惩罚性评分工具 |
| 住宅保温改造 | DOE Weatherization Assistance Program；Energy Saver weatherization | 把保温、密封、效率和室温稳定视为健康与经济韧性基础设施 | 住宅改造必须结合建筑条件、租住关系、资金和安全标准 |

## 气候风险、早期预警与社区韧性底座

这一层回答“当环境冲击发生时，人和服务是否还能不断线”：Human Infra 不能把气候风险看成遥远背景。热浪、洪水、火灾、风暴、干旱、空气质量恶化、停电、交通中断和供应链扰动，会同时冲击住房、能源、医疗、照护、食物、学校、工作和迁移。真正的基础设施必须包含风险识别、早期预警、冷却和避难入口、脆弱人群服务、灾后恢复和公平资源配置。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 全球风险框架 | IPCC AR6 Synthesis Report | 把气候风险、适应、损失与系统转型放入长期基础设施语境 | IPCC 是评估报告，不是本地风险图、工程方案或个体迁移建议 |
| 早期预警 | WMO Early Warnings for All | 把监测、预报、风险沟通和响应能力看成保护生命与服务连续性的基础设施 | 预警框架不能替代本地应急体系、语言可达性、撤离能力和信任建设 |
| 韧性工具 | U.S. Climate Resilience Toolkit；Climate Mapping for Resilience and Adaptation | 把气候暴露、资产、社区、适应选项和联邦资料连接到规划入口 | 工具适合规划和筛查，不是自动化搬迁、保险、贷款或救助资格判断 |
| 灾害损失与气候数据 | NOAA Billion-Dollar Weather and Climate Disasters；NOAA Climate Data Records | 把极端事件损失、气候记录和长期趋势纳入设施规划、预算和风险沟通 | 历史损失和气候数据不能保证未来事件路径，也不能替代本地 hazard 分析 |
| 健康风险 | CDC Climate and Health；CDC Heat and Health | 把高温、空气、极端天气、媒介传播疾病和健康影响接入公共卫生行动 | 健康资料不是个人医疗建议，也不能替代现场救援和临床判断 |
| 公平与环境负担 | CDC/ATSDR Environmental Justice Index | 把社会脆弱性、环境暴露和健康负担并入气候与灾害韧性决策 | 指数是社区规划信号，不是给个人或社区贴标签、拒绝服务或惩罚性评分的许可 |

## 家庭应急准备、个人韧性与灾前准备底座

这一层回答“警报响起之前，人是否已经有可执行的准备”：Human Infra 不能把灾害准备简化成个人买一个应急包。真正的灾前准备包括家庭通信计划、集合点、物资包、药物和医疗设备、电源与水、宠物和照护对象、残障与慢病需求、重要文件、天气风险认知、备用信息渠道和社区互助。没有这一层，公共预警会停留在“信息已发出”，却无法转化为真实行动能力。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 家庭准备总入口 | Red Cross How to Prepare for Emergencies | 把灾前行动从抽象“提高意识”变成家庭计划、物资、风险识别和本地准备入口 | 总入口不是本地撤离命令、实时风险图、保险建议或救援承诺 |
| 应急物资包 | Red Cross survival kit supplies | 把水、食物、照明、药物、文件、现金、卫生和通信备用品纳入个人运行连续性 | 物资清单不能替代本地 hazard、家庭成员健康需求和可负担性审查 |
| 家庭通信计划 | Red Cross make a plan | 把联系人、集合点、外地联系人、儿童和照护安排纳入行动脚本 | 计划模板不是现场指挥，也不能保证通信网络、交通和避难点可用 |
| 信息和应用入口 | Red Cross emergency app；NOAA Weather-Ready Nation | 把天气风险、通知工具、行动建议和 preparedness culture 接到家庭侧 | 应用和信息入口不能替代官方本地警报、无障碍沟通和线下备用路径 |
| 健康准备 | CDC Prepare Your Health；CDC disaster safety | 把药物、医疗设备、文件、慢病、避难健康、灾害暴露和恢复安全纳入准备 | 健康准备资料不是医疗建议、急救教程或个案临床判断 |

## 公共预警、应急通信与求助入口底座

这一层回答“危机发生时，信息和求助链路是否还能工作”：Human Infra 不能把灾害警报、911、天气广播、移动警报和第一响应者通信当作背景设施。危机中的人能否收到可信信息、听懂行动建议、联系求助入口、在断电或网络拥塞时保留备用渠道，并让响应者持续协同，会直接决定伤害、撤离、医疗、照护和社区恢复的边界。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 综合公共预警 | FEMA Integrated Public Alert and Warning System | 把多渠道公共警报分发视为生命安全和服务连续性的基础设施 | IPAWS 不是个人实时警报保证，也不能替代地方发布权限、语言可达和行动支持 |
| 移动无线警报 | FCC Wireless Emergency Alerts | 展示手机警报如何把紧急信息推送到受影响区域人群 | WEA 接收受设备、运营商、位置和设置影响，不能保证每个人收到或理解 |
| 广播警报 | FCC Emergency Alert System | 把广播、电视和有线系统纳入全国公共警报链路 | EAS 不是现场指挥，也不能替代多语言、无障碍和线下触达 |
| 天气广播 | NOAA Weather Radio | 为天气和危险警报提供持续广播入口 | 天气广播需要设备、覆盖和电源支持，不能替代本地撤离和避难安排 |
| 家庭警报准备 | Ready.gov Alerts and Warnings | 把家庭如何接收、确认和响应警报纳入准备工作 | 准备资料不是具体灾害路线、救援承诺或法律义务解释 |
| 求助入口 | 911.gov；Next Generation 911 | 把紧急呼叫、定位、数据和系统升级放入公共安全基础设施 | 911/NG911 资料不是服务可达保证；具体能力取决于本地系统、网络和调度资源 |
| 响应者通信 | FirstNet Authority | 把第一响应者通信网络视为灾害响应和跨机构协同基础设施 | FirstNet 资料不是个人通信服务承诺，也不能替代本地应急管理和互操作训练 |

## 灾后恢复、个人援助与临时安置底座

这一层回答“灾害之后，人能否重新接回生活”：Human Infra 不能只看预警、撤离和急救。灾后恢复还包括个人援助入口、恢复中心、临时避难、食物、账单和财务缓冲、低息灾害贷款、公共福利导航、文件重建、保险和长期重建。没有恢复路径，灾害会把住房、工作、学校、医疗、照护、身份和现金流同时切断。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 灾害入口与援助导航 | USA.gov disaster；USA.gov disaster assistance | 把灾后申请、机构入口和常见帮助类型聚合成居民可理解的入口 | 入口页不是资格承诺、个案法律意见或所有地方资源实时清单 |
| 财务、食物与账单帮助 | USA.gov disaster financial help；disaster food help；disaster help with bills | 把灾后现金、食品、账单和基本生活缓冲纳入恢复基础设施 | 资料不能替代具体项目资格、申请材料、截止日期和本地服务容量审查 |
| 恢复中心 | FEMA Disaster Recovery Center Locator | 把线下恢复中心视为灾后申请、文件、咨询和服务导航入口 | 恢复中心位置和开放时间会变化，不能保证所有受灾者可达 |
| 灾害贷款与企业恢复 | SBA Disaster Assistance | 把家庭、租户、业主和企业的灾后低息贷款纳入恢复路径 | 贷款不是补助承诺，也不能用债务替代公共救助、公平恢复和风险减缓 |
| 灾害福利与临时避难 | Benefits.gov Disaster Relief；Red Cross shelter locator | 把跨项目福利导航和临时避难入口接入灾后生活连续性 | 福利和避难入口不是实时床位、长期安置、法律保护或安全保证 |

## 免疫屏障、感染监测与公共卫生应急底座

这一层回答“人能否在可传播风险中继续安全生活”：Human Infra 不能把感染风险、疫苗接种、病原监测、医院感染、抗微生物耐药和公共卫生应急看成个人卫生习惯的小问题。群体免疫、实验室网络、法定报告、废水信号、感染防控、国际卫生规则和跨物种风险治理，会决定学校、照护机构、医院、工作场所和城市能否在疫情与长期感染风险中持续运行。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 免疫体系 | WHO vaccines and immunization；Immunization Agenda 2030；CDC vaccines | 把疫苗接种视为生命周期和群体防护基础设施，而不是单次个人选择 | 疫苗资料不是个人医疗建议；接种决策必须结合当地指南、禁忌证和专业评估 |
| 法定传染病监测 | CDC National Notifiable Diseases Surveillance System | 展示病例报告、地方和国家数据流如何支撑早期发现、趋势判断和响应 | 监测数据有报告延迟和定义差异，不能替代临床诊断或个人风险判断 |
| 全球流感监测 | WHO Global Influenza Surveillance and Response System | 用实验室和流行病学网络连接病毒监测、疫苗株选择和公共卫生响应 | GISRS 不是疫情预测保证，也不能覆盖所有呼吸道风险 |
| 国际卫生规则与应急 | WHO International Health Regulations；WHO emergencies overview；CDC emergency preparedness and response；CDC readiness | 把跨境公共卫生风险、通报、准备、响应和恢复放进制度基础设施 | 应急资料不是本地应急预案本身，也不能替代现场指挥和法律责任 |
| 感染防控 | WHO infection prevention and control；CDC National Healthcare Safety Network | 把手卫生、隔离、医疗相关感染和机构报告纳入系统防护 | 感染防控不能被简化成个人洁癖，也不是可复制的临床操作协议 |
| 抗微生物耐药 | WHO antimicrobial resistance；Global Antimicrobial Resistance and Use Surveillance System | 把抗生素使用、耐药监测和治疗失效风险纳入长期公共健康基础设施 | AMR 资料不是用药建议；抗菌药物使用必须由专业人员按指南处理 |
| One Health | WHO One Health | 把人、动物、环境和食物系统之间的病原与耐药风险放到同一框架 | One Health 是治理框架，不是把所有生态风险简化成单一因果链 |
| 废水监测 | CDC National Wastewater Surveillance System | 用社区级废水信号补充病例报告，观察病原传播趋势 | 废水数据是群体信号，不是个人感染检测或诊断 |

## 母婴健康、儿童发展与早期生命基础设施底座

这一层回答“人从哪里开始获得长期运行能力”：Human Infra 不能只从成年人如何优化睡眠、运动、AI 工具和长寿干预开始。孕产健康、新生儿生存、儿童生长、早期照护、语言和认知刺激、安全依恋、家庭压力、社区服务和基础数据系统，会深刻影响一个人后续的学习、免疫、情绪调节、执行能力、慢病风险和社会参与。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 孕产健康 | WHO maternal health；WHO maternal mortality；WHO antenatal care recommendations；Healthy People pregnancy and childbirth | 把孕产安全、产前照护、死亡风险和制度可及性放入人类运行能力的源头层 | 不是个人孕产医疗建议，也不能替代当地临床指南和专业照护 |
| 新生儿健康 | WHO newborn mortality | 把出生后最早期的死亡、照护和卫生系统质量视为基础设施指标 | 新生儿资料不是家庭护理处方，不能替代儿科和产科服务 |
| 儿童健康 | WHO child health | 把儿童疾病预防、照护、营养、发展和环境条件放在生命周期框架内 | 儿童健康资料不能被用于责备家庭或忽视贫困、服务可及性和环境约束 |
| 生长标准 | WHO Child Growth Standards | 提供观察儿童生长和营养状态的国际参考语言 | 生长曲线不是单次诊断工具，必须结合年龄、病史、环境和专业评估 |
| 早期发展框架 | Nurturing Care Framework；World Bank early childhood development | 把健康、营养、安全、响应性照护和早期学习连接成能力形成基础设施 | 早期发展不能被简化成家庭 KPI 或儿童排名系统 |
| 孕产与婴儿监测 | CDC Pregnancy Risk Assessment Monitoring System | 展示孕产前后调查如何连接母婴健康、服务使用和风险因素 | 监测调查是群体数据，不是个体评判、保险筛选或家庭监控工具 |
| 儿童发展观察 | CDC Child Development；Learn the Signs. Act Early. | 为早期发展、里程碑和及时支持提供公共健康入口 | 里程碑资料不是诊断结论，也不能制造对儿童差异的惩罚性标签 |
| 人口与家庭调查 | DHS Program | 用家庭、健康、生育、营养和服务数据观察早期生命条件 | 跨国调查适合群体分析，不能替代本地服务评估或个体资格判断 |

## 托育、早期教育与家庭工作连续性底座

这一层回答“孩子被谁安全照护、家庭能否继续运行”：Human Infra 不能把托育当成家庭私事或单纯消费选择。托育可得性、费用、质量、时间覆盖、照护劳动条件、早期学习、养育支持和服务导航，会同时影响儿童发展、父母就业、学习机会、家庭收入、恢复时间、心理压力和照护者健康。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 托育发展框架 | World Bank childcare | 把托育纳入人力资本、女性就业、儿童发展和经济韧性基础设施 | 全球框架不是本地托育名额、质量或费用保证，也不能替代家庭选择 |
| 照护劳动 | ILO Care Work and Care Jobs；DOL childcare | 把有偿和无偿照护劳动、工作条件、性别差异和劳动力参与放入制度设计 | 照护劳动资料不能用来把责任继续压回家庭或低薪照护者 |
| 托育制度与补助 | ACF Office of Child Care；Child Care and Development Fund | 展示托育补助、质量改进、州级执行和服务可得性的制度入口 | CCDF 资格和覆盖高度依赖地区、收入、年龄和项目规则，不是个体资格承诺 |
| 服务导航 | ChildCare.gov | 为家庭查找托育、理解许可、质量、安全和费用问题提供公共入口 | 导航页面不是机构背书，也不能保证某个托育点安全、可负担或有空位 |
| 供需与成本数据 | National Survey of Early Care and Education；Census child care | 观察托育供给、家庭使用、费用和照护安排如何影响家庭运行 | 调查数据适合政策和研究，不是个体家庭评价或托育机构评分 |
| 养育支持 | CDC Positive Parenting | 把发展阶段、亲子互动、安全和日常养育支持纳入公共健康入口 | 养育建议不是儿童诊断、家庭监控或责备父母的工具 |

## 法律身份、公民登记与权利入口底座

这一层回答“人能否被制度承认为一个可证明的人”：Human Infra 不能把出生登记、法律身份、民事登记、证件和生命统计当成行政背景。没有可证明身份的人，可能无法稳定进入教育、医疗、福利、金融、就业、迁移、继承、投票、数字身份和紧急救助；身份系统本身也可能制造排除、监控和歧视。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 法律身份框架 | UN Legal Identity Agenda | 把从出生到死亡的法律身份和登记系统视为进入权利与服务的基础设施 | 法律身份不是单一证件工程，也不能以登记名义扩大监控和排除 |
| 民事登记与生命统计 | UN Statistics CRVS；WHO CRVS | 把出生、死亡、婚姻、死因和人口统计接到公共健康、规划和权利保障 | CRVS 数据不能替代个案法律程序，也不能被用于惩罚性人群治理 |
| 身份覆盖数据 | World Bank ID4D data | 提供观察身份覆盖缺口、证件可得性和数字身份议题的数据入口 | ID4D 数据适合宏观分析，不是个人资格、信用或身份真实性判定 |
| 出生登记 | UNICEF birth registration | 把儿童是否被登记为进入教育、保护、医疗和法律权利的早期入口 | 出生登记不能被设计成排除无证父母、迁移家庭或弱势儿童的门槛 |

## 司法可及、法律援助与权利救济底座

这一层回答“人被制度承认之后，能否真的维护自己的权利”：Human Infra 不能把法律、纠纷解决、申诉、救济和法律援助当作外部事务。住房、劳动、家庭、债务、医疗、福利、身份、迁移和暴力风险都会变成法律问题；如果人无法理解程序、支付费用、找到帮助、提交材料、参加听证或获得可执行结果，纸面权利就无法转成真实生活能力。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 司法可及全球目标 | UN Sustainable Development Goal 16 | 把和平、正义、有效制度和人人可及的司法纳入发展基础设施 | SDG 目标不是个案法律意见，也不能替代本地司法程序、律师建议或救济路径 |
| 法治测量 | World Justice Project Rule of Law Index | 提供观察开放政府、基本权利、民事司法、刑事司法和约束政府权力的指标语言 | 指数适合宏观比较和研究，不是个人案件胜负预测、国家背书或投资判断 |
| 民事法律需求缺口 | Legal Services Corporation Justice Gap | 把低收入群体的民事法律问题、未满足法律需求和服务缺口转成可见议题 | 美国资料不能直接外推到其他地区，也不是个体服务资格、案件策略或胜诉承诺 |
| 法律援助研究 | Legal Services Corporation Justice Gap Research | 为民事法律援助、服务缺口和数据更新提供持续研究入口 | 研究资料不是法律建议，也不能替代当地法律援助机构的资格审查 |
| 公共法律援助入口 | DOJ Office for Access to Justice | 把联邦层面的司法可及、法律援助协调和公平程序纳入公共服务能力 | 政府页面不是个人案件代理，也不能证明某项服务在当地一定可获得 |
| 在线法律帮助 | ABA Free Legal Answers | 展示低收入用户如何通过线上问答获得志愿律师帮助的服务形态 | 在线问答不是紧急法律服务、完整代理或所有司法辖区通用方案 |

## 公民参与、投票可达与选举基础设施底座

这一层回答“人能否影响制度如何运行”：Human Infra 不能只研究人如何被登记、被服务、被救济，还必须研究人能否参与公共决策和制度反馈。选民登记、投票地点、邮寄表格、投票设备标准、无障碍投票、投票权执行、选举管理知识、投票率数据和选举观察，会决定政治权利是否能转成真实参与能力。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 选民登记与信息入口 | USA.gov voter registration；EAC voters；EAC National Mail Voter Registration Form | 把登记、州别规则、表格和选民信息作为进入公共决策的服务入口 | 资料不是个人资格判断、法律意见、投票结果承诺或实时州级规则替代品 |
| 投票系统与设备标准 | EAC Voluntary Voting System Guidelines；NIST voting | 把投票设备、可用性、安全、测试和标准纳入基础设施视角 | 技术标准不是某一设备认证结论，也不能替代本地选举管理、审计和采购监督 |
| 投票权与无障碍 | DOJ Voting Section；ADA voting；EAC voting accessibility | 把投票权执行、残障可达、语言和场地访问纳入参与基础设施 | 权利资料不是个案法律意见，也不能把无障碍当作投票后才补的可选项 |
| 投票率与参与数据 | International IDEA Voter Turnout Database | 为跨国投票参与、制度比较和长期趋势提供数据入口 | 投票率不能直接解释政治合法性、个体意愿或单次选举公正性 |
| 选举知识与观察 | ACE Electoral Knowledge Network；OSCE/ODIHR elections | 把选举管理、观察、制度设计和最佳实践作为公共能力资料 | 观察和知识资料不是党派背书、政权合法性判定或竞选策略工具 |

## 迁移、流离失所与人道服务连续性底座

这一层回答“当人离开原有居住地、身份系统和服务网络后，基础设施是否还能接住他”：Human Infra 不能默认每个人都在稳定国家、城市、地址和家庭网络里生活。战争、灾害、气候冲击、迫害、贫困和跨境迁移会让身份、住房、医疗、教育、照护、保护、信息、现金/物资和数据治理同时断裂；真正的基础设施必须考虑移动中的人、无证件人群、难民、寻求庇护者、无国籍者和内部流离失所者。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 全球迁移框架 | UN Global Compact for Migration；IOM World Migration Report | 把迁移放入权利、发展、劳动力、家庭、汇款和公共服务语境，而不是只看边境控制 | 全球框架和报告不是个人移民法律意见，也不能替代本地程序、庇护规则或资格判断 |
| 难民与行动数据 | UNHCR Operational Data Portal | 为难民、寻求庇护者、无国籍者和相关人群处境提供公开数据与行动响应入口 | 数据入口不是个案身份判定、安置承诺、遣返依据或自动化风险评分 |
| 内部流离失所 | IDMC Global Report on Internal Displacement | 把境内冲突、灾害和发展项目造成的离散纳入住房、身份、服务和保护缺口 | IDP 数据适合政策和规划，不能替代个案保护评估或本地登记程序 |
| 健康与迁移 | WHO Health and Migration Programme | 把迁移者、难民和流离失所者的健康权、服务可及性和系统包容性接入卫生体系 | 不是个人医疗建议，也不能用迁移身份降低服务质量、延迟救治或扩大监控 |
| 人道数据与态势信息 | OCHA Humanitarian Data Exchange；ReliefWeb | 让危机中的需求、位置、组织、数据集和报告成为协调入口 | 人道数据可能滞后、敏感或不完整，不能替代现场评估、保护审查和受影响人群参与 |
| 教育连续性 | INEE Minimum Standards | 把危机中的教育、保护、心理社会支持和学习连续性纳入标准 | 教育应急标准不是低质教育的借口，也不能忽视语言、身份、安全和长期认证问题 |
| 人道协调与庇护 | Inter-Agency Standing Committee；Global Shelter Cluster | 把跨机构协调、庇护、安置和部门责任接入服务连续性 | 协调框架不是现场指挥替代品，也不能绕开同意、隐私、问责和本地治理 |

## 数字接入、信息可达与公共服务基础设施底座

这一层回答“人能否进入现代信息和公共服务系统”：Human Infra 不能把 AI 工具、远程医疗、在线教育、福利申请、求职、政务服务和知识获取默认当作人人可用。网络连接、设备、可负担性、数字身份、可用性、语言、信息素养、图书馆和公共服务设计，会决定一个人是否真正能把技术变成能力。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 全球数字连接 | ITU ICT statistics | 把互联网、移动网络、设备和数字使用差异放入全球统计语境 | 宏观连接率不能证明个人可负担、稳定或安全可用 |
| 数字发展 | World Bank Digital Development | 把数字基础设施、服务、技能、信任和经济发展连接到公共政策 | 数字发展不是把所有服务搬上线，也不能替代线下可及性 |
| 家庭互联网与设备 | NTIA Digital Nation；U.S. Census computer and internet use | 观察家庭层面的设备、联网、使用场景和数字鸿沟 | 调查数据不能替代本地可用性、价格、设备质量和语言支持审查 |
| 数字身份 | NIST Identity and Access Management；NIST SP 800-63-4；Login.gov | 把认证、身份验证、账号恢复和反欺诈放入公共服务基础设施 | 数字身份不能变成排除无证件、低数字能力或高风险人群的门槛 |
| 公共数字服务体验 | Digital.gov；U.S. Web Design System | 把政府网站和服务做成可用、可访问、一致、可维护的公共界面 | 设计系统不是形式合规；必须验证真实用户能完成任务 |
| 信息素养 | UNESCO Media and Information Literacy | 把查找、理解、评估和使用信息视为现代生活能力基础 | 信息素养不能被用来把平台污染和虚假信息责任全部转嫁给个人 |
| 公共图书馆数据 | IMLS Public Libraries Survey；IMLS Search & Compare | 把图书馆视为互联网、学习、信息咨询和社区服务入口 | 图书馆数据不能替代本地服务质量、开放时间、语言和无障碍审查 |

## 个人数字安全、账号恢复与身份盗用防护底座

这一层回答“人能否保有自己的数字入口”：Human Infra 不能只看网络、设备和数字身份是否存在，还必须看普通人能否识别钓鱼、保护账号、处理账号接管、恢复身份、举报诈骗、修复信用和重新进入服务。账号失控、身份盗用、短信钓鱼、虚假客服、支付诈骗和恢复流程失败，会让金融、医疗、福利、教育、住房和工作服务同时断线。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 诈骗与钓鱼识别 | FTC scams；FTC phishing guidance | 把诈骗、钓鱼、社工和信息诱导视为服务入口风险，而不是个人“太笨” | 资料不是个案调查、法律意见或平台安全背书，也不能把责任全部转嫁给受害者 |
| 身份盗用恢复 | IdentityTheft.gov | 为身份盗用后的报告、恢复计划和信用修复提供官方入口 | 恢复入口不能保证损失追回、信用修复成功或所有机构立即接受 |
| 诈骗举报 | ReportFraud.ftc.gov；FBI IC3 | 把消费者诈骗和网络犯罪报告接入官方记录与响应渠道 | 举报入口不是紧急响应、赔付承诺、法律代理或执法结果保证 |
| 数字身份与认证 | NIST SP 800-63-4 | 为身份验证、认证器、账号生命周期和数字身份风险提供标准语境 | 身份标准不是单个系统合规证明，也不能用高门槛认证排除弱势人群 |
| 公共账号恢复 | Login.gov help；Login.gov policy | 把政府账号登录、帮助和身份服务政策放入公共服务入口连续性 | Login.gov 资料只适用于其服务范围，不能替代所有机构账号恢复路径 |

## 语言可达、清晰沟通与健康素养底座

这一层回答“服务存在之后，人能不能理解并使用”：Human Infra 不能把表单、说明、告知书、医疗指引、福利通知、法律材料和危机信息默认当成人人看得懂。语言可达、清晰写作、翻译解释、健康素养、认知可访问性和用户测试，会决定制度、医疗和数字服务能否真正被人使用。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 清晰语言 | PlainLanguage.gov；Digital.gov plain language | 把可理解、可行动、少术语和任务导向写作纳入公共服务基础设施 | 清晰语言不是营销文案，也不能替代法律、临床或安全准确性 |
| 有限英语能力服务 | LEP.gov | 把翻译、口译、语言援助和反歧视纳入公共服务入口 | 语言服务不是可选增值项，也不能用机器翻译替代高风险人工解释 |
| 文化与语言适切 | National CLAS Standards | 把文化、语言、组织治理和服务质量接入医疗与公共健康服务 | CLAS 不能停留在声明，必须落到人员、流程、质量和问责 |
| 健康素养 | CDC health literacy；CDC Clear Communication Index | 把健康信息理解、风险沟通、材料测试和可行动性纳入服务设计 | 健康素养不能被用来责备患者；系统必须降低理解成本 |
| 认知可访问性 | W3C cognitive accessibility | 把记忆、注意力、语言、执行功能和认知负担纳入数字服务设计 | 认知可访问性不能被自动扫描完全证明，必须做真实任务验证 |

## 交通可达、公共交通与日常移动底座

这一层回答“人能否到达需要到达的地方”：Human Infra 不能把上学、上班、就医、拿药、办福利、买食物、照护家人、参与社区和灾害撤离默认当成有路可走、有车可坐、费用可承受。交通系统会把空间距离转成时间成本、金钱成本、安全风险、残障阻碍和服务排除；没有移动能力，很多权利和服务只是纸面存在。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 全球交通发展 | World Bank Transport | 把交通连接、可达性、经济机会和服务可达性放入基础设施发展语境 | 交通发展资料不能替代本地线路、票价、道路安全和无障碍审查 |
| 公共交通数据 | FTA National Transit Database | 用运营、资产、服务和安全数据观察公共交通系统能力 | NTD 是系统级数据，不等于个人通勤可达或服务质量体验 |
| 家庭出行调查 | BTS National Household Travel Survey | 观察家庭出行方式、目的、时间、距离和群体差异 | NHTS 是调查数据，不能替代本地实时服务、费用和安全评估 |
| 交通公平地图 | USDOT Equitable Transportation Community Explorer RFI | 把交通负担、可达性和社区不利条件放到空间分析中 | 交通公平工具和地图是规划线索，不是个体资格、房价判断或自动资源剥夺工具 |
| 无障碍交通 | FTA ADA guidance；FTA ADA FAQs | 把残障者进入公共交通和辅助交通服务视为基础设施责任 | ADA 资料不是法律意见；服务设计必须结合当地法规、运营能力和个人需求 |

## 医疗可及性、初级卫生保健与基本服务底座

这一层回答“人生病或需要预防服务时，能否进入可信医疗系统”：Human Infra 不能把医疗服务默认当成随时可达。医保覆盖、费用负担、距离、等待时间、语言、医护人员分布、基本药物供应、初级保健连续性和质量差异，都会决定一个人能否及时诊断、治疗、转诊、康复和维持慢病管理。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 全民健康覆盖 | WHO Universal Health Coverage；World Bank UHC | 把服务覆盖和财务保护视为人能否进入医疗系统的制度底座 | UHC 资料不是本地保险资格、费用报销或具体服务承诺 |
| 初级卫生保健 | WHO Primary Health Care | 把预防、常见病处理、慢病连续管理、转诊和社区入口放到第一接触层 | PHC 不是替代急诊、专科或本地临床指南的万能入口 |
| 基本药物 | WHO Essential Medicines Lists | 把关键药物的选择、供应和可负担性纳入基础设施能力 | 基本药物清单不是个人用药建议，也不证明当地可获得或适合个人 |
| 医护人员供给 | WHO Health Workforce | 把受训人员、分布、保留和工作条件视为医疗服务能力的前提 | workforce 资料不能用于压榨医护或用人员短缺合理化低质量服务 |
| 医疗可及与保险覆盖 | CDC access to health care；CDC health insurance | 用官方统计观察可及性、保险覆盖和人群差异 | 统计资料不是个人资格判断、保险建议或医疗法律意见 |
| 医疗质量与差异 | AHRQ Data Tools / NHQDR | 把医疗质量、可及性和差异放入可查询指标体系 | 质量数据适合规划和审查，不是单个机构或个体治疗结果保证 |

## 远程医疗、数字照护与居家监测底座

这一层回答“医疗和照护能否离开固定诊室仍然连续”：Human Infra 不能把远程医疗只看成视频问诊工具。远程问诊、远程患者监测、居家设备、支付覆盖、宽带与设备、隐私安全、语言可达、照护者参与、临床升级路径和线下替代，会决定慢病随访、农村医疗、行动受限者照护、术后恢复和长期服务能否不断线。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 远程医疗入口 | Telehealth.HHS.gov | 把远程问诊、服务准备、隐私和患者/提供方信息放入公共入口 | 远程医疗资料不是医疗建议，也不保证服务、保险或地区可用性 |
| 远程患者监测 | HHS telehealth and remote patient monitoring | 把居家设备、数据回传和慢病随访纳入照护连续性基础设施 | RPM 不是自我诊断、自动治疗或替代急诊；必须有临床责任和升级路径 |
| 农村与服务可及 | HRSA telehealth | 把远程医疗放到医疗短缺、农村可及和卫生服务支持语境 | telehealth 不能掩盖线下服务缺口，也不能替代本地急诊和专科能力 |
| 支付与覆盖 | CMS telehealth；Medicare telehealth | 展示远程医疗能否进入真实使用，取决于覆盖规则、服务类型和支付政策 | 覆盖规则会变化且高度依赖计划、地区和服务，不能作为个体报销承诺 |
| 数字健康监管 | FDA Digital Health Center of Excellence | 把移动医疗、软件、设备和数字健康工具放入监管和风险框架 | 数字健康页面不是某个应用或设备有效性背书，也不能绕开医疗器械监管 |

## 药品可及、用药安全与供应连续性底座

这一层回答“医疗建议能否变成可持续治疗”：Human Infra 不能把药品当作处方纸上的自然结果。药品选择、供应、价格、医保覆盖、短缺、标签说明、药物相互作用、患者理解、药房渠道和用药错误，会决定慢病管理、急性治疗、心理健康、感染控制和照护连续性能否真正运行。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 基本药物选择 | WHO Essential Medicines Lists | 把关键药物的优先级、可及性和卫生系统采购能力纳入基础设施语言 | EML 不是个人用药建议，也不证明当地库存、报销或个体适用性 |
| 用药安全 | WHO Medication Without Harm；CDC Medication Safety Program | 把处方、调配、患者理解、相互作用、错误和伤害减少纳入系统安全 | 用药安全资料不是自我调整药物或替代药师/医生判断的许可 |
| 药品短缺 | FDA Drug Shortages | 把药品供应中断、替代方案压力和治疗连续性风险纳入基础设施观察 | 短缺列表不是个人替代用药建议，具体处理必须由临床和药学专业人员判断 |
| 药品标识与标签 | FDA National Drug Code Directory；DailyMed | 为药品识别、标签、说明书和成分信息提供公开资料入口 | 标签资料不能替代临床解释，也不能证明网络售药或来源可靠 |
| 患者药品信息 | MedlinePlus Medicines | 为患者理解药品用途、副作用、注意事项和沟通问题提供公共入口 | 患者资料不是诊断、处方或停药建议 |
| 支付与覆盖 | Medicare prescription drug coverage | 展示药品覆盖、计划、费用和可负担性如何影响治疗连续性 | Medicare 资料是美国制度入口，不是所有地区或个体的保险建议 |

## 心理健康、成瘾与危机照护底座

这一层回答“人在心理痛苦、成瘾风险或危机中能否被及时接住”：Human Infra 不能把抑郁、焦虑、精神障碍、物质使用障碍、过量风险和自杀危机简化成个人意志问题。可及的社区服务、治疗入口、危机热线、过量预防、连续照护、家庭与同伴支持、隐私保护和反污名机制，会决定一个人能否安全恢复并继续生活。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 全球心理健康框架 | WHO World Mental Health Report；WHO Mental Health Atlas | 把心理健康服务、政策、资源和系统能力放入公共基础设施语境 | 全球报告不能替代个体诊断、治疗建议或本地服务资格判断 |
| 基层精神卫生能力 | WHO mhGAP | 展示非专科场景如何识别和管理优先精神、神经和物质使用问题 | mhGAP 是卫生系统工具，不是普通人自我诊断或自行治疗指南 |
| 服务入口 | FindTreatment.gov；988 Suicide & Crisis Lifeline | 把治疗定位、危机支持和服务导航视为基础设施入口 | 服务入口不是医疗建议、服务质量保证或所有地区可得性承诺 |
| 疾病负担统计 | NIMH mental illness statistics | 为精神疾病流行程度和人群差异提供公开统计语境 | 统计资料不能给个人贴诊断标签，也不能用于保险、招聘或惩罚性筛选 |
| 成瘾与过量预防 | CDC overdose prevention | 把物质使用、过量风险、伤害减少和监测放入公共健康基础设施 | 过量预防资料不是个体治疗处方，也不能替代专业干预和紧急处置 |

## 人身安全、伤害预防与应急响应基础设施底座

这一层回答“人能否免于可预防伤害，并在危机后得到及时支持”：Human Infra 不能只讨论更长寿、更高效、更聪明，也必须讨论暴力、伤害、儿童逆境、自杀风险、急救系统、灾害冲击和恢复路径。一个人能否持续学习、工作、照护和创造，首先取决于生活环境是否足够安全、危机是否能被发现、救援是否能抵达、复原是否有支持。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 伤害与暴力负担 | WHO injuries and violence；CDC Injury Center | 把伤害和暴力视为公共健康与运行能力损失，而不是偶发个人不幸 | 伤害资料不是个案责任判定，也不能替代法律、临床或现场处置 |
| 伤害数据系统 | CDC WISQARS | 为非致死伤害、死亡、原因、年龄和地区差异提供可查询数据入口 | 数据系统适合公共健康规划，不是个人风险评分或保险筛选工具 |
| 暴力预防 | WHO violence；WHO violence against women；CDC Violence Prevention | 把暴力放入可预防的社会、关系、制度和环境风险框架 | 暴力预防资料不能替代受害者支持、司法程序或本地服务 |
| 儿童逆境 | CDC Adverse Childhood Experiences | 把童年创伤、家庭与社区风险连接到长期健康和执行能力 | ACEs 不是给儿童或家庭贴标签的工具，也不能忽视贫困和服务缺口 |
| 自杀预防与危机支持 | CDC Suicide Prevention；988 Suicide & Crisis Lifeline | 把危机识别、支持入口和预防框架纳入生命安全基础设施 | 资料索引不是危机个案处理指南；具体危机必须接入当地专业和紧急支持 |
| 急救与急诊系统 | WHO Emergency Care | 把急救、分诊、转运和急诊能力视为伤害与急症后的关键基础设施 | 急救系统资料不是急救操作教程，也不能替代专业训练和当地流程 |
| 灾害健康准备 | CDC Natural Disasters and Severe Weather | 把极端天气、灾害暴露、避难、恢复和健康风险接到社区运行能力 | 灾害资料不是现场应急指挥，也不能替代本地预案和权责链 |

## 建成环境、交通与环境暴露底座

这一层回答“人运行在什么物理世界里”：Human Infra 不能把住房、街道、通勤、空气污染、热暴露和交通伤害看成背景变量。睡眠是否安全、运动是否可达、社交是否便利、恢复是否可能、老年人是否能出门、儿童是否能上学，都会被建成环境和城市系统塑造。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 住房健康 | WHO Housing and health guidelines | 把拥挤、寒冷、过热、安全、无障碍和室内健康风险纳入人的长期运行条件 | 住房指南不是建筑规范全文，也不能替代本地法规、工程评估或个案检查 |
| 城市健康 | WHO Urban health | 把城市规划、服务可达、环境暴露和健康不平等连接起来 | 城市健康不能被简化成“多建公园”或单一指标排名 |
| 建成环境评估 | CDC Built Environment Assessment Tool | 为街道、土地使用、交通、食品零售和公共空间提供观察工具 | 评估工具适合社区规划和研究，不是个人健康诊断或房产价值判断 |
| 主动交通与社区设计 | CDC Active Communities Tool；CDC community design strategies | 把步行、骑行、公共空间、连接性和日常身体活动放入基础设施设计 | 主动交通策略必须同时考虑安全、无障碍、天气、治安和本地可达性 |
| 空气质量 | WHO Global Air Quality Guidelines；AirNow | 把颗粒物、臭氧等空气暴露纳入健康、恢复和户外活动决策 | 空气质量数据是风险沟通和公共卫生线索，不是个人医疗诊断 |
| 热风险 | CDC/ATSDR Heat and Health Index；CDC Tracking heat events | 把高温、社会脆弱性和健康风险接到地理与公共卫生规划 | 热风险地图不能替代现场救援、个体风险评估或雇主防暑责任 |
| 道路安全 | WHO Global status report on road safety | 把交通伤害视为系统设计、速度管理、道路用户保护和政策问题 | 道路安全资料不能替代本地交通工程审查或事故责任判定 |

## 学习、技能形成与能力成长底座

这一层回答“人如何从不会到会、从会到熟练、从熟练到能迁移”：Human Infra 不能只讨论健康状态和工具供给，也必须讨论学习机制、反馈质量、练习设计、教育证据、技能地图、终身学习和能力投资。复杂任务的执行能力不是一次性天赋，而是长期环境、训练、反馈和机会结构共同塑造的结果。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 学习科学 | National Academies How People Learn II | 把学习者、知识、文化、动机、情境和迁移放进同一套学习系统理解 | 学习科学不是速成技巧，也不能替代具体教学设计和反馈 |
| 教育证据 | IES What Works Clearinghouse | 为教育干预、课程、教学策略和证据等级提供可查证入口 | 教育证据依赖人群、场景和实施质量，不能机械套用到所有学习任务 |
| 教育统计 | UNESCO Institute for Statistics | 提供全球教育数据和指标语境，帮助观察能力基础设施的覆盖与差异 | 宏观统计不能替代本地学校、家庭和学习者情境 |
| 终身学习 | UNESCO Institute for Lifelong Learning | 把成人学习、终身学习和学习型社会放入能力持续更新框架 | 终身学习不能被用作把再培训责任完全转嫁给个人的口号 |
| 技能地图 | O*NET | 用职业、任务、技能、能力和工作活动描述真实劳动能力结构 | 技能 taxonomy 不是自动招聘、裁员或评价个人价值的工具 |
| 人力资本 | World Bank Human Capital Project | 把健康、教育和儿童成长连接成国家和社会层面的长期能力投资 | 人力资本是宏观政策语言，不是把人的价值还原为经济产出的许可 |

## 就业服务、劳动力发展与职业转换底座

这一层回答“人学会之后能否进入、保有和转换工作”：Human Infra 不能把就业简化成个人努力、简历技巧或单次招聘。职业信息、公共就业服务、培训资金、学徒制、岗位匹配、转岗支持、失业再就业、就业无障碍和劳动力市场制度，会决定学习成果能否变成收入、安全感、社会连接和长期发展。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 就业与发展框架 | World Bank Jobs and Development；ILO Employment Promotion | 把就业质量、生产性工作、制度支持和包容性增长纳入基础设施视角 | 全球框架不是个人求职建议，也不能把失业归因于个人能力不足 |
| 公共就业服务 | DOL Employment and Training Administration；American Job Centers | 把职业服务、培训、再就业和区域劳动力系统看成公共服务入口 | 公共服务页面不是岗位承诺、服务资格承诺或机构质量背书 |
| 劳动力制度 | Workforce Innovation and Opportunity Act | 把青年、成人、失业者、弱势群体和地方 workforce board 连接到制度路径 | WIOA 规则地区差异大，不能替代本地资格、资金和项目审查 |
| 学徒制 | Apprenticeship.gov | 把带薪学习、雇主参与、技能标准和职业通道纳入可执行路径 | 学徒信息不是岗位保证，也不能跳过劳动权益、工资和安全审查 |
| 职业信息 | O*NET Center；O*NET Online；My Next Move | 用任务、技能、知识、能力和兴趣连接职业导航、训练和转岗 | 职业 taxonomy 不是自动招聘、裁员、人格评价或收入承诺工具 |
| 就业无障碍 | Job Accommodation Network | 把合理便利、工作调整和残障就业支持纳入工作连续性基础设施 | JAN 资料不是法律意见、医疗判断或雇主合规证明 |

## 人口级健康数据底座

这一层支撑 Human Infra 的证据基础：如果要理解人类长期运行状态，不能只看单个网红式个案，也不能只看单次体检。All of Us、UK Biobank、NHANES、Framingham 和 GTEx 分别代表多来源长期健康数据、生物样本库、公共健康调查、长期队列和分子表型资源。它们共同提示：Human Infra 需要数据治理、代表性、同意、访问控制、隐私保护和跨层证据解释。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 参与者级纵向研究 | NIH All of Us Research Program；All of Us Researcher Workbench | 把电子健康记录、调查、基因组和其他参与者数据组织成研究基础设施，强调多样性和长期开放研究 | 研究数据不能替代个人诊断；使用时必须尊重同意、访问控制、隐私和数据使用规则 |
| 大型生物样本库 | UK Biobank | 连接基因、影像、生物标志物、生活方式和长期健康结局，适合研究复杂疾病风险和健康轨迹 | 队列有地域、年龄和参与者选择偏倚，不能直接代表全人类 |
| 公共营养与体检调查 | CDC NHANES | 用调查、体检和实验室数据支持美国人口健康和营养状态监测 | 是人口监测和研究资源，不是个人健康评分或诊断工具 |
| 长期心血管队列 | Framingham Heart Study | 展示长期随访如何把风险因素、生活方式和疾病结局连接成证据链 | 经典队列有历史和人口结构限制，外推到不同人群时必须谨慎 |
| 组织特异性分子表型 | GTEx | 把不同人体组织中的基因表达和遗传变异连接起来，为机制解释提供分子层数据 | 分子关联不是干预建议，不能直接推出药物、补剂或个人方案 |

## 学习型健康系统与真实世界证据底座

这一层回答“数据如何变成可信证据和可监管产品”：Human Infra 不能只堆积数据源，还必须描述临床试验登记、真实世界证据、分布式研究网络、通用数据模型、互操作标准和数字健康评估框架。没有这一层，个体追踪、可穿戴设备、AI 工具和长寿干预很容易停留在宣传叙事，无法进入可复核的证据生成链。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 临床研究登记 | ClinicalTrials.gov | 把试验设计、招募、干预、终点、状态和结果披露纳入公开登记体系 | 登记不等于有效或安全；必须看研究设计、状态、结果和适用人群 |
| 真实世界证据监管 | FDA Real-World Evidence Program | 把电子健康记录、保险理赔、登记系统和其他真实世界数据纳入监管证据讨论 | 真实世界数据不自动等于因果证据，偏倚、缺失、混杂和数据质量必须被审查 |
| 分布式研究网络 | PCORnet | 展示多机构健康数据如何在治理、标准化和隐私边界下支持患者中心研究 | 网络能力不能替代具体研究方案、IRB、数据使用协议和统计审查 |
| 通用数据模型 | OHDSI / OMOP Common Data Model | 为观察性健康数据提供标准化结构，便于跨机构分析和方法复用 | 标准化不消除原始数据偏差，也不保证不同机构语义完全一致 |
| 医疗数据互操作 | HL7 FHIR | 为临床数据交换、API 和应用集成提供事实标准之一 | 互操作标准不是隐私、同意或安全策略；具体实现仍需权限和审计 |
| 数字健康评估 | FDA Digital Health Center of Excellence；NICE Evidence Standards Framework；WHO digital health guideline | 把软件、数字疗法、AI 工具和移动健康应用放进证据、风险和健康系统语境 | 数字健康产品必须按风险、用途和地区监管要求评估，不能用“工具”身份绕开验证 |

## 患者健康记录访问、互操作与数据可携带底座

这一层回答“人是否能拿到并携带自己的健康数据”：Human Infra 不能只把健康数据看成研究者、医院、保险方或应用开发者的资产。患者本人、授权照护者和跨机构照护团队能否获得、核对、纠错、下载、授权、撤回和携带健康记录、理赔数据、药物清单、检查结果、转诊资料和照护计划，会决定转诊、远程医疗、慢病管理、紧急救治、照护交接和研究参与是否真的连续。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 个人健康记录获取 | ONC Get It, Check It, Use It | 把获取、核对和使用健康记录放到患者和照护者侧，而不是只看机构数据交换 | 个人健康记录资料不是法律意见，也不保证所有机构、格式和门户都完整可用 |
| 核心数据类别 | ONC United States Core Data for Interoperability | 用 USCDI 描述跨系统共享的核心健康数据类别 | 核心数据集不是完整病历，也不保证语义一致、数据质量或即时可得 |
| 全国交换框架 | ONC TEFCA | 把跨网络健康信息交换放入可信交换、共同协议和全国互操作语境 | TEFCA 不是个人即时取数保证，也不能绕开隐私、授权和本地实施差异 |
| 保险与患者访问 API | CMS Interoperability and Patient Access Final Rule | 把患者访问、支付方数据和 API 能力放进覆盖与保险数据连续性 | 规则资料不是个体保险权益承诺，也不保证第三方应用安全或适合使用 |
| Medicare 数据携带 | CMS Blue Button API | 展示 Medicare 受益人理赔数据如何通过标准 API 授权给可信应用 | Blue Button 是特定数据和人群的 API，不代表完整临床记录或所有保险数据 |
| 授权应用接入 | HL7 FHIR；SMART App Launch | 为健康应用在授权、安全和标准数据接口上接入临床系统提供基础标准 | 标准接口不是应用有效性、隐私实践或临床安全背书 |

## 信任、隐私与数据治理底座

这一层回答“Human Infra 怎样避免变成监控和滥用系统”：健康数据、基因数据、神经数据、行为数据和工作状态数据都可能触及人格、身份、就业、保险、医疗和社会机会。Human Infra 不能只追求更多采集、更强预测和更细评分，还必须把同意、撤回、最小必要、用途限制、访问控制、网络安全、受试者保护和数据共享治理写进基础设施层。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 健康隐私基线 | HHS HIPAA Privacy Rule；ONC privacy and security resources | 为受保护健康信息、覆盖实体、业务伙伴和健康信息使用披露提供美国制度语境 | HIPAA 不是所有健康数据的通用保护伞；仓库内容也不是法律意见或合规证明 |
| 受试者保护 | HHS Common Rule | 把知情同意、IRB、风险收益和受试者保护放入研究治理框架 | Common Rule 适用范围有边界，不能替代具体 IRB、伦理审查或当地法规 |
| 隐私风险管理 | NIST Privacy Framework | 提供识别、治理、控制、沟通和保护隐私风险的工程语言 | 框架不是合规证书，也不自动证明系统尊重主体权利 |
| 网络安全风险管理 | NIST Cybersecurity Framework | 把识别、保护、检测、响应和恢复纳入健康与数据系统的安全治理 | 安全框架不是具体控制实现；需要威胁建模、权限设计、日志和响应演练 |
| 基因数据共享 | NIH Genomic Data Sharing Policy；GA4GH Framework | 为基因组和健康相关数据的责任共享、访问控制、同意和跨机构研究提供治理语汇 | 基因数据高度可识别，不能把“开放科学”理解成无边界公开个人数据 |
| 健康数据访问边界 | ONC Information Blocking | 把患者访问、互操作、信息共享和例外条件放入健康信息政策语境 | 数据可访问不等于可以任意二次利用；共享必须与隐私、安全和授权并行 |

## 功能、生活质量与患者报告结局底座

这一层回答“系统到底有没有让人更好”：Human Infra 不能只用寿命、实验室指标、生产率或模型分数评价人类运行状态。功能能力、症状负担、生活质量、疼痛、疲劳、社会参与、日常活动和患者自报结果，都是判断基础设施是否真正服务于人的关键结局。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 患者报告结局 | PROMIS | 提供一套跨疾病、跨领域的患者报告结局测量系统，覆盖疼痛、疲劳、情绪、社会功能等 | 患者自报不是诊断本身，必须结合研究设计、临床语境和量表适用性解释 |
| 功能与残障框架 | WHO International Classification of Functioning, Disability and Health | 把健康从疾病诊断扩展到身体功能、活动、参与和环境因素 | ICF 是分类和框架，不是单一评分，也不能替代个体临床评估 |
| 健康效用与生活质量 | EQ-5D | 为移动能力、自我照护、日常活动、疼痛/不适、焦虑/抑郁等维度提供标准化健康状态描述 | 健康效用工具适合群体和经济评价，不能简化为个人价值排序 |
| 价值导向结局 | ICHOM patient-centered outcome measures | 让不同疾病和照护路径围绕患者真正关心的结果定义标准结局集 | 标准集需要按病种和场景使用，不能机械套到所有 Human Infra 应用 |
| 治疗毒性自报 | NCI PRO-CTCAE | 把患者对治疗相关不良事件的体验纳入症状和毒性评估 | 适用于肿瘤治疗相关语境，不能泛化为所有健康干预风险量表 |
| 生活质量框架 | WHOQOL；CDC Healthy Days；RAND SF-36 | 为主观健康、健康相关生活质量和日常受限天数提供可复用测量语言 | 生活质量指标不应被组织拿来排名、惩罚或压缩个体复杂处境 |

## 康复、辅助技术与可访问性底座

这一层回答“当人已经受伤、衰退、残障或处在慢病状态时，基础设施如何让他继续生活”：Human Infra 不能只服务于高表现个体，也必须覆盖康复服务、辅助产品、无障碍数字系统、沟通权利和合理便利。真正的人类基础设施不是筛掉能力受限者，而是把功能连续性、参与权和可达性放进系统设计。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 康复服务 | WHO rehabilitation；WHO Rehabilitation 2030 | 把康复视为卫生系统的一部分，服务损伤、疾病、老化和功能受限后的能力恢复与参与 | 康复不是单一训练清单，也不能替代个体临床评估和专业服务 |
| 辅助技术体系 | WHO/UNICEF Global report on assistive technology | 把轮椅、助听、视觉、沟通、认知和日常生活辅助产品视为基础设施 | 辅助产品需要适配、训练、维护和可负担性，不能只当作硬件采购 |
| 优先辅助产品 | WHO Priority Assistive Products List | 为基础辅助产品的可及性、采购和政策优先级提供参考 | 优先清单不是个人处方，也不能替代当地需求评估 |
| 数字可访问性 | W3C Web Content Accessibility Guidelines 2.2；W3C WAI WCAG overview | 把可感知、可操作、可理解和稳健性转成数字系统设计要求 | WCAG 不是只给残障用户的附加项，也不能用自动化扫描替代人工可用性验证 |
| 公共 ICT 可访问性 | U.S. Access Board Section 508 ICT standards | 为公共信息通信技术提供可访问性要求和采购/合规语境 | Section 508 是美国公共部门语境，不能直接替代其他司法辖区要求 |
| 有效沟通 | ADA.gov effective communication | 把辅助服务、辅助设备和有效沟通放进公共服务和商业场所责任边界 | 有效沟通不是形式合规；必须看具体人的沟通需求和服务场景 |

## 照护、家庭照护者与长期服务底座

这一层回答“当人不能完全靠自己维持运行时，谁在支撑他”：Human Infra 不能把照护视为家庭内部私事，也不能把慢病、残障、老化、术后恢复和临终阶段都交给个人硬扛。长期服务、居家社区支持、照护协调、家庭照护者支持、喘息服务和质量透明度，都是人能否继续生活、工作、学习和保有尊严的基础设施。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 家庭照护者战略 | National Strategy to Support Family Caregivers | 把家庭照护者支持从私人负担提升到国家级政策对象 | 战略文件不是福利资格承诺，也不能替代地方服务申请规则 |
| 照护者公共健康 | CDC Caregiving | 把照护者压力、健康影响、支持资源和公共健康语境接入 Human Infra | 照护者资料不是个体心理诊断，也不能把照护责任完全转嫁给家庭 |
| 照护负担证据 | National Academies Families Caring for an Aging America | 系统描述家庭照护在老龄社会中的劳动、风险、经济和健康影响 | 研究综述不是个人照护方案，也不能替代专业评估 |
| 居家社区服务 | Medicaid Home & Community-Based Services | 展示长期服务如何从机构照护转向居家和社区支持 | HCBS 资格、覆盖和等待名单高度依赖地区与项目，不能泛化承诺 |
| 居家医疗与临终照护 | Medicare home health services；Medicare hospice care | 把居家医疗、康复、护理和临终支持纳入服务可及性讨论 | Medicare 覆盖说明不是医疗建议，也不是所有人都符合资格 |
| 照护协调 | AHRQ Care Coordination | 把跨服务、跨专业、跨场景的信息交接和责任边界变成可设计对象 | 照护协调不能只靠提醒和表格，必须有明确角色、信息流和责任链 |
| 服务定位与质量透明 | ACL Eldercare Locator；Medicare Care Compare | 把寻找服务、比较机构和获得支持视为基础设施入口 | 服务目录和比较工具有更新滞后与地区差异，不能替代实地核验 |
| 长期照护系统 | WHO framework for an integrated continuum of long-term care | 把长期照护放入健康老龄化、功能能力、照护连续性和制度建设中 | 长期照护框架不能用来压缩主体权利、同意和照护者劳动价值 |

## 价值、成本与疾病负担底座

这一层回答“为什么值得建、先建哪里、代价由谁承担”：Human Infra 不是只追求更炫的设备、更多数据或更高模型分数。健康损失、残障、早死、生活质量下降、照护负担、医疗支出、工作损失和资源分配都需要进入证据链，才能判断某个基础设施是否真正有公共价值。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 全球疾病负担 | IHME Global Burden of Disease；GBD Compare | 用死亡、发病、YLL、YLD、DALY 等指标观察疾病、伤害和风险因素造成的总体损失 | DALY 是群体负担指标，不是个体生命价值排序，也不能替代伦理判断 |
| 全球健康估计 | WHO Global Health Estimates | 为死亡原因、疾病负担和健康趋势提供跨国家比较资料 | 全球估计适合宏观优先级，不等于每个地方的本地真实负担 |
| 成本效果分析 | WHO cost-effectiveness portal；Second Panel on Cost-Effectiveness in Health and Medicine | 把成本、效果、时间范围、视角和不确定性纳入干预选择 | 成本效果不是唯一决策标准，公平、尊严、风险和权利必须并行 |
| 健康技术评估 | NICE technology appraisal；NICE health technology evaluations manual | 展示技术、药物、设备和数字健康工具如何进入证据、价值和资源决策流程 | HTA 结论依赖地区制度、支付方、价格和证据质量，不能机械迁移 |
| 价值评估 | ICER value assessment framework；QALY and evLYG materials | 为价格、临床获益、生活质量、成本效果和不确定性提供公开评估语言 | QALY/evLYG 是决策工具，不是人的尊严或社会价值计量器 |
| 支付与服务模式 | CMS Value-Based Programs | 把质量、结果、成本和支付激励连接起来，说明基础设施会改变组织行为 | 价值支付可能制造指标博弈，必须同时审查公平、风险调整和未预期伤害 |
| 医疗支出数据 | AHRQ Medical Expenditure Panel Survey | 为医疗支出、保险、服务使用和人群经济负担提供基础数据 | 支出数据说明成本结构，不自动说明某个干预值得买单 |

## 长寿证据底座

这一层用于支撑 `domains/longevity-evidence/`：把 Bryan Johnson / Blueprint 这类个体运行系统放回更大的长寿研究基础设施中。它的核心不是列出“抗衰清单”，而是给每一种候选干预标注来源、物种、研究阶段、可迁移性和风险。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 机制框架 | Hallmarks of Aging；NIH / NIA geroscience 线路 | 提供讨论衰老过程、慢病共因和健康寿命的机制语言 | 机制合理不等于人体有效，也不等于可以自行干预 |
| 多站点小鼠测试 | NIA Interventions Testing Program；JAX ITP | 用遗传异质小鼠和多研究站点测试候选饮食、药物或其他干预对寿命和健康指标的影响 | 动物寿命结果不能直接外推为人类用药、补剂或生活方案 |
| 多物种候选筛选 | NIA Caenorhabditis Intervention Testing Program | 用遗传多样的线虫模型筛选可能影响寿命和健康衰退的药理干预 | 低等模型适合发现候选线索，不提供人体有效性结论 |
| 数据库归档 | HAGR GenAge、DrugAge、LongevityMap、CellAge | 把基因、药物、寿命、长寿变异和细胞衰老信息沉淀为可查证资料层 | 数据库条目是研究线索，不是推荐清单或证据等级终点 |
| 转化研究网络 | Translational Geroscience Network | 把 geroscience 假说推进到临床试验设计、样本、终点和数据管理 | 临床试验仍需看具体适应症、终点、状态、结果和安全性 |
| 人体试验范式 | MILES；TAME | MILES 展示 metformin 与人体衰老生物学指标的早期探索；TAME 代表“瞄准衰老而非单病种”的试验范式 | 不能写成 metformin 已经证明可抗衰；TAME 也不能替代已完成的临床终点证据 |

## 认知与人机协作底座

这一层用于支撑 AI 时代的 Human Infra 叙事：人不是被 AI 替代的抽象资源，而是与工具、任务、界面、组织约束和恢复环境共同组成的执行系统。这里的重点不是“使用更多 AI”，而是让协作系统可测量、可解释、可恢复、可审计。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 工作负荷测量 | NASA Task Load Index | 提供任务负荷的主观测量框架，适合讨论任务设计、界面压力和人机系统评估 | NASA-TLX 不是心理诊断，也不能单独证明某个工具更安全 |
| 认知负荷理论 | Sweller 的 Cognitive Load Theory | 把学习、任务设计和工具复杂度接回工作记忆限制，说明“信息更多”不等于“执行更强” | 教育和任务设计框架不能直接简化成通用效率公式 |
| 注意力恢复 | Kaplan Attention Restoration Theory | 把注意力、环境和恢复纳入工作系统，而不是只归因于自律 | 不能把自然暴露或环境设计包装成医疗治疗 |
| 以人为中心设计 | ISO 9241-210 | 给交互系统设计提供用户、任务、环境和迭代评估的标准语言 | 以人为中心不是视觉美化，也不是跳过安全验证 |
| 人机交互规则 | Guidelines for Human-AI Interaction | 把 AI 系统的提示、纠错、置信度、反馈和控制权设计成可审查对象 | 交互指南不能替代模型评估、数据治理或安全测试 |
| 人机团队 | National Academies Human-AI Teaming 线路 | 把 AI 视为团队成员或任务系统组件，强调信任、透明度、训练、权责和情境适配 | 高风险场景必须做具体任务验证，不能只凭“human-in-the-loop”口号 |
| AI 风险治理 | NIST AI Risk Management Framework | 提供治理、映射、测量和管理 AI 风险的框架，适合接入 Human Infra 的安全边界 | 框架不是合规豁免，也不自动证明具体 AI 系统可信 |
| 知识工作实证 | Generative AI at Work | 展示生成式 AI 在真实工作任务中可能改变生产率、学习曲线和人员差异 | 单一行业或任务的实证结果不能外推为所有知识工作 ROI |

## 神经伦理与 BCI 安全底座

这一层用于支撑 `domains/memory-editing/` 和 `domains/disembodied-cns/`：神经科技不是“更强输入输出接口”这么简单，它直接触及主体性、人格连续性、同意能力、隐私、可退出性、临床风险和长期设备依赖。仓库只能整理高层证据、审查问题和治理边界，不提供神经操控、植入、刺激、记忆调制或人体实验步骤。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 神经伦理原则 | NIH BRAIN Initiative neuroethics guiding principles | 把神经研究中的安全、主体性、隐私、公共参与和公平问题前置为研究设计约束 | 伦理原则不是技术可行性背书，也不能替代 IRB、临床监管或受试者保护 |
| 国际治理规范 | OECD Responsible Innovation in Neurotechnology；UNESCO Ethics of Neurotechnology | 把 neurotechnology 放入负责任创新、人格尊严、数据治理和社会影响框架 | 国际规范是治理底线，不是批准具体设备或实验的证据 |
| BCI 临床设备路径 | FDA implanted BCI guidance；FDA IDE | 把植入式 BCI 视为高风险医疗设备，要求非临床测试、临床设计、安全监测和监管路径 | 不能把临床试验登记或早期可行性试验写成产品安全性已经成立 |
| 试验登记与早期证据 | Neuralink PRIME；Synchron COMMAND | 显示 BCI 已进入真实临床试验和早期可行性研究，但样本量、适应症和终点都非常受限 | 不表示普通人增强、消费级脑控或去具身生命系统已经可执行 |
| 记忆干预伦理 | Memory modification scoping review；molecular memory modification；neuromodulation and memory | 为记忆编辑提供身份、真实性、伤害、同意和治疗边界的伦理语汇 | 不提供药物、刺激、植入或行为干预步骤；只作为伦理和证据边界资料 |
| 神经数据与主体权利 | UNESCO/OECD neurotechnology ethics；BRAIN neuroethics | 把神经数据视为高度敏感的人格相关信息，要求隐私、控制权、审计和退出机制 | 不把“采集更多神经数据”默认视为进步；必须证明保护和必要性 |

## 组织安全与事件学习底座

这一层用于支撑组织级 Human Infra：如果任务系统依赖人持续判断、交接、值守、复盘和协作，那么疲劳、沟通断裂、告警淹没、隐性工作、惩罚性文化和浅层复盘都会成为基础设施风险。这里的重点不是把医疗安全照搬到所有组织，而是吸收其成熟经验：把错误看成系统信号，把复盘转成改进动作，把疲劳和班次当作设计变量。

| 层级 | 资料或项目 | 对 Human Infra 的意义 | 使用边界 |
| --- | --- | --- | --- |
| 患者安全与系统观 | WHO Global Patient Safety Action Plan；To Err is Human | 把伤害、错误和防护从个人失误重构为系统设计、学习和治理问题 | 医疗安全经验不能直接外推到所有行业，必须重建任务语境 |
| 团队沟通与交接 | AHRQ TeamSTEPPS | 提供团队沟通、情境感知、互相支持和领导力的训练框架 | 培训材料不能替代 staffing、流程、工具和管理责任 |
| 单元级安全改进 | AHRQ CUSP | 把前线人员、管理支持、缺陷识别和持续改进结合成安全改进流程 | CUSP 是组织改进框架，不是一次性检查表 |
| 高可靠组织 | AHRQ PSNet High Reliability Organizations；Leveson STAMP | 说明高风险系统需要前置风险感知、韧性、冗余、反馈和组织学习 | “高可靠”不能变成品牌词，必须有事件数据和改进闭环 |
| 疲劳与班次风险 | NIOSH fatigue resources；OSHA worker fatigue | 把疲劳、长工时、夜班、恢复不足和事故风险纳入组织设计 | 不能把疲劳管理变成要求个人硬扛；排班和资源配置是系统责任 |
| 事件复盘与 RCA2 | AHRQ root cause analysis；IHI RCA2 | 把事故复盘从“找根因”推进到强行动项、风险降低和组织学习 | 复盘不应制造替罪羊，也不能停在无效建议和口号整改 |
| 安全文化测量 | AHRQ Surveys on Patient Safety Culture | 提供观察团队报告文化、沟通开放度、管理支持和学习能力的工具 | 测量必须用于改善系统，不应成为压制报告或排名惩罚工具 |

## 文献主干

| 主题 | 文献或资料 | 为什么重要 | 应放入的后续子域 |
| --- | --- | --- | --- |
| 衰老机制 | Lopez-Otin 等，The Hallmarks of Aging | 提供长寿证据和干预讨论的机制框架，但不能直接等同于人体疗效 | `domains/longevity-evidence/` |
| Geroscience | NIH GeroScience Interest Group；Translational Geroscience Network | 把衰老视为多个慢病和功能衰退的共同风险机制，并推动临床试验基础设施 | `domains/longevity-evidence/` 与 README 叙事 |
| 长寿干预测试 | NIA ITP / CITP；HAGR DrugAge | 提供候选干预从模型、数据库到证据等级整理的基础资料 | `domains/longevity-evidence/` 数据源和证据模型 |
| Metformin 与 TAME | MILES；TAME；metformin targeting aging 文献 | 是“把衰老作为干预目标”的经典转化案例，也展示证据边界和监管挑战 | 临床试验、药品安全、宣传边界 |
| 人口级健康数据 | All of Us；UK Biobank；NHANES；Framingham；GTEx | 为 Human Infra 提供长期队列、公共健康调查、生物样本库和分子表型基础设施 | 数据治理、隐私、代表性、可迁移性和子域证据模型 |
| 学习型健康系统与真实世界证据 | ClinicalTrials.gov；FDA RWE；PCORnet；OHDSI OMOP；HL7 FHIR；NICE ESF | 把数据、临床研究、互操作、监管和数字健康评估接成证据生成链 | 证据政策、数据治理、数字健康边界、临床试验和产品化审查 |
| 患者健康记录访问、互操作与数据可携带 | ONC health records；USCDI；TEFCA；CMS Patient Access；CMS Blue Button；HL7 FHIR / SMART | 把患者本人和授权照护者的数据访问、核对、携带和应用授权纳入 Human Infra，而不是默认机构数据会自然跟着人走 | 患者访问、数据可携带、跨机构交换、授权应用、保险数据 API、反数据锁定 |
| 信任、隐私与数据治理 | HHS HIPAA；Common Rule；NIST Privacy；NIST CSF；NIH GDS；GA4GH；ONC Information Blocking | 把敏感数据采集、共享、研究和产品化放回主体权利、受试者保护、安全和用途边界中 | 伦理边界、数据治理、神经数据权利、组织监控反滥用、安全审查 |
| 功能、生活质量与患者报告结局 | PROMIS；WHO ICF；EQ-5D；ICHOM；PRO-CTCAE；WHOQOL | 把“人是否真的更好”从口号转成可测量的功能、症状、生活质量和患者中心结果 | 结局定义、产品价值评估、照护路径、组织使用边界 |
| 康复、辅助技术与可访问性 | WHO rehabilitation；WHO/UNICEF assistive technology；WHO priority assistive products；WCAG；Section 508；ADA effective communication | 把能力恢复、功能补偿、数字无障碍和沟通权利放进基础设施设计 | 康复服务、辅助产品、无障碍设计、合理便利、反排除边界 |
| 价值、成本与疾病负担 | IHME GBD；WHO Global Health Estimates；WHO-CHOICE；NICE HTA；ICER；CMS；AHRQ MEPS | 把基础设施建设接回疾病负担、健康经济学、资源分配、支付激励和公共价值 | 优先级设定、经济评价、支付边界、公共卫生叙事 |
| 慢性压力、负荷与恢复 | McEwen / Stellar 的 allostatic load 线路；Cohen Perceived Stress Scale；WHO mental health at work；NIOSH WellBQ | 把压力、恢复、工作条件和长期疾病风险放进同一套生理与组织成本模型 | `docs/explanations/`、公共健康基线与组织使用边界 |
| 社会决定因素与生活环境 | WHO SDOH；Healthy People 2030；CDC/ATSDR SVI；CDC/ATSDR EJI；CDC PLACES；USDA Food Access；CMS AHC | 把个体运行能力接回住房、食物、环境、交通、社区和服务可及性 | 公共健康、资源配置、公平审查、组织使用边界 |
| 住房稳定、无家可归与驱逐风险 | UN-Habitat Housing；HUD AHAR；Census AHS；Household Pulse Survey；Eviction Lab | 把稳定、可负担、可持续居住的住所纳入 Human Infra，而不是默认每个人都有可保有的家 | 住房稳定、住房负担、无家可归、驱逐风险、临时居住、反住房污名 |
| 社会连接、孤独风险与社区归属 | WHO social connection report；CDC social connectedness；Healthy People Social and Community Context；NASEM social isolation；NHS social prescribing | 把关系网络、孤独风险、社区归属和服务转介纳入 Human Infra，而不是把断联和孤独归因于个人性格 | 社会连接、老年支持、社区参与、社会处方、危机发现、反污名边界 |
| 经济安全、社会保护与时间结构 | ILO Social Protection；World Bank Universal Social Protection / ASPIRE；DOL paid leave / FMLA；UN time use；ILO working time；Fed SHED；CFPB financial well-being；EITC | 把收入安全、社会保护、带薪休假、工作时间和现金缓冲纳入 Human Infra，而不是把资源不足归咎于个人 | 经济韧性、时间贫困、带薪照护、社会保障、金融压力、反贫困边界 |
| 公共福利、行政负担与服务导航 | USA.gov Benefit Finder；Performance.gov CX；SNAP；Medicaid.gov；HealthCare.gov Medicaid & CHIP；SSA SSI；ACF LIHEAP；Administrative Burden | 把资格理解、申请、证明材料、等待、续期、申诉、人工帮助和跨机构服务体验纳入 Human Infra，而不是默认福利会自动到达人 | 福利导航、服务递送、行政负担、申请成本、续期流失、反程序性排除 |
| 社区资源导航、社会服务转介与资源目录 | 211；Open Referral HSDS；Gravity Project；CMS AHC；ACL Eldercare Locator | 把本地资源目录、热线导航、社会需求筛查、转介和回访纳入 Human Infra，而不是默认人能自己找到正确机构并完成连接 | 社区资源导航、社会服务转介、资源目录、闭环转介、个案导航、反服务碎片化 |
| 金融接入、支付与消费者金融保护 | World Bank Financial Inclusion / Global Findex；FDIC Household Survey / Money Smart；CFPB Consumer Complaint Database / Credit Trends；Federal Reserve Payments Study | 把账户、支付、数字金融、信用、债务、费用、投诉和消费者保护纳入 Human Infra，而不是默认金融系统人人可用且安全 | 金融包容、支付网络、账户可得性、消费者保护、金融教育、反金融排除边界 |
| 保险、风险转移与理赔连续性 | NAIC consumer resources；USA.gov health insurance / unemployment benefits / workers' compensation；Benefits.gov Disability Assistance；FDIC deposit insurance；PBGC；World Bank disaster risk finance；NAIC flood insurance | 把疾病、失业、工伤、残障、灾害、银行倒闭和养老金中断后的风险分摊、理赔、收入替代和申诉渠道纳入 Human Infra，而不是默认家庭可以独自吸收冲击 | 保险覆盖、理赔、收入替代、残障援助、存款保险、养老金保障、灾害风险融资、反保险排除 |
| 食物保障、营养支持与水卫生 | FAO SOFI；FAOSTAT food security；WFP HungerMap；WHO healthy diet / malnutrition / food safety；WHO/UNICEF JMP；WHO drinking-water / sanitation | 把食物、营养、食品安全、饮水和卫生条件纳入 Human Infra，而不是把饥饿、营养不足和 WASH 缺口归因于个人选择 | 食物系统、儿童营养、WASH、灾害响应、公共健康、公平审查 |
| 能源接入、清洁烹饪与基础公用事业 | World Bank Energy；IEA electricity access；IEA clean cooking；WHO household air pollution；DOE LEAD Tool；DOE Weatherization；EPA IAQ | 把电力、清洁烹饪、室内空气、能源负担和住宅能效纳入 Human Infra，而不是默认家庭总有稳定、可负担、清洁能源 | 能源接入、清洁烹饪、室内环境、能源贫困、住宅韧性、反污名边界 |
| 气候风险、早期预警与社区韧性 | IPCC AR6；WMO Early Warnings for All；Climate Resilience Toolkit；CMRA；NOAA NCEI；CDC Climate and Health；CDC/ATSDR EJI | 把热浪、洪水、火灾、风暴、空气质量恶化、基础设施中断和灾后恢复纳入 Human Infra，而不是默认环境冲击只是背景 | 气候风险、预警、适应、社区韧性、环境正义、灾害恢复、反气候风险污名 |
| 家庭应急准备、个人韧性与灾前准备 | Red Cross preparedness；Red Cross survival kit；Red Cross make a plan；Red Cross emergency app；CDC Prepare Your Health；CDC disaster safety；NOAA Weather-Ready Nation | 把家庭计划、物资包、药物和健康文件、备用通信、特殊需求、天气风险认知和本地行动线索纳入 Human Infra，而不是默认收到警报就能行动 | 家庭应急计划、个人韧性、健康准备、应急物资包、备用通信、特殊需求、反个人责任转嫁边界 |
| 公共预警、应急通信与求助入口 | FEMA IPAWS；FCC WEA；FCC EAS；NOAA Weather Radio；Ready.gov alerts；911.gov；NG911；FirstNet | 把警报分发、移动和广播触达、天气广播、紧急呼叫和响应者通信纳入 Human Infra，而不是默认危机信息会自然抵达人 | 公共预警、应急通信、911/NG911、第一响应者通信、危机信息可达、反信息排除边界 |
| 灾后恢复、个人援助与临时安置 | USA.gov disaster / assistance / financial help / food help / bills help；FEMA DRC Locator；SBA Disaster Assistance；Benefits.gov Disaster Relief；Red Cross shelters | 把灾后援助、恢复中心、临时避难、食物、账单、贷款和福利导航纳入 Human Infra，而不是默认预警和急救之后生活会自然恢复 | 灾后恢复、个人援助、临时安置、财务缓冲、灾害贷款、福利导航、反救助资格误导 |
| 免疫屏障、感染监测与公共卫生应急 | WHO vaccines / IA2030；CDC vaccines；CDC NNDSS；WHO GISRS；WHO IHR / emergencies；WHO IPC；CDC NHSN；WHO AMR / GLASS；WHO One Health；CDC NWSS | 把疫苗、传染病监测、公共卫生应急、感染防控、AMR、One Health 和废水监测纳入 Human Infra，而不是把感染风险全部归因于个人卫生 | 免疫计划、疫情监测、应急准备、医疗机构安全、AMR 治理、跨物种风险 |
| 母婴健康、儿童发展与早期生命基础设施 | WHO maternal health / mortality / antenatal care；WHO newborn mortality；WHO child health / growth standards；Nurturing Care；CDC PRAMS；CDC Child Development；DHS；World Bank ECD；Healthy People pregnancy and childbirth | 把孕产、新生儿、儿童健康、生长、早期照护和家庭数据纳入 Human Infra，而不是把能力形成只看成成年后的个人努力 | 孕产健康、新生儿照护、儿童发展、早期学习、家庭支持、反监控边界 |
| 托育、早期教育与家庭工作连续性 | World Bank Childcare；ILO Care Work；DOL Childcare；ACF OCC / CCDF；ChildCare.gov；NSECE；Census child care；CDC Positive Parenting | 把托育、早期学习、照护劳动、费用、服务导航和父母工作连续性纳入 Human Infra，而不是把儿童照护全部交给家庭硬扛 | 托育可得性、早期教育、家庭时间、照护劳动、父母就业、服务导航、反托育污名 |
| 法律身份、公民登记与权利入口 | UN Legal Identity Agenda；UN Statistics CRVS；WHO CRVS；World Bank ID4D data；UNICEF birth registration | 把出生登记、法律身份、民事登记和生命统计纳入 Human Infra，而不是默认每个人都能证明自己、进入服务和被制度承认 | 法律身份、出生登记、CRVS、证件可得性、身份排除、服务入口、反监控边界 |
| 司法可及、法律援助与权利救济 | UN SDG 16；World Justice Project Rule of Law Index；Legal Services Corporation Justice Gap；DOJ Access to Justice；ABA Free Legal Answers | 把纠纷解决、民事法律需求、法律援助、程序可理解性和权利救济纳入 Human Infra，而不是默认纸面权利会自动变成现实能力 | 司法可及、法律援助、民事法律需求、申诉救济、在线法律帮助、反程序性排除 |
| 公民参与、投票可达与选举基础设施 | USA.gov voter registration；EAC voters / NVRA form；EAC VVSG；NIST voting；DOJ Voting Section；ADA voting；International IDEA turnout；ACE；OSCE ODIHR | 把选民登记、投票系统、无障碍投票、投票权执行、参与数据和选举观察纳入 Human Infra，而不是默认政治权利会自然变成真实参与 | 公民参与、选民登记、投票可达、选举系统标准、无障碍投票、选举观察、反党派操控边界 |
| 迁移、流离失所与人道服务连续性 | UN Global Compact for Migration；IOM World Migration Report；UNHCR Operational Data Portal；WHO Health and Migration；IDMC GRID；OCHA HDX；INEE Minimum Standards | 把跨境迁移、难民、内部流离失所和人道危机中的服务连续性纳入 Human Infra，而不是默认每个人都在稳定地址、国籍和服务网络里生活 | 迁移治理、庇护、保护、服务连续性、人道数据、教育应急、反排除边界 |
| 数字接入、信息可达与公共服务基础设施 | ITU ICT statistics；World Bank Digital Development；NTIA Digital Nation；U.S. Census computer and internet use；NIST Digital Identity Guidelines；Login.gov；Digital.gov；USWDS；UNESCO MIL；IMLS PLS | 把互联网、设备、数字身份、公共服务体验、信息素养和图书馆纳入 Human Infra，而不是默认每个人都能使用线上服务与 AI 工具 | 数字包容、公共服务设计、身份认证、信息素养、公共图书馆、反数字排除 |
| 个人数字安全、账号恢复与身份盗用防护 | FTC scams / phishing；IdentityTheft.gov；ReportFraud；FBI IC3；NIST SP 800-63-4；Login.gov | 把账号保护、身份盗用恢复、诈骗举报和公共账号恢复纳入 Human Infra，而不是默认数字入口天然安全且可恢复 | 账号安全、身份盗用、诈骗防护、账号恢复、网络犯罪报告、反受害者归因 |
| 语言可达、清晰沟通与健康素养 | PlainLanguage.gov；Digital.gov plain language；LEP.gov；National CLAS；CDC health literacy；CDC Clear Communication Index；W3C cognitive accessibility | 把说明、表单、通知、健康信息、语言服务和认知可访问性纳入 Human Infra，而不是默认人自然能理解复杂制度和医疗信息 | 清晰沟通、语言服务、健康素养、认知可访问性、反语言排除 |
| 交通可达、公共交通与日常移动 | World Bank Transport；FTA National Transit Database；BTS National Household Travel Survey；USDOT Equitable Transportation Community Explorer RFI；FTA ADA guidance / FAQs | 把到达学校、工作、医疗、福利、照护、食品和避难地点的移动能力纳入 Human Infra，而不是默认空间距离会自然消失 | 交通可达、通勤负担、公共交通、交通公平、无障碍出行、辅助交通、灾害撤离 |
| 医疗可及性、初级卫生保健与基本服务 | WHO UHC；WHO Primary Health Care；WHO Essential Medicines Lists；WHO Health Workforce；World Bank UHC；CDC access / insurance；AHRQ Data Tools | 把医疗覆盖、费用保护、第一接触服务、基本药物、医护 workforce 和质量差异纳入 Human Infra，而不是默认医疗会自然抵达人 | 医疗可及性、UHC、初级保健、基本药物、医护人员、保险覆盖、质量差异、反医疗排除 |
| 远程医疗、数字照护与居家监测 | Telehealth.HHS.gov；HHS Remote Patient Monitoring；HRSA Telehealth；CMS / Medicare telehealth；FDA Digital Health | 把远程问诊、远程监测、居家设备、覆盖规则和数字健康监管纳入 Human Infra，而不是默认医疗必须发生在固定诊室 | 远程医疗、RPM、虚拟照护、居家连续性、数字健康监管、反数字医疗排除 |
| 药品可及、用药安全与供应连续性 | WHO Essential Medicines；WHO Medication Without Harm；FDA Drug Shortages；FDA NDC；DailyMed；MedlinePlus；Medicare Part D；CDC Medication Safety | 把关键药物选择、短缺、标签、药品信息、支付覆盖和用药安全纳入 Human Infra，而不是默认处方会自然变成持续治疗 | 药品可及、供应连续性、用药安全、标签信息、患者理解、支付覆盖、反自行用药边界 |
| 心理健康、成瘾与危机照护 | WHO World Mental Health Report；WHO mhGAP；WHO Mental Health Atlas；FindTreatment.gov；NIMH mental illness；CDC overdose prevention；988 Lifeline | 把心理健康服务、成瘾治疗、过量预防和危机连续照护纳入 Human Infra，而不是把心理痛苦和成瘾风险归因于个人意志 | 心理健康服务、成瘾治疗、危机热线、过量预防、社区照护、反污名边界 |
| 人身安全、伤害预防与应急响应基础设施 | WHO injuries and violence；CDC Injury Center；CDC WISQARS；CDC Violence Prevention；CDC ACEs；CDC Suicide Prevention；988 Lifeline；WHO Emergency Care；CDC Natural Disasters | 把伤害、暴力、儿童逆境、自杀风险、急救和灾害冲击纳入 Human Infra，而不是默认人处在安全环境里 | 伤害监测、暴力预防、危机支持、急救系统、灾害准备、反惩罚性风险评分 |
| 建成环境、交通与环境暴露 | WHO Housing；WHO Urban Health；CDC BE Tool；CDC Active Communities Tool；WHO Air Quality Guidelines；AirNow；CDC Heat and Health Index；WHO Road Safety | 把住房、街道、通勤、空气、热风险和交通伤害纳入 Human Infra，而不是把生活空间当作背景 | 城市健康、社区规划、主动交通、环境暴露、道路安全、公平审查 |
| 学习、技能形成与能力成长 | How People Learn II；IES WWC；UNESCO UIS/UIL；O*NET；World Bank Human Capital | 把学习、反馈、技能、终身教育和能力投资纳入 Human Infra，而不是只看当下表现 | 学习系统、技能地图、组织训练、教育公平、知识工作 |
| 就业服务、劳动力发展与职业转换 | World Bank Jobs；ILO Employment Promotion；DOL ETA / WIOA；American Job Centers；Apprenticeship.gov；O*NET；My Next Move；JAN | 把公共就业服务、职业导航、再培训、学徒制、转岗和就业无障碍纳入 Human Infra，而不是默认能力会自然变成工作 | 就业服务、培训路径、职业转换、劳动力市场制度、就业无障碍、反自动筛选 |
| 自我追踪文化 | Gary Wolf / Quantified Self | 解释从个人记录、传感器、指标到生活系统的历史线路 | README 叙事与应用案例 |
| 公共健康基线 | WHO / HHS / CDC / AASM / Dietary Guidelines | 为睡眠、运动、营养、心理健康和恢复提供低风险底座 | `docs/reference/` 与应用案例 |
| 工作与福祉 | NIOSH Total Worker Health 文献与工具 | 把“工作设计”作为健康基础设施，而不是只要求个人自律 | 组织应用与安全边界 |
| 健康老龄化 | WHO ICOPE | 把老年照护从疾病中心转向能力维护和路径设计 | Longevity Evidence 与应用案例 |
| 照护、家庭照护者与长期服务 | National Strategy to Support Family Caregivers；CDC Caregiving；Families Caring；Medicaid HCBS；Medicare home health/hospice；AHRQ Care Coordination；WHO long-term care | 把家庭照护者、居家社区服务、照护协调和长期照护纳入 Human Infra，而不是把运行失败都归给个人和家庭 | 照护支持、长期服务、照护者健康、服务导航、老龄社会、反责任转嫁边界 |
| 数字健康验证 | Apple Heart Study | 展示可穿戴传感器进入健康系统时需要大规模验证、确认和边界沟通 | 数据脚本、证据政策、数字健康案例 |
| 极端环境人因 | NASA HRP / HSI | 把人的生理、认知、环境和任务风险当作工程约束 | 去具身中枢、未来等待、任务执行模型 |
| 神经科技治理 | NIH BRAIN、DARPA NESD、ClinicalTrials.gov 神经接口试验 | 提供记忆编辑、神经接口和主体权利讨论的真实研究背景 | `domains/memory-editing/` 与 `domains/disembodied-cns/` |
| 神经伦理 | BRAIN Neuroethics principles；OECD/UNESCO neurotechnology ethics | 为神经科技的主体性、隐私、同意、公平和公共治理提供规范主干 | `domains/memory-editing/`、`domains/disembodied-cns/` 与安全边界 |
| BCI 临床安全 | FDA implanted BCI guidance；FDA IDE；ClinicalTrials.gov BCI studies | 把 BCI 从技术演示拉回医疗设备、试验设计和长期安全问题 | BCI 试验、神经接口边界、审查清单 |
| 记忆干预伦理 | Memory modification ethics reviews；neuromodulation and memory | 连接记忆编辑与身份、真实性、创伤治疗、同意和伤害评估 | `domains/memory-editing/` 的高层伦理材料 |
| 系统安全 | Nancy Leveson, Engineering a Safer World | 把事故理解为控制、组织和系统约束问题，而不只是个体失误 | Human SRE、审查清单、安全边界 |
| 认知负荷 | NASA-TLX；Cognitive Load Theory | 把任务执行失败的一部分解释为负荷、界面和工作记忆限制，而不是个人意志不足 | AI 工具、知识工作和组织应用 |
| 注意力与恢复 | Attention Restoration Theory | 把环境、注意力疲劳和恢复放进任务系统设计 | 公共健康基线、知识工作、组织设计 |
| 人机协作 | NIST AI RMF；Guidelines for Human-AI Interaction；Human-AI Teaming | 把 AI 从“模型能力”重新放回人、任务、组织和风险治理系统 | AI 协作、Human SRE、宣传边界 |
| 生成式 AI 与知识工作 | Generative AI at Work；Microsoft New Future of Work | 为 AI 进入真实工作流提供实证和研究议程，而不是只靠产品宣传 | README 叙事、AI 工具边界、后续应用案例 |
| 组织安全 | WHO Patient Safety；AHRQ TeamSTEPPS / CUSP / HRO；IHI RCA2 | 把团队沟通、疲劳、事件复盘和组织学习纳入 Human Infra，而不是把失败归咎于个人 | 组织应用、安全边界、Human SRE、后续审查模板 |
| 疲劳管理 | NIOSH fatigue；OSHA worker fatigue | 把长工时、夜班和恢复不足视为安全风险和组织设计变量 | 职业健康、任务排班、高压组织应用 |

## 如何用于 README 和宣传

宣传时可以强表达：

```text
Human Infra 不是凭空发明的新词。
Bryan Johnson、NIA ITP、Geroscience、HAGR、All of Us、UK Biobank、NHANES、Framingham、GTEx、ClinicalTrials.gov、FDA RWE、PCORnet、OHDSI OMOP、HL7 FHIR、NIST Privacy Framework、GA4GH、PROMIS、WHO ICF、EQ-5D、ICHOM、WHO Rehabilitation、assistive technology、WCAG、Section 508、How People Learn、IES WWC、O*NET、World Bank Human Capital、UN-Habitat Housing、HUD AHAR、Census American Housing Survey、Household Pulse Survey、Eviction Lab、WHO social connection、CDC social connectedness、Healthy People Social and Community Context、NASEM social isolation、NHS social prescribing、ILO Social Protection、World Bank ASPIRE、DOL paid leave、FMLA、UN time use、Fed SHED、CFPB financial well-being、World Bank Global Findex、FDIC Household Survey、CFPB Consumer Complaint Database、Federal Reserve Payments Study、FAO SOFI、WFP HungerMap、WHO healthy diet、WHO malnutrition、WHO food safety、WHO/UNICEF JMP、WHO drinking-water、WHO sanitation、World Bank Energy、IEA electricity access、IEA clean cooking、WHO household air pollution、DOE LEAD Tool、DOE Weatherization、EPA IAQ、IPCC AR6、WMO Early Warnings for All、NOAA NCEI、Climate Resilience Toolkit、CMRA、CDC Climate and Health、CDC Heat and Health、CDC/ATSDR EJI、WHO IA2030、CDC NNDSS、WHO GISRS、IHR、WHO IPC、CDC NHSN、WHO AMR、GLASS、One Health、CDC NWSS、WHO maternal health、WHO newborn mortality、WHO child health、WHO child growth standards、Nurturing Care Framework、CDC PRAMS、CDC Child Development、DHS Program、World Bank ECD、World Bank Childcare、ILO Care Work、DOL Childcare、ACF Office of Child Care、CCDF、ChildCare.gov、NSECE、Census Child Care、CDC Positive Parenting、UN Legal Identity Agenda、UN Statistics CRVS、WHO CRVS、World Bank ID4D、UNICEF birth registration、UN SDG 16、World Justice Project Rule of Law Index、Legal Services Corporation Justice Gap、DOJ Access to Justice、ABA Free Legal Answers、EAC voters、EAC VVSG、NIST voting、DOJ Voting Section、ADA voting、International IDEA voter turnout、ACE Electoral Knowledge、OSCE ODIHR elections、UN Global Compact for Migration、IOM World Migration Report、UNHCR Operational Data Portal、WHO Health and Migration、IDMC GRID、OCHA HDX、INEE Minimum Standards、ITU ICT statistics、World Bank Digital Development、NTIA Digital Nation、U.S. Census computer and internet use、NIST Digital Identity Guidelines、Login.gov、FTC scams、FTC phishing、IdentityTheft.gov、ReportFraud、FBI IC3、Digital.gov、USWDS、UNESCO Media and Information Literacy、IMLS Public Libraries Survey、World Bank Transport、FTA National Transit Database、BTS National Household Travel Survey、USDOT Equitable Transportation Community Explorer RFI、FTA ADA guidance、WHO Universal Health Coverage、WHO Primary Health Care、WHO Essential Medicines Lists、WHO Health Workforce、World Bank UHC、CDC access to health care、CDC health insurance、AHRQ NHQDR Data Tools、WHO World Mental Health Report、WHO mhGAP、WHO Mental Health Atlas、FindTreatment.gov、NIMH mental illness、CDC overdose prevention、988 Lifeline、WHO injuries and violence、CDC Injury Center、CDC WISQARS、CDC Violence Prevention、CDC ACEs、CDC Suicide Prevention、988 Lifeline、WHO Emergency Care、CDC Natural Disasters、WHO Housing、WHO Urban Health、CDC Built Environment Assessment Tool、WHO Air Quality Guidelines、AirNow、CDC Heat and Health Index、WHO Road Safety、CDC Caregiving、Medicaid HCBS、Medicare home health、AHRQ Care Coordination、WHO long-term care、GBD、WHO-CHOICE、NICE HTA、ICER、Allostatic Load、WHO SDOH、CDC SVI、CDC PLACES、WHO mental health at work、NIOSH Total Worker Health、WHO ICOPE、WHO Patient Safety、AHRQ TeamSTEPPS、NASA HRP、Apple Heart Study、军队 H2F、NIH BRAIN、FDA BCI guidance、UNESCO/OECD neurotechnology ethics、NIST AI RMF、NASA-TLX 和系统安全工程，其实都在研究同一个更大的对象：
支撑人类长期运行、判断、创造、恢复和延续的基础设施。
```

药品可及、用药安全和供应连续性也应接入这条宣传链：WHO Essential Medicines、WHO Medication Without Harm、FDA Drug Shortages、FDA NDC、DailyMed、MedlinePlus、Medicare Part D 和 CDC Medication Safety 说明，治疗连续性不是处方纸自然带来的结果，而是一组供应、支付、标签、理解和安全防护基础设施。

家庭应急准备和个人韧性也应接入这条宣传链：Red Cross preparedness、survival kit、make a plan、emergency app、CDC Prepare Your Health 和 NOAA Weather-Ready Nation 说明，灾害准备不是个人买物资的私事；家庭计划、健康准备、备用通信、特殊需求和风险认知决定预警能否转成行动。

公共预警和应急通信也属于同一个对象：FEMA IPAWS、FCC WEA/EAS、NOAA Weather Radio、Ready.gov、911.gov、NG911 和 FirstNet 说明，危机中的“知道发生了什么、该往哪去、如何求助、响应者如何协同”本身就是人类运行基础设施。

灾后恢复和个人援助也应接入这条宣传链：USA.gov disaster assistance、FEMA Disaster Recovery Center Locator、SBA Disaster Assistance、Benefits.gov Disaster Relief 和 Red Cross shelters 说明，灾害不是警报响完就结束；住所、食物、账单、贷款、恢复中心和临时避难能否接上，决定生活能否重新启动。

远程医疗和居家监测也应接入这条宣传链：Telehealth.HHS.gov、HRSA Telehealth、CMS/Medicare Telehealth、HHS RPM 和 FDA Digital Health 说明，医疗可及性不只取决于有没有医院，还取决于诊疗、监测和照护能否跨越距离、设备、支付和数字能力断点。

社区资源导航和社会服务转介也应接入这条宣传链：211、Open Referral HSDS、Gravity Project、CMS AHC 和 ACL Eldercare Locator 说明，住房、食物、交通、照护和心理健康支持不只是“有没有项目”，还取决于资源目录、热线、筛查、转介、回访和本地服务容量能否闭环。

保险、风险转移和理赔连续性也应接入这条宣传链：NAIC、USA.gov health insurance / unemployment / workers' compensation、Benefits.gov Disability Assistance、FDIC、PBGC 和 World Bank disaster risk finance 说明，重大冲击后的恢复不只靠现金储蓄；覆盖、理赔、收入替代、申诉和资金保障决定家庭是否会被风险长期打断。

患者健康记录访问和数据可携带也应接入这条宣传链：ONC Get It, Check It, Use It、USCDI、TEFCA、CMS Patient Access、CMS Blue Button、HL7 FHIR 和 SMART App Launch 说明，健康数据不能只留在机构和应用之间流动；人本人能否获取、核对、携带和授权使用数据，也是连续照护基础设施。

公民参与和选举基础设施也应接入这条宣传链：USA.gov voter registration、EAC voters、EAC VVSG、NIST voting、DOJ Voting Section、ADA voting、International IDEA turnout、ACE 和 OSCE ODIHR 说明，人不仅要能进入制度，还要能影响制度如何运行；登记、投票可达、设备标准、无障碍、权利执行和选举观察本身就是公共反馈基础设施。

个人数字安全和身份盗用恢复也应接入这条宣传链：FTC scams/phishing、IdentityTheft.gov、ReportFraud、FBI IC3、NIST Digital Identity 和 Login.gov 说明，数字化不是把服务搬上网就完成；账号能否保住、被盗后能否恢复、诈骗能否报告和止损，本身就是现代生活基础设施。

但仓库文档必须弱结论：

- Bryan Johnson / Blueprint 是自我量化和个人运行系统案例，不是临床证据标准。
- NIA ITP、CITP、HAGR 和 Geroscience 是长寿证据基础设施，不是人体干预推荐。
- All of Us、UK Biobank、NHANES、Framingham 和 GTEx 是研究数据基础设施，不是个人诊断、健康评分或抗衰推荐系统。
- ClinicalTrials.gov、FDA RWE、PCORnet、OHDSI OMOP、HL7 FHIR、NICE ESF 和 WHO digital health guideline 是证据、互操作与监管基础设施，不表示某个具体产品或干预已经有效。
- ONC Get It, Check It, Use It、USCDI、TEFCA、CMS Patient Access、CMS Blue Button、HL7 FHIR 和 SMART App Launch 是患者访问、数据可携带和互操作资料，不是个人法律意见、完整病历保证、第三方应用背书、隐私安全承诺或任意二次利用健康数据的许可。
- HIPAA、Common Rule、NIST Privacy、NIST CSF、NIH GDS、GA4GH 和 ONC 资料是治理与风险边界，不是法律意见、合规认证或任意采集个人数据的许可。
- PROMIS、WHO ICF、EQ-5D、ICHOM、PRO-CTCAE、WHOQOL、CDC Healthy Days 和 SF-36 是结局测量语言，不是诊断工具，也不是把复杂人生压缩成单一分数的理由。
- WHO Rehabilitation、WHO/UNICEF assistive technology、WHO priority assistive products、WCAG、Section 508 和 ADA effective communication 是康复、辅助技术和可访问性资料，不是个人处方、设备推荐、形式合规豁免或排除能力受限者的理由。
- GBD、WHO Global Health Estimates、WHO-CHOICE、NICE HTA、ICER、CMS 和 AHRQ MEPS 是价值、成本和资源决策资料，不是把人的价值还原成金钱或 QALY/DALY 的许可。
- Allostatic Load、Perceived Stress Scale、WHO mental health at work、U.S. Surgeon General workplace well-being、NIOSH WellBQ、NIOSH/OSHA fatigue 资料是压力、恢复和工作条件的研究与治理语言，不是个人诊断工具，也不是组织监控或责任转嫁的许可。
- WHO SDOH、Healthy People 2030、CDC/ATSDR SVI、CDC/ATSDR EJI、CDC PLACES、USDA Food Access 和 CMS AHC 是社会与环境条件资料，不是给个体贴标签、拒绝服务或自动化决策的许可。
- UN-Habitat Housing、HUD AHAR、Census American Housing Survey、Household Pulse Survey 和 Eviction Lab 是住房稳定、住房负担、无家可归、搬迁压力和驱逐风险资料，不是法律意见、个案安置承诺、租赁资格判断、房产估值或给个人和社区贴住房污名标签的许可。
- WHO social connection、CDC social connectedness、Healthy People Social and Community Context、NASEM social isolation 和 NHS social prescribing 是社会连接、孤独风险、社区归属和服务转介资料，不是个人心理诊断、朋友数量 KPI、福利资格承诺、监控社交关系或把孤独归因于个人性格的许可。
- ILO Social Protection、World Bank ASPIRE、DOL paid leave、FMLA、UN time use、Fed SHED、CFPB financial well-being 和 EITC 是经济安全、时间结构和社会保护资料，不是福利资格承诺、税务建议、个人财务评分或把贫困归因于个人选择的许可。
- USA.gov Benefit Finder、Performance.gov CX、SNAP、Medicaid.gov、HealthCare.gov Medicaid & CHIP、SSA SSI、ACF LIHEAP 和行政负担文献是公共福利、服务递送、申请成本、续期、申诉和服务体验资料，不是个体资格承诺、法律意见、福利代办、自动审批工具或用复杂程序排除弱势人群的许可。
- 211、Open Referral HSDS、Gravity Project、CMS AHC 和 ACL Eldercare Locator 是社区资源导航、社会服务转介、资源目录和健康相关社会需求资料，不是服务资格承诺、个案管理替代品、资源实时可用性保证、自动化社会评分或未经同意共享敏感需求数据的许可。
- World Bank Financial Inclusion / Global Findex、FDIC Household Survey / Money Smart、CFPB Consumer Complaint Database / Credit Trends 和 Federal Reserve Payments Study 是金融接入、支付、信用、债务和消费者保护资料，不是开户资格承诺、投资建议、信贷建议、债务处理方案、机构背书或把金融排除归因于个人无知的许可。
- NAIC consumer resources / flood insurance、USA.gov health insurance / unemployment benefits / workers' compensation、Benefits.gov Disability Assistance、FDIC deposit insurance、PBGC 和 World Bank disaster risk finance 是保险、理赔、收入替代、存款/养老金保障和灾害风险融资资料，不是保险产品推荐、承保承诺、赔付保证、法律意见、投资建议或把高风险人群排除在保障之外的许可。
- FAO SOFI、FAOSTAT、WFP HungerMap、WHO healthy diet、WHO malnutrition、WHO food safety、WHO/UNICEF JMP 和 WHO drinking-water / sanitation 是食物保障、营养、食品安全和 WASH 资料，不是个人饮食处方、救助资格承诺、单户水质证明、具体食品检测报告或把饥饿归因于个人选择的许可。
- World Bank Energy、IEA electricity access、IEA clean cooking、WHO household air pollution、DOE LEAD Tool、DOE Weatherization 和 EPA IAQ 是能源接入、清洁烹饪、室内空气、能源负担和住宅能效资料，不是电网投资建议、单户空气检测、个体资格承诺、建筑合规证明或把能源贫困归因于个人选择的许可。
- IPCC AR6、WMO Early Warnings for All、Climate Resilience Toolkit、CMRA、NOAA NCEI、CDC Climate and Health、CDC Heat and Health 和 CDC/ATSDR EJI 是气候风险、早期预警、韧性规划、健康影响和环境正义资料，不是个体迁移建议、保险/贷款/救助资格判断、现场指挥替代品、自动搬迁依据或给高风险社区贴标签的许可。
- Red Cross preparedness / survival kit / make a plan / emergency app、CDC Prepare Your Health、CDC Natural Disasters safety 和 NOAA Weather-Ready Nation 是家庭应急准备、健康准备、物资包、风险认知和天气韧性资料，不是本地撤离命令、实时风险图、医疗建议、保险建议、救援承诺或把灾害责任转嫁给个人的许可。
- FEMA IPAWS、FCC WEA/EAS、NOAA Weather Radio、Ready.gov alerts、911.gov / NG911 和 FirstNet 是公共预警、应急通信、求助入口和第一响应者通信资料，不是实时警报保证、个人撤离路线、现场指挥替代品、通信可靠性承诺或绕开本地应急机构的许可。
- USA.gov disaster assistance、FEMA Disaster Recovery Center Locator、SBA Disaster Assistance、Benefits.gov Disaster Relief 和 Red Cross shelters 是灾后恢复、个人援助、临时避难、财务帮助、账单帮助和贷款资料，不是资格承诺、赔付保证、实时床位保证、法律意见、保险建议或用债务替代公共救助的许可。
- WHO vaccines / IA2030、CDC vaccines、CDC NNDSS、WHO GISRS、WHO IHR、WHO emergencies、WHO IPC、CDC NHSN、WHO AMR / GLASS、WHO One Health 和 CDC NWSS 是免疫、监测、应急、感染防控、耐药和废水信号资料，不是个人医疗建议、疫苗禁忌判断、疫情预测保证、临床操作协议或自动化限制个人自由的许可。
- WHO maternal health、WHO newborn mortality、WHO child health、WHO child growth standards、Nurturing Care、CDC PRAMS、CDC Child Development、DHS 和 World Bank ECD 是母婴、儿童和早期发展资料，不是个人孕产医疗建议、儿童诊断、家庭排名、保险筛选或监控父母的许可。
- World Bank Childcare、ILO Care Work、DOL Childcare、ACF Office of Child Care / CCDF、ChildCare.gov、NSECE、Census Child Care 和 CDC Positive Parenting 是托育、早期教育、照护劳动、服务导航和家庭工作连续性资料，不是个体补助资格承诺、托育机构背书、儿童诊断、父母评分、家庭监控或把托育缺口归因于家庭选择的许可。
- UN Legal Identity Agenda、UN Statistics CRVS、WHO CRVS、World Bank ID4D 和 UNICEF birth registration 是法律身份、民事登记、生命统计和出生登记资料，不是法律意见、证件资格承诺、身份真实性判定、移民身份判断、排除无证人群或扩大身份监控的许可。
- UN SDG 16、World Justice Project Rule of Law Index、Legal Services Corporation Justice Gap、DOJ Access to Justice 和 ABA Free Legal Answers 是司法可及、法律援助、民事法律需求和在线法律帮助资料，不是法律意见、律师推荐、案件代理、胜诉承诺、服务资格承诺或自动化司法评分许可。
- USA.gov voter registration、EAC voters、EAC National Mail Voter Registration Form、EAC VVSG、NIST voting、DOJ Voting Section、ADA voting、International IDEA turnout、ACE 和 OSCE ODIHR 是公民参与、投票可达、选举系统标准、投票权执行、投票率数据和选举观察资料，不是党派宣传、竞选策略、投票资格法律意见、选举结果背书或自动化操控公共意见的许可。
- UN Global Compact for Migration、IOM World Migration Report、UNHCR Operational Data Portal、WHO Health and Migration、IDMC GRID、OCHA HDX、ReliefWeb、INEE、IASC 和 Global Shelter Cluster 是迁移、流离失所、人道数据、健康迁移、教育应急和庇护协调资料，不是移民法律意见、庇护资格承诺、个案身份判定、遣返依据、现场指挥替代品或用迁移身份降低服务质量的许可。
- ITU、World Bank Digital Development、NTIA Digital Nation、U.S. Census computer and internet use、NIST Digital Identity Guidelines、Login.gov、Digital.gov、USWDS、UNESCO MIL 和 IMLS PLS 是数字接入、身份、公共服务、信息素养和图书馆资料，不是要求所有服务只保留线上渠道、用数字身份排除人群、或把信息污染责任全部转嫁给个人的许可。
- FTC scams/phishing、IdentityTheft.gov、ReportFraud、FBI IC3、NIST Digital Identity 和 Login.gov 是个人数字安全、身份盗用恢复、诈骗举报、账号恢复和认证资料，不是法律意见、执法承诺、损失追回保证、平台安全背书或把诈骗和账号盗用责任归咎于受害者的许可。
- PlainLanguage.gov、Digital.gov plain language、LEP.gov、National CLAS、CDC health literacy、CDC Clear Communication Index 和 W3C cognitive accessibility 是清晰沟通、语言服务、健康素养和认知可访问性资料，不是机器翻译背书、法律或医疗解释替代品、把理解失败归因于个人能力不足的许可。
- World Bank Transport、FTA National Transit Database、BTS National Household Travel Survey、USDOT Equitable Transportation Community Explorer RFI 和 FTA ADA guidance 是交通可达、公共交通、出行调查、交通公平和无障碍出行资料，不是个人路线建议、法律意见、服务资格承诺、房产价值判断、自动排除低机动性人群或把交通贫困归因于个人选择的许可。
- WHO UHC、WHO Primary Health Care、WHO Essential Medicines Lists、WHO Health Workforce、World Bank UHC、CDC access / insurance 和 AHRQ NHQDR Data Tools 是医疗可及性、基本服务、医护 workforce、保险覆盖和质量差异资料，不是医疗建议、保险资格承诺、药物处方、机构背书或用资源不足合理化低质量服务的许可。
- Telehealth.HHS.gov、HHS Remote Patient Monitoring、HRSA Telehealth、CMS/Medicare Telehealth 和 FDA Digital Health 是远程医疗、远程患者监测、覆盖规则和数字健康监管资料，不是医疗建议、保险报销承诺、具体服务可得性保证、急诊替代品或任何数字健康产品有效性背书。
- WHO Essential Medicines、WHO Medication Without Harm、FDA Drug Shortages、FDA NDC、DailyMed、MedlinePlus、Medicare Part D 和 CDC Medication Safety 是药品可及、用药安全、标签信息、短缺和覆盖资料，不是个人用药建议、替代药物建议、处方、停药建议、保险建议或网络购药背书。
- WHO World Mental Health Report、WHO mhGAP、WHO Mental Health Atlas、FindTreatment.gov、NIMH mental illness、CDC overdose prevention 和 988 Lifeline 是心理健康、成瘾、服务导航、危机支持和过量预防资料，不是个人诊断、治疗方案、药物建议、服务质量保证、法律意见或把心理痛苦和成瘾风险污名化的许可。
- WHO injuries and violence、CDC Injury Center、CDC WISQARS、CDC Violence Prevention、CDC ACEs、CDC Suicide Prevention、988 Lifeline、WHO Emergency Care 和 CDC Natural Disasters 是人身安全、伤害预防、危机支持和应急响应资料，不是个案责任判定、法律意见、临床处置、急救操作教程、自动化风险评分或现场指挥替代品。
- WHO Housing、WHO Urban Health、CDC BE Tool、CDC Active Communities Tool、WHO Air Quality Guidelines、AirNow、CDC Heat and Health Index 和 WHO Road Safety 是住房、城市、交通、空气、热风险和道路安全资料，不是个人医疗诊断、建筑合规认证、房产评分或自动化搬迁决策依据。
- How People Learn、IES WWC、UNESCO UIS/UIL、O*NET 和 World Bank Human Capital 是学习、技能和能力投资资料，不是速成学习法、自动人才评分、招聘筛选或把人还原成经济产出的许可。
- World Bank Jobs、ILO Employment Promotion、DOL ETA / WIOA、American Job Centers、Apprenticeship.gov、O*NET、My Next Move 和 JAN 是就业服务、劳动力发展、职业导航、学徒制、转岗和就业无障碍资料，不是岗位承诺、收入承诺、招聘筛选工具、法律意见、福利资格承诺或把失业归因于个人失败的许可。
- National Strategy to Support Family Caregivers、CDC Caregiving、Medicaid HCBS、Medicare home health/hospice、AHRQ Care Coordination 和 WHO long-term care 是照护支持与长期服务资料，不是福利资格承诺、医疗建议、机构背书或把照护劳动免费化的许可。
- MILES / TAME 是 metformin 与衰老生物学转化研究案例，不表示 metformin 已经被证明可用于普通人抗衰。
- Apple Heart Study 是数字健康验证案例，不表示所有可穿戴功能都可用于诊断。
- BRAIN、NESD、Neuralink PRIME 是神经科技研究和试验背景，不表示记忆编辑或去具身中枢已经可执行。
- FDA BCI guidance、OECD/UNESCO neurotechnology ethics 和记忆干预伦理文献说明神经科技必须进入临床监管、主体权利和长期安全治理，不表示任何植入、刺激或记忆调制可被普通项目复制。
- NIST AI RMF、Human-AI Interaction guidelines、NASA-TLX 和生成式 AI 工作研究说明 AI 协作必须进入风险、负荷和任务设计，不表示 AI 自动提高所有人的生产率。
- WHO Patient Safety、AHRQ、IHI、NIOSH 和 OSHA 资料说明组织系统会制造或缓解风险，不表示可以用“安全文化”包装责任转嫁。
- NASA、军队和职业健康案例能说明 Human Infra 的工程价值，但不能直接迁移到普通生活场景而不考虑伦理和权力关系。

## 下一批资料队列

- 长寿证据子域内部的数据模型、证据等级表和干预条目模板。
- 人口级健康数据条目模板：数据类型、样本偏倚、同意、访问控制、再识别风险和可迁移性。
- 学习型健康系统条目模板：数据来源、模型映射、终点定义、监管状态、互操作接口、偏倚控制和证据等级。
- 患者健康记录访问与数据可携带模板：数据类型、来源机构、患者或授权代表、身份核验、访问方式、格式、纠错路径、应用授权、撤回、审计日志、可访问性、隐私风险和反数据锁定边界。
- 信任与数据治理条目模板：数据类别、主体权利、同意范围、访问控制、最小必要、用途限制、日志审计、保留期限和删除路径。
- 功能与生活质量结局模板：目标人群、结局域、测量工具、最小重要差异、采集频率、解释边界和滥用风险。
- 康复与可访问性模板：功能目标、参与场景、辅助产品、训练维护、数字无障碍、沟通需求、合理便利和排除风险。
- 价值与疾病负担模板：目标问题、负担指标、成本口径、评估视角、时间范围、敏感性分析、公平影响和伦理边界。
- 压力与恢复模板：压力来源、暴露时长、恢复机会、主观负荷、工作条件、社会支持、疲劳风险、组织责任和滥用边界。
- 社会决定因素模板：地理尺度、生活条件、环境暴露、服务可及性、数据粒度、偏差风险、资源连接和反标签化边界。
- 住房稳定模板：住房负担、租住关系、搬迁风险、驱逐记录、临时居住、无家可归、儿童上学、证件保管、服务入口、隐私、法律援助和反住房污名边界。
- 社会连接与社区归属模板：关系网络、孤独风险、归属感、互助资源、社区参与、服务转介、老年支持、危机发现、隐私和反污名边界。
- 经济安全与时间结构模板：收入稳定性、现金缓冲、社会保护资格、带薪休假、工作时间、无偿照护、时间贫困、金融压力和责任边界。
- 公共福利与服务导航模板：福利类别、资格来源、申请入口、证明材料、身份核验、语言、无障碍、线下替代、等待时间、续期、申诉、人工帮助、数据共享和反程序性排除边界。
- 社区资源导航与社会服务转介模板：需求类型、资源目录来源、更新时间、服务容量、资格口径、地理覆盖、热线/线上/线下入口、转介责任、闭环回访、同意、数据共享、隐私和反服务碎片化边界。
- 金融接入与支付模板：账户可得性、身份要求、费用、支付工具、现金替代路径、数字金融、汇款、信用记录、债务压力、投诉渠道、欺诈风险、数据隐私和反金融排除边界。
- 保险与理赔连续性模板：风险类型、覆盖来源、资格/承保条件、等待期、保费、免赔额、理赔材料、支付时点、申诉路径、监管入口、收入替代比例、保障上限、排除条款和反保险排除边界。
- 食物保障与 WASH 模板：食物可得性、价格冲击、营养风险、儿童发育、食品安全、饮水安全、卫生设施、灾害暴露、服务可及性和本地检测边界。
- 能源与基础公用事业模板：电力可得性、供电稳定性、费用负担、清洁烹饪、室内空气、取暖制冷、关键设备供电、住宅能效、停电韧性和反能源贫困污名边界。
- 气候风险与社区韧性模板：hazard 类型、暴露资产、脆弱人群、预警渠道、撤离/避难、冷却入口、医疗连续性、停电、水食物供应、灾后恢复、公平资源配置和反气候风险污名边界。
- 家庭应急准备模板：hazard 类型、家庭成员、照护对象、宠物、通信计划、集合点、应急物资、药物、医疗设备、电源、水和食物、重要文件、现金、无障碍需求、天气信息入口、演练频率和反个人责任转嫁边界。
- 公共预警与应急通信模板：风险类型、发布机构、警报渠道、覆盖人群、语言和无障碍、确认机制、911/NG911 能力、第一响应者通信、断电/断网备用路径、谣言风险、隐私和本地指挥边界。
- 灾后恢复与个人援助模板：灾害类型、受影响地址、住房状态、文件缺失、恢复中心、临时避难、食物、账单、现金缓冲、贷款风险、保险/赔付、照护和医疗连续性、申请截止、申诉路径和反资格误导边界。
- 免疫与感染监测模板：目标病原、免疫覆盖、监测口径、报告延迟、实验室网络、感染防控、AMR、废水信号、应急触发和权利边界。
- 母婴与早期发展模板：孕产风险、产前产后照护、新生儿、生长标准、营养、响应性照护、早期学习、家庭压力、服务可及性和反监控边界。
- 托育与早期教育模板：儿童年龄、照护时段、费用负担、名额可得性、质量许可、早期学习、特殊需要、照护者劳动条件、父母工作/学习连续性、备用照护、交通和反托育污名边界。
- 法律身份与公民登记模板：出生登记、法律身份、证件可得性、CRVS 覆盖、姓名/性别/国籍变更、迁移状态、服务入口、纠错路径、隐私和反排除边界。
- 司法可及与法律援助模板：问题类型、法律身份、管辖地、费用能力、服务资格、语言、无障碍、证据材料、申诉期限、代理范围、在线/线下入口、隐私、执行路径和反程序性排除边界。
- 公民参与与选举基础设施模板：登记状态、身份要求、投票方式、地点和时间、邮寄/提前投票、无障碍和语言需求、设备标准、权利救济、信息可信度、观察和审计、隐私、反压迫和反党派操控边界。
- 迁移与人道服务连续性模板：迁移状态、流离失所类型、身份文件、庇护或保护需求、住房/营地/收容、医疗、教育、现金/物资、法律援助、语言、数据敏感性、跨机构协调、退出路径和反排除边界。
- 数字接入与公共服务模板：网络可得性、设备、费用、数字身份、账号恢复、语言、无障碍、信息素养、线下替代路径、公共图书馆和反数字排除边界。
- 个人数字安全与身份盗用恢复模板：账号类型、认证方式、恢复路径、备份联系方式、钓鱼/诈骗风险、身份盗用信号、举报入口、信用修复、服务中断影响、照护者协助、隐私和反受害者归因边界。
- 语言可达与清晰沟通模板：目标人群、语言需求、阅读水平、术语负担、翻译口译、告知材料、表单说明、健康素养、认知负担、用户测试、人工帮助和反语言排除边界。
- 交通可达与日常移动模板：目的地类型、距离、时间成本、费用、服务频率、换乘、可靠性、安全、无障碍、辅助交通、灾害撤离、照护出行和反交通贫困边界。
- 医疗可及性与基本服务模板：保险或支付路径、费用负担、第一接触入口、等待时间、距离、语言、基本药物、医护 workforce、转诊、质量差异、急慢病连续性和反医疗排除边界。
- 远程医疗与居家监测模板：服务类型、适用场景、线下替代、设备/宽带要求、身份核验、支付覆盖、数据流、临床责任、升级路径、语言和无障碍、照护者参与、隐私安全和反数字医疗排除边界。
- 药品可及与用药安全模板：药品名称、适应证边界、可得性、供应风险、费用/覆盖、替代路径、标签说明、相互作用、用药错误风险、患者理解、药房渠道、短缺处置和反自行用药边界。
- 心理健康与成瘾照护模板：服务入口、危机支持、诊断边界、治疗连续性、成瘾治疗、过量预防、同伴支持、隐私、非强制原则、家庭支持和反污名边界。
- 人身安全与应急响应模板：伤害类型、暴力风险、儿童逆境、危机入口、急救可达、灾害暴露、恢复支持、隐私、反污名和反惩罚性评分边界。
- 建成环境与交通暴露模板：住房风险、街道连接、主动交通、空气质量、热风险、道路安全、可达性、公平影响和本地审查边界。
- 学习与技能形成模板：学习目标、前置知识、反馈机制、练习设计、迁移场景、技能地图、机会结构和评价边界。
- 就业服务与职业转换模板：目标职业、现有技能、技能缺口、资格证书、培训资金、公共就业服务、学徒制、岗位可达性、就业无障碍、照护/交通约束、收入风险、劳动权益和反自动筛选边界。
- 照护与长期服务模板：照护对象、家庭照护者负担、服务资格、居家社区支持、照护协调、喘息服务、质量信息、退出权和责任边界。
- 人机协作子域或专题页的条目模板：任务、负荷、风险、反馈、恢复和审计。
- 记忆编辑子域内部的伦理审查模板：主体性、真实性、同意、退出、神经数据和长期伤害。
- 组织级 Human Infra 审查模板：排班、疲劳、交接、告警、事件学习、强行动项和安全文化测量。

## 来源清单

- Bryan Johnson Blueprint Protocol: https://protocol.bryanjohnson.com/
- Apple Heart Study, NEJM: https://www.nejm.org/doi/full/10.1056/NEJMoa1901183
- Apple Heart Study, PubMed: https://pubmed.ncbi.nlm.nih.gov/31722151/
- Stanford Medicine Apple Heart Study release: https://med.stanford.edu/news/all-news/2019/11/through-apple-heart-study--stanford-medicine-researchers-show-we.html
- NIOSH Total Worker Health Program: https://www.cdc.gov/niosh/twh/programs/index.html
- NIOSH Total Worker Health overview: https://www.cdc.gov/niosh/twh/index.html
- WHO Global Patient Safety Action Plan 2021-2030: https://www.who.int/publications/i/item/9789240032705
- To Err is Human, NCBI Bookshelf: https://www.ncbi.nlm.nih.gov/books/NBK225182/
- AHRQ TeamSTEPPS: https://www.ahrq.gov/teamstepps-program/index.html
- AHRQ Comprehensive Unit-based Safety Program: https://www.ahrq.gov/hai/cusp/index.html
- AHRQ PSNet High Reliability primer: https://psnet.ahrq.gov/primer/high-reliability
- AHRQ PSNet Root Cause Analysis primer: https://psnet.ahrq.gov/primer/root-cause-analysis
- AHRQ Surveys on Patient Safety Culture: https://www.ahrq.gov/sops/index.html
- IHI RCA2: https://www.ihi.org/resources/tools/rca2-improving-root-cause-analyses-and-actions-prevent-harm
- NIOSH Fatigue at Work: https://www.cdc.gov/niosh/bulletin/2023/fatigue.html
- OSHA Worker Fatigue: https://www.osha.gov/worker-fatigue
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
- Synchron COMMAND Study, ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT05035823
- FDA Investigational Device Exemption overview: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/investigational-device-exemption-ide
- FDA implanted BCI guidance: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/implanted-brain-computer-interface-bci-devices-patients-paralysis-or-amputation-non-clinical-testing
- Neuroethics Guiding Principles for the NIH BRAIN Initiative, PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC6297371/
- Neuroethics Guiding Principles for the NIH BRAIN Initiative, PubMed: https://pubmed.ncbi.nlm.nih.gov/30541767/
- OECD Recommendation on Responsible Innovation in Neurotechnology: https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0457
- UNESCO Ethics of Neurotechnology: https://www.unesco.org/en/ethics-neurotech
- UNESCO Recommendation on the Ethics of Neurotechnology: https://www.unesco.org/en/ethics-neurotech/recommendation
- Ethical Issues in Memory Modification Technology, PubMed: https://pubmed.ncbi.nlm.nih.gov/39417981/
- Neuromodulation and memory ethics, PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC10764565/
- The ethics of molecular memory modification, PubMed: https://pubmed.ncbi.nlm.nih.gov/25552663/
- Does Memory Modification Threaten Our Authenticity, PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC3189328/
- NASA Human Systems Integration lessons: https://www.nasa.gov/humans-in-space/commercial-space/leo-economy/nasa-shares-lessons-human-systems-integration/
- Nancy Leveson, Engineering a Safer World: https://direct.mit.edu/books/oa-monograph/2908/Engineering-a-Safer-WorldSystems-Thinking-Applied
- Lopez-Otin et al., The Hallmarks of Aging: https://pmc.ncbi.nlm.nih.gov/articles/PMC3836174/
- Hallmarks of Aging, PubMed: https://pubmed.ncbi.nlm.nih.gov/23746838/
- McEwen and Stellar, allostatic load: https://pubmed.ncbi.nlm.nih.gov/8379800/
- McEwen, stress and allostatic load review: https://pubmed.ncbi.nlm.nih.gov/9629234/
- Cohen et al., Perceived Stress Scale, PubMed: https://pubmed.ncbi.nlm.nih.gov/6668417/
- WHO burn-out occupational phenomenon in ICD-11: https://www.who.int/news/item/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases
- WHO Social Determinants of Health: https://www.who.int/news-room/fact-sheets/detail/social-determinants-of-health
- Healthy People 2030 Social Determinants of Health: https://odphp.health.gov/healthypeople/priority-areas/social-determinants-health
- CDC/ATSDR Social Vulnerability Index: https://www.atsdr.cdc.gov/place-health/php/svi/index.html
- CDC/ATSDR Environmental Justice Index: https://www.atsdr.cdc.gov/place-health/php/eji/index.html
- CDC PLACES: https://www.cdc.gov/places/index.html
- USDA Food Access Research Atlas: https://www.ers.usda.gov/data-products/food-access-research-atlas
- CMS Accountable Health Communities Model: https://www.cms.gov/priorities/innovation/innovation-models/ahcm
- UN-Habitat Housing: https://unhabitat.org/topic/housing
- HUD Annual Homeless Assessment Report: https://www.huduser.gov/portal/datasets/ahar.html
- U.S. Census American Housing Survey: https://www.census.gov/programs-surveys/ahs.html
- U.S. Census Household Pulse Survey: https://www.census.gov/programs-surveys/household-pulse-survey.html
- Eviction Lab: https://evictionlab.org/
- Eviction Lab Eviction Tracking System: https://evictionlab.org/eviction-tracking/
- WHO social connection report: https://www.who.int/publications/i/item/978240112360
- WHO social isolation and loneliness: https://www.who.int/teams/social-determinants-of-health/demographic-change-and-healthy-ageing/social-isolation-and-loneliness
- CDC Social Connectedness: https://www.cdc.gov/social-connectedness/about/index.html
- CDC Social Connectedness risk factors: https://www.cdc.gov/social-connectedness/risk-factors/index.html
- Healthy People 2030 Social and Community Context: https://odphp.health.gov/healthypeople/objectives-and-data/browse-objectives/social-and-community-context
- National Academies social isolation and loneliness report: https://www.nationalacademies.org/projects/HMD-HSP-17-25/publication/25663
- NHS England social prescribing: https://www.england.nhs.uk/personalisedcare/social-prescribing/
- ILO social protection: https://www.ilo.org/topics/social-protection
- ILO World Social Protection Report 2024-26: https://www.ilo.org/publications/flagship-reports/world-social-protection-report-2024-26-universal-social-protection-climate
- ILO Social Protection Floors Recommendation 2012 No. 202: https://www.ilo.org/resource/news/ilo-social-protection-floors-recommendation-2012-no-202
- World Bank Universal Social Protection: https://www.worldbank.org/en/topic/socialprotection/brief/universal-social-protection
- World Bank ASPIRE: https://www.worldbank.org/en/data/datatopics/aspire
- U.S. DOL paid leave: https://www.dol.gov/agencies/wb/featured-paid-leave
- U.S. DOL Family and Medical Leave Act: https://www.dol.gov/agencies/whd/fmla
- UN time-use statistics: https://unstats.un.org/unsd/gender/timeuse/
- ILO working time and work organization: https://www.ilo.org/topics/working-time-and-work-organization
- Federal Reserve Survey of Household Economics and Decisionmaking: https://www.federalreserve.gov/consumerscommunities/shed.htm
- CFPB financial well-being: https://www.consumerfinance.gov/consumer-tools/financial-well-being/
- IRS Earned Income Tax Credit: https://www.irs.gov/credits-deductions/individuals/earned-income-tax-credit-eitc
- USA.gov Benefit Finder: https://www.usa.gov/benefit-finder
- USAGov food assistance: https://www.usa.gov/food-help
- Performance.gov Federal Customer Experience: https://www.performance.gov/cx/
- Medicaid eligibility: https://www.medicaid.gov/eligibility
- HealthCare.gov Medicaid and CHIP: https://www.healthcare.gov/medicaid-chip/
- Social Security Supplemental Security Income: https://www.ssa.gov/ssi
- ACF Low Income Home Energy Assistance Program: https://www.acf.hhs.gov/ocs/low-income-home-energy-assistance-program-liheap
- Moynihan / Herd / Harvey administrative burden article: https://doi.org/10.1093/jopart/muu009
- Herd / Moynihan Administrative Burden book: https://www.russellsage.org/publications/administrative-burden
- 211: https://www.211.org/
- Open Referral Human Services Data Specification: https://docs.openreferral.org/en/latest/hsds/
- Gravity Project: https://thegravityproject.net/
- World Bank Financial Inclusion: https://www.worldbank.org/en/topic/financialinclusion
- World Bank Global Findex Database: https://www.worldbank.org/en/publication/globalfindex
- World Bank Digital Financial Services: https://www.worldbank.org/en/topic/financialinclusion/brief/digital-financial-services
- World Bank Payment Systems: https://www.worldbank.org/en/topic/financialinclusion/brief/payment-systems
- FDIC National Survey of Unbanked and Underbanked Households: https://www.fdic.gov/household-survey
- FDIC Money Smart: https://www.fdic.gov/resources/consumers/money-smart/
- CFPB Consumer Complaint Database: https://www.consumerfinance.gov/data-research/consumer-complaints/
- CFPB Consumer Credit Trends: https://www.consumerfinance.gov/data-research/consumer-credit-trends/
- Federal Reserve Payments Study: https://www.federalreserve.gov/paymentsystems/fr-payments-study.htm
- NAIC consumer resources: https://content.naic.org/consumer
- NAIC flood insurance: https://content.naic.org/cipr-topics/flood-insurance
- USA.gov health insurance: https://www.usa.gov/health-insurance
- USA.gov unemployment benefits: https://www.usa.gov/unemployment-benefits
- USA.gov workers' compensation: https://www.usa.gov/workers-compensation
- Benefits.gov Disability Assistance: https://www.benefits.gov/categories/Disability%20Assistance
- FDIC deposit insurance: https://www.fdic.gov/resources/deposit-insurance/
- Pension Benefit Guaranty Corporation: https://www.pbgc.gov/
- World Bank Disaster Risk Financing and Insurance: https://www.worldbank.org/en/topic/disasterriskmanagement/brief/disaster-risk-financing-and-insurance
- FAO State of Food Security and Nutrition in the World: https://www.fao.org/publications/fao-flagship-publications/the-state-of-food-security-and-nutrition-in-the-world/en
- FAOSTAT: https://www.fao.org/faostat/en/
- WFP HungerMap LIVE: https://hungermap.wfp.org/
- WHO healthy diet: https://www.who.int/news-room/fact-sheets/detail/healthy-diet
- WHO malnutrition: https://www.who.int/news-room/fact-sheets/detail/malnutrition
- WHO food safety: https://www.who.int/news-room/fact-sheets/detail/food-safety
- WHO/UNICEF Joint Monitoring Programme for Water Supply, Sanitation and Hygiene: https://washdata.org/
- WHO/UNICEF JMP data: https://washdata.org/data
- WHO drinking-water: https://www.who.int/news-room/fact-sheets/detail/drinking-water
- WHO sanitation: https://www.who.int/news-room/fact-sheets/detail/sanitation
- World Bank Energy: https://www.worldbank.org/en/topic/energy
- IEA access to electricity: https://www.iea.org/reports/sdg7-data-and-projections/access-to-electricity
- IEA access to clean cooking: https://www.iea.org/reports/sdg7-data-and-projections/access-to-clean-cooking
- WHO household air pollution: https://www.who.int/news-room/fact-sheets/detail/household-air-pollution-and-health
- DOE Low-Income Energy Affordability Data Tool: https://www.energy.gov/scep/slsc/lead-tool
- DOE Weatherization Assistance Program: https://www.energy.gov/scep/wap/weatherization-assistance-program
- DOE Energy Saver weatherization: https://www.energy.gov/energysaver/weatherize
- EPA Indoor Air Quality: https://www.epa.gov/indoor-air-quality-iaq
- IPCC AR6 Synthesis Report: https://www.ipcc.ch/report/ar6/syr/
- WMO Early Warnings for All: https://wmo.int/activities/early-warnings-all
- U.S. Climate Resilience Toolkit: https://toolkit.climate.gov/
- Climate Mapping for Resilience and Adaptation: https://resilience.climate.gov/
- NOAA Billion-Dollar Weather and Climate Disasters: https://www.ncei.noaa.gov/access/billions/
- NOAA Climate Data Records: https://www.ncei.noaa.gov/products/climate-data-records
- CDC Climate and Health: https://www.cdc.gov/climate-health/
- CDC Heat and Health: https://www.cdc.gov/heat-health/
- Red Cross how to prepare for emergencies: https://www.redcross.org/get-help/how-to-prepare-for-emergencies.html
- Red Cross survival kit supplies: https://www.redcross.org/get-help/how-to-prepare-for-emergencies/survival-kit-supplies.html
- Red Cross make a plan: https://www.redcross.org/get-help/how-to-prepare-for-emergencies/make-a-plan.html
- Red Cross emergency apps: https://www.redcross.org/get-help/how-to-prepare-for-emergencies/mobile-apps.html
- CDC Prepare Your Health: https://www.cdc.gov/prepare-your-health/
- CDC Natural Disasters safety: https://www.cdc.gov/natural-disasters/safety/
- NOAA Weather-Ready Nation: https://www.weather.gov/wrn/
- FEMA Integrated Public Alert and Warning System: https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system
- FCC Wireless Emergency Alerts: https://www.fcc.gov/consumers/guides/wireless-emergency-alerts-wea
- FCC Emergency Alert System: https://www.fcc.gov/emergency-alert-system
- NOAA Weather Radio: https://www.weather.gov/nwr/
- Ready.gov Alerts and Warnings: https://www.ready.gov/alerts
- 911.gov: https://www.911.gov/
- Next Generation 911: https://www.911.gov/issues/ng911
- FirstNet Authority: https://www.firstnet.gov/
- USA.gov disaster: https://www.usa.gov/disaster
- USA.gov disaster assistance: https://www.usa.gov/disaster-assistance
- USA.gov disaster financial help: https://www.usa.gov/disaster-financial-help
- USA.gov disaster food help: https://www.usa.gov/disaster-food-help
- USA.gov disaster help with bills: https://www.usa.gov/disaster-help-with-bills
- FEMA Disaster Recovery Center Locator: https://egateway.fema.gov/ESF6/DRCLocator
- SBA Disaster Assistance: https://www.sba.gov/funding-programs/disaster-assistance
- Benefits.gov Disaster Relief: https://www.benefits.gov/categories/Disaster%20Relief
- Red Cross find an open shelter: https://www.redcross.org/get-help/disaster-relief-and-recovery-services/find-an-open-shelter.html
- WHO vaccines and immunization: https://www.who.int/health-topics/vaccines-and-immunization
- WHO Immunization Agenda 2030: https://www.who.int/teams/immunization-vaccines-and-biologicals/strategies/ia2030
- CDC Vaccines and Immunizations: https://www.cdc.gov/vaccines/
- CDC National Notifiable Diseases Surveillance System: https://www.cdc.gov/nndss/
- WHO Global Influenza Surveillance and Response System: https://www.who.int/initiatives/global-influenza-surveillance-and-response-system
- WHO International Health Regulations: https://www.who.int/health-topics/international-health-regulations
- WHO emergencies overview: https://www.who.int/emergencies/overview
- CDC emergency preparedness and response: https://www.cdc.gov/emergency/
- CDC readiness and response: https://www.cdc.gov/readiness/php/index.html
- WHO infection prevention and control: https://www.who.int/teams/integrated-health-services/infection-prevention-control
- CDC National Healthcare Safety Network: https://www.cdc.gov/nhsn/
- WHO antimicrobial resistance: https://www.who.int/news-room/fact-sheets/detail/antimicrobial-resistance
- WHO Global Antimicrobial Resistance and Use Surveillance System: https://www.who.int/initiatives/glass
- WHO One Health: https://www.who.int/health-topics/one-health
- CDC National Wastewater Surveillance System: https://www.cdc.gov/nwss/
- WHO maternal health: https://www.who.int/health-topics/maternal-health
- WHO maternal mortality: https://www.who.int/news-room/fact-sheets/detail/maternal-mortality
- WHO antenatal care recommendations: https://www.who.int/publications/i/item/9789241549912
- WHO intrapartum care recommendations: https://www.who.int/publications/i/item/9789241550215
- WHO newborn mortality: https://www.who.int/news-room/fact-sheets/detail/newborn-mortality
- WHO child health: https://www.who.int/health-topics/child-health
- WHO Child Growth Standards: https://www.who.int/tools/child-growth-standards
- Nurturing Care Framework: https://www.who.int/publications/i/item/9789241514064
- Nurturing Care Framework site: https://nurturing-care.org/
- UN Legal Identity Agenda: https://unstats.un.org/legal-identity-agenda/
- UN Statistics Civil Registration and Vital Statistics: https://unstats.un.org/unsd/demographic-social/crvs/
- WHO Civil Registration and Vital Statistics: https://www.who.int/data/data-collection-tools/civil-registration-and-vital-statistics-%28crvs%29
- World Bank Identification for Development global dataset: https://datacatalog.worldbank.org/search/dataset/0040787/identification-for-development-id4d-global-dataset
- UNICEF birth registration: https://www.unicef.org/stories/birth-registration
- UN Sustainable Development Goal 16: https://sdgs.un.org/goals/goal16
- World Justice Project Rule of Law Index: https://worldjusticeproject.org/rule-of-law-index/
- Legal Services Corporation Justice Gap: https://justicegap.lsc.gov/
- Legal Services Corporation Justice Gap Research: https://www.lsc.gov/initiatives/justice-gap-research
- U.S. DOJ Office for Access to Justice: https://www.justice.gov/atj
- ABA Free Legal Answers: https://abafreelegalanswers.org/
- USA.gov voter registration: https://www.usa.gov/register-to-vote
- EAC voters: https://www.eac.gov/voters
- EAC National Mail Voter Registration Form: https://www.eac.gov/voters/national-mail-voter-registration-form
- EAC Voluntary Voting System Guidelines: https://www.eac.gov/voting-equipment/voluntary-voting-system-guidelines
- NIST voting: https://www.nist.gov/itl/voting
- DOJ Voting Section: https://www.justice.gov/crt/voting-section
- ADA voting: https://www.ada.gov/topics/voting/
- EAC voting accessibility: https://www.eac.gov/election-officials/voting-accessibility
- International IDEA Voter Turnout Database: https://www.idea.int/data-tools/data/voter-turnout-database
- ACE Electoral Knowledge Network: https://aceproject.org/
- OSCE ODIHR elections: https://www.osce.org/odihr/elections
- UN Global Compact for Migration: https://refugeesmigrants.un.org/migration-compact
- IOM World Migration Report: https://worldmigrationreport.iom.int/
- UNHCR Operational Data Portal: https://data.unhcr.org/en/situations
- WHO Health and Migration Programme: https://www.who.int/teams/health-and-migration-programme
- IDMC Global Report on Internal Displacement 2025: https://www.internal-displacement.org/global-report/grid2025/
- OCHA Humanitarian Data Exchange: https://data.humdata.org/
- ReliefWeb: https://reliefweb.int/
- INEE Minimum Standards: https://inee.org/minimum-standards
- Inter-Agency Standing Committee: https://interagencystandingcommittee.org/
- Global Shelter Cluster: https://sheltercluster.org/
- ITU ICT statistics: https://www.itu.int/itu-d/reports/statistics/
- World Bank Digital Development: https://www.worldbank.org/en/topic/digitaldevelopment
- NTIA Digital Nation Data Explorer: https://www.ntia.gov/data/explorer
- U.S. Census computer and internet use: https://www.census.gov/topics/population/computer-internet.html
- NIST Identity and Access Management: https://www.nist.gov/identity-and-access-management
- NIST Digital Identity Guidelines SP 800-63-4: https://pages.nist.gov/800-63-4/
- Login.gov: https://www.login.gov/
- Login.gov help: https://www.login.gov/help/
- Login.gov policy: https://www.login.gov/policy/
- FTC scams: https://consumer.ftc.gov/scams
- FTC phishing scams: https://consumer.ftc.gov/articles/how-recognize-avoid-phishing-scams
- IdentityTheft.gov: https://www.identitytheft.gov/
- ReportFraud.ftc.gov: https://reportfraud.ftc.gov/
- FBI Internet Crime Complaint Center: https://www.ic3.gov/
- Digital.gov: https://digital.gov/
- U.S. Web Design System: https://designsystem.digital.gov/
- UNESCO Media and Information Literacy: https://www.unesco.org/en/media-information-literacy
- IMLS Public Libraries Survey: https://www.imls.gov/research-evaluation/surveys/public-libraries-survey-pls
- IMLS Search & Compare: https://www.imls.gov/search-compare
- PlainLanguage.gov: https://www.plainlanguage.gov/
- Digital.gov plain language guide: https://digital.gov/guides/plain-language
- Digital.gov plain language principles: https://digital.gov/guides/plain-language/principles
- Limited English Proficiency federal resources: https://www.lep.gov/
- National CLAS Standards: https://thinkculturalhealth.hhs.gov/clas
- CDC health literacy: https://www.cdc.gov/health-literacy/php/about/index.html
- CDC Clear Communication Index: https://www.cdc.gov/ccindex/index.html
- W3C WAI cognitive accessibility: https://www.w3.org/WAI/cognitive/
- World Bank Transport: https://www.worldbank.org/en/topic/transport
- FTA National Transit Database: https://www.transit.dot.gov/ntd
- National Household Travel Survey: https://nhts.ornl.gov/
- USDOT Equitable Transportation Community Explorer RFI: https://www.federalregister.gov/documents/2023/02/21/2023-03396/request-for-information-on-us-dot-equitable-transportation-community-explorer-etce-tool-and-index
- FTA ADA guidance: https://www.transit.dot.gov/regulations-and-guidance/civil-rights-ada/ada-guidance
- FTA ADA frequently asked questions: https://www.transit.dot.gov/regulations-and-guidance/civil-rights-ada/frequently-asked-questions
- WHO Universal Health Coverage: https://www.who.int/health-topics/universal-health-coverage
- WHO Primary Health Care: https://www.who.int/health-topics/primary-health-care
- WHO Essential Medicines Lists: https://www.who.int/groups/expert-committee-on-selection-and-use-of-essential-medicines/essential-medicines-lists
- WHO Medication Without Harm: https://www.who.int/initiatives/medication-without-harm
- FDA Drug Shortages: https://www.fda.gov/drugs/drug-safety-and-availability/drug-shortages
- FDA National Drug Code Directory: https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory
- DailyMed: https://dailymed.nlm.nih.gov/dailymed/
- MedlinePlus Medicines: https://medlineplus.gov/medicines.html
- Medicare prescription drug coverage: https://www.medicare.gov/drug-coverage-part-d
- CDC Medication Safety Program: https://www.cdc.gov/medication-safety/
- WHO Health Workforce: https://www.who.int/health-topics/health-workforce
- World Bank Universal Health Coverage: https://www.worldbank.org/en/topic/universalhealthcoverage
- CDC access to health care: https://www.cdc.gov/nchs/fastats/access-to-health-care.htm
- CDC health insurance coverage: https://www.cdc.gov/nchs/fastats/health-insurance.htm
- AHRQ Data Tools: https://datatools.ahrq.gov/
- Telehealth.HHS.gov: https://telehealth.hhs.gov/
- HHS telehealth and remote patient monitoring: https://telehealth.hhs.gov/providers/best-practice-guides/telehealth-and-remote-patient-monitoring
- HRSA Telehealth: https://www.hrsa.gov/telehealth
- CMS Medicare telehealth coverage: https://www.cms.gov/medicare/coverage/telehealth
- Medicare telehealth: https://www.medicare.gov/coverage/telehealth
- WHO World Mental Health Report: https://www.who.int/publications/i/item/9789240049338
- WHO Mental Health Gap Action Programme: https://www.who.int/teams/mental-health-and-substance-use/treatment-care/mental-health-gap-action-programme
- WHO Mental Health Atlas 2020: https://www.who.int/publications/i/item/9789240036703
- FindTreatment.gov: https://findtreatment.gov/
- NIMH mental illness statistics: https://www.nimh.nih.gov/health/statistics/mental-illness
- CDC overdose prevention: https://www.cdc.gov/overdose-prevention/
- 988 Suicide & Crisis Lifeline: https://988lifeline.org/
- WHO injuries and violence: https://www.who.int/news-room/fact-sheets/detail/injuries-and-violence
- WHO violence: https://www.who.int/health-topics/violence
- WHO violence against women: https://www.who.int/news-room/fact-sheets/detail/violence-against-women
- CDC Injury Center: https://www.cdc.gov/injury/
- CDC WISQARS: https://www.cdc.gov/injury/wisqars/
- CDC Violence Prevention: https://www.cdc.gov/violence-prevention/
- CDC Adverse Childhood Experiences: https://www.cdc.gov/aces/about/index.html
- CDC Suicide Prevention: https://www.cdc.gov/suicide/
- WHO Emergency Care: https://www.who.int/health-topics/emergency-care
- CDC Natural Disasters and Severe Weather: https://www.cdc.gov/natural-disasters/
- CDC Pregnancy Risk Assessment Monitoring System: https://www.cdc.gov/prams/
- CDC Child Development: https://www.cdc.gov/child-development/
- CDC Learn the Signs. Act Early.: https://www.cdc.gov/ncbddd/actearly/index.html
- DHS Program: https://dhsprogram.com/
- World Bank Early Childhood Development: https://www.worldbank.org/en/topic/earlychildhooddevelopment
- Healthy People pregnancy and childbirth objectives: https://odphp.health.gov/healthypeople/objectives-and-data/browse-objectives/pregnancy-and-childbirth
- World Bank Childcare: https://www.worldbank.org/en/topic/education/brief/childcare
- ILO Care Work and Care Jobs: https://www.ilo.org/publications/major-publications/care-work-and-care-jobs-future-decent-work
- U.S. DOL childcare: https://www.dol.gov/agencies/wb/topics/childcare
- ACF Office of Child Care: https://www.acf.hhs.gov/occ
- Child Care and Development Fund: https://www.acf.hhs.gov/occ/programs/ccdf
- ChildCare.gov: https://childcare.gov/
- National Survey of Early Care and Education: https://www.acf.hhs.gov/opre/project/national-survey-early-care-and-education-2019-2017-2022
- U.S. Census child care: https://www.census.gov/topics/families/child-care.html
- CDC positive parenting tips: https://www.cdc.gov/child-development/positive-parenting-tips/index.html
- National Academies How People Learn II: https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures
- IES What Works Clearinghouse: https://ies.ed.gov/ncee/wwc/
- UNESCO Institute for Statistics: https://www.uis.unesco.org/en
- UNESCO Institute for Lifelong Learning: https://www.uil.unesco.org/en
- O*NET Center overview: https://www.onetcenter.org/overview.html
- World Bank Human Capital Project: https://www.worldbank.org/en/publication/human-capital
- World Bank Jobs and Development: https://www.worldbank.org/en/topic/jobsanddevelopment
- ILO Employment Promotion: https://www.ilo.org/topics/employment-promotion
- U.S. DOL Employment and Training Administration: https://www.dol.gov/agencies/eta
- Workforce Innovation and Opportunity Act: https://www.dol.gov/agencies/eta/wioa
- American Job Centers: https://www.dol.gov/agencies/eta/american-job-centers
- Apprenticeship.gov: https://www.apprenticeship.gov/
- O*NET Online: https://www.onetonline.org/
- My Next Move: https://www.mynextmove.org/
- Job Accommodation Network: https://askjan.org/
- WHO Housing and health guidelines: https://www.who.int/publications/i/item/9789241550376
- WHO Urban health: https://www.who.int/health-topics/urban-health
- CDC Built Environment Assessment Tool: https://www.cdc.gov/physical-activity/php/built-environment-assessment/index.html
- CDC Active Communities Tool: https://www.cdc.gov/active-communities-tool/php/about/index.html
- CDC community design strategies for physical activity: https://www.cdc.gov/physical-activity/php/strategies/increasing-physical-activity-through-community-design-prevention-strategies.html
- WHO Global Air Quality Guidelines: https://www.who.int/publications/i/item/9789240034228
- AirNow: https://www.airnow.gov/
- CDC/ATSDR Heat and Health Index: https://www.atsdr.cdc.gov/place-health/php/hhi/index.html
- CDC Tracking heat events: https://www.cdc.gov/environmental-health-tracking/php/data-research/tracking-heat-events.html
- WHO Global status report on road safety 2023: https://www.who.int/publications/i/item/9789240086517
- National Strategy to Support Family Caregivers, Federal Register notice: https://www.federalregister.gov/documents/2022/10/06/2022-21697/2022-national-strategy-to-support-family-caregivers-available-for-public-comments
- CDC Caregiving: https://www.cdc.gov/caregiving/index.html
- National Academies Families Caring for an Aging America, NCBI Bookshelf: https://www.ncbi.nlm.nih.gov/books/NBK396398/
- Medicaid Home & Community-Based Services: https://www.medicaid.gov/medicaid/home-community-based-services/index.html
- Medicare home health services: https://www.medicare.gov/coverage/home-health-services
- Medicare hospice care: https://www.medicare.gov/coverage/hospice-care
- Medicare Care Compare: https://www.medicare.gov/care-compare/
- AHRQ Care Coordination: https://www.ahrq.gov/ncepcr/care/coordination.html
- ACL Eldercare Locator: https://eldercare.acl.gov/Public/Index.aspx
- WHO framework for an integrated continuum of long-term care: https://www.who.int/publications/i/item/9789240038844
- Gary Wolf / Quantified Self background: https://quantifiedself.com/gary-wolf-bio/
- NIA Interventions Testing Program: https://www.nia.nih.gov/research/dab/interventions-testing-program-itp
- JAX Interventions Testing Program: https://www.jax.org/research-and-faculty/research-centers/aging-center/research/itp
- NIA Caenorhabditis Intervention Testing Program: https://www.nia.nih.gov/research/dab/caenorhabditis-intervention-testing-program-citp
- NIA CITP resource page: https://www.nia.nih.gov/research/resource/caenorhabditis-interventions-testing-program-citp
- CITP consortium: https://citpaging.org/
- NIH GeroScience Interest Group: https://oir.nih.gov/sigs/geroscience-interest-group-gsig
- NIA Translational Geroscience Network paper, PubMed: https://pubmed.ncbi.nlm.nih.gov/38650350/
- DrugAge database: https://genomics.senescence.info/drugs/
- GenAge database: https://genomics.senescence.info/genes/
- LongevityMap database: https://genomics.senescence.info/longevity/
- CellAge database: https://genomics.senescence.info/cells/
- NIH All of Us Research Program: https://allofus.nih.gov/
- All of Us Researcher Workbench: https://workbench.researchallofus.org/
- UK Biobank: https://www.ukbiobank.ac.uk/
- CDC National Health and Nutrition Examination Survey: https://www.cdc.gov/nchs/nhanes/index.html
- NHLBI Framingham Heart Study: https://www.nhlbi.nih.gov/science/framingham-heart-study-fhs
- GTEx Portal: https://gtexportal.org/home/
- NIH / NHGRI Genotype-Tissue Expression Project: https://www.genome.gov/Funded-Programs-Projects/Genotype-Tissue-Expression-Project
- GTEx Consortium atlas, PubMed: https://pubmed.ncbi.nlm.nih.gov/32913098/
- ClinicalTrials.gov: https://clinicaltrials.gov/
- FDA Real-World Evidence: https://www.fda.gov/science-research/science-and-research-special-topics/real-world-evidence
- PCORnet: https://pcornet.org/
- OHDSI: https://www.ohdsi.org/
- OMOP Common Data Model: https://ohdsi.github.io/CommonDataModel/
- HL7 FHIR: https://hl7.org/fhir/
- ONC Get It, Check It, Use It: https://www.healthit.gov/how-to-get-your-health-record/
- ONC United States Core Data for Interoperability: https://www.healthit.gov/isp/united-states-core-data-interoperability-uscdi
- ONC TEFCA: https://www.healthit.gov/topic/interoperability/policy/trusted-exchange-framework-and-common-agreement-tefca
- CMS Interoperability and Patient Access Final Rule: https://www.cms.gov/priorities/key-initiatives/burden-reduction/interoperability/policies-and-regulations/cms-interoperability-and-patient-access-final-rule-cms-9115-f
- CMS Blue Button API: https://bluebutton.cms.gov/
- HL7 SMART App Launch: https://hl7.org/fhir/smart-app-launch/
- FDA Digital Health Center of Excellence: https://www.fda.gov/medical-devices/digital-health-center-excellence
- NICE Evidence Standards Framework for Digital Health Technologies: https://www.nice.org.uk/what-nice-does/digital-health/evidence-standards-framework-esf-for-digital-health-technologies
- WHO guideline on digital interventions for health system strengthening: https://www.who.int/publications/i/item/9789241550505
- HHS HIPAA Privacy Rule: https://www.hhs.gov/hipaa/for-professionals/privacy/index.html
- HHS Common Rule: https://www.hhs.gov/ohrp/regulations-and-policy/regulations/common-rule/index.html
- NIST Privacy Framework: https://www.nist.gov/privacy-framework
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- NIH Genomic Data Sharing Policy: https://sharing.nih.gov/genomic-data-sharing-policy
- GA4GH Framework for Responsible Sharing of Genomic and Health-Related Data: https://www.ga4gh.org/product/framework-for-responsible-sharing-of-genomic-and-health-related-data/
- ONC Privacy and Security: https://healthit.gov/privacy-security/
- ONC Information Blocking: https://healthit.gov/information-blocking/
- PROMIS, HealthMeasures: https://www.healthmeasures.net/explore-measurement-systems/promis
- WHO International Classification of Functioning, Disability and Health: https://www.who.int/standards/classifications/international-classification-of-functioning-disability-and-health
- EuroQol EQ-5D instruments: https://euroqol.org/information-and-support/euroqol-instruments/
- ICHOM patient-centered outcome measures: https://www.ichom.org/patient-centered-outcome-measures/
- NCI PRO-CTCAE: https://healthcaredelivery.cancer.gov/pro-ctcae/
- WHOQOL: https://www.who.int/tools/whoqol
- CDC Healthy Days Methods and Measures: https://stacks.cdc.gov/view/cdc/6406
- RAND 36-Item Short Form Survey: https://www.rand.org/health-care/surveys_tools/mos/36-item-short-form.html
- WHO Rehabilitation: https://www.who.int/news-room/fact-sheets/detail/rehabilitation
- WHO Rehabilitation 2030: https://www.who.int/initiatives/rehabilitation-2030
- WHO/UNICEF Global report on assistive technology: https://www.who.int/publications/i/item/9789240049451
- WHO Priority Assistive Products List: https://www.who.int/publications/i/item/priority-assistive-products-list
- W3C Web Content Accessibility Guidelines 2.2: https://www.w3.org/TR/WCAG22/
- W3C WAI WCAG overview: https://www.w3.org/WAI/standards-guidelines/wcag/
- U.S. Access Board Section 508 ICT standards: https://www.access-board.gov/ict/
- ADA.gov Effective Communication: https://www.ada.gov/resources/effective-communication/
- IHME Global Burden of Disease: https://www.healthdata.org/research-analysis/gbd
- IHME GBD Compare: https://vizhub.healthdata.org/gbd-compare/
- WHO Global Health Estimates: https://www.who.int/data/global-health-estimates
- WHO cost-effectiveness portal: https://www.who.int/universal-health-coverage/compendium/cost-effectiveness-portal
- WHO-CHOICE frequently asked questions: https://www.who.int/news-room/questions-and-answers/item/who-choice-frequently-asked-questions
- NICE technology appraisal guidance: https://www.nice.org.uk/what-nice-does/our-guidance/about-technology-appraisal-guidance
- NICE health technology evaluations manual: https://www.nice.org.uk/process/pmg36
- ICER value assessment framework: https://icer.org/assessment/value-assessment-framework-2020/
- ICER QALY and evLYG explainer: https://icer.org/our-approach/methods-process/cost-effectiveness-the-qaly-and-the-evlyg/
- CMS Value-Based Programs: https://www.cms.gov/medicare/quality/value-based-programs
- AHRQ Medical Expenditure Panel Survey: https://meps.ahrq.gov/mepsweb/
- Second Panel on Cost-Effectiveness in Health and Medicine, PubMed: https://pubmed.ncbi.nlm.nih.gov/27623463/
- MILES, ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT02432287
- TAME Trial, AFAR: https://www.afar.org/tame-trial
- Metformin as a Tool to Target Aging, PubMed: https://pubmed.ncbi.nlm.nih.gov/27304507/
- Targeting Aging with Metformin, PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC6248732/
- Critical review of metformin as putative anti-aging drug, PubMed: https://pubmed.ncbi.nlm.nih.gov/34421827/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI RMF 1.0 PDF: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- NASA Task Load Index: https://www.nasa.gov/human-systems-integration-division/nasa-task-load-index-tlx/
- Hart and Staveland, NASA-TLX, NASA NTRS: https://ntrs.nasa.gov/citations/20000021488
- Sweller, Cognitive load during problem solving, DOI: https://doi.org/10.1007/BF00375122
- Kaplan, The restorative benefits of nature, DOI: https://doi.org/10.1016/0272-4944(95)90001-2
- ISO 9241-210 human-centred design: https://www.iso.org/standard/77520.html
- Guidelines for Human-AI Interaction, DOI: https://doi.org/10.1145/3290605.3300233
- Microsoft Research, Guidelines for Human-AI Interaction: https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/
- National Academies Human-AI Teaming report: https://www.nationalacademies.org/read/26355
- National Academies Human-AI Teaming DOI: https://doi.org/10.17226/26355
- NBER Generative AI at Work: https://www.nber.org/papers/w31161
- Microsoft New Future of Work: https://www.microsoft.com/en-us/research/project/the-new-future-of-work/
- WHO Guidelines on physical activity and sedentary behaviour: https://www.who.int/publications/i/item/9789240015128
- HHS Physical Activity Guidelines for Americans: https://odphp.health.gov/our-work/nutrition-physical-activity/physical-activity-guidelines
- Dietary Guidelines for Americans: https://www.dietaryguidelines.gov/
- AASM / Sleep Research Society adult sleep duration consensus, PubMed: https://pubmed.ncbi.nlm.nih.gov/26039963/
- CDC Sleep and Sleep Disorders: https://www.cdc.gov/sleep/
- WHO Guidelines on mental health at work: https://www.who.int/publications/i/item/9789240053052
- U.S. Surgeon General Workplace Mental Health and Well-Being Framework: https://www.hhs.gov/surgeongeneral/priorities/workplace-well-being/index.html
- NIOSH Worker Well-Being Questionnaire: https://www.cdc.gov/niosh/twh/worker-well-being/wellbq.html
