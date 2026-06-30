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
    ├── cognitive-augmentation/ # 认知增强与工具放大
    ├── digital-identity-security/ # 数字身份安全
    ├── disembodied-cns/   # 去具身外部维持型中枢生命系统
    ├── endocrine-hormonal-regulation/ # 内分泌与激素调节
    ├── extracellular-matrix-glycation/ # 细胞外基质与糖化
    ├── financial-resilience-access/ # 财务韧性与资源可及
    ├── fluid-electrolyte-acid-base-homeostasis/ # 体液电解质酸碱稳态
    ├── future-waiting/    # 去未来 / 压缩等待路径
    ├── healthcare-access-continuity/ # 医疗服务连续性
    ├── caregiving-long-term-care/ # 照护与长期照护
    ├── housing-built-environment-stability/ # 住房与建成环境稳定
    ├── governance-rights/ # 治理与主体权利
    ├── genomic-stability-dna-repair/ # 基因组稳定性与 DNA 修复
    ├── gastrointestinal-barrier-absorption/ # 消化屏障与吸收
    ├── blood-oxygen-hemostasis/ # 血液氧运与止血
    ├── health-literacy-navigation/ # 健康素养与服务导航
    ├── immune-maintenance/# 免疫系统维护
    ├── information-integrity-trust/ # 信息完整性与信任
    ├── legal-identity-civil-registration/ # 法律身份与民事登记
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
- `domains/healthcare-access-continuity/` 负责初级卫生保健、急诊、预防、转诊、随访、费用、质量和医疗服务连续性。
- `domains/caregiving-long-term-care/` 负责家庭照护、长期照护、居家社区支持、照护协调、照护者负担和尊严边界。
- `domains/housing-built-environment-stability/` 负责住房稳定、住房质量、室内环境、无障碍、社区资源和建成环境健康。
- `domains/transportation-access-mobility/` 负责公共交通、无障碍交通、出行时间、医疗交通、交通成本和外部资源可达性。
- `domains/legal-identity-civil-registration/` 负责法律身份、出生登记、民事登记、生命统计、身份文件、身份覆盖和服务资格。
- `domains/emergency-preparedness-response/` 负责灾害准备、预警、应急通信、急救医疗、安置、公共卫生应急和灾后恢复。
- `domains/cellular-reprogramming/` 负责山中因子、部分重编程、化学重编程、AI 因子设计和表观遗传编辑等细胞状态可重写谱系，不提供实验协议或人体应用建议。
- `domains/regenerative-medicine/` 负责干细胞、组织工程、器官再生、类器官、移植和生物制造的高层研究框架。
- `domains/rehabilitation-functioning/` 负责康复、功能恢复、失能预防、活动能力、自理、沟通和社会参与。
- `domains/cancer-control/` 负责癌症预防、早筛、治疗、复发、肿瘤演化和长期风险治理。
- `domains/immune-maintenance/` 负责免疫衰老、感染防御、慢性炎症、自身免疫和免疫监视。
- `domains/antimicrobial-resilience/` 负责抗微生物耐药、感染控制和现代医学抗感染底座。
- `domains/neuro-continuity/` 负责大脑、记忆、意识、人格和主体身份连续性。
- `domains/sensory-continuity/` 负责视觉、听觉、平衡、触觉和感官反馈连续性。
- `domains/future-waiting/` 负责度规红移固有时差分路径（黑洞等待室）等“压缩等待 / 去未来”思想实验、证据边界和风险约束。
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
- `domains/oral-health-continuity/` 负责口腔健康、牙齿、牙周、咀嚼、疼痛、感染、营养和沟通连续性。
- `domains/measurement-feedback/` 负责主体状态测量、风险评分、生物标志物、可穿戴、预测模型和反馈闭环。
- 原始资料归档在 `docs/source-notes/`；稳定结论必须沉淀到 `docs/` 或对应子域 README，不能长期依赖零散临时文件名。

## 设计原则

- Human Infra 的上位对象是“人类任务执行系统”，不是单一长寿产品。
- Longevity Evidence 承接原 Biocat，但不再占据根目录概念中心。
- “永生”的不同路径必须按机制拆分：长寿证据、营养代谢、基因组稳定性、端粒维护、蛋白稳态、自噬、线粒体、细胞衰老、细胞外基质与糖化、微生物生态、干细胞储备、肝肾清除、消化屏障与吸收、呼吸氧合、血液氧运与止血、内分泌激素调节、淋巴与脑淋巴清除、体液电解质酸碱稳态、热稳态、身体活动、心血管韧性、肌骨完整性、皮肤屏障与伤口愈合、泌尿生殖连续性、生殖与生育连续性、注意力与执行控制、学习与技能获得、时间分配与有效时间、财务韧性、职业与工作设计、信息完整性与信任、医疗服务连续性、照护与长期照护、住房与建成环境、交通接入、法律身份与民事登记、应急准备与响应、细胞重编程、再生医学、康复功能、癌症控制、免疫维护、抗微生物韧性、神经连续性、感官连续性、未来等待、生物停滞、去具身中枢、记忆编辑、认知增强、AI 代理安全、数字身份安全、心理稳定、睡眠恢复、辅助技术、社会连接、物质暴露控制、资源环境、供应链连续性、合成生物学与生物安全、空间极端栖居、风险工程、健康素养导航、治理权利、口腔健康、痛苦控制和测量反馈不能混成一个概念桶。
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

- 2026-06-20：从 Biocat 单项目重组为 Human Infra 总项目；旧 Biocat 迁入 `domains/longevity-evidence/`；新增 `disembodied-cns` 与 `memory-editing` 子域；四份最新资料归档到 `docs/source-notes/`；按 Docs-as-Code 和 Diataxis 补齐根文件、协作模板、文档分层和结构检查脚本。
- 2026-06-22：新增 `domains/future-waiting/` 和度规红移固有时差分路径（黑洞等待室），用于承载“压缩等待 / 去未来”类永生路径思想实验。
- 2026-06-23：新增 GitHub Actions `make check` 门禁和 `.github/AGENTS.md`，准备远程仓库协作入口。
- 2026-06-26：新增根目录静态 Web 看板 `human-infra-dashboard.html`，采用黄金分割三块布局展示主体持续性与生命路径预测模型。
- 2026-06-26：新增专项 Web 展示页 `singularity-human-infra.html`，将《奇点更近》学习资料转译为 Human Infra 价值展示、预测模型和可视化。
- 2026-06-26：新增 `web/` Observable Framework 应用，作为科研叙事、书籍转译、预测模型和交互图表的正式 Web 入口。
- 2026-06-27：新增 `tools/arxiv_html_paper_tool.py` 与 `tools/arxiv-html-paper/`，把 arXiv HTML papers 前端框架沉淀为可复用 Astro 工具链。
- 2026-06-29：新增可控度规等待室假设 working paper 入口和审计账本，把黑洞等待室收敛为固有时差分、退出采用、风险扣减和递归等待的可审查模型。
- 2026-06-30：新增 `domains/cellular-reprogramming/`，承载山中因子、部分重编程、化学重编程、AI 因子设计和表观遗传编辑的机制谱系与安全边界。
- 2026-06-30：新增 `docs/reference/research-domain-atlas.md` 和 10 个研究域骨架，把有效永生的先验条件映射为可独立维护的研究域。
- 2026-06-30：新增第二波 8 个研究域骨架，覆盖康复功能、心理稳定、睡眠恢复、辅助技术、抗微生物韧性、环境底座、感官连续性和痛苦控制。
- 2026-06-30：新增第三波 8 个研究域骨架，覆盖营养代谢、身体活动、心血管韧性、肌骨完整性、社会连接、物质暴露控制、健康素养导航和口腔健康连续性。
- 2026-06-30：新增第四波 8 个分子维护研究域骨架，覆盖基因组稳定性、端粒维护、蛋白稳态、自噬、线粒体生物能量学、细胞衰老清除、微生物生态、干细胞储备和肝肾清除。
- 2026-06-30：新增第五波 5 个外部技术风险域骨架，覆盖数字身份安全、AI 代理安全、供应链连续性、合成生物学与生物安全、空间与极端栖居。
- 2026-06-30：新增第六波 6 个生理与结构维护域骨架，覆盖呼吸氧合、内分泌激素调节、血液氧运与止血、皮肤屏障与伤口愈合、细胞外基质与糖化、淋巴与脑淋巴清除。
- 2026-06-30：新增第七波 5 个基础稳态与未来选择权域骨架，覆盖消化屏障与吸收、体液电解质酸碱稳态、热稳态、泌尿生殖连续性、生殖与生育连续性。
- 2026-06-30：新增第八波 6 个主体代理与任务资源域骨架，覆盖注意力与执行控制、学习与技能获得、时间分配与有效时间、财务韧性、职业与工作设计、信息完整性与信任。
- 2026-06-30：新增第九波 6 个服务接入与生活连续性域骨架，覆盖医疗服务连续性、照护与长期照护、住房与建成环境、交通接入、法律身份与民事登记、应急准备与响应。
