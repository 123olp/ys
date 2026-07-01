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
    ├── cataract-vision-restoration-continuity/ # 白内障与视觉恢复连续性
    ├── glaucoma-visual-field-protection-continuity/ # 青光眼与视野保护连续性
    ├── diabetic-retinopathy-screening-treatment-continuity/ # 糖尿病视网膜病变筛治连续性
    ├── age-related-macular-degeneration-central-vision-continuity/ # AMD 与中央视觉连续性
    ├── refractive-error-glasses-contact-lens-continuity/ # 屈光不正与矫正工具连续性
    ├── low-vision-rehabilitation-assistive-technology-continuity/ # 低视力康复与辅助技术连续性
    ├── dry-eye-ocular-surface-comfort-continuity/ # 干眼与眼表舒适连续性
    ├── eye-injury-urgent-vision-protection-continuity/ # 眼外伤急性视觉保护连续性
    ├── pediatric-vision-screening-amblyopia-continuity/ # 儿童视力筛查与弱视连续性
    ├── retinal-detachment-urgent-referral-continuity/ # 视网膜脱离急转连续性
    ├── hearing-auditory-communication-continuity/ # 听力与听觉沟通连续性
    ├── age-related-hearing-loss-hearing-aid-continuity/ # 年龄相关听损与助听连续性
    ├── noise-induced-hearing-loss-prevention-continuity/ # 噪声性听损预防连续性
    ├── tinnitus-sound-tolerance-sleep-continuity/ # 耳鸣、声音耐受与睡眠连续性
    ├── otitis-media-child-hearing-development-continuity/ # 儿童中耳炎与听觉发育连续性
    ├── sudden-hearing-loss-urgent-referral-continuity/ # 突发听损急转连续性
    ├── cochlear-implant-communication-continuity/ # 人工耳蜗沟通连续性
    ├── newborn-hearing-screening-language-development-continuity/ # 新生儿听筛与语言发展连续性
    ├── auditory-processing-listening-effort-continuity/ # 听觉处理与听觉努力连续性
    ├── hearing-assistive-devices-alerting-access-continuity/ # 听觉辅助设备与警报接入连续性
    ├── captions-relay-service-communication-access-continuity/ # 字幕中继与沟通访问连续性
    ├── vestibular-balance-spatial-orientation/ # 前庭、平衡与空间定向
    ├── bppv-positional-vertigo-continuity/ # BPPV 与位置性眩晕连续性
    ├── menieres-disease-episodic-vertigo-continuity/ # 梅尼埃病发作性眩晕连续性
    ├── vestibular-neuritis-labyrinthitis-acute-vertigo-continuity/ # 前庭神经炎/迷路炎急性眩晕连续性
    ├── persistent-postural-perceptual-dizziness-continuity/ # PPPD 慢性头晕连续性
    ├── vestibular-migraine-dizziness-sensory-load-continuity/ # 前庭性偏头痛与感官负荷连续性
    ├── bilateral-vestibular-hypofunction-gaze-gait-stability-continuity/ # 双侧前庭低下与凝视步态连续性
    ├── vestibular-rehabilitation-balance-compensation-continuity/ # 前庭康复与平衡补偿连续性
    ├── gait-balance-assessment-fall-screening-continuity/ # 步态平衡评估与跌倒筛查连续性
    ├── motion-sickness-transport-virtual-environment-tolerance-continuity/ # 运动病与虚拟环境耐受连续性
    ├── vestibular-ototoxicity-medication-chemical-risk-continuity/ # 耳毒性药物/化学前庭风险连续性
    ├── speech-language-communication-continuity/ # 言语、语言与沟通连续性
    ├── aphasia-language-access-recovery-continuity/ # 失语语言访问与恢复连续性
    ├── dysarthria-speech-intelligibility-continuity/ # 构音障碍与言语可懂度连续性
    ├── apraxia-of-speech-motor-planning-continuity/ # 言语失用与运动计划连续性
    ├── voice-disorders-phonation-communication-continuity/ # 嗓音障碍与发声沟通连续性
    ├── stuttering-fluency-participation-continuity/ # 口吃流畅性与参与连续性
    ├── developmental-language-disorder-child-communication-continuity/ # 发展性语言障碍与儿童沟通连续性
    ├── speech-sound-disorder-articulation-phonology-continuity/ # 语音障碍、构音与音系连续性
    ├── augmentative-alternative-communication-aac-continuity/ # AAC 替代增强沟通连续性
    ├── social-communication-pragmatic-language-continuity/ # 社会沟通与语用语言连续性
    ├── cognitive-communication-disorder-executive-language-continuity/ # 认知沟通与执行语言连续性
    ├── swallowing-dysphagia-aspiration-nutrition/ # 吞咽、误吸与营养连续性
    ├── oropharyngeal-dysphagia-swallow-safety-continuity/ # 口咽吞咽安全连续性
    ├── esophageal-dysphagia-motility-obstruction-continuity/ # 食管吞咽通道连续性
    ├── aspiration-pneumonia-airway-protection-continuity/ # 误吸肺炎与气道保护连续性
    ├── choking-foreign-body-airway-risk-continuity/ # 窒息异物气道风险连续性
    ├── texture-modified-diet-thickened-liquid-continuity/ # 质地调整饮食与稠液连续性
    ├── enteral-feeding-tube-nutrition-continuity/ # 管饲营养通道连续性
    ├── pediatric-feeding-swallowing-development-continuity/ # 儿童摄食吞咽发育连续性
    ├── post-stroke-dysphagia-screening-recovery-continuity/ # 卒中后吞咽筛查恢复连续性
    ├── neurodegenerative-dysphagia-nutrition-continuity/ # 神经退行性吞咽营养连续性
    ├── feeding-assistance-mealtime-dignity-continuity/ # 进食协助与用餐尊严连续性
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
    ├── long-distance-travel-booking-itinerary-continuity/ # 长距离旅行预订与行程连续性
    ├── air-passenger-rights-disruption-refund-continuity/ # 航空旅客权利、中断与退款连续性
    ├── aviation-security-screening-identity-continuity/ # 航空安检、身份核验与筛查连续性
    ├── baggage-personal-property-travel-continuity/ # 行李与旅行个人物品连续性
    ├── lodging-temporary-accommodation-access-continuity/ # 临时住宿与住宿接入连续性
    ├── travel-advisory-consular-assistance-continuity/ # 旅行警示与领事协助连续性
    ├── travel-health-preparedness-continuity/ # 旅行健康准备连续性
    ├── customs-border-entry-declaration-continuity/ # 海关、边境入境与申报连续性
    ├── online-retail-order-shipping-fulfillment-continuity/ # 在线零售订单、发货与履约连续性
    ├── consumer-return-refund-dispute-resolution-continuity/ # 消费者退货、退款与争议解决连续性
    ├── consumer-warranty-service-contract-repair-continuity/ # 消费品保修、服务合同与维修连续性
    ├── right-to-repair-parts-manuals-access-continuity/ # 维修权、零件、手册与诊断接入连续性
    ├── payment-card-dispute-unauthorized-charge-continuity/ # 支付卡争议、错误交易与未授权扣款连续性
    ├── gift-card-prepaid-stored-value-continuity/ # 礼品卡、预付卡与储值余额连续性
    ├── price-fee-disclosure-junk-fee-continuity/ # 价格、费用披露与垃圾费用连续性
    ├── consumer-reviews-endorsements-marketplace-trust-continuity/ # 消费者评价、背书与市场信任连续性
    ├── credit-card-revolving-credit-cost-continuity/ # 信用卡循环信用、成本与还款连续性
    ├── consumer-loan-origination-apr-disclosure-continuity/ # 消费贷款发放、APR 披露与还款义务连续性
    ├── mortgage-origination-servicing-foreclosure-continuity/ # 房贷发放、服务、止赎与住房连续性
    ├── auto-loan-lease-servicing-repossession-continuity/ # 车贷、租赁、服务与收车连续性
    ├── student-loan-servicing-repayment-forgiveness-continuity/ # 学生贷款服务、还款与减免连续性
    ├── payday-small-dollar-title-loan-continuity/ # 发薪日贷款、小额高成本贷款与汽车抵押贷款连续性
    ├── buy-now-pay-later-installment-financing-continuity/ # 先买后付、分期融资与平台授信连续性
    ├── remittance-money-transfer-disclosure-continuity/ # 汇款、跨境转账与费用汇率披露连续性
    ├── auto-insurance-liability-collision-claims-continuity/ # 汽车保险、责任碰撞与事故理赔连续性
    ├── homeowners-renters-property-insurance-claims-continuity/ # 房主租客、个人财产与住所理赔连续性
    ├── flood-insurance-nfip-claims-continuity/ # 洪水保险、NFIP 与灾后理赔连续性
    ├── catastrophe-wind-wildfire-earthquake-insurance-continuity/ # 风暴野火地震巨灾保险连续性
    ├── disability-income-insurance-claim-continuity/ # 残障收入保险与理赔连续性
    ├── long-term-care-insurance-benefit-activation-continuity/ # 长期照护保险与福利启动连续性
    ├── travel-insurance-trip-protection-claims-continuity/ # 旅行保险、行程保护与理赔连续性
    ├── personal-liability-umbrella-insurance-defense-continuity/ # 个人责任、伞形保险与法律防御连续性
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
    ├── personal-vehicle-maintenance-recall-repair-continuity/ # 个人车辆维护、召回与维修连续性
    ├── fuel-ev-charging-refueling-access-continuity/ # 燃料、EV 充电与补能入口连续性
    ├── parking-curb-access-towing-impound-continuity/ # 停车、路缘、拖车与扣押连续性
    ├── walking-bicycling-micromobility-continuity/ # 步行、骑行与微移动连续性
    ├── paratransit-nemt-access-continuity/ # Paratransit 与 NEMT 可达连续性
    ├── taxi-rideshare-demand-response-mobility-continuity/ # 出租车、网约车与需求响应交通连续性
    ├── transit-fare-payment-toll-account-continuity/ # 交通票卡、支付与过路费账户连续性
    ├── multimodal-trip-planning-real-time-wayfinding-continuity/ # 多模式路线规划、实时信息与导向连续性
    ├── public-restroom-sanitation-hygiene-access-continuity/ # 公共厕所、卫生与如厕可达连续性
    ├── public-drinking-water-hydration-access-continuity/ # 公共饮水与补水可达连续性
    ├── public-seating-shade-rest-cooling-access-continuity/ # 公共座椅、遮阴、休息与降温连续性
    ├── community-resilience-hub-shelter-center-continuity/ # 社区韧性中心、避难与灾害服务连续性
    ├── public-library-community-anchor-access-continuity/ # 公共图书馆与社区锚点接入连续性
    ├── parks-recreation-green-space-access-continuity/ # 公园、娱乐与绿地接入连续性
    ├── public-wifi-device-charging-connectivity-continuity/ # 公共 Wi-Fi、设备充电与连接连续性
    ├── public-accommodation-accessibility-service-continuity/ # 公共场所无障碍与服务接入连续性
    ├── grocery-retail-food-store-access-continuity/ # Grocery、食品零售与日常食物采购连续性
    ├── snap-ebt-redemption-retailer-payment-continuity/ # SNAP EBT 兑换、零售商与支付连续性
    ├── wic-benefit-redemption-infant-maternal-nutrition-continuity/ # WIC 兑换、母婴营养与早期食物连续性
    ├── food-bank-pantry-community-food-distribution-continuity/ # 食品银行、pantry 与社区食品发放连续性
    ├── emergency-food-disaster-feeding-continuity/ # 灾害供餐与应急食品发放连续性
    ├── home-delivered-meals-congregate-nutrition-services-continuity/ # 送餐、集体餐与营养服务连续性
    ├── infant-formula-baby-food-supply-safety-continuity/ # 婴儿配方与婴幼儿食品供应安全连续性
    ├── prepared-food-restaurant-cafeteria-safety-access-continuity/ # 熟食、餐馆与 cafeteria 安全可达连续性
    ├── retail-pharmacy-prescription-dispensing-continuity/ # 药房处方配药连续性
    ├── pharmacy-benefit-formulary-prior-authorization-continuity/ # 药品福利、处方集与事前授权连续性
    ├── medication-reconciliation-regimen-adherence-continuity/ # 用药核对与依从执行连续性
    ├── patient-medication-labeling-counseling-continuity/ # 患者药品标签与咨询理解连续性
    ├── unused-medicine-takeback-disposal-continuity/ # 未用药回收处置连续性
    ├── durable-medical-equipment-supplier-repair-continuity/ # DME 供应商与维修连续性
    ├── home-oxygen-respiratory-equipment-supply-continuity/ # 居家氧疗与呼吸设备供应连续性
    ├── diabetes-insulin-glucose-monitoring-supplies-continuity/ # 糖尿病胰岛素与血糖监测耗材连续性
    ├── provider-directory-network-adequacy-continuity/ # Provider 名录与网络充足性连续性
    ├── primary-care-panel-appointment-access-continuity/ # 初级照护 panel 与预约可达连续性
    ├── specialist-referral-authorization-navigation-continuity/ # 专科转诊、授权与导航连续性
    ├── appointment-availability-wait-time-continuity/ # 预约容量与等待时间连续性
    ├── outpatient-laboratory-specimen-result-routing-continuity/ # 门诊检验标本与结果路由连续性
    ├── diagnostic-imaging-order-scheduling-report-continuity/ # 诊断影像医嘱、预约与报告连续性
    ├── ambulatory-procedure-surgery-center-continuity/ # 门诊操作与 ASC 连续性
    ├── after-hours-urgent-care-triage-continuity/ # 非工作时间 urgent care 与分诊连续性
    ├── health-insurance-enrollment-renewal-continuity/ # 健康保险参保续保连续性
    ├── insurance-eligibility-benefits-verification-continuity/ # 保险资格与权益核验连续性
    ├── medical-service-prior-authorization-utilization-management-continuity/ # 医疗服务授权与利用管理连续性
    ├── claims-adjudication-eob-denial-continuity/ # 理赔、EOB 与拒付连续性
    ├── patient-billing-payment-plan-continuity/ # 患者账单与付款计划连续性
    ├── price-transparency-good-faith-estimate-continuity/ # 价格透明与预估费用连续性
    ├── surprise-billing-balance-bill-protection-continuity/ # 意外账单与余额账单保护连续性
    ├── charity-care-financial-assistance-medical-debt-continuity/ # Charity care、经济援助与医疗债务连续性
    ├── patient-portal-account-message-continuity/ # 患者门户、账号与医疗消息连续性
    ├── medical-record-access-amendment-release-continuity/ # 医疗记录访问、修正与释放连续性
    ├── clinical-results-notification-followup-continuity/ # 临床结果通知与随访闭环连续性
    ├── informed-consent-refusal-shared-decision-continuity/ # 知情同意、拒绝与共同决策连续性
    ├── healthcare-language-interpreter-effective-communication-continuity/ # 医疗语言服务与有效沟通连续性
    ├── healthcare-disability-accommodation-accessibility-continuity/ # 医疗残障便利与无障碍连续性
    ├── patient-grievance-complaint-ombuds-continuity/ # 患者投诉、申诉与 Ombuds 连续性
    ├── healthcare-civil-rights-nondiscrimination-continuity/ # 医疗民权与反歧视连续性
    ├── emergency-contact-next-of-kin-notification-continuity/ # 紧急联系人与近亲通知连续性
    ├── personal-health-record-emergency-summary-continuity/ # 个人健康记录与急救摘要连续性
    ├── medical-id-allergy-critical-alert-continuity/ # 医疗 ID、过敏与关键警报连续性
    ├── medication-list-implant-device-emergency-continuity/ # 药物清单与植入设备急救连续性
    ├── chronic-condition-emergency-action-plan-continuity/ # 慢病急救行动计划连续性
    ├── immunization-record-proof-continuity/ # 免疫记录与证明连续性
    ├── organ-donor-registry-anatomical-gift-continuity/ # 器官捐赠登记与遗体捐赠连续性
    ├── access-functional-needs-emergency-registry-continuity/ # 功能需求与急救登记连续性
    ├── death-certificate-registration-cause-of-death-record-continuity/ # 死亡证明、登记与死因记录连续性
    ├── funeral-cremation-burial-disposition-continuity/ # 葬礼、火化、土葬与遗体处置连续性
    ├── cemetery-memorial-remains-location-continuity/ # 墓地、纪念与遗体位置连续性
    ├── bereavement-leave-grief-support-continuity/ # 丧亲假与悲伤支持连续性
    ├── survivor-benefits-death-notification-continuity/ # 遗属福利与死亡通知连续性
    ├── life-insurance-beneficiary-claim-continuity/ # 寿险受益人与理赔连续性
    ├── estate-inventory-asset-liability-handoff-continuity/ # 遗产清单、资产负债与交接连续性
    ├── post-death-account-closure-service-cancellation-continuity/ # 死亡后账户关闭与服务取消连续性
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
    ├── outbreak-case-investigation-contact-tracing-continuity/ # 暴发病例调查与接触追踪
    ├── isolation-quarantine-work-school-continuity/ # 隔离检疫与工作学校连续性
    ├── community-testing-screening-access-continuity/ # 社区检测与筛查可达
    ├── vaccination-campaign-booster-delivery-continuity/ # 疫苗行动与加强针递送
    ├── mask-respirator-source-control-fit-access-continuity/ # 口罩呼吸防护与源头控制
    ├── indoor-ventilation-filtration-outbreak-control-continuity/ # 室内通风过滤与暴发控制
    ├── school-workplace-outbreak-operations-continuity/ # 学校工作场所暴发运营
    ├── healthcare-surge-triage-capacity-continuity/ # 医疗挤兑分诊与容量
    ├── medical-countermeasure-stockpile-distribution-continuity/ # 医疗对策储备与分发
    ├── wastewater-pathogen-surveillance-early-warning-continuity/ # 污水病原体监测与早期预警
    ├── chemical-release-shelter-evacuation-continuity/ # 化学释放避险与撤离
    ├── community-right-to-know-chemical-risk-disclosure-continuity/ # 社区化学风险知情披露
    ├── hazmat-incident-command-emergency-response-continuity/ # HazMat 事故指挥与响应
    ├── industrial-process-safety-management-continuity/ # 工业过程安全管理
    ├── toxic-plume-air-monitoring-risk-communication-continuity/ # 有毒羽流监测与风险沟通
    ├── hazwoper-responder-ppe-safety-continuity/ # HAZWOPER 响应者 PPE 安全
    ├── decontamination-exposure-triage-continuity/ # 去污与暴露分诊
    ├── hazardous-materials-transportation-erg-continuity/ # 危险材料运输与 ERG
    ├── oil-spill-hazardous-release-response-recovery-continuity/ # 油污危险释放响应恢复
    ├── battery-thermal-runaway-fire-hazard-continuity/ # 电池热失控火灾风险
    ├── maternal-newborn-child-development/ # 母婴健康与儿童发展
    ├── patient-safety-organizational-learning/ # 患者安全与组织学习
    ├── caregiving-long-term-care/ # 照护与长期照护
    ├── housing-built-environment-stability/ # 住房与建成环境稳定
    ├── rental-lease-tenancy-rights-continuity/ # 租赁、租约与居住权连续性
    ├── eviction-prevention-court-diversion-continuity/ # 驱逐预防与法院 diversion 连续性
    ├── emergency-rental-assistance-arrears-continuity/ # 应急租金援助与欠租连续性
    ├── housing-choice-voucher-public-housing-continuity/ # 住房选择券与公屋连续性
    ├── fair-housing-discrimination-reasonable-accommodation-continuity/ # 公平住房、歧视与合理便利连续性
    ├── housing-habitability-inspection-code-enforcement-continuity/ # 住房可居住性、检查与 code enforcement 连续性
    ├── hud-approved-housing-counseling-navigation-continuity/ # HUD 批准住房咨询与导航连续性
    ├── manufactured-housing-park-tenure-safety-continuity/ # 制造房屋园区 tenure 安全连续性
    ├── self-represented-litigant-court-self-help-continuity/ # 自行诉讼人与法院自助连续性
    ├── court-efiling-document-submission-continuity/ # 法院电子 filing 与文档提交连续性
    ├── remote-hybrid-court-hearing-access-continuity/ # 远程/混合法院 hearing 可达连续性
    ├── court-language-access-interpreter-continuity/ # 法院语言服务与口译连续性
    ├── court-disability-accommodation-accessibility-continuity/ # 法院残障便利与可达连续性
    ├── court-fees-fines-ability-to-pay-continuity/ # 法院费用罚金与支付能力连续性
    ├── jury-service-summons-hardship-continuity/ # 陪审传票与 hardship 连续性
    ├── small-claims-civil-dispute-resolution-continuity/ # 小额民事纠纷解决连续性
    ├── data-broker-registry-opt-out-deletion-continuity/ # 数据经纪登记、退出与删除连续性
    ├── privacy-rights-access-correction-deletion-continuity/ # 隐私权访问、更正与删除连续性
    ├── opt-out-preference-signal-consent-revocation-continuity/ # 退出偏好信号与同意撤回连续性
    ├── commercial-surveillance-adtech-profile-continuity/ # 商业监控、广告技术与画像连续性
    ├── sensitive-location-data-exposure-continuity/ # 敏感位置数据暴露连续性
    ├── biometric-identifier-template-governance-continuity/ # 生物特征标识与模板治理连续性
    ├── children-teen-data-privacy-consent-continuity/ # 儿童青少年数据隐私与同意连续性
    ├── data-breach-notification-identity-recovery-continuity/ # 数据泄露通知与身份恢复连续性
    ├── content-provenance-authenticity-credential-continuity/ # 内容来源、真实性凭据与验证连续性
    ├── synthetic-media-watermarking-disclosure-continuity/ # 合成媒体水印与披露连续性
    ├── ai-impersonation-deepfake-fraud-continuity/ # AI 冒充、deepfake 与诈骗连续性
    ├── voice-call-caller-id-authentication-continuity/ # 电话 caller ID 认证与号码冒充连续性
    ├── email-domain-authentication-spoofing-continuity/ # 邮件域名认证与 spoofing 连续性
    ├── official-web-domain-brand-impersonation-continuity/ # 官方网站域名与品牌冒充连续性
    ├── digital-evidence-preservation-chain-of-custody-continuity/ # 数字证据保存与链路连续性
    ├── platform-content-moderation-notice-appeal-continuity/ # 平台内容审核通知与申诉连续性
    ├── copyright-authorship-registration-licensing-continuity/ # 版权作者身份、登记与许可连续性
    ├── dmca-notice-counter-notice-platform-removal-continuity/ # DMCA 通知反通知与平台移除连续性
    ├── creative-commons-open-content-license-continuity/ # Creative Commons 开放内容许可连续性
    ├── open-source-software-license-compliance-continuity/ # 开源软件许可证合规连续性
    ├── trademark-brand-identity-rights-continuity/ # 商标品牌身份权利连续性
    ├── patent-invention-disclosure-maintenance-continuity/ # 专利发明披露与维护连续性
    ├── creator-royalty-rights-metadata-continuity/ # 创作者版税权利元数据连续性
    ├── ai-training-data-rights-opt-out-provenance-continuity/ # AI 训练数据权利、退出与 provenance 连续性
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
    ├── scholarly-identity-orcid-affiliation-continuity/ # 科研身份、ORCID 与机构归属连续性
    ├── persistent-identifier-doi-citation-metadata-continuity/ # 持久标识符、DOI 与引用元数据连续性
    ├── research-data-repository-fair-sharing-continuity/ # 研究数据仓库与 FAIR 共享连续性
    ├── research-software-capsule-reproducibility-continuity/ # 研究软件、计算胶囊与可复现性连续性
    ├── preregistration-registered-report-study-plan-continuity/ # 预注册、注册报告与研究计划连续性
    ├── lab-notebook-protocol-versioning-continuity/ # 实验记录、协议与版本连续性
    ├── contributor-role-authorship-attribution-continuity/ # 贡献者角色、作者身份与归因连续性
    ├── conflict-of-interest-funding-disclosure-continuity/ # 利益冲突、资金与披露连续性
    ├── research-artifact-archive-retention-preservation-continuity/ # 研究产物归档、保留与保存连续性
    ├── systematic-review-protocol-search-screening-continuity/ # 系统综述协议、检索与筛选连续性
    ├── risk-of-bias-critical-appraisal-continuity/ # 风险偏倚与批判性评价连续性
    ├── meta-analysis-effect-size-heterogeneity-continuity/ # Meta 分析、效应量与异质性连续性
    ├── publication-reporting-bias-detection-continuity/ # 发表与报告偏倚检测连续性
    ├── evidence-certainty-grade-summary-findings-continuity/ # GRADE 证据确定性与发现摘要连续性
    ├── evidence-to-decision-guideline-panel-continuity/ # 证据到决策与指南小组连续性
    ├── guideline-appraisal-adaptation-localization-continuity/ # 指南评价、适配与本地化连续性
    ├── living-evidence-surveillance-update-continuity/ # 活证据监测与更新连续性
    ├── rapid-review-emergency-evidence-triage-continuity/ # 快速综述与紧急证据分诊连续性
    ├── research-misconduct-investigation-correction-continuity/ # 科研不端调查与纠错连续性
    ├── retraction-expression-concern-correction-continuity/ # 撤稿、表达关注与更正连续性
    ├── preprint-versioning-public-review-continuity/ # 预印本版本与公开评审连续性
    ├── journal-editorial-policy-peer-review-integrity-continuity/ # 期刊编辑政策与同行评审完整性连续性
    ├── predatory-publishing-paper-mill-detection-continuity/ # 掠夺性出版与 paper mill 检测连续性
    ├── citation-network-claim-propagation-continuity/ # 引用网络与主张传播连续性
    ├── research-metrics-incentives-assessment-continuity/ # 科研指标、激励与评价连续性
    ├── replication-reproducibility-many-labs-continuity/ # 复制、复现与多实验室验证连续性
    ├── science-communication-evidence-translation-continuity/ # 科学传播与证据转译连续性
    ├── standards-metrology-quality-infrastructure/ # 标准计量与质量基础设施
    ├── cybersecurity-resilience-critical-services/ # 网络安全韧性与关键服务
    ├── compute-data-center-ai-infrastructure/ # 算力、数据中心与 AI 基础设施
    ├── clinical-trials-regulatory-science-translation/ # 临床试验、监管科学与转化
    ├── geospatial-navigation-location-infrastructure/ # 空间定位、导航与位置基础设施
    ├── weather-climate-observation-forecasting/ # 天气气候观测与预报
    ├── severe-weather-watch-warning-risk-communication-continuity/ # 强天气预警与风险沟通连续性
    ├── river-flash-flood-warning-evacuation-continuity/ # 河流洪水、山洪与撤离连续性
    ├── hurricane-storm-surge-evacuation-shelter-continuity/ # 飓风风暴潮撤离避难连续性
    ├── tornado-warning-safe-room-shelter-continuity/ # 龙卷风预警与安全室避难连续性
    ├── winter-storm-cold-exposure-power-continuity/ # 冬季风暴、寒冷暴露与供能连续性
    ├── drought-water-restriction-household-health-continuity/ # 干旱、水限制与家庭健康连续性
    ├── landslide-mudslide-debris-flow-warning-continuity/ # 滑坡泥石流预警与撤离连续性
    ├── wildfire-smoke-clean-air-respiratory-continuity/ # 野火烟雾、清洁空气与呼吸连续性
    ├── thunderstorm-lightning-outdoor-safety-continuity/ # 雷暴闪电与户外安全连续性
    ├── coastal-flooding-erosion-inundation-continuity/ # 沿海洪水、侵蚀与淹没连续性
    ├── building-fire-life-safety-codes/ # 建筑消防与生命安全规范
    ├── manufacturing-repair-capacity/ # 制造与维修能力
    ├── public-procurement-contracting-capacity/ # 公共采购与合同能力
    ├── animal-health-zoonotic-interface-one-health/ # 动物健康、人兽共患界面与 One Health
    ├── human-animal-bond-companion-care-continuity/ # 人-动物纽带与伴侣照护连续性
    ├── veterinary-care-access-cost-continuity/ # 兽医可及与费用连续性
    ├── service-animal-disability-access-continuity/ # 服务动物与残障可达连续性
    ├── pet-identification-microchip-reunification-continuity/ # 宠物身份、微芯片与重聚连续性
    ├── pet-food-medication-supply-safety-continuity/ # 宠物食品、药品供应与安全连续性
    ├── pet-disaster-evacuation-sheltering-continuity/ # 宠物灾害撤离与避难连续性
    ├── animal-shelter-rescue-rehoming-continuity/ # 动物收容、救助与再安置连续性
    ├── animal-welfare-cruelty-reporting-continuity/ # 动物福利与虐待报告连续性
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
    ├── depression-mood-disorder-functioning-continuity/ # 抑郁心境与功能连续性
    ├── anxiety-stress-threat-regulation-continuity/ # 焦虑压力与威胁调节连续性
    ├── trauma-ptsd-adversity-recovery-continuity/ # 创伤 PTSD 与逆境恢复连续性
    ├── psychosis-reality-testing-community-continuity/ # 精神病性现实检验与社区连续性
    ├── bipolar-mood-episode-stability-continuity/ # 双相情绪周期稳定连续性
    ├── adhd-executive-function-neurodevelopment-continuity/ # ADHD 执行功能与神经发育连续性
    ├── autism-neurodiversity-support-continuity/ # 自闭神经多样性支持连续性
    ├── eating-disorders-nutrition-body-continuity/ # 进食障碍营养与身体连续性
    ├── memory-editing/    # 记忆编辑与人格连续性
    ├── microbiome-ecology/ # 微生物生态
    ├── mitochondrial-bioenergetics/ # 线粒体生物能量学
    ├── musculoskeletal-integrity/ # 肌骨完整性
    ├── neuro-continuity/  # 神经与身份连续性
    ├── nutrition-metabolic-health/ # 营养与代谢健康
    ├── oral-health-continuity/ # 口腔健康连续性
    ├── dental-caries-prevention-restoration-continuity/ # 龋病预防与修复连续性
    ├── periodontal-disease-systemic-inflammation-continuity/ # 牙周病与炎症连续性
    ├── tooth-loss-prosthodontic-chewing-continuity/ # 缺牙修复与咀嚼连续性
    ├── dental-pain-emergency-infection-continuity/ # 牙痛急性感染连续性
    ├── oral-cancer-mucosal-lesion-early-detection-continuity/ # 口腔癌早期识别连续性
    ├── pediatric-oral-health-development-continuity/ # 儿童口腔与发育连续性
    ├── geriatric-long-term-care-oral-health-continuity/ # 老年长期照护口腔连续性
    ├── dental-care-access-insurance-workforce-continuity/ # 牙科可及性与劳动力连续性
    ├── xerostomia-salivary-function-oral-medication-continuity/ # 口干唾液功能连续性
    ├── temporomandibular-orofacial-pain-jaw-function-continuity/ # 颞下颌与口颌面痛连续性
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
    ├── domestic-violence-coercive-control-safety-continuity/ # 家庭暴力、亲密伴侣暴力与胁迫控制安全连续性
    ├── sexual-assault-forensic-exam-advocacy-continuity/ # 性暴力、医疗鉴定与受害者 advocacy 连续性
    ├── stalking-harassment-protection-order-continuity/ # 跟踪骚扰、威胁与保护令连续性
    ├── victim-witness-rights-notification-continuity/ # 受害者/证人权利、通知与法院导航连续性
    ├── crime-victim-compensation-restitution-continuity/ # 犯罪受害者补偿与 restitution 连续性
    ├── survivor-safe-housing-emergency-transfer-continuity/ # 受害者安全住所与 emergency transfer 连续性
    ├── human-trafficking-victim-identification-services-continuity/ # 人口贩运受害者识别与服务连续性
    ├── missing-persons-unidentified-remains-resolution-continuity/ # 失踪人员、无名遗体与身份恢复连续性
    ├── product-safety-recall-systems/ # 产品安全与召回系统
    ├── bathroom-bathing-toileting-transfer-fall-safety-continuity/ # 浴室洗澡、如厕转移与跌倒安全连续性
    ├── stairs-steps-handrail-threshold-fall-safety-continuity/ # 楼梯、台阶、扶手与门槛跌倒安全连续性
    ├── home-lighting-nighttime-pathway-visibility-continuity/ # 居家照明、夜间路径与可见性连续性
    ├── bedroom-bed-transfer-entrapment-safety-continuity/ # 卧室、床转移与夹陷安全连续性
    ├── smoke-alarm-home-fire-escape-readiness-continuity/ # 烟雾报警与家庭火灾逃生准备连续性
    ├── carbon-monoxide-alarm-combustion-appliance-safety-continuity/ # 一氧化碳报警与燃烧设备安全连续性
    ├── furniture-tv-tip-over-anchoring-child-safety-continuity/ # 家具电视倾倒、锚固与儿童安全连续性
    ├── household-poison-storage-child-resistant-packaging-continuity/ # 家庭毒物储存与儿童防护包装连续性
    ├── window-covering-cord-strangulation-child-safety-continuity/ # 窗饰拉绳勒颈与儿童安全连续性
    ├── hot-water-scald-burn-prevention-continuity/ # 热水烫伤与烧伤预防连续性
    ├── drowning-water-safety-supervision-continuity/ # 溺水、水域安全与监督连续性
    ├── pool-spa-barrier-drain-entrapment-safety-continuity/ # 泳池/水疗池屏障与排水夹陷安全连续性
    ├── boating-life-jacket-watercraft-safety-continuity/ # 船艇、救生衣与水上载具安全连续性
    ├── child-passenger-safety-car-seat-restraint-continuity/ # 儿童乘员、安全座椅与约束连续性
    ├── bicycle-helmet-wheeled-sports-head-injury-prevention-continuity/ # 自行车/轮式运动头部伤害预防连续性
    ├── playground-surface-equipment-fall-injury-prevention-continuity/ # 游乐场表面、设备与跌落伤害预防连续性
    ├── sports-concussion-return-to-play-protocol-continuity/ # 运动脑震荡返学返赛协议连续性
    ├── infant-safe-sleep-suid-risk-reduction-continuity/ # 婴儿安全睡眠与 SUID 风险降低连续性
    ├── firearm-safe-storage-injury-prevention-continuity/ # 枪支安全储存与伤害预防连续性
    ├── atv-off-highway-vehicle-injury-prevention-continuity/ # ATV/OHV 越野车辆伤害预防连续性
    ├── emergency-supply-kit-go-bag-rotation-continuity/ # 应急物资包、撤离包与轮换连续性
    ├── family-emergency-communication-reunification-continuity/ # 家庭应急通信与团聚连续性
    ├── evacuation-route-transportation-shelter-plan-continuity/ # 撤离路线、交通与避难计划连续性
    ├── shelter-in-place-clean-air-room-indoor-protection-continuity/ # 就地避险、清洁空气房与室内保护连续性
    ├── backup-power-battery-generator-safety-continuity/ # 备用电、电池与发电机安全连续性
    ├── emergency-food-water-storage-treatment-continuity/ # 应急食物、水储存与处理连续性
    ├── refrigerated-medication-medical-device-power-outage-continuity/ # 温控药品、医疗设备与停电连续性
    ├── emergency-financial-document-cash-readiness-continuity/ # 应急金融文件、现金与恢复资料连续性
    ├── disability-access-functional-needs-personal-preparedness-continuity/ # 残障、无障碍与功能需求个人准备连续性
    ├── older-adult-caregiver-disaster-preparedness-continuity/ # 老年人与照护者灾害准备连续性
    ├── disaster-individual-assistance-benefits-navigation-continuity/ # 灾后个人援助与福利导航连续性
    ├── disaster-temporary-housing-displacement-recovery-continuity/ # 灾后临时住房、流离与恢复连续性
    ├── disaster-recovery-center-service-access-continuity/ # 灾后恢复中心与服务可达连续性
    ├── disaster-case-management-long-term-recovery-continuity/ # 灾后个案管理与长期恢复连续性
    ├── disaster-unemployment-income-disruption-continuity/ # 灾害失业、收入中断与现金流连续性
    ├── disaster-legal-aid-rights-claims-continuity/ # 灾害法律援助、权利与主张连续性
    ├── disaster-debris-waste-sanitation-cleanup-continuity/ # 灾后废弃物、卫生与清理连续性
    ├── post-flood-mold-moisture-indoor-recovery-continuity/ # 洪水后霉菌、湿气与室内恢复连续性
    ├── disaster-behavioral-health-distress-recovery-continuity/ # 灾害行为健康、痛苦与恢复连续性
    ├── disaster-volunteer-donations-management-continuity/ # 灾害志愿、捐赠与协调管理连续性
    ├── sensory-continuity/ # 感官连续性
    ├── sleep-circadian-recovery/ # 睡眠、节律与恢复
    ├── skin-barrier-wound-healing/ # 皮肤屏障与伤口愈合
    ├── pressure-injury-prevention-repositioning-support-surface-continuity/ # 压力损伤、减压与支撑面连续性
    ├── chronic-wound-venous-diabetic-pressure-ulcer-continuity/ # 慢性伤口、静脉/糖尿病/压力性溃疡连续性
    ├── wound-infection-cellulitis-sepsis-continuity/ # 伤口感染、蜂窝织炎与脓毒症风险连续性
    ├── diabetic-foot-ulcer-amputation-prevention-continuity/ # 糖尿病足溃疡与截肢预防连续性
    ├── burn-wound-aftercare-scar-function-continuity/ # 烧伤创面后续照护、瘢痕与功能连续性
    ├── surgical-wound-dehiscence-ssi-continuity/ # 手术切口、裂开与 SSI 连续性
    ├── incontinence-associated-dermatitis-moisture-skin-continuity/ # 失禁相关皮炎、潮湿与皮肤保护连续性
    ├── eczema-atopic-dermatitis-itch-sleep-continuity/ # 湿疹/特应性皮炎、瘙痒与睡眠连续性
    ├── psoriasis-inflammatory-skin-systemic-burden-continuity/ # 银屑病、炎症皮肤与系统负担连续性
    ├── skin-care-supplies-dressings-barrier-products-continuity/ # 皮肤护理用品、敷料与屏障产品连续性
    ├── social-connection-relational-infra/ # 社会连接与关系基础设施
    ├── loneliness-social-isolation-risk-continuity/ # 孤独与社会隔离风险连续性
    ├── social-prescribing-community-referral-continuity/ # 社会处方与社区转介连续性
    ├── mutual-aid-neighbor-support-network-continuity/ # 互助与邻里支持网络连续性
    ├── volunteering-civic-service-participation-continuity/ # 志愿服务与公民参与连续性
    ├── community-mediation-neighbor-conflict-resolution-continuity/ # 社区调解与邻里冲突解决连续性
    ├── restorative-justice-repair-accountability-continuity/ # 修复性司法与责任修复连续性
    ├── reputation-defamation-public-trust-repair-continuity/ # 声誉诽谤与公共信任修复连续性
    ├── references-vouching-recommendation-social-capital-continuity/ # 推荐背书与社会资本连续性
    ├── third-place-belonging-social-participation-continuity/ # 第三空间、归属与社会参与连续性
    ├── purpose-meaning-existential-continuity/ # 目的意义与存在连续性
    ├── spiritual-care-religious-practice-continuity/ # 精神照护与宗教实践连续性
    ├── cultural-heritage-identity-continuity/ # 文化遗产与身份连续性
    ├── arts-creative-expression-participation-continuity/ # 艺术创造表达与参与连续性
    ├── leisure-recreation-restorative-activity-continuity/ # 休闲娱乐与恢复性活动连续性
    ├── narrative-identity-life-review-continuity/ # 叙事身份与生命回顾连续性
    ├── ritual-ceremony-life-transition-continuity/ # 仪式典礼与生命过渡连续性
    ├── dignity-personhood-respect-continuity/ # 尊严人格与尊重连续性
    ├── human-factors-ergonomics-task-system-continuity/ # 人因工效与任务系统连续性
    ├── cognitive-load-workload-measurement-continuity/ # 认知负荷与工作负荷测量连续性
    ├── fatigue-risk-alertness-continuity/ # 疲劳风险与警觉性连续性
    ├── situational-awareness-decision-environment-continuity/ # 情境感知与决策环境连续性
    ├── handoff-checklist-procedure-reliability-continuity/ # 交接清单与过程可靠性连续性
    ├── incident-reporting-just-culture-learning-continuity/ # 事件报告与公正文化学习连续性
    ├── automation-bias-mode-confusion-oversight-continuity/ # 自动化偏误、模式混淆与监督连续性
    ├── alert-fatigue-interruption-signal-management-continuity/ # 告警疲劳、中断与信号管理连续性
    ├── space-extreme-habitation/ # 空间与极端栖居
    ├── stem-cell-reserve-renewal/ # 干细胞储备与组织更新
    ├── substance-exposure-control/ # 物质暴露控制
    ├── supply-chain-continuity/ # 供应链连续性
    ├── synthetic-biology-biosecurity/ # 合成生物学与生物安全
    ├── thermal-homeostasis-resilience/ # 热稳态与温度韧性
    ├── time-allocation-effective-time/ # 时间分配与有效时间
    ├── transportation-access-mobility/ # 交通接入与日常移动
    ├── urogenital-continuity/ # 泌尿生殖连续性
    ├── urinary-tract-infection-pyelonephritis-urosepsis-continuity/ # 尿路感染、肾盂肾炎与尿源性脓毒症连续性
    ├── catheter-associated-uti-device-infection-continuity/ # 导尿相关 UTI 与设备感染连续性
    ├── urinary-retention-bladder-emptying-continuity/ # 尿潴留与膀胱排空连续性
    ├── overactive-bladder-nocturia-sleep-continuity/ # 膀胱过度活动、夜尿与睡眠连续性
    ├── kidney-stone-obstruction-renal-colic-continuity/ # 肾结石、尿路梗阻与肾绞痛连续性
    ├── benign-prostatic-hyperplasia-luts-continuity/ # BPH 与下尿路症状连续性
    ├── urinary-diversion-urostomy-supplies-continuity/ # 尿流改道、尿路造口与耗材连续性
    ├── dialysis-access-vascular-peritoneal-continuity/ # 透析血管/腹膜通路连续性
    ├── home-dialysis-supply-self-management-continuity/ # 家庭透析供应与自我管理连续性
    ├── kidney-transplant-immunosuppression-graft-continuity/ # 肾移植、免疫抑制与移植物连续性
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
- `domains/skin-barrier-wound-healing/` 负责皮肤屏障、伤口愈合、压力损伤、感染入口、热调节和感觉边界；`domains/pressure-injury-prevention-repositioning-support-surface-continuity/`、`domains/chronic-wound-venous-diabetic-pressure-ulcer-continuity/`、`domains/wound-infection-cellulitis-sepsis-continuity/`、`domains/diabetic-foot-ulcer-amputation-prevention-continuity/`、`domains/burn-wound-aftercare-scar-function-continuity/`、`domains/surgical-wound-dehiscence-ssi-continuity/`、`domains/incontinence-associated-dermatitis-moisture-skin-continuity/`、`domains/eczema-atopic-dermatitis-itch-sleep-continuity/`、`domains/psoriasis-inflammatory-skin-systemic-burden-continuity/` 和 `domains/skin-care-supplies-dressings-barrier-products-continuity/` 负责压力损伤预防、慢性伤口、伤口感染/蜂窝织炎、糖尿病足、烧伤后创面、手术切口/SSI、潮湿相关皮炎、湿疹、银屑病和皮肤护理用品这些皮肤边界执行层失效模式。
- `domains/urogenital-continuity/` 负责膀胱、尿路、尿控、盆底、泌尿感染、性功能和日常尊严；`domains/urinary-tract-infection-pyelonephritis-urosepsis-continuity/`、`domains/catheter-associated-uti-device-infection-continuity/`、`domains/urinary-retention-bladder-emptying-continuity/`、`domains/overactive-bladder-nocturia-sleep-continuity/`、`domains/kidney-stone-obstruction-renal-colic-continuity/`、`domains/benign-prostatic-hyperplasia-luts-continuity/`、`domains/urinary-diversion-urostomy-supplies-continuity/`、`domains/dialysis-access-vascular-peritoneal-continuity/`、`domains/home-dialysis-supply-self-management-continuity/` 和 `domains/kidney-transplant-immunosuppression-graft-continuity/` 负责尿路感染、导尿设备、尿潴留、夜尿、结石梗阻、BPH/LUTS、尿流改道、透析通路、家庭透析和肾移植这些排泄出口与肾脏替代执行层失效模式。
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
- `domains/outbreak-case-investigation-contact-tracing-continuity/`、`domains/isolation-quarantine-work-school-continuity/`、`domains/community-testing-screening-access-continuity/`、`domains/vaccination-campaign-booster-delivery-continuity/`、`domains/mask-respirator-source-control-fit-access-continuity/`、`domains/indoor-ventilation-filtration-outbreak-control-continuity/`、`domains/school-workplace-outbreak-operations-continuity/`、`domains/healthcare-surge-triage-capacity-continuity/`、`domains/medical-countermeasure-stockpile-distribution-continuity/` 和 `domains/wastewater-pathogen-surveillance-early-warning-continuity/` 负责传染病暴发响应执行连续性，覆盖病例调查、接触追踪、隔离检疫、社区检测、疫苗行动、呼吸防护、室内空气控制、学校工作场所运营、医疗挤兑、医疗对策和污水早期预警。
- `domains/chemical-release-shelter-evacuation-continuity/`、`domains/community-right-to-know-chemical-risk-disclosure-continuity/`、`domains/hazmat-incident-command-emergency-response-continuity/`、`domains/industrial-process-safety-management-continuity/`、`domains/toxic-plume-air-monitoring-risk-communication-continuity/`、`domains/hazwoper-responder-ppe-safety-continuity/`、`domains/decontamination-exposure-triage-continuity/`、`domains/hazardous-materials-transportation-erg-continuity/`、`domains/oil-spill-hazardous-release-response-recovery-continuity/` 和 `domains/battery-thermal-runaway-fire-hazard-continuity/` 负责危险材料与工业事故执行连续性，覆盖化学释放避险撤离、社区知情披露、HazMat 指挥、过程安全、有毒羽流沟通、响应者 PPE、暴露后分诊、危险品运输、油污恢复和电池热失控。
- `domains/maternal-newborn-child-development/` 负责孕产健康、新生儿健康、儿童健康、生长标准、早期发展和养育照护。
- `domains/patient-safety-organizational-learning/` 负责患者安全、事件报告、团队沟通、根因分析、CUSP、TeamSTEPPS 和安全文化。
- `domains/caregiving-long-term-care/` 负责家庭照护、长期照护、居家社区支持、照护协调、照护者负担和尊严边界。
- `domains/housing-built-environment-stability/` 负责住房稳定、住房质量、室内环境、无障碍、社区资源和建成环境健康。
- `domains/rental-lease-tenancy-rights-continuity/`、`domains/eviction-prevention-court-diversion-continuity/`、`domains/emergency-rental-assistance-arrears-continuity/`、`domains/housing-choice-voucher-public-housing-continuity/`、`domains/fair-housing-discrimination-reasonable-accommodation-continuity/`、`domains/housing-habitability-inspection-code-enforcement-continuity/`、`domains/hud-approved-housing-counseling-navigation-continuity/` 和 `domains/manufactured-housing-park-tenure-safety-continuity/` 负责住房 tenure 稳定与可居住性执行连续性，覆盖租赁居住权、驱逐预防、欠租援助、住房补贴、公平住房、可居住性检查、住房咨询和制造房屋园区稳定。
- `domains/self-represented-litigant-court-self-help-continuity/`、`domains/court-efiling-document-submission-continuity/`、`domains/remote-hybrid-court-hearing-access-continuity/`、`domains/court-language-access-interpreter-continuity/`、`domains/court-disability-accommodation-accessibility-continuity/`、`domains/court-fees-fines-ability-to-pay-continuity/`、`domains/jury-service-summons-hardship-continuity/` 和 `domains/small-claims-civil-dispute-resolution-continuity/` 负责法院接入与民事程序执行连续性，覆盖自助中心、电子提交、远程听证、语言口译、残障便利、费用罚金、陪审义务和小额纠纷恢复。
- `domains/data-broker-registry-opt-out-deletion-continuity/`、`domains/privacy-rights-access-correction-deletion-continuity/`、`domains/opt-out-preference-signal-consent-revocation-continuity/`、`domains/commercial-surveillance-adtech-profile-continuity/`、`domains/sensitive-location-data-exposure-continuity/`、`domains/biometric-identifier-template-governance-continuity/`、`domains/children-teen-data-privacy-consent-continuity/` 和 `domains/data-breach-notification-identity-recovery-continuity/` 负责个人数据权利、隐私暴露与数据经纪连续性，覆盖数据经纪、访问更正删除、同意撤回、商业监控、位置数据、生物特征、未成年数据和泄露恢复。
- `domains/content-provenance-authenticity-credential-continuity/`、`domains/synthetic-media-watermarking-disclosure-continuity/`、`domains/ai-impersonation-deepfake-fraud-continuity/`、`domains/voice-call-caller-id-authentication-continuity/`、`domains/email-domain-authentication-spoofing-continuity/`、`domains/official-web-domain-brand-impersonation-continuity/`、`domains/digital-evidence-preservation-chain-of-custody-continuity/` 和 `domains/platform-content-moderation-notice-appeal-continuity/` 负责数字内容可信、合成媒体与冒充风险连续性，覆盖内容来源凭据、合成媒体披露、AI 冒充、电话认证、邮件认证、官网品牌冒充、数字证据保存和平台审核通知申诉。
- `domains/copyright-authorship-registration-licensing-continuity/`、`domains/dmca-notice-counter-notice-platform-removal-continuity/`、`domains/creative-commons-open-content-license-continuity/`、`domains/open-source-software-license-compliance-continuity/`、`domains/trademark-brand-identity-rights-continuity/`、`domains/patent-invention-disclosure-maintenance-continuity/`、`domains/creator-royalty-rights-metadata-continuity/` 和 `domains/ai-training-data-rights-opt-out-provenance-continuity/` 负责知识产权、数字作品与 AI 训练数据权利连续性，覆盖版权作者身份登记许可、DMCA 通知反通知、开放内容许可、开源软件许可证、商标品牌身份、专利披露维护、创作者版税元数据和 AI 训练数据权利/provenance。
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
- `domains/scholarly-identity-orcid-affiliation-continuity/`、`domains/persistent-identifier-doi-citation-metadata-continuity/`、`domains/research-data-repository-fair-sharing-continuity/`、`domains/research-software-capsule-reproducibility-continuity/`、`domains/preregistration-registered-report-study-plan-continuity/`、`domains/lab-notebook-protocol-versioning-continuity/`、`domains/contributor-role-authorship-attribution-continuity/`、`domains/conflict-of-interest-funding-disclosure-continuity/` 和 `domains/research-artifact-archive-retention-preservation-continuity/` 负责科研身份、持久标识与可复现研究基础设施，覆盖 ORCID/ROR、DOI 元数据、FAIR 数据仓库、研究软件胶囊、预注册、实验协议版本、贡献者角色、利益冲突披露和研究产物保存。
- `domains/systematic-review-protocol-search-screening-continuity/`、`domains/risk-of-bias-critical-appraisal-continuity/`、`domains/meta-analysis-effect-size-heterogeneity-continuity/`、`domains/publication-reporting-bias-detection-continuity/`、`domains/evidence-certainty-grade-summary-findings-continuity/`、`domains/evidence-to-decision-guideline-panel-continuity/`、`domains/guideline-appraisal-adaptation-localization-continuity/`、`domains/living-evidence-surveillance-update-continuity/` 和 `domains/rapid-review-emergency-evidence-triage-continuity/` 负责证据综合与指南转化连续性，覆盖系统综述协议、检索筛选、风险偏倚、Meta 分析、报告偏倚、GRADE、证据到决策、指南适配、活证据更新和快速综述边界。
- `domains/research-misconduct-investigation-correction-continuity/`、`domains/retraction-expression-concern-correction-continuity/`、`domains/preprint-versioning-public-review-continuity/`、`domains/journal-editorial-policy-peer-review-integrity-continuity/`、`domains/predatory-publishing-paper-mill-detection-continuity/`、`domains/citation-network-claim-propagation-continuity/`、`domains/research-metrics-incentives-assessment-continuity/`、`domains/replication-reproducibility-many-labs-continuity/` 和 `domains/science-communication-evidence-translation-continuity/` 负责科研纠错、出版完整性与科学传播连续性，覆盖科研不端调查纠错、撤稿/关注/更正、预印本版本与公开评审、期刊编辑与同行评审、paper mill 检测、引用网络主张传播、科研指标激励、复制复现和证据传播边界。
- `domains/standards-metrology-quality-infrastructure/` 负责标准、计量、校准、认证、合格评定、质量管理和互操作规范。
- `domains/cybersecurity-resilience-critical-services/` 负责网络安全、关键服务韧性、事件响应、备份恢复和数字风险治理。
- `domains/compute-data-center-ai-infrastructure/` 负责算力、数据中心、AI 基础设施、芯片、能源、水、网络、成本和接入治理。
- `domains/clinical-trials-regulatory-science-translation/` 负责临床试验、监管科学、真实世界证据、安全监测和医学转化证据路径。
- `domains/geospatial-navigation-location-infrastructure/` 负责地理空间数据、地址、地图、GNSS/GPS、地理编码、应急位置和位置互操作。
- `domains/weather-climate-observation-forecasting/` 负责天气气候观测、预报模型、气候服务、极端天气和早期预警风险输入。
- `domains/severe-weather-watch-warning-risk-communication-continuity/`、`domains/river-flash-flood-warning-evacuation-continuity/`、`domains/hurricane-storm-surge-evacuation-shelter-continuity/`、`domains/tornado-warning-safe-room-shelter-continuity/`、`domains/winter-storm-cold-exposure-power-continuity/`、`domains/drought-water-restriction-household-health-continuity/`、`domains/landslide-mudslide-debris-flow-warning-continuity/`、`domains/wildfire-smoke-clean-air-respiratory-continuity/`、`domains/thunderstorm-lightning-outdoor-safety-continuity/` 和 `domains/coastal-flooding-erosion-inundation-continuity/` 负责强天气和自然 hazard 执行连续性，覆盖预警理解、撤离避难、就地保护、空气暴露控制、寒冷/水限制和沿海淹没，不提供实时预警、路线、现场操作、工程、医疗、保险或法律建议。
- `domains/building-fire-life-safety-codes/` 负责建筑规范、消防规范、生命安全、疏散、烟雾报警、无障碍和韧性改造。
- `domains/manufacturing-repair-capacity/` 负责制造、维修、维护、备件、质量、本地生产和关键设备恢复能力。
- `domains/public-procurement-contracting-capacity/` 负责公共采购、合同、供应商管理、应急采购、透明度和交付验收。
- `domains/animal-health-zoonotic-interface-one-health/` 负责动物健康、兽医公共卫生、人兽共患病、食品动物、野生动物和 One Health 界面。
- `domains/human-animal-bond-companion-care-continuity/`、`domains/veterinary-care-access-cost-continuity/`、`domains/service-animal-disability-access-continuity/`、`domains/pet-identification-microchip-reunification-continuity/`、`domains/pet-food-medication-supply-safety-continuity/`、`domains/pet-disaster-evacuation-sheltering-continuity/`、`domains/animal-shelter-rescue-rehoming-continuity/` 和 `domains/animal-welfare-cruelty-reporting-continuity/` 负责伴侣动物、服务动物与宠物照护连续性，覆盖人-动物纽带、兽医可及费用、服务动物残障可达、宠物身份重聚、宠物食药供应安全、灾害撤离避难、收容救助再安置和动物福利虐待报告。
- 伴侣动物和服务动物相关域必须与 One Health 区分：前者关注家庭、关系、残障辅助和照护连续性，后者关注动物-人类-环境公共卫生界面。
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
- `domains/domestic-violence-coercive-control-safety-continuity/`、`domains/sexual-assault-forensic-exam-advocacy-continuity/`、`domains/stalking-harassment-protection-order-continuity/`、`domains/victim-witness-rights-notification-continuity/`、`domains/crime-victim-compensation-restitution-continuity/`、`domains/survivor-safe-housing-emergency-transfer-continuity/`、`domains/human-trafficking-victim-identification-services-continuity/` 和 `domains/missing-persons-unidentified-remains-resolution-continuity/` 负责家庭暴力/胁迫控制、性暴力 forensic exam 与 advocacy、跟踪骚扰保护令、受害者/证人权利通知、犯罪受害者补偿、受害者安全住所、人口贩运受害者服务和失踪/无名身份恢复这些受害者安全、服务与恢复执行连续性条件。
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
- `domains/vision-eye-health-continuity/` 负责视觉输入总框架；`domains/cataract-vision-restoration-continuity/`、`domains/glaucoma-visual-field-protection-continuity/`、`domains/diabetic-retinopathy-screening-treatment-continuity/`、`domains/age-related-macular-degeneration-central-vision-continuity/`、`domains/refractive-error-glasses-contact-lens-continuity/`、`domains/low-vision-rehabilitation-assistive-technology-continuity/`、`domains/dry-eye-ocular-surface-comfort-continuity/`、`domains/eye-injury-urgent-vision-protection-continuity/`、`domains/pediatric-vision-screening-amblyopia-continuity/` 和 `domains/retinal-detachment-urgent-referral-continuity/` 负责白内障、青光眼、糖尿病视网膜病变、AMD、屈光矫正、低视力康复、干眼、眼外伤、儿童视筛弱视和视网膜脱离这些视觉下层失效模式。
- `domains/hearing-auditory-communication-continuity/` 负责听觉沟通总框架；`domains/age-related-hearing-loss-hearing-aid-continuity/`、`domains/noise-induced-hearing-loss-prevention-continuity/`、`domains/tinnitus-sound-tolerance-sleep-continuity/`、`domains/otitis-media-child-hearing-development-continuity/`、`domains/sudden-hearing-loss-urgent-referral-continuity/`、`domains/cochlear-implant-communication-continuity/`、`domains/newborn-hearing-screening-language-development-continuity/`、`domains/auditory-processing-listening-effort-continuity/`、`domains/hearing-assistive-devices-alerting-access-continuity/` 和 `domains/captions-relay-service-communication-access-continuity/` 负责老年听损、噪声听损、耳鸣、儿童中耳炎、突发听损、人工耳蜗、新生儿听筛、听觉处理、听觉辅助设备和字幕中继服务这些听觉沟通下层失效模式。
- `domains/vestibular-balance-spatial-orientation/` 负责前庭平衡总框架；`domains/bppv-positional-vertigo-continuity/`、`domains/menieres-disease-episodic-vertigo-continuity/`、`domains/vestibular-neuritis-labyrinthitis-acute-vertigo-continuity/`、`domains/persistent-postural-perceptual-dizziness-continuity/`、`domains/vestibular-migraine-dizziness-sensory-load-continuity/`、`domains/bilateral-vestibular-hypofunction-gaze-gait-stability-continuity/`、`domains/vestibular-rehabilitation-balance-compensation-continuity/`、`domains/gait-balance-assessment-fall-screening-continuity/`、`domains/motion-sickness-transport-virtual-environment-tolerance-continuity/` 和 `domains/vestibular-ototoxicity-medication-chemical-risk-continuity/` 负责 BPPV、梅尼埃病、前庭神经炎/迷路炎、PPPD、前庭性偏头痛、双侧前庭低下、前庭康复、步态平衡筛查、运动病/虚拟环境耐受和耳毒性前庭风险这些空间行动下层失效模式。
- `domains/speech-language-communication-continuity/` 负责言语语言沟通总框架；`domains/aphasia-language-access-recovery-continuity/`、`domains/dysarthria-speech-intelligibility-continuity/`、`domains/apraxia-of-speech-motor-planning-continuity/`、`domains/voice-disorders-phonation-communication-continuity/`、`domains/stuttering-fluency-participation-continuity/`、`domains/developmental-language-disorder-child-communication-continuity/`、`domains/speech-sound-disorder-articulation-phonology-continuity/`、`domains/augmentative-alternative-communication-aac-continuity/`、`domains/social-communication-pragmatic-language-continuity/` 和 `domains/cognitive-communication-disorder-executive-language-continuity/` 负责失语、构音障碍、言语失用、嗓音障碍、口吃、发展性语言障碍、语音障碍、AAC、社会语用沟通和认知沟通这些表达理解执行层失效模式。
- `domains/swallowing-dysphagia-aspiration-nutrition/` 负责吞咽、误吸与营养总框架；`domains/oropharyngeal-dysphagia-swallow-safety-continuity/`、`domains/esophageal-dysphagia-motility-obstruction-continuity/`、`domains/aspiration-pneumonia-airway-protection-continuity/`、`domains/choking-foreign-body-airway-risk-continuity/`、`domains/texture-modified-diet-thickened-liquid-continuity/`、`domains/enteral-feeding-tube-nutrition-continuity/`、`domains/pediatric-feeding-swallowing-development-continuity/`、`domains/post-stroke-dysphagia-screening-recovery-continuity/`、`domains/neurodegenerative-dysphagia-nutrition-continuity/` 和 `domains/feeding-assistance-mealtime-dignity-continuity/` 负责口咽吞咽、食管吞咽、误吸肺炎、窒息、质地饮食、管饲、儿童摄食、卒中吞咽、神经退行性吞咽和进食协助这些吞咽摄食执行层失效模式。
- `domains/smell-taste-chemosensory-continuity/` 和 `domains/peripheral-neuropathy-somatosensory-continuity/` 负责化学感知和身体边界反馈的机制、证据、变量和禁止用途。
- `domains/space-weather-geomagnetic-storm-resilience/`、`domains/planetary-defense-near-earth-object-risk/`、`domains/volcanic-ashfall-geohazard-continuity/`、`domains/earthquake-seismic-risk-built-environment-continuity/`、`domains/tsunami-warning-coastal-evacuation-continuity/` 和 `domains/extreme-heat-cooling-public-health-continuity/` 负责空间天气、行星防御、火山灰、地震、海啸和极端高温这些行星、地球物理与极端热风险的机制、预警、基础设施失效和禁止用途。
- `domains/noise-exposure-acoustic-environment-continuity/`、`domains/light-exposure-circadian-environment-continuity/`、`domains/lead-heavy-metal-exposure-control/`、`domains/radon-asbestos-indoor-hazard-continuity/`、`domains/mold-dampness-indoor-biological-exposure/` 和 `domains/vector-borne-disease-environmental-control/` 负责噪声、光照节律、铅与重金属、氡与石棉、霉菌潮湿和病媒传播这些慢性环境暴露与日常损耗条件的机制、证据、变量和禁止用途。
- `domains/advance-care-planning-medical-decision-continuity/`、`domains/supported-decision-making-guardianship-rights/`、`domains/healthcare-personal-representative-hipaa-access-continuity/`、`domains/financial-fiduciary-power-of-attorney-continuity/`、`domains/representative-payee-benefits-management-continuity/` 和 `domains/trust-estate-affairs-succession-continuity/` 负责预先医疗照护计划、支持性决策、医疗个人代表、财务受托、代表收款人和事务继承这些决策权、代理权与受托连续性条件。
- `domains/credit-consumer-reporting-access-continuity/`、`domains/tenant-screening-rental-access-continuity/`、`domains/background-check-record-screening-continuity/`、`domains/employment-algorithmic-hiring-screening-continuity/`、`domains/insurance-underwriting-algorithmic-risk-scoring-continuity/` 和 `domains/public-benefits-eligibility-automated-decision-continuity/` 负责信用/消费者报告、租房筛查、背景记录筛查、算法招聘、保险算法评分和公共福利自动资格系统这些算法化准入、筛查与资格连续性条件。
- `domains/education-record-transcript-verification-continuity/`、`domains/professional-licensure-certification-continuity/`、`domains/skills-competency-credentialing-continuity/`、`domains/continuing-education-recertification-continuity/`、`domains/apprenticeship-work-based-learning-continuity/` 和 `domains/verifiable-credential-wallet-interoperability/` 负责教育记录核验、职业证照认证、技能胜任力凭证、继续教育再认证、学徒制工作中学习和可验证凭证钱包互操作这些资格证明、授权与能力可携带连续性条件。
- `domains/income-payroll-employment-record-continuity/`、`domains/tax-administration-filing-record-continuity/`、`domains/social-security-earnings-benefit-record-continuity/`、`domains/retirement-pension-savings-plan-continuity/`、`domains/unemployment-insurance-wage-record-continuity/` 和 `domains/workers-compensation-occupational-injury-benefit-continuity/` 负责工资雇佣记录、税务申报记录、社会保险收入与福利记录、退休养老金计划、失业保险工资记录和工伤职业伤害权益这些劳动成果到未来保障的记录连续性条件。
- `domains/family-medical-leave-job-protection-continuity/`、`domains/paid-sick-family-leave-wage-replacement-continuity/`、`domains/pregnancy-parental-work-continuity/`、`domains/workplace-accommodation-return-to-work-continuity/`、`domains/disability-income-work-capacity-benefit-continuity/` 和 `domains/family-caregiver-respite-work-continuity/` 负责家庭医疗假岗位保护、带薪病假/家庭假工资替代、孕产育儿工作连续性、合理便利复工、残障收入与工作能力福利、家庭照护者喘息与工作连续性这些工作中断与照护事件连续性条件。
- `domains/vital-records-life-event-continuity/`、`domains/name-change-identity-record-synchronization-continuity/`、`domains/address-residency-mail-service-continuity/`、`domains/household-composition-dependent-eligibility-continuity/`、`domains/family-law-custody-child-support-continuity/` 和 `domains/kinship-foster-adoption-care-continuity/` 负责生命事件记录、姓名变更同步、地址居住地邮件路由、家庭组成资格关系、家庭法监护抚养、亲属照护寄养收养这些家庭事实与制度记录连续性条件。
- `domains/banking-deposit-account-access-continuity/`、`domains/debt-obligation-collection-relief-continuity/`、`domains/real-property-title-deed-record-continuity/`、`domains/driver-license-vehicle-registration-continuity/`、`domains/passport-travel-document-mobility-continuity/`、`domains/contract-subscription-billing-consent-continuity/` 和 `domains/notary-document-authentication-signature-continuity/` 负责银行账户存款访问、债务义务催收救济、不动产权属地契、驾照车辆登记、护照旅行证件、合同订阅账单、公证文件认证签名这些资源控制、移动资格与交易执行连续性条件。
- `domains/long-distance-travel-booking-itinerary-continuity/`、`domains/air-passenger-rights-disruption-refund-continuity/`、`domains/aviation-security-screening-identity-continuity/`、`domains/baggage-personal-property-travel-continuity/`、`domains/lodging-temporary-accommodation-access-continuity/`、`domains/travel-advisory-consular-assistance-continuity/`、`domains/travel-health-preparedness-continuity/` 和 `domains/customs-border-entry-declaration-continuity/` 负责长距离旅行预订行程、航空中断退款、安检身份核验、行李个人物品、临时住宿、旅行警示领事协助、旅行健康准备和海关边境申报这些旅行、临时住宿与跨境移动执行连续性条件。
- `domains/online-retail-order-shipping-fulfillment-continuity/`、`domains/consumer-return-refund-dispute-resolution-continuity/`、`domains/consumer-warranty-service-contract-repair-continuity/`、`domains/right-to-repair-parts-manuals-access-continuity/`、`domains/payment-card-dispute-unauthorized-charge-continuity/`、`domains/gift-card-prepaid-stored-value-continuity/`、`domains/price-fee-disclosure-junk-fee-continuity/` 和 `domains/consumer-reviews-endorsements-marketplace-trust-continuity/` 负责在线零售订单履约、退货退款争议、消费品保修维修、维修权零件手册、支付卡争议未授权扣款、礼品卡预付储值、价格费用披露和消费者评价背书市场信任这些消费者交易、履约与市场信任连续性条件。
- `domains/credit-card-revolving-credit-cost-continuity/`、`domains/consumer-loan-origination-apr-disclosure-continuity/`、`domains/mortgage-origination-servicing-foreclosure-continuity/`、`domains/auto-loan-lease-servicing-repossession-continuity/`、`domains/student-loan-servicing-repayment-forgiveness-continuity/`、`domains/payday-small-dollar-title-loan-continuity/`、`domains/buy-now-pay-later-installment-financing-continuity/` 和 `domains/remittance-money-transfer-disclosure-continuity/` 负责信用卡循环信用成本、消费贷款 APR 披露、房贷服务止赎、车贷租赁收车、学生贷款还款减免、发薪日/小额/汽车抵押贷款、BNPL 分期融资和汇款转账费用汇率这些消费者信贷、贷款服务与跨期资源连续性条件。
- `domains/auto-insurance-liability-collision-claims-continuity/`、`domains/homeowners-renters-property-insurance-claims-continuity/`、`domains/flood-insurance-nfip-claims-continuity/`、`domains/catastrophe-wind-wildfire-earthquake-insurance-continuity/`、`domains/disability-income-insurance-claim-continuity/`、`domains/long-term-care-insurance-benefit-activation-continuity/`、`domains/travel-insurance-trip-protection-claims-continuity/` 和 `domains/personal-liability-umbrella-insurance-defense-continuity/` 负责汽车保险理赔、房主租客财产理赔、洪水/NFIP 理赔、风暴野火地震巨灾保险、残障收入保险理赔、长期照护福利启动、旅行保险理赔和个人责任伞形保险防御这些个人保险、财产责任、灾害与理赔执行连续性条件。
- `domains/citizenship-nationality-statelessness-continuity/`、`domains/immigration-status-residency-work-authorization-continuity/`、`domains/asylum-refugee-protection-status-continuity/`、`domains/detention-custody-confinement-status-continuity/`、`domains/civil-commitment-involuntary-treatment-rights-continuity/`、`domains/court-notice-service-process-default-judgment-continuity/` 和 `domains/criminal-record-relief-collateral-consequences-continuity/` 负责公民国籍无国籍、移民居留工作授权、庇护难民保护、拘押羁押监管状态、非自愿治疗权利、法院通知缺席判决和犯罪记录附带后果这些法律状态与强制程序连续性条件。
- `domains/school-enrollment-attendance-continuity/`、`domains/special-education-iep-504-accommodation-continuity/`、`domains/school-meals-nutrition-access-continuity/`、`domains/school-health-services-chronic-condition-continuity/`、`domains/school-transportation-safe-routes-continuity/`、`domains/school-discipline-exclusion-restraint-continuity/`、`domains/school-mental-health-counseling-support-continuity/` 和 `domains/school-climate-bullying-violence-prevention-continuity/` 负责入学出勤、特殊教育 IEP/504、校餐营养、学校健康服务、通学安全、纪律排除约束、学校心理健康、学校气候欺凌暴力预防这些学校服务连续性条件。
- `domains/postsecondary-admissions-transfer-articulation-continuity/`、`domains/student-financial-aid-grant-scholarship-continuity/`、`domains/academic-advising-degree-progress-continuity/`、`domains/campus-basic-needs-student-support-continuity/`、`domains/campus-disability-accommodations-accessibility-continuity/`、`domains/campus-mental-health-crisis-student-support-continuity/`、`domains/campus-safety-title-ix-clery-continuity/` 和 `domains/international-student-sevis-status-continuity/` 负责高等教育入学转学衔接、学生资助奖助学金、学业指导学位进度、校园基本需求、校园残障便利、校园心理危机支持、校园安全 Title IX/Clery 和国际学生 SEVIS 身份连续性这些高等教育学生生命周期条件。
- `domains/email-account-recovery-continuity/`、`domains/phone-number-sim-portability-account-security-continuity/`、`domains/mfa-passkey-credential-recovery-continuity/`、`domains/password-manager-secret-vault-continuity/`、`domains/cloud-backup-file-sync-data-portability-continuity/`、`domains/messaging-contact-graph-portability-continuity/`、`domains/domain-dns-web-presence-continuity/` 和 `domains/platform-account-suspension-appeals-continuity/` 负责邮箱账号恢复、手机号 SIM 携转安全、MFA/passkey 凭证恢复、密码管理器密钥库、云备份文件同步数据可携带、消息联系人图谱可携带、域名 DNS Web 存在和平台账号停权申诉这些数字账户与通信可达连续性条件。
- `domains/personal-computing-device-lifecycle-repair-continuity/`、`domains/home-network-router-iot-security-continuity/`、`domains/software-supply-chain-dependency-provenance-continuity/`、`domains/software-update-vulnerability-patch-continuity/`、`domains/open-source-maintainer-sustainability-continuity/`、`domains/pki-certificate-cryptographic-trust-continuity/`、`domains/cloud-service-exit-interoperability-continuity/` 和 `domains/api-platform-dependency-runtime-continuity/` 负责个人计算设备生命周期维修、家庭网络路由器 IoT 安全、软件供应链来源证明、软件更新补丁、开源维护者可持续、PKI 证书密码信任、云服务退出互操作和 API 平台运行时依赖这些软件、设备与信任连续性条件。
- `domains/calendar-scheduling-appointment-continuity/`、`domains/notification-alert-routing-attention-continuity/`、`domains/reminder-alarm-routine-task-continuity/`、`domains/meeting-video-conferencing-remote-collaboration-continuity/`、`domains/document-capture-ocr-pdf-record-workflow-continuity/`、`domains/search-index-discovery-retrieval-continuity/`、`domains/personal-automation-integration-workflow-continuity/` 和 `domains/collaborative-document-permission-version-continuity/` 负责日历排程预约、通知警报路由、提醒闹钟例行任务、会议视频远程协作、文件捕获 OCR PDF 记录流、搜索索引发现检索、个人自动化集成工作流和协作文档权限版本这些个人操作与任务协调连续性条件。
- `domains/home-access-lock-key-entry-continuity/`、`domains/household-appliance-maintenance-repair-continuity/`、`domains/home-refrigeration-food-storage-continuity/`、`domains/cooking-meal-preparation-kitchen-safety-continuity/`、`domains/laundry-clothing-footwear-hygiene-continuity/`、`domains/household-cleaning-disinfection-pest-control-continuity/`、`domains/postal-parcel-delivery-pickup-continuity/` 和 `domains/household-maintenance-repair-contractor-continuity/` 负责住所进入、家电维护、家庭冷藏、烹饪备餐、衣物鞋履卫生、家庭清洁消毒害虫控制、邮件包裹接收和家庭维修承包商这些家庭物理运行连续性条件。
- `domains/personal-vehicle-maintenance-recall-repair-continuity/`、`domains/fuel-ev-charging-refueling-access-continuity/`、`domains/parking-curb-access-towing-impound-continuity/`、`domains/walking-bicycling-micromobility-continuity/`、`domains/paratransit-nemt-access-continuity/`、`domains/taxi-rideshare-demand-response-mobility-continuity/`、`domains/transit-fare-payment-toll-account-continuity/` 和 `domains/multimodal-trip-planning-real-time-wayfinding-continuity/` 负责车辆、补能、停车、主动出行、辅助交通、按需交通、移动支付和出行信息这些个人移动执行连续性条件。
- `domains/public-restroom-sanitation-hygiene-access-continuity/`、`domains/public-drinking-water-hydration-access-continuity/`、`domains/public-seating-shade-rest-cooling-access-continuity/`、`domains/community-resilience-hub-shelter-center-continuity/`、`domains/public-library-community-anchor-access-continuity/`、`domains/parks-recreation-green-space-access-continuity/`、`domains/public-wifi-device-charging-connectivity-continuity/` 和 `domains/public-accommodation-accessibility-service-continuity/` 负责公共厕所、公共饮水、公共休息遮阴、社区韧性/避难中心、图书馆社区锚点、公园绿地、公共 Wi-Fi/设备充电和公共场所无障碍服务这些公共空间生存接入连续性条件。
- `domains/grocery-retail-food-store-access-continuity/`、`domains/snap-ebt-redemption-retailer-payment-continuity/`、`domains/wic-benefit-redemption-infant-maternal-nutrition-continuity/`、`domains/food-bank-pantry-community-food-distribution-continuity/`、`domains/emergency-food-disaster-feeding-continuity/`、`domains/home-delivered-meals-congregate-nutrition-services-continuity/`、`domains/infant-formula-baby-food-supply-safety-continuity/` 和 `domains/prepared-food-restaurant-cafeteria-safety-access-continuity/` 负责 grocery/食品零售、SNAP EBT 兑换、WIC 母婴营养兑换、食品银行/pantry、灾害供餐、送餐/集体营养服务、婴儿配方/婴幼儿食品供应安全和餐馆/cafeteria 熟食安全可达这些食物获得执行连续性条件。
- `domains/retail-pharmacy-prescription-dispensing-continuity/`、`domains/pharmacy-benefit-formulary-prior-authorization-continuity/`、`domains/medication-reconciliation-regimen-adherence-continuity/`、`domains/patient-medication-labeling-counseling-continuity/`、`domains/unused-medicine-takeback-disposal-continuity/`、`domains/durable-medical-equipment-supplier-repair-continuity/`、`domains/home-oxygen-respiratory-equipment-supply-continuity/` 和 `domains/diabetes-insulin-glucose-monitoring-supplies-continuity/` 负责药房配药、药品福利/处方集/事前授权、用药核对与依从执行、患者药品标签/咨询理解、未用药回收处置、DME 供应维修、居家氧疗/呼吸设备供应和糖尿病胰岛素/血糖监测耗材这些治疗获得与医用品执行连续性条件。
- `domains/provider-directory-network-adequacy-continuity/`、`domains/primary-care-panel-appointment-access-continuity/`、`domains/specialist-referral-authorization-navigation-continuity/`、`domains/appointment-availability-wait-time-continuity/`、`domains/outpatient-laboratory-specimen-result-routing-continuity/`、`domains/diagnostic-imaging-order-scheduling-report-continuity/`、`domains/ambulatory-procedure-surgery-center-continuity/` 和 `domains/after-hours-urgent-care-triage-continuity/` 负责 provider 名录/网络充足性、初级照护 panel/预约、专科转诊/授权导航、预约容量/等待时间、门诊检验标本/结果路由、诊断影像医嘱/报告回传、门诊操作/ASC 和非工作时间 urgent care/triage 这些门诊访问与临床服务执行连续性条件。
- `domains/health-insurance-enrollment-renewal-continuity/`、`domains/insurance-eligibility-benefits-verification-continuity/`、`domains/medical-service-prior-authorization-utilization-management-continuity/`、`domains/claims-adjudication-eob-denial-continuity/`、`domains/patient-billing-payment-plan-continuity/`、`domains/price-transparency-good-faith-estimate-continuity/`、`domains/surprise-billing-balance-bill-protection-continuity/` 和 `domains/charity-care-financial-assistance-medical-debt-continuity/` 负责健康保险参保续保、权益核验、医疗服务授权、理赔/EOB/拒付、患者账单/付款计划、价格透明/GFE、意外账单保护和 charity care/医疗债务这些医疗支付执行连续性条件。
- `domains/patient-portal-account-message-continuity/`、`domains/medical-record-access-amendment-release-continuity/`、`domains/clinical-results-notification-followup-continuity/`、`domains/informed-consent-refusal-shared-decision-continuity/`、`domains/healthcare-language-interpreter-effective-communication-continuity/`、`domains/healthcare-disability-accommodation-accessibility-continuity/`、`domains/patient-grievance-complaint-ombuds-continuity/` 和 `domains/healthcare-civil-rights-nondiscrimination-continuity/` 负责患者门户/医疗消息、病历访问修正释放、临床结果通知随访、知情同意/拒绝/共同决策、医疗语言服务、医疗残障便利、患者投诉/ombuds 和医疗民权反歧视这些患者权利与临床沟通连续性条件。
- `domains/emergency-contact-next-of-kin-notification-continuity/`、`domains/personal-health-record-emergency-summary-continuity/`、`domains/medical-id-allergy-critical-alert-continuity/`、`domains/medication-list-implant-device-emergency-continuity/`、`domains/chronic-condition-emergency-action-plan-continuity/`、`domains/immunization-record-proof-continuity/`、`domains/organ-donor-registry-anatomical-gift-continuity/` 和 `domains/access-functional-needs-emergency-registry-continuity/` 负责主体无法表达、急救、灾害和死亡边界中的紧急联系人、急救健康摘要、医疗 ID/关键警报、药物/植入设备、慢病行动计划、免疫记录、器官捐赠登记和功能需求登记连续性条件。
- `domains/death-certificate-registration-cause-of-death-record-continuity/`、`domains/funeral-cremation-burial-disposition-continuity/`、`domains/cemetery-memorial-remains-location-continuity/`、`domains/bereavement-leave-grief-support-continuity/`、`domains/survivor-benefits-death-notification-continuity/`、`domains/life-insurance-beneficiary-claim-continuity/`、`domains/estate-inventory-asset-liability-handoff-continuity/` 和 `domains/post-death-account-closure-service-cancellation-continuity/` 负责死亡边界后的死亡证明/死因记录、遗体处置、墓地纪念、遗属恢复、遗属福利、寿险理赔、遗产清单和账户关闭服务取消连续性条件。
- `domains/loneliness-social-isolation-risk-continuity/`、`domains/social-prescribing-community-referral-continuity/`、`domains/mutual-aid-neighbor-support-network-continuity/`、`domains/volunteering-civic-service-participation-continuity/`、`domains/community-mediation-neighbor-conflict-resolution-continuity/`、`domains/restorative-justice-repair-accountability-continuity/`、`domains/reputation-defamation-public-trust-repair-continuity/`、`domains/references-vouching-recommendation-social-capital-continuity/` 和 `domains/third-place-belonging-social-participation-continuity/` 负责关系执行与社会资本连续性，覆盖孤独隔离风险、社会处方转介、互助邻里、志愿服务、社区调解、修复性司法、声誉信任修复、推荐背书和第三空间归属参与。
- `domains/purpose-meaning-existential-continuity/`、`domains/spiritual-care-religious-practice-continuity/`、`domains/cultural-heritage-identity-continuity/`、`domains/arts-creative-expression-participation-continuity/`、`domains/leisure-recreation-restorative-activity-continuity/`、`domains/narrative-identity-life-review-continuity/`、`domains/ritual-ceremony-life-transition-continuity/` 和 `domains/dignity-personhood-respect-continuity/` 负责意义、文化、身份与尊严连续性，覆盖主体为什么继续、如何表达、如何归属、如何被承认和如何避免被去人格化。
- `domains/human-factors-ergonomics-task-system-continuity/`、`domains/cognitive-load-workload-measurement-continuity/`、`domains/fatigue-risk-alertness-continuity/`、`domains/situational-awareness-decision-environment-continuity/`、`domains/handoff-checklist-procedure-reliability-continuity/`、`domains/incident-reporting-just-culture-learning-continuity/`、`domains/automation-bias-mode-confusion-oversight-continuity/` 和 `domains/alert-fatigue-interruption-signal-management-continuity/` 负责人因与操作可靠性连续性，覆盖人-工具-流程适配、认知负荷、疲劳警觉、情境感知、交接清单、事件学习、自动化监督和告警中断管理。
- `domains/disembodied-cns/` 负责去具身外部维持型中枢生命系统的高层架构建模，不提供实验操作协议。
- `domains/memory-editing/` 负责记忆编辑的概念、证据、验证和伦理边界，不提供可执行神经操控步骤。
- `domains/biostasis-cryopreservation/` 负责冷冻保存、生物停滞、休眠和等待未来修复路径。
- `domains/cognitive-augmentation/` 负责 AI 辅助、外部记忆、学习系统、脑机接口和行动放大工具。
- `domains/ai-agency-safety/` 负责 AI 代理、工具调用、授权、监督、审计、回滚和失效隔离。
- `domains/ai-evaluation-benchmark-validity-continuity/`、`domains/ai-red-teaming-adversarial-testing-continuity/`、`domains/ai-incident-reporting-post-deployment-monitoring-continuity/`、`domains/ai-data-provenance-contamination-drift-continuity/`、`domains/synthetic-data-generation-validation-continuity/`、`domains/ai-model-supply-chain-provenance-release-continuity/`、`domains/ai-agent-tool-permission-sandbox-continuity/`、`domains/human-ai-oversight-handoff-accountability-continuity/` 和 `domains/ai-resource-cost-latency-budget-continuity/` 负责 AI 评测、红队、部署后监控、数据谱系、合成数据、模型供应链、agent 工具权限、人机交接问责和资源成本延迟预算这些 AI 运行治理连续性条件。
- `domains/semiconductor-manufacturing-metrology-continuity/`、`domains/semiconductor-advanced-packaging-continuity/`、`domains/chip-design-eda-verification-ip-continuity/`、`domains/ai-hardware-accelerator-performance-continuity/`、`domains/data-center-cooling-water-thermal-continuity/`、`domains/large-load-grid-interconnection-transmission-continuity/`、`domains/grid-scale-energy-storage-flexibility-continuity/`、`domains/advanced-nuclear-energy-safety-generation-continuity/`、`domains/undersea-cable-internet-backbone-continuity/` 和 `domains/satellite-communications-spectrum-orbit-continuity/` 负责半导体制造计量、先进封装、芯片设计验证、AI 加速器性能、数据中心冷却水热、并网输电、储能灵活性、先进核能、海底光缆和卫星通信这些先进计算、能源与连接物理底座。
- `domains/cardiac-arrest-cpr-defibrillation-continuity/`、`domains/sepsis-shock-early-recognition-resuscitation-continuity/`、`domains/trauma-system-hemorrhage-control-continuity/`、`domains/intensive-care-organ-support-delirium-continuity/`、`domains/mechanical-ventilation-respiratory-failure-continuity/`、`domains/ecmo-extracorporeal-life-support-continuity/`、`domains/acute-kidney-injury-renal-replacement-continuity/`、`domains/transfusion-blood-management-hemorrhage-continuity/`、`domains/overdose-poisoning-reversal-toxicology-continuity/` 和 `domains/burn-injury-critical-care-rehabilitation-continuity/` 负责心脏骤停、脓毒症休克、创伤出血、ICU 多器官支持、呼吸衰竭、ECMO、急性肾损伤、输血、大量过量/中毒和烧伤这些急性死亡边界与临时器官支持条件。
- `domains/acute-coronary-syndrome-reperfusion-continuity/`、`domains/acute-heart-failure-decompensation-continuity/`、`domains/cardiac-arrhythmia-syncope-decompensation-continuity/`、`domains/venous-thromboembolism-pulmonary-embolism-continuity/`、`domains/hypertensive-crisis-end-organ-risk-continuity/`、`domains/diabetic-hyperglycemic-hypoglycemic-crisis-continuity/`、`domains/anaphylaxis-allergic-emergency-continuity/`、`domains/asthma-copd-exacerbation-airway-continuity/`、`domains/acute-gastrointestinal-bleeding-endoscopy-continuity/` 和 `domains/obstetric-emergency-hemorrhage-hypertension-continuity/` 负责急性冠脉综合征、急性心衰、心律失常/晕厥、VTE/肺栓塞、高血压危象、糖尿病急性危象、过敏性休克、哮喘/COPD 急性加重、急性消化道出血和产科急症这些进入骤停、ICU 或不可逆损伤之前的时间关键窗口。
- `domains/hypertension-detection-control-continuity/`、`domains/lipid-atherosclerosis-risk-management-continuity/`、`domains/prediabetes-diabetes-prevention-continuity/`、`domains/obesity-adiposity-metabolic-risk-continuity/`、`domains/tobacco-nicotine-cessation-continuity/`、`domains/alcohol-use-risk-reduction-continuity/`、`domains/chronic-kidney-disease-screening-progression-continuity/`、`domains/cancer-screening-early-detection-continuity/`、`domains/osteoporosis-fracture-prevention-bone-health-continuity/` 和 `domains/fall-risk-prevention-home-safety-continuity/` 负责高血压、血脂/ASCVD、糖尿病前期、肥胖代谢风险、烟草、酒精、CKD、癌筛、骨质疏松和跌倒风险这些急症与失能之前的长期筛查和风险因子执行层。
- `domains/bathroom-bathing-toileting-transfer-fall-safety-continuity/`、`domains/stairs-steps-handrail-threshold-fall-safety-continuity/`、`domains/home-lighting-nighttime-pathway-visibility-continuity/`、`domains/bedroom-bed-transfer-entrapment-safety-continuity/`、`domains/smoke-alarm-home-fire-escape-readiness-continuity/`、`domains/carbon-monoxide-alarm-combustion-appliance-safety-continuity/`、`domains/furniture-tv-tip-over-anchoring-child-safety-continuity/`、`domains/household-poison-storage-child-resistant-packaging-continuity/`、`domains/window-covering-cord-strangulation-child-safety-continuity/` 和 `domains/hot-water-scald-burn-prevention-continuity/` 负责把跌倒/家居安全总域拆成浴室、楼梯、夜间路径、卧室转移、火灾、CO、家具倾倒、毒物储存、窗饰拉绳和热水烫伤这些家庭伤害执行层。
- `domains/drowning-water-safety-supervision-continuity/`、`domains/pool-spa-barrier-drain-entrapment-safety-continuity/`、`domains/boating-life-jacket-watercraft-safety-continuity/`、`domains/child-passenger-safety-car-seat-restraint-continuity/`、`domains/bicycle-helmet-wheeled-sports-head-injury-prevention-continuity/`、`domains/playground-surface-equipment-fall-injury-prevention-continuity/`、`domains/sports-concussion-return-to-play-protocol-continuity/`、`domains/infant-safe-sleep-suid-risk-reduction-continuity/`、`domains/firearm-safe-storage-injury-prevention-continuity/` 和 `domains/atv-off-highway-vehicle-injury-prevention-continuity/` 负责把儿童、运动和娱乐伤害预防拆成溺水、水域设施、船艇、儿童乘员、轮式运动、游乐场、运动脑震荡、婴儿安全睡眠、枪支安全储存和 ATV/OHV 这些独立执行层。
- `domains/emergency-supply-kit-go-bag-rotation-continuity/`、`domains/family-emergency-communication-reunification-continuity/`、`domains/evacuation-route-transportation-shelter-plan-continuity/`、`domains/shelter-in-place-clean-air-room-indoor-protection-continuity/`、`domains/backup-power-battery-generator-safety-continuity/`、`domains/emergency-food-water-storage-treatment-continuity/`、`domains/refrigerated-medication-medical-device-power-outage-continuity/`、`domains/emergency-financial-document-cash-readiness-continuity/`、`domains/disability-access-functional-needs-personal-preparedness-continuity/` 和 `domains/older-adult-caregiver-disaster-preparedness-continuity/` 负责把家庭与个人应急准备拆成物资包、通信团聚、撤离、就地避险、备用电、食水、药物设备停电、金融文件、功能需求和老年照护者准备这些可独立审查的执行层。
- `domains/disaster-individual-assistance-benefits-navigation-continuity/`、`domains/disaster-temporary-housing-displacement-recovery-continuity/`、`domains/disaster-recovery-center-service-access-continuity/`、`domains/disaster-case-management-long-term-recovery-continuity/`、`domains/disaster-unemployment-income-disruption-continuity/`、`domains/disaster-legal-aid-rights-claims-continuity/`、`domains/disaster-debris-waste-sanitation-cleanup-continuity/`、`domains/post-flood-mold-moisture-indoor-recovery-continuity/`、`domains/disaster-behavioral-health-distress-recovery-continuity/` 和 `domains/disaster-volunteer-donations-management-continuity/` 负责把灾后恢复拆成个人援助导航、临时住房、恢复中心、长期个案管理、灾害收入中断、法律援助、废弃物卫生清理、洪水霉菌湿气、行为健康恢复和志愿捐赠管理这些可独立审查的恢复执行层。
- `domains/breast-cancer-screening-treatment-survivorship-continuity/`、`domains/colorectal-cancer-screening-treatment-continuity/`、`domains/lung-cancer-screening-treatment-continuity/`、`domains/prostate-cancer-screening-treatment-continuity/`、`domains/cervical-cancer-hpv-prevention-screening-continuity/`、`domains/ovarian-cancer-symptom-detection-treatment-continuity/`、`domains/pancreatic-cancer-high-risk-detection-treatment-continuity/`、`domains/liver-cancer-cirrhosis-surveillance-treatment-continuity/`、`domains/childhood-cancer-treatment-survivorship-continuity/` 和 `domains/cancer-survivorship-late-effects-continuity/` 负责器官/阶段特异癌症连续性，覆盖筛查路径、异常闭环、治疗负担、复发监测、晚期效应、家庭/工作/照护和幸存者生活质量。
- `domains/sleep-disordered-breathing-screening-treatment-continuity/`、`domains/chronic-insomnia-cbti-access-continuity/`、`domains/sexual-health-sti-prevention-continuity/`、`domains/hiv-testing-prep-prevention-continuity/`、`domains/chronic-viral-hepatitis-screening-liver-protection-continuity/`、`domains/contraception-family-planning-access-continuity/`、`domains/menstrual-health-cycle-literacy-continuity/`、`domains/perimenopause-menopause-midlife-health-continuity/`、`domains/pelvic-floor-continence-function-continuity/` 和 `domains/skin-cancer-uv-protection-early-detection-continuity/` 负责睡眠呼吸障碍、慢性失眠、性健康/STI、HIV、病毒性肝炎、避孕家庭计划、月经健康、更年期、盆底功能和 UV/皮肤癌预防这些生活史预防与功能连续性条件。
- `domains/chronic-pain-functional-restoration-continuity/`、`domains/low-back-pain-spine-function-continuity/`、`domains/osteoarthritis-joint-function-continuity/`、`domains/autoimmune-rheumatic-disease-inflammatory-burden-continuity/`、`domains/inflammatory-bowel-disease-digestive-continuity/`、`domains/chronic-liver-disease-masld-mash-continuity/`、`domains/thyroid-disease-endocrine-function-continuity/`、`domains/iron-deficiency-anemia-oxygen-carrying-continuity/`、`domains/asthma-copd-maintenance-control-continuity/` 和 `domains/allergic-atopic-disease-immunologic-burden-continuity/` 负责慢性疼痛、腰背痛、骨关节炎、自身免疫风湿病、炎症性肠病、MASLD/MASH 慢性肝病、甲状腺疾病、铁缺乏贫血、哮喘/COPD 长期控制和过敏/特应性疾病这些慢性专科负担与功能恢复条件。
- `domains/parkinsons-disease-movement-control-continuity/`、`domains/multiple-sclerosis-demyelination-function-continuity/`、`domains/amyotrophic-lateral-sclerosis-motor-neuron-continuity/`、`domains/huntington-disease-genetic-neurodegeneration-continuity/`、`domains/spinal-muscular-atrophy-motor-neuron-continuity/`、`domains/muscular-dystrophy-progressive-weakness-continuity/`、`domains/myasthenia-gravis-neuromuscular-junction-continuity/`、`domains/spinal-cord-injury-paralysis-secondary-complications-continuity/`、`domains/me-cfs-post-exertional-energy-limitation-continuity/` 和 `domains/long-covid-post-acute-infection-continuity/` 负责帕金森病、多发性硬化、ALS、亨廷顿病、脊髓性肌萎缩症、肌营养不良、重症肌无力、脊髓损伤、ME/CFS 和 Long COVID 这些慢性神经退行、神经肌肉与感染后功能连续性条件。
- `domains/digital-identity-security/` 负责数字身份、账号、凭据、身份恢复、服务入口和数据可携带。
- `domains/mental-health-affective-stability/` 负责心理健康、情绪稳定、动机、成瘾、创伤和自杀风险。
- `domains/depression-mood-disorder-functioning-continuity/`、`domains/anxiety-stress-threat-regulation-continuity/`、`domains/trauma-ptsd-adversity-recovery-continuity/`、`domains/psychosis-reality-testing-community-continuity/`、`domains/bipolar-mood-episode-stability-continuity/`、`domains/adhd-executive-function-neurodevelopment-continuity/`、`domains/autism-neurodiversity-support-continuity/` 和 `domains/eating-disorders-nutrition-body-continuity/` 负责心理健康、神经发育与功能连续性，覆盖抑郁心境功能、焦虑压力威胁调节、创伤/PTSD 恢复、精神病性现实检验、双相情绪周期稳定、ADHD 执行功能、自闭神经多样性支持和进食障碍营养身体连续性。
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
- `domains/purpose-meaning-existential-continuity/`、`domains/spiritual-care-religious-practice-continuity/`、`domains/cultural-heritage-identity-continuity/`、`domains/arts-creative-expression-participation-continuity/`、`domains/leisure-recreation-restorative-activity-continuity/`、`domains/narrative-identity-life-review-continuity/`、`domains/ritual-ceremony-life-transition-continuity/` 和 `domains/dignity-personhood-respect-continuity/` 负责目的意义、精神照护、文化身份、创造表达、休闲恢复、叙事身份、仪式承认和尊严人格。
- `domains/human-factors-ergonomics-task-system-continuity/`、`domains/cognitive-load-workload-measurement-continuity/`、`domains/fatigue-risk-alertness-continuity/`、`domains/situational-awareness-decision-environment-continuity/`、`domains/handoff-checklist-procedure-reliability-continuity/`、`domains/incident-reporting-just-culture-learning-continuity/`、`domains/automation-bias-mode-confusion-oversight-continuity/` 和 `domains/alert-fatigue-interruption-signal-management-continuity/` 负责人因工效、认知负荷、疲劳警觉、情境感知、交接清单、事件学习、自动化监督和告警中断管理。
- `domains/depression-mood-disorder-functioning-continuity/`、`domains/anxiety-stress-threat-regulation-continuity/`、`domains/trauma-ptsd-adversity-recovery-continuity/`、`domains/psychosis-reality-testing-community-continuity/`、`domains/bipolar-mood-episode-stability-continuity/`、`domains/adhd-executive-function-neurodevelopment-continuity/`、`domains/autism-neurodiversity-support-continuity/` 和 `domains/eating-disorders-nutrition-body-continuity/` 负责心理健康、神经发育和功能连续性的证据边界，不提供诊断、治疗、药物、危机处置、饮食控制、行为训练、家庭干预、个体风险评分、招聘/教育筛选或敏感资料收集。
- `domains/governance-rights/` 负责主体权利、法律身份、同意、退出、数据权、AI 治理和研究伦理。
- `domains/pain-suffering-control/` 负责疼痛、痛苦、症状负担、姑息医学和可承受持续性。
- `domains/health-literacy-navigation/` 负责健康素养、医疗服务导航、可理解信息、风险沟通和共同决策。
- `domains/language-access-plain-communication/` 负责清晰语言、语言服务、有限英语能力访问、CLAS、认知可访问性和关键服务材料理解。
- `domains/labor-rights-workplace-protection/` 负责劳动标准、工资工时、安全权利、反歧视、反报复、申诉入口和劳动组织治理。
- `domains/oral-health-continuity/` 负责口腔健康、牙齿、牙周、咀嚼、疼痛、感染、营养和沟通连续性。
- `domains/dental-caries-prevention-restoration-continuity/`、`domains/periodontal-disease-systemic-inflammation-continuity/`、`domains/tooth-loss-prosthodontic-chewing-continuity/`、`domains/dental-pain-emergency-infection-continuity/`、`domains/oral-cancer-mucosal-lesion-early-detection-continuity/`、`domains/pediatric-oral-health-development-continuity/`、`domains/geriatric-long-term-care-oral-health-continuity/`、`domains/dental-care-access-insurance-workforce-continuity/`、`domains/xerostomia-salivary-function-oral-medication-continuity/` 和 `domains/temporomandibular-orofacial-pain-jaw-function-continuity/` 负责把口腔健康拆成牙体、牙周、缺牙修复、急性牙痛感染、口腔癌、儿童/老年口腔、服务可及、唾液功能和颌面痛这些可独立审查的持续性条件。
- `domains/measurement-feedback/` 负责主体状态测量、风险评分、生物标志物、可穿戴、预测模型和反馈闭环。
- 原始资料归档在 `docs/source-notes/`；稳定结论必须沉淀到 `docs/` 或对应子域 README，不能长期依赖零散临时文件名。

## 设计原则

- Human Infra 的上位对象是“人类任务执行系统”，不是单一长寿产品。
- Longevity Evidence 承接原 Biocat，但不再占据根目录概念中心。
- “永生”的不同路径必须按机制拆分：长寿证据、营养代谢、基因组稳定性、端粒维护、蛋白稳态、自噬、线粒体、细胞衰老、细胞外基质与糖化、微生物生态、干细胞储备、肝肾清除、消化屏障与吸收、呼吸氧合、血液氧运与止血、内分泌激素调节、淋巴与脑淋巴清除、体液电解质酸碱稳态、热稳态、身体活动、心血管韧性、肌骨完整性、皮肤屏障与伤口愈合、泌尿生殖连续性、生殖与生育连续性、注意力与执行控制、学习与技能获得、教育可及与终身学习、时间分配与有效时间、财务韧性、金融包容与支付系统、就业服务、健康劳动力容量、职业与工作设计、信息完整性与信任、媒体信息素养与公共图书馆、科研基础设施与开放科学转化、标准计量与质量基础设施、网络安全韧性与关键服务、算力数据中心与 AI 基础设施、临床试验与监管科学转化、空间定位导航与位置基础设施、天气气候观测与预报、空间天气与地磁暴、行星防御与近地天体、火山灰、地震、海啸、极端高温与制冷公共卫生、建筑消防与生命安全规范、制造与维修能力、公共采购与合同能力、动物健康与 One Health 界面、公共卫生实验室与诊断能力、血液器官组织生物警戒、废弃物与危险材料连续性、辐射核安全防护、化学安全与中毒控制、关键矿物材料韧性、食物安全、水卫生连续性、能源韧性、医疗服务连续性、社区健康工作者与同伴支持、药品与治疗连续性、患者数据互操作、远程照护、健康数据隐私治理、功能与生活质量结局、健康经济与价值评估、免疫与公共卫生监测、母婴儿童早期生命、患者安全与组织学习、社会决定因素与社区脆弱性、公共服务设计与可达性、行政负担与程序摩擦、公民数据与开放政府透明、社区资源导航、照护与长期照护、住房与建成环境、交通接入、法律身份与民事登记、司法可及与法律援助、公民参与与选举接入、迁移流离失所与人道连续性、数字包容与连接、社会保护与福利递送、保险与风险转移、托育与家庭连续性、劳动权利与工作场所保护、语言可达与清晰沟通、应急准备与响应、应急预警与通信、家庭应急准备与韧性、灾后恢复与救济连续性、人身安全与暴力预防、产品安全与召回系统、细胞重编程、基因治疗与基因编辑递送安全、生物年龄钟验证、多组学个人基线、工程细胞疗法、类器官组织芯片模型、异种移植与工程器官替换、再生医学、康复功能、癌症控制、免疫维护、抗微生物韧性、神经连续性、感官连续性、未来等待、生物停滞、去具身中枢、记忆编辑、认知增强、AI 代理安全、数字身份安全、心理稳定、睡眠恢复、辅助技术、社会连接、目的意义、精神照护、文化身份、艺术创造、休闲恢复、叙事身份、仪式过渡、尊严人格、物质暴露控制、资源环境、供应链连续性、合成生物学与生物安全、空间极端栖居、风险工程、健康素养导航、治理权利、口腔健康、痛苦控制和测量反馈不能混成一个概念桶。
- 所有健康、神经、生命支持相关结论必须保留来源、适用对象、不确定性和伦理边界。
- 新增研究域必须能回到 `docs/reference/research-domain-atlas.md` 的先验条件和域判定契约。
- 有效永生 A-K 主干域优先从 `docs/reference/transcendental-domain-index.md` 进入；若候选对象已落入既有主干域，先补域内资料，不重复建目录。
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
- 2026-06-30：新增第五十二波 8 个个人移动执行连续性域，覆盖个人车辆维护召回维修、燃料/EV 充电补能、停车路缘拖车扣押、步行骑行微移动、paratransit/NEMT、出租车网约车需求响应交通、交通票卡/过路费账户和多模式实时导向。
- 2026-06-30：新增第五十三波 8 个公共空间生存接入连续性域，覆盖公共厕所卫生、公共饮水补水、公共座椅遮阴休息降温、社区韧性/避难中心、公共图书馆社区锚点、公园娱乐绿地、公共 Wi-Fi/设备充电和公共场所无障碍服务。
- 2026-06-30：新增第五十四波 8 个食物获得执行连续性域，覆盖 grocery/食品零售、SNAP EBT 兑换、WIC 母婴营养兑换、食品银行/pantry、灾害供餐、送餐/集体营养服务、婴儿配方/婴幼儿食品供应安全和餐馆/cafeteria 熟食安全可达。
- 2026-06-30：新增第五十五波 8 个治疗获得与医用品执行连续性域，覆盖药房处方配药、药品福利/处方集/事前授权、用药核对与依从执行、患者药品标签/咨询理解、未用药回收处置、DME 供应维修、居家氧疗/呼吸设备供应和糖尿病胰岛素/血糖监测耗材连续性。
- 2026-06-30：新增第五十六波 8 个门诊访问与临床服务执行连续性域，覆盖 provider 名录/网络充足性、初级照护 panel/预约、专科转诊/授权导航、预约容量/等待时间、门诊检验标本/结果路由、诊断影像医嘱/报告回传、门诊操作/ASC 和非工作时间 urgent care/triage 连续性。
- 2026-06-30：新增第五十七波 8 个医疗支付、理赔、账单与成本保护连续性域，覆盖健康保险参保续保、权益核验、医疗服务授权、理赔/EOB/拒付、患者账单/付款计划、价格透明/GFE、意外账单保护和 charity care/医疗债务连续性。
- 2026-06-30：新增第五十八波 8 个患者权利、记录访问、临床沟通与医疗民权连续性域，覆盖患者门户/医疗消息、病历访问修正释放、临床结果通知随访、知情同意/拒绝/共同决策、医疗语言服务、医疗残障便利、患者投诉/ombuds 和医疗民权反歧视连续性。
- 2026-06-30：新增第五十九波 8 个急救健康信息与紧急交接连续性域，覆盖紧急联系人/近亲通知、个人健康记录急救摘要、医疗 ID/过敏关键警报、药物清单/植入设备急救转交、慢病急救行动计划、免疫记录证明、器官捐赠登记和 access/functional needs 急救登记连续性。
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
- 2026-07-01：新增第八十九波 10 个视觉失效与眼病功能连续性域，覆盖白内障、青光眼、糖尿病视网膜病变、年龄相关性黄斑变性、屈光不正、低视力康复、干眼、眼外伤、儿童视筛弱视和视网膜脱离。
- 2026-07-01：新增第九十波 10 个听觉沟通执行连续性域，覆盖年龄相关听损、噪声性听损、耳鸣、儿童中耳炎、突发听损、人工耳蜗、新生儿听筛、听觉处理、听觉辅助设备和字幕/中继沟通访问。
- 2026-07-01：新增第九十一波 10 个前庭、平衡与空间定向执行连续性域，覆盖 BPPV、梅尼埃病、前庭神经炎/迷路炎、PPPD、前庭性偏头痛、双侧前庭低下、前庭康复、步态平衡筛查、运动病/虚拟环境耐受和耳毒性前庭风险。
- 2026-07-01：新增第九十二波 10 个言语语言沟通执行连续性域，覆盖失语、构音障碍、言语失用、嗓音障碍、口吃、发展性语言障碍、语音障碍、AAC、社会语用沟通和认知沟通障碍。
- 2026-07-01：新增第九十三波 10 个吞咽、摄食与营养入口执行连续性域，覆盖口咽吞咽、食管吞咽、误吸肺炎、窒息、质地调整饮食/稠液、管饲、儿童摄食吞咽、卒中后吞咽、神经退行性吞咽和进食协助/用餐尊严。
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
- 2026-06-30：新增第六十波死亡后与遗属连续性研究域，覆盖死亡证明/死因记录、遗体处置、墓地纪念、丧亲恢复、遗属福利、寿险理赔、遗产清单和死亡后账户关闭。
- 2026-07-01：新增第六十一波关系执行与社会资本连续性研究域，覆盖孤独隔离风险、社会处方社区转介、互助邻里支持、志愿服务公民参与、社区调解、修复性司法、声誉信任修复、推荐背书和第三空间归属参与。
- 2026-07-01：新增第六十二波意义、文化、身份与尊严连续性研究域，覆盖目的意义、精神照护、文化遗产、艺术创造表达、休闲娱乐恢复、叙事身份生命回顾、仪式典礼生命过渡和尊严人格承认。
- 2026-07-01：新增第六十三波人因与操作可靠性连续性研究域，覆盖人因工效学任务系统、认知负荷/工作负荷测量、疲劳风险/警觉性、情境感知/决策环境、交接清单/过程可靠性、事件报告/公正文化学习、自动化偏误/模式混淆监督和告警疲劳/中断信号管理。
- 2026-07-01：新增第六十四波心理健康、神经发育与功能连续性研究域，覆盖抑郁心境功能、焦虑压力威胁调节、创伤/PTSD 恢复、精神病性现实检验、双相情绪周期稳定、ADHD 执行功能、自闭神经多样性支持和进食障碍营养身体连续性。
- 2026-07-01：新增第六十五波伴侣动物、服务动物与宠物照护连续性研究域，覆盖人-动物纽带/伴侣照护、兽医可及费用、服务动物残障可达、宠物身份微芯片重聚、宠物食药供应安全、宠物灾害撤离避难、动物收容救助再安置和动物福利虐待报告。
- 2026-07-01：新增第六十六波旅行、临时住宿与跨境移动执行连续性研究域，覆盖长距离旅行预订行程、航空中断退款、航空安检身份核验、行李个人物品、临时住宿接入、旅行警示领事协助、旅行健康准备和海关边境申报。
- 2026-07-01：新增第六十七波消费者交易、履约与市场信任连续性研究域，覆盖在线零售订单履约、退货退款争议、消费品保修维修、维修权零件手册、支付卡争议未授权扣款、礼品卡预付储值、价格费用披露和消费者评价背书市场信任。
- 2026-07-01：新增第六十八波消费者信贷、贷款服务与跨期资源连续性研究域，覆盖信用卡循环信用成本、消费贷款 APR 披露、房贷服务止赎、车贷租赁收车、学生贷款还款减免、发薪日小额高成本贷款、BNPL 分期融资和汇款转账费用汇率披露。
- 2026-07-01：新增第六十九波个人保险、财产责任、灾害与理赔执行连续性研究域，覆盖汽车保险责任碰撞理赔、房主租客财产理赔、洪水/NFIP 理赔、风暴野火地震巨灾保险、残障收入保险理赔、长期照护福利启动、旅行保险行程保护理赔和个人责任伞形保险防御。
- 2026-07-01：新增第七十波受害者安全、服务与恢复执行连续性研究域，覆盖家庭暴力/胁迫控制、性暴力医疗 forensic exam 与 advocacy、跟踪骚扰保护令、受害者/证人权利通知、犯罪受害者补偿与 restitution、安全住所 emergency transfer、人口贩运受害者识别服务和失踪人员/无名遗体身份恢复。
- 2026-07-01：新增第七十一波住房 tenure 稳定与可居住性执行连续性研究域，覆盖租赁租约居住权、驱逐预防法院 diversion、应急租金援助与欠租、住房选择券/公屋、公平住房/合理便利、住房可居住性检查 code enforcement、HUD 批准住房咨询和制造房屋园区 tenure 安全。
- 2026-07-01：新增第七十二波法院接入与民事程序执行连续性研究域，覆盖自行诉讼人自助、法院电子 filing、远程/混合 hearing、法院语言服务、法院残障便利、法院罚金费用支付能力、陪审传票 hardship 和小额民事纠纷恢复。
- 2026-07-01：新增第七十三波个人数据权利、隐私暴露与数据经纪连续性研究域，覆盖数据经纪登记/退出/删除、隐私权访问更正删除、退出偏好信号与同意撤回、商业监控广告画像、敏感位置数据、生物特征模板治理、儿童青少年数据隐私和数据泄露通知身份恢复。
- 2026-07-01：新增第七十四波数字内容可信、合成媒体与冒充风险连续性研究域，覆盖内容来源凭据、合成媒体水印披露、AI 冒充 deepfake fraud、电话 caller ID 认证、邮件域名认证、官网品牌冒充、数字证据保存链和平台内容审核通知申诉。
- 2026-07-01：新增第七十五波知识产权、数字作品与 AI 训练数据权利连续性研究域，覆盖版权作者身份登记许可、DMCA 通知反通知、Creative Commons 开放内容、开源软件许可证、商标品牌身份、专利发明披露维护、创作者版税权利元数据和 AI 训练数据权利/退出/provenance。
- 2026-07-01：新增第七十六波科研身份、持久标识与可复现研究基础设施研究域，覆盖 ORCID/ROR、DOI 元数据、FAIR 数据仓库、研究软件胶囊、预注册、实验协议版本、贡献者角色、利益冲突披露和研究产物保存。
- 2026-07-01：新增第七十七波证据综合与指南转化连续性研究域，覆盖系统综述协议/检索/筛选、风险偏倚与批判性评价、Meta 分析与异质性、发表/报告偏倚、GRADE 证据确定性、证据到决策、指南评价/适配/本地化、活证据监测更新和快速综述/紧急证据分诊。
- 2026-07-01：新增第七十八波科研纠错、出版完整性与科学传播连续性研究域，覆盖科研不端调查纠错、撤稿/表达关注/更正、预印本版本与公开评审、期刊编辑与同行评审完整性、掠夺性出版与 paper mill 检测、引用网络主张传播、科研指标激励、复制/复现/多实验室验证和科学传播证据转译。
- 2026-07-01：新增第七十九波 AI 评测与运行治理连续性研究域，覆盖 AI 评测基准有效性、红队对抗测试、事故报告部署后监控、数据谱系污染漂移、合成数据验证、模型供应链发布、agent 工具权限沙箱、人机监督交接问责和 AI 资源成本延迟预算。
- 2026-07-01：新增第八十波先进计算、能源与连接底座连续性研究域，覆盖半导体制造计量、先进封装、芯片设计/EDA/IP 验证、AI 加速器性能、数据中心冷却水热、大型负载并网输电、电网级储能灵活性、先进核能安全发电、海底光缆互联网骨干和卫星通信频谱轨道。
- 2026-07-01：新增第八十一波急性救援与临时器官支持连续性研究域，覆盖心脏骤停 CPR/除颤、脓毒症休克早识别复苏、创伤系统出血控制、ICU 器官支持谵妄、机械通气呼吸衰竭、ECMO/ECLS、急性肾损伤肾脏替代、输血血液管理、过量/中毒逆转毒理和烧伤重症康复。
- 2026-07-01：新增第八十二波急性内科与时间关键急症连续性研究域，覆盖急性冠脉综合征再灌注、急性心衰失代偿、心律失常/晕厥、静脉血栓栓塞/肺栓塞、高血压危象、糖尿病高低血糖危象、过敏性休克、哮喘/COPD 急性加重、急性消化道出血和产科出血/高血压急症。
- 2026-07-01：新增第八十三波预防筛查与风险因子控制连续性研究域，覆盖高血压检测控制、血脂/动脉粥样硬化风险管理、糖尿病前期预防、肥胖/脂肪代谢风险、烟草尼古丁戒断、酒精风险降低、CKD 筛查进展、癌症筛查早诊、骨质疏松骨折预防和跌倒/家居安全预防。
- 2026-07-01：新增第八十四波生活史预防与功能连续性研究域，覆盖睡眠呼吸障碍、慢性失眠/CBT-I 可及、STI 预防、HIV 检测/PrEP、慢性病毒性肝炎、避孕与家庭计划、月经健康、围绝经期/更年期、盆底控尿控便和皮肤癌/UV 防护。
- 2026-07-01：新增第八十五波慢性专科负担与功能恢复连续性研究域，覆盖慢性疼痛、腰背痛、骨关节炎、自身免疫风湿病、炎症性肠病、MASLD/MASH 慢性肝病、甲状腺疾病、铁缺乏贫血、哮喘/COPD 长期控制和过敏/特应性疾病。
- 2026-07-01：新增第八十六波慢性神经退行、神经肌肉与感染后功能连续性研究域，覆盖帕金森病、多发性硬化、ALS、亨廷顿病、脊髓性肌萎缩症、肌营养不良、重症肌无力、脊髓损伤、ME/CFS 和 Long COVID。
- 2026-07-01：新增第八十七波器官/阶段特异癌症连续性研究域，覆盖乳腺癌、结直肠癌、肺癌、前列腺癌、宫颈癌、卵巢癌、胰腺癌、肝癌、儿童癌症和癌症幸存者晚期效应。
- 2026-07-01：新增第八十八波口腔、牙科与颌面功能连续性研究域，覆盖龋病、牙周病、缺牙修复咀嚼、牙痛急性感染、口腔癌早期识别、儿童口腔、老年长期照护口腔、牙科服务可及性、口干唾液功能和颞下颌/口颌面痛。
- 2026-07-01：新增第九十四波 10 个泌尿与肾脏替代执行连续性域，覆盖尿路感染/肾盂肾炎/尿源性脓毒症、导尿相关 UTI、尿潴留、膀胱过度活动/夜尿、肾结石梗阻、BPH/LUTS、尿流改道/尿路造口、透析通路、家庭透析供应和肾移植免疫抑制。
- 2026-07-01：新增第九十五波 10 个皮肤屏障、伤口、压力损伤与皮肤病执行连续性域，覆盖压力损伤预防、慢性伤口、伤口感染/蜂窝织炎、糖尿病足、烧伤后创面、手术切口/SSI、潮湿相关皮炎、湿疹、银屑病和皮肤护理用品。
- 2026-07-01：新增第九十六波 10 个居家伤害预防与家庭安全执行连续性域，覆盖浴室洗澡如厕转移、楼梯台阶扶手门槛、夜间路径照明、卧室床转移夹陷、烟雾报警家庭逃生、一氧化碳报警燃烧设备、家具/电视倾倒锚固、家庭毒物储存儿童防护包装、窗饰拉绳勒颈和热水烫伤预防。
- 2026-07-01：新增第九十七波 10 个儿童、运动与娱乐伤害预防执行连续性域，覆盖溺水水域安全、泳池/水疗池屏障与排水夹陷、船艇救生衣、儿童乘员约束、轮式运动头部伤害、游乐场表面设备、运动脑震荡返学返赛、婴儿安全睡眠、枪支安全储存和 ATV/OHV 伤害预防。
- 2026-07-01：新增第九十八波 10 个家庭与个人应急准备执行连续性域，覆盖应急物资包、家庭应急通信团聚、撤离交通避难、就地避险清洁空气房、备用电与发电机安全、应急食水、温控药品/医疗设备停电、应急金融文件现金、残障功能需求个人准备和老年照护者灾害准备。
- 2026-07-01：新增第九十九波 10 个灾后恢复执行连续性域，覆盖个人援助导航、临时住房、恢复中心、长期个案管理、灾害失业收入中断、灾害法律援助、废弃物卫生清理、洪水后霉菌湿气、灾害行为健康和志愿捐赠管理。
- 2026-07-01：新增第一百波 10 个传染病暴发响应执行连续性域，覆盖病例调查接触追踪、隔离检疫工作学校、社区检测筛查、疫苗行动加强针递送、口罩呼吸防护、室内通风过滤、学校工作场所运营、医疗挤兑分诊容量、医疗对策储备分发和污水病原体早期预警。
- 2026-07-01：新增第一百零一波 10 个危险材料与工业事故执行连续性域，覆盖化学释放避险撤离、社区化学风险知情披露、HazMat 事故指挥、工业过程安全、有毒羽流空气监测、HAZWOPER 响应者 PPE、暴露后去污分诊、危险材料运输 ERG、油污危险释放响应恢复和电池热失控火灾风险。
- 2026-07-01：新增 `docs/reference/transcendental-domain-index.md`，把有效永生 A-K 主干域整理为先验追问入口，避免重复建立同义研究域。
- 2026-07-01：新增第一百零二波 10 个强天气与自然 hazard 执行连续性域，把官方预警到主体保护行动的转换层纳入 Human Infra。
