# Research Domain Atlas

Research Domain Atlas 定义 Human Infra 的研究域生成规则：凡是在“有效永生 / 主体持续性最大化”的先验追问链条中构成必要条件、支撑条件、风险条件或反馈条件的对象，都可以被抽象为研究域。

## 生成原则

```text
有效永生何以可能？
  -> 主体必须继续存在
  -> 身体基底必须可维护
  -> 大脑、记忆、身份和行动能力必须连续
  -> 时间窗口必须被延展
  -> 风险函数必须被压低
  -> 资源、环境和社会支持必须稳定
  -> 工具和认知系统必须放大主体而不是吞噬主体
  -> 数字身份、AI 代理、供应链、生物安全和极端栖居等外部技术底座必须可控
  -> 治理和权利必须保护同意、退出和身份
  -> 测量、预测和反馈必须让维护过程可校正
```

研究域不是按“技术热度”生成，而是按“主体持续性成立条件”生成。

## 域判定契约

一个候选域只有同时满足这些条件，才应进入 `domains/`：

| 条件 | 判断问题 |
| --- | --- |
| 独立机制 | 它是否通过独立机制改变主体持续性变量？ |
| 独立证据体系 | 它是否需要自己的论文、数据、案例或审查标准？ |
| 独立失败模式 | 它失败时是否会产生不同于其他域的风险？ |
| 独立伦理边界 | 它是否需要单独说明禁止用途、同意、退出或安全红线？ |
| 独立维护价值 | 放进已有域是否会让已有域概念混乱？ |

## 当前研究域地图

| 先验条件 | 研究域 | 主体变量 | 主要失败模式 |
| --- | --- | --- | --- |
| 身体状态可长期维护 | `longevity-evidence/` | 健康寿命、疾病风险、干预证据 | 把证据不足的干预写成疗效 |
| 营养代谢可稳定 | `nutrition-metabolic-health/` | 能量供给、代谢稳定、营养质量、慢病风险 | 把饮食、补剂或单一指标写成个体处方 |
| 遗传信息可长期保持 | `genomic-stability-dna-repair/` | DNA 损伤、修复能力、突变负荷、癌前风险 | 把分子指标写成个体寿命或治疗结论 |
| 复制边界可维护 | `telomere-maintenance/` | 端粒长度、端粒酶、复制能力、癌症风险 | 忽略端粒延长与肿瘤风险的张力 |
| 细胞状态可重写 | `cellular-reprogramming/` | 表观遗传状态、细胞身份、组织功能 | 去分化、肿瘤化、过度外推 |
| 蛋白质量控制可稳定 | `proteostasis-autophagy/` | 蛋白稳态、自噬、溶酶体、聚集负担 | 把自噬激活写成无条件有益 |
| 细胞能源可持续 | `mitochondrial-bioenergetics/` | 线粒体功能、ATP、氧化还原、疲劳 | 把能量指标写成寿命预测 |
| 衰老细胞负担可治理 | `cellular-senescence-clearance/` | senescence burden、SASP、炎症、组织环境 | 忽略衰老细胞的肿瘤抑制和修复角色 |
| 组织材料结构可维护 | `extracellular-matrix-glycation/` | ECM、胶原、弹性、糖化、交联、纤维化 | 把抗糖化或组织硬度写成个体处方 |
| 宿主-微生物生态可稳定 | `microbiome-ecology/` | 菌群结构、代谢物、免疫互作、炎症 | 把相关性写成因果干预结论 |
| 内源性修复储备可维护 | `stem-cell-reserve-renewal/` | 干细胞储备、生态位、组织更新、再生能力 | 把干细胞激活写成无条件有益 |
| 身体部件可修复 | `regenerative-medicine/` | 器官功能、组织修复、替代能力 | 整合失败、免疫排斥、功能不持久 |
| 营养入口可转化为可用输入 | `gastrointestinal-barrier-absorption/` | 消化、吸收、肠道屏障、胃肠动力 | 把胃肠症状、菌群或吸收问题写成个体处方 |
| 呼吸氧合可持续 | `respiratory-oxygenation/` | 通气、氧合、肺储备、空气暴露 | 把血氧或肺功能写成个体诊断 |
| 血液运输与止血可平衡 | `blood-oxygen-hemostasis/` | 血红蛋白、氧运、凝血、出血、血栓 | 把血液指标写成用药或急救建议 |
| 跨器官激素协调可稳定 | `endocrine-hormonal-regulation/` | 激素轴、反馈环、代谢信号、压力反应 | 把激素指标写成补充、处方或寿命判断 |
| 清除网络可运行 | `lymphatic-glymphatic-clearance/` | 淋巴运输、组织液、脑废物清除、水肿 | 把清除假说写成确定治疗路径 |
| 内部化学环境可稳定 | `fluid-electrolyte-acid-base-homeostasis/` | 水分、电解质、渗透压、酸碱、内环境 | 把实验室指标写成补液、药物或急救建议 |
| 温度边界可维持 | `thermal-homeostasis-resilience/` | 体温、散热、出汗、热暴露、寒冷暴露 | 把热病、低体温或补水写成个体急救指南 |
| 行动输入可维持 | `physical-activity-mobility/` | 身体活动、心肺适能、力量、移动能力 | 把运动表现写成通用处方或忽视损伤恢复 |
| 循环系统可韧性运行 | `cardiovascular-resilience/` | 血压、血脂、血管、心脏、卒中和心衰风险 | 把单项指标写成确定风险或治疗建议 |
| 承载结构可持续 | `musculoskeletal-integrity/` | 肌肉、骨骼、关节、跌倒、疼痛和独立性 | 存活但失能、跌倒骨折、长期疼痛 |
| 外界屏障可维护 | `skin-barrier-wound-healing/` | 皮肤屏障、伤口愈合、感染入口、热调节 | 把伤口或皮肤表现写成诊断和护理方案 |
| 排泄、性功能和尊严可连续 | `urogenital-continuity/` | 尿控、尿路、盆底、感染、性功能、尊严 | 把症状、感染或性功能写成诊断和治疗建议 |
| 生殖未来选择权可保留 | `reproductive-fertility-continuity/` | 生育力、配子质量、生殖衰老、生殖自主性 | 把生育力、激素或年龄写成个体选择结论 |
| 注意力可被稳定分配 | `attention-executive-control/` | 持续注意、工作记忆、抑制控制、任务切换、冲动控制 | 把注意力效率写成诊断、药物或高压工作处方 |
| 时间可转化为能力 | `learning-skill-acquisition/` | 学习速度、反馈质量、练习轮次、技能迁移、再训练 | 把课程、工具或学习技巧写成确定能力提升承诺 |
| 日历时间可转化为有效时间 | `time-allocation-effective-time/` | 可支配时间、恢复时间、等待成本、行政负担、任务摩擦 | 把节省时间写成压榨恢复、关系和主体自主性的理由 |
| 资源入口可承受冲击 | `financial-resilience-access/` | 收入稳定、储蓄缓冲、债务、保险、支付能力、资产安全 | 把财务韧性写成投资、保险、税务或福利个体建议 |
| 工作系统可持续 | `occupational-work-design/` | 工时、暴露、人体工学、压力、自主性、收入、技能机会 | 把生产率最大化写成压榨劳动或规避安全权利 |
| 劳动权利可执行 | `labor-rights-workplace-protection/` | 工资工时、安全权利、反歧视、反报复、申诉入口、组织治理 | 把公共劳动资料写成个案法律意见、工资判断或争议策略 |
| 信息环境可支撑判断 | `information-integrity-trust/` | 来源可信度、证据质量、误导暴露、可追溯性、信任链 | 提供操控、伪造、平台规避或虚假内容传播策略 |
| 功能可恢复 | `rehabilitation-functioning/` | 活动能力、自理能力、沟通能力、社会参与 | 存活但失能、长期依赖、参与中断 |
| 癌症风险可压低 | `cancer-control/` | 肿瘤发生、进展、复发、死亡风险 | 耐药、复发、筛查误判、治疗伤害 |
| 免疫系统可维护 | `immune-maintenance/` | 感染防御、炎症、免疫监视 | 感染、慢性炎症、自身免疫 |
| 抗感染医学底座可持续 | `antimicrobial-resilience/` | 感染可治性、耐药传播、医疗安全 | 耐药扩散、普通感染高死亡化、医疗系统失效 |
| 清除与代谢器官可运行 | `renal-hepatic-clearance/` | 肾功能、肝功能、解毒、药物清除、内环境 | 毒性积累、药物风险、治疗选择受限 |
| 神经和身份连续 | `neuro-continuity/` | 记忆、意识、人格、行动能力 | 神经退行、身份断裂、主体不连续 |
| 感官反馈可持续 | `sensory-continuity/` | 视觉、听觉、平衡、感官反馈 | 跌倒、隔离、沟通失败、认知负担 |
| 记忆可审查地处理 | `memory-editing/` | 记忆痕迹、人格连续性、同意 | 操控、伪记忆、不可逆损伤 |
| 中枢可外部维持 | `disembodied-cns/` | 神经维持、生命支持、接口闭环 | 去主体化、控制失效、生命支持失败 |
| 等待成本可压缩 | `future-waiting/` | 主观时间、相对时间、未来窗口 | 退出失败、连续性失败、工程风险 |
| 损耗可暂停 | `biostasis-cryopreservation/` | 结构保存、代谢降低、未来修复机会 | 不可逆损坏、复温失败、复活外推 |
| 认知与行动可放大 | `cognitive-augmentation/` | 学习、判断、记忆外化、工具能力 | 依赖、失控、主体自主性下降 |
| AI 代理可受控 | `ai-agency-safety/` | AI 代理、授权、工具调用、监督、审计 | 代理越权、误导、泄露、不可逆行动 |
| 数字身份可恢复 | `digital-identity-security/` | 账号、凭据、身份恢复、服务入口 | 身份盗用、账号丢失、服务断线 |
| 心理和动机系统可稳定 | `mental-health-affective-stability/` | 情绪稳定、压力恢复、动机、自杀风险 | 自伤、成瘾、行动崩塌、关系断裂 |
| 恢复调度可稳定 | `sleep-circadian-recovery/` | 睡眠、昼夜节律、疲劳、恢复能力 | 慢性疲劳、错误、代谢/免疫/情绪失稳 |
| 能力可被工具补偿 | `assistive-technology-access/` | 辅助设备、无障碍、环境适配 | 有技术但不可及、维护失败、参与排除 |
| 有害暴露可控制 | `substance-exposure-control/` | 烟草、酒精、成瘾性物质、毒性暴露、自主性 | 暴露累积、成瘾、风险迁移、主体控制权下降 |
| 外部风险可治理 | `risk-engineering/` | 风险暴露、预警、恢复能力 | 事故、灾害、暴力、系统性失效 |
| 环境底座可承载主体 | `planetary-health-environment/` | 空气、水、气候、污染、生态系统 | 环境暴露、资源崩塌、迁移、灾害 |
| 资源和社会底座可持续 | `resource-social-infra/` | 食物、水、能源、住房、照护、医疗可及 | 断供、贫困、服务排除、社会孤立 |
| 食物输入可持续 | `food-security-nutrition-access/` | 食物可得性、可负担性、食品安全、营养输入、价格冲击、供应稳定 | 饥饿、营养不足、食品不安全、价格冲击或供应断裂 |
| 水卫生条件可持续 | `water-sanitation-hygiene-continuity/` | 安全饮用水、卫生设施、洗手、污水处理、WASH 覆盖、服务可靠性 | 感染、脱水、尊严损害、照护负担或公共卫生风险 |
| 能源服务可运行 | `energy-access-resilience/` | 电力、清洁烹饪、能源负担、停电、温控、通信供能、医疗设备供电 | 照明、烹饪、温控、通信、医疗设备和数字服务中断 |
| 医疗服务可连续 | `healthcare-access-continuity/` | 初级卫生保健、急诊、预防、转诊、随访、费用、质量 | 有医疗资源但不可及、不可负担、不可连续或质量不可审查 |
| 药品和治疗可持续执行 | `medicine-access-treatment-continuity/` | 基本药物、短缺、标签、覆盖、药房可及、用药安全 | 处方无法转化为持续治疗，或把药品资料写成个体用药建议 |
| 患者数据可携带互通 | `patient-data-interoperability/` | 健康记录访问、数据可携带、互操作、授权应用、跨机构交换 | 资料被机构锁住、照护交接断裂、或绕过授权与隐私边界 |
| 远程照护可达可升级 | `telehealth-remote-monitoring-access/` | 远程问诊、远程患者监测、居家设备、覆盖、升级路径 | 远程数据被误当诊断，或把 telehealth 写成急诊替代和产品背书 |
| 敏感健康数据可被治理 | `health-data-privacy-governance/` | 同意、撤回、隐私、安全、共享、用途边界、审计、再识别风险 | 测量系统变成监控、歧视、越权使用或不可逆隐私暴露 |
| 功能和生活质量可被主体中心地衡量 | `functioning-quality-of-life-outcomes/` | 功能状态、生活质量、症状负担、患者报告结局、主体体验 | 指标替代真实体验，或把人压缩成单一分数和资格判断 |
| 稀缺资源价值可审查 | `health-economics-value-assessment/` | 疾病负担、成本效果、HTA、预算影响、公平、公共价值 | 把资源配置简化为价格、投资、报销或个体治疗取舍建议 |
| 群体免疫和传染病风险可监测 | `immunization-public-health-surveillance/` | 免疫覆盖、病例监测、IPC、HAI、AMR、One Health、废水信号 | 把群体监测写成个体医疗建议、疫情保证或公共卫生规避 |
| 早期生命条件可支撑未来主体 | `maternal-newborn-child-development/` | 孕产安全、新生儿、儿童健康、生长、早期发展、养育照护 | 把母婴儿童资料写成个体医疗、育儿、排名或家庭监控建议 |
| 医疗组织可从错误中学习 | `patient-safety-organizational-learning/` | 事件报告、近失误、团队沟通、根因分析、安全文化、行动闭环 | 把患者安全写成追责、机构背书、法律判断或惩罚性监控 |
| 照护可持续 | `caregiving-long-term-care/` | 家庭照护、长期照护、居家社区支持、照护协调、照护者负担 | 长寿退化为无人照护、照护者崩溃、失能支持中断或尊严丧失 |
| 居住环境可稳定 | `housing-built-environment-stability/` | 住房稳定、住房质量、室内环境、无障碍、社区资源、建成环境 | 居住空间持续制造暴露、跌倒、孤立、服务断点或照护不可行 |
| 日常移动和服务接入可达 | `transportation-access-mobility/` | 公共交通、无障碍交通、出行时间、医疗交通、交通成本、交通安全 | 有资源但到不了，服务延误、缺席、孤立或撤离不可达 |
| 法律身份可被承认 | `legal-identity-civil-registration/` | 法律身份、出生登记、民事登记、生命统计、身份文件、服务资格 | 无证、登记缺失、身份错误或制度不承认导致权利与服务断线 |
| 权利救济可达 | `access-to-justice-legal-aid/` | 民事法律需求、法律援助、司法可及、程序负担、代理缺口、申诉执行 | 名义权利无法转化为住房、收入、安全、身份和服务恢复 |
| 公共决策参与可达 | `civic-participation-election-access/` | 选民登记、投票可及、无障碍投票、选举标准、公共参与、制度反馈 | 被排除在公共规则生成之外，资源、权利和风险分配缺少主体反馈 |
| 迁移和流离失所状态可连续 | `migration-displacement-humanitarian-continuity/` | 迁移、难民、流离失所、身份连续、医疗、教育、庇护、保护、人道协调 | 跨地点和跨制度后身份、服务、庇护、教育和保护断裂 |
| 数字连接可达 | `digital-inclusion-connectivity/` | 互联网接入、设备、数字技能、可负担性、无障碍、人工帮助、数字公共服务 | 数字排除导致医疗、福利、教育、工作、身份和应急信息不可达 |
| 社会保护可递送 | `social-protection-benefits-delivery/` | 公共福利、社会保护、资格、申请、续期、支付、申诉、行政负担 | 名义权利无法转化为食物、住房、医疗、能源或收入支持 |
| 社区资源可导航 | `community-resource-navigation/` | 资源目录、社会需求筛查、转介、闭环回访、人工协助 | 资源存在但找不到、转介失败、回访缺失或敏感需求数据被滥用 |
| 上游生活环境可支撑主体 | `social-determinants-community-vulnerability/` | 社会决定因素、社区脆弱性、环境正义、地方健康估计、食物可达、社会需求 | 把结构性风险写成个体失败，或用脆弱性指标支持排除、歧视和资源拒绝 |
| 公共服务可完成 | `public-service-design-accessibility/` | 公共服务设计、表单负担、客户体验、无障碍、人工帮助、反馈路径 | 名义服务无法完成，或用数字化替代人工帮助、无障碍和申诉责任 |
| 危机警报和求助入口可达 | `emergency-alerts-communications/` | 公共警报、WEA/EAS、天气广播、911/NG911、第一响应通信 | 警报不到达、通信失效、误报滥用、求助入口被绕过或官方系统被伪造 |
| 灾后恢复可连续 | `disaster-recovery-relief-continuity/` | 个人援助、恢复中心、临时安置、灾害贷款、救济导航、恢复时间 | 灾害后住房、资金、文件、医疗、食物和家庭连续性长期断裂 |
| 资源流通入口可持续 | `financial-inclusion-payment-systems/` | 账户、支付、汇款、数字金融服务、消费者保护、支付系统可靠性 | 收入、福利、救济和交易因账户、支付、费用或欺诈失败而断线 |
| 能力可转化为工作入口 | `workforce-employment-services/` | 就业服务、WIOA、学徒制、职业信息、再就业、合理便利 | 学习和能力无法转化为收入、社会角色、工作入口和长期任务窗口 |
| 家庭能桥接危机窗口 | `household-emergency-preparedness-resilience/` | 家庭计划、物资包、健康准备、备用通信、文件、特殊需求 | 公共救援抵达前食物、水、药物、通信、照护和文件断裂 |
| 公共知识入口可达 | `media-information-literacy-public-libraries/` | 信息素养、来源判断、公共图书馆、数字技能、社区学习 | 信息噪声、误导、数字排除和公共材料不可理解导致判断失败 |
| 健康服务有人力承载 | `health-workforce-capacity/` | 卫生人力供给、分布、训练、保留、负荷、技能组合 | 医学技术存在但等待、短缺、倦怠、误诊和照护断点增加 |
| 制度流程成本可承受 | `administrative-burden-procedural-friction/` | 学习成本、心理成本、合规成本、证明、等待、续期、申诉 | 名义权利被程序摩擦转化为申请放弃、资格断线和有效时间损耗 |
| 社区中介可连接服务 | `community-health-workers-peer-support/` | CHW、peer support、导航员、信任、文化适配、转介闭环 | 服务存在但不被信任、理解、坚持或反馈，恢复支持无法进入日常生活 |
| 公共系统可被观察 | `civic-data-open-government-transparency/` | 开放数据、公共记录、FOIA、绩效数据、元数据、问责反馈 | 公共资源分配、服务失败、腐败、歧视和治理缺口不可见 |
| 学习机会可持续 | `education-access-lifelong-learning/` | 教育可及、成人学习、再培训、基础技能、数字学习、技能迁移 | 长寿无法转化为能力复利，技能过时和技术排除扩大 |
| 未来技术窗口可生成 | `research-infrastructure-open-science-translation/` | 科研基础设施、开放科学、复现性、研究数据、资助、转化科学 | 研究不可复现、数据不可得、资助断裂和技术转化失败 |
| 技术测量可可信 | `standards-metrology-quality-infrastructure/` | 标准、计量、校准、认证、质量管理、合格评定、互操作 | 测量不可比、设备不可互通、质量不可审查和假合格风险 |
| 数字关键服务可恢复 | `cybersecurity-resilience-critical-services/` | 网络安全、事件响应、备份恢复、关键服务韧性、数字风险治理 | 医疗、金融、身份、公共服务和 AI 工具被攻击、勒索或中断 |
| AI 算力底座可用 | `compute-data-center-ai-infrastructure/` | 算力、数据中心、芯片、云、能源、水、网络、接入治理 | AI 和科学模拟能力集中、短缺、中断或被资源约束截断 |
| 医学发现可监管转化 | `clinical-trials-regulatory-science-translation/` | 临床试验、监管科学、真实世界证据、安全监测、批准路径 | 有前沿发现但人体证据不足、安全遗漏或监管转化失败 |
| 空间位置层可用 | `geospatial-navigation-location-infrastructure/` | 地理空间数据、地址、地图、GNSS/GPS、地理编码、应急位置、服务可达 | 人、资源、风险和服务不可定位，导致救援、配送、交通、转介和公共服务失败 |
| 天气气候风险可提前观测 | `weather-climate-observation-forecasting/` | 观测系统、预报模型、气候服务、极端天气、预警提前量、环境风险窗口 | 热、洪水、风暴、干旱、火灾天气或空气风险无法提前进入行动 |
| 栖居空间可保护生命 | `building-fire-life-safety-codes/` | 建筑规范、消防规范、疏散、烟雾报警、无障碍、结构韧性 | 居住、照护、学习、工作和公共空间成为火灾、烟雾、结构和疏散风险源 |
| 关键物质系统可制造修复 | `manufacturing-repair-capacity/` | 制造、维修、维护、备件、质量、本地生产、关键设备恢复 | 设备损坏、备件短缺、质量缺陷和生产能力不足导致服务与工具系统失效 |
| 公共预算可转化为服务 | `public-procurement-contracting-capacity/` | 公共采购、合同、供应商管理、应急采购、透明度、交付验收 | 有预算和政策但采购失败、合同失效、腐败、延误或劣质交付 |
| 动物-人类-环境界面可治理 | `animal-health-zoonotic-interface-one-health/` | 动物健康、兽医公共卫生、人兽共患病、食品动物、野生动物、One Health | 上游动物疾病、AMR、食品系统和生态界面风险穿透公共卫生屏障 |
| 风险可被实验室确认 | `public-health-laboratory-diagnostic-capacity/` | 公共卫生实验室、诊断网络、检测确认、质量管理、实验室扩容 | 不可见风险无法确认、检测延误、假阴性/假阳性或实验室容量崩溃 |
| 外部生物材料可安全供应 | `blood-organ-tissue-biovigilance-transplantation/` | 血液供应、输血安全、器官/组织捐献、移植体系、追踪、生物警戒 | 血液短缺、移植等待失败、感染/免疫风险、分配失衡或追踪失败 |
| 残余物和危险材料可治理 | `waste-management-hazardous-materials-continuity/` | 固体废物、医疗废物、危险废物、处理处置、服务连续性 | 废物堆积、污染扩散、感染入口、危险材料暴露或服务中断 |
| 不可见高能暴露可限制 | `radiation-nuclear-safety-protection/` | 辐射防护、核安全、辐射监测、放射性材料、应急治理 | 电离辐射暴露、污染、长期癌症风险、事故传播或恐慌治理失败 |
| 化学毒性暴露可响应 | `chemical-safety-poison-control-toxicology/` | 化学品安全、毒性暴露、毒物中心、毒理证据、风险沟通 | 急性中毒、慢性毒性、混合暴露、误判处置或化学事故扩散 |
| 未来技术物质输入可持续 | `critical-minerals-materials-resilience/` | 关键矿物、战略材料、加工依赖、替代、回收、供应韧性 | AI、能源、医疗设备、制造和通信因材料瓶颈不可及或不可维修 |
| 可呼吸环境可维持 | `air-quality-ventilation-exposure-control/` | 室内外空气质量、通风、过滤、气溶胶、烟雾、监测、风险沟通 | 空气污染、感染性气溶胶、烟雾或室内暴露持续侵蚀呼吸、认知和恢复能力 |
| 食物输入可安全 | `food-safety-contamination-control/` | 食源性病原体、毒素、过敏原、检查、追溯、召回、暴发治理 | 食物成为感染、毒性、过敏、信任崩溃和公共供餐中断入口 |
| 工作暴露可控制 | `occupational-exposure-industrial-hygiene/` | 工业卫生、暴露识别、控制层级、化学/物理/生物/噪声/热/粉尘风险 | 工作以长期疾病、感官损伤、呼吸损害、神经毒性或行动能力损耗换取收入 |
| 医疗设备可可靠运行 | `medical-device-equipment-safety-maintenance/` | 医疗器械、设备安全、UDI、不良事件、召回、维护、网络安全、可用性 | 诊断、治疗、监测、生命支持和康复工具因设备失效、误用、断供或攻击中断 |
| 照护环境感染屏障可运行 | `sterilization-disinfection-infection-control/` | 清洁、消毒、灭菌、再处理、环境感染控制、HAI 预防 | 医疗和照护场所把服务过程变成感染传播、耐药扩散和信任损失入口 |
| 物理空间可进入可使用 | `built-environment-accessibility-universal-design/` | 建成环境无障碍、通用设计、可达路径、公共设施、标识和撤离可达 | 身体、感官、认知或照护状态变化后无法进入、移动、使用服务或参与社会 |
| 个体诊断观测可可信 | `clinical-laboratory-diagnostic-quality/` | 临床实验室质量、检测准确性、能力验证、诊断管理、临床效用 | 检测误差、诊断延误、假阳性/假阴性或不可比结果污染治疗与预测路径 |
| 药品真实世界安全可反馈 | `pharmacovigilance-drug-safety-monitoring/` | 不良事件报告、上市后安全、标签更新、REMS、用药错误、风险沟通 | 治疗在真实世界中产生未识别伤害、相互作用、用药错误或信任崩溃 |
| 药品质量和供应完整性可审查 | `pharmaceutical-quality-supply-integrity/` | GMP、质量缺陷、污染、假劣药、短缺、冷链、追溯、召回 | 药物可及但质量失败、污染、假劣、断供或不可追溯，导致治疗失败和毒性风险 |
| 急性可逆窗口可接入 | `emergency-medical-services-prehospital-care/` | EMS、调度、响应时间、院前照护、转运、质量改进 | 创伤、心脏骤停、卒中或呼吸急症未在可逆窗口内进入医疗系统 |
| 高风险修复通道可安全执行 | `surgical-anesthesia-perioperative-safety/` | 手术安全、麻醉安全、团队检查、围手术期监测、并发症预防 | 修复性干预因可预防错误、感染、出血、麻醉风险或团队失效变成新伤害 |
| 移动过程可避免严重伤害 | `road-traffic-injury-prevention-safe-mobility/` | 道路安全系统、速度管理、车辆安全、执法公平、交通伤害监测 | 出行过程制造死亡、严重伤害、长期失能、家庭收入中断和照护负担 |
| 地理距离不能排除主体 | `rural-health-access-geographic-equity/` | 农村服务密度、距离、交通、宽带、卫生人力、药房/医院可达 | 可修复风险因地点、距离、宽带、人力和设施稀缺被延误或放弃 |
| 住所缺失时服务不能断线 | `homelessness-unsheltered-health-continuity/` | 庇护、外展、卫生、睡眠、安全、身份、住房服务、医疗连续性 | 露宿、卫生缺失、暴露、创伤、慢病失控和服务断点把主体推出恢复路径 |
| 制度转换不能切断健康连续性 | `correctional-health-reentry-continuity/` | 羁押健康、释放转介、药物、慢病、心理、感染、身份、住房、福利 | 释放后药物中断、过量死亡、复发、无家可归、感染失访和社会连接断裂 |
| 功能状态变化后仍能自主生活 | `disability-services-independent-living/` | HCBS、独立生活、个人协助、合理便利、辅助技术、无障碍、社区融合 | 机构化、照护中断、孤立、公共服务排除和主体自主性下降 |
| 认知退行时主体仍被保护 | `dementia-cognitive-decline-care-continuity/` | 认知衰退、照护计划、照护者负担、记忆/判断支持、安全、尊严 | 用药、财务、居住、安全和照护风险失控，导致主体失权和危机迁移 |
| 长疗程感染照护可连续 | `chronic-infectious-disease-care-continuity/` | HIV、结核、病毒性肝炎、治疗连续性、耐药、隐私、去污名、随访 | 失访、耐药、器官损伤、传播、污名和公共卫生屏障失效 |
| 急性自毁风险可被接住 | `suicide-crisis-response-continuity/` | 危机热线、移动危机响应、危机稳定、急诊衔接、随访、恢复支持 | 自伤或自杀风险在孤立、延误、错误处置和断裂随访中清零未来选择权 |
| 成瘾恢复可连续 | `substance-use-treatment-recovery-continuity/` | 治疗入口、恢复支持、同伴支持、过量预防、减害治理、服务保留 | 过量、复发、污名、刑事化、住房断裂和服务断点持续侵蚀主体控制权 |
| 脆弱成年人可被保护 | `elder-justice-adult-protective-services/` | 成人保护、老年虐待、财务剥削、照护忽视、长期照护监察、保护转介 | 虐待、忽视、财务控制、社会隔离和权利剥夺把长寿转化为更长受害窗口 |
| 儿童安全可支撑未来主体 | `child-protection-family-safety/` | 儿童虐待忽视、ACEs、儿童福利、家庭支持、创伤知情服务 | 早期创伤、家庭失稳、剥削和制度误伤破坏未来主体能力形成 |
| 欺诈不能夺走资源入口 | `fraud-scams-consumer-protection/` | 诈骗识别、身份盗用恢复、投诉举报、消费者保护、风险沟通 | 资金、身份、账号、信用、信任和公共服务入口被欺诈系统性夺走 |
| 数字空间可安全参与 | `online-safety-digital-harm-prevention/` | 网络霸凌、在线骚扰、数字虐待、儿童在线保护、平台求助、恢复路径 | 数字入口变成胁迫、剥削、羞辱、心理伤害和身份风险源 |
| 低概率复杂疾病路径可被识别 | `rare-disease-diagnostic-odyssey-care-coordination/` | 罕见病、未确诊疾病、诊断漫游、专家网络、患者登记、孤儿药路径 | 误诊、延误、重复检查、研究窗口错失和家庭负担把可修复机会推迟到不可逆阶段 |
| 多疾病多药物可被统一协调 | `multimorbidity-polypharmacy-care-coordination/` | 多病共存、多重用药、药物重整、治疗负担、跨专科照护计划 | 指南叠加、冲突处方、相互作用、处方级联和治疗负担侵蚀功能状态 |
| 出院和照护转移不能断线 | `care-transitions-discharge-continuity/` | 出院计划、交接、用药重整、复诊、转诊、再入院、闭环随访 | 离开医院后信息、责任、药物和随访断裂，恢复窗口被浪费 |
| 严重疾病可被居家和缓和系统接住 | `home-health-hospice-palliative-care-continuity/` | 居家医疗、缓和医疗、安宁疗护、症状负担、目标照护、照护者支持 | 长寿退化为不可承受痛苦、照护者崩溃、目标失配和尊严丧失 |
| 临床语言和文化接口可理解 | `medical-interpreter-cultural-mediation/` | 医疗解释、语言协助、CLAS、LEP、文化中介、同意理解 | 风险、同意、治疗和随访信息失真，导致误诊、误用药、失访和权利失效 |
| 主体偏好能进入医疗决策 | `patient-advocacy-shared-decision-making/` | 患者倡导、共同决策、决策辅助、主体偏好、治疗负担、知情同意 | 信息不对称、被动同意、目标不匹配和治疗负担让医疗路径偏离主体未来选择权 |
| 主体历史可长期保存 | `life-logging-personal-archives-continuity/` | 生命日志、个人档案、元数据、备份、迁移、长期可读性 | 病史、作品、偏好、证据链和项目上下文丢失，长期主体解释能力下降 |
| 数字资产和权限可交接 | `digital-legacy-data-succession/` | 数字遗产、账号继承、受托访问、失能代理、资料交接 | 失能、死亡或账号丢失时资料、权益、作品和长期项目断裂或被滥用 |
| 主体状态可连续观测 | `wearables-continuous-sensing-personal-informatics/` | 可穿戴、连续监测、自我追踪、远程数据采集、反馈闭环 | 风险偏移、恢复不足和行为反馈不可见，主体只能在损害显性化后反应 |
| 认知上下文可外部承载 | `personal-knowledge-management-cognitive-offloading/` | 外部记忆、笔记、检索、知识库、AI 助手、项目上下文恢复 | 工作记忆负担、重复解释、知识丢失和项目重启成本侵蚀创造密度 |
| 神经接口可被安全治理 | `brain-computer-interface-neurotechnology-governance/` | BCI、神经记录、刺激、解码、神经数据、设备安全、神经伦理 | 高带宽接口变成神经数据滥用、身份边界混乱、不可逆设备风险和强制控制 |
| 物理行动可被具身辅助 | `robotics-embodied-assistance-care-automation/` | 机器人、外骨骼、家庭辅助、康复机器人、照护自动化 | 能力下降后移动、操作、康复和日常照护负担失控，独立生活窗口缩短 |
| 高成本风险可分摊 | `insurance-risk-transfer/` | 覆盖率、保费、自付、理赔、拒赔、风险池、保障缺口 | 疾病、失业、工伤、残障、灾害或养老金风险由个体独自承担 |
| 托育和家庭运行可持续 | `childcare-family-continuity/` | 托育可及、费用、质量、早期发展、父母工作连续性、家庭压力 | 儿童发展受损、照护者工作中断、时间贫困和家庭压力升级 |
| 应急响应可接住主体 | `emergency-preparedness-response/` | 灾害准备、预警、应急通信、急救医疗、安置、公共卫生应急、恢复 | 低频高冲击事件一次性清零长期积累，通信、医疗、撤离或恢复失败 |
| 人身安全可保护 | `personal-safety-violence-prevention/` | 暴力暴露、求助入口、受害者服务、法律保护、创伤支持、住房安全 | 暴力、胁迫、跟踪、犯罪伤害和创伤直接截断生命、行动能力和未来选择权 |
| 缺陷产品可发现和召回 | `product-safety-recall-systems/` | 缺陷报告、不良事件、投诉、召回覆盖、通知到达、纠正、替代路径 | 缺陷产品持续使用，导致伤害、医疗中断、交通风险和家庭安全风险 |
| 关键供应链可连续 | `supply-chain-continuity/` | 药品、能源、食物、设备、通信、物流 | 断供、单点故障、替代失败 |
| 生物技术双重用途可治理 | `synthetic-biology-biosecurity/` | 生物安全、生物安保、双重用途、治理 | 病原风险、误用、实验外泄 |
| 极端环境可栖居 | `space-extreme-habitation/` | 辐射、微重力、隔离、闭环生命支持 | 环境失效、资源闭环失败、远程医疗失败 |
| 关系网络可支撑主体 | `social-connection-relational-infra/` | 社会连接、孤独、照护网络、信任、协作 | 孤立、照护断裂、危机无人接住 |
| 权利和治理可保护主体 | `governance-rights/` | 同意、退出、数据权、法律身份 | 被控制、被剥夺、被系统吞噬 |
| 服务入口可理解可导航 | `health-literacy-navigation/` | 健康素养、服务导航、风险沟通、共同决策 | 有资源但不会用、误解、延误、行政排除 |
| 语言和表达可理解 | `language-access-plain-communication/` | plain language、语言服务、LEP、CLAS、认知可访问性、表单理解 | 材料读不懂、听不懂、不能执行，或简化时删掉权利和风险 |
| 口腔系统可持续 | `oral-health-continuity/` | 咀嚼、牙周、口腔疼痛、感染、沟通 | 营养障碍、疼痛、感染、社交退缩 |
| 持续存在可承受 | `pain-suffering-control/` | 疼痛、症状负担、生活质量、尊严 | 延长痛苦、有效时间崩塌、退出权受损 |
| 状态可观测和校正 | `measurement-feedback/` | 测量、预测、反馈、风险评分 | 错误预测、偏差、指标替代真实终点 |

## 主链路

```text
有效永生 / 主体持续性最大化
  -> 生物基底维护
  -> 神经与身份连续
  -> 时间窗口延展
  -> 认知与工具增强
  -> 风险函数压低
  -> 资源环境支撑
  -> 外部技术底座可控
  -> 制度治理保护
  -> 测量、预测与反馈
  -> 各研究域通过证据、模型和治理进入同一个主体持续性系统
```

## 组合关系

```text
cellular-reprogramming
  -> genomic-stability-dna-repair
  -> telomere-maintenance
  -> proteostasis-autophagy
  -> mitochondrial-bioenergetics
  -> cellular-senescence-clearance
  -> extracellular-matrix-glycation
  -> stem-cell-reserve-renewal
  -> regenerative-medicine
  -> gastrointestinal-barrier-absorption
  -> respiratory-oxygenation
  -> blood-oxygen-hemostasis
  -> endocrine-hormonal-regulation
  -> lymphatic-glymphatic-clearance
  -> fluid-electrolyte-acid-base-homeostasis
  -> thermal-homeostasis-resilience
  -> nutrition-metabolic-health
  -> physical-activity-mobility
  -> cardiovascular-resilience
  -> musculoskeletal-integrity
  -> skin-barrier-wound-healing
  -> urogenital-continuity
  -> reproductive-fertility-continuity
  -> attention-executive-control
  -> learning-skill-acquisition
  -> time-allocation-effective-time
  -> rehabilitation-functioning
  -> cancer-control
  -> immune-maintenance
  -> microbiome-ecology
  -> renal-hepatic-clearance
  -> antimicrobial-resilience
```

这组关系处理“身体能否被修复且不失控”。

```text
neuro-continuity
  -> sensory-continuity
  -> memory-editing
  -> cognitive-augmentation
  -> ai-agency-safety
  -> digital-identity-security
  -> disembodied-cns
```

这组关系处理“延续的是否仍是同一个主体”。

```text
future-waiting
  -> biostasis-cryopreservation
  -> measurement-feedback
```

这组关系处理“等待未来时如何降低自身时间成本和损耗成本”。

```text
risk-engineering
  -> planetary-health-environment
  -> resource-social-infra
  -> food-security-nutrition-access
  -> water-sanitation-hygiene-continuity
  -> energy-access-resilience
  -> healthcare-access-continuity
  -> medicine-access-treatment-continuity
  -> patient-data-interoperability
  -> telehealth-remote-monitoring-access
  -> health-data-privacy-governance
  -> functioning-quality-of-life-outcomes
  -> health-economics-value-assessment
  -> immunization-public-health-surveillance
  -> maternal-newborn-child-development
  -> patient-safety-organizational-learning
  -> caregiving-long-term-care
  -> housing-built-environment-stability
  -> transportation-access-mobility
  -> legal-identity-civil-registration
  -> access-to-justice-legal-aid
  -> civic-participation-election-access
  -> migration-displacement-humanitarian-continuity
  -> digital-inclusion-connectivity
  -> social-protection-benefits-delivery
  -> community-resource-navigation
  -> social-determinants-community-vulnerability
  -> public-service-design-accessibility
  -> emergency-alerts-communications
  -> disaster-recovery-relief-continuity
  -> financial-inclusion-payment-systems
  -> workforce-employment-services
  -> household-emergency-preparedness-resilience
  -> media-information-literacy-public-libraries
  -> health-workforce-capacity
  -> administrative-burden-procedural-friction
  -> community-health-workers-peer-support
  -> civic-data-open-government-transparency
  -> education-access-lifelong-learning
  -> research-infrastructure-open-science-translation
  -> standards-metrology-quality-infrastructure
  -> cybersecurity-resilience-critical-services
  -> compute-data-center-ai-infrastructure
  -> clinical-trials-regulatory-science-translation
  -> geospatial-navigation-location-infrastructure
  -> weather-climate-observation-forecasting
  -> building-fire-life-safety-codes
  -> manufacturing-repair-capacity
  -> public-procurement-contracting-capacity
  -> animal-health-zoonotic-interface-one-health
  -> public-health-laboratory-diagnostic-capacity
  -> blood-organ-tissue-biovigilance-transplantation
  -> waste-management-hazardous-materials-continuity
  -> radiation-nuclear-safety-protection
  -> chemical-safety-poison-control-toxicology
  -> critical-minerals-materials-resilience
  -> air-quality-ventilation-exposure-control
  -> food-safety-contamination-control
  -> occupational-exposure-industrial-hygiene
  -> medical-device-equipment-safety-maintenance
  -> sterilization-disinfection-infection-control
  -> built-environment-accessibility-universal-design
  -> clinical-laboratory-diagnostic-quality
  -> pharmacovigilance-drug-safety-monitoring
  -> pharmaceutical-quality-supply-integrity
  -> emergency-medical-services-prehospital-care
  -> surgical-anesthesia-perioperative-safety
  -> road-traffic-injury-prevention-safe-mobility
  -> rural-health-access-geographic-equity
  -> homelessness-unsheltered-health-continuity
  -> correctional-health-reentry-continuity
  -> disability-services-independent-living
  -> dementia-cognitive-decline-care-continuity
  -> chronic-infectious-disease-care-continuity
  -> suicide-crisis-response-continuity
  -> substance-use-treatment-recovery-continuity
  -> elder-justice-adult-protective-services
  -> child-protection-family-safety
  -> fraud-scams-consumer-protection
  -> online-safety-digital-harm-prevention
  -> rare-disease-diagnostic-odyssey-care-coordination
  -> multimorbidity-polypharmacy-care-coordination
  -> care-transitions-discharge-continuity
  -> home-health-hospice-palliative-care-continuity
  -> medical-interpreter-cultural-mediation
  -> patient-advocacy-shared-decision-making
  -> life-logging-personal-archives-continuity
  -> digital-legacy-data-succession
  -> wearables-continuous-sensing-personal-informatics
  -> personal-knowledge-management-cognitive-offloading
  -> brain-computer-interface-neurotechnology-governance
  -> robotics-embodied-assistance-care-automation
  -> insurance-risk-transfer
  -> childcare-family-continuity
  -> emergency-preparedness-response
  -> personal-safety-violence-prevention
  -> product-safety-recall-systems
  -> financial-resilience-access
  -> occupational-work-design
  -> labor-rights-workplace-protection
  -> information-integrity-trust
  -> supply-chain-continuity
  -> synthetic-biology-biosecurity
  -> space-extreme-habitation
  -> social-connection-relational-infra
  -> health-literacy-navigation
  -> language-access-plain-communication
  -> substance-exposure-control
  -> assistive-technology-access
  -> governance-rights
```

这组关系处理“主体如何避免被外部环境、制度和尾部风险截断”。

```text
mental-health-affective-stability
  -> sleep-circadian-recovery
  -> attention-executive-control
  -> learning-skill-acquisition
  -> time-allocation-effective-time
  -> pain-suffering-control
  -> oral-health-continuity
  -> rehabilitation-functioning
```

这组关系处理“存在时间如何转化为可承受、可恢复、可行动的有效时间”。

## 使用规则

- 新材料先进入对应研究域；跨域原则进入 `docs/`。
- 不确定归属时，先看它主要改变身体、神经、时间、认知、风险、资源、治理还是测量。
- 一项技术可被多个域引用，但只能有一个主拥有域。
- 不因概念传播性强就建域；必须满足独立机制、证据、失败模式和伦理边界。
- 高风险域只写边界、证据和治理，不写可执行人体操作。
