# domains 目录说明

`domains/` 保存 Human Infra 的独立子域。每个子域都是一个有边界的研究或产品方向，必须说明对象、非目标、证据要求和上游/下游关系。

## 目录结构

```text
domains/
├── AGENTS.md
├── README.md
├── antimicrobial-resilience/
│   ├── AGENTS.md
│   └── README.md
├── assistive-technology-access/
│   ├── AGENTS.md
│   └── README.md
├── biostasis-cryopreservation/
│   ├── AGENTS.md
│   └── README.md
├── ai-agency-safety/
│   ├── AGENTS.md
│   └── README.md
├── attention-executive-control/
│   ├── AGENTS.md
│   └── README.md
├── cancer-control/
│   ├── AGENTS.md
│   └── README.md
├── cellular-reprogramming/
│   ├── AGENTS.md
│   └── README.md
├── cognitive-augmentation/
│   ├── AGENTS.md
│   └── README.md
├── digital-identity-security/
│   ├── AGENTS.md
│   └── README.md
├── disembodied-cns/
│   ├── AGENTS.md
│   └── README.md
├── future-waiting/
│   ├── AGENTS.md
│   ├── README.md
│   └── paths/
├── governance-rights/
│   ├── AGENTS.md
│   └── README.md
├── immune-maintenance/
│   ├── AGENTS.md
│   └── README.md
├── longevity-evidence/
│   ├── AGENTS.md
│   ├── README.md
│   ├── data/
│   ├── docs/
│   └── scripts/
├── genomic-stability-dna-repair/
│   ├── AGENTS.md
│   └── README.md
├── telomere-maintenance/
│   ├── AGENTS.md
│   └── README.md
├── proteostasis-autophagy/
│   ├── AGENTS.md
│   └── README.md
├── mitochondrial-bioenergetics/
│   ├── AGENTS.md
│   └── README.md
├── cellular-senescence-clearance/
│   ├── AGENTS.md
│   └── README.md
├── extracellular-matrix-glycation/
│   ├── AGENTS.md
│   └── README.md
├── financial-resilience-access/
│   ├── AGENTS.md
│   └── README.md
├── food-security-nutrition-access/
│   ├── AGENTS.md
│   └── README.md
├── water-sanitation-hygiene-continuity/
│   ├── AGENTS.md
│   └── README.md
├── energy-access-resilience/
│   ├── AGENTS.md
│   └── README.md
├── healthcare-access-continuity/
│   ├── AGENTS.md
│   └── README.md
├── medicine-access-treatment-continuity/
│   ├── AGENTS.md
│   └── README.md
├── patient-data-interoperability/
│   ├── AGENTS.md
│   └── README.md
├── telehealth-remote-monitoring-access/
│   ├── AGENTS.md
│   └── README.md
├── health-data-privacy-governance/
│   ├── AGENTS.md
│   └── README.md
├── functioning-quality-of-life-outcomes/
│   ├── AGENTS.md
│   └── README.md
├── health-economics-value-assessment/
│   ├── AGENTS.md
│   └── README.md
├── immunization-public-health-surveillance/
│   ├── AGENTS.md
│   └── README.md
├── maternal-newborn-child-development/
│   ├── AGENTS.md
│   └── README.md
├── patient-safety-organizational-learning/
│   ├── AGENTS.md
│   └── README.md
├── caregiving-long-term-care/
│   ├── AGENTS.md
│   └── README.md
├── housing-built-environment-stability/
│   ├── AGENTS.md
│   └── README.md
├── transportation-access-mobility/
│   ├── AGENTS.md
│   └── README.md
├── legal-identity-civil-registration/
│   ├── AGENTS.md
│   └── README.md
├── access-to-justice-legal-aid/
│   ├── AGENTS.md
│   └── README.md
├── civic-participation-election-access/
│   ├── AGENTS.md
│   └── README.md
├── migration-displacement-humanitarian-continuity/
│   ├── AGENTS.md
│   └── README.md
├── digital-inclusion-connectivity/
│   ├── AGENTS.md
│   └── README.md
├── social-protection-benefits-delivery/
│   ├── AGENTS.md
│   └── README.md
├── community-resource-navigation/
│   ├── AGENTS.md
│   └── README.md
├── social-determinants-community-vulnerability/
│   ├── AGENTS.md
│   └── README.md
├── public-service-design-accessibility/
│   ├── AGENTS.md
│   └── README.md
├── emergency-alerts-communications/
│   ├── AGENTS.md
│   └── README.md
├── disaster-recovery-relief-continuity/
│   ├── AGENTS.md
│   └── README.md
├── financial-inclusion-payment-systems/
│   ├── AGENTS.md
│   └── README.md
├── workforce-employment-services/
│   ├── AGENTS.md
│   └── README.md
├── household-emergency-preparedness-resilience/
│   ├── AGENTS.md
│   └── README.md
├── media-information-literacy-public-libraries/
│   ├── AGENTS.md
│   └── README.md
├── health-workforce-capacity/
│   ├── AGENTS.md
│   └── README.md
├── administrative-burden-procedural-friction/
│   ├── AGENTS.md
│   └── README.md
├── community-health-workers-peer-support/
│   ├── AGENTS.md
│   └── README.md
├── civic-data-open-government-transparency/
│   ├── AGENTS.md
│   └── README.md
├── education-access-lifelong-learning/
│   ├── AGENTS.md
│   └── README.md
├── research-infrastructure-open-science-translation/
│   ├── AGENTS.md
│   └── README.md
├── standards-metrology-quality-infrastructure/
│   ├── AGENTS.md
│   └── README.md
├── cybersecurity-resilience-critical-services/
│   ├── AGENTS.md
│   └── README.md
├── compute-data-center-ai-infrastructure/
│   ├── AGENTS.md
│   └── README.md
├── clinical-trials-regulatory-science-translation/
│   ├── AGENTS.md
│   └── README.md
├── geospatial-navigation-location-infrastructure/
│   ├── AGENTS.md
│   └── README.md
├── weather-climate-observation-forecasting/
│   ├── AGENTS.md
│   └── README.md
├── building-fire-life-safety-codes/
│   ├── AGENTS.md
│   └── README.md
├── manufacturing-repair-capacity/
│   ├── AGENTS.md
│   └── README.md
├── public-procurement-contracting-capacity/
│   ├── AGENTS.md
│   └── README.md
├── animal-health-zoonotic-interface-one-health/
│   ├── AGENTS.md
│   └── README.md
├── public-health-laboratory-diagnostic-capacity/
│   ├── AGENTS.md
│   └── README.md
├── blood-organ-tissue-biovigilance-transplantation/
│   ├── AGENTS.md
│   └── README.md
├── waste-management-hazardous-materials-continuity/
│   ├── AGENTS.md
│   └── README.md
├── radiation-nuclear-safety-protection/
│   ├── AGENTS.md
│   └── README.md
├── chemical-safety-poison-control-toxicology/
│   ├── AGENTS.md
│   └── README.md
├── critical-minerals-materials-resilience/
│   ├── AGENTS.md
│   └── README.md
├── air-quality-ventilation-exposure-control/
│   ├── AGENTS.md
│   └── README.md
├── food-safety-contamination-control/
│   ├── AGENTS.md
│   └── README.md
├── occupational-exposure-industrial-hygiene/
│   ├── AGENTS.md
│   └── README.md
├── medical-device-equipment-safety-maintenance/
│   ├── AGENTS.md
│   └── README.md
├── sterilization-disinfection-infection-control/
│   ├── AGENTS.md
│   └── README.md
├── built-environment-accessibility-universal-design/
│   ├── AGENTS.md
│   └── README.md
├── insurance-risk-transfer/
│   ├── AGENTS.md
│   └── README.md
├── childcare-family-continuity/
│   ├── AGENTS.md
│   └── README.md
├── emergency-preparedness-response/
│   ├── AGENTS.md
│   └── README.md
├── personal-safety-violence-prevention/
│   ├── AGENTS.md
│   └── README.md
├── product-safety-recall-systems/
│   ├── AGENTS.md
│   └── README.md
├── microbiome-ecology/
│   ├── AGENTS.md
│   └── README.md
├── stem-cell-reserve-renewal/
│   ├── AGENTS.md
│   └── README.md
├── renal-hepatic-clearance/
│   ├── AGENTS.md
│   └── README.md
├── gastrointestinal-barrier-absorption/
│   ├── AGENTS.md
│   └── README.md
├── respiratory-oxygenation/
│   ├── AGENTS.md
│   └── README.md
├── blood-oxygen-hemostasis/
│   ├── AGENTS.md
│   └── README.md
├── endocrine-hormonal-regulation/
│   ├── AGENTS.md
│   └── README.md
├── lymphatic-glymphatic-clearance/
│   ├── AGENTS.md
│   └── README.md
├── fluid-electrolyte-acid-base-homeostasis/
│   ├── AGENTS.md
│   └── README.md
├── thermal-homeostasis-resilience/
│   ├── AGENTS.md
│   └── README.md
├── nutrition-metabolic-health/
│   ├── AGENTS.md
│   └── README.md
├── physical-activity-mobility/
│   ├── AGENTS.md
│   └── README.md
├── cardiovascular-resilience/
│   ├── AGENTS.md
│   └── README.md
├── musculoskeletal-integrity/
│   ├── AGENTS.md
│   └── README.md
├── skin-barrier-wound-healing/
│   ├── AGENTS.md
│   └── README.md
├── urogenital-continuity/
│   ├── AGENTS.md
│   └── README.md
├── reproductive-fertility-continuity/
│   ├── AGENTS.md
│   └── README.md
├── measurement-feedback/
│   ├── AGENTS.md
│   └── README.md
├── mental-health-affective-stability/
│   ├── AGENTS.md
│   └── README.md
├── memory-editing/
│   ├── AGENTS.md
│   └── README.md
├── neuro-continuity/
│   ├── AGENTS.md
│   └── README.md
├── pain-suffering-control/
│   ├── AGENTS.md
│   └── README.md
├── planetary-health-environment/
│   ├── AGENTS.md
│   └── README.md
├── regenerative-medicine/
│   ├── AGENTS.md
│   └── README.md
├── rehabilitation-functioning/
│   ├── AGENTS.md
│   └── README.md
├── resource-social-infra/
│   ├── AGENTS.md
│   └── README.md
├── risk-engineering/
│   ├── AGENTS.md
│   └── README.md
├── sensory-continuity/
│   ├── AGENTS.md
│   └── README.md
├── sleep-circadian-recovery/
│   ├── AGENTS.md
│   └── README.md
├── social-connection-relational-infra/
│   ├── AGENTS.md
│   └── README.md
├── space-extreme-habitation/
│   ├── AGENTS.md
│   └── README.md
├── substance-exposure-control/
│   ├── AGENTS.md
│   └── README.md
├── supply-chain-continuity/
│   ├── AGENTS.md
│   └── README.md
├── synthetic-biology-biosecurity/
│   ├── AGENTS.md
│   └── README.md
├── health-literacy-navigation/
│   ├── AGENTS.md
│   └── README.md
├── language-access-plain-communication/
│   ├── AGENTS.md
│   └── README.md
├── labor-rights-workplace-protection/
│   ├── AGENTS.md
│   └── README.md
├── information-integrity-trust/
│   ├── AGENTS.md
│   └── README.md
├── learning-skill-acquisition/
│   ├── AGENTS.md
│   └── README.md
├── occupational-work-design/
│   ├── AGENTS.md
│   └── README.md
├── oral-health-continuity/
│   ├── AGENTS.md
│   └── README.md
└── time-allocation-effective-time/
    ├── AGENTS.md
    └── README.md
```

## 职责边界

- `longevity-evidence/` 是当前唯一含数据和采集脚本的产品化子域。
- `genomic-stability-dna-repair/`、`telomere-maintenance/`、`proteostasis-autophagy/`、`mitochondrial-bioenergetics/`、`cellular-senescence-clearance/`、`extracellular-matrix-glycation/`、`microbiome-ecology/`、`stem-cell-reserve-renewal/` 和 `renal-hepatic-clearance/` 负责分子维护、结构材料、宿主生态、内源性修复和肝肾清除底座。
- `respiratory-oxygenation/`、`blood-oxygen-hemostasis/`、`endocrine-hormonal-regulation/` 和 `lymphatic-glymphatic-clearance/` 负责氧合、血液运输、激素协调和清除网络这些跨器官稳态条件。
- `gastrointestinal-barrier-absorption/`、`fluid-electrolyte-acid-base-homeostasis/` 和 `thermal-homeostasis-resilience/` 负责营养进入、内环境化学和体温边界这些基础稳态条件。
- `nutrition-metabolic-health/`、`physical-activity-mobility/`、`cardiovascular-resilience/` 和 `musculoskeletal-integrity/` 负责营养、行动、循环和承载结构这些身体运行条件。
- `urogenital-continuity/` 和 `reproductive-fertility-continuity/` 负责尿控、泌尿感染、性功能、生育力、生殖衰老和未来选择权。
- `attention-executive-control/`、`learning-skill-acquisition/` 和 `time-allocation-effective-time/` 负责注意力、学习能力和有效时间这些主体代理与任务资源条件。
- `financial-resilience-access/`、`financial-inclusion-payment-systems/`、`workforce-employment-services/`、`education-access-lifelong-learning/`、`occupational-work-design/`、`labor-rights-workplace-protection/`、`language-access-plain-communication/`、`media-information-literacy-public-libraries/` 和 `information-integrity-trust/` 负责财务韧性、金融支付入口、就业服务、教育与终身学习、工作环境、劳动权利、语言理解入口、公共知识入口和信息可信度这些资源入口与认知环境条件。
- `food-security-nutrition-access/`、`water-sanitation-hygiene-continuity/`、`energy-access-resilience/`、`social-protection-benefits-delivery/`、`community-resource-navigation/`、`social-determinants-community-vulnerability/`、`public-service-design-accessibility/`、`administrative-burden-procedural-friction/`、`civic-data-open-government-transparency/`、`insurance-risk-transfer/` 和 `childcare-family-continuity/` 负责食物、水卫生、能源、公共福利、社区资源导航、社区脆弱性、公共服务可达、行政负担、开放数据透明、保险风险池和托育家庭连续性这些基础生计、公共服务与风险分摊条件。
- `research-infrastructure-open-science-translation/`、`standards-metrology-quality-infrastructure/`、`compute-data-center-ai-infrastructure/`、`cybersecurity-resilience-critical-services/`、`geospatial-navigation-location-infrastructure/`、`manufacturing-repair-capacity/`、`supply-chain-continuity/` 和 `ai-agency-safety/` 负责科研转化、标准计量质量、算力 AI 基础设施、网络安全韧性、空间定位导航、制造维修能力、供应链连续和 AI 代理安全这些技术窗口生成、可信化和可用性的外部底座。
- `healthcare-access-continuity/`、`medicine-access-treatment-continuity/`、`patient-data-interoperability/`、`telehealth-remote-monitoring-access/`、`health-data-privacy-governance/`、`functioning-quality-of-life-outcomes/`、`health-economics-value-assessment/`、`clinical-trials-regulatory-science-translation/`、`immunization-public-health-surveillance/`、`animal-health-zoonotic-interface-one-health/`、`maternal-newborn-child-development/`、`patient-safety-organizational-learning/`、`health-workforce-capacity/`、`community-health-workers-peer-support/`、`caregiving-long-term-care/`、`housing-built-environment-stability/`、`building-fire-life-safety-codes/`、`transportation-access-mobility/`、`legal-identity-civil-registration/`、`emergency-preparedness-response/`、`weather-climate-observation-forecasting/`、`emergency-alerts-communications/`、`household-emergency-preparedness-resilience/` 和 `disaster-recovery-relief-continuity/` 负责医疗接入、药品治疗连续性、患者数据互操作、远程照护、健康数据治理、结局评估、价值评估、临床监管转化、公共卫生监测、动物健康界面、早期生命发展、患者安全、健康劳动力、社区中介支持、长期照护、居住空间、建筑消防生命安全、交通可达、法律身份、应急响应、天气气候观测、预警通信、家庭准备和灾后恢复这些服务接入与生活连续性条件。
- `public-procurement-contracting-capacity/` 负责公共采购、合同、供应商管理、应急采购、透明度和交付验收这些公共能力落地条件。
- `public-health-laboratory-diagnostic-capacity/`、`blood-organ-tissue-biovigilance-transplantation/`、`waste-management-hazardous-materials-continuity/`、`radiation-nuclear-safety-protection/`、`chemical-safety-poison-control-toxicology/` 和 `critical-minerals-materials-resilience/` 负责风险确认、外部生物材料安全、残余物治理、不可见高能暴露、化学毒理和未来技术物质输入这些外部安全与材料支撑条件。
- `air-quality-ventilation-exposure-control/`、`food-safety-contamination-control/`、`occupational-exposure-industrial-hygiene/`、`medical-device-equipment-safety-maintenance/`、`sterilization-disinfection-infection-control/` 和 `built-environment-accessibility-universal-design/` 负责可呼吸环境、食物污染控制、工作暴露控制、医疗设备可靠性、感染控制屏障和物理空间可达性这些日常环境与工具可靠性条件。
- `access-to-justice-legal-aid/`、`civic-participation-election-access/`、`migration-displacement-humanitarian-continuity/` 和 `digital-inclusion-connectivity/` 负责司法可及、公民参与、迁移流离失所人道连续性和数字连接这些制度参与与公共服务接入条件。
- `personal-safety-violence-prevention/` 和 `product-safety-recall-systems/` 负责暴力预防、受害者支持、产品缺陷报告、召回和纠正这些公共安全连续性条件。
- `cellular-reprogramming/` 负责山中因子、部分重编程、化学重编程、AI 因子设计和表观遗传编辑等“细胞状态可重写”谱系，不提供实验协议或人体应用建议。
- `regenerative-medicine/`、`cancer-control/` 和 `immune-maintenance/` 负责身体基底维护相关的机制、风险和证据边界。
- `rehabilitation-functioning/`、`assistive-technology-access/`、`skin-barrier-wound-healing/` 和 `sensory-continuity/` 负责功能恢复、能力补偿、外界屏障和感官反馈连续性。
- `antimicrobial-resilience/` 负责抗微生物耐药、感染控制和现代医学抗感染底座。
- `neuro-continuity/`、`memory-editing/`、`cognitive-augmentation/`、`ai-agency-safety/`、`digital-identity-security/` 和 `disembodied-cns/` 负责神经、身份、认知、AI 代理、数字入口和去具身连续性相关边界。
- `mental-health-affective-stability/`、`sleep-circadian-recovery/` 和 `pain-suffering-control/` 负责心理稳定、恢复调度和持续存在的可承受性。
- `social-connection-relational-infra/` 负责社会连接、孤独、照护网络、信任和社区关系。
- `substance-exposure-control/` 负责烟草、酒精、成瘾性物质、有害暴露和主体自主性风险。
- `health-literacy-navigation/` 和 `language-access-plain-communication/` 负责健康素养、服务导航、清晰语言、语言服务、可理解信息、风险沟通和共同决策。
- `oral-health-continuity/` 负责口腔健康、咀嚼、疼痛、感染、营养和沟通连续性。
- `future-waiting/` 和 `biostasis-cryopreservation/` 负责等待未来的时间成本和损耗成本路径。
- `risk-engineering/`、`planetary-health-environment/`、`resource-social-infra/`、`supply-chain-continuity/`、`synthetic-biology-biosecurity/`、`space-extreme-habitation/` 和 `governance-rights/` 负责外部风险、环境底座、资源底座、关键供应链、生物安全、极端栖居和主体权利保护。
- `measurement-feedback/` 负责所有研究域进入定量模型前的测量、预测和反馈接口。
- 子域之间共享 Human Infra 的伦理和证据原则，但不能共享模糊数据目录或脚本目录。

## 维护规则

- 新子域必须先在 `docs/reference/domain-map.md` 中说明存在理由、边界和非目标。
- 子域内新增文件或目录时，同步更新该子域 `AGENTS.md`。
- 跨子域概念进入 `docs/`；子域专属材料留在对应子域。
- 不为了“未来可能需要”创建空数据、空脚本或空框架目录。
