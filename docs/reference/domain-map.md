# 域地图

Human Infra 的上位对象是“人类任务执行系统”。不同子域分别处理这个系统的不同层次、尺度和风险。

## 目标终态

如果没有历史包袱，项目应按下面的边界组织：

- `docs/`：稳定理论、伦理原则、域地图和资料归档。
- `domains/longevity-evidence/`：健康寿命、干预证据、临床试验和安全边界。
- `domains/nutrition-metabolic-health/`：营养、饮食质量、代谢健康、体重、糖尿病风险和食物环境。
- `domains/genomic-stability-dna-repair/`：基因组稳定性、DNA 损伤、修复系统、突变负荷和癌前风险。
- `domains/telomere-maintenance/`：端粒长度、端粒酶、复制衰老、组织更新和癌症风险。
- `domains/cellular-reprogramming/`：细胞重编程、表观遗传年轻化、身份保持和肿瘤风险边界。
- `domains/gene-therapy-genome-editing-delivery-safety/`：基因治疗、基因编辑、递送载体、表达控制、长期随访和遗传安全。
- `domains/biological-age-clocks-biomarker-validation/`：表观遗传年龄钟、组学年龄、功能年龄、衰老 biomarker、替代终点和验证边界。
- `domains/multiomics-personal-baseline-systems-biology/`：基因组、表观组、转录组、蛋白组、代谢组、微生物组、纵向个人基线和系统生物学。
- `domains/engineered-cell-therapy-regenerative-platforms/`：CAR-T、TCR-T、TIL、NK、iPSC 衍生细胞、可编程细胞和活体药物安全。
- `domains/organoids-organ-on-chip-disease-models/`：类器官、organ-on-chip、组织芯片、患者来源模型、替代方法和模型验证。
- `domains/xenotransplantation-bioengineered-organ-replacement/`：异种移植、基因编辑动物器官、工程器官、器官保存灌注和替代性器官供给。
- `domains/proteostasis-autophagy/`：蛋白稳态、自噬、溶酶体、蛋白聚集和细胞质量控制。
- `domains/mitochondrial-bioenergetics/`：线粒体功能、细胞能量、氧化应激、疲劳和行动能力。
- `domains/cellular-senescence-clearance/`：细胞衰老、SASP、senolytics、组织炎症和衰老细胞负担。
- `domains/extracellular-matrix-glycation/`：细胞外基质、胶原、弹性、糖化终产物、交联和纤维化。
- `domains/microbiome-ecology/`：宿主-微生物生态、菌群失调、代谢、免疫和炎症。
- `domains/stem-cell-reserve-renewal/`：干细胞储备、生态位、组织更新、内源性修复和再生能力。
- `domains/regenerative-medicine/`：再生医学、组织修复、器官再生和部件替换。
- `domains/gastrointestinal-barrier-absorption/`：消化、吸收、肠道屏障、胃肠动力和营养进入系统。
- `domains/respiratory-oxygenation/`：呼吸系统、气体交换、氧合、通气、睡眠呼吸和空气暴露。
- `domains/blood-oxygen-hemostasis/`：血液、红细胞、氧气运输、凝血、出血、血栓和血液安全。
- `domains/endocrine-hormonal-regulation/`：内分泌系统、激素轴、反馈环、代谢信号和跨器官稳态。
- `domains/lymphatic-glymphatic-clearance/`：淋巴系统、组织液、免疫运输、脑淋巴/类淋巴清除和水肿风险。
- `domains/fluid-electrolyte-acid-base-homeostasis/`：水分、电解质、渗透压、酸碱平衡和内环境化学稳态。
- `domains/thermal-homeostasis-resilience/`：体温调节、热暴露、寒冷暴露、散热、出汗和温度韧性。
- `domains/physical-activity-mobility/`：身体活动、久坐、心肺适能、力量、平衡和移动能力。
- `domains/cardiovascular-resilience/`：心脏、血管、血压、动脉粥样硬化、血栓、卒中和心衰。
- `domains/musculoskeletal-integrity/`：肌肉、骨骼、关节、跌倒、连接组织和行动承载结构。
- `domains/skin-barrier-wound-healing/`：皮肤屏障、伤口愈合、压力损伤、感染入口、热调节和触觉边界。
- `domains/urogenital-continuity/`：膀胱、尿路、尿控、盆底、泌尿感染、性功能和日常尊严。
- `domains/reproductive-fertility-continuity/`：生育力、生殖衰老、配子质量、妊娠风险、生殖自主性和未来选择权。
- `domains/attention-executive-control/`：注意力、执行功能、工作记忆、抑制控制、任务切换、冲动控制和分心环境。
- `domains/learning-skill-acquisition/`：学习科学、技能形成、训练反馈、迁移能力、再训练和终身学习。
- `domains/time-allocation-effective-time/`：时间使用、时间贫困、行政负担、等待成本、任务摩擦、有效时间和主观时间。
- `domains/financial-resilience-access/`：收入稳定、储蓄缓冲、债务、保险、医疗支付能力、财务冲击和资源可及性。
- `domains/occupational-work-design/`：职业安全、工作组织、人体工学、工时、职业暴露、压力、倦怠和工作可持续性。
- `domains/information-integrity-trust/`：信息可信度、证据质量、误导信息、平台传播、AI 生成内容和信任链。
- `domains/food-security-nutrition-access/`：食物安全、食物可得性、可负担性、食品安全、营养输入、价格冲击和供应稳定。
- `domains/water-sanitation-hygiene-continuity/`：安全饮用水、卫生设施、洗手、污水处理、WASH 覆盖和服务可靠性。
- `domains/energy-access-resilience/`：电力、清洁烹饪、能源负担、停电、温控、通信供能和医疗设备供电。
- `domains/healthcare-access-continuity/`：初级卫生保健、急诊、预防、转诊、随访、费用、质量和医疗服务连续性。
- `domains/medicine-access-treatment-continuity/`：基本药物、药品短缺、标签、患者药品信息、覆盖、费用和用药安全。
- `domains/patient-data-interoperability/`：健康记录访问、数据可携带、互操作标准、授权应用和跨机构数据连续性。
- `domains/telehealth-remote-monitoring-access/`：远程医疗、远程患者监测、居家设备、覆盖规则和数字照护连续性。
- `domains/health-data-privacy-governance/`：健康、基因、行为、神经和服务数据的隐私、同意、退出、安全、共享和用途边界。
- `domains/functioning-quality-of-life-outcomes/`：功能状态、生活质量、症状负担、患者报告结局和主体中心结果。
- `domains/health-economics-value-assessment/`：疾病负担、成本效果、HTA、价值框架、预算影响、资源分配和公平边界。
- `domains/immunization-public-health-surveillance/`：免疫计划、传染病监测、公共卫生应急、感染防控、AMR、One Health 和废水监测。
- `domains/maternal-newborn-child-development/`：孕产健康、新生儿健康、儿童健康、生长标准、早期发展和养育照护。
- `domains/patient-safety-organizational-learning/`：患者安全、事件报告、团队沟通、根因分析、CUSP、TeamSTEPPS 和安全文化。
- `domains/caregiving-long-term-care/`：家庭照护、长期照护、居家社区支持、照护协调、照护者负担和尊严边界。
- `domains/housing-built-environment-stability/`：住房稳定、住房质量、室内环境、无障碍、社区资源和建成环境健康。
- `domains/transportation-access-mobility/`：公共交通、无障碍交通、出行时间、医疗交通、交通成本和外部资源可达性。
- `domains/legal-identity-civil-registration/`：法律身份、出生登记、民事登记、生命统计、身份文件、身份覆盖和服务资格。
- `domains/access-to-justice-legal-aid/`：民事法律需求、法律援助、司法可及、程序负担、代理缺口和权利救济。
- `domains/civic-participation-election-access/`：选民登记、投票可及、无障碍投票、选举标准、公共参与和制度反馈。
- `domains/migration-displacement-humanitarian-continuity/`：迁移、难民、流离失所、身份连续、医疗/教育/庇护/保护服务和人道协调。
- `domains/digital-inclusion-connectivity/`：互联网接入、设备可及、可负担性、数字技能、无障碍、人工帮助和数字公共服务入口。
- `domains/social-protection-benefits-delivery/`：公共福利、社会保护、资格、申请、续期、支付、申诉和行政负担。
- `domains/community-resource-navigation/`：211、社区资源目录、社会需求筛查、转介、闭环回访和本地服务导航。
- `domains/social-determinants-community-vulnerability/`：社会决定因素、社区脆弱性、环境正义、地方健康估计、食物可达和健康相关社会需求。
- `domains/public-service-design-accessibility/`：公共数字服务、表单、客户体验、无障碍、人工帮助、状态反馈和任务完成路径。
- `domains/emergency-alerts-communications/`：公共预警、WEA/EAS、NOAA Weather Radio、911/NG911、FirstNet 和危机通信入口。
- `domains/disaster-recovery-relief-continuity/`：灾后个人援助、恢复中心、临时安置、灾害贷款、救济服务和恢复连续性。
- `domains/financial-inclusion-payment-systems/`：账户、支付系统、汇款、数字金融服务、消费者金融保护和资源流动基础设施。
- `domains/workforce-employment-services/`：就业服务、劳动力发展、学徒制、职业信息、再就业支持和合理便利。
- `domains/household-emergency-preparedness-resilience/`：家庭应急计划、物资包、健康准备、备用通信、重要文件和特殊需求安排。
- `domains/media-information-literacy-public-libraries/`：媒体信息素养、公共图书馆、可信知识入口、数字技能和社区学习空间。
- `domains/health-workforce-capacity/`：健康劳动力供给、分布、训练、保留、负荷、技能组合和短缺风险。
- `domains/administrative-burden-procedural-friction/`：学习成本、心理成本、合规成本、证明负担、等待、续期、申诉和程序摩擦。
- `domains/community-health-workers-peer-support/`：社区健康工作者、同伴支持、导航员、可信中介、转介闭环和恢复支持。
- `domains/civic-data-open-government-transparency/`：开放数据、公共记录、FOIA、绩效数据、元数据、问责和公共反馈。
- `domains/education-access-lifelong-learning/`：教育可及、成人学习、再培训、基础技能、数字学习和技能迁移。
- `domains/research-infrastructure-open-science-translation/`：科研基础设施、开放科学、复现性、研究数据、资助、转化科学和知识扩散。
- `domains/standards-metrology-quality-infrastructure/`：标准、计量、校准、认证、合格评定、质量管理和互操作规范。
- `domains/cybersecurity-resilience-critical-services/`：网络安全、关键服务韧性、事件响应、备份恢复和数字风险治理。
- `domains/compute-data-center-ai-infrastructure/`：算力、数据中心、AI 基础设施、芯片、能源、水、网络、成本和接入治理。
- `domains/clinical-trials-regulatory-science-translation/`：临床试验、监管科学、真实世界证据、安全监测和医学转化证据路径。
- `domains/geospatial-navigation-location-infrastructure/`：地理空间数据、地址、地图、GNSS/GPS、地理编码、应急位置和位置互操作。
- `domains/weather-climate-observation-forecasting/`：天气气候观测、预报模型、气候服务、极端天气和早期预警风险输入。
- `domains/space-weather-geomagnetic-storm-resilience/`：空间天气、地磁暴、电网、卫星、通信、导航和时间同步韧性。
- `domains/planetary-defense-near-earth-object-risk/`：近地天体、撞击风险、行星防御、监测、预警、偏转和国际协调。
- `domains/volcanic-ashfall-geohazard-continuity/`：火山喷发、火山灰、空气、水、农业、航空、建筑和设备连续性。
- `domains/earthquake-seismic-risk-built-environment-continuity/`：地震危险性、抗震建筑、医院、道路、水电燃气、通信和恢复。
- `domains/tsunami-warning-coastal-evacuation-continuity/`：海啸监测、警报、沿海撤离、垂直避难、无障碍和灾后恢复。
- `domains/extreme-heat-cooling-public-health-continuity/`：极端高温、热健康、制冷可及、能源负担、住房、劳动暴露和城市热岛。
- `domains/noise-exposure-acoustic-environment-continuity/`：噪声暴露、声环境、听力保存、睡眠破坏、沟通负担和压力恢复。
- `domains/light-exposure-circadian-environment-continuity/`：光照暴露、昼夜节律、自然光、夜间光、轮班照明、光污染和睡眠时相。
- `domains/lead-heavy-metal-exposure-control/`：铅、汞、镉、砷、旧住房、饮水、土壤、粉尘、职业和产品暴露。
- `domains/radon-asbestos-indoor-hazard-continuity/`：氡、石棉、旧建筑、学校、工作场所和长期肺部风险。
- `domains/mold-dampness-indoor-biological-exposure/`：霉菌、潮湿、漏水、室内过敏原、灾后水损和住房质量。
- `domains/vector-borne-disease-environmental-control/`：蚊媒、蜱媒、病媒控制、气候水文、动物宿主、住房环境和公共卫生响应。
- `domains/advance-care-planning-medical-decision-continuity/`：预先医疗照护计划、advance directives、医疗代理人、治疗目标和失能时医疗偏好传递。
- `domains/supported-decision-making-guardianship-rights/`：支持性决策、监护、保佐、能力变化、最低限制替代和权利监督。
- `domains/healthcare-personal-representative-hipaa-access-continuity/`：HIPAA personal representative、授权照护者、医疗记录访问、隐私边界和照护资料连续性。
- `domains/financial-fiduciary-power-of-attorney-continuity/`：financial power of attorney、受托义务、账单支付、资产管理、记录和防剥削。
- `domains/representative-payee-benefits-management-continuity/`：SSA representative payee、VA fiduciary、公共福利代管、报告义务和支付监督。
- `domains/trust-estate-affairs-succession-continuity/`：事务整理、受益人、trustee、executor、账户文件和失能/死亡边界交接。
- `domains/credit-consumer-reporting-access-continuity/`：信用报告、消费者报告、specialty reports、错误记录、争议更正、身份混淆和准入影响。
- `domains/tenant-screening-rental-access-continuity/`：租客报告、驱逐记录、租金历史、收入验证、租赁平台筛查和住房准入错误。
- `domains/background-check-record-screening-continuity/`：背景调查、犯罪记录、身份匹配、教育/执照核验、制裁名单、不利行动和记录准确性。
- `domains/employment-algorithmic-hiring-screening-continuity/`：AI 招聘、自动简历筛选、就业测评、视频面试评分、job matching 和反歧视边界。
- `domains/insurance-underwriting-algorithmic-risk-scoring-continuity/`：保险承保、风险评分、外部数据、费率、索赔自动化和模型治理。
- `domains/public-benefits-eligibility-automated-decision-continuity/`：公共福利资格、自动化 eligibility、数据匹配、续期、终止、申诉和人工复核。
- `domains/building-fire-life-safety-codes/`：建筑规范、消防规范、生命安全、疏散、烟雾报警、无障碍和韧性改造。
- `domains/manufacturing-repair-capacity/`：制造、维修、维护、备件、质量、本地生产和关键设备恢复能力。
- `domains/public-procurement-contracting-capacity/`：公共采购、合同、供应商管理、应急采购、透明度和交付验收。
- `domains/animal-health-zoonotic-interface-one-health/`：动物健康、兽医公共卫生、人兽共患病、食品动物、野生动物和 One Health 界面。
- `domains/public-health-laboratory-diagnostic-capacity/`：公共卫生实验室、诊断网络、检测确认、质量管理、实验室扩容和风险确认能力。
- `domains/blood-organ-tissue-biovigilance-transplantation/`：血液供应、输血安全、器官/组织捐献、移植体系、追踪和生物警戒。
- `domains/waste-management-hazardous-materials-continuity/`：固体废弃物、医疗废物、危险废物、处理处置、服务连续性和环境暴露边界。
- `domains/radiation-nuclear-safety-protection/`：电离辐射防护、核安全、辐射监测、放射性材料风险和辐射应急治理。
- `domains/chemical-safety-poison-control-toxicology/`：化学品安全、毒性暴露、毒物中心、毒理证据、暴露监测和风险沟通。
- `domains/critical-minerals-materials-resilience/`：关键矿物、战略材料、加工依赖、替代回收和未来技术物质输入韧性。
- `domains/air-quality-ventilation-exposure-control/`：室内外空气污染、通风、过滤、气溶胶、烟雾和空气暴露治理。
- `domains/food-safety-contamination-control/`：食源性病原体、毒素、过敏原、检查、追溯、召回和暴发治理。
- `domains/occupational-exposure-industrial-hygiene/`：工作场所化学、物理、生物、粉尘、噪声、热、辐射和皮肤暴露控制。
- `domains/medical-device-equipment-safety-maintenance/`：医疗设备生命周期、不良事件、UDI、召回、维护、网络安全和可用性。
- `domains/sterilization-disinfection-infection-control/`：清洁、消毒、灭菌、再处理、环境感染控制和医疗照护相关感染预防。
- `domains/built-environment-accessibility-universal-design/`：物理空间可达、路径连续、公共设施、通用设计和环境参与条件。
- `domains/clinical-laboratory-diagnostic-quality/`：临床实验室质量、检测准确性、能力验证、诊断管理和临床效用。
- `domains/pharmacovigilance-drug-safety-monitoring/`：不良事件报告、真实世界安全信号、标签更新、用药错误和风险沟通。
- `domains/pharmaceutical-quality-supply-integrity/`：药品制造质量、GMP、质量缺陷、污染、假劣药、短缺、冷链和追溯。
- `domains/emergency-medical-services-prehospital-care/`：EMS、调度、响应时间、院前照护、转运和时间关键急性响应。
- `domains/surgical-anesthesia-perioperative-safety/`：手术安全、麻醉安全、团队检查、围手术期并发症预防和质量改进。
- `domains/road-traffic-injury-prevention-safe-mobility/`：道路交通伤害、安全系统、速度管理、车辆安全、交通数据和安全移动。
- `domains/rural-health-access-geographic-equity/`：农村健康可及、地理距离、服务密度、宽带、交通、卫生人力和农村公平。
- `domains/homelessness-unsheltered-health-continuity/`：无家可归、露宿、庇护、外展、住房服务、卫生、安全和健康连续性。
- `domains/correctional-health-reentry-continuity/`：羁押健康、释放转介、药物连续性、身份、住房、福利和重返社会。
- `domains/disability-services-independent-living/`：独立生活、HCBS、个人协助、合理便利、辅助技术、无障碍和社区融合。
- `domains/dementia-cognitive-decline-care-continuity/`：痴呆、认知衰退、照护计划、照护者负担、尊严、安全和服务导航。
- `domains/chronic-infectious-disease-care-continuity/`：HIV、结核、病毒性肝炎、治疗连续性、耐药、隐私、去污名和公共卫生随访。
- `domains/suicide-crisis-response-continuity/`：自杀预防、危机热线、移动危机响应、急诊衔接、随访和恢复支持。
- `domains/substance-use-treatment-recovery-continuity/`：物质使用障碍治疗、恢复支持、同伴支持、过量预防、减害治理和服务连续性。
- `domains/elder-justice-adult-protective-services/`：老年虐待、成人保护、财务剥削、照护忽视、长期照护监察和保护转介。
- `domains/child-protection-family-safety/`：儿童虐待忽视、ACEs、儿童福利、家庭支持、创伤知情服务和制度伤害风险。
- `domains/fraud-scams-consumer-protection/`：诈骗识别、身份盗用恢复、投诉举报、消费者保护和反受害者归因风险沟通。
- `domains/online-safety-digital-harm-prevention/`：网络霸凌、在线骚扰、数字虐待、儿童在线保护、平台求助和数字伤害恢复。
- `domains/rare-disease-diagnostic-odyssey-care-coordination/`：罕见病、未确诊疾病、诊断漫游、专家网络、患者登记和孤儿药路径。
- `domains/multimorbidity-polypharmacy-care-coordination/`：多病共存、多重用药、多专科冲突、药物重整、治疗负担和复杂照护计划。
- `domains/care-transitions-discharge-continuity/`：出院计划、照护转移、交接、用药重整、随访、再入院和跨机构责任断点。
- `domains/home-health-hospice-palliative-care-continuity/`：居家医疗、缓和医疗、安宁疗护、严重疾病、症状负担、家庭照护和目标照护。
- `domains/medical-interpreter-cultural-mediation/`：医疗解释、语言协助、CLAS、LEP、文化中介、知情同意理解和临床沟通安全。
- `domains/patient-advocacy-shared-decision-making/`：患者倡导、共同决策、决策辅助、主体偏好、治疗负担、知情同意和未来选择权。
- `domains/life-logging-personal-archives-continuity/`：生命日志、个人数字档案、元数据、备份、迁移和长期可读性。
- `domains/digital-legacy-data-succession/`：数字遗产、账号继承、数据授权、受托访问、失能代理和资料交接。
- `domains/wearables-continuous-sensing-personal-informatics/`：可穿戴、连续监测、个人信息学、自我追踪、远程数据采集和反馈闭环。
- `domains/personal-knowledge-management-cognitive-offloading/`：个人知识管理、外部记忆、认知卸载、检索、知识库、AI 助手和项目上下文恢复。
- `domains/brain-computer-interface-neurotechnology-governance/`：脑机接口、神经记录、刺激、解码、神经数据、设备安全和神经伦理治理。
- `domains/robotics-embodied-assistance-care-automation/`：机器人、具身辅助、外骨骼、家庭辅助、康复机器人和照护自动化。
- `domains/armed-conflict-civilian-protection-ihl/`：武装冲突、平民保护、国际人道法、人道准入、医疗中立和冲突服务断点。
- `domains/peacebuilding-conflict-prevention-social-cohesion/`：和平建设、冲突预防、社会凝聚、调解、制度信任和脆弱性。
- `domains/continuity-of-government-public-administration-resilience/`：政府连续性、公共行政韧性、基本职能、授权代理、记录、支付和公共服务恢复。
- `domains/telecommunications-network-resilience-continuity/`：电信网络、应急通信、宽带、移动网络、冗余、备电和恢复时间。
- `domains/macroeconomic-monetary-fiscal-stability/`：通胀、就业、利率、财政空间、公共债务、金融稳定和基本成本。
- `domains/anti-corruption-public-integrity-accountability/`：反腐败、公共廉洁、透明、审计、利益冲突、采购廉洁和问责。
- `domains/agricultural-production-food-system-resilience/`：农业生产、作物畜牧、灌溉、种子、肥料、劳动力和气候适应。
- `domains/soil-health-land-degradation-drought-resilience/`：土壤健康、土地退化、侵蚀、盐渍化、荒漠化、旱灾和土地恢复。
- `domains/water-resources-hydrology-flood-drought-management/`：水资源、水文观测、流域、地下水、水库、洪水、干旱和水安全。
- `domains/biodiversity-ecosystem-services-resilience/`：生物多样性、生态系统服务、授粉、过滤、蓄水、降温和生态恢复。
- `domains/wildfire-landscape-fire-resilience/`：野火、火灾天气、景观燃料、荒野-城市交界、烟雾、疏散和恢复。
- `domains/freight-logistics-port-cold-chain-continuity/`：货运、港口、仓储、冷链、运输节点、关键物资配送和最后一公里。
- `domains/coastal-marine-resilience-blue-economy-continuity/`：海岸带、海平面、风暴潮、侵蚀、海洋生态、海岸社区和蓝色经济连续性。
- `domains/fisheries-aquatic-food-systems-continuity/`：捕捞渔业、水产养殖、水产品营养、渔业治理、渔民生计和水生食物系统连续性。
- `domains/dams-levees-flood-control-infrastructure-safety/`：水坝、堤防、防洪墙、闸门、泵站、排涝系统、检查维护和工程失效风险。
- `domains/public-works-civil-infrastructure-asset-management/`：道路、桥梁、隧道、排水、公共设施、资产登记、状态评估和维护优先级。
- `domains/urban-planning-land-use-zoning-resilience/`：城市规划、土地使用、分区、密度、服务布局、公共空间、风险避让和空间公平。
- `domains/green-blue-infrastructure-urban-nature-cooling/`：城市树冠、绿地、水体、湿地、雨洪自然基设施、热岛缓解和恢复空间。
- `domains/electric-grid-reliability-resilience-continuity/`：电网可靠性、资源充足性、输配电资产、停电恢复、关键负荷和韧性投资。
- `domains/water-wastewater-utility-service-continuity/`：饮用水、污水处理、管网、泵站、水质监测、应急供水和服务恢复。
- `domains/fuel-thermal-energy-service-continuity/`：取暖燃料、燃气、液体燃料、区域能源、热泵、备用燃料和热服务恢复。
- `domains/public-transit-service-operations-continuity/`：公交、轨道、轮渡、paratransit、班次可靠性、运营人力、资产状态和服务恢复。
- `domains/critical-infrastructure-lifeline-interdependency-resilience/`：能源、水务、通信、交通、医疗、食品、金融和政府生命线互依赖。
- `domains/utility-affordability-shutoff-protection-continuity/`：公用事业账单负担、欠费、援助入口、分期安排、断供保护和消费者申诉。
- `domains/insurance-risk-transfer/`：健康、失业、工伤、残障、灾害、存款、养老金等风险转移和风险池。
- `domains/childcare-family-continuity/`：托育可及、托育费用、照护质量、早期儿童发展、父母工作连续性和家庭压力。
- `domains/emergency-preparedness-response/`：灾害准备、预警、应急通信、急救医疗、安置、公共卫生应急和灾后恢复。
- `domains/personal-safety-violence-prevention/`：人身安全、暴力预防、求助入口、受害者服务、法律保护和创伤支持。
- `domains/product-safety-recall-systems/`：消费品、食品、药品、医疗器械、车辆缺陷报告、召回通知、纠正措施和风险沟通。
- `domains/rehabilitation-functioning/`：康复、功能恢复、失能预防和社会参与能力。
- `domains/cancer-control/`：癌症预防、早筛、治疗、复发和长期肿瘤风险。
- `domains/immune-maintenance/`：免疫衰老、感染防御、慢性炎症、自身免疫和免疫监视。
- `domains/antimicrobial-resilience/`：抗微生物耐药、感染控制和现代医学抗感染底座。
- `domains/renal-hepatic-clearance/`：肾脏、肝脏、解毒、代谢、药物清除和系统稳态。
- `domains/neuro-continuity/`：大脑、记忆、意识、人格和主体身份连续性。
- `domains/sensory-continuity/`：视觉、听觉、平衡和感官反馈连续性。
- `domains/vision-eye-health-continuity/`：视力、眼健康、视觉损害、低视力支持、阅读、移动和视觉任务参与。
- `domains/hearing-auditory-communication-continuity/`：听力损失、听觉沟通、耳鸣、助听支持、声音警报和沟通疲劳。
- `domains/vestibular-balance-spatial-orientation/`：前庭、眩晕、平衡、空间定向、跌倒和移动信心。
- `domains/speech-language-communication-continuity/`：失语、构音障碍、言语运动障碍、沟通参与、同意表达和替代沟通。
- `domains/swallowing-dysphagia-aspiration-nutrition/`：吞咽障碍、误吸、窒息、营养水分入口、进食尊严和照护负担。
- `domains/smell-taste-chemosensory-continuity/`：嗅觉、味觉、化学感知、危险气味识别、食欲、营养和生活质量。
- `domains/peripheral-neuropathy-somatosensory-continuity/`：周围神经病变、触觉、痛觉、本体感觉、足部风险和身体边界反馈。
- `domains/future-waiting/`：去未来、压缩等待和低主观时间成本等待路径。
- `domains/disembodied-cns/`：去具身外部维持型中枢生命系统。
- `domains/memory-editing/`：记忆读写、人格连续性和主体权利保护。
- `domains/biostasis-cryopreservation/`：生物停滞、冷冻保存、休眠和等待未来修复。
- `domains/cognitive-augmentation/`：AI、外部记忆、学习系统、脑机接口和认知增强。
- `domains/ai-agency-safety/`：AI 代理、授权、工具调用、监督、审计和失效隔离。
- `domains/digital-identity-security/`：数字身份、账号、凭据、身份恢复、服务入口和数据可携带。
- `domains/mental-health-affective-stability/`：心理健康、情绪稳定、动机、成瘾、创伤和自杀风险。
- `domains/sleep-circadian-recovery/`：睡眠、昼夜节律、疲劳和恢复系统。
- `domains/assistive-technology-access/`：辅助技术、无障碍、义肢、助听、低视力辅助和环境适配。
- `domains/substance-exposure-control/`：烟草、酒精、成瘾性物质、有害暴露和行为风险控制。
- `domains/risk-engineering/`：事故、灾害、暴力、系统故障和尾部风险工程。
- `domains/planetary-health-environment/`：空气、水、气候、污染、生态系统和食物系统。
- `domains/resource-social-infra/`：食物、水、能源、住房、医疗、照护和社会支持。
- `domains/supply-chain-continuity/`：药品、能源、食物、设备、通信、芯片、物流和替代路径。
- `domains/synthetic-biology-biosecurity/`：合成生物学、生物安全、生物安保、双重用途风险和治理边界。
- `domains/space-extreme-habitation/`：空间飞行、极端环境、闭环生命支持、隔离、辐射和远程医疗。
- `domains/social-connection-relational-infra/`：社会连接、孤独、社会隔离、家庭照护网络、信任和社区关系。
- `domains/governance-rights/`：同意、退出、数据权、法律身份、AI 治理和研究伦理。
- `domains/pain-suffering-control/`：疼痛、痛苦、症状负担、姑息医学和可承受持续性。
- `domains/health-literacy-navigation/`：健康素养、医疗服务导航、可理解信息、共同决策和系统入口。
- `domains/language-access-plain-communication/`：清晰语言、语言服务、有限英语能力访问、CLAS、认知可访问性和关键服务材料理解。
- `domains/labor-rights-workplace-protection/`：劳动标准、工资工时、安全权利、反歧视、反报复、申诉入口和劳动组织治理。
- `domains/oral-health-continuity/`：口腔健康、牙齿、牙周、咀嚼、疼痛、感染、营养和沟通连续性。
- `domains/causal-inference-target-trial-emulation/`：因果推断、反事实、目标试验模拟、混杂和选择偏差审查。
- `domains/survival-analysis-healthspan-risk-modeling/`：生存分析、风险函数、健康寿命、竞争风险和有效时间终点建模。
- `domains/human-digital-twin-life-course-simulation/`：人类数字孪生、生命历程仿真、主体状态向量、状态转移和场景模拟。
- `domains/implementation-science-adherence-behavior-change/`：实施科学、依从性、技术采用、行为改变和真实世界效果。
- `domains/uncertainty-quantification-model-calibration/`：不确定性量化、模型校准、外部验证、漂移监测和报告边界。
- `domains/data-quality-missingness-representativeness/`：数据质量、缺失机制、代表性、测量误差和数据入口门禁。
- `domains/privacy-preserving-computation-federated-learning/`：隐私保护计算、差分隐私、联邦学习、协作分析、合成数据和隐私-效用边界。
- `domains/knowledge-graph-ontology-semantic-interoperability/`：知识图谱、本体、受控词表、语义互操作、FAIR 原则和跨域知识结构。
- `domains/model-cards-ai-audit-documentation/`：模型卡、数据集说明、系统卡、AI 审计文档、模型限制和用途边界。
- `domains/technology-foresight-horizon-scanning/`：技术预见、地平线扫描、弱信号、情景分析、成熟度和未来技术窗口。
- `domains/research-portfolio-prioritization-funding-governance/`：研究组合、优先级设定、资金治理、价值信息、阶段门和停止条件。
- `domains/intellectual-property-technology-transfer-access/`：知识产权、专利、许可、技术转移、公共资助成果和技术可及性。
- `domains/trustworthy-scientific-communication-peer-review/`：可信科研传播、同行评审、预印本、撤稿、勘误、引用语境和出版伦理。
- `domains/research-participant-consent-community-engagement/`：研究参与者同意、退出、再联系、社区参与、结果回馈和研究信任。
- `domains/biobanking-biospecimen-quality-chain-of-custody/`：生物样本库、预分析变量、样本质量、冷链、追踪、保管链和二次使用。
- `domains/longitudinal-cohort-retention-followup-infrastructure/`：纵向队列、长期随访、参与者留存、失访、事件确认和生命历程数据链接。
- `domains/registries-real-world-data-governance/`：患者登记、疾病登记、产品登记、真实世界数据、真实世界证据和登记质量治理。
- `domains/scientific-instrumentation-sensor-calibration-maintenance/`：科研仪器、传感器、校准、漂移、维护、参考材料和测量不确定性。
- `domains/nanomedicine-targeted-delivery-molecular-repair/`：纳米医学、靶向递送、纳米材料、释放控制、分子诊断和远期分子修复。
- `domains/ai-drug-discovery-protein-design/`：AI 药物发现、蛋白设计、分子生成、候选优化、预测模型和湿实验验证。
- `domains/epigenetic-editing-gene-regulation-therapeutics/`：表观遗传编辑、基因表达调控、染色质状态、可逆沉默和治疗性重编程。
- `domains/brain-preservation-connectomics-emulation/`：脑保存、连接组学、神经结构记录、全脑仿真和人格连续性证据边界。
- `domains/post-quantum-cryptography-long-term-data-security/`：后量子密码、长期保密、密码迁移、加密敏捷性和未来解密风险。
- `domains/safety-critical-software-formal-methods/`：安全关键软件、形式化方法、模型检查、证明、保证案例和高风险系统失效。
- `domains/long-term-digital-preservation-format-migration/`：长期数字保存、格式迁移、校验、元数据、备份、可读性和档案连续性。
- `domains/cerebrovascular-stroke-brain-perfusion-resilience/`：卒中、脑灌注、TIA、再灌注窗口、二级预防和脑血管韧性。
- `domains/traumatic-brain-injury-neurotrauma-recovery/`：TBI、脑震荡、重复头部冲击、神经创伤恢复和长期后遗症。
- `domains/delirium-acute-cognitive-failure-prevention/`：谵妄、ICU/住院急性认知失败、术后认知风险和可预防诱因。
- `domains/disorders-of-consciousness-coma-recovery/`：昏迷、无反应觉醒、最低意识状态、意识评估、康复和照护伦理。
- `domains/epilepsy-seizure-network-stability/`：癫痫、发作频率、脑网络兴奋性、治疗连续性和发作相关伤害。
- `domains/autonomic-nervous-system-homeostasis/`：自主神经、心率血压调节、体位耐受、出汗、消化排尿和压力恢复。
- `domains/migraine-headache-effective-time-burden/`：偏头痛、头痛障碍、感官敏感、认知雾、发作不可预测性和有效时间负担。
- `domains/measurement-feedback/`：主体状态测量、风险评分、预测模型和反馈闭环。

## 域关系

```text
Human Infra
├── Human Runtime Infrastructure
│   ├── 生理基础设施
│   ├── 认知基础设施
│   ├── 情绪与动机基础设施
│   ├── 环境与工具基础设施
│   └── 观测、反馈与恢复基础设施
├── Longevity Evidence
│   ├── 长寿干预
│   ├── 临床试验
│   ├── 药品安全
│   └── 公开证据账本
├── Nutrition And Metabolic Health
│   ├── 饮食质量 / 食物环境
│   ├── 体重 / 糖尿病 / 代谢健康
│   └── 能量供给、修复材料和慢病风险
├── Genomic Stability And DNA Repair
│   ├── DNA 损伤 / 修复系统
│   ├── 突变负荷 / 复制压力
│   └── 遗传信息完整性和癌前风险
├── Telomere Maintenance
│   ├── 端粒长度 / 端粒酶
│   ├── 复制衰老 / 组织更新
│   └── 修复能力和癌症风险边界
├── Cellular Reprogramming
│   ├── OSKM / OSK / iPS
│   ├── 部分重编程
│   ├── mRNA / 化学重编程
│   ├── AI 设计因子 / 表观遗传编辑
│   └── 年轻化、去分化、身份保持和肿瘤风险边界
├── Proteostasis And Autophagy
│   ├── 蛋白折叠 / 蛋白清除
│   ├── 自噬 / 溶酶体
│   └── 聚集负担和细胞质量控制
├── Mitochondrial Bioenergetics
│   ├── 线粒体功能 / ATP
│   ├── 氧化还原 / 线粒体质量控制
│   └── 疲劳、行动和恢复能力
├── Cellular Senescence Clearance
│   ├── senescence burden / SASP
│   ├── senolytics / senomorphics
│   └── 炎症、组织环境和癌症边界
├── Extracellular Matrix And Glycation
│   ├── 胶原 / 弹性 / 基质重塑
│   ├── 糖化终产物 / 交联 / 纤维化
│   └── 组织力学和结构性老化
├── Microbiome Ecology
│   ├── 宿主-微生物生态
│   ├── 代谢物 / 免疫互作
│   └── 菌群失调、感染抵抗和药物反应
├── Stem Cell Reserve And Renewal
│   ├── 干细胞储备 / 生态位
│   ├── 内源性组织更新
│   └── 再生能力和肿瘤风险
├── Regenerative Medicine
│   ├── 干细胞 / 组织工程
│   ├── 器官再生 / 器官替代
│   └── 长期整合与功能恢复
├── Gastrointestinal Barrier And Absorption
│   ├── 消化 / 吸收 / 胃肠动力
│   ├── 肠道屏障 / 黏膜免疫
│   └── 营养进入、药物吸收和水分损失
├── Respiratory Oxygenation
│   ├── 肺 / 气道 / 肺泡
│   ├── 通气 / 氧合 / 二氧化碳排出
│   └── 慢性肺病、缺氧和呼吸失败
├── Blood Oxygen And Hemostasis
│   ├── 红细胞 / 血红蛋白 / 氧气运输
│   ├── 血小板 / 凝血 / 止血
│   └── 贫血、出血、血栓和血液安全
├── Endocrine Hormonal Regulation
│   ├── 甲状腺 / 胰岛 / 肾上腺 / 性腺
│   ├── 激素轴 / 反馈环
│   └── 代谢、压力、骨骼、情绪和跨器官稳态
├── Lymphatic And Glymphatic Clearance
│   ├── 淋巴管 / 淋巴结 / 组织液
│   ├── 脑膜淋巴 / glymphatic clearance
│   └── 免疫运输、水肿和脑废物清除
├── Fluid Electrolyte Acid Base Homeostasis
│   ├── 水分 / 电解质 / 渗透压
│   ├── 酸碱平衡 / 内环境
│   └── 神经、肌肉、心律和药物安全
├── Thermal Homeostasis And Resilience
│   ├── 体温调节 / 散热 / 出汗
│   ├── 热暴露 / 寒冷暴露
│   └── 温度极端与急性失稳风险
├── Physical Activity And Mobility
│   ├── 身体活动 / 久坐
│   ├── 心肺适能 / 力量 / 平衡
│   └── 移动能力和行动密度
├── Cardiovascular Resilience
│   ├── 血压 / 血脂 / 血管
│   ├── 心梗 / 卒中 / 心衰
│   └── 循环系统风险函数
├── Musculoskeletal Integrity
│   ├── 肌肉 / 骨骼 / 关节
│   ├── 跌倒 / 骨折 / 肌少症
│   └── 行动承载结构
├── Skin Barrier And Wound Healing
│   ├── 皮肤屏障 / 伤口愈合
│   ├── 慢性伤口 / 压力损伤
│   └── 感染入口、热调节和照护负担
├── Urogenital Continuity
│   ├── 尿控 / 尿路 / 盆底
│   ├── 泌尿感染 / 性功能
│   └── 睡眠、尊严、照护和社会参与
├── Reproductive Fertility Continuity
│   ├── 生育力 / 配子质量 / 生殖衰老
│   ├── 妊娠风险 / 生殖自主性
│   └── 未来选择权和长期计划
├── Attention Executive Control
│   ├── 注意力 / 工作记忆 / 执行功能
│   ├── 抑制控制 / 任务切换 / 冲动控制
│   └── 有效行动密度和分心风险
├── Learning Skill Acquisition
│   ├── 学习科学 / 练习反馈
│   ├── 技能迁移 / 再训练
│   └── 能力复利和技术采用能力
├── Education Access Lifelong Learning
│   ├── 基础教育 / 成人学习 / 继续教育
│   ├── 再培训 / 数字学习 / 基础技能
│   └── 学习机会、认证和技能迁移
├── Time Allocation And Effective Time
│   ├── 时间使用 / 时间贫困
│   ├── 行政负担 / 等待成本 / 任务摩擦
│   └── 可支配时间、恢复时间和主观时间质量
├── Financial Resilience And Access
│   ├── 收入 / 储蓄 / 债务 / 保险
│   ├── 医疗支付能力 / 财务冲击
│   └── 资源入口和经济缓冲
├── Occupational Work Design
│   ├── 职业安全 / 工作组织 / 人体工学
│   ├── 工时 / 暴露 / 压力 / 技能转型
│   └── 工作可持续性和恢复边界
├── Information Integrity And Trust
│   ├── 信息可信度 / 证据质量
│   ├── 误导信息 / AI 生成内容 / 平台传播
│   └── 判断环境和信任链
├── Food Security And Nutrition Access
│   ├── 食物可得 / 可负担 / 食品安全
│   ├── 营养输入 / 价格冲击
│   └── 食物系统连续性
├── Water Sanitation Hygiene Continuity
│   ├── 安全饮用水 / 卫生设施
│   ├── 洗手 / 污水处理 / WASH 覆盖
│   └── 感染控制、尊严和灾害连续性
├── Energy Access And Resilience
│   ├── 电力 / 清洁烹饪
│   ├── 温控 / 通信供能 / 医疗设备供电
│   └── 能源负担、停电和韧性
├── Healthcare Access Continuity
│   ├── 初级卫生保健 / 急诊 / 预防
│   ├── 转诊 / 随访 / 连续照护
│   └── 医疗可及、费用、质量和服务断点
├── Medicine Access Treatment Continuity
│   ├── 基本药物 / 药品短缺 / 标签信息
│   ├── 覆盖 / 费用 / 药房可及
│   └── 治疗执行、用药安全和供应连续性
├── Patient Data Interoperability
│   ├── 健康记录访问 / 数据可携带
│   ├── USCDI / TEFCA / FHIR / Blue Button
│   └── 授权共享、照护交接和患者复核
├── Telehealth Remote Monitoring Access
│   ├── 远程问诊 / 远程患者监测
│   ├── 居家设备 / 覆盖规则 / 数据回传
│   └── 距离、行动限制和慢病随访断点
├── Health Data Privacy Governance
│   ├── 隐私 / 同意 / 撤回 / 安全
│   ├── 基因与健康数据共享 / 信息阻断边界
│   └── 数据可用性、主体权利和信任基础设施
├── Functioning Quality Of Life Outcomes
│   ├── 功能状态 / 生活质量 / 症状负担
│   ├── 患者报告结局 / 主体体验
│   └── 有效时间和干预真实价值
├── Health Economics Value Assessment
│   ├── 疾病负担 / 成本效果 / HTA
│   ├── QALY / DALY / 预算影响 / 公平
│   └── 稀缺资源如何转化为主体持续性收益
├── Immunization Public Health Surveillance
│   ├── 免疫计划 / 传染病监测
│   ├── 感染防控 / AMR / One Health / 废水监测
│   └── 群体风险屏障和公共卫生预警
├── Maternal Newborn Child Development
│   ├── 孕产健康 / 新生儿健康 / 儿童健康
│   ├── 生长标准 / 早期发展 / 养育照护
│   └── 早期生命条件和长期能力形成
├── Patient Safety Organizational Learning
│   ├── 患者安全 / 事件报告
│   ├── TeamSTEPPS / CUSP / RCA2 / 安全文化
│   └── 医疗组织学习和可避免伤害降低
├── Caregiving And Long-Term Care
│   ├── 家庭照护 / 长期照护
│   ├── 居家社区支持 / 照护协调
│   └── 照护者负担、失能支持和尊严边界
├── Housing And Built Environment Stability
│   ├── 住房稳定 / 住房质量
│   ├── 室内环境 / 无障碍 / 社区资源
│   └── 恢复空间、照护可行性和建成环境健康
├── Transportation Access And Mobility
│   ├── 公共交通 / 无障碍交通
│   ├── 医疗交通 / 出行时间 / 交通成本
│   └── 外部资源可达性和服务连接
├── Legal Identity And Civil Registration
│   ├── 法律身份 / 出生登记 / 民事登记
│   ├── 生命统计 / 身份文件 / 服务资格
│   └── 制度承认、权利入口和身份连续性
├── Access To Justice And Legal Aid
│   ├── 民事法律需求 / 法律援助
│   ├── 程序负担 / 代理缺口 / 申诉执行
│   └── 权利救济和制度恢复路径
├── Civic Participation And Election Access
│   ├── 选民登记 / 投票可及 / 无障碍投票
│   ├── 选举标准 / 审计 / 信任
│   └── 公共参与和制度反馈
├── Migration Displacement And Humanitarian Continuity
│   ├── 迁移 / 难民 / 国内流离失所
│   ├── 身份 / 医疗 / 教育 / 庇护 / 保护
│   └── 跨地点、跨制度和人道服务连续性
├── Digital Inclusion And Connectivity
│   ├── 互联网接入 / 设备 / 数字技能
│   ├── 可负担性 / 无障碍 / 人工帮助
│   └── 数字公共服务入口
├── Social Protection And Benefits Delivery
│   ├── 公共福利 / 社会保护
│   ├── 资格 / 申请 / 续期 / 支付 / 申诉
│   └── 行政负担、人工帮助和制度性缓冲
├── Community Resource Navigation
│   ├── 211 / 资源目录 / 社会需求筛查
│   ├── 转介 / 闭环回访 / 人工协助
│   └── 本地服务发现、匹配和确认到达
├── Social Determinants And Community Vulnerability
│   ├── SDOH / 社区脆弱性 / 环境正义
│   ├── 地方健康估计 / 食物可达 / 社会需求
│   └── 上游风险分布和结构性恢复条件
├── Public Service Design And Accessibility
│   ├── 公共数字服务 / 表单 / 客户体验
│   ├── 无障碍 / 人工帮助 / 状态反馈
│   └── 名义权利到可完成任务的接口
├── Emergency Alerts And Communications
│   ├── IPAWS / WEA / EAS / NOAA Weather Radio
│   ├── 911 / NG911 / FirstNet
│   └── 危机警报、求助入口和响应通信
├── Disaster Recovery Relief Continuity
│   ├── 个人援助 / 恢复中心 / 临时安置
│   ├── 灾害贷款 / 救济导航 / 恢复时间
│   └── 灾后资源、住房、文件和家庭连续性
├── Financial Inclusion And Payment Systems
│   ├── 账户 / 支付 / 汇款
│   ├── 数字金融服务 / 消费者保护
│   └── 收入、福利、救济和交易流通入口
├── Workforce Employment Services
│   ├── 就业服务 / WIOA / 学徒制
│   ├── 职业信息 / 再就业 / 合理便利
│   └── 技能到收入、角色和任务入口的转化
├── Household Emergency Preparedness Resilience
│   ├── 家庭计划 / 物资包 / 健康准备
│   ├── 备用通信 / 重要文件 / 特殊需求
│   └── 公共救援抵达前的家庭韧性窗口
├── Media Information Literacy Public Libraries
│   ├── 媒体与信息素养 / 来源判断
│   ├── 公共图书馆 / 数字技能 / 社区学习
│   └── 判断、学习和公共服务使用的知识入口
├── Health Workforce Capacity
│   ├── 卫生人力供给 / 分布 / 培训
│   ├── 保留 / 负荷 / 技能组合
│   └── 医学技术转化为真实照护的容量约束
├── Administrative Burden Procedural Friction
│   ├── 学习成本 / 心理成本 / 合规成本
│   ├── 证明 / 等待 / 续期 / 申诉
│   └── 名义权利穿过制度流程的摩擦成本
├── Community Health Workers Peer Support
│   ├── CHW / peer support / 导航员
│   ├── 信任 / 文化适配 / 转介闭环
│   └── 医疗、公共卫生和社会服务进入日常生活的关系接口
├── Civic Data Open Government Transparency
│   ├── 开放数据 / 公共记录 / FOIA
│   ├── 绩效数据 / 元数据 / 问责反馈
│   └── 公共系统可观察、可审查和可反馈的治理接口
├── Research Infrastructure Open Science Translation
│   ├── 科研基础设施 / 开放科学 / 复现性
│   ├── 研究数据 / 资助 / 转化科学
│   └── 未来技术窗口生成、验证和扩散
├── Standards Metrology Quality Infrastructure
│   ├── 标准 / 计量 / 校准
│   ├── 认证 / 合格评定 / 质量管理
│   └── 可比较、可复现、可互操作的技术底座
├── Cybersecurity Resilience Critical Services
│   ├── 网络安全 / 事件响应 / 备份恢复
│   ├── 关键服务韧性 / 勒索软件风险
│   └── 数字服务连续性和攻击恢复
├── Compute Data Center AI Infrastructure
│   ├── 算力 / 数据中心 / AI 基础设施
│   ├── 芯片 / 能源 / 水 / 网络 / 成本
│   └── AI、模拟和自动化能力的物质底座
├── Clinical Trials Regulatory Science Translation
│   ├── 临床试验 / 监管科学 / 真实世界证据
│   ├── 终点 / 安全监测 / 批准路径
│   └── 医学发现进入可用干预的转化通道
├── Insurance And Risk Transfer
│   ├── 健康 / 失业 / 工伤 / 残障 / 灾害保险
│   ├── 存款保险 / 养老金担保
│   └── 风险池、理赔和保障缺口
├── Childcare And Family Continuity
│   ├── 托育可及 / 托育费用 / 照护质量
│   ├── 早期儿童发展 / 父母工作连续性
│   └── 家庭压力、儿童未来选择权和照护者有效时间
├── Emergency Preparedness And Response
│   ├── 灾害准备 / 预警 / 应急通信
│   ├── 急救医疗 / 安置 / 公共卫生应急
│   └── 尾部风险响应和灾后恢复
├── Personal Safety And Violence Prevention
│   ├── 暴力预防 / 求助入口 / 受害者服务
│   ├── 法律保护 / 医疗创伤支持 / 住房安全
│   └── 人身安全、尊严和恢复连续性
├── Product Safety And Recall Systems
│   ├── 缺陷报告 / 不良事件 / 投诉
│   ├── 召回通知 / 纠正措施 / 替代路径
│   └── 外部产品安全和伤害降低
├── Rehabilitation And Functioning
│   ├── 康复 / 功能恢复
│   ├── 失能预防 / 衰弱
│   └── 活动、自理、沟通和参与能力
├── Cancer Control
│   ├── 预防 / 早筛
│   ├── 治疗 / 复发
│   └── 肿瘤演化和长期风险
├── Immune Maintenance
│   ├── 免疫衰老
│   ├── 感染防御
│   ├── 慢性炎症
│   └── 免疫监视
├── Antimicrobial Resilience
│   ├── 耐药性 / 感染控制
│   ├── 抗感染药物有效性
│   └── 医疗安全底座
├── Renal And Hepatic Clearance
│   ├── 肾功能 / 肝功能
│   ├── 解毒 / 药物代谢 / 清除
│   └── 内环境稳定和治疗可用性
├── Future Waiting
│   ├── 度规红移固有时差分路径（黑洞等待室）
│   ├── 相对论时间膨胀等待
│   ├── 休眠 / 冬眠等待
│   └── 等待未来的主观时间成本
├── Disembodied CNS
│   ├── 人工生命支持
│   ├── 神经接口
│   ├── 外部控制器
│   ├── 传感器反馈
│   └── 主体连续性
├── Neuro Continuity
│   ├── 大脑保存 / 神经保护
│   ├── 认知退行防控
│   └── 意识、人格和身份连续
├── Sensory Continuity
│   ├── 视觉 / 听觉
│   ├── 前庭 / 触觉反馈
│   └── 感知、行动和沟通
├── Memory Editing
│   ├── 记忆痕迹读写
│   ├── 记忆删除、写入和重构的验证
│   ├── 人格连续性
│   └── 同意、退出和审计
├── Biostasis And Cryopreservation
│   ├── 冷冻保存
│   ├── 生物停滞
│   └── 未来修复依赖
├── Cognitive Augmentation
│   ├── AI 协作
│   ├── 外部记忆 / 知识系统
│   └── 学习、判断和行动放大
├── AI Agency Safety
│   ├── AI 代理 / 工具调用
│   ├── 授权 / 监督 / 审计
│   └── 越权、泄露和不可逆行动隔离
├── Digital Identity Security
│   ├── 数字身份 / 账号 / 凭据
│   ├── 认证 / 授权 / 恢复
│   └── 服务入口和身份连续性
├── Mental Health And Affective Stability
│   ├── 情绪稳定 / 动机
│   ├── 成瘾 / 创伤
│   └── 自伤、自杀和危机风险
├── Sleep Circadian And Recovery
│   ├── 睡眠质量
│   ├── 昼夜节律
│   └── 疲劳与恢复能力
├── Assistive Technology Access
│   ├── 助听 / 低视力辅助 / 轮椅 / 义肢
│   ├── 沟通辅助 / 认知辅助
│   └── 无障碍与环境适配
├── Substance Exposure Control
│   ├── 烟草 / 酒精
│   ├── 成瘾性物质 / 有害暴露
│   └── 自主性和风险函数
├── Risk Engineering
│   ├── 事故 / 灾害 / 暴力
│   ├── 预警 / 响应 / 恢复
│   └── 尾部风险
├── Planetary Health And Environment
│   ├── 空气 / 水 / 气候
│   ├── 污染 / 热风险
│   └── 生态系统和食物系统
├── Resource And Social Infrastructure
│   ├── 食物 / 水 / 能源 / 住房
│   ├── 医疗 / 照护 / 康复
│   └── 教育 / 就业 / 社会支持
├── Geospatial Navigation Location Infrastructure
│   ├── 地理空间数据 / 地址 / 地图
│   ├── GNSS/GPS / 地理编码 / 导航
│   └── 位置层、资源可达和应急定位
├── Weather Climate Observation Forecasting
│   ├── 观测系统 / 预报模型 / 气候服务
│   ├── 极端天气 / 早期预警输入
│   └── 外部环境风险窗口
├── Building Fire Life Safety Codes
│   ├── 建筑规范 / 消防规范 / 生命安全
│   ├── 疏散 / 烟雾报警 / 无障碍
│   └── 栖居空间和公共空间风险控制
├── Manufacturing Repair Capacity
│   ├── 制造 / 维修 / 维护
│   ├── 备件 / 质量 / 本地生产
│   └── 关键设备和基础设施恢复能力
├── Public Procurement Contracting Capacity
│   ├── 公共采购 / 合同管理
│   ├── 供应商 / 应急采购 / 透明度
│   └── 公共资源到服务交付的转化能力
├── Animal Health Zoonotic Interface One Health
│   ├── 动物健康 / 兽医公共卫生
│   ├── 人兽共患病 / 食品动物 / 野生动物
│   └── 人-动物-环境界面风险屏障
├── Public Health Laboratory Diagnostic Capacity
│   ├── 公共卫生实验室 / 诊断网络
│   ├── 检测确认 / 质量管理 / 实验室扩容
│   └── 不可见风险到可行动信号的确认层
├── Blood Organ Tissue Biovigilance Transplantation
│   ├── 血液供应 / 输血安全
│   ├── 器官与组织捐献 / 移植体系 / 生物警戒
│   └── 外部生物材料的安全供应、追踪和分配
├── Waste Management Hazardous Materials Continuity
│   ├── 固体废物 / 医疗废物 / 危险废物
│   ├── 收集 / 处理 / 处置 / 服务连续性
│   └── 残余物、污染和危险材料的反向风险治理
├── Radiation Nuclear Safety Protection
│   ├── 电离辐射防护 / 核安全
│   ├── 辐射监测 / 放射性材料 / 应急治理
│   └── 不可见高能暴露的测量、限制和响应
├── Chemical Safety Poison Control Toxicology
│   ├── 化学品安全 / 毒性暴露
│   ├── 毒物中心 / 毒理证据 / 风险沟通
│   └── 化学暴露的咨询、监测、监管和预防
├── Critical Minerals Materials Resilience
│   ├── 关键矿物 / 战略材料
│   ├── 加工依赖 / 替代 / 回收 / 供应韧性
│   └── AI、能源、医疗设备和制造的物质输入层
├── Supply Chain Continuity
│   ├── 药品 / 能源 / 食物 / 设备
│   ├── 通信 / 芯片 / 物流
│   └── 断供、替代和恢复时间
├── Synthetic Biology Biosecurity
│   ├── 合成生物学 / 生物安全
│   ├── 生物安保 / 双重用途
│   └── 高风险研究治理边界
├── Space Extreme Habitation
│   ├── 空间飞行 / 极端环境
│   ├── 辐射 / 微重力 / 隔离
│   └── 闭环生命支持和远程医疗
├── Social Connection And Relational Infrastructure
│   ├── 孤独 / 社会隔离
│   ├── 家庭 / 照护网络 / 社区信任
│   └── 关系连续性和求助能力
├── Governance And Rights
│   ├── 同意 / 退出 / 审计
│   ├── 数据权 / 法律身份
│   └── AI、神经和医学治理
├── Pain And Suffering Control
│   ├── 疼痛 / 症状负担
│   ├── 姑息医学 / 生活质量
│   └── 尊严、同意和可承受性
├── Health Literacy And Navigation
│   ├── 健康素养 / plain language
│   ├── 服务导航 / 共同决策
│   └── 医疗与社会资源入口
├── Language Access And Plain Communication
│   ├── 清晰语言 / 语言服务 / 有限英语能力访问
│   ├── CLAS / 认知可访问性 / 表单理解
│   └── 关键服务材料能否被读懂、听懂和执行
├── Labor Rights And Workplace Protection
│   ├── 劳动标准 / 工资工时 / 安全权利
│   ├── 反歧视 / 反报复 / 申诉入口
│   └── 工作是否支撑而不是侵蚀主体持续性
├── Oral Health Continuity
│   ├── 龋病 / 牙周 / 牙齿缺失
│   ├── 咀嚼 / 疼痛 / 感染
│   └── 营养、沟通和社会参与
├── Knowledge Governance And Technology Diffusion
│   ├── 隐私保护计算 / 联邦学习
│   ├── 知识图谱 / 本体 / 语义互操作
│   ├── 模型卡 / AI 审计文档
│   ├── 技术预见 / 地平线扫描
│   ├── 研究组合 / 资金治理
│   └── 知识产权 / 技术转移 / 可及性
├── Research Evidence Infrastructure
│   ├── 可信科研传播 / 同行评审 / 撤稿纠错
│   ├── 研究参与者同意 / 社区参与
│   ├── 生物样本库 / 样本质量 / 保管链
│   ├── 纵向队列 / 留存 / 随访
│   ├── 登记系统 / 真实世界数据治理
│   └── 科研仪器 / 传感器校准维护
└── Measurement And Feedback
    ├── 生物标志物 / 生物年龄
    ├── 风险评分 / 预测模型
    └── 反馈闭环
```

## 为什么拆分

旧 Biocat 只覆盖“长寿证据与健康干预”。它能回答某个干预有没有证据、效果多大、风险在哪里，但无法承载 Human Infra 的全部问题。

“永生”和“记忆编辑”也不应直接混入 Biocat，因为它们不是普通长寿干预证据页，而是远期高风险研究域：

- `disembodied-cns` 关注身体功能由外部系统代理后的生命支持、接口闭环和主体连续性。
- `memory-editing` 关注神经系统中记忆痕迹的读写、删除、重构、验证和伦理约束。
- `future-waiting` 关注通过物理或生物状态改变减少等待未来的主观时间成本，例如度规红移固有时差分路径（黑洞等待室）。
- `cellular-reprogramming` 关注细胞身份、表观遗传年龄、组织功能和重编程风险之间的机制关系。它不是普通“长寿干预条目”，而是细胞状态可重写范式的独立机制域。
- `genomic-stability-dna-repair`、`telomere-maintenance`、`proteostasis-autophagy`、`mitochondrial-bioenergetics`、`cellular-senescence-clearance`、`microbiome-ecology`、`stem-cell-reserve-renewal` 和 `renal-hepatic-clearance` 关注疾病出现之前的分子维护、生态维护和清除底座。
- `respiratory-oxygenation`、`endocrine-hormonal-regulation`、`blood-oxygen-hemostasis`、`skin-barrier-wound-healing`、`extracellular-matrix-glycation` 和 `lymphatic-glymphatic-clearance` 关注氧气、激素、血液、屏障、材料结构和清除网络这些跨器官维护条件。
- `gastrointestinal-barrier-absorption`、`fluid-electrolyte-acid-base-homeostasis`、`thermal-homeostasis-resilience`、`urogenital-continuity` 和 `reproductive-fertility-continuity` 关注营养入口、内部化学环境、温度边界、排泄/性功能尊严和生殖未来选择权。
- `attention-executive-control`、`learning-skill-acquisition` 和 `time-allocation-effective-time` 关注注意力、学习能力和有效时间这些把寿命转化为任务完成的主体代理资源。
- `financial-resilience-access`、`occupational-work-design` 和 `information-integrity-trust` 关注财务入口、工作环境和信息可信度这些决定主体能否获得资源、保持判断和持续行动的外部条件。
- `food-security-nutrition-access`、`water-sanitation-hygiene-continuity`、`energy-access-resilience`、`social-protection-benefits-delivery`、`financial-inclusion-payment-systems`、`insurance-risk-transfer` 和 `childcare-family-continuity` 关注基础生计、资源流动与风险分摊。它们不能只放在 `resource-social-infra` 中，因为食物、水卫生、能源、福利递送、金融支付入口、风险池和托育各自有独立证据、失败模式和伦理边界。
- `healthcare-access-continuity`、`caregiving-long-term-care`、`housing-built-environment-stability`、`transportation-access-mobility`、`legal-identity-civil-registration` 和 `emergency-preparedness-response` 关注服务接入与生活连续性。它们不能只放进 `resource-social-infra`，因为每个域都有独立证据来源、失败模式、伦理边界和公共系统接口。
- `access-to-justice-legal-aid`、`civic-participation-election-access`、`migration-displacement-humanitarian-continuity`、`digital-inclusion-connectivity`、`personal-safety-violence-prevention` 和 `product-safety-recall-systems` 关注制度参与、人道连续性与公共安全。它们不能只放进 `governance-rights`、`risk-engineering` 或 `supply-chain-continuity`，因为司法救济、公共决策参与、跨制度移动连续性、数字连接、人身安全和产品召回各自有独立机制、来源体系和禁止用途边界。
- `medicine-access-treatment-continuity`、`patient-data-interoperability`、`telehealth-remote-monitoring-access`、`community-resource-navigation`、`social-determinants-community-vulnerability`、`public-service-design-accessibility`、`language-access-plain-communication`、`labor-rights-workplace-protection` 和 `workforce-employment-services` 关注治疗执行、数据连续、远程照护、社区转介、上游结构性风险、公共服务完成、语言理解、劳动权利和就业入口。它们不能只放进 `healthcare-access-continuity`、`health-literacy-navigation`、`resource-social-infra`、`digital-inclusion-connectivity`、`occupational-work-design` 或 `learning-skill-acquisition`，因为药品、数据、远程设备、资源目录、社区脆弱性、公共服务设计、语言服务、劳动执行和就业服务各自有独立来源体系、失败模式和禁止用途边界。
- `emergency-alerts-communications` 和 `disaster-recovery-relief-continuity` 从 `emergency-preparedness-response` 中拆出，分别处理危机信息/求助入口和灾后恢复/救济连续性。它们不能只放进宽泛应急域，因为预警通信与灾后恢复各自有独立系统、官方来源、时效约束和禁止用途边界。
- `health-data-privacy-governance`、`functioning-quality-of-life-outcomes`、`health-economics-value-assessment`、`immunization-public-health-surveillance`、`maternal-newborn-child-development` 和 `patient-safety-organizational-learning` 关注健康数据权利、主体结局、公共价值、群体免疫屏障、早期生命能力形成和医疗组织学习。它们不能只放进 `patient-data-interoperability`、`measurement-feedback`、`financial-resilience-access`、`immune-maintenance`、`reproductive-fertility-continuity` 或 `risk-engineering`，因为隐私治理、结局评估、价值评估、公共卫生监测、母婴儿童发展和患者安全各自有独立机制、证据体系、失败模式和禁止用途边界。
- `household-emergency-preparedness-resilience`、`media-information-literacy-public-libraries`、`health-workforce-capacity`、`administrative-burden-procedural-friction`、`community-health-workers-peer-support` 和 `civic-data-open-government-transparency` 关注家庭准备、公共知识入口、卫生人力容量、制度程序成本、社区关系接口和公共系统可观测性。它们不能只放进 `emergency-preparedness-response`、`information-integrity-trust`、`healthcare-access-continuity`、`public-service-design-accessibility`、`community-resource-navigation` 或 `governance-rights`，因为家庭桥接窗口、信息素养和图书馆、人力供给、行政负担、社区中介和开放数据透明各自有独立来源体系、失败模式和禁止用途边界。
- `education-access-lifelong-learning`、`research-infrastructure-open-science-translation`、`standards-metrology-quality-infrastructure`、`cybersecurity-resilience-critical-services`、`compute-data-center-ai-infrastructure` 和 `clinical-trials-regulatory-science-translation` 关注教育机会、未来技术生成、可信测量、数字韧性、AI 算力底座和医学监管转化。它们不能只放进 `learning-skill-acquisition`、`longevity-evidence`、`measurement-feedback`、`digital-identity-security`、`cognitive-augmentation` 或 `healthcare-access-continuity`，因为教育系统、科研生态、标准质量基础设施、网络安全、算力资源和临床监管证据各自有独立来源体系、失败模式和禁止用途边界。
- `geospatial-navigation-location-infrastructure`、`weather-climate-observation-forecasting`、`building-fire-life-safety-codes`、`manufacturing-repair-capacity`、`public-procurement-contracting-capacity` 和 `animal-health-zoonotic-interface-one-health` 关注空间定位、外部风险预测、栖居生命安全、关键设备恢复、公共交付能力和动物-人类-环境界面。它们不能只放进 `transportation-access-mobility`、`emergency-alerts-communications`、`housing-built-environment-stability`、`supply-chain-continuity`、`public-service-design-accessibility` 或 `immunization-public-health-surveillance`，因为位置层、观测预报、建筑消防规范、制造维修、采购合同和 One Health 各自有独立来源体系、失败模式和禁止用途边界。
- `public-health-laboratory-diagnostic-capacity`、`blood-organ-tissue-biovigilance-transplantation`、`waste-management-hazardous-materials-continuity`、`radiation-nuclear-safety-protection`、`chemical-safety-poison-control-toxicology` 和 `critical-minerals-materials-resilience` 关注风险确认、外部生物材料安全、残余物治理、不可见高能暴露、化学毒理和未来技术物质输入。它们不能只放进 `immunization-public-health-surveillance`、`blood-oxygen-hemostasis`、`water-sanitation-hygiene-continuity`、`risk-engineering`、`substance-exposure-control` 或 `supply-chain-continuity`，因为实验室诊断、血液器官组织生物警戒、废弃物/危险材料、辐射核安全、化学毒理和关键材料韧性各自有独立来源体系、失败模式和禁止用途边界。
- `air-quality-ventilation-exposure-control`、`food-safety-contamination-control`、`occupational-exposure-industrial-hygiene`、`medical-device-equipment-safety-maintenance`、`sterilization-disinfection-infection-control` 和 `built-environment-accessibility-universal-design` 关注可呼吸环境、食品污染控制、工作暴露控制、医疗设备可靠性、感染控制屏障和物理空间可达性。它们不能只放进 `planetary-health-environment`、`food-security-nutrition-access`、`occupational-work-design`、`medicine-access-treatment-continuity`、`antimicrobial-resilience` 或 `assistive-technology-access`，因为空气治理、食品污染、工业卫生、医疗设备生命周期、灭菌消毒感染控制和建成环境无障碍各自有独立来源体系、失败模式和禁止用途边界。
- `clinical-laboratory-diagnostic-quality`、`pharmacovigilance-drug-safety-monitoring`、`pharmaceutical-quality-supply-integrity`、`emergency-medical-services-prehospital-care`、`surgical-anesthesia-perioperative-safety` 和 `road-traffic-injury-prevention-safe-mobility` 关注临床观测质量、真实世界药品安全、治疗物质质量、急性响应窗口、高风险修复通道和安全移动。它们不能只放进 `healthcare-access-continuity`、`medicine-access-treatment-continuity`、`public-health-laboratory-diagnostic-capacity`、`patient-safety-organizational-learning`、`transportation-access-mobility` 或 `risk-engineering`，因为临床检验、药物警戒、药品质量、院前急救、围手术期安全和道路交通伤害预防各自有独立来源体系、失败模式和禁止用途边界。
- `rural-health-access-geographic-equity`、`homelessness-unsheltered-health-continuity`、`correctional-health-reentry-continuity`、`disability-services-independent-living`、`dementia-cognitive-decline-care-continuity` 和 `chronic-infectious-disease-care-continuity` 关注农村地理排除、住所缺失、羁押重返、残障服务、认知衰退和慢性传染病长期照护这些结构性脆弱窗口。它们不能只放进 `healthcare-access-continuity`、`housing-built-environment-stability`、`governance-rights`、`assistive-technology-access`、`neuro-continuity` 或 `immunization-public-health-surveillance`，因为这些场景各自有独立服务断点、权利边界、污名风险、长期照护模型和禁止用途边界。
- `suicide-crisis-response-continuity`、`substance-use-treatment-recovery-continuity`、`elder-justice-adult-protective-services`、`child-protection-family-safety`、`fraud-scams-consumer-protection` 和 `online-safety-digital-harm-prevention` 关注急性自毁风险、成瘾恢复、老年/成人保护、儿童保护、诈骗消费者保护和在线伤害预防。它们不能只放进 `mental-health-affective-stability`、`substance-exposure-control`、`personal-safety-violence-prevention`、`digital-identity-security` 或 `information-integrity-trust`，因为这些危机场景各自有独立入口、转介链条、受害者保护边界、禁止输出内容和恢复连续性模型。
- `rare-disease-diagnostic-odyssey-care-coordination`、`multimorbidity-polypharmacy-care-coordination`、`care-transitions-discharge-continuity`、`home-health-hospice-palliative-care-continuity`、`medical-interpreter-cultural-mediation` 和 `patient-advocacy-shared-decision-making` 关注高复杂度照护导航、转移交接、严重疾病支持、临床沟通和主体参与决策。它们不能只放进 `healthcare-access-continuity`、`medicine-access-treatment-continuity`、`caregiving-long-term-care`、`health-literacy-navigation` 或 `language-access-plain-communication`，因为诊断漫游、治疗冲突、出院断点、临终/居家连续性、专业医疗解释和共同决策各自有独立来源体系、失败模式、伦理边界和禁止用途。
- `life-logging-personal-archives-continuity`、`digital-legacy-data-succession`、`wearables-continuous-sensing-personal-informatics`、`personal-knowledge-management-cognitive-offloading`、`brain-computer-interface-neurotechnology-governance` 和 `robotics-embodied-assistance-care-automation` 关注主体历史、权限、状态、知识、神经接口和物理行动能力如何被外部系统承载。它们不能只放进 `digital-identity-security`、`health-data-privacy-governance`、`measurement-feedback`、`cognitive-augmentation`、`assistive-technology-access` 或 `ai-agency-safety`，因为个人档案、数字继承、连续感知、认知卸载、神经接口和具身辅助各自有独立来源体系、失败模式、伦理边界和禁止用途。
- `armed-conflict-civilian-protection-ihl`、`peacebuilding-conflict-prevention-social-cohesion`、`continuity-of-government-public-administration-resilience`、`telecommunications-network-resilience-continuity`、`macroeconomic-monetary-fiscal-stability` 和 `anti-corruption-public-integrity-accountability` 关注战争、社会冲突、政府中断、通信失效、宏观失稳和腐败这些集体层条件如何同时击穿多个个人级持续性变量。它们不能只放进 `risk-engineering`、`governance-rights`、`emergency-preparedness-response`、`public-service-design-accessibility` 或 `information-integrity-trust`，因为平民保护、和平建设、公共行政连续性、通信网络韧性、宏观稳定和公共廉洁各自有独立证据体系、治理边界和禁止用途。
- `agricultural-production-food-system-resilience`、`soil-health-land-degradation-drought-resilience`、`water-resources-hydrology-flood-drought-management`、`biodiversity-ecosystem-services-resilience`、`wildfire-landscape-fire-resilience` 和 `freight-logistics-port-cold-chain-continuity` 关注农业生产、土壤土地、水文、生态系统服务、野火和物理物流这些资源进入个人生活之前的上游底座。它们不能只放进 `food-security-nutrition-access`、`planetary-health-environment`、`weather-climate-observation-forecasting`、`water-sanitation-hygiene-continuity`、`supply-chain-continuity` 或 `risk-engineering`，因为生产、土地、水文、生态服务、野火和物流节点各自有独立来源体系、失败模式和禁止用途。
- `coastal-marine-resilience-blue-economy-continuity`、`fisheries-aquatic-food-systems-continuity`、`dams-levees-flood-control-infrastructure-safety`、`public-works-civil-infrastructure-asset-management`、`urban-planning-land-use-zoning-resilience` 和 `green-blue-infrastructure-urban-nature-cooling` 关注海岸海洋、水生食物、防洪工程资产、公共工程资产、城市空间治理和城市自然基础设施。它们不能只放进 `water-resources-hydrology-flood-drought-management`、`biodiversity-ecosystem-services-resilience`、`freight-logistics-port-cold-chain-continuity`、`transportation-access-mobility`、`housing-built-environment-stability` 或 `planetary-health-environment`，因为海岸海洋、渔业、防洪工程、公共工程资产、土地使用和绿蓝设施各自有独立来源体系、失败模式和禁止用途。
- `electric-grid-reliability-resilience-continuity`、`water-wastewater-utility-service-continuity`、`fuel-thermal-energy-service-continuity`、`public-transit-service-operations-continuity`、`critical-infrastructure-lifeline-interdependency-resilience` 和 `utility-affordability-shutoff-protection-continuity` 关注电网、水务、热能、公共交通、生命线互依赖和公用事业可负担性这些日常服务底座。它们不能只放进 `energy-access-resilience`、`water-sanitation-hygiene-continuity`、`transportation-access-mobility`、`telecommunications-network-resilience-continuity`、`risk-engineering` 或 `financial-resilience-resource-access`，因为公用事业生命线既有工程连续性、运营连续性、互依赖级联和家庭层面断供失败，也有独立来源体系、监管边界和禁止用途。
- `gene-therapy-genome-editing-delivery-safety`、`biological-age-clocks-biomarker-validation`、`multiomics-personal-baseline-systems-biology`、`engineered-cell-therapy-regenerative-platforms`、`organoids-organ-on-chip-disease-models` 和 `xenotransplantation-bioengineered-organ-replacement` 关注遗传状态可改写、衰老状态可测量、多层组学可建模、治疗细胞可编程、人体相关模型可降低试错成本、器官失败可获得替换路径这些生物医学平台条件。它们不能只放进 `cellular-reprogramming`、`regenerative-medicine`、`clinical-trials-regulatory-science-translation`、`measurement-feedback` 或 `blood-organ-tissue-biovigilance-transplantation`，因为递送安全、年龄钟验证、多组学基线、工程细胞、类器官/组织芯片和异种/工程器官各自有独立变量、证据体系、监管边界和禁止用途。
- `causal-inference-target-trial-emulation`、`survival-analysis-healthspan-risk-modeling`、`human-digital-twin-life-course-simulation`、`implementation-science-adherence-behavior-change`、`uncertainty-quantification-model-calibration` 和 `data-quality-missingness-representativeness` 关注定量模型何以可能：干预效应如何识别、风险如何随时间表达、主体状态如何动态仿真、技术如何真实落地、模型如何校准、数据如何审查。它们不能只放进 `measurement-feedback`、`life-path-prediction-model-governance`、`clinical-trials-regulatory-science-translation` 或 `research-infrastructure-open-science-translation`，因为因果识别、生存结局、数字孪生、实施落地、不确定性校准和数据入口门禁各自有独立方法、失败模式和禁止用途。
- `privacy-preserving-computation-federated-learning`、`knowledge-graph-ontology-semantic-interoperability`、`model-cards-ai-audit-documentation`、`technology-foresight-horizon-scanning`、`research-portfolio-prioritization-funding-governance` 和 `intellectual-property-technology-transfer-access` 关注研究系统何以可信、可组合、可审计、可预警、可排序和可扩散。它们不能只放进 `health-data-privacy-governance`、`information-integrity-trust`、`research-infrastructure-open-science-translation`、`standards-metrology-quality-infrastructure` 或 `medicine-access-treatment-continuity`，因为隐私保护计算、语义知识结构、模型审计、未来技术扫描、研究组合治理和技术转移可及各自有独立机制、证据体系、失败模式和禁止用途。
- `trustworthy-scientific-communication-peer-review`、`research-participant-consent-community-engagement`、`biobanking-biospecimen-quality-chain-of-custody`、`longitudinal-cohort-retention-followup-infrastructure`、`registries-real-world-data-governance` 和 `scientific-instrumentation-sensor-calibration-maintenance` 关注研究结论进入 Human Infra 模型之前的证据基础设施。它们不能只放进 `research-infrastructure-open-science-translation`、`data-quality-missingness-representativeness`、`clinical-trials-regulatory-science-translation`、`standards-metrology-quality-infrastructure` 或 `measurement-feedback`，因为科研传播纠错、参与者同意、样本质量、长期随访、真实世界登记和仪器校准各自有独立机制、证据体系、失败模式和禁止用途。
- `nanomedicine-targeted-delivery-molecular-repair`、`ai-drug-discovery-protein-design`、`epigenetic-editing-gene-regulation-therapeutics`、`brain-preservation-connectomics-emulation`、`post-quantum-cryptography-long-term-data-security`、`safety-critical-software-formal-methods` 和 `long-term-digital-preservation-format-migration` 关注未来技术窗口从产生、筛选、递送、调控、信息保存、长期安全、可靠软件执行到长期可读的连续性条件。它们不能只放进 `longevity-evidence`、`gene-therapy-genome-editing-delivery-safety`、`neuro-continuity`、`digital-identity-security`、`cybersecurity-resilience-critical-services`、`research-infrastructure-open-science-translation` 或 `measurement-feedback`，因为分子递送、AI 分子设计、表观状态编辑、脑结构保存、密码迁移、形式化验证和数字保存各自有独立证据、失败模式、监管边界和禁止用途。
- `cerebrovascular-stroke-brain-perfusion-resilience`、`traumatic-brain-injury-neurotrauma-recovery`、`delirium-acute-cognitive-failure-prevention`、`disorders-of-consciousness-coma-recovery`、`epilepsy-seizure-network-stability`、`autonomic-nervous-system-homeostasis` 和 `migraine-headache-effective-time-burden` 关注急性脑灌注、脑外伤、谵妄、意识障碍、发作网络、自主调节和头痛失能如何中断主体连续性。它们不能只放进 `neuro-continuity`、`cardiovascular-resilience`、`risk-engineering`、`pain-suffering-control`、`dementia-cognitive-decline-care-continuity` 或 `measurement-feedback`，因为卒中、TBI、谵妄、意识障碍、癫痫、自主神经和偏头痛各自有独立变量、时间窗口、证据体系、失败模式和禁止用途边界。
- `vision-eye-health-continuity`、`hearing-auditory-communication-continuity`、`vestibular-balance-spatial-orientation`、`speech-language-communication-continuity`、`swallowing-dysphagia-aspiration-nutrition`、`smell-taste-chemosensory-continuity` 和 `peripheral-neuropathy-somatosensory-continuity` 关注视觉输入、听觉沟通、空间定向、主体表达、安全摄食、化学危险识别和身体边界反馈如何支撑主体行动。它们不能只放进 `sensory-continuity`、`assistive-technology-access`、`rehabilitation-functioning`、`oral-health-continuity`、`neuro-continuity` 或 `pain-suffering-control`，因为视觉、听力、前庭、言语语言、吞咽、嗅味觉和周围神经各自有独立机制、证据体系、失败模式和禁止用途边界。
- `space-weather-geomagnetic-storm-resilience`、`planetary-defense-near-earth-object-risk`、`volcanic-ashfall-geohazard-continuity`、`earthquake-seismic-risk-built-environment-continuity`、`tsunami-warning-coastal-evacuation-continuity` 和 `extreme-heat-cooling-public-health-continuity` 关注太阳活动、近地天体、火山灰、地震、海啸和极端高温如何从外部物理事件变成主体持续性风险。它们不能只放进 `weather-climate-observation-forecasting`、`risk-engineering`、`emergency-preparedness-response`、`critical-infrastructure-lifeline-interdependency-resilience` 或 `disaster-recovery-relief-continuity`，因为空间天气、行星防御、火山灰、地震、海啸和极端高温各自有独立监测体系、预警窗口、基础设施失效模式和禁止用途。
- `noise-exposure-acoustic-environment-continuity`、`light-exposure-circadian-environment-continuity`、`lead-heavy-metal-exposure-control`、`radon-asbestos-indoor-hazard-continuity`、`mold-dampness-indoor-biological-exposure` 和 `vector-borne-disease-environmental-control` 关注噪声、光照节律、重金属、建筑遗留危害、潮湿霉菌和病媒传播如何把日常环境变成慢性损耗条件。它们不能只放进 `air-quality-ventilation-exposure-control`、`occupational-exposure-industrial-hygiene`、`chemical-safety-poison-control-toxicology`、`housing-built-environment-stability`、`planetary-health-environment` 或 `immunization-public-health-surveillance`，因为这些暴露各自有独立观测方式、健康终点、空间分布、治理责任和禁止用途。
- `advance-care-planning-medical-decision-continuity`、`supported-decision-making-guardianship-rights`、`healthcare-personal-representative-hipaa-access-continuity`、`financial-fiduciary-power-of-attorney-continuity`、`representative-payee-benefits-management-continuity` 和 `trust-estate-affairs-succession-continuity` 关注主体失能、不能表达或死亡边界附近的意愿、权限、资源和责任如何不中断且不被滥用。它们不能只放进 `patient-advocacy-shared-decision-making`、`access-to-justice-legal-aid`、`digital-legacy-data-succession`、`financial-resilience-access`、`social-protection-benefits-delivery` 或 `elder-justice-adult-protective-services`，因为医疗代理、支持性决策、HIPAA 访问、财务受托、代表收款人和事务继承各自有独立角色、文件、监督机制、滥用风险和禁止用途。
- `credit-consumer-reporting-access-continuity`、`tenant-screening-rental-access-continuity`、`background-check-record-screening-continuity`、`employment-algorithmic-hiring-screening-continuity`、`insurance-underwriting-algorithmic-risk-scoring-continuity` 和 `public-benefits-eligibility-automated-decision-continuity` 关注报告、筛查、评分、背景记录和自动化资格判定如何在主体进入金融、住房、工作、保险和福利系统之前改变准入概率。它们不能只放进 `financial-inclusion-payment-systems`、`housing-built-environment-stability`、`labor-rights-workplace-protection`、`insurance-risk-transfer`、`social-protection-benefits-delivery` 或 `model-cards-ai-audit-documentation`，因为这些判定层各自有独立数据来源、错误模式、通知/不利行动、争议/更正、监管责任和禁止用途。
- `nutrition-metabolic-health`、`physical-activity-mobility`、`cardiovascular-resilience` 和 `musculoskeletal-integrity` 关注能量、行动、循环和承载结构这四类常规运行条件。
- `regenerative-medicine`、`cancer-control` 和 `immune-maintenance` 关注身体基底长期可维护性中的不同失败模式。
- `rehabilitation-functioning`、`assistive-technology-access` 和 `sensory-continuity` 关注主体存活之后是否仍能行动、沟通、感知和参与。
- `antimicrobial-resilience` 关注现代医学抗感染底座是否会被耐药性侵蚀。
- `neuro-continuity`、`cognitive-augmentation`、`memory-editing` 和 `disembodied-cns` 关注延续的是否仍是能够行动、记忆和选择的同一主体。
- `mental-health-affective-stability`、`sleep-circadian-recovery`、`pain-suffering-control` 和 `oral-health-continuity` 关注存在时间是否能转化为可承受、可恢复、可行动、可进食和可沟通的有效时间。
- `substance-exposure-control` 关注可避免暴露和成瘾如何同时侵蚀健康风险、资源预算和主体自主性。
- `biostasis-cryopreservation` 关注暂停损耗并等待未来修复，与 `future-waiting` 的时间差分路径互补。
- `risk-engineering`、`planetary-health-environment`、`weather-climate-observation-forecasting`、`resource-social-infra`、`social-determinants-community-vulnerability`、`public-service-design-accessibility`、`public-procurement-contracting-capacity`、`administrative-burden-procedural-friction`、`civic-data-open-government-transparency`、`emergency-alerts-communications`、`household-emergency-preparedness-resilience`、`disaster-recovery-relief-continuity`、`financial-inclusion-payment-systems`、`workforce-employment-services`、`education-access-lifelong-learning`、`health-workforce-capacity`、`community-health-workers-peer-support`、`media-information-literacy-public-libraries`、`social-connection-relational-infra`、`health-literacy-navigation` 和 `governance-rights` 关注主体不被外部风险、资源断裂、结构性脆弱性、服务不可达、采购交付失败、行政摩擦、系统不可观测、危机通信失败、家庭准备不足、灾后恢复失败、支付入口失败、就业入口失败、教育机会断裂、健康人力短缺、社区中介断裂、信息素养不足、环境退化、关系孤立、服务不可理解或制度控制截断。
- `digital-identity-security`、`ai-agency-safety`、`research-infrastructure-open-science-translation`、`standards-metrology-quality-infrastructure`、`cybersecurity-resilience-critical-services`、`compute-data-center-ai-infrastructure`、`geospatial-navigation-location-infrastructure`、`manufacturing-repair-capacity`、`clinical-trials-regulatory-science-translation`、`supply-chain-continuity`、`synthetic-biology-biosecurity`、`animal-health-zoonotic-interface-one-health` 和 `space-extreme-habitation` 关注外部技术底座是否会放大主体持续性，或反过来通过身份断线、代理越权、知识生成失败、标准失准、网络攻击、算力短缺、定位失效、制造维修不足、临床转化失败、断供、生物风险、动物-人类界面风险和极端环境失效截断主体。
- `causal-inference-target-trial-emulation`、`survival-analysis-healthspan-risk-modeling`、`human-digital-twin-life-course-simulation`、`implementation-science-adherence-behavior-change`、`uncertainty-quantification-model-calibration` 和 `data-quality-missingness-representativeness` 关注各域如何从资料、叙事和机制假设进入可审查的定量模型。
- `privacy-preserving-computation-federated-learning`、`knowledge-graph-ontology-semantic-interoperability`、`model-cards-ai-audit-documentation`、`technology-foresight-horizon-scanning`、`research-portfolio-prioritization-funding-governance` 和 `intellectual-property-technology-transfer-access` 关注各域如何从资料堆、模型输出和未来技术信号进入可治理、可追踪、可排序和可实际扩散的研究基础设施。
- `trustworthy-scientific-communication-peer-review`、`research-participant-consent-community-engagement`、`biobanking-biospecimen-quality-chain-of-custody`、`longitudinal-cohort-retention-followup-infrastructure`、`registries-real-world-data-governance` 和 `scientific-instrumentation-sensor-calibration-maintenance` 关注科研证据如何被发表纠错、主体授权、物质保存、长期观察、真实世界反馈和测量硬件校准所约束。
- `nanomedicine-targeted-delivery-molecular-repair`、`ai-drug-discovery-protein-design`、`epigenetic-editing-gene-regulation-therapeutics`、`brain-preservation-connectomics-emulation`、`post-quantum-cryptography-long-term-data-security`、`safety-critical-software-formal-methods` 和 `long-term-digital-preservation-format-migration` 关注未来技术如何从候选能力变成可到达、可验证、可保存、可安全运行和可长期复用的主体持续性条件。
- `cerebrovascular-stroke-brain-perfusion-resilience`、`traumatic-brain-injury-neurotrauma-recovery`、`delirium-acute-cognitive-failure-prevention`、`disorders-of-consciousness-coma-recovery`、`epilepsy-seizure-network-stability`、`autonomic-nervous-system-homeostasis` 和 `migraine-headache-effective-time-burden` 关注急性神经连续性与意识韧性，防止脑灌注、创伤、谵妄、意识边界、脑网络发作、自主调节和头痛负担把主体行动窗口切断。
- `vision-eye-health-continuity`、`hearing-auditory-communication-continuity`、`vestibular-balance-spatial-orientation`、`speech-language-communication-continuity`、`swallowing-dysphagia-aspiration-nutrition`、`smell-taste-chemosensory-continuity` 和 `peripheral-neuropathy-somatosensory-continuity` 关注感官、沟通与具身反馈连续性，防止视觉输入、听觉沟通、空间平衡、表达同意、安全进食、危险气味识别和身体边界反馈断裂。
- `space-weather-geomagnetic-storm-resilience`、`planetary-defense-near-earth-object-risk`、`volcanic-ashfall-geohazard-continuity`、`earthquake-seismic-risk-built-environment-continuity`、`tsunami-warning-coastal-evacuation-continuity` 和 `extreme-heat-cooling-public-health-continuity` 关注行星、地球物理与极端热风险连续性，防止电网/卫星/通信/定位扰动、天体撞击、火山灰、地震、海啸和高温把主体外部生存条件击穿。
- `noise-exposure-acoustic-environment-continuity`、`light-exposure-circadian-environment-continuity`、`lead-heavy-metal-exposure-control`、`radon-asbestos-indoor-hazard-continuity`、`mold-dampness-indoor-biological-exposure` 和 `vector-borne-disease-environmental-control` 关注慢性环境暴露与日常损耗条件，防止噪声、节律错配、神经毒性、建筑遗留危害、潮湿生物暴露和病媒传播持续削弱恢复、认知、呼吸、居住和公共卫生连续性。
- `advance-care-planning-medical-decision-continuity`、`supported-decision-making-guardianship-rights`、`healthcare-personal-representative-hipaa-access-continuity`、`financial-fiduciary-power-of-attorney-continuity`、`representative-payee-benefits-management-continuity` 和 `trust-estate-affairs-succession-continuity` 关注决策权、代理权与受托连续性，防止主体失能或不能表达后，医疗偏好、权利参与、医疗资料、财务任务、公共收入和长期事务被猜测、冻结、夺走或滥用。
- `credit-consumer-reporting-access-continuity`、`tenant-screening-rental-access-continuity`、`background-check-record-screening-continuity`、`employment-algorithmic-hiring-screening-continuity`、`insurance-underwriting-algorithmic-risk-scoring-continuity` 和 `public-benefits-eligibility-automated-decision-continuity` 关注算法化准入、筛查与资格连续性，防止报告错误、筛查黑箱、记录失配、算法招聘偏差、保险评分和福利自动终止把主体排除在关键资源系统之外。
- `measurement-feedback` 关注所有研究域如何被观测、建模、反馈和校正。

把它们拆开，能避免一个错误概念：用“长寿方法”统摄所有人类增强、生命延续和神经干预问题。

## 本轮迁移切片

- 根目录从 Biocat 改为 Human Infra。
- 旧 Biocat 文档、数据和脚本迁入 `domains/longevity-evidence/`。
- 四份最新资料改名归档到 `docs/source-notes/`。
- 新增 Human Infra 总理论、域地图、伦理边界和两个远期研究域 README。
- 新增 `domains/cellular-reprogramming/`，承载山中因子到部分重编程、化学重编程、AI 因子设计和表观遗传编辑的机制谱系。
- 新增研究域图谱和 10 个先验条件域骨架，全部只创建 README / AGENTS，不创建空数据或脚本目录。
- 新增第三十六波 6 个行星、地球物理与极端热风险连续性域骨架，覆盖空间天气地磁暴、行星防御近地天体、火山灰地质灾害、地震建成环境、海啸预警沿海撤离和极端高温制冷公共卫生。
- 新增第三十七波 6 个慢性环境暴露与日常损耗条件域骨架，覆盖噪声暴露声环境、光照昼夜节律、铅与重金属暴露、氡与石棉室内危害、霉菌潮湿室内生物暴露和病媒传播环境控制。
- 新增第三十八波 6 个决策权、代理权与受托连续性域骨架，覆盖预先医疗照护计划、支持性决策监护权利、医疗个人代表 HIPAA 访问、财务受托授权代理、代表收款人福利代管和事务信托遗产继承连续性。
- 新增第三十九波 6 个算法化准入、筛查与资格连续性域骨架，覆盖信用与消费者报告、租房筛查、背景记录筛查、算法招聘、保险算法评分和公共福利自动资格系统。
- 新增第二波 8 个研究域骨架，覆盖功能恢复、心理稳定、睡眠恢复、辅助技术、抗微生物韧性、环境底座、感官连续性和痛苦控制。
- 新增第三波 8 个研究域骨架，覆盖营养代谢、身体活动、心血管韧性、肌骨完整性、社会连接、物质暴露控制、健康素养导航和口腔健康连续性。
- 新增第四波 8 个研究域骨架，覆盖基因组稳定性、端粒维护、蛋白稳态、自噬、线粒体生物能量学、细胞衰老清除、微生物生态、干细胞储备和肝肾清除。
- 新增第五波 5 个外部技术风险域骨架，覆盖数字身份安全、AI 代理安全、供应链连续性、合成生物学与生物安全、空间与极端栖居。
- 新增第六波 6 个生理与结构维护域骨架，覆盖呼吸氧合、内分泌激素调节、血液氧运与止血、皮肤屏障与伤口愈合、细胞外基质与糖化、淋巴与脑淋巴清除。
- 新增第七波 5 个基础稳态与未来选择权域骨架，覆盖消化屏障与吸收、体液电解质酸碱稳态、热稳态、泌尿生殖连续性、生殖与生育连续性。
- 新增第八波 6 个主体代理与任务资源域骨架，覆盖注意力与执行控制、学习与技能获得、时间分配与有效时间、财务韧性、职业与工作设计、信息完整性与信任。
- 新增第九波 6 个服务接入与生活连续性域骨架，覆盖医疗服务连续性、照护与长期照护、住房与建成环境、交通接入、法律身份与民事登记、应急准备与响应。
- 新增第十波 6 个基础生计与风险分摊域骨架，覆盖食物安全与营养可及、水卫生连续性、能源可及与韧性、社会保护与福利递送、保险与风险转移、托育与家庭连续性。
- 新增第十一波 6 个制度参与、人道连续性与公共安全域骨架，覆盖司法可及与法律援助、公民参与与选举接入、迁移流离失所与人道连续性、数字包容与连接、人身安全与暴力预防、产品安全与召回系统。
- 新增第十二波 6 个治疗、服务理解与劳动保护域骨架，覆盖药品与治疗连续性、患者数据互操作、远程医疗与居家监测、社区资源导航、语言可达与清晰沟通、劳动权利与工作场所保护。
- 新增第十三波 6 个数据治理、结局评估与公共卫生安全域骨架，覆盖健康数据隐私治理、功能与生活质量结局、健康经济与价值评估、免疫与公共卫生监测、母婴儿童早期生命、患者安全与组织学习。
- 新增第十四波 6 个公共服务、应急、金融和就业相关域骨架，覆盖社会决定因素与社区脆弱性、公共服务设计与可达性、应急预警与通信、灾后恢复与救济连续性、金融包容与支付系统、劳动力与就业服务。
- 新增第十五波 6 个家庭准备、信息素养、健康劳动力、行政摩擦、社区中介和开放政府透明域骨架，覆盖家庭应急准备、媒体信息素养与公共图书馆、健康劳动力容量、行政负担与程序摩擦、社区健康工作者与同伴支持、公民数据与开放政府透明。
- 新增第十六波 6 个教育、科研、标准、网络安全、算力和临床转化域骨架，覆盖教育可及与终身学习、科研基础设施与开放科学转化、标准计量与质量基础设施、网络安全韧性与关键服务、算力数据中心与 AI 基础设施、临床试验与监管科学转化。
- 新增第十七波 6 个空间、天气、建筑、制造、采购和 One Health 相关域骨架，覆盖空间定位导航与位置基础设施、天气气候观测与预报、建筑消防与生命安全规范、制造与维修能力、公共采购与合同能力、动物健康与人兽共患界面。
- 新增第十八波 6 个实验室、人体材料、废弃物、辐射、化学和关键材料相关域骨架，覆盖公共卫生实验室诊断能力、血液器官组织生物警戒、废弃物危险材料连续性、辐射核安全防护、化学安全中毒控制和关键矿物材料韧性。
- 新增第二十七波 6 个海岸、土木与城市基础设施域骨架，覆盖海岸海洋蓝色经济、渔业水生食物、防洪工程安全、公共工程资产管理、城市土地使用规划和城市绿蓝基础设施。
- 新增第二十八波 6 个公用事业生命线连续性域骨架，覆盖电网可靠性、水务污水公用事业、燃料热能服务、公共交通运营、关键基础设施生命线互依赖和公用事业可负担性断供保护。
- 新增第二十九波 6 个生物医学平台域骨架，覆盖基因治疗与基因编辑递送安全、生物年龄钟验证、多组学个人基线、工程细胞疗法、类器官组织芯片模型和异种移植工程器官替换。
- 新增第三十波 6 个定量方法学域骨架，覆盖因果推断与目标试验模拟、生存分析与健康寿命风险建模、人类数字孪生生命历程仿真、实施科学与依从行为改变、不确定性量化与模型校准、数据质量缺失代表性审查。
- 新增第三十一波 6 个知识治理、技术预见与扩散域骨架，覆盖隐私保护计算、知识图谱本体语义互操作、模型卡 AI 审计文档、技术预见地平线扫描、研究组合资金治理和知识产权技术转移可及。

## 主动不做

- 不把 Biocat 采集脚本泛化为 Human Infra 通用采集框架。
- 不引入 Web 框架、数据库或服务端目录。
- 不新增记忆编辑或中枢生命支持的实验协议。
- 不新增细胞重编程实验协议、载体构建、剂量、给药或人体应用建议。
- 不新增再生医学、癌症、免疫、神经、生物停滞、认知增强等高风险域的操作协议或个体建议。
- 不新增饮食、运动、心血管、肌骨、戒断、牙科、保险、福利或法律相关的个体处方和申请建议。
- 不新增基因编辑、端粒酶激活、senolytic、干细胞、微生物组、肝肾检测解释、药物剂量或实验操作建议。
- 不新增黑客攻击、账号接管、认证绕过、AI 越狱、恶意自动化、供应链规避、生物实验协议、病原体工程、危险环境操作或生命支持建造指南。
- 不新增氧疗、呼吸机、激素方案、抗凝/止血用药、输血、伤口处理、敷料、淋巴引流、设备使用或个体医疗建议。
- 不新增胃肠诊疗、饮食处方、补液电解质、酸碱处理、热病急救、泌尿感染处理、盆底训练、生育治疗、辅助生殖、妊娠管理或避孕建议。
- 不新增 ADHD、心理、神经诊断治疗、学习/职业处方、个体日程安排、投资/保险/税务/福利建议、劳动争议建议或信息操控策略。
- 不新增个体诊断治疗、医生/医院/保险选择、护理计划、机构选择、住房申请、租买房、维修、交通路线、驾驶、法律身份申请、移民、证件办理、应急撤离、急救或生存操作建议。
- 不新增用药、剂量、替代药物、停药、购药、处方解释、病历解释、保险权益判断、远程分诊、设备选择、社区资源资格判断、翻译认证替代、劳动争议策略、工资计算或投诉策略建议。
- 不新增法律合规判断、PHI/基因/神经数据处理架构、去标识化保证、个体量表分数解释、诊断、残障/保险判断、投资/报销/覆盖建议、疫苗医学建议、疫情预测保证、孕产/儿童医疗建议、家庭监控、医疗事故法律意见、机构排名或患者安全惩罚性监控。
- 不新增实时灾害指挥、撤离路线、急救医疗、危险物资储存、宣传操控、微定向影响、职业/执照/移民/薪资建议、个案申请策略、福利/税务/法律争议处理、心理咨询、危机处理、人肉搜索、隐私攻击、监控目标定位、访问控制规避或 FOIA 个案法律建议。
- 不新增个体饮食、食品处置、补水、水质检测、净水购买、电气施工、发电设备、燃料储存、福利申请、资格判断、保险选择、理赔、托育机构选择、育儿处方、补贴申请、虚假材料、制度规避或保险欺诈建议。
- 不新增法律意见、案件策略、竞选操控、投票压制、移民/庇护个案建议、边境穿越路线、黑客攻击、账号绕过、自卫战术、武器、跟踪定位、产品维修改装、药品停用、医疗器械操作、车辆处理、索赔或恐慌传播建议。
- 不新增个体社区风险评分、公共服务申请策略、实时应急指挥、警报发布操作、灾害救济资格判断、灾害贷款/保险/住房建议、银行/支付产品建议、职业规划、简历面试、工资判断、招聘承诺或就业法律建议。
- 不新增实时灾害指挥、撤离路线、急救医疗、危险物储存、宣传操控、平台规避、内容伪造、择医排名、职业执照建议、虚假证明、个案申请、CHW 医疗替代、隐私攻击、再识别操作或 FOIA 个案法律策略。
- 不新增个人升学择校、留学考试、职业证书、教育投资、论文代写、学术操控、数据造假、认证规避、检测伪造、网络攻击、漏洞利用、盗用算力、绕过计费、芯片走私、临床试验入组、治疗用药、停药、人体试验操作或监管规避建议。
- 不新增跟踪监控、人肉搜索、危险路线、实时灾害指挥、撤离路线、建筑施工、电气消防改造、灭火救援、制造维修步骤、假冒零件、投标策略、围标串标、采购规避、动物诊疗、养殖防疫操作、野生动物捕捉、病原体处理或动物交易建议。
- 不新增样本采集、检测操作、病原处理、输血/移植决策、器官匹配、人体材料获取、危险废物处置、放射源/核材料操作、辐射事故现场指挥、化学中毒处理、化学合成混配、关键矿物投资交易、非法采矿、受管制材料获取或危险回收建议。
- 不新增作战战术、武器、目标选择、政治动员、宣传操控、通信破坏、网络入侵、投资交易、税务规避、洗钱、制裁规避、腐败操作、举报策略、个案法律/金融/行政/政治建议。
- 不新增个体寿命预测、个体死亡日期、临床治疗建议、试验入组建议、模型输出保证、自动化决策、歧视性风险评分、数据再识别、数据清洗伪造、统计显著性操控或将不确定模型写成事实结论。
- 不新增论文代写、伪造审稿、操控引用、IRB 规避、诱导研究参与、非法采样、样本来源隐匿、队列参与者重新识别、真实世界数据越权访问、选择性登记报告、伪造校准、设备篡改、医疗器械改装或把仪器读数写成个人诊断和寿命预测。
- 不新增实时海岸、风暴潮、海啸、洪水、水坝、堤防、排水、撤离、船只航行、港口作业、市政应急、防洪工程设计、公共工程检查维修、城市开发、分区变更、基础设施弱点利用、非法捕捞、海关规避或工程/地产/保险/采购/投资建议。
- 不新增电网调度、控制系统、设施弱点、绕供、绕表、公交逃票、公共设施攻击、燃料储存操作、管线/泵站/发电设备维修、实时恢复指挥、个体账单争议、资格申请、缴费规避、断供法律策略或公用事业投资建议。
- 不新增基因编辑设计、递送载体构建、细胞制造、类器官培养、组织芯片制造、异种移植操作、器官保存灌注、动物处理、样本处理、人体试验、治疗选择、检测解释、生物年龄检测购买建议或个体医疗建议。
- 不新增自制纳米材料、非临床给药、双重用途分子设计、表观遗传编辑操作、脑保存操作、脑仿真身份承诺、密码攻击、认证绕过、安全关键系统规避、档案窃取、版权规避或数字永生承诺。
- 不新增卒中急救、脑震荡返赛返工许可、谵妄/昏迷/癫痫/自主神经/偏头痛个体诊断、用药、预后、急救、活动许可、影像/EEG/可穿戴解释或 AI 个人医疗结论。
- 不新增眼科/听力/前庭/言语语言/吞咽/嗅味觉/周围神经的个体诊断、治疗、设备处方、检查解释、康复计划、饮食质地调整、误吸处置、跌倒训练、驾驶/工作/活动许可或 AI 个人医疗结论。
- 不新增实时空间天气操作、地震预测、海啸撤离路线、火山避难命令、近地天体撞击预测、极端高温个人急救、建筑安全、工程设计、保险、投资或公共安全替代建议。
- 不把度规红移固有时差分路径、相对论等待或其他未来等待路径写成当前可执行工程。
- 不把远期研究域伪装成当前可执行产品。

## 验证点

- 根 README 能解释 Human Infra，而不是只解释 Biocat。
- Biocat 的数据和脚本仍能在子域内被定位和编译。
- “永生”和“记忆编辑”有独立边界，不污染长寿证据模型。
- “细胞重编程”有独立机制边界，不把山中因子、部分重编程、化学重编程或商业公告混入普通长寿干预证据账本。
- “度规红移固有时差分路径（黑洞等待室）”有独立 Future Waiting 边界，不污染长寿证据、记忆编辑或去具身中枢模型。
- 新增研究域都能回到 [Research Domain Atlas](research-domain-atlas.md) 的先验条件和域判定契约。
- 原始资料有稳定归档路径，后续不会继续留在根目录。
