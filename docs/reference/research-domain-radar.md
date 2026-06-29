# Research Domain Radar

Research Domain Radar 记录尚未晋升为正式 `domains/*` 的潜在研究域。它服务持续调研：先收集可能影响主体持续性的方向，再按 Research Domain Atlas 的契约判断是否晋升。

## 晋升规则

候选方向只有满足以下条件，才从 radar 晋升为正式域：

```text
有独立机制
有独立证据体系
有独立失败模式
有独立伦理边界
有独立维护价值
```

否则留在 radar 或归入已有域。

## 第一批候选域

| 候选域 | 先验条件 | 可能主变量 | 当前归属建议 | 晋升触发 |
| --- | --- | --- | --- | --- |
| `genomic-stability-dna-repair` | 主体细胞必须长期保持基因组完整性 | DNA 损伤、突变负荷、修复能力、癌前风险 | 先归入 `longevity-evidence/` 与 `cancer-control/` 交叉 | 出现足够独立的 DNA 修复干预、风险模型和证据账本 |
| `telomere-maintenance` | 复制能力和组织更新不能被端粒限制过早截断 | 端粒长度、端粒酶、癌症风险、组织再生 | 先归入 `longevity-evidence/` | 需要独立处理端粒收益与癌症风险时晋升 |
| `proteostasis-autophagy` | 蛋白错误折叠、聚集和清除能力必须长期稳定 | 蛋白稳态、自噬、溶酶体功能、神经退行风险 | 先归入 `longevity-evidence/` 与 `neuro-continuity/` | 蛋白稳态成为独立治疗和测量主线时晋升 |
| `mitochondrial-bioenergetics` | 主体行动和修复依赖细胞能源系统 | 线粒体功能、氧化压力、疲劳、肌肉和神经功能 | 先归入 `longevity-evidence/` | 有独立证据矩阵和临床终点时晋升 |
| `metabolic-nutrient-sensing` | 营养感知决定代谢状态、修复和衰老速度 | 胰岛素、mTOR、AMPK、NAD、代谢健康 | 先归入 `longevity-evidence/` | 与长寿干预证据账本分离价值足够高时晋升 |
| `cellular-senescence-clearance` | 衰老细胞积累会改变炎症和组织功能 | senescence burden、SASP、senolytics、组织功能 | 先归入 `longevity-evidence/`、`immune-maintenance/` | senolytics / senomorphics 证据与风险足够独立时晋升 |
| `microbiome-dysbiosis` | 主体免疫、代谢和炎症受微生物生态影响 | 菌群失调、炎症、代谢、免疫 | 先归入 `immune-maintenance/` | 微生物组干预成为独立证据体系时晋升 |
| `cardiovascular-resilience` | 心血管系统是长期死亡风险核心通道 | 血压、动脉粥样硬化、血栓、心衰、卒中 | 先归入 `longevity-evidence/` 与 `risk-engineering/` | 需要独立风险函数和干预谱系时晋升 |
| `renal-hepatic-clearance` | 解毒、代谢和清除能力支撑长期药物与系统稳定 | 肝肾功能、药物代谢、毒性负担 | 先归入 `longevity-evidence/` | 器官功能维护需要独立体系时晋升 |
| `reproductive-embryonic-rejuvenation` | 自然繁殖包含年龄重置线索 | 胚胎年龄归零、配子质量、代际连续性 | 先归入 `cellular-reprogramming/` | 若成为细胞年轻化理论主轴则晋升 |
| `digital-identity-security` | 主体在数字社会中必须保有身份、账户和数据入口 | 账号安全、身份盗用、恢复能力、服务入口 | 先归入 `governance-rights/` 与 `resource-social-infra/` | 数字身份成为主体持续性的独立基础设施时晋升 |
| `ai-agency-safety` | AI 工具放大主体能力，也可能替代或支配主体 | AI 代理、控制权、可解释性、偏差、失控 | 先归入 `cognitive-augmentation/` 与 `governance-rights/` | AI 代理成为独立行动层时晋升 |
| `space-extreme-habitation` | 主体可能需要跨越极端环境和地外生存风险 | 辐射、微重力、隔离、闭环生命支持、任务风险 | 先归入 `risk-engineering/` 与 `resource-social-infra/` | 空间栖居、极端环境或闭环生态成为独立路线时晋升 |
| `supply-chain-continuity` | 药物、能源、食物和设备断供会截断主体持续性 | 供应链、库存、替代、断供风险 | 先归入 `resource-social-infra/` | 需要独立建模关键物资连续性时晋升 |
| `synthetic-biology-biosecurity` | 生物技术既能修复主体，也能制造新型风险 | 合成生物学、病原体风险、双重用途、治理 | 先归入 `risk-engineering/` 与 `governance-rights/` | 双重用途治理成为独立研究主线时晋升 |

## 已从 Radar 晋升的方向

| 晋升域 | 晋升理由 |
| --- | --- |
| `rehabilitation-functioning/` | 功能恢复、失能预防和社会参与具有独立变量、证据体系和失败模式 |
| `mental-health-affective-stability/` | 心理稳定、动机、成瘾、创伤和自杀风险能直接截断主体行动 |
| `sleep-circadian-recovery/` | 睡眠和昼夜节律是恢复系统的基础调度器 |
| `assistive-technology-access/` | 辅助技术把损伤从终止条件转化为可补偿条件，并具有独立可及性问题 |
| `antimicrobial-resilience/` | 抗感染能力是手术、移植、癌症治疗和长期医学体系的底座 |
| `planetary-health-environment/` | 空气、水、气候、污染和生态系统是主体持续性的上游环境条件 |
| `sensory-continuity/` | 感官系统是主体感知、沟通、行动和反馈闭环的基础 |
| `pain-suffering-control/` | 持续存在必须同时审查痛苦、可承受性、尊严和有效时间质量 |

## 来源信号

| 来源 | 对域雷达的启发 |
| --- | --- |
| Hallmarks of Aging: An Expanding Universe | 提示基因组稳定性、端粒、蛋白稳态、自噬、营养感知、线粒体、细胞衰老、干细胞耗竭、细胞通讯、慢性炎症和菌群失调等候选机制 |
| WHO Social Determinants of Health | 提示资源、权力、生活环境、工作、社会条件对健康和持续性的基础作用 |
| Healthy People 2030 SDOH framework | 提示经济稳定、教育、医疗可及、社区环境、社会与社区情境可作为资源基础设施维度 |
| NIST AI Risk Management Framework | 提示 AI 系统需要从 govern、map、measure、manage 进入主体权利和认知增强治理 |
| NASA Human Research Program | 提示极端环境、空间飞行、辐射、隔离、医疗支持和人因风险可作为未来主体持续性场景 |
| WHO Rehabilitation 2030 | 提示康复和功能恢复是健康系统核心组成，不只是医疗后处理 |
| WHO Assistive Technology | 提示辅助技术可及性是功能持续和社会参与的关键基础设施 |
| WHO Antimicrobial Resistance | 提示耐药性会侵蚀现代医学和长期感染控制底座 |
| WHO Vision and Hearing resources | 提示感官系统是主体感知、沟通和行动连续性的基础 |
| CDC Sleep / NHLBI Sleep resources | 提示睡眠不足和节律失调会影响认知、慢病、心理和恢复能力 |
| WHO Mental Health / Suicide resources | 提示心理健康、自杀风险和社会连接是主体持续行动的核心条件 |
| CDC Chronic Pain / WHO Palliative Care | 提示疼痛、症状负担和姑息照护决定持续存在的可承受性 |

Source links:

- https://pubmed.ncbi.nlm.nih.gov/36599349/
- https://www.who.int/health-topics/social-determinants-of-health
- https://odphp.health.gov/healthypeople/priority-areas/social-determinants-health
- https://www.nist.gov/itl/ai-risk-management-framework
- https://www.nasa.gov/hrp/
- https://www.who.int/initiatives/rehabilitation-2030
- https://www.who.int/health-topics/assistive-technology
- https://www.who.int/news-room/fact-sheets/detail/antimicrobial-resistance
- https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment
- https://www.who.int/news-room/fact-sheets/detail/deafness-and-hearing-loss
- https://www.cdc.gov/sleep/
- https://www.who.int/health-topics/mental-health
- https://www.cdc.gov/chronic-pain/
- https://www.who.int/news-room/fact-sheets/detail/palliative-care

## 使用规则

- Radar 不是正式域清单，不代表这些方向已经成熟。
- 每轮新增正式域前，先检查 radar 是否已有候选、是否满足晋升规则。
- 如果候选域只是在已有域中提供一个变量，就不要晋升。
- 如果候选域有独立证据、失败模式和伦理边界，再新增目录、ADR 和门禁。
