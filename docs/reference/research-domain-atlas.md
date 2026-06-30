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
| 关键供应链可连续 | `supply-chain-continuity/` | 药品、能源、食物、设备、通信、物流 | 断供、单点故障、替代失败 |
| 生物技术双重用途可治理 | `synthetic-biology-biosecurity/` | 生物安全、生物安保、双重用途、治理 | 病原风险、误用、实验外泄 |
| 极端环境可栖居 | `space-extreme-habitation/` | 辐射、微重力、隔离、闭环生命支持 | 环境失效、资源闭环失败、远程医疗失败 |
| 关系网络可支撑主体 | `social-connection-relational-infra/` | 社会连接、孤独、照护网络、信任、协作 | 孤立、照护断裂、危机无人接住 |
| 权利和治理可保护主体 | `governance-rights/` | 同意、退出、数据权、法律身份 | 被控制、被剥夺、被系统吞噬 |
| 服务入口可理解可导航 | `health-literacy-navigation/` | 健康素养、服务导航、风险沟通、共同决策 | 有资源但不会用、误解、延误、行政排除 |
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
  -> financial-resilience-access
  -> occupational-work-design
  -> information-integrity-trust
  -> supply-chain-continuity
  -> synthetic-biology-biosecurity
  -> space-extreme-habitation
  -> social-connection-relational-infra
  -> health-literacy-navigation
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
