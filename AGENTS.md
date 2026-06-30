# Human Infra 架构说明

Human Infra 是以人类任务执行为中心的基础设施项目。根目录只承载总项目入口、稳定理论文档和子域路由，不直接承载某一个具体产品的全部数据与脚本。

## 目录结构

```text
human_infra/
├── .github/              # GitHub 协作模板与远程质量门禁
│   ├── AGENTS.md         # .github 目录说明
│   ├── ISSUE_TEMPLATE/   # issue 模板
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/        # GitHub Actions 工作流
├── AGENTS.md              # 记录总项目架构、职责边界和维护规则
├── human-infra-dashboard.html # 静态 Web 看板：展示主体持续性与生命路径预测模型
├── singularity-human-infra.html # 专项 Web 展示页：将《奇点更近》学习资料转译为 Human Infra 价值与预测模型
├── web/                   # Observable Framework 正式 Web 应用：科研叙事、预测模型和交互图表
│   ├── AGENTS.md          # web 目录说明
│   ├── README.md          # 本地运行、构建和页面职责
│   └── src/               # Framework 页面、组件、样式和展示数据
├── tools/                 # 仓库检查脚本和可复用工程工具
│   ├── AGENTS.md          # tools 目录说明
│   ├── check_repository.py
│   ├── arxiv_html_paper_tool.py
│   └── arxiv-html-paper/  # arXiv HTML papers 复用模板包
├── README.md              # Human Infra 定位、边界、目录和变更日志
├── docs/                  # 总理论、域地图、伦理边界和原始资料归档
│   ├── AGENTS.md          # docs 目录说明
│   ├── README.md          # docs 入口和阅读顺序
│   ├── decisions/         # 架构与域边界决策记录
│   ├── explanations/      # 概念解释和理论文章
│   ├── how-to/            # 任务导向操作说明
│   ├── reference/         # 域地图、伦理边界、术语和标准
│   ├── source-notes/      # 最新原始资料的改名归档
│   └── tutorials/         # 学习路径
└── domains/               # 可独立演化的子域
    ├── AGENTS.md          # 子域目录维护规则
    ├── antimicrobial-resilience/ # 抗微生物韧性
    ├── assistive-technology-access/ # 辅助技术与无障碍
    ├── ai-agency-safety/  # AI 代理安全
    ├── attention-executive-control/ # 注意力与执行控制
    ├── biostasis-cryopreservation/ # 生物停滞与冷冻保存
    ├── cancer-control/    # 癌症控制
    ├── cardiovascular-resilience/ # 心血管韧性
    ├── cellular-senescence-clearance/ # 细胞衰老与清除
    ├── cellular-reprogramming/ # 细胞重编程与表观遗传年轻化谱系
    ├── gene-therapy-genome-editing-delivery-safety/ # 基因治疗、基因编辑与递送安全
    ├── biological-age-clocks-biomarker-validation/ # 生物年龄钟与标志物验证
    ├── multiomics-personal-baseline-systems-biology/ # 多组学个人基线与系统生物学
    ├── engineered-cell-therapy-regenerative-platforms/ # 工程细胞疗法与再生平台
    ├── organoids-organ-on-chip-disease-models/ # 类器官、组织芯片与疾病模型
    ├── xenotransplantation-bioengineered-organ-replacement/ # 异种移植与工程器官替换
    ├── causal-inference-target-trial-emulation/ # 因果推断与目标试验模拟
    ├── survival-analysis-healthspan-risk-modeling/ # 生存分析与健康寿命风险建模
    ├── human-digital-twin-life-course-simulation/ # 人类数字孪生与生命历程仿真
    ├── implementation-science-adherence-behavior-change/ # 实施科学、依从性与行为改变
    ├── uncertainty-quantification-model-calibration/ # 不确定性量化与模型校准
    ├── data-quality-missingness-representativeness/ # 数据质量、缺失与代表性
    ├── privacy-preserving-computation-federated-learning/ # 隐私保护计算与联邦学习
    ├── knowledge-graph-ontology-semantic-interoperability/ # 知识图谱、本体与语义互操作
    ├── model-cards-ai-audit-documentation/ # 模型卡与 AI 审计文档
    ├── technology-foresight-horizon-scanning/ # 技术预见与地平线扫描
    ├── research-portfolio-prioritization-funding-governance/ # 研究组合优先级与资金治理
    ├── intellectual-property-technology-transfer-access/ # 知识产权、技术转移与可及性
    ├── trustworthy-scientific-communication-peer-review/ # 可信科研传播与同行评审
    ├── research-participant-consent-community-engagement/ # 研究参与者同意与社区参与
    ├── biobanking-biospecimen-quality-chain-of-custody/ # 生物样本库、样本质量与保管链
    ├── longitudinal-cohort-retention-followup-infrastructure/ # 纵向队列留存与随访基础设施
    ├── registries-real-world-data-governance/ # 登记系统与真实世界数据治理
    ├── scientific-instrumentation-sensor-calibration-maintenance/ # 科研仪器与传感器校准维护
    ├── nanomedicine-targeted-delivery-molecular-repair/ # 纳米医学、靶向递送与分子修复
    ├── ai-drug-discovery-protein-design/ # AI 药物发现与蛋白设计
    ├── epigenetic-editing-gene-regulation-therapeutics/ # 表观遗传编辑与基因调控疗法
    ├── brain-preservation-connectomics-emulation/ # 脑保存、连接组与仿真假设
    ├── post-quantum-cryptography-long-term-data-security/ # 后量子密码与长期数据安全
    ├── safety-critical-software-formal-methods/ # 安全关键软件与形式化方法
    ├── long-term-digital-preservation-format-migration/ # 长期数字保存与格式迁移
    ├── cerebrovascular-stroke-brain-perfusion-resilience/ # 卒中、脑灌注与脑血管韧性
    ├── traumatic-brain-injury-neurotrauma-recovery/ # TBI、脑震荡与神经创伤恢复
    ├── delirium-acute-cognitive-failure-prevention/ # 谵妄与急性认知失败预防
    ├── disorders-of-consciousness-coma-recovery/ # 意识障碍、昏迷与恢复边界
    ├── epilepsy-seizure-network-stability/ # 癫痫、发作与脑网络稳定
    ├── autonomic-nervous-system-homeostasis/ # 自主神经系统稳态
    ├── migraine-headache-effective-time-burden/ # 偏头痛、头痛障碍与有效时间负担
    ├── vision-eye-health-continuity/ # 视觉与眼健康连续性
    ├── hearing-auditory-communication-continuity/ # 听力与听觉沟通连续性
    ├── vestibular-balance-spatial-orientation/ # 前庭、平衡与空间定向
    ├── speech-language-communication-continuity/ # 言语、语言与沟通连续性
    ├── swallowing-dysphagia-aspiration-nutrition/ # 吞咽、误吸与营养连续性
    ├── smell-taste-chemosensory-continuity/ # 嗅味觉与化学感知连续性
    ├── peripheral-neuropathy-somatosensory-continuity/ # 周围神经病变与躯体感觉连续性
    ├── space-weather-geomagnetic-storm-resilience/ # 空间天气与地磁暴韧性
    ├── planetary-defense-near-earth-object-risk/ # 行星防御与近地天体风险
    ├── volcanic-ashfall-geohazard-continuity/ # 火山灰与地质灾害连续性
    ├── earthquake-seismic-risk-built-environment-continuity/ # 地震、抗震与建成环境连续性
    ├── tsunami-warning-coastal-evacuation-continuity/ # 海啸预警与沿海撤离连续性
    ├── extreme-heat-cooling-public-health-continuity/ # 极端高温、制冷与公共卫生连续性
    ├── noise-exposure-acoustic-environment-continuity/ # 噪声暴露与声环境连续性
    ├── light-exposure-circadian-environment-continuity/ # 光照暴露与昼夜节律环境连续性
    ├── lead-heavy-metal-exposure-control/ # 铅与重金属暴露控制
    ├── radon-asbestos-indoor-hazard-continuity/ # 氡、石棉与室内长期危害连续性
    ├── mold-dampness-indoor-biological-exposure/ # 霉菌、潮湿与室内生物暴露
    ├── vector-borne-disease-environmental-control/ # 病媒传播疾病与环境控制
    ├── advance-care-planning-medical-decision-continuity/ # 预先医疗照护计划与医疗决策连续性
    ├── supported-decision-making-guardianship-rights/ # 支持性决策、监护与权利保护
    ├── healthcare-personal-representative-hipaa-access-continuity/ # 医疗个人代表与 HIPAA 访问连续性
    ├── financial-fiduciary-power-of-attorney-continuity/ # 财务受托与授权代理连续性
    ├── representative-payee-benefits-management-continuity/ # 代表收款人与福利代管连续性
    ├── trust-estate-affairs-succession-continuity/ # 事务、信托、遗产与继承连续性
    ├── credit-consumer-reporting-access-continuity/ # 信用与消费者报告准入连续性
    ├── tenant-screening-rental-access-continuity/ # 租房筛查与租赁准入连续性
    ├── background-check-record-screening-continuity/ # 背景调查与记录筛查连续性
    ├── employment-algorithmic-hiring-screening-continuity/ # 算法招聘与就业筛查连续性
    ├── insurance-underwriting-algorithmic-risk-scoring-continuity/ # 保险承保算法评分连续性
    ├── public-benefits-eligibility-automated-decision-continuity/ # 公共福利资格自动化判定连续性
    ├── education-record-transcript-verification-continuity/ # 教育记录、成绩单与学历核验连续性
    ├── professional-licensure-certification-continuity/ # 职业执照、专业认证与授权连续性
    ├── skills-competency-credentialing-continuity/ # 技能、胜任力与微证书连续性
    ├── continuing-education-recertification-continuity/ # 继续教育、再认证与续证连续性
    ├── apprenticeship-work-based-learning-continuity/ # 学徒制与工作中学习连续性
    ├── verifiable-credential-wallet-interoperability/ # 可验证凭证钱包与互操作连续性
    ├── income-payroll-employment-record-continuity/ # 工资、薪资与雇佣记录连续性
    ├── tax-administration-filing-record-continuity/ # 税务行政与申报记录连续性
    ├── social-security-earnings-benefit-record-continuity/ # 社会保险收入与福利记录连续性
    ├── retirement-pension-savings-plan-continuity/ # 退休、养老金与储蓄计划连续性
    ├── unemployment-insurance-wage-record-continuity/ # 失业保险工资记录连续性
    ├── workers-compensation-occupational-injury-benefit-continuity/ # 工伤与职业伤害权益连续性
    ├── family-medical-leave-job-protection-continuity/ # 家庭医疗假与岗位保护连续性
    ├── paid-sick-family-leave-wage-replacement-continuity/ # 带薪病假、家庭假与工资替代连续性
    ├── pregnancy-parental-work-continuity/ # 孕产育儿工作连续性
    ├── workplace-accommodation-return-to-work-continuity/ # 工作场所合理便利与复工连续性
    ├── disability-income-work-capacity-benefit-continuity/ # 残障收入、工作能力与福利连续性
    ├── family-caregiver-respite-work-continuity/ # 家庭照护者、喘息服务与工作连续性
    ├── vital-records-life-event-continuity/ # 生命事件与核心民事记录连续性
    ├── name-change-identity-record-synchronization-continuity/ # 姓名变更与身份记录同步连续性
    ├── address-residency-mail-service-continuity/ # 地址、居住地与邮件服务连续性
    ├── household-composition-dependent-eligibility-continuity/ # 家庭组成、受扶养人与资格关系连续性
    ├── family-law-custody-child-support-continuity/ # 家庭法、监护权与子女抚养连续性
    ├── kinship-foster-adoption-care-continuity/ # 亲属照护、寄养、收养与儿童安置连续性
    ├── banking-deposit-account-access-continuity/ # 银行账户、存款保险与账户访问连续性
    ├── debt-obligation-collection-relief-continuity/ # 债务义务、催收与债务救济连续性
    ├── real-property-title-deed-record-continuity/ # 不动产权属、地契与土地记录连续性
    ├── driver-license-vehicle-registration-continuity/ # 驾照、车辆登记与个人移动资格连续性
    ├── passport-travel-document-mobility-continuity/ # 护照、旅行证件与跨境移动连续性
    ├── contract-subscription-billing-consent-continuity/ # 合同、订阅、账单与持续同意连续性
    ├── notary-document-authentication-signature-continuity/ # 公证、文件认证与签名连续性
    ├── citizenship-nationality-statelessness-continuity/ # 公民身份、国籍与无国籍连续性
    ├── immigration-status-residency-work-authorization-continuity/ # 移民身份、居留与工作授权连续性
    ├── asylum-refugee-protection-status-continuity/ # 庇护、难民与保护状态连续性
    ├── detention-custody-confinement-status-continuity/ # 拘押、羁押与监管状态连续性
    ├── civil-commitment-involuntary-treatment-rights-continuity/ # 民事收治、非自愿治疗与权利连续性
    ├── court-notice-service-process-default-judgment-continuity/ # 法院通知、送达与缺席判决连续性
    ├── criminal-record-relief-collateral-consequences-continuity/ # 犯罪记录救济与附带后果连续性
    ├── school-enrollment-attendance-continuity/ # 学校入学与出勤连续性
    ├── special-education-iep-504-accommodation-continuity/ # 特殊教育、IEP 与 504 便利连续性
    ├── school-meals-nutrition-access-continuity/ # 校餐与营养可及连续性
    ├── school-health-services-chronic-condition-continuity/ # 学校健康服务与慢病连续性
    ├── school-transportation-safe-routes-continuity/ # 通学交通与安全路线连续性
    ├── school-discipline-exclusion-restraint-continuity/ # 学校纪律、排除与约束隔离连续性
    ├── school-mental-health-counseling-support-continuity/ # 学校心理健康与咨询支持连续性
    ├── school-climate-bullying-violence-prevention-continuity/ # 学校气候、欺凌与暴力预防连续性
    ├── postsecondary-admissions-transfer-articulation-continuity/ # 高等教育入学、转学与衔接连续性
    ├── student-financial-aid-grant-scholarship-continuity/ # 学生资助、助学金与奖学金连续性
    ├── academic-advising-degree-progress-continuity/ # 学业指导与学位进度连续性
    ├── campus-basic-needs-student-support-continuity/ # 校园基本需求与学生支持连续性
    ├── campus-disability-accommodations-accessibility-continuity/ # 校园残障便利与无障碍连续性
    ├── campus-mental-health-crisis-student-support-continuity/ # 校园心理健康、危机与学生支持连续性
    ├── campus-safety-title-ix-clery-continuity/ # 校园安全、Title IX 与 Clery 连续性
    ├── international-student-sevis-status-continuity/ # 国际学生 SEVIS 身份连续性
    ├── email-account-recovery-continuity/ # 邮箱账号恢复连续性
    ├── phone-number-sim-portability-account-security-continuity/ # 手机号、SIM 与携转账号安全连续性
    ├── mfa-passkey-credential-recovery-continuity/ # MFA、passkey 与凭证恢复连续性
    ├── password-manager-secret-vault-continuity/ # 密码管理器与密钥库连续性
    ├── cloud-backup-file-sync-data-portability-continuity/ # 云备份、文件同步与数据可携带连续性
    ├── messaging-contact-graph-portability-continuity/ # 消息与联系人图谱可携带连续性
    ├── domain-dns-web-presence-continuity/ # 域名、DNS 与 Web 存在连续性
    ├── platform-account-suspension-appeals-continuity/ # 平台账号停权与申诉连续性
    ├── personal-computing-device-lifecycle-repair-continuity/ # 个人计算设备生命周期与维修连续性
    ├── home-network-router-iot-security-continuity/ # 家庭网络、路由器与 IoT 安全连续性
    ├── software-supply-chain-dependency-provenance-continuity/ # 软件供应链、依赖与来源证明连续性
    ├── software-update-vulnerability-patch-continuity/ # 软件更新、漏洞与补丁连续性
    ├── open-source-maintainer-sustainability-continuity/ # 开源维护者可持续性连续性
    ├── pki-certificate-cryptographic-trust-continuity/ # PKI、证书与密码信任连续性
    ├── cloud-service-exit-interoperability-continuity/ # 云服务退出与互操作连续性
    ├── api-platform-dependency-runtime-continuity/ # API、平台依赖与运行时连续性
    ├── calendar-scheduling-appointment-continuity/ # 日历、排程与预约连续性
    ├── notification-alert-routing-attention-continuity/ # 通知、警报路由与注意力连续性
    ├── reminder-alarm-routine-task-continuity/ # 提醒、闹钟与例行任务连续性
    ├── meeting-video-conferencing-remote-collaboration-continuity/ # 会议、视频会议与远程协作连续性
    ├── document-capture-ocr-pdf-record-workflow-continuity/ # 文件捕获、OCR、PDF 与记录工作流连续性
    ├── search-index-discovery-retrieval-continuity/ # 搜索、索引、发现与检索连续性
    ├── personal-automation-integration-workflow-continuity/ # 个人自动化、集成与工作流连续性
    ├── collaborative-document-permission-version-continuity/ # 协作文档、权限与版本连续性
    ├── home-access-lock-key-entry-continuity/ # 住所进入、钥匙与门禁连续性
    ├── household-appliance-maintenance-repair-continuity/ # 家用电器维护与维修连续性
    ├── home-refrigeration-food-storage-continuity/ # 家庭冷藏与食品保存连续性
    ├── cooking-meal-preparation-kitchen-safety-continuity/ # 烹饪备餐与厨房安全连续性
    ├── laundry-clothing-footwear-hygiene-continuity/ # 洗衣、衣物、鞋履与卫生连续性
    ├── household-cleaning-disinfection-pest-control-continuity/ # 家庭清洁、消毒与害虫控制连续性
    ├── postal-parcel-delivery-pickup-continuity/ # 邮件、包裹、投递与自提连续性
    ├── household-maintenance-repair-contractor-continuity/ # 家庭维修、承包商与修复服务连续性
    ├── cognitive-augmentation/ # 认知增强与工具放大
    ├── digital-identity-security/ # 数字身份安全
    ├── disembodied-cns/   # 去具身外部维持型中枢生命系统
    ├── endocrine-hormonal-regulation/ # 内分泌与激素调节
    ├── extracellular-matrix-glycation/ # 细胞外基质与糖化
    ├── financial-resilience-access/ # 财务韧性与资源可及
    ├── food-security-nutrition-access/ # 食物安全与营养可及
    ├── water-sanitation-hygiene-continuity/ # 水、环境卫生与个人卫生连续性
    ├── energy-access-resilience/ # 能源可及与韧性
    ├── fluid-electrolyte-acid-base-homeostasis/ # 体液电解质酸碱稳态
    ├── future-waiting/    # 去未来 / 压缩等待路径
    ├── healthcare-access-continuity/ # 医疗服务连续性
    ├── medicine-access-treatment-continuity/ # 药品可及与治疗连续性
    ├── patient-data-interoperability/ # 患者数据访问与互操作
    ├── telehealth-remote-monitoring-access/ # 远程医疗与居家监测
    ├── health-data-privacy-governance/ # 健康数据隐私治理
    ├── functioning-quality-of-life-outcomes/ # 功能与生活质量结局
    ├── health-economics-value-assessment/ # 健康经济与价值评估
    ├── immunization-public-health-surveillance/ # 免疫与公共卫生监测
    ├── maternal-newborn-child-development/ # 母婴健康与儿童发展
    ├── patient-safety-organizational-learning/ # 患者安全与组织学习
    ├── caregiving-long-term-care/ # 照护与长期照护
    ├── housing-built-environment-stability/ # 住房与建成环境稳定
    ├── governance-rights/ # 治理与主体权利
    ├── genomic-stability-dna-repair/ # 基因组稳定性与 DNA 修复
    ├── gastrointestinal-barrier-absorption/ # 消化屏障与吸收
    ├── blood-oxygen-hemostasis/ # 血液氧运与止血
    ├── health-literacy-navigation/ # 健康素养与服务导航
    ├── language-access-plain-communication/ # 语言可达与清晰沟通
    ├── labor-rights-workplace-protection/ # 劳动权利与工作场所保护
    ├── immune-maintenance/# 免疫系统维护
    ├── information-integrity-trust/ # 信息完整性与信任
    ├── legal-identity-civil-registration/ # 法律身份与民事登记
    ├── access-to-justice-legal-aid/ # 司法可及与法律援助
    ├── civic-participation-election-access/ # 公民参与与选举接入
    ├── migration-displacement-humanitarian-continuity/ # 迁移、流离失所与人道连续性
    ├── digital-inclusion-connectivity/ # 数字包容与连接
    ├── social-protection-benefits-delivery/ # 社会保护与福利递送
    ├── community-resource-navigation/ # 社区资源导航与转介
    ├── social-determinants-community-vulnerability/ # 社会决定因素与社区脆弱性
    ├── public-service-design-accessibility/ # 公共服务设计与可达性
    ├── emergency-alerts-communications/ # 应急预警与通信
    ├── disaster-recovery-relief-continuity/ # 灾后恢复与救济连续性
    ├── financial-inclusion-payment-systems/ # 金融包容与支付系统
    ├── workforce-employment-services/ # 劳动力与就业服务
    ├── household-emergency-preparedness-resilience/ # 家庭应急准备与韧性
    ├── media-information-literacy-public-libraries/ # 媒体信息素养与公共图书馆
    ├── health-workforce-capacity/ # 健康劳动力容量
    ├── administrative-burden-procedural-friction/ # 行政负担与程序摩擦
    ├── community-health-workers-peer-support/ # 社区健康工作者与同伴支持
    ├── civic-data-open-government-transparency/ # 公民数据与开放政府透明
    ├── education-access-lifelong-learning/ # 教育可及与终身学习
    ├── research-infrastructure-open-science-translation/ # 科研基础设施、开放科学与转化
    ├── standards-metrology-quality-infrastructure/ # 标准计量与质量基础设施
    ├── cybersecurity-resilience-critical-services/ # 网络安全韧性与关键服务
    ├── compute-data-center-ai-infrastructure/ # 算力、数据中心与 AI 基础设施
    ├── clinical-trials-regulatory-science-translation/ # 临床试验、监管科学与转化
    ├── geospatial-navigation-location-infrastructure/ # 空间定位、导航与位置基础设施
    ├── weather-climate-observation-forecasting/ # 天气气候观测与预报
    ├── building-fire-life-safety-codes/ # 建筑消防与生命安全规范
    ├── manufacturing-repair-capacity/ # 制造与维修能力
    ├── public-procurement-contracting-capacity/ # 公共采购与合同能力
    ├── animal-health-zoonotic-interface-one-health/ # 动物健康、人兽共患界面与 One Health
    ├── public-health-laboratory-diagnostic-capacity/ # 公共卫生实验室与诊断能力
    ├── blood-organ-tissue-biovigilance-transplantation/ # 血液、器官、组织与生物警戒
    ├── waste-management-hazardous-materials-continuity/ # 废弃物、危险材料与处置连续性
    ├── radiation-nuclear-safety-protection/ # 辐射与核安全防护
    ├── chemical-safety-poison-control-toxicology/ # 化学安全、中毒控制与毒理响应
    ├── critical-minerals-materials-resilience/ # 关键矿物与材料韧性
    ├── air-quality-ventilation-exposure-control/ # 空气质量、通风与暴露控制
    ├── food-safety-contamination-control/ # 食品安全与污染控制
    ├── occupational-exposure-industrial-hygiene/ # 职业暴露与工业卫生
    ├── medical-device-equipment-safety-maintenance/ # 医疗器械、设备安全与维护
    ├── sterilization-disinfection-infection-control/ # 灭菌、消毒与感染控制
    ├── built-environment-accessibility-universal-design/ # 建成环境无障碍与通用设计
    ├── clinical-laboratory-diagnostic-quality/ # 临床检验与诊断质量
    ├── pharmacovigilance-drug-safety-monitoring/ # 药物警戒与药品安全监测
    ├── pharmaceutical-quality-supply-integrity/ # 药品质量与供应完整性
    ├── emergency-medical-services-prehospital-care/ # 急救医疗服务与院前照护
    ├── surgical-anesthesia-perioperative-safety/ # 手术、麻醉与围手术期安全
    ├── road-traffic-injury-prevention-safe-mobility/ # 道路交通伤害预防与安全移动
    ├── rural-health-access-geographic-equity/ # 农村健康可及与地理公平
    ├── homelessness-unsheltered-health-continuity/ # 无家可归与露宿健康连续性
    ├── correctional-health-reentry-continuity/ # 羁押健康与重返社会连续性
    ├── disability-services-independent-living/ # 残障服务与独立生活
    ├── dementia-cognitive-decline-care-continuity/ # 痴呆认知衰退与照护连续性
    ├── chronic-infectious-disease-care-continuity/ # 慢性传染病照护连续性
    ├── suicide-crisis-response-continuity/ # 自杀危机响应连续性
    ├── substance-use-treatment-recovery-continuity/ # 物质使用障碍治疗与恢复连续性
    ├── elder-justice-adult-protective-services/ # 老年正义与成人保护服务
    ├── child-protection-family-safety/ # 儿童保护与家庭安全
    ├── fraud-scams-consumer-protection/ # 诈骗、欺诈与消费者保护
    ├── online-safety-digital-harm-prevention/ # 在线安全与数字伤害预防
    ├── rare-disease-diagnostic-odyssey-care-coordination/ # 罕见病诊断漫游与照护协调
    ├── multimorbidity-polypharmacy-care-coordination/ # 多病共存、多重用药与照护协调
    ├── care-transitions-discharge-continuity/ # 照护转移与出院连续性
    ├── home-health-hospice-palliative-care-continuity/ # 居家医疗、缓和医疗、安宁疗护与临终连续性
    ├── medical-interpreter-cultural-mediation/ # 医疗解释、语言可达与文化中介
    ├── patient-advocacy-shared-decision-making/ # 患者倡导与共同决策
    ├── life-logging-personal-archives-continuity/ # 生命日志、个人档案与资料连续性
    ├── digital-legacy-data-succession/ # 数字遗产、数据继承与账号连续性
    ├── wearables-continuous-sensing-personal-informatics/ # 可穿戴、连续感知与个人信息学
    ├── personal-knowledge-management-cognitive-offloading/ # 个人知识管理与认知卸载
    ├── brain-computer-interface-neurotechnology-governance/ # 脑机接口、神经技术与治理
    ├── robotics-embodied-assistance-care-automation/ # 机器人、具身辅助与照护自动化
    ├── armed-conflict-civilian-protection-ihl/ # 武装冲突、平民保护与国际人道法
    ├── peacebuilding-conflict-prevention-social-cohesion/ # 和平建设、冲突预防与社会凝聚
    ├── continuity-of-government-public-administration-resilience/ # 政府连续性与公共行政韧性
    ├── telecommunications-network-resilience-continuity/ # 电信网络韧性与通信连续性
    ├── macroeconomic-monetary-fiscal-stability/ # 宏观经济、货币与财政稳定
    ├── anti-corruption-public-integrity-accountability/ # 反腐败、公共廉洁与问责
    ├── agricultural-production-food-system-resilience/ # 农业生产与食物系统韧性
    ├── soil-health-land-degradation-drought-resilience/ # 土壤健康、土地退化与旱灾韧性
    ├── water-resources-hydrology-flood-drought-management/ # 水资源、水文与洪旱管理
    ├── biodiversity-ecosystem-services-resilience/ # 生物多样性与生态系统服务韧性
    ├── wildfire-landscape-fire-resilience/ # 野火、景观火灾与社区韧性
    ├── freight-logistics-port-cold-chain-continuity/ # 货运、港口、仓储与冷链连续性
    ├── coastal-marine-resilience-blue-economy-continuity/ # 海岸海洋韧性与蓝色经济连续性
    ├── fisheries-aquatic-food-systems-continuity/ # 渔业与水生食物系统连续性
    ├── dams-levees-flood-control-infrastructure-safety/ # 水坝、堤防与防洪基础设施安全
    ├── public-works-civil-infrastructure-asset-management/ # 公共工程与土木基础设施资产管理
    ├── urban-planning-land-use-zoning-resilience/ # 城市规划、土地使用与分区韧性
    ├── green-blue-infrastructure-urban-nature-cooling/ # 绿蓝基础设施、城市自然与降温
    ├── electric-grid-reliability-resilience-continuity/ # 电网可靠性与韧性连续性
    ├── water-wastewater-utility-service-continuity/ # 水务与污水公用事业连续性
    ├── fuel-thermal-energy-service-continuity/ # 燃料与热能服务连续性
    ├── public-transit-service-operations-continuity/ # 公共交通服务运营连续性
    ├── critical-infrastructure-lifeline-interdependency-resilience/ # 关键基础设施生命线互依赖韧性
    ├── utility-affordability-shutoff-protection-continuity/ # 公用事业可负担性与断供保护
    ├── insurance-risk-transfer/ # 保险与风险转移
    ├── childcare-family-continuity/ # 托育与家庭连续性
    ├── learning-skill-acquisition/ # 学习与技能获得
    ├── longevity-evidence/# 原 Biocat 长寿证据账本
    ├── lymphatic-glymphatic-clearance/ # 淋巴与脑淋巴清除
    ├── measurement-feedback/ # 测量、预测与反馈
    ├── mental-health-affective-stability/ # 心理健康与情绪稳定
    ├── memory-editing/    # 记忆编辑与人格连续性
    ├── microbiome-ecology/ # 微生物生态
    ├── mitochondrial-bioenergetics/ # 线粒体生物能量学
    ├── musculoskeletal-integrity/ # 肌骨完整性
    ├── neuro-continuity/  # 神经与身份连续性
    ├── nutrition-metabolic-health/ # 营养与代谢健康
    ├── oral-health-continuity/ # 口腔健康连续性
    ├── occupational-work-design/ # 职业与工作设计
    ├── pain-suffering-control/ # 疼痛与痛苦控制
    ├── physical-activity-mobility/ # 身体活动与移动能力
    ├── planetary-health-environment/ # 星球健康与环境
    ├── proteostasis-autophagy/ # 蛋白稳态与自噬
    ├── regenerative-medicine/ # 再生医学与组织修复
    ├── rehabilitation-functioning/ # 康复与功能恢复
    ├── reproductive-fertility-continuity/ # 生殖与生育连续性
    ├── renal-hepatic-clearance/ # 肾脏与肝脏清除能力
    ├── respiratory-oxygenation/ # 呼吸氧合
    ├── resource-social-infra/ # 资源与社会基础设施
    ├── risk-engineering/  # 风险工程
    ├── emergency-preparedness-response/ # 应急准备与响应
    ├── personal-safety-violence-prevention/ # 人身安全与暴力预防
    ├── product-safety-recall-systems/ # 产品安全与召回系统
    ├── sensory-continuity/ # 感官连续性
    ├── sleep-circadian-recovery/ # 睡眠、节律与恢复
    ├── skin-barrier-wound-healing/ # 皮肤屏障与伤口愈合
    ├── social-connection-relational-infra/ # 社会连接与关系基础设施
    ├── space-extreme-habitation/ # 空间与极端栖居
    ├── stem-cell-reserve-renewal/ # 干细胞储备与组织更新
    ├── substance-exposure-control/ # 物质暴露控制
    ├── supply-chain-continuity/ # 供应链连续性
    ├── synthetic-biology-biosecurity/ # 合成生物学与生物安全
    ├── thermal-homeostasis-resilience/ # 热稳态与温度韧性
    ├── time-allocation-effective-time/ # 时间分配与有效时间
    ├── transportation-access-mobility/ # 交通接入与日常移动
    ├── urogenital-continuity/ # 泌尿生殖连续性
    └── telomere-maintenance/ # 端粒维护
```

## 职责边界

- `.github/` 只放 GitHub 协作模板和远程质量门禁，不放长期知识正文。
- `human-infra-dashboard.html` 是根目录静态展示入口，只承载可直接打开的模型看板，不承载数据采集、个人预测或生产服务逻辑。
- `singularity-human-infra.html` 是根目录专项展示入口，用于把《奇点更近》学习资料转译为 Human Infra 的价值展示、预测模型和 D3 可视化，不作为事实核验或医学建议。
- `web/` 是 Observable Framework 正式 Web 应用目录，用于多页科研叙事、书籍转译、预测模型和交互可视化；它不承载采集脚本、个人预测服务或医学决策逻辑。
- `tools/` 保存仓库维护脚本和可迁移工程工具；其中 arXiv HTML papers 复用工具只负责资源安装、资产校验和 Astro 模板生成，不承载 Human Infra 正文理论。
- `docs/` 只放 Human Infra 的上位理论、域边界、伦理原则和原始资料归档，不放具体采集脚本。
- `domains/` 中每个子域必须有独立 README 和 AGENTS，明确自身对象、非目标、证据要求和上下游关系。
- `domains/longevity-evidence/` 承接原 Biocat，负责长寿干预证据、临床试验、药品安全、公开数据源和采集脚本。
- `domains/genomic-stability-dna-repair/` 负责基因组稳定性、DNA 损伤、修复系统、突变负荷和癌前风险。
- `domains/telomere-maintenance/` 负责端粒长度、端粒酶、复制衰老、组织更新和癌症风险。
- `domains/proteostasis-autophagy/` 负责蛋白稳态、自噬、溶酶体、蛋白聚集和细胞质量控制。
- `domains/mitochondrial-bioenergetics/` 负责线粒体功能、细胞能量、氧化应激、疲劳和行动能力。
- `domains/cellular-senescence-clearance/` 负责细胞衰老、SASP、senolytics、组织炎症和衰老细胞负担。
- `domains/extracellular-matrix-glycation/` 负责细胞外基质、胶原、弹性、AGEs、交联、纤维化和组织力学。
- `domains/microbiome-ecology/` 负责人体微生物生态、菌群失调、代谢、免疫和炎症。
- `domains/stem-cell-reserve-renewal/` 负责干细胞储备、生态位、组织更新、内源性修复和再生能力。
- `domains/renal-hepatic-clearance/` 负责肾脏、肝脏、解毒、代谢、药物清除和系统稳态。
- `domains/gastrointestinal-barrier-absorption/` 负责消化、吸收、肠道屏障、胃肠动力和营养进入系统。
- `domains/respiratory-oxygenation/` 负责肺、气道、通气、氧合、睡眠呼吸、空气暴露和呼吸失败风险。
- `domains/blood-oxygen-hemostasis/` 负责红细胞、血红蛋白、氧气运输、凝血、出血、血栓和血液安全。
- `domains/endocrine-hormonal-regulation/` 负责激素轴、反馈环、代谢信号、压力反应、生殖、骨骼和情绪调节。
- `domains/lymphatic-glymphatic-clearance/` 负责淋巴系统、组织液、免疫运输、脑膜淋巴、glymphatic clearance 和水肿。
- `domains/fluid-electrolyte-acid-base-homeostasis/` 负责水分、电解质、渗透压、酸碱平衡和内环境稳定。
- `domains/thermal-homeostasis-resilience/` 负责体温调节、热暴露、寒冷暴露、散热、出汗和温度韧性。
- `domains/nutrition-metabolic-health/` 负责营养、饮食质量、代谢健康、体重、糖尿病风险和食物环境。
- `domains/physical-activity-mobility/` 负责身体活动、久坐、心肺适能、力量、平衡和移动能力。
- `domains/cardiovascular-resilience/` 负责心脏、血管、血压、动脉粥样硬化、血栓、卒中、心衰和循环系统韧性。
- `domains/musculoskeletal-integrity/` 负责肌肉、骨骼、关节、肌少症、骨质疏松、跌倒和行动承载结构。
- `domains/skin-barrier-wound-healing/` 负责皮肤屏障、伤口愈合、压力损伤、感染入口、热调节和感觉边界。
- `domains/urogenital-continuity/` 负责膀胱、尿路、尿控、盆底、泌尿感染、性功能和日常尊严。
- `domains/reproductive-fertility-continuity/` 负责生育力、生殖衰老、配子质量、妊娠风险、生殖自主性和未来选择权。
- `domains/attention-executive-control/` 负责注意力、执行功能、工作记忆、抑制控制、任务切换、冲动控制和分心环境。
- `domains/learning-skill-acquisition/` 负责学习科学、技能形成、反馈、迁移、再训练和终身学习。
- `domains/time-allocation-effective-time/` 负责时间使用、时间贫困、行政负担、等待成本、任务摩擦、有效时间和主观时间质量。
- `domains/financial-resilience-access/` 负责收入稳定、储蓄缓冲、债务、保险、医疗支付能力、财务冲击和资源可及性。
- `domains/occupational-work-design/` 负责职业安全、工作组织、人体工学、工时、职业暴露、压力、倦怠和工作可持续性。
- `domains/information-integrity-trust/` 负责信息可信度、证据质量、误导信息、平台传播、AI 生成内容和信任链。
- `domains/food-security-nutrition-access/` 负责食物安全、饥饿、营养不足、食品安全、价格冲击和食物系统连续性。
- `domains/water-sanitation-hygiene-continuity/` 负责安全饮用水、卫生设施、洗手、污水处理、WASH 覆盖和服务可靠性。
- `domains/energy-access-resilience/` 负责电力、清洁烹饪、能源负担、停电、温控、通信供能和医疗设备供电。
- `domains/healthcare-access-continuity/` 负责初级卫生保健、急诊、预防、转诊、随访、费用、质量和医疗服务连续性。
- `domains/medicine-access-treatment-continuity/` 负责基本药物、药品短缺、标签、患者药品信息、覆盖、费用和用药安全这些治疗执行条件。
- `domains/patient-data-interoperability/` 负责健康记录访问、数据可携带、互操作标准、授权应用和跨机构数据连续性。
- `domains/telehealth-remote-monitoring-access/` 负责远程医疗、远程患者监测、居家设备、数字照护连续性和升级路径。
- `domains/health-data-privacy-governance/` 负责健康、基因、行为、神经和服务数据的隐私、同意、退出、安全、共享和用途边界。
- `domains/functioning-quality-of-life-outcomes/` 负责功能状态、生活质量、症状负担、患者报告结局和主体中心结果。
- `domains/health-economics-value-assessment/` 负责疾病负担、成本效果、HTA、价值框架、预算影响、资源分配和公平边界。
- `domains/immunization-public-health-surveillance/` 负责免疫计划、传染病监测、公共卫生应急、感染防控、AMR、One Health 和废水监测。
- `domains/maternal-newborn-child-development/` 负责孕产健康、新生儿健康、儿童健康、生长标准、早期发展和养育照护。
- `domains/patient-safety-organizational-learning/` 负责患者安全、事件报告、团队沟通、根因分析、CUSP、TeamSTEPPS 和安全文化。
- `domains/caregiving-long-term-care/` 负责家庭照护、长期照护、居家社区支持、照护协调、照护者负担和尊严边界。
- `domains/housing-built-environment-stability/` 负责住房稳定、住房质量、室内环境、无障碍、社区资源和建成环境健康。
- `domains/transportation-access-mobility/` 负责公共交通、无障碍交通、出行时间、医疗交通、交通成本和外部资源可达性。
- `domains/legal-identity-civil-registration/` 负责法律身份、出生登记、民事登记、生命统计、身份文件、身份覆盖和服务资格。
- `domains/access-to-justice-legal-aid/` 负责民事法律需求、法律援助、司法可及、程序负担和权利救济。
- `domains/civic-participation-election-access/` 负责选民登记、投票可及、无障碍投票、选举标准、公共参与和制度反馈。
- `domains/migration-displacement-humanitarian-continuity/` 负责迁移、难民、流离失所、身份连续、健康/教育/庇护/保护服务和人道协调。
- `domains/digital-inclusion-connectivity/` 负责互联网接入、设备可及、可负担性、数字技能、无障碍、人工帮助和数字公共服务接入。
- `domains/social-protection-benefits-delivery/` 负责公共福利、社会保护、资格、申请、续期、支付、申诉和行政负担。
- `domains/community-resource-navigation/` 负责 211、社区资源目录、社会需求筛查、转介、闭环回访和本地服务导航。
- `domains/social-determinants-community-vulnerability/` 负责社会决定因素、社区脆弱性、环境正义、地方健康估计、食物可达和健康相关社会需求。
- `domains/public-service-design-accessibility/` 负责公共数字服务、表单、客户体验、无障碍、人工帮助、状态反馈和任务完成路径。
- `domains/emergency-alerts-communications/` 负责公共预警、WEA/EAS、NOAA Weather Radio、911/NG911、FirstNet 和危机通信入口。
- `domains/disaster-recovery-relief-continuity/` 负责灾后个人援助、恢复中心、临时安置、灾害贷款、救济服务和恢复连续性。
- `domains/financial-inclusion-payment-systems/` 负责账户、支付系统、汇款、数字金融服务、消费者金融保护和资源流动基础设施。
- `domains/workforce-employment-services/` 负责就业服务、劳动力发展、学徒制、职业信息、再就业支持和合理便利。
- `domains/household-emergency-preparedness-resilience/` 负责家庭应急计划、物资包、健康准备、备用通信、重要文件和特殊需求安排。
- `domains/media-information-literacy-public-libraries/` 负责媒体信息素养、公共图书馆、可信知识入口、数字技能和社区学习空间。
- `domains/health-workforce-capacity/` 负责健康劳动力供给、分布、训练、保留、负荷、技能组合和短缺风险。
- `domains/administrative-burden-procedural-friction/` 负责学习成本、心理成本、合规成本、证明负担、等待、续期、申诉和程序摩擦。
- `domains/community-health-workers-peer-support/` 负责社区健康工作者、同伴支持、导航员、可信中介、转介闭环和恢复支持。
- `domains/civic-data-open-government-transparency/` 负责开放数据、公共记录、FOIA、绩效数据、元数据、问责和公共反馈。
- `domains/education-access-lifelong-learning/` 负责教育可及、成人学习、再培训、基础技能、数字学习和技能迁移。
- `domains/research-infrastructure-open-science-translation/` 负责科研基础设施、开放科学、复现性、研究数据、资助、转化科学和知识扩散。
- `domains/standards-metrology-quality-infrastructure/` 负责标准、计量、校准、认证、合格评定、质量管理和互操作规范。
- `domains/cybersecurity-resilience-critical-services/` 负责网络安全、关键服务韧性、事件响应、备份恢复和数字风险治理。
- `domains/compute-data-center-ai-infrastructure/` 负责算力、数据中心、AI 基础设施、芯片、能源、水、网络、成本和接入治理。
- `domains/clinical-trials-regulatory-science-translation/` 负责临床试验、监管科学、真实世界证据、安全监测和医学转化证据路径。
- `domains/geospatial-navigation-location-infrastructure/` 负责地理空间数据、地址、地图、GNSS/GPS、地理编码、应急位置和位置互操作。
- `domains/weather-climate-observation-forecasting/` 负责天气气候观测、预报模型、气候服务、极端天气和早期预警风险输入。
- `domains/building-fire-life-safety-codes/` 负责建筑规范、消防规范、生命安全、疏散、烟雾报警、无障碍和韧性改造。
- `domains/manufacturing-repair-capacity/` 负责制造、维修、维护、备件、质量、本地生产和关键设备恢复能力。
- `domains/public-procurement-contracting-capacity/` 负责公共采购、合同、供应商管理、应急采购、透明度和交付验收。
- `domains/animal-health-zoonotic-interface-one-health/` 负责动物健康、兽医公共卫生、人兽共患病、食品动物、野生动物和 One Health 界面。
- `domains/public-health-laboratory-diagnostic-capacity/` 负责公共卫生实验室、检测确认、诊断网络、质量管理、实验室扩容和风险确认能力。
- `domains/blood-organ-tissue-biovigilance-transplantation/` 负责血液供应、输血安全、器官/组织捐献、移植体系、追踪和生物警戒。
- `domains/waste-management-hazardous-materials-continuity/` 负责固体废物、医疗废物、危险废物、处置连续性和环境暴露边界。
- `domains/radiation-nuclear-safety-protection/` 负责电离辐射防护、核安全、辐射监测、放射性材料风险和辐射应急治理。
- `domains/chemical-safety-poison-control-toxicology/` 负责化学品安全、毒性暴露、毒物中心、毒理证据、暴露监测和风险沟通。
- `domains/critical-minerals-materials-resilience/` 负责关键矿物、关键材料、加工依赖、替代回收和未来技术物质输入韧性。
- `domains/air-quality-ventilation-exposure-control/` 负责空气质量、通风、过滤、气溶胶、烟雾和空气暴露治理。
- `domains/food-safety-contamination-control/` 负责食源性病原体、毒素、过敏原、检查、追溯和召回。
- `domains/occupational-exposure-industrial-hygiene/` 负责工作场所化学、物理、生物、粉尘、噪声、热、辐射和皮肤暴露控制。
- `domains/medical-device-equipment-safety-maintenance/` 负责医疗设备生命周期、不良事件、UDI、召回、维护、网络安全和可用性。
- `domains/sterilization-disinfection-infection-control/` 负责清洁、消毒、灭菌、再处理、环境感染控制和医疗照护相关感染预防。
- `domains/built-environment-accessibility-universal-design/` 负责物理空间可达、路径连续、公共设施、通用设计和环境参与条件。
- `domains/clinical-laboratory-diagnostic-quality/` 负责临床实验室质量、检测准确性、能力验证、诊断管理和临床效用。
- `domains/pharmacovigilance-drug-safety-monitoring/` 负责不良事件报告、真实世界安全信号、标签更新、REMS、用药错误和风险沟通。
- `domains/pharmaceutical-quality-supply-integrity/` 负责药品制造质量、GMP、质量缺陷、污染、假劣药、短缺、冷链和追溯。
- `domains/emergency-medical-services-prehospital-care/` 负责 EMS、调度、响应时间、院前照护、转运和时间关键急性响应。
- `domains/surgical-anesthesia-perioperative-safety/` 负责手术安全、麻醉安全、团队检查、围手术期并发症预防和质量改进。
- `domains/road-traffic-injury-prevention-safe-mobility/` 负责道路交通伤害、安全系统、速度管理、车辆安全、交通数据和安全移动。
- `domains/rural-health-access-geographic-equity/` 负责农村地理距离、服务密度、宽带、交通、卫生人力和农村健康公平。
- `domains/homelessness-unsheltered-health-continuity/` 负责无家可归、露宿、庇护、外展、住房服务、卫生、安全和照护断点。
- `domains/correctional-health-reentry-continuity/` 负责羁押内健康、释放转介、药物连续性、身份、住房、福利和重返社会服务。
- `domains/disability-services-independent-living/` 负责独立生活、HCBS、个人协助、合理便利、辅助技术、无障碍和社区融合。
- `domains/dementia-cognitive-decline-care-continuity/` 负责痴呆、认知衰退、照护计划、照护者负担、尊严、安全和服务导航。
- `domains/chronic-infectious-disease-care-continuity/` 负责 HIV、结核、病毒性肝炎、长期治疗连续性、耐药、隐私和去污名。
- `domains/suicide-crisis-response-continuity/` 负责自杀预防、危机热线、移动危机响应、急诊衔接、随访和恢复支持。
- `domains/substance-use-treatment-recovery-continuity/` 负责物质使用障碍治疗、恢复支持、同伴支持、过量预防、减害治理和服务连续性。
- `domains/elder-justice-adult-protective-services/` 负责老年虐待、成人保护、财务剥削、照护忽视、长期照护监察和保护转介。
- `domains/child-protection-family-safety/` 负责儿童虐待忽视、ACEs、儿童福利、家庭支持、创伤知情服务和制度伤害风险。
- `domains/fraud-scams-consumer-protection/` 负责诈骗识别、身份盗用恢复、投诉举报、消费者保护和反受害者归因风险沟通。
- `domains/online-safety-digital-harm-prevention/` 负责网络霸凌、在线骚扰、数字虐待、儿童在线保护、平台求助和数字伤害恢复。
- `domains/rare-disease-diagnostic-odyssey-care-coordination/` 负责罕见病、未确诊疾病、诊断延误、专家网络、患者登记和孤儿药路径。
- `domains/multimorbidity-polypharmacy-care-coordination/` 负责多病共存、多重用药、多专科冲突、药物重整、治疗负担和照护计划。
- `domains/care-transitions-discharge-continuity/` 负责出院计划、照护转移、交接、用药重整、随访、再入院和跨机构责任断点。
- `domains/home-health-hospice-palliative-care-continuity/` 负责居家医疗、缓和医疗、安宁疗护、严重疾病、症状负担、家庭照护和目标照护。
- `domains/medical-interpreter-cultural-mediation/` 负责医疗解释服务、语言协助、CLAS、LEP、文化中介、知情同意理解和临床沟通安全。
- `domains/patient-advocacy-shared-decision-making/` 负责患者倡导、共同决策、决策辅助、主体偏好、治疗负担、知情同意和未来选择权。
- `domains/life-logging-personal-archives-continuity/` 负责生命日志、个人数字档案、元数据、备份、迁移、长期可读性和主体历史资料连续性。
- `domains/digital-legacy-data-succession/` 负责数字遗产、账号继承、数据授权、受托访问、失能代理、密钥依赖和资料交接。
- `domains/wearables-continuous-sensing-personal-informatics/` 负责可穿戴、连续监测、个人信息学、自我追踪、远程数据采集和反馈闭环。
- `domains/personal-knowledge-management-cognitive-offloading/` 负责个人知识管理、外部记忆、认知卸载、检索、知识库、AI 助手和项目上下文恢复。
- `domains/brain-computer-interface-neurotechnology-governance/` 负责脑机接口、神经记录、刺激、解码、神经数据、设备安全和神经伦理治理。
- `domains/robotics-embodied-assistance-care-automation/` 负责机器人、具身辅助、外骨骼、家庭辅助、康复机器人和照护自动化。
- `domains/armed-conflict-civilian-protection-ihl/` 负责武装冲突中的平民保护、国际人道法、人道准入、医疗中立和冲突服务断点。
- `domains/peacebuilding-conflict-prevention-social-cohesion/` 负责和平建设、冲突预防、社会凝聚、调解、制度信任和暴力升级风险。
- `domains/continuity-of-government-public-administration-resilience/` 负责政府连续性、公共行政韧性、基本职能、授权代理、记录、支付和公共服务恢复。
- `domains/telecommunications-network-resilience-continuity/` 负责电信网络、应急通信、冗余、备电、拥塞、覆盖和通信恢复时间。
- `domains/macroeconomic-monetary-fiscal-stability/` 负责通胀、就业、财政空间、公共债务、金融稳定和基本成本这些宏观资源条件。
- `domains/anti-corruption-public-integrity-accountability/` 负责反腐败、公共廉洁、透明、审计、利益冲突、申诉和问责。
- `domains/agricultural-production-food-system-resilience/` 负责农业生产、作物畜牧、灌溉、种子、肥料、劳动力和气候适应。
- `domains/soil-health-land-degradation-drought-resilience/` 负责土壤健康、土地退化、侵蚀、盐渍化、荒漠化和旱灾韧性。
- `domains/water-resources-hydrology-flood-drought-management/` 负责水资源、水文观测、流域、地下水、洪水、干旱和水安全。
- `domains/biodiversity-ecosystem-services-resilience/` 负责生物多样性、生态系统服务、授粉、过滤、蓄水、降温和生态恢复。
- `domains/wildfire-landscape-fire-resilience/` 负责野火、火灾天气、景观燃料、WUI、烟雾、疏散和社区恢复。
- `domains/freight-logistics-port-cold-chain-continuity/` 负责货运、港口、仓储、冷链、运输节点和最后一公里物流连续性。
- `domains/coastal-marine-resilience-blue-economy-continuity/` 负责海岸带、海平面、风暴潮、侵蚀、海洋生态、海岸社区和蓝色经济连续性。
- `domains/fisheries-aquatic-food-systems-continuity/` 负责捕捞渔业、水产养殖、水产品营养、渔业治理、渔民生计和水生食物系统连续性。
- `domains/dams-levees-flood-control-infrastructure-safety/` 负责水坝、堤防、防洪工程、闸门、泵站、排涝系统和工程失效风险治理。
- `domains/public-works-civil-infrastructure-asset-management/` 负责道路、桥梁、隧道、排水、公共设施、资产状态、维护优先级和服务水平。
- `domains/urban-planning-land-use-zoning-resilience/` 负责城市规划、土地使用、分区、密度、服务布局、公共空间、风险避让和空间公平。
- `domains/green-blue-infrastructure-urban-nature-cooling/` 负责城市树冠、绿地、水体、湿地、雨洪自然基设施、热岛缓解和城市恢复环境。
- `domains/electric-grid-reliability-resilience-continuity/` 负责电网可靠性、资源充足性、输配电资产、停电恢复、关键负荷和韧性投资。
- `domains/water-wastewater-utility-service-continuity/` 负责饮用水、污水处理、管网、泵站、水质监测、应急供水和水务服务恢复。
- `domains/fuel-thermal-energy-service-continuity/` 负责取暖燃料、燃气、液体燃料、区域能源、热泵、备用燃料和热服务恢复。
- `domains/public-transit-service-operations-continuity/` 负责公交、轨道、轮渡、paratransit、班次可靠性、运营人力、资产状态和服务恢复。
- `domains/critical-infrastructure-lifeline-interdependency-resilience/` 负责能源、水务、通信、交通、医疗、食品、金融和政府生命线之间的互依赖与级联风险。
- `domains/utility-affordability-shutoff-protection-continuity/` 负责公用事业账单负担、欠费、援助入口、断供保护、消费者申诉和程序摩擦。
- `domains/gene-therapy-genome-editing-delivery-safety/` 负责基因治疗、基因编辑、递送载体、表达控制、长期随访和遗传安全。
- `domains/biological-age-clocks-biomarker-validation/` 负责表观遗传年龄钟、组学年龄、功能年龄、衰老 biomarker 和验证边界。
- `domains/multiomics-personal-baseline-systems-biology/` 负责基因组、表观组、转录组、蛋白组、代谢组、微生物组和个人基线系统生物学。
- `domains/engineered-cell-therapy-regenerative-platforms/` 负责 CAR-T、TCR-T、TIL、NK、iPSC 衍生细胞和可编程细胞平台。
- `domains/organoids-organ-on-chip-disease-models/` 负责类器官、organ-on-chip、组织芯片、患者来源模型和人体相关新方法学。
- `domains/xenotransplantation-bioengineered-organ-replacement/` 负责异种移植、基因编辑动物器官、工程器官、器官保存灌注和替代性器官供给。
- `domains/causal-inference-target-trial-emulation/` 负责因果推断、反事实、目标试验模拟、混杂和选择偏差审查。
- `domains/survival-analysis-healthspan-risk-modeling/` 负责生存分析、风险函数、健康寿命、竞争风险和有效时间终点建模。
- `domains/human-digital-twin-life-course-simulation/` 负责人类数字孪生、生命历程仿真、主体状态向量、状态转移和场景模拟。
- `domains/implementation-science-adherence-behavior-change/` 负责实施科学、依从性、技术采用、行为改变和真实世界效果。
- `domains/uncertainty-quantification-model-calibration/` 负责不确定性量化、模型校准、外部验证、漂移监测和报告边界。
- `domains/data-quality-missingness-representativeness/` 负责数据质量、缺失机制、代表性、测量误差和数据入口门禁。
- `domains/privacy-preserving-computation-federated-learning/` 负责隐私保护计算、差分隐私、联邦学习、安全协作学习和隐私-效用边界。
- `domains/knowledge-graph-ontology-semantic-interoperability/` 负责知识图谱、本体、受控词表、语义互操作和 FAIR 知识结构。
- `domains/model-cards-ai-audit-documentation/` 负责模型卡、数据说明、系统卡、AI 审计文档和模型用途限制。
- `domains/technology-foresight-horizon-scanning/` 负责技术预见、地平线扫描、弱信号、情景分析和未来技术候选队列。
- `domains/research-portfolio-prioritization-funding-governance/` 负责研究组合优先级、资金治理、阶段门、学习价值和停止条件。
- `domains/intellectual-property-technology-transfer-access/` 负责知识产权、许可、技术转移、公共资助成果和技术可及性。
- `domains/trustworthy-scientific-communication-peer-review/` 负责同行评审、预印本、撤稿、勘误、引用语境和科研传播纠错链。
- `domains/research-participant-consent-community-engagement/` 负责研究参与者知情同意、退出、再联系、社区参与、结果回馈和研究信任。
- `domains/biobanking-biospecimen-quality-chain-of-custody/` 负责生物样本库、样本质量、预分析变量、冷链、追踪和保管链。
- `domains/longitudinal-cohort-retention-followup-infrastructure/` 负责纵向队列、长期随访、参与者留存、失访、事件确认和生命历程数据基础设施。
- `domains/registries-real-world-data-governance/` 负责患者/疾病/产品登记、真实世界数据、真实世界证据、数据质量和用途边界。
- `domains/scientific-instrumentation-sensor-calibration-maintenance/` 负责科研仪器、传感器、校准、漂移、维护和测量不确定性。
- `domains/nanomedicine-targeted-delivery-molecular-repair/` 负责纳米医学、靶向递送、纳米材料、分子诊断和远期分子修复证据边界。
- `domains/ai-drug-discovery-protein-design/` 负责 AI 药物发现、蛋白设计、结构预测、生成式分子设计和自动化实验闭环。
- `domains/epigenetic-editing-gene-regulation-therapeutics/` 负责表观遗传编辑、基因表达调控、转录沉默/激活和状态改写疗法边界。
- `domains/brain-preservation-connectomics-emulation/` 负责脑保存、连接组学、神经结构可读性、全脑仿真和上传假设审查。
- `domains/post-quantum-cryptography-long-term-data-security/` 负责后量子密码、长期数据安全、加密迁移和未来解密风险。
- `domains/safety-critical-software-formal-methods/` 负责安全关键软件、形式化方法、验证确认、运行时监控和失效安全。
- `domains/long-term-digital-preservation-format-migration/` 负责长期数字保存、格式迁移、校验、元数据、备份和可读性治理。
- `domains/cerebrovascular-stroke-brain-perfusion-resilience/` 负责卒中、脑灌注、脑血管事件、再灌注窗口和长期功能恢复。
- `domains/traumatic-brain-injury-neurotrauma-recovery/` 负责 TBI、脑震荡、重复头部冲击、神经创伤恢复和长期后遗症。
- `domains/delirium-acute-cognitive-failure-prevention/` 负责谵妄、ICU/住院急性认知失败、术后认知风险和可预防诱因。
- `domains/disorders-of-consciousness-coma-recovery/` 负责昏迷、无反应觉醒、最低意识状态、意识评估、康复和照护伦理。
- `domains/epilepsy-seizure-network-stability/` 负责癫痫、发作频率、脑网络兴奋性、治疗连续性和发作相关伤害。
- `domains/autonomic-nervous-system-homeostasis/` 负责自主神经、心率血压调节、体位耐受、出汗、消化排尿和压力恢复。
- `domains/migraine-headache-effective-time-burden/` 负责偏头痛、头痛障碍、感官敏感、认知雾、发作不可预测性和有效时间负担。
- `domains/insurance-risk-transfer/` 负责健康、失业、工伤、残障、灾害、存款、养老金等风险转移和风险池。
- `domains/childcare-family-continuity/` 负责托育可及、托育费用、照护质量、早期儿童发展、父母工作连续性和家庭压力。
- `domains/emergency-preparedness-response/` 负责灾害准备、预警、应急通信、急救医疗、安置、公共卫生应急和灾后恢复。
- `domains/personal-safety-violence-prevention/` 负责人身安全、暴力预防、求助入口、受害者服务、法律保护和创伤支持。
- `domains/product-safety-recall-systems/` 负责消费品、食品、药品、医疗器械、车辆缺陷报告、召回通知、纠正措施和风险沟通。
- `domains/cellular-reprogramming/` 负责山中因子、部分重编程、化学重编程、AI 因子设计和表观遗传编辑等细胞状态可重写谱系，不提供实验协议或人体应用建议。
- `domains/regenerative-medicine/` 负责干细胞、组织工程、器官再生、类器官、移植和生物制造的高层研究框架。
- `domains/rehabilitation-functioning/` 负责康复、功能恢复、失能预防、活动能力、自理、沟通和社会参与。
- `domains/cancer-control/` 负责癌症预防、早筛、治疗、复发、肿瘤演化和长期风险治理。
- `domains/immune-maintenance/` 负责免疫衰老、感染防御、慢性炎症、自身免疫和免疫监视。
- `domains/antimicrobial-resilience/` 负责抗微生物耐药、感染控制和现代医学抗感染底座。
- `domains/neuro-continuity/` 负责大脑、记忆、意识、人格和主体身份连续性。
- `domains/sensory-continuity/` 负责视觉、听觉、平衡、触觉和感官反馈连续性。
- `domains/future-waiting/` 负责度规红移固有时差分路径（黑洞等待室）等“压缩等待 / 去未来”思想实验、证据边界和风险约束。
- `domains/vision-eye-health-continuity/`、`domains/hearing-auditory-communication-continuity/`、`domains/vestibular-balance-spatial-orientation/`、`domains/speech-language-communication-continuity/`、`domains/swallowing-dysphagia-aspiration-nutrition/`、`domains/smell-taste-chemosensory-continuity/` 和 `domains/peripheral-neuropathy-somatosensory-continuity/` 负责视觉输入、听觉沟通、空间平衡、语言表达、吞咽摄食、化学感知和身体边界反馈的机制、证据、变量和禁止用途。
- `domains/space-weather-geomagnetic-storm-resilience/`、`domains/planetary-defense-near-earth-object-risk/`、`domains/volcanic-ashfall-geohazard-continuity/`、`domains/earthquake-seismic-risk-built-environment-continuity/`、`domains/tsunami-warning-coastal-evacuation-continuity/` 和 `domains/extreme-heat-cooling-public-health-continuity/` 负责空间天气、行星防御、火山灰、地震、海啸和极端高温这些行星、地球物理与极端热风险的机制、预警、基础设施失效和禁止用途。
- `domains/noise-exposure-acoustic-environment-continuity/`、`domains/light-exposure-circadian-environment-continuity/`、`domains/lead-heavy-metal-exposure-control/`、`domains/radon-asbestos-indoor-hazard-continuity/`、`domains/mold-dampness-indoor-biological-exposure/` 和 `domains/vector-borne-disease-environmental-control/` 负责噪声、光照节律、铅与重金属、氡与石棉、霉菌潮湿和病媒传播这些慢性环境暴露与日常损耗条件的机制、证据、变量和禁止用途。
- `domains/advance-care-planning-medical-decision-continuity/`、`domains/supported-decision-making-guardianship-rights/`、`domains/healthcare-personal-representative-hipaa-access-continuity/`、`domains/financial-fiduciary-power-of-attorney-continuity/`、`domains/representative-payee-benefits-management-continuity/` 和 `domains/trust-estate-affairs-succession-continuity/` 负责预先医疗照护计划、支持性决策、医疗个人代表、财务受托、代表收款人和事务继承这些决策权、代理权与受托连续性条件。
- `domains/credit-consumer-reporting-access-continuity/`、`domains/tenant-screening-rental-access-continuity/`、`domains/background-check-record-screening-continuity/`、`domains/employment-algorithmic-hiring-screening-continuity/`、`domains/insurance-underwriting-algorithmic-risk-scoring-continuity/` 和 `domains/public-benefits-eligibility-automated-decision-continuity/` 负责信用/消费者报告、租房筛查、背景记录筛查、算法招聘、保险算法评分和公共福利自动资格系统这些算法化准入、筛查与资格连续性条件。
- `domains/education-record-transcript-verification-continuity/`、`domains/professional-licensure-certification-continuity/`、`domains/skills-competency-credentialing-continuity/`、`domains/continuing-education-recertification-continuity/`、`domains/apprenticeship-work-based-learning-continuity/` 和 `domains/verifiable-credential-wallet-interoperability/` 负责教育记录核验、职业证照认证、技能胜任力凭证、继续教育再认证、学徒制工作中学习和可验证凭证钱包互操作这些资格证明、授权与能力可携带连续性条件。
- `domains/income-payroll-employment-record-continuity/`、`domains/tax-administration-filing-record-continuity/`、`domains/social-security-earnings-benefit-record-continuity/`、`domains/retirement-pension-savings-plan-continuity/`、`domains/unemployment-insurance-wage-record-continuity/` 和 `domains/workers-compensation-occupational-injury-benefit-continuity/` 负责工资雇佣记录、税务申报记录、社会保险收入与福利记录、退休养老金计划、失业保险工资记录和工伤职业伤害权益这些劳动成果到未来保障的记录连续性条件。
- `domains/family-medical-leave-job-protection-continuity/`、`domains/paid-sick-family-leave-wage-replacement-continuity/`、`domains/pregnancy-parental-work-continuity/`、`domains/workplace-accommodation-return-to-work-continuity/`、`domains/disability-income-work-capacity-benefit-continuity/` 和 `domains/family-caregiver-respite-work-continuity/` 负责家庭医疗假岗位保护、带薪病假/家庭假工资替代、孕产育儿工作连续性、合理便利复工、残障收入与工作能力福利、家庭照护者喘息与工作连续性这些工作中断与照护事件连续性条件。
- `domains/vital-records-life-event-continuity/`、`domains/name-change-identity-record-synchronization-continuity/`、`domains/address-residency-mail-service-continuity/`、`domains/household-composition-dependent-eligibility-continuity/`、`domains/family-law-custody-child-support-continuity/` 和 `domains/kinship-foster-adoption-care-continuity/` 负责生命事件记录、姓名变更同步、地址居住地邮件路由、家庭组成资格关系、家庭法监护抚养、亲属照护寄养收养这些家庭事实与制度记录连续性条件。
- `domains/banking-deposit-account-access-continuity/`、`domains/debt-obligation-collection-relief-continuity/`、`domains/real-property-title-deed-record-continuity/`、`domains/driver-license-vehicle-registration-continuity/`、`domains/passport-travel-document-mobility-continuity/`、`domains/contract-subscription-billing-consent-continuity/` 和 `domains/notary-document-authentication-signature-continuity/` 负责银行账户存款访问、债务义务催收救济、不动产权属地契、驾照车辆登记、护照旅行证件、合同订阅账单、公证文件认证签名这些资源控制、移动资格与交易执行连续性条件。
- `domains/citizenship-nationality-statelessness-continuity/`、`domains/immigration-status-residency-work-authorization-continuity/`、`domains/asylum-refugee-protection-status-continuity/`、`domains/detention-custody-confinement-status-continuity/`、`domains/civil-commitment-involuntary-treatment-rights-continuity/`、`domains/court-notice-service-process-default-judgment-continuity/` 和 `domains/criminal-record-relief-collateral-consequences-continuity/` 负责公民国籍无国籍、移民居留工作授权、庇护难民保护、拘押羁押监管状态、非自愿治疗权利、法院通知缺席判决和犯罪记录附带后果这些法律状态与强制程序连续性条件。
- `domains/school-enrollment-attendance-continuity/`、`domains/special-education-iep-504-accommodation-continuity/`、`domains/school-meals-nutrition-access-continuity/`、`domains/school-health-services-chronic-condition-continuity/`、`domains/school-transportation-safe-routes-continuity/`、`domains/school-discipline-exclusion-restraint-continuity/`、`domains/school-mental-health-counseling-support-continuity/` 和 `domains/school-climate-bullying-violence-prevention-continuity/` 负责入学出勤、特殊教育 IEP/504、校餐营养、学校健康服务、通学安全、纪律排除约束、学校心理健康、学校气候欺凌暴力预防这些学校服务连续性条件。
- `domains/postsecondary-admissions-transfer-articulation-continuity/`、`domains/student-financial-aid-grant-scholarship-continuity/`、`domains/academic-advising-degree-progress-continuity/`、`domains/campus-basic-needs-student-support-continuity/`、`domains/campus-disability-accommodations-accessibility-continuity/`、`domains/campus-mental-health-crisis-student-support-continuity/`、`domains/campus-safety-title-ix-clery-continuity/` 和 `domains/international-student-sevis-status-continuity/` 负责高等教育入学转学衔接、学生资助奖助学金、学业指导学位进度、校园基本需求、校园残障便利、校园心理危机支持、校园安全 Title IX/Clery 和国际学生 SEVIS 身份连续性这些高等教育学生生命周期条件。
- `domains/email-account-recovery-continuity/`、`domains/phone-number-sim-portability-account-security-continuity/`、`domains/mfa-passkey-credential-recovery-continuity/`、`domains/password-manager-secret-vault-continuity/`、`domains/cloud-backup-file-sync-data-portability-continuity/`、`domains/messaging-contact-graph-portability-continuity/`、`domains/domain-dns-web-presence-continuity/` 和 `domains/platform-account-suspension-appeals-continuity/` 负责邮箱账号恢复、手机号 SIM 携转安全、MFA/passkey 凭证恢复、密码管理器密钥库、云备份文件同步数据可携带、消息联系人图谱可携带、域名 DNS Web 存在和平台账号停权申诉这些数字账户与通信可达连续性条件。
- `domains/personal-computing-device-lifecycle-repair-continuity/`、`domains/home-network-router-iot-security-continuity/`、`domains/software-supply-chain-dependency-provenance-continuity/`、`domains/software-update-vulnerability-patch-continuity/`、`domains/open-source-maintainer-sustainability-continuity/`、`domains/pki-certificate-cryptographic-trust-continuity/`、`domains/cloud-service-exit-interoperability-continuity/` 和 `domains/api-platform-dependency-runtime-continuity/` 负责个人计算设备生命周期维修、家庭网络路由器 IoT 安全、软件供应链来源证明、软件更新补丁、开源维护者可持续、PKI 证书密码信任、云服务退出互操作和 API 平台运行时依赖这些软件、设备与信任连续性条件。
- `domains/calendar-scheduling-appointment-continuity/`、`domains/notification-alert-routing-attention-continuity/`、`domains/reminder-alarm-routine-task-continuity/`、`domains/meeting-video-conferencing-remote-collaboration-continuity/`、`domains/document-capture-ocr-pdf-record-workflow-continuity/`、`domains/search-index-discovery-retrieval-continuity/`、`domains/personal-automation-integration-workflow-continuity/` 和 `domains/collaborative-document-permission-version-continuity/` 负责日历排程预约、通知警报路由、提醒闹钟例行任务、会议视频远程协作、文件捕获 OCR PDF 记录流、搜索索引发现检索、个人自动化集成工作流和协作文档权限版本这些个人操作与任务协调连续性条件。
- `domains/home-access-lock-key-entry-continuity/`、`domains/household-appliance-maintenance-repair-continuity/`、`domains/home-refrigeration-food-storage-continuity/`、`domains/cooking-meal-preparation-kitchen-safety-continuity/`、`domains/laundry-clothing-footwear-hygiene-continuity/`、`domains/household-cleaning-disinfection-pest-control-continuity/`、`domains/postal-parcel-delivery-pickup-continuity/` 和 `domains/household-maintenance-repair-contractor-continuity/` 负责住所进入、家电维护、家庭冷藏、烹饪备餐、衣物鞋履卫生、家庭清洁消毒害虫控制、邮件包裹接收和家庭维修承包商这些家庭物理运行连续性条件。
- `domains/disembodied-cns/` 负责去具身外部维持型中枢生命系统的高层架构建模，不提供实验操作协议。
- `domains/memory-editing/` 负责记忆编辑的概念、证据、验证和伦理边界，不提供可执行神经操控步骤。
- `domains/biostasis-cryopreservation/` 负责冷冻保存、生物停滞、休眠和等待未来修复路径。
- `domains/cognitive-augmentation/` 负责 AI 辅助、外部记忆、学习系统、脑机接口和行动放大工具。
- `domains/ai-agency-safety/` 负责 AI 代理、工具调用、授权、监督、审计、回滚和失效隔离。
- `domains/digital-identity-security/` 负责数字身份、账号、凭据、身份恢复、服务入口和数据可携带。
- `domains/mental-health-affective-stability/` 负责心理健康、情绪稳定、动机、成瘾、创伤和自杀风险。
- `domains/sleep-circadian-recovery/` 负责睡眠、昼夜节律、疲劳和恢复系统。
- `domains/assistive-technology-access/` 负责辅助技术、无障碍、义肢、助听、低视力辅助、轮椅和沟通辅助。
- `domains/substance-exposure-control/` 负责烟草、酒精、成瘾性物质、有害暴露和主体自主性风险。
- `domains/risk-engineering/` 负责事故、灾害、暴力、环境风险、系统故障和尾部风险工程。
- `domains/planetary-health-environment/` 负责空气、水、气候、污染、生态系统和食物系统。
- `domains/resource-social-infra/` 负责食物、水、能源、住房、医疗、照护、金融、教育、就业和社会支持。
- `domains/supply-chain-continuity/` 负责药品、能源、食物、设备、通信、芯片、物流和替代路径。
- `domains/synthetic-biology-biosecurity/` 负责合成生物学、生物安全、生物安保、双重用途风险和治理边界。
- `domains/space-extreme-habitation/` 负责空间飞行、极端环境、闭环生命支持、隔离、辐射和远程医疗。
- `domains/social-connection-relational-infra/` 负责社会连接、孤独、社会隔离、家庭照护网络、信任和社区关系。
- `domains/governance-rights/` 负责主体权利、法律身份、同意、退出、数据权、AI 治理和研究伦理。
- `domains/pain-suffering-control/` 负责疼痛、痛苦、症状负担、姑息医学和可承受持续性。
- `domains/health-literacy-navigation/` 负责健康素养、医疗服务导航、可理解信息、风险沟通和共同决策。
- `domains/language-access-plain-communication/` 负责清晰语言、语言服务、有限英语能力访问、CLAS、认知可访问性和关键服务材料理解。
- `domains/labor-rights-workplace-protection/` 负责劳动标准、工资工时、安全权利、反歧视、反报复、申诉入口和劳动组织治理。
- `domains/oral-health-continuity/` 负责口腔健康、牙齿、牙周、咀嚼、疼痛、感染、营养和沟通连续性。
- `domains/measurement-feedback/` 负责主体状态测量、风险评分、生物标志物、可穿戴、预测模型和反馈闭环。
- 原始资料归档在 `docs/source-notes/`；稳定结论必须沉淀到 `docs/` 或对应子域 README，不能长期依赖零散临时文件名。

## 设计原则

- Human Infra 的上位对象是“人类任务执行系统”，不是单一长寿产品。
- Longevity Evidence 承接原 Biocat，但不再占据根目录概念中心。
- “永生”的不同路径必须按机制拆分：长寿证据、营养代谢、基因组稳定性、端粒维护、蛋白稳态、自噬、线粒体、细胞衰老、细胞外基质与糖化、微生物生态、干细胞储备、肝肾清除、消化屏障与吸收、呼吸氧合、血液氧运与止血、内分泌激素调节、淋巴与脑淋巴清除、体液电解质酸碱稳态、热稳态、身体活动、心血管韧性、肌骨完整性、皮肤屏障与伤口愈合、泌尿生殖连续性、生殖与生育连续性、注意力与执行控制、学习与技能获得、教育可及与终身学习、时间分配与有效时间、财务韧性、金融包容与支付系统、就业服务、健康劳动力容量、职业与工作设计、信息完整性与信任、媒体信息素养与公共图书馆、科研基础设施与开放科学转化、标准计量与质量基础设施、网络安全韧性与关键服务、算力数据中心与 AI 基础设施、临床试验与监管科学转化、空间定位导航与位置基础设施、天气气候观测与预报、空间天气与地磁暴、行星防御与近地天体、火山灰、地震、海啸、极端高温与制冷公共卫生、建筑消防与生命安全规范、制造与维修能力、公共采购与合同能力、动物健康与 One Health 界面、公共卫生实验室与诊断能力、血液器官组织生物警戒、废弃物与危险材料连续性、辐射核安全防护、化学安全与中毒控制、关键矿物材料韧性、食物安全、水卫生连续性、能源韧性、医疗服务连续性、社区健康工作者与同伴支持、药品与治疗连续性、患者数据互操作、远程照护、健康数据隐私治理、功能与生活质量结局、健康经济与价值评估、免疫与公共卫生监测、母婴儿童早期生命、患者安全与组织学习、社会决定因素与社区脆弱性、公共服务设计与可达性、行政负担与程序摩擦、公民数据与开放政府透明、社区资源导航、照护与长期照护、住房与建成环境、交通接入、法律身份与民事登记、司法可及与法律援助、公民参与与选举接入、迁移流离失所与人道连续性、数字包容与连接、社会保护与福利递送、保险与风险转移、托育与家庭连续性、劳动权利与工作场所保护、语言可达与清晰沟通、应急准备与响应、应急预警与通信、家庭应急准备与韧性、灾后恢复与救济连续性、人身安全与暴力预防、产品安全与召回系统、细胞重编程、基因治疗与基因编辑递送安全、生物年龄钟验证、多组学个人基线、工程细胞疗法、类器官组织芯片模型、异种移植与工程器官替换、再生医学、康复功能、癌症控制、免疫维护、抗微生物韧性、神经连续性、感官连续性、未来等待、生物停滞、去具身中枢、记忆编辑、认知增强、AI 代理安全、数字身份安全、心理稳定、睡眠恢复、辅助技术、社会连接、物质暴露控制、资源环境、供应链连续性、合成生物学与生物安全、空间极端栖居、风险工程、健康素养导航、治理权利、口腔健康、痛苦控制和测量反馈不能混成一个概念桶。
- 所有健康、神经、生命支持相关结论必须保留来源、适用对象、不确定性和伦理边界。
- 新增研究域必须能回到 `docs/reference/research-domain-atlas.md` 的先验条件和域判定契约。
- 自研代码只做连接、清洗、归一化、证据编排和产品表达；优先复用官方 API、公开数据库和成熟工具。

## 维护规则

- 架构级新增、删除、移动目录时，必须同步更新本文件和目标目录下的 `AGENTS.md`。
- 子域新增数据或脚本前，先确认它是否属于现有子域；若不属于，先更新 `docs/reference/domain-map.md` 再建目录。
- 不把远期研究域伪装成当前可执行产品。
- 不把 AI 总结当作事实源；公开结论必须能回到原始资料或公开数据库。
- 应用框架只允许用于明确产品形态和验证路径的展示层；当前正式 Web 展示统一收敛到 `web/` 的 Observable Framework 结构。

## 变更日志

- 2026-06-30：新增第四十二波 6 个工作中断与照护事件连续性域，覆盖家庭医疗假岗位保护、带薪病假/家庭假工资替代、孕产育儿工作连续性、合理便利复工、残障收入与工作能力福利、家庭照护者喘息与工作连续性。
- 2026-06-30：新增第四十三波 6 个生命事件、家庭关系与制度记录连续性域，覆盖生命事件记录、姓名变更同步、地址居住地邮件路由、家庭组成资格关系、家庭法监护抚养、亲属照护寄养收养。
- 2026-06-30：新增第四十四波 7 个资源控制、移动资格与交易执行连续性域，覆盖银行账户存款访问、债务义务催收救济、不动产权属地契、驾照车辆登记、护照旅行证件、合同订阅账单、公证文件认证签名。
- 2026-06-30：新增第四十五波 7 个法律状态、保护身份、强制程序与记录救济连续性域，覆盖公民国籍无国籍、移民居留工作授权、庇护难民保护、拘押羁押监管状态、非自愿治疗权利、法院通知缺席判决和犯罪记录附带后果。
- 2026-06-30：新增第四十六波 8 个学校服务连续性域，覆盖入学出勤、特殊教育 IEP/504、校餐营养、学校健康服务、通学安全、纪律排除约束、学校心理健康和学校气候欺凌暴力预防。
- 2026-06-30：新增第四十七波 8 个高等教育学生生命周期连续性域，覆盖入学转学衔接、学生资助奖助学金、学业指导学位进度、校园基本需求、校园残障便利、校园心理危机支持、校园安全 Title IX/Clery 和国际学生 SEVIS 身份。
- 2026-06-30：新增第四十八波 8 个数字账户与通信可达连续性域，覆盖邮箱账号恢复、手机号 SIM 携转安全、MFA/passkey 凭证恢复、密码管理器密钥库、云备份文件同步数据可携带、消息联系人图谱可携带、域名 DNS Web 存在和平台账号停权申诉。
- 2026-06-30：新增第四十九波 8 个软件、设备与信任连续性域，覆盖个人计算设备生命周期维修、家庭网络路由器 IoT 安全、软件供应链依赖来源证明、软件更新漏洞补丁、开源维护者可持续、PKI 证书密码信任、云服务退出互操作和 API 平台运行时依赖。
- 2026-06-20：从 Biocat 单项目重组为 Human Infra 总项目；旧 Biocat 迁入 `domains/longevity-evidence/`；新增 `disembodied-cns` 与 `memory-editing` 子域；四份最新资料归档到 `docs/source-notes/`；按 Docs-as-Code 和 Diataxis 补齐根文件、协作模板、文档分层和结构检查脚本。
- 2026-06-22：新增 `domains/future-waiting/` 和度规红移固有时差分路径（黑洞等待室），用于承载“压缩等待 / 去未来”类永生路径思想实验。
- 2026-06-23：新增 GitHub Actions `make check` 门禁和 `.github/AGENTS.md`，准备远程仓库协作入口。
- 2026-06-26：新增根目录静态 Web 看板 `human-infra-dashboard.html`，采用黄金分割三块布局展示主体持续性与生命路径预测模型。
- 2026-06-26：新增专项 Web 展示页 `singularity-human-infra.html`，将《奇点更近》学习资料转译为 Human Infra 价值展示、预测模型和可视化。
- 2026-06-26：新增 `web/` Observable Framework 应用，作为科研叙事、书籍转译、预测模型和交互图表的正式 Web 入口。
- 2026-06-27：新增 `tools/arxiv_html_paper_tool.py` 与 `tools/arxiv-html-paper/`，把 arXiv HTML papers 前端框架沉淀为可复用 Astro 工具链。
- 2026-06-29：新增可控度规等待室假设 working paper 入口和审计账本，把黑洞等待室收敛为固有时差分、退出采用、风险扣减和递归等待的可审查模型。
- 2026-06-30：新增第四十一波 6 个收入、税务、社保、退休、失业和工伤权益记录连续性域，覆盖工资雇佣记录、税务申报记录、社会保险收入与福利记录、退休养老金计划、失业保险工资记录和工伤职业伤害权益。
- 2026-06-30：新增第四十波 6 个资格证明、证照与能力可携带连续性域，覆盖教育记录核验、职业证照认证、技能胜任力凭证、继续教育再认证、学徒制工作中学习和可验证凭证钱包互操作。
- 2026-06-30：新增第三十九波 6 个算法化准入、筛查与资格连续性域，覆盖信用与消费者报告、租房筛查、背景记录筛查、算法招聘、保险算法评分和公共福利自动资格系统。
- 2026-06-30：新增第三十八波 6 个决策权、代理权与受托连续性域，覆盖预先医疗照护计划、支持性决策、医疗个人代表、财务受托、代表收款人和事务继承。
- 2026-06-30：新增第三十七波 6 个慢性环境暴露与日常损耗条件域，覆盖噪声、光照节律、铅与重金属、氡与石棉、霉菌潮湿和病媒传播风险。
- 2026-06-30：新增第三十六波 6 个行星、地球物理与极端热风险连续性域，覆盖空间天气、行星防御、火山灰、地震、海啸和极端高温。
- 2026-06-30：新增第三十五波 7 个感官、沟通与具身反馈连续性域，覆盖视觉眼健康、听力听觉沟通、前庭平衡空间定向、言语语言沟通、吞咽误吸营养、嗅味觉化学感知和周围神经躯体感觉。
- 2026-06-30：新增农业生产、土壤土地、水资源、生态系统服务、野火韧性和物流冷链六个研究域，补齐初级生产、自然系统与物理流通底座。
- 2026-06-30：新增海岸海洋蓝色经济、渔业水生食物、防洪工程安全、公共工程资产管理、城市土地使用规划和城市绿蓝基础设施六个研究域，补齐自然-工程-城市交界底座。
- 2026-06-30：新增电网可靠性、水务污水公用事业、燃料热能服务、公共交通运营、关键基础设施生命线互依赖和公用事业可负担性断供保护六个研究域，补齐公用事业生命线连续性底座。
- 2026-06-30：新增基因治疗与基因编辑递送安全、生物年龄钟验证、多组学个人基线、工程细胞疗法、类器官组织芯片模型和异种移植工程器官替换六个研究域，补齐生物医学平台层。
- 2026-06-30：新增因果推断与目标试验模拟、生存分析与健康寿命风险建模、人类数字孪生生命历程仿真、实施科学与依从行为改变、不确定性量化与模型校准、数据质量缺失代表性六个研究域，补齐定量方法学层。
- 2026-06-30：新增隐私保护计算、知识图谱本体语义互操作、模型卡 AI 审计文档、技术预见地平线扫描、研究组合资金治理和知识产权技术转移可及六个研究域，补齐知识治理与技术扩散层。
- 2026-06-30：新增可信科研传播与同行评审、研究参与者同意与社区参与、生物样本库保管链、纵向队列随访、登记与真实世界数据治理、科研仪器与传感器校准维护六个研究域，补齐科研证据基础设施层。
- 2026-06-30：新增复杂照护导航、交接与决策连续性域，覆盖罕见病诊断漫游、多病共存多重用药、出院交接、居家/缓和/安宁疗护、医疗解释文化中介和患者共同决策。
- 2026-06-30：新增外部化主体连续性域，覆盖生命日志个人档案、数字遗产继承、可穿戴连续感知、个人知识管理认知卸载、脑机接口治理和机器人具身辅助。
- 2026-06-30：新增 `domains/cellular-reprogramming/`，承载山中因子、部分重编程、化学重编程、AI 因子设计和表观遗传编辑的机制谱系与安全边界。
- 2026-06-30：新增第十四波公共服务、应急、金融和就业相关域：社会决定因素与社区脆弱性、公共服务设计与可达性、应急预警与通信、灾后恢复与救济连续性、金融包容与支付系统、劳动力与就业服务。
- 2026-06-30：新增 `docs/reference/research-domain-atlas.md` 和 10 个研究域骨架，把有效永生的先验条件映射为可独立维护的研究域。
- 2026-06-30：新增第二波 8 个研究域骨架，覆盖康复功能、心理稳定、睡眠恢复、辅助技术、抗微生物韧性、环境底座、感官连续性和痛苦控制。
- 2026-06-30：新增第三波 8 个研究域骨架，覆盖营养代谢、身体活动、心血管韧性、肌骨完整性、社会连接、物质暴露控制、健康素养导航和口腔健康连续性。
- 2026-06-30：新增第四波 8 个分子维护研究域骨架，覆盖基因组稳定性、端粒维护、蛋白稳态、自噬、线粒体生物能量学、细胞衰老清除、微生物生态、干细胞储备和肝肾清除。
- 2026-06-30：新增第五波 5 个外部技术风险域骨架，覆盖数字身份安全、AI 代理安全、供应链连续性、合成生物学与生物安全、空间与极端栖居。
- 2026-06-30：新增第六波 6 个生理与结构维护域骨架，覆盖呼吸氧合、内分泌激素调节、血液氧运与止血、皮肤屏障与伤口愈合、细胞外基质与糖化、淋巴与脑淋巴清除。
- 2026-06-30：新增第七波 5 个基础稳态与未来选择权域骨架，覆盖消化屏障与吸收、体液电解质酸碱稳态、热稳态、泌尿生殖连续性、生殖与生育连续性。
- 2026-06-30：新增第八波 6 个主体代理与任务资源域骨架，覆盖注意力与执行控制、学习与技能获得、时间分配与有效时间、财务韧性、职业与工作设计、信息完整性与信任。
- 2026-06-30：新增第九波 6 个服务接入与生活连续性域骨架，覆盖医疗服务连续性、照护与长期照护、住房与建成环境、交通接入、法律身份与民事登记、应急准备与响应。
- 2026-06-30：新增第十波 6 个基础生计与风险分摊域骨架，覆盖食物安全与营养可及、水卫生连续性、能源可及与韧性、社会保护与福利递送、保险与风险转移、托育与家庭连续性。
- 2026-06-30：新增第十一波 6 个制度参与、人道连续性与公共安全域骨架，覆盖司法可及与法律援助、公民参与与选举接入、迁移流离失所与人道连续性、数字包容与连接、人身安全与暴力预防、产品安全与召回系统。
- 2026-06-30：新增第十二波 6 个治疗、服务理解与劳动保护域骨架，覆盖药品与治疗连续性、患者数据互操作、远程医疗与居家监测、社区资源导航、语言可达与清晰沟通、劳动权利与工作场所保护。
- 2026-06-30：新增第十三波 6 个数据治理、结局评估与公共卫生安全域骨架，覆盖健康数据隐私治理、功能与生活质量结局、健康经济与价值评估、免疫与公共卫生监测、母婴儿童早期生命、患者安全与组织学习。
- 2026-06-30：新增第十五波 6 个家庭准备、信息素养、健康劳动力、行政摩擦、社区中介和开放政府透明域骨架，覆盖家庭应急准备、媒体信息素养与公共图书馆、健康劳动力容量、行政负担与程序摩擦、社区健康工作者与同伴支持、公民数据与开放政府透明。
- 2026-06-30：新增第十六波 6 个教育、科研、标准、网络安全、算力和临床转化域骨架，覆盖教育可及与终身学习、科研基础设施与开放科学转化、标准计量与质量基础设施、网络安全韧性与关键服务、算力数据中心与 AI 基础设施、临床试验与监管科学转化。
- 2026-06-30：新增第十七波 6 个空间、天气、建筑、制造、采购和 One Health 相关域骨架，覆盖空间定位导航与位置基础设施、天气气候观测与预报、建筑消防与生命安全规范、制造与维修能力、公共采购与合同能力、动物健康与人兽共患界面。
- 2026-06-30：新增第十八波 6 个实验室、人体材料、废弃物、辐射、化学和关键材料相关域骨架，覆盖公共卫生实验室诊断能力、血液器官组织生物警戒、废弃物危险材料连续性、辐射核安全防护、化学安全中毒控制和关键矿物材料韧性。
- 2026-06-30：新增第十九波 6 个日常环境与工具可靠性域骨架，覆盖空气质量通风、食品安全污染控制、职业暴露工业卫生、医疗设备安全维护、灭菌消毒感染控制和建成环境无障碍通用设计。
- 2026-06-30：新增第二十波 6 个临床可靠性与急性风险窗口域骨架，覆盖临床检验诊断质量、药物警戒药品安全、药品质量供应完整性、急救医疗服务院前照护、手术麻醉围手术期安全和道路交通伤害预防。
- 2026-06-30：新增第二十一波 6 个结构性脆弱与连续照护断点域骨架，覆盖农村健康可及、无家可归健康连续性、羁押重返健康连续性、残障独立生活、痴呆认知衰退照护和慢性传染病照护连续性。
- 2026-06-30：新增第二十二波 6 个危机、剥削与恢复连续性域骨架，覆盖自杀危机响应、物质使用障碍治疗恢复、老年正义成人保护、儿童保护家庭安全、诈骗消费者保护和在线数字伤害预防。
- 2026-06-30：新增第二十五波 6 个文明连续性、集体安全与宏观制度底座域骨架，覆盖武装冲突平民保护、和平建设冲突预防、政府连续性、电信网络韧性、宏观经济稳定和公共廉洁问责。
- 2026-06-30：新增第三十三波 7 个未来技术连续性域骨架，覆盖纳米医学靶向递送、AI 药物发现蛋白设计、表观遗传编辑、脑保存连接组仿真、后量子密码、安全关键软件形式化方法和长期数字保存。
- 2026-06-30：新增第三十四波 7 个急性神经连续性与意识韧性域骨架，覆盖卒中脑灌注韧性、TBI 神经创伤恢复、谵妄急性认知失败预防、意识障碍昏迷恢复、癫痫发作网络稳定、自主神经稳态和偏头痛有效时间负担。
