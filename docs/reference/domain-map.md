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
- `food-security-nutrition-access`、`water-sanitation-hygiene-continuity`、`energy-access-resilience`、`social-protection-benefits-delivery`、`insurance-risk-transfer` 和 `childcare-family-continuity` 关注基础生计与风险分摊。它们不能只放在 `resource-social-infra` 中，因为食物、水卫生、能源、福利递送、风险池和托育各自有独立证据、失败模式和伦理边界。
- `healthcare-access-continuity`、`caregiving-long-term-care`、`housing-built-environment-stability`、`transportation-access-mobility`、`legal-identity-civil-registration` 和 `emergency-preparedness-response` 关注服务接入与生活连续性。它们不能只放进 `resource-social-infra`，因为每个域都有独立证据来源、失败模式、伦理边界和公共系统接口。
- `access-to-justice-legal-aid`、`civic-participation-election-access`、`migration-displacement-humanitarian-continuity`、`digital-inclusion-connectivity`、`personal-safety-violence-prevention` 和 `product-safety-recall-systems` 关注制度参与、人道连续性与公共安全。它们不能只放进 `governance-rights`、`risk-engineering` 或 `supply-chain-continuity`，因为司法救济、公共决策参与、跨制度移动连续性、数字连接、人身安全和产品召回各自有独立机制、来源体系和禁止用途边界。
- `medicine-access-treatment-continuity`、`patient-data-interoperability`、`telehealth-remote-monitoring-access`、`community-resource-navigation`、`language-access-plain-communication` 和 `labor-rights-workplace-protection` 关注治疗执行、数据连续、远程照护、社区转介、语言理解和劳动权利。它们不能只放进 `healthcare-access-continuity`、`health-literacy-navigation`、`resource-social-infra` 或 `occupational-work-design`，因为药品、数据、远程设备、资源目录、语言服务和劳动执行各自有独立来源体系、失败模式和禁止用途边界。
- `nutrition-metabolic-health`、`physical-activity-mobility`、`cardiovascular-resilience` 和 `musculoskeletal-integrity` 关注能量、行动、循环和承载结构这四类常规运行条件。
- `regenerative-medicine`、`cancer-control` 和 `immune-maintenance` 关注身体基底长期可维护性中的不同失败模式。
- `rehabilitation-functioning`、`assistive-technology-access` 和 `sensory-continuity` 关注主体存活之后是否仍能行动、沟通、感知和参与。
- `antimicrobial-resilience` 关注现代医学抗感染底座是否会被耐药性侵蚀。
- `neuro-continuity`、`cognitive-augmentation`、`memory-editing` 和 `disembodied-cns` 关注延续的是否仍是能够行动、记忆和选择的同一主体。
- `mental-health-affective-stability`、`sleep-circadian-recovery`、`pain-suffering-control` 和 `oral-health-continuity` 关注存在时间是否能转化为可承受、可恢复、可行动、可进食和可沟通的有效时间。
- `substance-exposure-control` 关注可避免暴露和成瘾如何同时侵蚀健康风险、资源预算和主体自主性。
- `biostasis-cryopreservation` 关注暂停损耗并等待未来修复，与 `future-waiting` 的时间差分路径互补。
- `risk-engineering`、`planetary-health-environment`、`resource-social-infra`、`social-connection-relational-infra`、`health-literacy-navigation` 和 `governance-rights` 关注主体不被外部风险、资源断裂、环境退化、关系孤立、服务不可理解或制度控制截断。
- `digital-identity-security`、`ai-agency-safety`、`supply-chain-continuity`、`synthetic-biology-biosecurity` 和 `space-extreme-habitation` 关注外部技术底座是否会放大主体持续性，或反过来通过身份断线、代理越权、断供、生物风险和极端环境失效截断主体。
- `measurement-feedback` 关注所有研究域如何被观测、建模、反馈和校正。

把它们拆开，能避免一个错误概念：用“长寿方法”统摄所有人类增强、生命延续和神经干预问题。

## 本轮迁移切片

- 根目录从 Biocat 改为 Human Infra。
- 旧 Biocat 文档、数据和脚本迁入 `domains/longevity-evidence/`。
- 四份最新资料改名归档到 `docs/source-notes/`。
- 新增 Human Infra 总理论、域地图、伦理边界和两个远期研究域 README。
- 新增 `domains/cellular-reprogramming/`，承载山中因子到部分重编程、化学重编程、AI 因子设计和表观遗传编辑的机制谱系。
- 新增研究域图谱和 10 个先验条件域骨架，全部只创建 README / AGENTS，不创建空数据或脚本目录。
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
- 不新增个体饮食、食品处置、补水、水质检测、净水购买、电气施工、发电设备、燃料储存、福利申请、资格判断、保险选择、理赔、托育机构选择、育儿处方、补贴申请、虚假材料、制度规避或保险欺诈建议。
- 不新增法律意见、案件策略、竞选操控、投票压制、移民/庇护个案建议、边境穿越路线、黑客攻击、账号绕过、自卫战术、武器、跟踪定位、产品维修改装、药品停用、医疗器械操作、车辆处理、索赔或恐慌传播建议。
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
