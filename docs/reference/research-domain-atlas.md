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
  -> 感官、沟通、摄食和具身反馈必须保持可用
  -> 行星、地球物理与极端热风险必须可被观测、预警、缓解和恢复
  -> 慢性环境暴露必须被识别、降低并纳入恢复成本
  -> 失能或不能表达时，意愿、权限、资源和责任必须可连续
  -> 进入金融、住房、工作、保险和福利系统前，准入判定必须可观察、可纠错、可申诉
  -> 学习、技能、授权和合规状态必须可被长期证明、核验、携带和恢复
  -> 家庭事实、生命事件、姓名、地址、监护和儿童安置关系必须可被制度持续识别
  -> 工具和认知系统必须放大主体而不是吞噬主体
  -> 家庭物理操作系统必须让住所、食物、卫生、物品、投递和维修可连续
  -> 个人移动执行系统必须让车辆、补能、停车、主动出行、辅助交通、按需交通、支付账户和实时导向可连续
  -> 公共空间生存接入系统必须让离家后的如厕、补水、休息降温、避难、连接、绿地恢复和无障碍服务可连续
  -> 食物获得执行系统必须让日常采购、福利兑换、社区发放、灾害供餐、送餐服务、婴儿配方和外部熟食可连续
  -> 治疗获得执行系统必须让处方、药品福利、用药核对、药品信息、未用药处置、DME、氧疗和糖尿病耗材可连续
  -> 门诊访问执行系统必须让 provider 名录、初级照护、专科转诊、预约、检验、影像、门诊操作和非工作时间入口可连续
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
| 遗传状态可被安全改写 | `gene-therapy-genome-editing-delivery-safety/` | 基因治疗、基因编辑、递送载体、表达控制、脱靶和长期随访 | 编辑错误、递送失败、免疫反应、脱靶和长期风险把高杠杆干预转成新风险 |
| 衰老指标必须被验证 | `biological-age-clocks-biomarker-validation/` | 表观遗传年龄钟、组学年龄、功能年龄、衰老 biomarker 和替代终点 | 指标与真实终点错配，导致伪优化、错误干预和寿命叙事外推 |
| 主体状态必须可多层观测 | `multiomics-personal-baseline-systems-biology/` | 基因组、表观组、转录组、蛋白组、代谢组、微生物组和个人基线 | 单一指标看不到系统状态，模型误判个体差异、风险轨迹和干预反应 |
| 细胞可作为治疗平台 | `engineered-cell-therapy-regenerative-platforms/` | CAR-T、TCR-T、TIL、NK、iPSC 衍生细胞、可编程细胞和安全开关 | 活体药物扩增失控、脱靶、毒性、制造失败或长期恶性风险 |
| 人体相关模型必须降低试错成本 | `organoids-organ-on-chip-disease-models/` | 类器官、organ-on-chip、组织芯片、患者来源模型和替代方法 | 模型失真导致候选干预错误进入或退出临床，或把体外信号外推成人体疗效 |
| 器官失败必须有替换路径 | `xenotransplantation-bioengineered-organ-replacement/` | 异种移植、工程器官、器官保存灌注、器官供给和移植平台风险 | 器官衰竭、供给不足、免疫排斥、感染和长期功能失败直接截断生命路径 |
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
| 视觉输入必须可持续 | `vision-eye-health-continuity/` | 视力、眼病、视觉功能、低视力支持、视觉任务参与 | 阅读、移动、工作、照护和环境反馈被视觉损失压缩 |
| 听觉沟通必须可持续 | `hearing-auditory-communication-continuity/` | 听力、言语识别、助听支持、耳鸣、沟通疲劳 | 沟通失败、孤立、认知负担和安全警报漏接 |
| 空间定向和平衡必须稳定 | `vestibular-balance-spatial-orientation/` | 前庭、眩晕、平衡、空间定向、跌倒、移动信心 | 跌倒、移动恐惧、外出减少和行动半径收缩 |
| 语言表达与理解必须可达 | `speech-language-communication-continuity/` | 失语、构音、言语运动、沟通参与、替代沟通 | 主体偏好、同意、关系和社会角色无法表达 |
| 吞咽必须保护气道和营养 | `swallowing-dysphagia-aspiration-nutrition/` | 吞咽安全、误吸、营养水分、饮食尊严 | 进食从恢复输入变成窒息、肺炎、营养不足和尊严损害 |
| 化学感知必须支撑安全与食欲 | `smell-taste-chemosensory-continuity/` | 嗅觉、味觉、气味危险信号、食欲、营养 | 烟气、燃气、腐败食品识别下降，食欲、生活质量和营养受损 |
| 躯体感觉必须反馈身体边界 | `peripheral-neuropathy-somatosensory-continuity/` | 周围神经、触觉、痛觉、本体感觉、足部风险 | 损伤不可感、步态不稳、跌倒、溃疡和精细操作反馈丧失 |
| 记忆可审查地处理 | `memory-editing/` | 记忆痕迹、人格连续性、同意 | 操控、伪记忆、不可逆损伤 |
| 中枢可外部维持 | `disembodied-cns/` | 神经维持、生命支持、接口闭环 | 去主体化、控制失效、生命支持失败 |
| 等待成本可压缩 | `future-waiting/` | 主观时间、相对时间、未来窗口 | 退出失败、连续性失败、工程风险 |
| 损耗可暂停 | `biostasis-cryopreservation/` | 结构保存、代谢降低、未来修复机会 | 不可逆损坏、复温失败、复活外推 |
| 认知与行动可放大 | `cognitive-augmentation/` | 学习、判断、记忆外化、工具能力 | 依赖、失控、主体自主性下降 |
| AI 代理可受控 | `ai-agency-safety/` | AI 代理、授权、工具调用、监督、审计 | 代理越权、误导、泄露、不可逆行动 |
| 数字身份可恢复 | `digital-identity-security/` | 账号、凭据、身份恢复、服务入口 | 身份盗用、账号丢失、服务断线 |
| 心理和动机系统可稳定 | `mental-health-affective-stability/` | 情绪稳定、压力恢复、动机、自杀风险 | 自伤、成瘾、行动崩塌、关系断裂 |
| 动机能量必须可持续 | `depression-mood-disorder-functioning-continuity/` | 抑郁、心境低落、快感缺失、动机衰退、功能损害 | 时间存在但无法转化为行动、关系和长期目标推进 |
| 威胁系统必须可调节 | `anxiety-stress-threat-regulation-continuity/` | 焦虑、压力、威胁感知、回避、惊恐 | 持续威胁监测吞噬注意力、睡眠、判断和恢复 |
| 创伤后必须能重新进入未来 | `trauma-ptsd-adversity-recovery-continuity/` | PTSD、逆境、再创伤、安全感、记忆触发 | 过去风险持续支配身体、关系和服务接入 |
| 现实检验必须被社区承接 | `psychosis-reality-testing-community-continuity/` | 精神病性体验、现实检验、社区支持、权利保护 | 感知解释失稳导致住房、医疗、关系和权利断裂 |
| 情绪周期必须保护长期资产 | `bipolar-mood-episode-stability-continuity/` | 躁狂/轻躁狂、抑郁发作、节律、冲动风险 | 周期性波动反复清空关系、财务、学习和工作进展 |
| 执行功能必须能转化目标 | `adhd-executive-function-neurodevelopment-continuity/` | ADHD、注意、冲动、时间感、任务启动 | 目标无法稳定启动、维持和完成，行动密度被长期压低 |
| 神经多样性必须被环境支持 | `autism-neurodiversity-support-continuity/` | 自闭谱系、感官差异、沟通、例行、支持需求 | 不适配环境造成过载、排除和尊严损伤 |
| 身体供能和身体信任必须稳定 | `eating-disorders-nutrition-body-continuity/` | 进食障碍、身体形象、限制/暴食/补偿、营养风险 | 身体供能、认知、心血管、电解质和身份安全同步受损 |
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
| 空间天气风险必须可治理 | `space-weather-geomagnetic-storm-resilience/` | 太阳活动、地磁暴、电网、卫星、通信、导航、时间同步 | 电力、卫星、通信、定位、金融和医疗等关键系统被太阳活动级联扰动 |
| 行星撞击尾部风险必须可监测 | `planetary-defense-near-earth-object-risk/` | 近地天体、轨道监测、撞击概率、预警、偏转、国际协调 | 低概率高后果撞击破坏生态、基础设施、食物系统和社会秩序 |
| 火山灰地质风险必须可缓解 | `volcanic-ashfall-geohazard-continuity/` | 火山喷发、火山灰、空气、水、农业、航空、建筑、设备 | 火山灰把空气、水、交通、食物和设备系统同时拖入恢复压力 |
| 地震建成环境风险必须可承受 | `earthquake-seismic-risk-built-environment-continuity/` | 地震危险性、抗震建筑、医院、道路、水电燃气、通信、恢复 | 建筑和生命线基础设施在短时间内转化为死亡、创伤和服务断点 |
| 海啸短窗口撤离必须闭环 | `tsunami-warning-coastal-evacuation-continuity/` | 海啸监测、警报、沿海撤离、垂直避难、无障碍、灾后恢复 | 警报、理解、撤离、避难或恢复任一断裂都会放大沿海死亡和失能风险 |
| 极端高温必须被制冷和公共卫生接住 | `extreme-heat-cooling-public-health-continuity/` | 热健康、制冷可及、能源负担、住房质量、劳动暴露、城市热岛 | 高温通过体温调节失败、睡眠破坏、劳动暴露、停电和住房质量压缩有效时间 |
| 声环境必须不持续损耗恢复 | `noise-exposure-acoustic-environment-continuity/` | 交通噪声、职业噪声、社区噪声、听力、睡眠、沟通、压力负荷 | 噪声长期破坏睡眠、听觉、注意力、沟通和心血管压力恢复 |
| 光照节律必须可同步 | `light-exposure-circadian-environment-continuity/` | 自然光、夜间光、室内照明、轮班、光污染、睡眠时相 | 节律错配让睡眠、警觉、代谢、情绪和有效时间持续失稳 |
| 重金属暴露必须被切断 | `lead-heavy-metal-exposure-control/` | 铅、汞、镉、砷、住房、饮水、土壤、粉尘、职业和产品暴露 | 神经毒性、儿童发育损伤、肾血液系统负担和认知资本损耗 |
| 建筑遗留危害必须可识别 | `radon-asbestos-indoor-hazard-continuity/` | 氡、石棉、旧建筑、学校、工作场所、长期肺部风险 | 看不见的室内暴露通过长潜伏期肺部和癌症风险侵蚀健康寿命 |
| 潮湿生物暴露必须被治理 | `mold-dampness-indoor-biological-exposure/` | 霉菌、潮湿、漏水、室内过敏原、灾后水损、住房质量 | 住房变成呼吸、免疫、睡眠和心理压力的持续暴露源 |
| 病媒传播风险必须被环境控制接住 | `vector-borne-disease-environmental-control/` | 蚊媒、蜱媒、气候水文、动物宿主、住房环境、病媒控制 | 感染风险重新定价居住、工作、旅行、农业和公共卫生连续性 |
| 医疗偏好必须可在失能时传递 | `advance-care-planning-medical-decision-continuity/` | advance directives、health care proxy、治疗目标、偏好沟通 | 主体无法表达时，医疗团队和家属只能猜测偏好，导致过度、过少或错位治疗 |
| 决策能力变化后权利必须被支持 | `supported-decision-making-guardianship-rights/` | 支持性决策、监护、最低限制替代、权利监督 | 保护安排可能变成失权、隔离、控制和剥夺主体参与 |
| 医疗信息访问必须在授权边界内连续 | `healthcare-personal-representative-hipaa-access-continuity/` | HIPAA personal representative、照护者访问、医疗记录、隐私边界 | 没有授权访问会让药物、结果、预约和转诊断裂；越权访问会侵蚀隐私 |
| 财务任务必须可被受托代办且防剥削 | `financial-fiduciary-power-of-attorney-continuity/` | financial power of attorney、fiduciary duty、账单、资产、记录 | 失能后住房、保险、照护和支付可能断线，或被代理人滥用资源 |
| 公共福利收入必须在能力下降时仍服务主体 | `representative-payee-benefits-management-continuity/` | representative payee、VA fiduciary、福利代管、报告和监督 | 底线收入可能被挪用、浪费、断供或无法转化为住房、食物和医疗 |
| 事务和长期项目必须在失能/死亡边界可交接 | `trust-estate-affairs-succession-continuity/` | 事务整理、受益人、trustee、executor、账户文件、项目交接 | 资源、资料、责任和项目被冻结、丢失、争议化或无法继续服务主体意图 |
| 信用与消费者报告必须可纠错 | `credit-consumer-reporting-access-continuity/` | 信用报告、消费者报告、specialty reports、身份错误、争议更正 | 错误报告把过去或他人记录转成金融、住房、就业和保险入口的错误排除 |
| 租房筛查必须不把住房入口黑箱化 | `tenant-screening-rental-access-continuity/` | 租客报告、驱逐记录、租金历史、收入验证、租赁平台筛查 | 主体因记录错误、模型误判或不可解释筛查失去住房、睡眠、恢复和工作底座 |
| 背景记录筛查必须可解释且可更正 | `background-check-record-screening-continuity/` | 犯罪记录、身份匹配、教育/执照核验、不利行动、记录准确性 | 错误匹配、陈旧记录或不可纠错记录把主体排除在工作、住房、照护和教育之外 |
| 算法招聘必须不切断就业入口 | `employment-algorithmic-hiring-screening-continuity/` | 自动简历筛选、就业测评、视频面试评分、job matching、合理便利 | 自动筛选把能力、收入、保险、学习机会和社会参与入口错误关闭 |
| 保险算法评分必须可治理 | `insurance-underwriting-algorithmic-risk-scoring-continuity/` | 承保、风险评分、外部数据、费率、索赔自动化、模型治理 | 风险池入口因不可解释评分、外部数据错误或自动化拒赔而失效 |
| 福利资格自动判定必须保留人工复核 | `public-benefits-eligibility-automated-decision-continuity/` | eligibility、数据匹配、续期、终止、申诉、人工复核 | 自动终止、错配、证明负担或无法复核让食物、医疗、住房、能源和现金缓冲断线 |
| 学习历史必须可核验可携带 | `education-record-transcript-verification-continuity/` | 教育记录、成绩单、学籍、学历、访问更正、授权披露 | 记录丢失、错误或不可核验让学习历史无法进入升学、就业、执照和服务系统 |
| 专业授权必须可持续 | `professional-licensure-certification-continuity/` | 职业执照、专业认证、注册资格、续证、惩戒、恢复、互认 | 资格失效、不可携带或监管黑箱把主体排除在高信任职业和公共服务之外 |
| 真实能力必须能被准确表达 | `skills-competency-credentialing-continuity/` | 技能本体、胜任力框架、微证书、数字徽章、作品证据、测评 | 技能定义失真、评估偏差或平台锁定让主体能力被低估、误配或不可迁移 |
| 职业能力必须持续更新 | `continuing-education-recertification-continuity/` | 继续教育、CPD、CEU/CME、再认证、续证、能力维护、合规记录 | 长寿命职业周期中知识过时、记录断裂或续证负担过高导致授权和收入中断 |
| 工作时间必须能转化为技能资产 | `apprenticeship-work-based-learning-continuity/` | 注册学徒、在岗训练、导师制、工时记录、技能标准、结业证明 | 工作中学习退化为不可携带廉价劳动，经验无法沉淀为资格和未来选择权 |
| 凭证必须可机器核验且可恢复 | `verifiable-credential-wallet-interoperability/` | 可验证凭证、数字钱包、DID、签发验证、撤销、选择性披露、恢复 | 钱包、密钥、撤销状态或信任注册表失效让身份、资格和授权证明断线 |
| 劳动收入必须可被制度承认 | `income-payroll-employment-record-continuity/` | 工资、工时、薪资单、雇佣证明、收入核验、记录纠错 | 工资雇佣记录缺失或错误让收入证明、福利资格、信用、租房和退休权益断线 |
| 纳税记录必须可访问可纠错 | `tax-administration-filing-record-continuity/` | 税务申报、tax transcripts、纳税人身份、扣缴、退税抵免、账户纠错 | 税务账号错误、身份盗用或记录不可访问阻断退税、公共服务、资助和资格核验 |
| 缴费历史必须转化为社会保障 | `social-security-earnings-benefit-record-continuity/` | 收入记录、工作 credits、福利声明、退休、残障、遗属、记录更正 | 漏报、身份错配或账户不可访问削弱老年、失能和家庭风险边界的基本保障 |
| 工作期资源必须延续到退休期 | `retirement-pension-savings-plan-continuity/` | 养老金、401(k)、IRA、rollover、vesting、受益人、丢失账户、计划终止 | 账户遗失、计划终止、受益人错误或转移失败削弱劳动退出后的资源连续性 |
| 失业冲击必须可被工资记录接住 | `unemployment-insurance-wage-record-continuity/` | UI wage records、基期、雇主报送、资格判定、申诉、overpayment、欺诈防控 | 工资记录错配、身份盗用、申诉困难或支付延迟放大失业对住房、健康和学习窗口的冲击 |
| 工作伤害必须转化为恢复支持 | `workers-compensation-occupational-injury-benefit-continuity/` | 工伤、职业病、伤害记录、医疗给付、工资替代、复工、OSHA 记录 | 报告缺失、记录争议或复工压力把工作伤害转成长期失能和收入断裂 |
| 家庭医疗事件不能自动切断工作角色 | `family-medical-leave-job-protection-continuity/` | 家庭医疗假、严重健康状况、照护假、军属照护、岗位保护、反报复、复工入口 | 疾病或照护责任直接导致岗位、保险、收入和职业身份断裂 |
| 疾病与照护窗口必须有工资替代 | `paid-sick-family-leave-wage-replacement-continuity/` | 带薪病假、带薪家庭假、带薪医疗假、替代率、等待期、公共/雇主计划 | 名义休假存在但无法负担，主体被迫带病工作、治疗中断或退出工作 |
| 孕产育儿不能被排除出工作系统 | `pregnancy-parental-work-continuity/` | 怀孕便利、分娩恢复、父母假、哺乳/泵奶支持、育儿责任、反歧视 | 生育和育儿责任被转化为职业惩罚、收入下降和长期工作轨迹中断 |
| 能力变化必须能被合理便利和复工路径接住 | `workplace-accommodation-return-to-work-continuity/` | 合理便利、interactive process、modified duty、phased return、工作能力、辅助技术 | 工作系统只有完全可用/完全退出两种状态，能力变化被永久化为失业或失能 |
| 残障收入与工作能力必须可连续治理 | `disability-income-work-capacity-benefit-continuity/` | SSDI、SSI、残障收入、工作 credits、工作能力、复工激励、福利悬崖 | 长期功能受限后现金流、医疗覆盖、复工试探和未来选择权同时断裂 |
| 家庭照护者不能被照护责任耗尽退出系统 | `family-caregiver-respite-work-continuity/` | 家庭照护者支持、respite care、照护培训、工作灵活性、照护者健康、负担 | 家庭照护被当作无限免费资源，照护者失去健康、收入、睡眠、社交和职业角色 |
| 生命事件必须成为可核验身份锚点 | `vital-records-life-event-continuity/` | 出生、死亡、婚姻、离婚、认证副本、记录更正、生命统计 | 生命事件记录缺失、错误或不可访问让身份、亲属关系、服务资格和权益交接断线 |
| 姓名变化必须跨系统同步 | `name-change-identity-record-synchronization-continuity/` | 姓名变更、SSA、护照、州证件、税务、雇主、金融、医疗、福利记录 | 同一主体在不同系统中被拆成多个身份，导致资格延迟、支付失败、旅行受阻或服务拒绝 |
| 地址和邮件必须能路由服务 | `address-residency-mail-service-continuity/` | 地址变更、居住地、邮件转递、关键通知、辖区、服务路由 | 迁居、无固定住址、邮件丢失或地址不同步使通知、资格、投票、税务、福利和救援断线 |
| 家庭组成必须能被资格系统正确建模 | `household-composition-dependent-eligibility-continuity/` | household、dependent、共同居住、照护关系、税务、保险、福利资格单位 | 家庭事实变化或制度定义错配导致错误拒绝、错误支付、覆盖断裂或追缴风险 |
| 家庭责任必须可执行可审查 | `family-law-custody-child-support-continuity/` | 亲子关系、监护权、养育时间、子女抚养、法院命令、执行记录 | 命令缺失、执行失败或冲突升级让儿童资源、安全、医疗教育授权和照护连续性断裂 |
| 原照护失稳后儿童安置必须连续 | `kinship-foster-adoption-care-continuity/` | 亲属照护、寄养、收养、安置稳定性、permanency、儿童记录 | 保护过程因频繁转移、记录丢失、服务失败或关系断裂转化为新的创伤和能力形成损失 |
| 可用资金必须能被持续访问 | `banking-deposit-account-access-continuity/` | 银行账户、信用社账户、存款保险、账户恢复、错误交易、支付入口 | 账户失效、冻结、凭据丢失、机构倒闭或错误交易让收入、福利、储蓄和支付能力断线 |
| 债务义务必须可被治理和重组 | `debt-obligation-collection-relief-continuity/` | 债务类型、催收、信用后果、破产、债务救济、消费者保护 | 债务压力、催收、诉讼、扣押或错误记录吞噬现金流、注意力、住房和重新开始能力 |
| 不动产资源必须可证明可追溯 | `real-property-title-deed-record-continuity/` | 地契、产权链、土地记录、抵押、留置、房产税、title insurance | 产权链错误、地契丢失、留置或税费断点让居住、资产、继承和灾后恢复失去制度保护 |
| 地方移动资格必须连续 | `driver-license-vehicle-registration-continuity/` | 驾照、州 ID、REAL ID、车辆 title、登记、车牌、地址同步 | 移动凭证丢失、吊销、跨州错配或车辆记录断裂压缩工作、医疗、照护和撤离行动半径 |
| 跨境移动资格必须连续 | `passport-travel-document-mobility-continuity/` | 护照、旅行证件、领事服务、紧急证件、旅行警示、跨境身份 | 证件过期、丢失、扣留或领事服务不可达截断跨境医疗、工作、学习、家庭和撤离选择权 |
| 离家行程脚本必须可恢复 | `long-distance-travel-booking-itinerary-continuity/` | 订票、确认号、行程单、改签、取消、通知、跨服务衔接 | 行程错配、取消通知失败或不可改签会连锁影响住宿、医疗、照护、工作和回程 |
| 航空中断必须有恢复边界 | `air-passenger-rights-disruption-refund-continuity/` | 延误、取消、退款、拒载、停机坪延误、残障航空旅行、消费者投诉 | 航空中断消耗时间、现金、药物余量和住宿窗口，并可能截断跨境安排 |
| 航空筛查必须可通过且可访问 | `aviation-security-screening-identity-continuity/` | TSA 安检、身份核验、REAL ID、旅客支持、医疗设备、可访问筛查 | 身份错配、安检不可访问或沟通失败会使主体失去航班、医疗用品和时间窗口 |
| 移动物品必须支撑离家生存 | `baggage-personal-property-travel-continuity/` | 托运行李、随身物品、延误/丢失/损坏行李、药品、证件、设备 | 行李物品损失会扩散为身份、治疗、卫生、工作、住宿和尊严风险 |
| 临时住宿必须提供恢复基地 | `lodging-temporary-accommodation-access-continuity/` | 酒店、短租、入住资格、取消、无障碍客房、灾害临时安置、住宿诈骗 | 住宿失败会压垮睡眠、卫生、药物保存、设备充电、家庭协调和再行动能力 |
| 海外求助链必须可达 | `travel-advisory-consular-assistance-continuity/` | 旅行警示、STEP、使领馆、领事协助、紧急证件、海外危机通信 | 警示失读、登记缺失或求助边界误解会放大海外医疗、自由、身份和家庭断裂 |
| 旅行健康暴露必须提前治理 | `travel-health-preparedness-continuity/` | 目的地健康资料、旅行健康风险、疫苗与预防资料、慢病准备、药品供应 | 旅行暴露和医疗可及性变化会改变健康状态转移函数并造成治疗中断 |
| 边境申报与入境记录必须可信 | `customs-border-entry-declaration-continuity/` | 海关申报、边境检查、I-94、受限物品、农业检疫、关税、可信旅客 | 申报、记录、证件或物品边界失败会损失时间、物资、医疗用品和后续身份记录 |
| 订单承诺必须转化为实际履约 | `online-retail-order-shipping-fulfillment-continuity/` | 在线订单、邮购/电话订单、确认、发货、延迟、未交付、取消、履约纠错 | 下单后未履约、延迟、虚假发货或平台推诿会锁住资金、时间和替代采购窗口 |
| 失败交易必须可回收 | `consumer-return-refund-dispute-resolution-continuity/` | 退货、退款、换货、store credit、取消、商家争议、消费者投诉 | 商品或服务不匹配时，缺少退款争议机制会把可恢复资源变成沉没成本 |
| 产品故障后必须可维修可替换 | `consumer-warranty-service-contract-repair-continuity/` | 保修、服务合同、维修、替换、登记、产品文件 | 保修和服务合同不透明会把产品故障转化为强制替换、等待和长期资源浪费 |
| 产品所有权必须包含最低维修接入 | `right-to-repair-parts-manuals-access-continuity/` | 维修权、零件、手册、诊断工具、软件锁、独立维修 | 手册、零件或诊断入口被封闭时，故障产品无法进入恢复路径，设备寿命被人为缩短 |
| 支付错误必须可纠正 | `payment-card-dispute-unauthorized-charge-continuity/` | 信用卡、借记卡、EFT、账单错误、未授权扣款、错误解决 | 未授权扣款或账单错误无法纠正会直接削弱现金流、账户安全和交易信任 |
| 储值余额必须保持可见可用 | `gift-card-prepaid-stored-value-continuity/` | 礼品卡、预付卡、store credit、平台余额、到期、费用、余额查询 | 余额到期、费用侵蚀、诈骗或平台关闭会把名义资源变成不可用资源 |
| 真实交易成本必须事前可见 | `price-fee-disclosure-junk-fee-continuity/` | 标价、总价披露、强制费用、drip pricing、junk fees、账单透明 | 隐藏费用和分段加价会污染预算、比较和退出选择，使低成本判断变成高成本结果 |
| 市场信任输入必须可审查 | `consumer-reviews-endorsements-marketplace-trust-continuity/` | 在线评价、虚假评价、背书、网红披露、评价压制、推荐排名 | 刷评、隐性广告和评价压制会污染选择输入，增加错误交易、诈骗和资源浪费概率 |
| 短期信用桥接必须可计价可还款 | `credit-card-revolving-credit-cost-continuity/` | 信用卡账户、额度、APR、费用、宽限期、最低还款、循环余额、逾期 | 利息费用和最低还款不透明会把短期购买转成长期现金流压缩 |
| 消费贷款必须披露真实跨期义务 | `consumer-loan-origination-apr-disclosure-continuity/` | 个人贷款、分期贷款、承保、放款、APR、费用、还款计划、服务转移 | 披露、服务或还款计划失败会让当前资源获得变成不可控债务负担 |
| 房贷服务必须维持住房稳定 | `mortgage-origination-servicing-foreclosure-continuity/` | Loan Estimate、Closing Disclosure、托管账户、服务商转移、损失缓解、止赎 | 付款错配、服务错误或止赎升级会把长期住房基础设施切断 |
| 车辆融资必须维持移动入口 | `auto-loan-lease-servicing-repossession-continuity/` | 车贷、租赁、经销商融资、APR、附加产品、逾期、收车、留置权 | 收车、差额债务或留置权错误会切断通勤、照护、医疗和工作行动链 |
| 教育融资必须保持记录和还款连续 | `student-loan-servicing-repayment-forgiveness-continuity/` | 学生贷款、服务商、还款计划、延期、宽限、PSLF、减免、违约 | 服务记录和付款计数断裂会压缩职业选择、现金流和长期教育资本收益 |
| 应急现金桥接不能变成债务循环 | `payday-small-dollar-title-loan-continuity/` | 发薪日贷款、小额高成本贷款、title loan、滚续、账户访问、抵押物 | 高成本滚续、自动扣款和抵押物风险会把短期缺口变成长期束缚 |
| 即时消费分期必须保持未来义务可见 | `buy-now-pay-later-installment-financing-continuity/` | BNPL、商家分期、平台授信、自动扣款、退款同步、逾期费用 | 多平台义务、退款不同步或逾期费用会隐藏未来现金流占用 |
| 跨境资金支持必须可披露可纠错 | `remittance-money-transfer-disclosure-continuity/` | 汇款、跨境转账、费用、汇率、收款金额、取消、错误解决、合规延迟 | 费用汇率不透明、收款失败或合规阻断会破坏家庭支持和跨境资源传递 |
| 车辆事故损失必须可理赔可恢复 | `auto-insurance-liability-collision-claims-continuity/` | liability、collision、comprehensive、UM/UIM、deductible、adjuster、repair estimate、total loss | 事故责任、维修估价、total loss 或 subrogation 失败会切断移动能力和现金流恢复 |
| 住所财产损失必须可证明可赔付 | `homeowners-renters-property-insurance-claims-continuity/` | homeowners、renters、personal property、loss of use、ALE、inventory、proof of loss | 财产清单、proof of loss 或临时居住费用失败会放大家庭恢复成本 |
| 洪水风险必须纳入专门保险与灾后现金流 | `flood-insurance-nfip-claims-continuity/` | NFIP、private flood insurance、flood maps、waiting period、proof of loss、appeal | 洪水通常不在普通房主险中，覆盖误解和理赔失败会压垮灾后住房恢复 |
| 区域巨灾风险必须可保可重建 | `catastrophe-wind-wildfire-earthquake-insurance-continuity/` | wind、wildfire、earthquake、hail、catastrophe deductible、FAIR Plan、nonrenewal | 巨灾免赔额、保险退出和高风险区域不可保会让住所资产和迁移选择同时受损 |
| 残障收入中断必须可替代 | `disability-income-insurance-claim-continuity/` | short-term disability、long-term disability、own occupation、any occupation、medical evidence、appeal | 疾病伤残后收入替代失败会把健康事件转化为长期现金流与职业连续性断裂 |
| 长期照护成本必须可触发可支付 | `long-term-care-insurance-benefit-activation-continuity/` | ADL、cognitive trigger、elimination period、care plan、invoices、premium increase | 福利触发、等待期、发票或保费上涨失败会把失能照护成本转嫁给家庭系统 |
| 离家移动风险必须可临时恢复 | `travel-insurance-trip-protection-claims-continuity/` | trip cancellation/interruption、travel medical、evacuation、baggage/delay、covered reasons、documentation | 旅行中断、医疗撤离或行李延误理赔失败会让离家状态变成现金、医疗和资料断点 |
| 高额个人责任必须有防御与资产边界 | `personal-liability-umbrella-insurance-defense-continuity/` | personal liability、umbrella/excess、limits、defense costs、claim notice、coverage dispute | 责任 claim、法律防御或 coverage dispute 失败会把单次事故扩展成长期资产暴露 |
| 持续交易关系必须可理解可退出 | `contract-subscription-billing-consent-continuity/` | 合同、服务条款、订阅、自动续费、账单、取消、争议、持续同意 | 隐性续费、暗黑模式、账单错误和取消摩擦持续消耗金钱、时间、注意力和控制权 |
| 关键文件必须可签署可认证 | `notary-document-authentication-signature-continuity/` | 公证、签名、电子签名、文件认证、apostille、授权文件、跨机构承认 | 文件无效、认证缺失、身份无法确认或签名记录失效让授权、事实和跨境文件不可执行 |
| 国家成员资格必须可证明 | `citizenship-nationality-statelessness-continuity/` | 公民身份、国籍、自然化、国籍证明、无国籍风险、领事保护 | 无国籍、国籍争议或证明缺失使旅行、保护、投票、福利、家庭团聚和法律救济断裂 |
| 居留和工作授权必须连续 | `immigration-status-residency-work-authorization-continuity/` | 移民身份、居留资格、工作授权、身份变更、续期、雇佣核验 | 身份过期、授权延误、雇主锁定或文件丢失压缩工作、医疗、住房、教育和家庭行动 |
| 人道保护身份必须连续 | `asylum-refugee-protection-status-continuity/` | 庇护、难民、临时保护、人道保护、安置、家庭团聚 | 原制度失效后，保护身份悬置会让安全、住所、医疗、教育、工作和家庭团聚长期断裂 |
| 强制限制状态必须可追踪可恢复 | `detention-custody-confinement-status-continuity/` | 逮捕、拘留、羁押、移民拘押、释放、通信、法律入口 | 位置不明、联系断裂、药物中断、法律入口失败或释放转接失败让主体快速失去恢复路径 |
| 强制治疗必须保护权利连续性 | `civil-commitment-involuntary-treatment-rights-continuity/` | 非自愿评估、民事收治、强制治疗、最小限制、复查、出院转接 | 危机干预若缺少复查、同意、语言、残障权利和社区转接，会把安全措施变成失权链条 |
| 程序通知必须让主体能回应 | `court-notice-service-process-default-judgment-continuity/` | 法律通知、送达、听证通知、回应期限、缺席判决、执行后果 | 未收到或无法理解程序会导致工资、住房、债务、家庭权利和信用被静默剥夺 |
| 记录救济必须限制长期尾部后果 | `criminal-record-relief-collateral-consequences-continuity/` | 刑事记录、封存清除、记录更正、附带后果、重返资格 | 过去事件通过记录和附带后果长期截断工作、住房、证照、投票、家庭和服务入口 |
| 儿童必须能稳定进入学校并持续出勤 | `school-enrollment-attendance-continuity/` | 入学、转学、出勤、长期缺勤、无家可归学生保护、学籍交接 | 入学失败、长期缺勤或学籍交接断裂会削弱学习轮次、校内服务入口和未来教育路径 |
| 残障学生必须获得可执行支持 | `special-education-iep-504-accommodation-continuity/` | IDEA、IEP、Section 504、合理便利、相关服务、评估、转衔 | 功能限制若没有转化为学校支持，会变成学习排除、纪律风险、家庭负担和长期能力损耗 |
| 学校餐食必须支撑每日营养 | `school-meals-nutrition-access-continuity/` | 校餐、早餐、午餐、免费/减价资格、CEP、暑期餐食、特殊饮食 | 饥饿、营养缺口、餐食债务或假期断点会削弱注意力、健康恢复和家庭资源韧性 |
| 学生健康条件必须进入学校运行系统 | `school-health-services-chronic-condition-continuity/` | 学校护士、慢病支持、用药、免疫记录、急救计划、返校支持 | 慢病和急性风险若不能在学校被支持，会转化为缺勤、急性事件和学习日损耗 |
| 到校路径必须安全可靠 | `school-transportation-safe-routes-continuity/` | 校车、通学路线、步行骑行安全、交通资格、无障碍交通 | 通学不可达或不安全会压缩出勤、学习时间、家庭工作连续性和儿童安全 |
| 纪律系统必须避免排除性长尾 | `school-discipline-exclusion-restraint-continuity/` | 停学、开除、课堂移除、约束隔离、复学、纪律民权数据 | 排除性纪律会把行为、残障、创伤或社会风险转化为学习日损失和制度尾部后果 |
| 学校必须提供心理恢复入口 | `school-mental-health-counseling-support-continuity/` | 学校咨询、社工、心理师、危机转介、社区照护衔接、隐私同意 | 心理支持缺口会让压力、创伤、孤立和危机压缩出勤、学习参与和求助能力 |
| 学校环境必须安全可归属 | `school-climate-bullying-violence-prevention-continuity/` | 学校气候、归属感、欺凌、骚扰、暴力预防、报告机制、民权边界 | 欺凌、骚扰、暴力和不可信报告机制会制造恐惧缺勤、慢性压力和长期关系损耗 |
| 高等教育入口必须承认已有学习成果 | `postsecondary-admissions-transfer-articulation-continuity/` | 录取、注册、转学、学分转换、衔接协议、重新入学、时间到学位 | 入学衔接失败或学分损失会把既有学习资本转成重复成本、延迟毕业和路径放弃 |
| 学生学习现金流必须连续 | `student-financial-aid-grant-scholarship-continuity/` | FAFSA、Title IV、Pell、贷款、work-study、奖助学金、SAP、发放、债务 | 资助断裂、SAP 失效、账单 hold 或生活费缺口会把学习机会转成债务和退学风险 |
| 学位路径必须可导航可预警 | `academic-advising-degree-progress-continuity/` | advising、degree audit、课程排序、学业预警、学分积累、完成路径 | 课程迷航、无效学分、先修阻塞和学业预警缺失会消耗有效时间并延迟完成 |
| 校园基本需求必须被接住 | `campus-basic-needs-student-support-continuity/` | 食物、住房、交通、托育、应急资金、福利导航、学生支持 | 生存性摩擦会吞噬学习时间、睡眠、恢复、出勤和校园参与 |
| 高校残障便利必须可执行 | `campus-disability-accommodations-accessibility-continuity/` | ADA/504、合理便利、可访问材料、辅助技术、考试住宿、数字无障碍 | 便利延迟或不可执行会把功能限制转成课程排除、成绩损耗和职业入口关闭 |
| 校园心理危机必须有恢复路径 | `campus-mental-health-crisis-student-support-continuity/` | 咨询、危机响应、休学返校、同伴支持、社区转介、隐私同意 | 心理危机、孤立和服务容量不足会截断学习、安全、关系和返校路径 |
| 校园安全与民权程序必须可信 | `campus-safety-title-ix-clery-continuity/` | Title IX、Clery、校园犯罪数据、预警、支持性措施、安全报告 | 伤害、报复、报告失信或安全通知失败会制造恐惧缺勤、创伤和制度退出 |
| 国际学生身份必须与学籍同步 | `international-student-sevis-status-continuity/` | SEVIS、I-20、DSO、课程负荷、CPT/OPT、旅行签注、身份维护 | 记录错误、授权误解或期限错过会把学习、工作、旅行和居留路径转成身份风险 |
| 邮箱恢复入口必须可达 | `email-account-recovery-continuity/` | 邮箱账号、恢复邮箱、密码重置、通知、邮件归档、账号接管风险 | 邮箱丢失或被接管会切断医疗、金融、教育、工作、政府和平台账号恢复链 |
| 手机号控制权必须稳定 | `phone-number-sim-portability-account-security-continuity/` | 手机号、SIM/eSIM、携号转网、短信验证、运营商账号、SIM swap | 号码丢失、被转出或停机会连带破坏通信、验证、通知和多账户恢复 |
| 强认证必须可恢复 | `mfa-passkey-credential-recovery-continuity/` | MFA、passkey、硬件密钥、恢复码、可信设备、凭证生命周期 | 强认证若无恢复路径，会把安全工具变成不可恢复锁定和服务排除 |
| 机密凭证库必须可继承可迁移 | `password-manager-secret-vault-continuity/` | 密码管理器、密钥库、恢复密钥、紧急访问、共享保险库 | 密码库单点失效会让分散账号、家庭代理、团队交接和数字遗产同时断裂 |
| 数字资料必须可恢复可导出 | `cloud-backup-file-sync-data-portability-continuity/` | 云存储、文件同步、备份、版本历史、数据导出、格式迁移 | 误删、勒索、账号停权或供应商锁定会摧毁作品、证据、记忆和恢复资料 |
| 联系人图谱必须可迁移 | `messaging-contact-graph-portability-continuity/` | 消息账号、联系人、群组、聊天历史、备份导出、互操作 | 账号停权、设备丢失或平台锁定会切断协作、照护、求助和社会支持网络 |
| 公共数字地址必须长期可达 | `domain-dns-web-presence-continuity/` | 域名、DNS、注册商、续费、证书、托管、邮箱域、Web 可达性 | 域名过期、DNS 劫持、证书失效或托管中断会让作品、社区和邮件入口消失 |
| 平台准入必须可申诉可退出 | `platform-account-suspension-appeals-continuity/` | 账号停权、内容移除、申诉、透明度、收入冻结、数据退出 | 错误停权和申诉失败会切断创作、商业、学习、社交和社区参与 |
| 个人计算设备必须可修可迁移 | `personal-computing-device-lifecycle-repair-continuity/` | 手机、电脑、平板、外设、维修、替换、支持窗口、数据迁移、报废 | 设备故障、锁定或不可迁移会把账号、资料、工作流和恢复通道同时切断 |
| 家庭网络必须可信可恢复 | `home-network-router-iot-security-continuity/` | 路由器、Wi-Fi、宽带网关、IoT、固件更新、默认凭证、设备标签 | 家庭网络失控或断连会中断远程医疗、学习、工作、监测和身份验证 |
| 软件制品来源必须可审查 | `software-supply-chain-dependency-provenance-continuity/` | 依赖、包管理器、构建、SBOM、签名、来源证明、制品仓库 | 供应链污染会让主体依赖的软件工具和服务从基础设施变成风险源 |
| 漏洞暴露窗口必须可缩短 | `software-update-vulnerability-patch-continuity/` | 更新、漏洞披露、补丁部署、回滚、支持终止、KEV | 未修补软件或错误更新会造成勒索、账号接管、数据损坏和服务中断 |
| 开源维护必须可持续 | `open-source-maintainer-sustainability-continuity/` | 维护者时间、资金、安全响应、治理、交接、项目健康、关键依赖 | 维护者枯竭和项目废弃会让关键依赖停止修复、审计和发布 |
| 证书与密钥信任链必须连续 | `pki-certificate-cryptographic-trust-continuity/` | PKI、TLS 证书、CA、密钥管理、吊销、根信任、证书透明度、算法迁移 | 证书过期、密钥泄露或根信任失效会让 Web、API、更新和身份验证不可达或不可信 |
| 云服务必须可退出可互操作 | `cloud-service-exit-interoperability-continuity/` | SaaS、云服务、数据导出、迁移、互操作、合同退出、供应商锁定 | 云锁定、停服、涨价或封禁会把资料、身份和工作流变成许可条件 |
| API 运行时依赖必须有降级路径 | `api-platform-dependency-runtime-continuity/` | 第三方 API、SDK、SLA、限流、计费、版本废弃、降级、替代路径 | API 中断、废弃或政策变化会直接让主体和组织工具链任务失败 |
| 未来时间承诺必须可执行 | `calendar-scheduling-appointment-continuity/` | 日历、时区、预约、改期、邀请、提醒、跨平台同步 | 日程错配、时区错误、预约丢失或改期失败会让医疗、工作、学习、照护和协作机会断线 |
| 关键事件必须被正确路由 | `notification-alert-routing-attention-continuity/` | 通知、推送、警报、权限、静音、优先级、确认、渠道路由 | 漏报、误报、通知疲劳和注意力碎片化会同时造成风险响应失败和恢复能力下降 |
| 重复维护任务必须可触发可补救 | `reminder-alarm-routine-task-continuity/` | 闹钟、提醒、重复任务、到期日、确认、错过任务、补救 | 小任务遗忘、延迟和例程断裂会累积为健康、资源、设备、关系和项目失败 |
| 远程协作现场必须可达 | `meeting-video-conferencing-remote-collaboration-continuity/` | 视频会议、语音、屏幕共享、字幕、录制、纪要、行动项 | 距离、带宽、设备、语言、无障碍或记录断点会让协作、照护和决策中断 |
| 纸面事实必须进入可保存记录流 | `document-capture-ocr-pdf-record-workflow-continuity/` | 扫描、OCR、PDF/PDF-A、表单、元数据、提交、归档 | 文件不可读、不可找、不可提交或长期格式失效会让事实证明和权利执行断线 |
| 资料必须能被发现和检索 | `search-index-discovery-retrieval-continuity/` | 搜索、索引、元数据、sitemap、schema、目录、断链、来源验证 | 资料存在但找不到、搜不准、链接坏掉或来源不明会让外部记忆和组织知识失效 |
| 重复流程必须可自动化且可控 | `personal-automation-integration-workflow-continuity/` | 触发器、动作、webhook、OAuth、脚本、日志、人工中止 | 自动化静默失败、权限过宽、平台锁定或重复提交会把降本工具变成隐形风险 |
| 协作文档必须保留权限与版本 | `collaborative-document-permission-version-continuity/` | 共享文档、权限、所有者、评论、版本历史、导出、归档 | 权限断裂、所有者离开、链接失效或版本丢失会切断团队记忆、证据和行动项 |
| 住所必须可进入 | `home-access-lock-key-entry-continuity/` | 钥匙、锁具、门禁、访客授权、紧急出入 | 住所进不去、权限丢失、锁具失效或逃生路径被阻断会切断睡眠、药品、文件、设备和照护 |
| 家用设备必须可维护 | `household-appliance-maintenance-repair-continuity/` | 家电生命周期、召回、维修、替换、能效、安全故障 | 设备停摆、维修延迟或召回漏接会让食物、清洁、洗衣、温控和照护任务断裂 |
| 家庭冷藏必须保全营养输入 | `home-refrigeration-food-storage-continuity/` | 冷藏、冷冻、停电、温度控制、食品保存 | 温度失控、停电或设备故障会把食物资源转成浪费、感染风险和预算损失 |
| 烹饪备餐必须安全可持续 | `cooking-meal-preparation-kitchen-safety-continuity/` | 烹饪设备、备餐、食品处理、厨房火灾、烫伤、交叉污染 | 烹饪链失效会把营养输入转成火灾、伤害、食源性风险和时间损耗 |
| 衣物鞋履卫生必须支撑外出与尊严 | `laundry-clothing-footwear-hygiene-continuity/` | 洗衣、衣物、鞋履、天气防护、卫生用品 | 换洗、鞋履或防护断裂会压缩工作、学习、照护、社交和恢复 |
| 家庭卫生必须可治理 | `household-cleaning-disinfection-pest-control-continuity/` | 清洁、消毒、化学品安全、害虫控制、室内卫生 | 清洁不足、化学误用或害虫暴露会制造感染、过敏、毒性和居住压力 |
| 邮件包裹必须可接收 | `postal-parcel-delivery-pickup-continuity/` | 邮件、包裹、签收、自提、追踪、地址同步 | 文件、药品、设备、账单或身份材料收不到会切断远程服务和物理资源交付 |
| 家庭故障必须可被可信维修 | `household-maintenance-repair-contractor-continuity/` | 维修请求、承包商、报价、许可、投诉、维修记录 | 维修延误、诈骗、无证服务或记录缺失会让住房、设备、水电、卫生和安全持续恶化 |
| 个人车辆必须可维护 | `personal-vehicle-maintenance-recall-repair-continuity/` | 车辆维护、轮胎、制动、召回、维修记录、替代路径 | 车辆故障、召回漏接或维修失败会把医疗、工作、照护、教育和食物任务截断 |
| 移动能源入口必须可达 | `fuel-ev-charging-refueling-access-continuity/` | 加油、EV 充电、站点、支付、排队、停电、灾害补能 | 补能失败会让车辆资产、撤离能力、照护任务和跨区域服务可达性同时失效 |
| 到达后的路缘空间必须可用 | `parking-curb-access-towing-impound-continuity/` | 停车、装卸、无障碍停车、路缘、拖车、扣押、费用通知 | 找不到停车、被拖车扣押或路缘不可用会把名义到达转成任务失败 |
| 短距离主动移动必须安全 | `walking-bicycling-micromobility-continuity/` | 人行道、自行车道、交叉口、照明、共享设备、微移动 | 最后一公里不安全或不可达会切断低成本通勤、医疗、学习和邻里服务 |
| 医疗与残障相关出行必须可预约 | `paratransit-nemt-access-continuity/` | ADA paratransit、NEMT、资格、预约、接送窗口、缺乘 | 资格、调度或缺乘失败会让治疗、复诊、康复和日常参与断裂 |
| 按需交通必须可补位 | `taxi-rideshare-demand-response-mobility-continuity/` | 出租车、网约车、需求响应交通、供给、价格、无障碍车辆、平台治理 | 固定线路或私车不足时，按需交通失败会放大服务不可达和时间损耗 |
| 交通支付账户必须不中断 | `transit-fare-payment-toll-account-continuity/` | 票卡、移动支付、优惠资格、余额、过路费、罚费、账户恢复 | 支付和账户失败会把公共交通、收费道路和优惠资格从可用资源变成摩擦 |
| 实时路线与导向必须可信 | `multimodal-trip-planning-real-time-wayfinding-continuity/` | GTFS/Realtime、换乘、延误、无障碍路径、标识、离线备份 | 信息不准、换乘失败或导向缺失会让复杂交通网络在行动时失效 |
| 公共如厕卫生必须可达 | `public-restroom-sanitation-hygiene-access-continuity/` | 公共厕所、洗手、卫生维护、经期卫生、家庭/无障碍厕所 | 如厕和卫生接入失败会压缩离家停留时间、尊严、安全和公共参与 |
| 公共补水必须可信 | `public-drinking-water-hydration-access-continuity/` | 饮水机、补水站、水质告警、应急供水、高温补水 | 脱水、热应激、疲劳和用药风险会把公共空间任务转成身体风险 |
| 公共休息降温必须允许停留 | `public-seating-shade-rest-cooling-access-continuity/` | 公共座椅、遮阴、树冠、候车休息、降温设施、冷却中心 | 不能休息和降温会让老人、儿童、残障者、慢病患者和户外劳动者被排除出公共空间 |
| 社区韧性中心必须接回生命线 | `community-resilience-hub-shelter-center-continuity/` | 韧性中心、避难所、冷却/取暖/清洁空气中心、公共充电、物资分发 | 灾害中电力、温控、通信、水和信息断裂会让主体失联、暴露和恢复失败 |
| 图书馆社区锚点必须低门槛可用 | `public-library-community-anchor-access-continuity/` | 公共电脑、Wi-Fi、打印扫描、学习空间、数字技能、服务导航 | 信息、设备和服务申请入口断裂会放大数字排除、就业失败和公共服务不可达 |
| 公园绿地必须支撑恢复 | `parks-recreation-green-space-access-continuity/` | 公园、绿地、步道、运动场、游乐场、自然接触、公共娱乐设施 | 绿地不可达会减少身体活动、心理恢复、社交连接和热环境缓冲 |
| 公共连接和充电必须不断线 | `public-wifi-device-charging-connectivity-continuity/` | 公共 Wi-Fi、公共电脑、设备充电、断电通信恢复、数字服务访问 | 失联、没电、导航支付失败和错过告警会截断离家任务与灾害恢复 |
| 公共场所无障碍必须连续 | `public-accommodation-accessibility-service-continuity/` | 无障碍入口、有效沟通、合理便利、服务动物、辅助设备、临时中断 | 身体、感官、认知和沟通差异会被服务接口失败转化为制度排除 |
| 日常食品零售必须可达 | `grocery-retail-food-store-access-continuity/` | Grocery、食品零售、低收入低可达地区、营业时间、支付、替代采购 | 食品店不可达、价格/支付/距离摩擦会把食物供给变成不可执行的营养输入 |
| SNAP EBT 必须能真实兑换 | `snap-ebt-redemption-retailer-payment-continuity/` | SNAP EBT、授权零售商、在线购买、PIN、交易失败、账户安全 | 福利存在但不能在合规零售端兑换，会把社会保护变成账面权益 |
| WIC 母婴营养兑换必须连续 | `wic-benefit-redemption-infant-maternal-nutrition-continuity/` | WIC、eWIC、vendor、食品包、婴儿配方、母婴营养 | 母婴营养福利、配方奶和指定食品不可兑换会直接压缩孕产妇、婴儿和儿童发育窗口 |
| 社区食品发放必须可靠 | `food-bank-pantry-community-food-distribution-continuity/` | 食品银行、pantry、TEFAP、库存、发放点、资格、隐私 | 市场和福利不足时，社区发放失败会让短期饥饿、羞辱成本和健康风险放大 |
| 灾害供餐必须接住断供窗口 | `emergency-food-disaster-feeding-continuity/` | 灾害供餐、D-SNAP、应急食品、临时餐点、物流、生命线恢复 | 灾害切断零售、交通、冷链和厨房后，供餐失败会把危机变成营养和安全崩溃 |
| 送餐与集体营养服务必须不中断 | `home-delivered-meals-congregate-nutrition-services-continuity/` | 送餐上门、集体餐、老年营养服务、配送、照护发现 | 行动受限或社交孤立主体无法外出取食时，送餐和集体餐中断会同时削弱营养、监督和关系支持 |
| 婴儿配方和婴幼儿食品必须安全供应 | `infant-formula-baby-food-supply-safety-continuity/` | 婴儿配方、婴幼儿食品、短缺、召回、过敏原、喂养安全 | 婴儿食品短缺、召回或错误替代会把供应链问题直接转成高脆弱主体风险 |
| 外部熟食必须安全可达 | `prepared-food-restaurant-cafeteria-safety-access-continuity/` | 餐馆、cafeteria、熟食、食品规范、过敏原、食源性暴发 | 主体依赖外部供餐时，卫生、过敏原、停业或价格摩擦会把便利输入变成感染、过敏和任务失败 |
| 处方必须能被真实配出 | `retail-pharmacy-prescription-dispensing-continuity/` | 零售药房、邮寄药房、专科药房、处方传递、库存、取药、配送、refill | 临床处方如果无法传递、配药、取药或补药，就会从治疗方案退化为纸面指令 |
| 药品福利和事前授权必须可执行 | `pharmacy-benefit-formulary-prior-authorization-continuity/` | formulary、prior authorization、step therapy、exceptions、coverage determination、PBM | 支付规则和授权摩擦会把医学方案截断在药房柜台或保险系统内 |
| 用药核对和依从执行必须连续 | `medication-reconciliation-regimen-adherence-continuity/` | 药历、出院转诊用药、服药计划、依从性、治疗负担 | 药物进入家庭后，清单错配、重复用药、漏服或负担过高会把治疗转成风险 |
| 药品标签和咨询必须可理解 | `patient-medication-labeling-counseling-continuity/` | Medication Guide、Patient Medication Information、处方标签、药师咨询、语言可及 | 主体不理解用法、警示和风险时，药物材料无法稳定转化为正确行动 |
| 未用药必须可安全回收处置 | `unused-medicine-takeback-disposal-continuity/` | 过期药、未用药、管制药、take-back、drop box、mail-back、家庭储存 | 治疗结束后的药品如果留在家庭中，会形成误服、滥用、中毒、过量和环境风险 |
| DME 供应维修必须不中断 | `durable-medical-equipment-supplier-repair-continuity/` | DMEPOS、供应商、coverage、配送、维修、替换、耗材 | 居家治疗和残障支持设备若供应、维修或耗材中断，主体独立生活和治疗执行会断裂 |
| 居家氧疗和呼吸设备必须可补给 | `home-oxygen-respiratory-equipment-supply-continuity/` | 氧气浓缩机、便携氧、CPAP/BiPAP、耗材、电力依赖、供应商补给 | 呼吸支持被设备、耗材、电力或配送故障截断时，日常生存和睡眠恢复都会失稳 |
| 糖尿病药物与监测耗材必须连续 | `diabetes-insulin-glucose-monitoring-supplies-continuity/` | 胰岛素、泵耗材、CGM、血糖仪、试纸、传感器、冷藏、支付 | 胰岛素、监测和耗材任一断点都会让日常风险控制从连续反馈退化为盲飞 |
| Provider 名录必须真实可用 | `provider-directory-network-adequacy-continuity/` | Provider directory、network adequacy、可接诊状态、距离、语言、无障碍、保险网络 | 保险或服务名义存在，但 provider 不可联系、不可接诊、距离过远或信息错误，会把医疗覆盖变成幽灵网络 |
| 初级照护入口必须可持续 | `primary-care-panel-appointment-access-continuity/` | Primary care、PCP panel、new patient intake、随访、同日预约、FQHC | 没有常规照护关系会让预防、慢病、转诊和复诊退化成碎片化急性访问 |
| 专科转诊必须闭环 | `specialist-referral-authorization-navigation-continuity/` | Referral order、prior authorization、e-consult、资料转交、预约、反馈回传 | 转诊发出但授权、资料、预约或回传失败，会让复杂问题卡在系统缝隙中 |
| 预约必须落在风险窗口内 | `appointment-availability-wait-time-continuity/` | Appointment availability、wait time、排班容量、取消名单、no-show、改期 | 服务存在但等待越过疾病、恢复或风险窗口，会把可处理问题推迟成失能或急性化 |
| 门诊检验必须完成并回传 | `outpatient-laboratory-specimen-result-routing-continuity/` | 检验医嘱、标本采集、采样点、结果路由、portal、异常结果闭环 | 标本、结果或异常回访断裂，会让检测能力无法转化为行动信号 |
| 诊断影像必须完成并可共享 | `diagnostic-imaging-order-scheduling-report-continuity/` | 影像医嘱、prior authorization、预约、报告、影像共享、critical results | 影像预约、报告或共享断裂，会制造重复检查、诊断延误和资料丢失 |
| 门诊操作必须有准备与恢复回路 | `ambulatory-procedure-surgery-center-continuity/` | ASC、门诊内镜、输注、术前工作流、陪同接送、恢复观察、follow-up | 低住院化操作如果缺准备、接送、观察或随访，会把效率收益转成安全断点 |
| 非工作时间入口必须可分流 | `after-hours-urgent-care-triage-continuity/` | 夜间/周末照护、urgent care、retail clinic、护士热线、tele-triage、闭环回传 | 不能等待但又非明确急救的时间断点如果无人接住，会推高失访、急诊拥堵和风险升级 |
| 健康保险覆盖必须持续 | `health-insurance-enrollment-renewal-continuity/` | Open enrollment、special enrollment、renewal、Medicaid/Marketplace 转换、premium payment | 参保、续保或保费断点会让医疗风险转移在服务发生前失效 |
| 保险权益必须可核验 | `insurance-eligibility-benefits-verification-continuity/` | Eligibility、benefits verification、coverage active、deductible、copay、network status | 覆盖状态、权益或网络状态错误会把服务后成本转成不可预期账单 |
| 医疗服务授权必须可追踪 | `medical-service-prior-authorization-utilization-management-continuity/` | Prior authorization、utilization management、medical necessity、coverage criteria、peer review | 授权延迟、补件或拒绝会把检查、影像、手术、设备和治疗截断 |
| 理赔和 EOB 必须闭环 | `claims-adjudication-eob-denial-continuity/` | Claim adjudication、EOB、denial reason、coordination of benefits、resubmission、appeal window | 服务完成后若 claim 拒付或解释不清，会转化为账单、债务和行政负担 |
| 患者账单必须可理解可缓冲 | `patient-billing-payment-plan-continuity/` | Patient statement、patient responsibility、payment plan、billing inquiry、collections handoff | 账单错误、期限压力和催收交接会把治疗事件转化为长期财务压力 |
| 医疗价格必须可预期 | `price-transparency-good-faith-estimate-continuity/` | Hospital price transparency、payer transparency、GFE、machine-readable files、bill-estimate mismatch | 成本不可见会让主体无法规划资源，并可能因恐惧账单推迟治疗 |
| 意外账单必须受保护 | `surprise-billing-balance-bill-protection-continuity/` | No Surprises Act、balance billing、out-of-network emergency care、air ambulance、notice/consent | 主体无法选择网络状态时，高额余额账单会把急性医疗事件变成债务冲击 |
| 医疗债务必须有援助和限制 | `charity-care-financial-assistance-medical-debt-continuity/` | Financial assistance policy、charity care、limitation on charges、collections、medical debt | 高额医疗账单若无经济援助、收费限制和催收边界，会吞噬住房、信用和未来医疗接入 |
| 医疗状态必须对主体可见 | `patient-portal-account-message-continuity/` | Patient portal、secure messaging、notifications、proxy access、patient-facing APIs | 门户失联、通知失败和消息断点会让主体错过结果、任务、账单、预约和照护反馈 |
| 医疗记录必须可获得可修正 | `medical-record-access-amendment-release-continuity/` | HIPAA access、amendment、release of information、information blocking、record portability | 记录不可得或错误不可修正会让转诊、第二意见、急救和长期管理建立在缺失或错误事实上 |
| 临床结果必须形成随访闭环 | `clinical-results-notification-followup-continuity/` | Result notification、critical values、abnormal findings、incidental findings、follow-up tracking | 检测和诊断信号若未通知、未理解或未随访，会把可修复窗口推迟到不可逆阶段 |
| 医疗行动必须代表主体选择 | `informed-consent-refusal-shared-decision-continuity/` | Informed consent/refusal、shared decision-making、decision aids、risk communication | 同意被形式化或拒绝权不可表达，会让医疗路径偏离主体目标、价值和未来选择权 |
| 医疗沟通必须可理解 | `healthcare-language-interpreter-effective-communication-continuity/` | Interpreter services、language assistance、CLAS、LEP、effective communication | 语言和沟通失败会导致误诊、误用药、无效同意、失访和权利失效 |
| 医疗系统必须适配残障主体 | `healthcare-disability-accommodation-accessibility-continuity/` | Reasonable modification、auxiliary aids、accessible medical equipment、disability-inclusive care | 空间、设备和流程不可达会把名义医疗服务变成实际排除 |
| 医疗错误和权利侵害必须可反馈 | `patient-grievance-complaint-ombuds-continuity/` | Patient grievance、complaints、ombudsman、state survey agency、quality feedback | 投诉和 ombuds 入口不可达会让延误、错误、歧视和沟通失败无法进入纠错回路 |
| 医疗服务必须不因受保护特征排除主体 | `healthcare-civil-rights-nondiscrimination-continuity/` | Section 1557、Title VI、Section 504、ADA、nondiscrimination、HHS OCR | 医疗歧视和民权保护缺口会让主体在最需要服务时被降级、拒绝、污名化或失权 |
| 紧急联系人必须可达 | `emergency-contact-next-of-kin-notification-continuity/` | Emergency contact、next of kin、authorized contact、caregiver notification | 主体无法表达时，联系人缺失或过期会让医疗、照护、身份确认和恢复支持断链 |
| 急救摘要必须可读 | `personal-health-record-emergency-summary-continuity/` | Personal health record、emergency summary、wallet card、minimum health data | 分散病历若不能转成急救窗口可读摘要，会延误诊疗、转诊和风险识别 |
| 关键健康警报必须可见 | `medical-id-allergy-critical-alert-continuity/` | Medical ID、allergy/adverse reaction、critical condition alert、wearable/phone profile | 过敏、关键病情或设备限制不可见时，急救链可能发生误治、禁忌和延误 |
| 药物和植入设备必须可转交 | `medication-list-implant-device-emergency-continuity/` | Medication list、high-risk medications、implant/device card、UDI/model information | 药物和设备状态丢失会导致相互作用、禁忌、停药、重复治疗和设备安全风险 |
| 慢病危机必须有行动计划 | `chronic-condition-emergency-action-plan-continuity/` | Chronic-condition action plan、symptom zones、escalation path、school/work/home execution | 慢病在发作、断供或灾害中若无预置计划，会从可管理状态变成急性失控 |
| 免疫记录必须可证明 | `immunization-record-proof-continuity/` | Immunization record、IIS、vaccine card、school/work/travel proof | 接种事件若不能被证明，会影响入学、工作、旅行、医疗和公共卫生准入 |
| 捐赠意愿必须可识别 | `organ-donor-registry-anatomical-gift-continuity/` | Organ donor registry、anatomical gift、state registry、driver-license marker | 死亡边界后的捐赠意愿若不可见，会中断主体意愿执行和他人生命资源转移 |
| 功能需求必须被应急系统看见 | `access-functional-needs-emergency-registry-continuity/` | Access and functional needs、medical needs registry、power-dependent equipment、transport/shelter access | 灾害平均人模型会排除电力、设备、语言、交通、照护和无障碍依赖者 |
| 死亡事实必须可证明 | `death-certificate-registration-cause-of-death-record-continuity/` | Death certificate、death registration、cause of death、certified copy、vital statistics | 死亡记录缺失或错误会阻塞遗属福利、理赔、遗产、账户关闭和公共卫生学习 |
| 遗体处置必须可授权可负担 | `funeral-cremation-burial-disposition-continuity/` | Funeral service、cremation、burial、body disposition、price disclosure | 死亡后高压决策若缺少价格透明和授权边界，会吞噬遗属时间、资金和尊严 |
| 遗体位置和纪念记录必须可查 | `cemetery-memorial-remains-location-continuity/` | Cemetery plot、grave marker、columbarium、ashes/remains location、memorial record | 遗体或骨灰位置失联会破坏纪念、迁移、家庭历史和长期文化连续性 |
| 幸存者悲伤恢复必须被缓冲 | `bereavement-leave-grief-support-continuity/` | Bereavement leave、grief support、EAP、peer support、school/work adjustment | 死亡事件会外溢消耗幸存者时间、注意力、收入和心理稳定 |
| 遗属福利必须能启动 | `survivor-benefits-death-notification-continuity/` | Survivor benefits、death notification、SSA/VA/employer benefits、pension notification | 死亡通知和遗属福利断裂会让家庭在最脆弱窗口失去收入与服务资格 |
| 寿险风险转移必须能兑现 | `life-insurance-beneficiary-claim-continuity/` | Life insurance policy、beneficiary designation、death claim、policy locator | 保单或受益人失联会让风险转移工具无法转化为幸存者资源 |
| 遗产资产负债必须可盘点 | `estate-inventory-asset-liability-handoff-continuity/` | Estate inventory、asset list、liability list、executor、creditor notice | 资产债务和文件不可见会造成资源流失、催收误伤、家庭冲突和任务长期滞留 |
| 死亡后账户服务必须可关闭 | `post-death-account-closure-service-cancellation-continuity/` | Account closure、service cancellation、automatic payment stop、deceased account handling | 账号、订阅和自动扣款继续运行会长期消耗遗属资源并扩大身份盗用风险 |
| 栖居空间可保护生命 | `building-fire-life-safety-codes/` | 建筑规范、消防规范、疏散、烟雾报警、无障碍、结构韧性 | 居住、照护、学习、工作和公共空间成为火灾、烟雾、结构和疏散风险源 |
| 关键物质系统可制造修复 | `manufacturing-repair-capacity/` | 制造、维修、维护、备件、质量、本地生产、关键设备恢复 | 设备损坏、备件短缺、质量缺陷和生产能力不足导致服务与工具系统失效 |
| 公共预算可转化为服务 | `public-procurement-contracting-capacity/` | 公共采购、合同、供应商管理、应急采购、透明度、交付验收 | 有预算和政策但采购失败、合同失效、腐败、延误或劣质交付 |
| 动物-人类-环境界面可治理 | `animal-health-zoonotic-interface-one-health/` | 动物健康、兽医公共卫生、人兽共患病、食品动物、野生动物、One Health | 上游动物疾病、AMR、食品系统和生态界面风险穿透公共卫生屏障 |
| 伴侣动物关系必须可照护 | `human-animal-bond-companion-care-continuity/` | 伴侣动物、人-动物纽带、日常照护、陪伴、家庭节律 | 关系支持和照护责任因费用、住房、疾病或灾害断裂 |
| 宠物医疗入口必须可及 | `veterinary-care-access-cost-continuity/` | 兽医服务、急诊、费用、预约、低成本支持、地理可达 | 宠物病痛、照护费用和服务不可达转化为家庭压力、动物痛苦和关系断裂 |
| 服务动物辅助必须可进入公共生活 | `service-animal-disability-access-continuity/` | 服务动物、任务辅助、公共进入、处理者权利、残障可达 | 服务动物被拒绝或规则混乱会截断残障主体的行动、工作和公共参与 |
| 宠物身份必须可找回 | `pet-identification-microchip-reunification-continuity/` | 微芯片、标签、登记、联系方式更新、走失宠物、重聚 | 宠物走失后身份不可识别会扩大情感损失、动物风险和收容压力 |
| 宠物食药供应必须安全连续 | `pet-food-medication-supply-safety-continuity/` | 宠物食品、动物药、处方配药、召回、标签、供应中断 | 食药质量、召回或断供会把日常照护转化为动物健康和家庭执行风险 |
| 宠物灾害撤离必须纳入家庭计划 | `pet-disaster-evacuation-sheltering-continuity/` | 宠物灾害准备、撤离、避难、物资、服务动物、重聚 | 灾害中宠物不可带走或不可安置会阻止人撤离并扩大灾后关系损失 |
| 收容转接必须保护动物和家庭 | `animal-shelter-rescue-rehoming-continuity/` | 动物收容、救助、寄养、领养、再安置、失主重聚 | 家庭照护断点缺少转接会造成动物伤害、公共压力和家庭长期负担 |
| 动物福利伤害必须可报告转介 | `animal-welfare-cruelty-reporting-continuity/` | 动物福利、虐待忽视、囤积、遗弃、报告入口、转介 | 动物虐待和忽视既伤害动物，也暴露家庭暴力、照护失败和社区风险 |
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
| 武装冲突中平民仍被保护 | `armed-conflict-civilian-protection-ihl/` | IHL、平民保护、人道准入、医疗中立、冲突服务断点 | 战争、占领或武装暴力直接清零生命、身份、医疗、家庭和资源连续性 |
| 冲突可被预防和降级 | `peacebuilding-conflict-prevention-social-cohesion/` | 社会凝聚、信任、调解、申诉通道、脆弱性 | 社会撕裂、复仇循环、群体暴力和制度失信把长期生活窗口击穿 |
| 公共行政可连续运行 | `continuity-of-government-public-administration-resilience/` | 基本职能、授权代理、记录、支付、服务恢复 | 危机中身份、福利、救济、医疗、信息和公共服务入口同时中断 |
| 通信网络可持续连接 | `telecommunications-network-resilience-continuity/` | 网络覆盖、冗余、备电、应急通信、恢复时间 | 警报、求助、支付、医疗、身份、家庭联系和公共服务失联 |
| 宏观资源系统可稳定 | `macroeconomic-monetary-fiscal-stability/` | 通胀、就业、财政空间、公共债务、金融稳定、基本成本 | 技术和服务存在但不可负担，收入、预算、工作和未来选择权被压缩 |
| 公共权力可被约束问责 | `anti-corruption-public-integrity-accountability/` | 透明、审计、利益冲突、采购廉洁、申诉、问责 | 预算、法律、医疗、救济和基础设施被私人利益俘获，名义服务失真 |
| 食物必须先被生产出来 | `agricultural-production-food-system-resilience/` | 作物、畜牧、灌溉、种子、肥料、劳动力、气候适应 | 食物安全在源头断裂，价格、营养、收入和社会稳定被击穿 |
| 土地和土壤必须维持功能 | `soil-health-land-degradation-drought-resilience/` | 土壤健康、土地退化、侵蚀、盐渍化、旱灾、土地恢复 | 生产、蓄水、过滤和生态缓冲下降，贫困、迁移和饥饿压力上升 |
| 水资源必须可观测可调度 | `water-resources-hydrology-flood-drought-management/` | 水文、流域、地下水、水库、洪水、干旱、水安全 | 饮水、农业、能源、住房、交通和医疗被洪旱或断供同时击穿 |
| 生态系统服务必须持续 | `biodiversity-ecosystem-services-resilience/` | 授粉、过滤、蓄水、降温、病害调节、生态恢复 | 自然服务退化使食物、水、空气、热风险和疾病风险同时恶化 |
| 火灾景观风险必须可治理 | `wildfire-landscape-fire-resilience/` | 野火、火灾天气、景观燃料、WUI、烟雾、疏散、恢复 | 住房、空气、电力、通信、医疗和保险被复合火灾风险击穿 |
| 关键物资必须能到达人 | `freight-logistics-port-cold-chain-continuity/` | 货运、港口、仓储、冷链、运输节点、最后一公里 | 药品、食物、设备、备件和救援物资存在但无法抵达主体 |
| 海岸带必须抵御复合风险 | `coastal-marine-resilience-blue-economy-continuity/` | 海岸带、海平面、风暴潮、侵蚀、海洋生态、蓝色经济 | 海岸社区、港口、住房、渔业、旅游和公共服务被海岸风险持续击穿 |
| 水生食物系统必须可持续 | `fisheries-aquatic-food-systems-continuity/` | 捕捞渔业、水产养殖、水产品营养、治理、渔民生计 | 蛋白质来源、生计、价格、生态压力和食品系统韧性同时失稳 |
| 防洪工程必须可审查 | `dams-levees-flood-control-infrastructure-safety/` | 水坝、堤防、防洪墙、闸门、泵站、排涝、检查维护 | 工程资产失效使洪水、供水、能源、住房和交通风险同步放大 |
| 公共工程资产必须持续维护 | `public-works-civil-infrastructure-asset-management/` | 道路、桥梁、隧道、排水、公用设施、资产状态、维护优先级 | 公共工程老化、维护积压和资产不可见导致服务、移动和安全失败 |
| 城市空间必须支撑生命路径 | `urban-planning-land-use-zoning-resilience/` | 土地使用、分区、密度、服务布局、公共空间、风险避让 | 空间排布把住房、交通、服务、热风险、灾害风险和机会结构固化为不平等 |
| 城市自然系统必须降温蓄水 | `green-blue-infrastructure-urban-nature-cooling/` | 树冠、绿地、水体、湿地、雨洪自然基设施、热岛缓解 | 城市热岛、内涝、恢复空间缺失和自然服务不足侵蚀健康与有效时间 |
| 电力生命线必须可靠 | `electric-grid-reliability-resilience-continuity/` | 电网可靠性、资源充足性、输配电、停电恢复、关键负荷 | 停电使医疗、通信、水务、冷链、温控、支付和数字工具同时中断 |
| 水务污水服务必须连续 | `water-wastewater-utility-service-continuity/` | 饮用水、污水处理、管网、泵站、水质监测、应急供水 | 饮水、卫生、医疗清洁和公共卫生因水务中断失效 |
| 热能服务必须可持续 | `fuel-thermal-energy-service-continuity/` | 取暖燃料、燃气、区域能源、热泵、备用燃料、热服务 | 寒冷、热暴露、食品药品损坏和关键设施中断放大 |
| 公共交通必须真实运营 | `public-transit-service-operations-continuity/` | 班次、覆盖、车辆、站点、paratransit、运营人力、服务恢复 | 医疗、工作、教育、食物和照护因公共交通断点不可达 |
| 生命线互依赖必须可审查 | `critical-infrastructure-lifeline-interdependency-resilience/` | 能源、水务、通信、交通、医疗、食品、金融、政府互依赖 | 单部门故障级联放大，多个主体支撑条件同时断裂 |
| 公用事业必须可负担不断供 | `utility-affordability-shutoff-protection-continuity/` | 账单负担、欠费、援助、分期、断供保护、消费者申诉 | 服务存在但被费用和程序摩擦切断，家庭层面基础设施失效 |
| 高成本风险可分摊 | `insurance-risk-transfer/` | 覆盖率、保费、自付、理赔、拒赔、风险池、保障缺口 | 疾病、失业、工伤、残障、灾害或养老金风险由个体独自承担 |
| 托育和家庭运行可持续 | `childcare-family-continuity/` | 托育可及、费用、质量、早期发展、父母工作连续性、家庭压力 | 儿童发展受损、照护者工作中断、时间贫困和家庭压力升级 |
| 应急响应可接住主体 | `emergency-preparedness-response/` | 灾害准备、预警、应急通信、急救医疗、安置、公共卫生应急、恢复 | 低频高冲击事件一次性清零长期积累，通信、医疗、撤离或恢复失败 |
| 人身安全可保护 | `personal-safety-violence-prevention/` | 暴力暴露、求助入口、受害者服务、法律保护、创伤支持、住房安全 | 暴力、胁迫、跟踪、犯罪伤害和创伤直接截断生命、行动能力和未来选择权 |
| 家庭暴力安全退出必须可执行 | `domestic-violence-coercive-control-safety-continuity/` | 亲密伴侣暴力、胁迫控制、安全联系、求助入口、保护资源、恢复支持 | 家庭和亲密关系变成控制系统，住房、医疗、工作、照护、通信和未来选择权被持续压缩 |
| 性暴力后的医疗取证与倡导必须可达 | `sexual-assault-forensic-exam-advocacy-continuity/` | forensic exam、医疗照护、advocacy、保密选项、证据边界、创伤支持 | 伤害后医疗、证据、心理恢复和制度入口断裂，主体被迫独自承担恢复成本 |
| 跟踪骚扰保护必须持续 | `stalking-harassment-protection-order-continuity/` | 跟踪模式、骚扰威胁、保护令、通知执行、安全沟通、记录边界 | 持续威胁使行动半径、工作学习、居住稳定和社交参与长期收缩 |
| 受害者/证人权利通知必须可理解 | `victim-witness-rights-notification-continuity/` | 案件通知、参与权利、保护安排、服务转介、程序可理解性 | 司法过程不可见或不可理解时，安全、恢复、出庭协作和权利实现同时失败 |
| 犯罪伤害后的财务恢复必须可接续 | `crime-victim-compensation-restitution-continuity/` | victim compensation、restitution、医疗心理费用、丧葬费用、收入损失 | 犯罪伤害转化为医疗债务、收入中断、住房失稳和长期恢复失败 |
| 幸存者安全住所必须可转移 | `survivor-safe-housing-emergency-transfer-continuity/` | 庇护、临时住房、VAWA housing protections、emergency transfer、保密联系 | 离开危险关系或犯罪伤害后无安全住所，主体被迫在危险和无家可归之间选择 |
| 人口贩运受害者必须可识别并接入服务 | `human-trafficking-victim-identification-services-continuity/` | 识别、转介、保护、医疗法律服务、福利导航、反二次伤害 | 剥削被误读为普通违规、移民问题或个人选择，导致主体继续被控制和伤害 |
| 失踪与无名身份必须可追踪恢复 | `missing-persons-unidentified-remains-resolution-continuity/` | 失踪报告、无名遗体、NamUs、家属通知、身份线索、长期不确定性 | 人的存在状态、家属行动、法律事务和哀悼恢复长期悬空 |
| 缺陷产品可发现和召回 | `product-safety-recall-systems/` | 缺陷报告、不良事件、投诉、召回覆盖、通知到达、纠正、替代路径 | 缺陷产品持续使用，导致伤害、医疗中断、交通风险和家庭安全风险 |
| 关键供应链可连续 | `supply-chain-continuity/` | 药品、能源、食物、设备、通信、物流 | 断供、单点故障、替代失败 |
| 生物技术双重用途可治理 | `synthetic-biology-biosecurity/` | 生物安全、生物安保、双重用途、治理 | 病原风险、误用、实验外泄 |
| 极端环境可栖居 | `space-extreme-habitation/` | 辐射、微重力、隔离、闭环生命支持 | 环境失效、资源闭环失败、远程医疗失败 |
| 关系网络可支撑主体 | `social-connection-relational-infra/` | 社会连接、孤独、照护网络、信任、协作 | 孤立、照护断裂、危机无人接住 |
| 孤独隔离风险必须可识别 | `loneliness-social-isolation-risk-continuity/` | 孤独、社会隔离、连接质量、关系断裂、求助能力 | 关系风险不可见会延迟照护、危机发现、恢复支持和健康风险干预 |
| 社区支持必须可转介 | `social-prescribing-community-referral-continuity/` | 社会处方、link worker、社区转介、活动参与、闭环回访 | 医疗或公共服务知道需求但无法把主体接入实际社区支持 |
| 邻里互助必须可激活 | `mutual-aid-neighbor-support-network-continuity/` | 互助网络、邻里照看、低摩擦求助、灾害互助 | 正式服务未抵达时无人临时支撑，导致小缺口升级成失稳 |
| 服务参与可沉淀社会资本 | `volunteering-civic-service-participation-continuity/` | 志愿服务、公民服务、参与记录、技能、关系和信誉 | 主体缺少贡献场景，技能、归属、弱连接和机会入口无法复利 |
| 日常冲突必须可低成本修复 | `community-mediation-neighbor-conflict-resolution-continuity/` | 社区调解、邻里纠纷、对话、协议执行、升级风险 | 低强度冲突升级为搬迁、诉讼、孤立、暴力或长期资源损耗 |
| 伤害后责任链必须可修复 | `restorative-justice-repair-accountability-continuity/` | 修复性司法、责任承担、受害者需要、再融入、关系修复 | 伤害事件只剩排除、惩罚或沉默，受害者恢复和责任修复同时失败 |
| 声誉和公共信任必须可纠错 | `reputation-defamation-public-trust-repair-continuity/` | 声誉损伤、诽谤、更正申诉、信任资产、公共记录 | 错误信息或声誉损伤阻断工作、协作、服务和社区机会 |
| 推荐背书必须可转化机会 | `references-vouching-recommendation-social-capital-continuity/` | 推荐人、背书、介绍信、弱连接、社会资本 | 能力无法被可信转译为机会，主体被排除在教育、工作、照护和合作入口之外 |
| 第三空间必须承载归属参与 | `third-place-belonging-social-participation-continuity/` | 公共图书馆、公园、社区锚点、弱连接、归属空间 | 非家庭非工作空间消失，弱连接、恢复、学习、求助和公共参与断裂 |
| 目的意义必须支撑长期行动 | `purpose-meaning-existential-continuity/` | 目的感、意义感、希望、存在痛苦、价值排序、长期目标 | 意义断裂会削弱继续行动、恢复、等待未来和承担长期项目的理由 |
| 精神照护必须尊重实践边界 | `spiritual-care-religious-practice-continuity/` | spiritual care、chaplaincy、宗教实践、信仰共同体、spiritual distress | 精神或宗教实践被切断或强迫时，尊严、身份、恢复和共同体支持受损 |
| 文化身份必须可连续 | `cultural-heritage-identity-continuity/` | 语言、文化实践、非物质文化遗产、共同体记忆、代际传递 | 文化断裂会削弱归属、照护沟通、代际传递和身份稳定 |
| 创造表达必须可参与 | `arts-creative-expression-participation-continuity/` | 艺术参与、创作表达、社区艺术、表达自由、文化参与 | 主体失去表达和创造入口，生活质量、身份表达、情绪恢复和社会可见性下降 |
| 休闲恢复必须可获得 | `leisure-recreation-restorative-activity-continuity/` | 休闲、娱乐、游戏、户外活动、恢复性活动、非生产性时间 | 非任务恢复空间被压缩，压力、倦怠、孤独和行动质量恶化 |
| 叙事身份必须可整合 | `narrative-identity-life-review-continuity/` | life review、reminiscence、自传记忆、生命故事、身份重组 | 记忆资料无法组织成自我叙事，身份稳定、意义感和跨代转交下降 |
| 仪式转换必须被承认 | `ritual-ceremony-life-transition-continuity/` | 仪式、典礼、过渡礼、纪念、公共承认、生命转换 | 重大转换缺少共同体承认，身份、关系和悲伤恢复更容易断裂 |
| 尊严人格必须被保护 | `dignity-personhood-respect-continuity/` | dignity、personhood、尊重、非羞辱、person-centered care | 人被降格为病例、号码、风险标签或负担，主体性和未来选择权被侵蚀 |
| 任务系统必须适配人 | `human-factors-ergonomics-task-system-continuity/` | human factors、ergonomics、human systems integration、usability、任务系统 | 人、工具、环境和流程失配时，错误、伤害、绕行和长期损耗会系统性增加 |
| 工作负荷必须可测量 | `cognitive-load-workload-measurement-continuity/` | NASA-TLX、mental workload、工作记忆、任务复杂度、时间压力 | 认知过载会削弱注意、判断、学习和恢复，使任务失败被误归咎于个人能力 |
| 疲劳风险必须被治理 | `fatigue-risk-alertness-continuity/` | 长工时、夜班、sleep debt、alertness、恢复窗口 | 疲劳降低警觉和判断，增加事故、医疗错误、驾驶风险和长期恢复债务 |
| 情境感知必须可维持 | `situational-awareness-decision-environment-continuity/` | situation awareness、sensemaking、共享心智模型、态势显示、决策支持 | 主体不知道发生了什么、将会怎样和谁负责时，行动会变成盲目反应 |
| 交接和流程必须可靠 | `handoff-checklist-procedure-reliability-continuity/` | handoff、checklist、SOP、read-back、briefing/debriefing、standard work | 状态在跨人、跨班次、跨机构、跨工具转移时丢失，造成重复、遗漏和失控 |
| 事件必须转化为学习 | `incident-reporting-just-culture-learning-continuity/` | incident reporting、near miss、just culture、RCA/RCA2、纠正措施 | 事故和险情被压制或只用于追责时，系统无法学习，同类失败持续复发 |
| 自动化必须可监督 | `automation-bias-mode-confusion-oversight-continuity/` | automation bias、mode confusion、overreliance、override、supervisory control | 主体过度信任或误解自动化模式时，工具会放大错误并削弱人工接管能力 |
| 信号环境必须可管理 | `alert-fatigue-interruption-signal-management-continuity/` | alarm/alert fatigue、notification fatigue、中断、优先级、升级路由 | 噪声、误报和中断淹没重要信号，注意力预算被耗尽，真正风险无人响应 |
| 权利和治理可保护主体 | `governance-rights/` | 同意、退出、数据权、法律身份 | 被控制、被剥夺、被系统吞噬 |
| 服务入口可理解可导航 | `health-literacy-navigation/` | 健康素养、服务导航、风险沟通、共同决策 | 有资源但不会用、误解、延误、行政排除 |
| 语言和表达可理解 | `language-access-plain-communication/` | plain language、语言服务、LEP、CLAS、认知可访问性、表单理解 | 材料读不懂、听不懂、不能执行，或简化时删掉权利和风险 |
| 口腔系统可持续 | `oral-health-continuity/` | 咀嚼、牙周、口腔疼痛、感染、沟通 | 营养障碍、疼痛、感染、社交退缩 |
| 持续存在可承受 | `pain-suffering-control/` | 疼痛、症状负担、生活质量、尊严 | 延长痛苦、有效时间崩塌、退出权受损 |
| 干预效应必须可识别 | `causal-inference-target-trial-emulation/` | 因果图、反事实、目标试验模拟、混杂、选择偏差 | 把相关性误写成因果，导致错误干预排序 |
| 寿命和健康寿命风险必须可建模 | `survival-analysis-healthspan-risk-modeling/` | 风险函数、生存曲线、健康寿命、竞争风险、有效时间 | 用静态指标替代时间路径，误读寿命和失能风险 |
| 主体状态必须可动态仿真 | `human-digital-twin-life-course-simulation/` | 主体状态向量、状态转移、生命历程仿真、场景模拟 | 多域变量无法合成路径，只剩碎片化叙事 |
| 干预必须真实落地 | `implementation-science-adherence-behavior-change/` | 采用、依从、fidelity、sustainment、行为摩擦 | 论文有效但现实不可获得、不可坚持或不可维护 |
| 模型必须可校准 | `uncertainty-quantification-model-calibration/` | 校准、外部验证、预测区间、不确定性、漂移 | 精确数字制造虚假确定性，预测越界使用 |
| 数据入口必须可信 | `data-quality-missingness-representativeness/` | 缺失机制、代表性、测量误差、数据血缘、覆盖偏差 | 偏倚数据污染因果、预测、仿真和治理结论 |
| 敏感数据必须可安全学习 | `privacy-preserving-computation-federated-learning/` | 差分隐私、联邦学习、协作分析、隐私预算、效用损失 | 数据集中化、再识别、模型反演、隐私叙事过度承诺 |
| 知识必须可组合可查询 | `knowledge-graph-ontology-semantic-interoperability/` | 本体、知识图谱、语义互操作、受控词表、FAIR 元数据 | 概念漂移、域重复、证据错配、许可受限术语误用 |
| 模型必须可审计 | `model-cards-ai-audit-documentation/` | 模型卡、数据说明、系统卡、审计记录、禁止用途 | 模型输出被误读为权威、营销背书、个人评分或寿命承诺 |
| 未来技术必须可预警 | `technology-foresight-horizon-scanning/` | 弱信号、情景分析、成熟度、证据缺口、复核周期 | 被新闻热度、融资叙事、专利数量或公司公告牵引 |
| 研究资源必须可排序 | `research-portfolio-prioritization-funding-governance/` | 组合优先级、价值信息、阶段门、学习价值、停止条件 | 无限发散、资源错配、单一指标压倒公共价值 |
| 技术成熟必须转化为可及 | `intellectual-property-technology-transfer-access/` | 专利、许可、技术转移、生产扩散、价格和地域可及性 | 技术存在但不可获得、不可负担、许可锁定或转化失败 |
| 科研传播必须可纠错 | `trustworthy-scientific-communication-peer-review/` | 同行评审、预印本、撤稿、勘误、引用语境、利益冲突 | 把未审查、已撤回、被夸大或断章引用的材料写成稳定证据 |
| 人体研究必须保留主体合法性 | `research-participant-consent-community-engagement/` | 知情同意、退出、再联系、社区参与、结果回馈、信任 | 长期研究退化为数据抽取，代表性、留存和伦理正当性同时下降 |
| 生物样本必须可追踪可信 | `biobanking-biospecimen-quality-chain-of-custody/` | 样本质量、预分析变量、冷链、追踪、保管链、二次使用 | 样本退化、污染、错配或同意越界污染组学和 biomarker 证据 |
| 生命路径必须可长期观察 | `longitudinal-cohort-retention-followup-infrastructure/` | 纵向队列、随访、留存、失访、事件确认、生命历程链接 | 失访、选择偏差和随访断裂扭曲寿命、健康寿命和风险路径 |
| 真实世界反馈必须可治理 | `registries-real-world-data-governance/` | 患者登记、疾病登记、产品登记、RWD/RWE、数据质量、用途边界 | 登记缺失、用途越界、数据漂移和相关性外推污染技术反馈 |
| 测量硬件必须可校准维护 | `scientific-instrumentation-sensor-calibration-maintenance/` | 仪器、传感器、校准、漂移、维护、参考材料、不确定性 | 设备误差被误读为生命路径、环境暴露或技术效果信号 |
| 远期治疗必须能到达靶点 | `nanomedicine-targeted-delivery-molecular-repair/` | 纳米材料、靶向递送、释放控制、分子诊断、分子修复边界 | 有效载荷存在但到不了、控不住、监测不了或毒性失控 |
| 未来药物和蛋白必须可设计验证 | `ai-drug-discovery-protein-design/` | 分子生成、蛋白设计、ADMET 预测、湿实验验证、模型边界 | 把模型生成误读成疗效，把筛选加速误读成临床成功 |
| 基因表达状态必须可调控但不失控 | `epigenetic-editing-gene-regulation-therapeutics/` | 表观编辑、染色质状态、可逆沉默、表达重编程、脱靶风险 | 误把表达调控写成安全逆龄或永久治疗，忽略脱靶和长期效应 |
| 脑信息连续性必须可保存可解释 | `brain-preservation-connectomics-emulation/` | 脑保存、连接组、神经结构记录、仿真、人格连续性 | 把结构保存误写成意识延续，把仿真假设误写成复活证明 |
| 长期数据必须抵抗未来解密 | `post-quantum-cryptography-long-term-data-security/` | PQC、密码迁移、加密敏捷性、长期保密、harvest-now-decrypt-later | 医疗、身份和研究档案被未来量子或迁移失败破坏 |
| 高风险系统必须可证明可信 | `safety-critical-software-formal-methods/` | 形式化方法、模型检查、证明、保证案例、安全关键软件 | 生命支持、医疗、AI 和基础设施软件因隐性缺陷级联失败 |
| 外部记忆必须长期可读 | `long-term-digital-preservation-format-migration/` | 格式迁移、校验、元数据、备份、存储介质、可读性 | 作品、记忆、授权、证据和项目上下文随格式、介质或平台消失 |
| 脑灌注必须维持 | `cerebrovascular-stroke-brain-perfusion-resilience/` | 脑血流、卒中、TIA、再灌注、二级预防 | 意识、语言、运动、认知和未来选择权在短时间内被脑血流失败截断 |
| 脑外伤必须可预防和恢复 | `traumatic-brain-injury-neurotrauma-recovery/` | TBI、脑震荡、重复冲击、恢复轨迹 | 事故后注意、记忆、情绪、睡眠和人格表现长期受损 |
| 急性认知失败必须可预防 | `delirium-acute-cognitive-failure-prevention/` | 谵妄、ICU/住院、镇静、睡眠、感染、药物 | 医疗系统反向制造主体失联、长期认知损害和死亡风险 |
| 意识边界必须可审查 | `disorders-of-consciousness-coma-recovery/` | 昏迷、无反应觉醒、最低意识、评估、代理决策 | 误诊、误放弃、无意义维持或主体连续性误判 |
| 脑网络发作必须稳定 | `epilepsy-seizure-network-stability/` | 癫痫、发作频率、网络兴奋性、治疗连续性 | 意识和行动窗口反复中断，伤害、SUDEP、污名和社会限制上升 |
| 自动调节必须稳定 | `autonomic-nervous-system-homeostasis/` | 心率血压、体位耐受、HRV、出汗、消化排尿、压力恢复 | 晕厥、疲劳、脑雾、跌倒和有效时间损耗 |
| 发作性头痛负担必须计入有效时间 | `migraine-headache-effective-time-burden/` | 偏头痛、头痛障碍、感官敏感、认知雾、失能天数 | 低死亡但高失能疾病长期吞噬学习、工作、关系和创造窗口 |
| 状态可观测和校正 | `measurement-feedback/` | 测量、预测、反馈、风险评分 | 错误预测、偏差、指标替代真实终点 |

## 主链路

```text
有效永生 / 主体持续性最大化
  -> 生物基底维护
  -> 生物医学平台可验证、可递送、可治理
  -> 定量方法学可识别、可建模、可校准
  -> 知识治理与技术扩散可追踪、可审计、可排序、可获得
  -> 科研证据基础设施可发表纠错、主体授权、样本保管、长期随访、真实世界登记和仪器校准
  -> 未来技术连续性可生成、可递送、可调控、可保存、可安全执行和可长期读取
  -> 急性神经连续性可保护意识、灌注、认知、脑网络、自动调节和有效时间
  -> 感官、沟通与具身反馈连续性可维持输入、表达、定向、摄食和身体边界
  -> 行星、地球物理与极端热风险可被观测、预警、缓解和恢复
  -> 慢性环境暴露可被识别、降低并纳入恢复成本
  -> 决策权、代理权与受托连续性可保护失能边界上的意愿、访问、资源和责任
  -> 神经与身份连续
  -> 时间窗口延展
  -> 认知与工具增强
  -> 风险函数压低
  -> 资源环境支撑
  -> 初级生产、自然资本、物理物流、海岸土木、城市空间与公用事业生命线底座可持续
  -> 外部技术底座可控
  -> 文明连续性、集体安全与宏观制度底座可维持
  -> 制度治理保护
  -> 测量、预测与反馈
  -> 各研究域通过证据、模型和治理进入同一个主体持续性系统
```

## 组合关系

```text
cellular-reprogramming
  -> gene-therapy-genome-editing-delivery-safety
  -> biological-age-clocks-biomarker-validation
  -> multiomics-personal-baseline-systems-biology
  -> engineered-cell-therapy-regenerative-platforms
  -> organoids-organ-on-chip-disease-models
  -> xenotransplantation-bioengineered-organ-replacement
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
  -> cerebrovascular-stroke-brain-perfusion-resilience
  -> traumatic-brain-injury-neurotrauma-recovery
  -> delirium-acute-cognitive-failure-prevention
  -> disorders-of-consciousness-coma-recovery
  -> epilepsy-seizure-network-stability
  -> autonomic-nervous-system-homeostasis
  -> migraine-headache-effective-time-burden
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
  -> causal-inference-target-trial-emulation
  -> survival-analysis-healthspan-risk-modeling
  -> human-digital-twin-life-course-simulation
  -> implementation-science-adherence-behavior-change
  -> uncertainty-quantification-model-calibration
  -> data-quality-missingness-representativeness
  -> measurement-feedback
```

这组关系处理“等待未来时如何降低自身时间成本和损耗成本”。

```text
future-technology-continuity
  -> nanomedicine-targeted-delivery-molecular-repair
  -> ai-drug-discovery-protein-design
  -> epigenetic-editing-gene-regulation-therapeutics
  -> brain-preservation-connectomics-emulation
  -> post-quantum-cryptography-long-term-data-security
  -> safety-critical-software-formal-methods
  -> long-term-digital-preservation-format-migration
```

这组关系处理“未来技术能否被发现、递送、调控、保存、安全执行并在长周期中保持可读可用”。

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
  -> credit-consumer-reporting-access-continuity
  -> tenant-screening-rental-access-continuity
  -> background-check-record-screening-continuity
  -> employment-algorithmic-hiring-screening-continuity
  -> insurance-underwriting-algorithmic-risk-scoring-continuity
  -> public-benefits-eligibility-automated-decision-continuity
  -> education-record-transcript-verification-continuity
  -> professional-licensure-certification-continuity
  -> skills-competency-credentialing-continuity
  -> continuing-education-recertification-continuity
  -> apprenticeship-work-based-learning-continuity
  -> verifiable-credential-wallet-interoperability
  -> income-payroll-employment-record-continuity
  -> tax-administration-filing-record-continuity
  -> social-security-earnings-benefit-record-continuity
  -> retirement-pension-savings-plan-continuity
  -> unemployment-insurance-wage-record-continuity
  -> workers-compensation-occupational-injury-benefit-continuity
  -> family-medical-leave-job-protection-continuity
  -> paid-sick-family-leave-wage-replacement-continuity
  -> pregnancy-parental-work-continuity
  -> workplace-accommodation-return-to-work-continuity
  -> disability-income-work-capacity-benefit-continuity
  -> family-caregiver-respite-work-continuity
  -> vital-records-life-event-continuity
  -> name-change-identity-record-synchronization-continuity
  -> address-residency-mail-service-continuity
  -> household-composition-dependent-eligibility-continuity
  -> family-law-custody-child-support-continuity
  -> kinship-foster-adoption-care-continuity
  -> banking-deposit-account-access-continuity
  -> debt-obligation-collection-relief-continuity
  -> real-property-title-deed-record-continuity
  -> driver-license-vehicle-registration-continuity
  -> passport-travel-document-mobility-continuity
  -> long-distance-travel-booking-itinerary-continuity
  -> air-passenger-rights-disruption-refund-continuity
  -> aviation-security-screening-identity-continuity
  -> baggage-personal-property-travel-continuity
  -> lodging-temporary-accommodation-access-continuity
  -> travel-advisory-consular-assistance-continuity
  -> travel-health-preparedness-continuity
  -> customs-border-entry-declaration-continuity
  -> online-retail-order-shipping-fulfillment-continuity
  -> consumer-return-refund-dispute-resolution-continuity
  -> consumer-warranty-service-contract-repair-continuity
  -> right-to-repair-parts-manuals-access-continuity
  -> payment-card-dispute-unauthorized-charge-continuity
  -> gift-card-prepaid-stored-value-continuity
  -> price-fee-disclosure-junk-fee-continuity
  -> consumer-reviews-endorsements-marketplace-trust-continuity
  -> credit-card-revolving-credit-cost-continuity
  -> consumer-loan-origination-apr-disclosure-continuity
  -> mortgage-origination-servicing-foreclosure-continuity
  -> auto-loan-lease-servicing-repossession-continuity
  -> student-loan-servicing-repayment-forgiveness-continuity
  -> payday-small-dollar-title-loan-continuity
  -> buy-now-pay-later-installment-financing-continuity
  -> remittance-money-transfer-disclosure-continuity
  -> auto-insurance-liability-collision-claims-continuity
  -> homeowners-renters-property-insurance-claims-continuity
  -> flood-insurance-nfip-claims-continuity
  -> catastrophe-wind-wildfire-earthquake-insurance-continuity
  -> disability-income-insurance-claim-continuity
  -> long-term-care-insurance-benefit-activation-continuity
  -> travel-insurance-trip-protection-claims-continuity
  -> personal-liability-umbrella-insurance-defense-continuity
  -> contract-subscription-billing-consent-continuity
  -> notary-document-authentication-signature-continuity
  -> citizenship-nationality-statelessness-continuity
  -> immigration-status-residency-work-authorization-continuity
  -> asylum-refugee-protection-status-continuity
  -> detention-custody-confinement-status-continuity
  -> civil-commitment-involuntary-treatment-rights-continuity
  -> court-notice-service-process-default-judgment-continuity
  -> criminal-record-relief-collateral-consequences-continuity
  -> school-enrollment-attendance-continuity
  -> special-education-iep-504-accommodation-continuity
  -> school-meals-nutrition-access-continuity
  -> school-health-services-chronic-condition-continuity
  -> school-transportation-safe-routes-continuity
  -> school-discipline-exclusion-restraint-continuity
  -> school-mental-health-counseling-support-continuity
  -> school-climate-bullying-violence-prevention-continuity
  -> postsecondary-admissions-transfer-articulation-continuity
  -> student-financial-aid-grant-scholarship-continuity
  -> academic-advising-degree-progress-continuity
  -> campus-basic-needs-student-support-continuity
  -> campus-disability-accommodations-accessibility-continuity
  -> campus-mental-health-crisis-student-support-continuity
  -> campus-safety-title-ix-clery-continuity
  -> international-student-sevis-status-continuity
  -> email-account-recovery-continuity
  -> phone-number-sim-portability-account-security-continuity
  -> mfa-passkey-credential-recovery-continuity
  -> password-manager-secret-vault-continuity
  -> cloud-backup-file-sync-data-portability-continuity
  -> messaging-contact-graph-portability-continuity
  -> domain-dns-web-presence-continuity
  -> platform-account-suspension-appeals-continuity
  -> personal-computing-device-lifecycle-repair-continuity
  -> home-network-router-iot-security-continuity
  -> software-supply-chain-dependency-provenance-continuity
  -> software-update-vulnerability-patch-continuity
  -> open-source-maintainer-sustainability-continuity
  -> pki-certificate-cryptographic-trust-continuity
  -> cloud-service-exit-interoperability-continuity
  -> api-platform-dependency-runtime-continuity
  -> calendar-scheduling-appointment-continuity
  -> notification-alert-routing-attention-continuity
  -> reminder-alarm-routine-task-continuity
  -> meeting-video-conferencing-remote-collaboration-continuity
  -> document-capture-ocr-pdf-record-workflow-continuity
  -> search-index-discovery-retrieval-continuity
  -> personal-automation-integration-workflow-continuity
  -> collaborative-document-permission-version-continuity
  -> home-access-lock-key-entry-continuity
  -> household-appliance-maintenance-repair-continuity
  -> home-refrigeration-food-storage-continuity
  -> cooking-meal-preparation-kitchen-safety-continuity
  -> laundry-clothing-footwear-hygiene-continuity
  -> household-cleaning-disinfection-pest-control-continuity
  -> postal-parcel-delivery-pickup-continuity
  -> household-maintenance-repair-contractor-continuity
  -> personal-vehicle-maintenance-recall-repair-continuity
  -> fuel-ev-charging-refueling-access-continuity
  -> parking-curb-access-towing-impound-continuity
  -> walking-bicycling-micromobility-continuity
  -> paratransit-nemt-access-continuity
  -> taxi-rideshare-demand-response-mobility-continuity
  -> transit-fare-payment-toll-account-continuity
  -> multimodal-trip-planning-real-time-wayfinding-continuity
  -> public-restroom-sanitation-hygiene-access-continuity
  -> public-drinking-water-hydration-access-continuity
  -> public-seating-shade-rest-cooling-access-continuity
  -> community-resilience-hub-shelter-center-continuity
  -> public-library-community-anchor-access-continuity
  -> parks-recreation-green-space-access-continuity
  -> public-wifi-device-charging-connectivity-continuity
  -> public-accommodation-accessibility-service-continuity
  -> grocery-retail-food-store-access-continuity
  -> snap-ebt-redemption-retailer-payment-continuity
  -> wic-benefit-redemption-infant-maternal-nutrition-continuity
  -> food-bank-pantry-community-food-distribution-continuity
  -> emergency-food-disaster-feeding-continuity
  -> home-delivered-meals-congregate-nutrition-services-continuity
  -> infant-formula-baby-food-supply-safety-continuity
  -> prepared-food-restaurant-cafeteria-safety-access-continuity
  -> retail-pharmacy-prescription-dispensing-continuity
  -> pharmacy-benefit-formulary-prior-authorization-continuity
  -> medication-reconciliation-regimen-adherence-continuity
  -> patient-medication-labeling-counseling-continuity
  -> unused-medicine-takeback-disposal-continuity
  -> durable-medical-equipment-supplier-repair-continuity
  -> home-oxygen-respiratory-equipment-supply-continuity
  -> diabetes-insulin-glucose-monitoring-supplies-continuity
  -> provider-directory-network-adequacy-continuity
  -> primary-care-panel-appointment-access-continuity
  -> specialist-referral-authorization-navigation-continuity
  -> appointment-availability-wait-time-continuity
  -> outpatient-laboratory-specimen-result-routing-continuity
  -> diagnostic-imaging-order-scheduling-report-continuity
  -> ambulatory-procedure-surgery-center-continuity
  -> after-hours-urgent-care-triage-continuity
  -> health-insurance-enrollment-renewal-continuity
  -> insurance-eligibility-benefits-verification-continuity
  -> medical-service-prior-authorization-utilization-management-continuity
  -> claims-adjudication-eob-denial-continuity
  -> patient-billing-payment-plan-continuity
  -> price-transparency-good-faith-estimate-continuity
  -> surprise-billing-balance-bill-protection-continuity
  -> charity-care-financial-assistance-medical-debt-continuity
  -> patient-portal-account-message-continuity
  -> medical-record-access-amendment-release-continuity
  -> clinical-results-notification-followup-continuity
  -> informed-consent-refusal-shared-decision-continuity
  -> healthcare-language-interpreter-effective-communication-continuity
  -> healthcare-disability-accommodation-accessibility-continuity
  -> patient-grievance-complaint-ombuds-continuity
  -> healthcare-civil-rights-nondiscrimination-continuity
  -> emergency-contact-next-of-kin-notification-continuity
  -> personal-health-record-emergency-summary-continuity
  -> medical-id-allergy-critical-alert-continuity
  -> medication-list-implant-device-emergency-continuity
  -> chronic-condition-emergency-action-plan-continuity
  -> immunization-record-proof-continuity
  -> organ-donor-registry-anatomical-gift-continuity
  -> access-functional-needs-emergency-registry-continuity
  -> death-certificate-registration-cause-of-death-record-continuity
  -> funeral-cremation-burial-disposition-continuity
  -> cemetery-memorial-remains-location-continuity
  -> bereavement-leave-grief-support-continuity
  -> survivor-benefits-death-notification-continuity
  -> life-insurance-beneficiary-claim-continuity
  -> estate-inventory-asset-liability-handoff-continuity
  -> post-death-account-closure-service-cancellation-continuity
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
  -> human-animal-bond-companion-care-continuity
  -> veterinary-care-access-cost-continuity
  -> service-animal-disability-access-continuity
  -> pet-identification-microchip-reunification-continuity
  -> pet-food-medication-supply-safety-continuity
  -> pet-disaster-evacuation-sheltering-continuity
  -> animal-shelter-rescue-rehoming-continuity
  -> animal-welfare-cruelty-reporting-continuity
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
  -> armed-conflict-civilian-protection-ihl
  -> peacebuilding-conflict-prevention-social-cohesion
  -> continuity-of-government-public-administration-resilience
  -> telecommunications-network-resilience-continuity
  -> macroeconomic-monetary-fiscal-stability
  -> anti-corruption-public-integrity-accountability
  -> agricultural-production-food-system-resilience
  -> soil-health-land-degradation-drought-resilience
  -> water-resources-hydrology-flood-drought-management
  -> biodiversity-ecosystem-services-resilience
  -> wildfire-landscape-fire-resilience
  -> freight-logistics-port-cold-chain-continuity
  -> coastal-marine-resilience-blue-economy-continuity
  -> fisheries-aquatic-food-systems-continuity
  -> dams-levees-flood-control-infrastructure-safety
  -> public-works-civil-infrastructure-asset-management
  -> urban-planning-land-use-zoning-resilience
  -> green-blue-infrastructure-urban-nature-cooling
  -> electric-grid-reliability-resilience-continuity
  -> water-wastewater-utility-service-continuity
  -> fuel-thermal-energy-service-continuity
  -> public-transit-service-operations-continuity
  -> critical-infrastructure-lifeline-interdependency-resilience
  -> utility-affordability-shutoff-protection-continuity
  -> insurance-risk-transfer
  -> childcare-family-continuity
  -> emergency-preparedness-response
  -> personal-safety-violence-prevention
  -> domestic-violence-coercive-control-safety-continuity
  -> sexual-assault-forensic-exam-advocacy-continuity
  -> stalking-harassment-protection-order-continuity
  -> victim-witness-rights-notification-continuity
  -> crime-victim-compensation-restitution-continuity
  -> survivor-safe-housing-emergency-transfer-continuity
  -> human-trafficking-victim-identification-services-continuity
  -> missing-persons-unidentified-remains-resolution-continuity
  -> product-safety-recall-systems
  -> financial-resilience-access
  -> occupational-work-design
  -> labor-rights-workplace-protection
  -> information-integrity-trust
  -> supply-chain-continuity
  -> synthetic-biology-biosecurity
  -> space-extreme-habitation
  -> social-connection-relational-infra
  -> loneliness-social-isolation-risk-continuity
  -> social-prescribing-community-referral-continuity
  -> mutual-aid-neighbor-support-network-continuity
  -> volunteering-civic-service-participation-continuity
  -> community-mediation-neighbor-conflict-resolution-continuity
  -> restorative-justice-repair-accountability-continuity
  -> reputation-defamation-public-trust-repair-continuity
  -> references-vouching-recommendation-social-capital-continuity
  -> third-place-belonging-social-participation-continuity
  -> purpose-meaning-existential-continuity
  -> spiritual-care-religious-practice-continuity
  -> cultural-heritage-identity-continuity
  -> arts-creative-expression-participation-continuity
  -> leisure-recreation-restorative-activity-continuity
  -> narrative-identity-life-review-continuity
  -> ritual-ceremony-life-transition-continuity
  -> dignity-personhood-respect-continuity
  -> human-factors-ergonomics-task-system-continuity
  -> cognitive-load-workload-measurement-continuity
  -> fatigue-risk-alertness-continuity
  -> situational-awareness-decision-environment-continuity
  -> handoff-checklist-procedure-reliability-continuity
  -> incident-reporting-just-culture-learning-continuity
  -> automation-bias-mode-confusion-oversight-continuity
  -> alert-fatigue-interruption-signal-management-continuity
  -> health-literacy-navigation
  -> language-access-plain-communication
  -> substance-exposure-control
  -> assistive-technology-access
  -> governance-rights
```

这组关系处理“主体如何避免被外部环境、制度和尾部风险截断”。

```text
mental-health-affective-stability
  -> depression-mood-disorder-functioning-continuity
  -> anxiety-stress-threat-regulation-continuity
  -> trauma-ptsd-adversity-recovery-continuity
  -> psychosis-reality-testing-community-continuity
  -> bipolar-mood-episode-stability-continuity
  -> adhd-executive-function-neurodevelopment-continuity
  -> autism-neurodiversity-support-continuity
  -> eating-disorders-nutrition-body-continuity
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
